"""Test doubles. Unit and pipeline tests must never touch a real provider or store."""

from typing import Any

from pydantic import BaseModel

from taskflow.domain.models import Chunk, LLMCall, ScoredChunk


class FakeLLMProvider:
    """Returns canned structured responses. Configure per purpose, or raise on demand."""

    name = "fake"

    def __init__(
        self, responses: dict[str, BaseModel] | None = None, raises: Exception | None = None
    ):
        self._responses = responses or {}
        self._raises = raises
        self.calls: list[dict[str, Any]] = []

    async def complete_structured(self, *, purpose, system, user, schema, model="fake-model"):
        self.calls.append({"purpose": purpose, "user": user, "model": model})
        if self._raises:
            raise self._raises
        return self._responses[purpose], LLMCall(
            purpose=purpose,
            provider=self.name,
            model=model,
            prompt_tokens=100,
            completion_tokens=200,
            cost_usd=0.0,
            latency_ms=1,
        )

    async def health(self) -> bool:
        return self._raises is None


class FakeVectorStore:
    """Returns a fixed chunk list so retrieval quality never varies inside a unit test."""

    def __init__(self, chunks: list[Chunk] | None = None, scores: list[float] | None = None):
        self._chunks = chunks or []
        self._scores = scores or [0.9] * len(self._chunks)

    async def hybrid_search(self, query, *, k=20, filters=None) -> list[ScoredChunk]:
        return [
            ScoredChunk(chunk=c, rrf_score=s, rerank_score=s)
            for c, s in zip(self._chunks, self._scores, strict=False)
        ][:k]

    async def count(self) -> int:
        return len(self._chunks)

    async def health(self) -> bool:
        return True
