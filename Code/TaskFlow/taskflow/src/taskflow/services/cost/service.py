"""Cost tracking service.

Calculates token usage cost in USD per completion call based on provider pricing
configured in config/providers.yaml.
"""

from taskflow.config.settings import providers_config
from taskflow.domain.models import LLMCall


def calculate_cost(
    provider: str,
    prompt_tokens: int,
    completion_tokens: int,
) -> float:
    """Calculate token usage cost in USD."""
    cfg = providers_config()
    provider_cfg = cfg.get("providers", {}).get(provider, {})
    pricing = provider_cfg.get("pricing", {})

    in_rate = float(pricing.get("in_per_1k", 0.0))
    out_rate = float(pricing.get("out_per_1k", 0.0))

    cost_in = (prompt_tokens / 1000.0) * in_rate
    cost_out = (completion_tokens / 1000.0) * out_rate
    return round(cost_in + cost_out, 6)


def total_trace_cost(calls: list[LLMCall]) -> float:
    """Calculate total USD cost for all LLM calls in a trace."""
    return round(sum(c.cost_usd for c in calls), 6)
