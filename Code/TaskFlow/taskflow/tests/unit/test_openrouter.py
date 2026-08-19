"""Unit tests for Phase P10 OpenRouter Provider Adapter."""

import pytest

from taskflow.adapters.llm.openrouter import OpenRouterProvider
from taskflow.domain.errors import ProviderError


@pytest.mark.asyncio
async def test_openrouter_health_unconfigured():
    """OpenRouter health returns False when API key is missing."""
    provider = OpenRouterProvider(api_key="")
    assert not await provider.health()


@pytest.mark.asyncio
async def test_openrouter_complete_missing_key():
    """OpenRouter throws ProviderError when API key is missing."""
    provider = OpenRouterProvider(api_key="")
    with pytest.raises(ProviderError) as exc_info:
        await provider.complete(system="sys", user="user", model="openai/gpt-4o-mini")
    assert "OPENROUTER_API_KEY missing" in str(exc_info.value)
