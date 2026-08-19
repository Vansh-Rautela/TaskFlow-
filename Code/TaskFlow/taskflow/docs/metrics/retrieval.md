# Retrieval Metrics — Phase P5

- **Queries Evaluated:** 70
- **Recall@5:** 28.57%
- **MRR@10:** 0.2857
- **Retrieval Gap Rate:** 0.00%
- **Average Latency:** 39.1 ms

## Evaluation Configuration
- **Vector Store:** Embedded Qdrant (`taskflow_kb`)
- **Query Processing:** Normalization + Alias Expansion (`query_builder.py`)
- **Fusion:** Dense (`bge-small-en-v1.5`) + Sparse (`bm25`) RRF Fusion
