"""Qdrant embedded vector store adapter.

Handles FastEmbed locally for both dense (cosine) and sparse (bm25/idf) embeddings.
Implements the VectorStore interface.
"""

import uuid

from fastembed import SparseTextEmbedding, TextEmbedding
from qdrant_client import QdrantClient, models

from taskflow.config.settings import settings
from taskflow.domain.models import Chunk, RetrievalResult, ScoredChunk
from taskflow.services.retrieve.chunking import DocumentChunk

# A deterministic namespace for UUID5 generation so identical chunk_ids get identical uuids
NAMESPACE_TASKFLOW = uuid.UUID("f0e1d2c3-b4a5-9687-7869-5a4b3c2d1e0f")


class QdrantVectorStore:
    def __init__(self, collection_name: str | None = None, location: str | None = None) -> None:
        if location:
            self.client = QdrantClient(location=location)
        else:
            self.client = QdrantClient(path=settings().qdrant_path)

        self.collection_name = collection_name or settings().qdrant_collection

        # Initialize local FastEmbed models
        self.dense_model = TextEmbedding("BAAI/bge-small-en-v1.5")
        self.sparse_model = SparseTextEmbedding("Qdrant/bm25")

    def setup_collection(self) -> None:
        """Create the collection and index payloads idempotently."""
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config={
                    "dense": models.VectorParams(size=384, distance=models.Distance.COSINE)
                },
                sparse_vectors_config={
                    "bm25": models.SparseVectorParams(modifier=models.Modifier.IDF)
                },
            )

        # Create payload indexes to filter explicitly
        for field in ["tenant_id", "doc_type", "product_tier", "intents", "doc_id"]:
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name=field,
                field_schema=models.PayloadSchemaType.KEYWORD,
            )

    def ingest(self, chunks: list[DocumentChunk], tenant_id: str) -> None:
        """Embed and ingest chunks natively via FastEmbed into Qdrant."""
        if not chunks:
            return

        texts = [c.text for c in chunks]
        dense_embeddings = list(self.dense_model.embed(texts))
        sparse_embeddings = list(self.sparse_model.embed(texts))

        points = []
        for i, c in enumerate(chunks):
            point_id = str(uuid.uuid5(NAMESPACE_TASKFLOW, c.chunk_id))
            meta = {
                "chunk_id": c.chunk_id,
                "doc_id": c.doc_id,
                "title": c.title,
                "section_heading": c.section_heading,
                "tenant_id": tenant_id,
                "text": c.text,
            }
            vector = {
                "dense": dense_embeddings[i].tolist(),
                "bm25": models.SparseVector(
                    indices=sparse_embeddings[i].indices.tolist(),
                    values=sparse_embeddings[i].values.tolist(),
                ),
            }
            points.append(models.PointStruct(id=point_id, vector=vector, payload=meta))

        self.client.upsert(collection_name=self.collection_name, points=points)

    def search(self, query: str, tenant_id: str, limit: int = 5) -> RetrievalResult:
        """Perform a hybrid query (Dense + Sparse RRF)."""
        q_dense = next(iter(self.dense_model.embed([query]))).tolist()
        q_sparse = next(iter(self.sparse_model.embed([query])))

        results = self.client.query_points(
            collection_name=self.collection_name,
            prefetch=[
                models.Prefetch(
                    query=q_dense,
                    using="dense",
                    limit=20,
                    filter=models.Filter(
                        must=[
                            models.FieldCondition(
                                key="tenant_id", match=models.MatchValue(value=tenant_id)
                            )
                        ]
                    ),
                ),
                models.Prefetch(
                    query=models.SparseVector(
                        indices=q_sparse.indices.tolist(),
                        values=q_sparse.values.tolist(),
                    ),
                    using="bm25",
                    limit=20,
                    filter=models.Filter(
                        must=[
                            models.FieldCondition(
                                key="tenant_id", match=models.MatchValue(value=tenant_id)
                            )
                        ]
                    ),
                ),
            ],
            query=models.FusionQuery(fusion=models.Fusion.RRF),
            limit=limit,
        )

        chunks = []
        for point in results.points:
            payload = point.payload or {}
            chunk = Chunk(
                chunk_id=payload.get("chunk_id", "unknown"),
                doc_id=payload.get("doc_id", "unknown"),
                title=payload.get("title", ""),
                section=payload.get("section_heading"),
                text=payload.get("text", ""),
                doc_type=payload.get("doc_type", "unknown"),
                product_tier=payload.get("product_tier"),
                intents=payload.get("intents", []),
                version="1.0",
                source_path="",
                tenant_id=tenant_id,
            )
            chunks.append(
                ScoredChunk(
                    chunk=chunk,
                    rrf_score=point.score,
                )
            )

        return RetrievalResult(
            query_used=query,
            chunks=chunks,
            sufficient=len(chunks) > 0,
            latency_ms=0,
        )
