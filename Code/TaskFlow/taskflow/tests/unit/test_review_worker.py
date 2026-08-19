"""Unit tests for Phase P8 Review Service and Outbox Worker."""

from datetime import UTC, datetime, timedelta

import pytest

from taskflow.adapters.db.engine import build_engine, build_session_factory
from taskflow.adapters.db.orm import Base
from taskflow.adapters.db.repositories import SQLiteOutboxRepository, SQLiteReviewRepository
from taskflow.domain.enums import Channel, OutboxState, ReviewState, RouteAction
from taskflow.domain.models import (
    ConfidenceBreakdown,
    DraftOutput,
    OutboundMessage,
    ReviewItem,
    RoutingDecision,
)
from taskflow.services.review.service import (
    approve_review,
    edit_and_approve_review,
    list_pending_reviews,
    reject_review,
)
from taskflow.worker import run_worker_loop


@pytest.fixture
async def factory():
    engine = build_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    sf = build_session_factory(engine)
    yield sf
    await engine.dispose()


def _make_review_item(review_id: str = "rev-001") -> ReviewItem:
    now = datetime.now(UTC)
    return ReviewItem(
        review_id=review_id,
        trace_id="tr-001",
        conversation_id="conv-001",
        tenant_id="test",
        state=ReviewState.PENDING,
        draft=DraftOutput(
            response_text="Original draft response text [chunk-001].",
            citations=[{"chunk_id": "chunk-001", "doc_title": "Policy"}],
            tone="friendly",
            complexity="simple",
            draft_confidence=0.85,
        ),
        decision=RoutingDecision(
            action=RouteAction.HUMAN_REVIEW,
            reason="Confidence score below threshold",
            reason_code="low_confidence",
            confidence=ConfidenceBreakdown(
                gates=[],
                weights={},
                score=0.65,
                threshold=0.70,
            ),
        ),
        created_at=now,
        sla_deadline=now + timedelta(hours=4),
    )


@pytest.mark.asyncio
async def test_list_pending_reviews(factory):
    """Retrieve all pending review queue items."""
    review_repo = SQLiteReviewRepository(factory)
    item = _make_review_item("rev-101")
    await review_repo.create(item)

    pending = await list_pending_reviews(review_repo)
    assert len(pending) == 1
    assert pending[0].review_id == "rev-101"


@pytest.mark.asyncio
async def test_approve_review(factory):
    """Approve pending review item and enqueue outbound message into outbox."""
    review_repo = SQLiteReviewRepository(factory)
    outbox_repo = SQLiteOutboxRepository(factory)
    item = _make_review_item("rev-102")
    await review_repo.create(item)

    success = await approve_review(review_repo, outbox_repo, "rev-102", operator="agent_smith")
    assert success

    updated = await review_repo.get("rev-102")
    assert updated.state == ReviewState.APPROVED

    claimed = await outbox_repo.claim(limit=10)
    assert len(claimed) == 1
    assert "Original draft response text" in claimed[0].body_text


@pytest.mark.asyncio
async def test_edit_and_approve_review(factory):
    """Record operator edit diff and enqueue edited outbound message."""
    review_repo = SQLiteReviewRepository(factory)
    outbox_repo = SQLiteOutboxRepository(factory)
    item = _make_review_item("rev-103")
    await review_repo.create(item)

    edited_text = "Edited draft response text with custom clarification."
    success = await edit_and_approve_review(
        review_repo, outbox_repo, "rev-103", edited_text=edited_text, operator="agent_smith"
    )
    assert success

    updated = await review_repo.get("rev-103")
    assert updated.state == ReviewState.EDITED

    claimed = await outbox_repo.claim(limit=10)
    assert len(claimed) == 1
    assert claimed[0].body_text == edited_text


@pytest.mark.asyncio
async def test_optimistic_lock_collision(factory):
    """Second concurrent review transition attempt returns False."""
    review_repo = SQLiteReviewRepository(factory)
    outbox_repo = SQLiteOutboxRepository(factory)
    item = _make_review_item("rev-104")
    await review_repo.create(item)

    # First operator approves
    res1 = await approve_review(review_repo, outbox_repo, "rev-104", operator="operator_1")
    assert res1

    # Second operator attempts to reject the same item
    res2 = await reject_review(review_repo, "rev-104", operator="operator_2")
    assert not res2


@pytest.mark.asyncio
async def test_worker_process_batch(factory):
    """Worker claims queued outbox messages and delivers them."""
    outbox_repo = SQLiteOutboxRepository(factory)
    outbound = OutboundMessage(
        outbound_id="out-555",
        conversation_id="c-555",
        tenant_id="test",
        channel=Channel.EMAIL,
        recipient="user@example.com",
        subject="Re: Support",
        body_text="Your ticket has been updated.",
        reply_headers={},
        state=OutboxState.QUEUED,
        idempotency_key="idemp-555",
        retry_count=0,
    )
    await outbox_repo.enqueue(outbound)

    processed = await run_worker_loop(outbox_repo, run_once=True)
    assert processed == 1
