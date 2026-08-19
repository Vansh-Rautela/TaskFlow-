import pytest

from tests.fixtures.fakes import FakeLLMProvider, FakeVectorStore


@pytest.fixture
def fake_llm():
    return FakeLLMProvider()


@pytest.fixture
def fake_store():
    return FakeVectorStore()


@pytest.fixture
def weights():
    return {
        "citation_coverage": 0.35,
        "grounding_entailment": 0.25,
        "retrieval_relevance": 0.20,
        "intent_confidence": 0.10,
        "tone_alignment": 0.10,
    }
