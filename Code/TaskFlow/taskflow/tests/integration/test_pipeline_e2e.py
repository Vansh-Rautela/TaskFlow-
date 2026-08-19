"""Integration tests for TaskFlow end-to-end pipeline execution."""

from datetime import UTC, datetime

import pytest

from taskflow.adapters.db.engine import build_engine, build_session_factory
from taskflow.adapters.db.orm import Base
from taskflow.adapters.db.repositories import (
    SQLiteOutboxRepository,
    SQLiteReviewRepository,
    SQLiteTraceRepository,
)
from taskflow.adapters.vector.qdrant_store import QdrantVectorStore
from taskflow.domain.enums import Channel, Intent, RouteAction
from taskflow.domain.models import Citation, ClassificationOutput, DraftOutput, InboundMessage
from taskflow.pipeline.orchestrator import Deps, run_pipeline
from taskflow.services.retrieve.chunking import DocumentChunk
from tests.fixtures.fakes import FakeLLMProvider


@pytest.mark.asyncio
async def test_full_pipeline_auto_send_flow(tmp_path):
    """Test full pipeline end-to-end execution resulting in AUTO_SEND action."""
    db_path = tmp_path / "test_pipeline.db"
    engine = build_engine(f"sqlite+aiosqlite:///{db_path}")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    sf = build_session_factory(engine)
    trace_repo = SQLiteTraceRepository(sf)
    review_repo = SQLiteReviewRepository(sf)
    outbox_repo = SQLiteOutboxRepository(sf)

    fake_llm = FakeLLMProvider(
        responses={
            "classification": ClassificationOutput(
                intent=Intent.REFUND, confidence=0.95, reasoning="Clear refund request"
            ),
            "draft": DraftOutput(
                response_text="Hello, we can process your prorated refund. [KB-REFUND-006:2]",
                citations=[Citation(chunk_id="KB-REFUND-006:2", doc_title="Refund Policy")],
                tone="friendly",
                complexity="simple",
                draft_confidence=0.92,
            ),
        }
    )

    qdrant = QdrantVectorStore(location=":memory:")
    qdrant.setup_collection()
    qdrant.ingest(
        chunks=[
            DocumentChunk(
                chunk_id="KB-REFUND-006:1",
                doc_id="refund-doc",
                ordinal=0,
                title="Refund Policy Overview",
                section_heading="General Policy",
                text="We offer prorated refund credits for enterprise plans upon seat reduction.",
            ),
            DocumentChunk(
                chunk_id="KB-REFUND-006:2",
                doc_id="refund-doc",
                ordinal=1,
                title="Refund Policy Details",
                section_heading="Prorated Refunds",
                text="We issue prorated refunds for unused seat licenses on annual plans upon request.",
            ),
        ],
        tenant_id="test-tenant",
    )
    deps = Deps(
        trace_repo=trace_repo,
        llm_router=fake_llm,
        vector_store=qdrant,
        review_repo=review_repo,
        outbox_repo=outbox_repo,
    )

    msg = InboundMessage(
        message_id="msg-e2e-001",
        dedupe_key="email:prov-e2e-001",
        tenant_id="test-tenant",
        channel=Channel.EMAIL,
        sender="customer@acme.com",
        subject="Refund Request",
        body_text="Hi, I would like a prorated refund for 3 unused seats on my account.",
        body_redacted="Hi, I would like a prorated refund for 3 unused seats on my account.",
        provider_message_id="prov-e2e-001",
        received_at=datetime.now(UTC),
    )

    decision = await run_pipeline(msg, deps)

    assert decision.action == RouteAction.AUTO_SEND
    assert decision.confidence is not None
    assert decision.confidence.score >= 0.70

    # Verify trace persisted
    traces = await trace_repo.recent(limit=10)
    assert len(traces) == 1
    assert traces[0].intent == Intent.REFUND

    # Verify outbound message enqueued
    claimed = await outbox_repo.claim(limit=10)
    assert len(claimed) == 1
    assert claimed[0].recipient == "customer@acme.com"

    await engine.dispose()


@pytest.mark.asyncio
async def test_full_pipeline_human_review_flow(tmp_path):
    """Test full pipeline execution for billing complaint resulting in HUMAN_REVIEW."""
    db_path = tmp_path / "test_pipeline_review.db"
    engine = build_engine(f"sqlite+aiosqlite:///{db_path}")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    sf = build_session_factory(engine)
    trace_repo = SQLiteTraceRepository(sf)
    review_repo = SQLiteReviewRepository(sf)
    outbox_repo = SQLiteOutboxRepository(sf)

    fake_llm = FakeLLMProvider(
        responses={
            "classification": ClassificationOutput(
                intent=Intent.COMPLAINT, confidence=0.98, reasoning="Customer threat"
            ),
            "draft": DraftOutput(
                response_text="We apologize for the issue. [KB-BILLING-001:1]",
                citations=[Citation(chunk_id="KB-BILLING-001:1", doc_title="Billing Policy")],
                tone="apologetic",
                complexity="simple",
                draft_confidence=0.85,
            ),
        }
    )

    qdrant = QdrantVectorStore(location=":memory:")
    qdrant.setup_collection()
    deps = Deps(
        trace_repo=trace_repo,
        llm_router=fake_llm,
        vector_store=qdrant,
        review_repo=review_repo,
        outbox_repo=outbox_repo,
    )

    msg = InboundMessage(
        message_id="msg-e2e-002",
        dedupe_key="email:prov-e2e-002",
        tenant_id="test-tenant",
        channel=Channel.EMAIL,
        sender="angry@acme.com",
        subject="URGENT COMPLAINT",
        body_text="Your system double charged my credit card 4111222233334444! Fix this!",
        body_redacted="Your system double charged my credit card 4111222233334444! Fix this!",
        provider_message_id="prov-e2e-002",
        received_at=datetime.now(UTC),
    )

    decision = await run_pipeline(msg, deps)

    assert decision.action == RouteAction.HUMAN_REVIEW

    # Verify review item created with customer sender
    pending = await review_repo.pending()
    assert len(pending) == 1
    assert pending[0].sender_email == "angry@acme.com"

    await engine.dispose()
