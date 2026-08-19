"""Vector store port definition."""

from typing import Protocol

from taskflow.domain.models import RetrievalResult
from taskflow.services.retrieve.chunking import DocumentChunk


class VectorStore(Protocol):
    """Protocol for vector store adapters. Services depend on this."""

    def setup_collection(self) -> None: ...

    def ingest(self, chunks: list[DocumentChunk], tenant_id: str) -> None: ...

    def search(self, query: str, tenant_id: str, limit: int = 5) -> RetrievalResult: ...
