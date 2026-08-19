"""Unit tests for Phase P9 FastAPI REST API endpoints."""

from datetime import UTC, datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from taskflow.adapters.db.engine import build_engine, build_session_factory
from taskflow.adapters.db.orm import Base
from taskflow.adapters.db.repositories import (
    SQLiteOutboxRepository,
    SQLiteReviewRepository,
    SQLiteTraceRepository,
)
from taskflow.adapters.vector.qdrant_store import QdrantVectorStore
from taskflow.api.app import app, deps_container
from taskflow.domain.enums import ReviewState, RouteAction
from taskflow.domain.models import (
    ConfidenceBreakdown,
    DraftOutput,
    ReviewItem,
    RoutingDecision,
)
from taskflow.pipeline.orchestrator import Deps
from tests.unit.test_providers import MockSuccessProvider


@pytest.fixture
async def api_deps():
    engine = build_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    factory = build_session_factory(engine)
    trace_repo = SQLiteTraceRepository(factory)
    review_repo = SQLiteReviewRepository(factory)
    outbox_repo = SQLiteOutboxRepository(factory)

    mock_p = MockSuccessProvider()
    from taskflow.adapters.llm.router import ProviderRouter

    router = ProviderRouter(providers={"claude": mock_p, "ollama": mock_p})
    vector_store = QdrantVectorStore(location=":memory:")
    vector_store.setup_collection()

    deps = Deps(
        trace_repo=trace_repo,
        llm_router=router,
        vector_store=vector_store,
    )

    deps_container["deps"] = deps
    deps_container["trace_repo"] = trace_repo
    deps_container["review_repo"] = review_repo
    deps_container["outbox_repo"] = outbox_repo
    deps_container["engine"] = engine

    yield deps

    await engine.dispose()


def test_healthz_endpoint():
    """Health check endpoint returns 200 OK."""
    client = TestClient(app)
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.asyncio
async def test_ingest_message_api(api_deps):
    """POST /messages ingests inbound message and returns routing decision."""
    client = TestClient(app)
    payload = {
        "message_id": "api-msg-001",
        "tenant_id": "test-tenant",
        "channel": "console",
        "sender": "user@example.com",
        "subject": "Need help with API error",
        "body_text": "API returning 500 internal server error",
    }
    response = client.post("/messages", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["message_id"] == "api-msg-001"
    assert "action" in data


@pytest.mark.asyncio
async def test_list_traces_api(api_deps):
    """GET /traces returns recent execution traces."""
    client = TestClient(app)
    response = client.get("/traces")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_list_and_approve_review_api(api_deps):
    """GET /reviews returns pending items and POST /reviews/{id}/approve approves."""
    client = TestClient(app)
    review_repo = deps_container["review_repo"]

    now = datetime.now(UTC)
    item = ReviewItem(
        review_id="rev-api-1",
        trace_id="tr-api-1",
        conversation_id="c-api-1",
        tenant_id="test",
        state=ReviewState.PENDING,
        draft=DraftOutput(
            response_text="Draft text [chunk-001].",
            citations=[],
            tone="friendly",
            complexity="simple",
            draft_confidence=0.8,
        ),
        decision=RoutingDecision(
            action=RouteAction.HUMAN_REVIEW,
            reason="Low confidence",
            reason_code="low_confidence",
            confidence=ConfidenceBreakdown(gates=[], weights={}, score=0.6, threshold=0.7),
        ),
        created_at=now,
        sla_deadline=now + timedelta(hours=4),
    )
    await review_repo.create(item)

    # Test list reviews endpoint
    list_resp = client.get("/reviews")
    assert list_resp.status_code == 200
    items = list_resp.json()
    assert len(items) == 1
    assert items[0]["review_id"] == "rev-api-1"

    # Test approve review endpoint
    appr_resp = client.post(
        "/reviews/rev-api-1/approve", json={"operator": "admin", "reason": "looks good"}
    )
    assert appr_resp.status_code == 200
    assert appr_resp.json()["status"] == "approved"


@pytest.mark.asyncio
async def test_metrics_api(api_deps):
    """GET /metrics returns system performance & cost summary."""
    client = TestClient(app)
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "total_traces" in data
    assert "auto_send_rate_pct" in data
