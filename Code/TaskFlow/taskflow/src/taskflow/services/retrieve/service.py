"""Production retrieval service for Phase P5.

Uses VectorStore port with dense + sparse RRF hybrid search, query expansion,
sufficiency gating, and context injection detection.
"""

import time

from taskflow.domain.models import RetrievalResult
from taskflow.ports.vector_store import VectorStore
from taskflow.services.retrieve.injection import detect_context_injection
from taskflow.services.retrieve.query_builder import build_query
from taskflow.services.retrieve.sufficiency import evaluate_sufficiency


async def retrieve_context(
    query: str, tenant_id: str, vector_store: VectorStore | None = None
) -> RetrievalResult:
    """Execute hybrid retrieval over VectorStore port and return enriched RetrievalResult."""
    if vector_store is None:
        raise ValueError("vector_store instance required for retrieval service")

    start_ns = time.perf_counter_ns()
    expanded_query = build_query(query)

    result = vector_store.search(query=expanded_query, tenant_id=tenant_id, limit=5)
    elapsed_ms = (time.perf_counter_ns() - start_ns) // 1_000_000

    sufficient, gap_reason, top_score, support_count = evaluate_sufficiency(result.chunks)
    suspicious = detect_context_injection(result.chunks)

    return RetrievalResult(
        query_used=expanded_query,
        chunks=result.chunks,
        sufficient=sufficient,
        gap_reason=gap_reason,
        suspicious_context=suspicious,
        latency_ms=elapsed_ms,
        top_score=top_score,
        support_count=support_count,
    )
