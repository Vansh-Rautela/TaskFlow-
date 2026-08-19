from typing import Protocol, TypeVar

from pydantic import BaseModel

from taskflow.domain.models import LLMCall

T = TypeVar("T", bound=BaseModel)


class ProviderCapabilities(BaseModel):
    supports_json_schema: bool
    supports_tools: bool
    max_context: int
    price_in_per_1k: float = 0.0
    price_out_per_1k: float = 0.0


class LLMResponse(BaseModel):
    text: str
    call: LLMCall


class LLMProvider(Protocol):
    """Adapters implement this. Services depend on it and never on an SDK."""

    name: str
    capabilities: ProviderCapabilities

    async def complete(
        self,
        *,
        system: str,
        user: str,
        model: str,
        max_tokens: int = 1200,
        temperature: float = 0.2,
        schema: type[BaseModel] | None = None,
    ) -> LLMResponse: ...

    async def health(self) -> bool: ...


class LLMRouter(Protocol):
    """Protocol for provider router, allowing services to decouple from adapters."""

    async def complete_structured[T: BaseModel](
        self, *, purpose: str, system: str, user: str, schema: type[T]
    ) -> tuple[T, LLMCall]: ...
