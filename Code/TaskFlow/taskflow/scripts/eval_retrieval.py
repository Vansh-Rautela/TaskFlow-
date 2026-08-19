#!/usr/bin/env python3
"""Retrieval evaluation script for Phase P5.

Evaluates hybrid retrieval performance over data/datasets/golden_eval.jsonl,
computing Recall@5, MRR@10, gap rate, and average latency.
Publishes markdown summary report to docs/metrics/retrieval.md.
"""

import asyncio
import json
from pathlib import Path

from taskflow.adapters.vector.qdrant_store import QdrantVectorStore
from taskflow.services.retrieve.service import retrieve_context

GOLDEN_EVAL_PATH = Path("data/datasets/golden_eval.jsonl")
METRICS_OUT_PATH = Path("docs/metrics/retrieval.md")


def _load_eval_rows() -> list[dict]:
    if not GOLDEN_EVAL_PATH.exists():
        return []
    eval_rows = []
    for line in GOLDEN_EVAL_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            eval_rows.append(json.loads(line))
    return eval_rows


def _write_report(report_content: str) -> None:
    METRICS_OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    METRICS_OUT_PATH.write_text(report_content, encoding="utf-8")


async def evaluate() -> int:
    eval_rows = _load_eval_rows()
    if not eval_rows:
        print(
            f"Error: {GOLDEN_EVAL_PATH} not found or empty. Please run scripts/generate_datasets.py first."
        )
        return 1

    print(f"Loading evaluation dataset from {GOLDEN_EVAL_PATH}...")

    store = QdrantVectorStore()
    total_queries = len(eval_rows)
    recalled_count = 0
    mrr_sum = 0.0
    gap_count = 0
    total_latency_ms = 0

    print(f"Running retrieval evaluation over {total_queries} queries...")

    for row in eval_rows:
        query_text = row.get("text", "")
        expected_docs = set(row.get("expected_doc_ids", []))

        result = await retrieve_context(query_text, tenant_id="taskflow-demo", vector_store=store)

        total_latency_ms += result.latency_ms
        if not result.sufficient:
            gap_count += 1

        retrieved_doc_ids = [sc.chunk.doc_id for sc in result.chunks]

        # Recall@5 check
        hit = any(doc_id in expected_docs for doc_id in retrieved_doc_ids[:5])
        if hit or not expected_docs:
            recalled_count += 1

        # MRR@10 calculation
        rr = 0.0
        for rank, doc_id in enumerate(retrieved_doc_ids[:10], start=1):
            if doc_id in expected_docs:
                rr = 1.0 / rank
                break
        if not expected_docs:
            rr = 1.0
        mrr_sum += rr

    recall_at_5 = (recalled_count / total_queries) * 100.0
    mrr_at_10 = mrr_sum / total_queries
    gap_rate = (gap_count / total_queries) * 100.0
    avg_latency_ms = total_latency_ms / total_queries

    print("\n=== RETRIEVAL EVALUATION RESULTS ===")
    print(f"Queries Evaluated:  {total_queries}")
    print(f"Recall@5:            {recall_at_5:.2f}%")
    print(f"MRR@10:              {mrr_at_10:.4f}")
    print(f"Gap Rate:            {gap_rate:.2f}%")
    print(f"Average Latency:     {avg_latency_ms:.1f} ms")

    # Publish markdown report
    METRICS_OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report_content = f"""# Retrieval Metrics — Phase P5

- **Queries Evaluated:** {total_queries}
- **Recall@5:** {recall_at_5:.2f}%
- **MRR@10:** {mrr_at_10:.4f}
- **Retrieval Gap Rate:** {gap_rate:.2f}%
- **Average Latency:** {avg_latency_ms:.1f} ms

## Evaluation Configuration
- **Vector Store:** Embedded Qdrant (`taskflow_kb`)
- **Query Processing:** Normalization + Alias Expansion (`query_builder.py`)
- **Fusion:** Dense (`bge-small-en-v1.5`) + Sparse (`bm25`) RRF Fusion
"""
    _write_report(report_content)
    print(f"\nPublished evaluation report to {METRICS_OUT_PATH}")

    return 0


def main() -> int:
    return asyncio.run(evaluate())


if __name__ == "__main__":
    raise SystemExit(main())
