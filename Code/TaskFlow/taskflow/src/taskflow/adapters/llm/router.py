"""Provider Router implementation for Phase P4.

Routes structured LLM requests through prioritized providers with automatic failover,
schema validation, cost tracking, and offline mode support.
"""

import structlog
from pydantic import BaseModel, ValidationError

from taskflow.adapters.llm.claude import ClaudeProvider
from taskflow.adapters.llm.ollama import OllamaProvider
from taskflow.adapters.llm.openrouter import OpenRouterProvider
from taskflow.config.settings import model_for, provider_priority, settings
from taskflow.domain.errors import AllProvidersFailed, ProviderError, SchemaError, TransientError
from taskflow.domain.models import LLMCall
from taskflow.ports.llm import LLMProvider, LLMRouter

logger = structlog.get_logger()


class ProviderRouter(LLMRouter):
    """Priority-based failover LLM router implementing ports.llm.LLMRouter."""

    def __init__(self, providers: dict[str, LLMProvider] | None = None) -> None:
        if providers is not None:
            self._providers = providers
        else:
            self._providers = {
                "openrouter": OpenRouterProvider(),
                "claude": ClaudeProvider(),
                "ollama": OllamaProvider(),
            }

    async def complete_structured[T: BaseModel](
        self, *, purpose: str, system: str, user: str, schema: type[T]
    ) -> tuple[T, LLMCall]:
        """Attempt completion using priority order until one succeeds or all fail."""
        priority = provider_priority()
        mode = settings().taskflow_llm_mode

        logger.info(
            "router_structured_complete_start", purpose=purpose, mode=mode, priority=priority
        )

        attempts = 0
        last_error: Exception | None = None

        for provider_name in priority:
            provider = self._providers.get(provider_name)
            if not provider:
                logger.warning("provider_not_found", provider=provider_name)
                continue

            attempts += 1
            model_name = model_for(provider_name, purpose)

            try:
                response = await provider.complete(
                    system=system,
                    user=user,
                    model=model_name,
                    schema=schema,
                )

                # Parse and validate structured output against target schema
                try:
                    if isinstance(response.text, str):
                        parsed_obj = schema.model_validate_json(response.text)
                    else:
                        parsed_obj = schema.model_validate(response.text)
                except ValidationError as val_err:
                    raise SchemaError(
                        f"Output from provider {provider_name} failed schema validation: {val_err}"
                    ) from val_err

                call_record = LLMCall(
                    purpose=purpose,
                    provider=provider_name,
                    model=model_name,
                    prompt_tokens=response.call.prompt_tokens,
                    completion_tokens=response.call.completion_tokens,
                    cost_usd=response.call.cost_usd,
                    latency_ms=response.call.latency_ms,
                    attempts=attempts,
                    failed_over=(attempts > 1),
                )

                logger.info(
                    "router_complete_success",
                    provider=provider_name,
                    model=model_name,
                    cost_usd=call_record.cost_usd,
                    attempts=attempts,
                )
                return parsed_obj, call_record

            except (ProviderError, SchemaError, TransientError, TimeoutError) as err:
                logger.warning(
                    "provider_attempt_failed",
                    provider=provider_name,
                    error=str(err),
                    attempt=attempts,
                )
                last_error = err
                continue
            except Exception as err:
                logger.warning(
                    "provider_attempt_unexpected_failure",
                    provider=provider_name,
                    error=str(err),
                    attempt=attempts,
                )
                last_error = err
                continue

        raise AllProvidersFailed(
            f"All providers failed for mode '{mode}'. Last error: {last_error}"
        ) from last_error
