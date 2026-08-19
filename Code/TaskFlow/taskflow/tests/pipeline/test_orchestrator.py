"""Pipeline end-to-end unit tests using mocks for LLM and Retrieval.

These prove that given a message, the orchestrator invokes all the appropriate stages,
assembles the pipeline state correctly, and delegates to the decision engine.
"""

from datetime import UTC, datetime

import pytest

from taskflow.adapters.db.engine import build_engine, build_session_factory
from taskflow.adapters.db.orm import Base
from taskflow.adapters.db.repositories import SQLiteTraceRepository
from taskflow.adapters.llm.router import ProviderRouter
from taskflow.domain.enums import Channel, RouteAction
from taskflow.domain.models import InboundMessage
from taskflow.pipeline.orchestrator import Deps, run_pipeline
from tests.unit.test_providers import MockSuccessProvider
from tests.unit.test_retrieval import MockVectorStore


def _utcnow() -> datetime:
    return datetime.now(UTC)


@pytest.fixture
async def deps(tmp_path):
    url = f"sqlite+aiosqlite:///{tmp_path}/pipeline_test.db"
    engine = build_engine(url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    factory = build_session_factory(engine)
    trace_repo = SQLiteTraceRepository(factory)
    mock_provider = MockSuccessProvider()
    llm_router = ProviderRouter(providers={"claude": mock_provider, "ollama": mock_provider})
    vector_store = MockVectorStore()

    deps = Deps(trace_repo=trace_repo, llm_router=llm_router, vector_store=vector_store)
    yield deps

    await engine.dispose()


@pytest.mark.asyncio
async def test_clean_draft_auto_sends(deps):
    """The happy path: orchestrator assembles the state correctly and it passes."""
    msg = InboundMessage(
        message_id="msg-123",
        dedupe_key="test:msg-123",
        tenant_id="test",
        channel=Channel.EMAIL,
        sender="tester@example.com",
        subject=None,
        body_text="I need an invoice",  # will trigger BILLING (0.9V) from classify dummy
        body_redacted="I need an invoice",
        provider_message_id="test-123",
        received_at=_utcnow(),
    )

    decision = await run_pipeline(msg, deps)

    assert decision.action == RouteAction.AUTO_SEND
    assert decision.reason_code == "auto_send"


@pytest.mark.asyncio
async def test_complaint_escalates(deps):
    """If the classifier assigns Intent.COMPLAINT, Gate G4 blocks the message."""
    msg = InboundMessage(
        message_id="msg-456",
        dedupe_key="test:msg-456",
        tenant_id="test",
        channel=Channel.EMAIL,
        sender="tester@example.com",
        subject=None,
        body_text="Your service is terrible and I want to complain",  # triggers COMPLAINT
        body_redacted="Your service is terrible and I want to complain",
        provider_message_id="test-456",
        received_at=_utcnow(),
    )

    decision = await run_pipeline(msg, deps)

    # Gate G4 INTENT will block complaints
    assert decision.action == RouteAction.HUMAN_REVIEW
    assert decision.reason_code == "G4_intent_allows_auto"
