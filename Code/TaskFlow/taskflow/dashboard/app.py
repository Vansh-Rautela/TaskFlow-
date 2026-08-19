"""Streamlit Human Operator Console & Observability Dashboard for TaskFlow (Phase P9).

Provides interactive human-in-the-loop review operations, trace log exploration,
and real-time LLM performance & cost metrics.
"""

import asyncio
from datetime import UTC, datetime

import streamlit as st

from taskflow.adapters.db.engine import build_engine, build_session_factory
from taskflow.adapters.db.orm import Base
from taskflow.adapters.db.repositories import (
    SQLiteOutboxRepository,
    SQLiteReviewRepository,
    SQLiteTraceRepository,
)
from taskflow.services.review.service import (
    approve_review,
    edit_and_approve_review,
    list_pending_reviews,
    reject_review,
)

st.set_page_config(
    page_title="TaskFlow Operator Dashboard",
    page_icon="⚡",
    layout="wide",
)


def run_async(coro):
    return asyncio.run(coro)


async def _get_repos():
    db_url = "sqlite+aiosqlite:///data/taskflow.db"
    engine = build_engine(db_url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    factory = build_session_factory(engine)
    trace_repo = SQLiteTraceRepository(factory)
    review_repo = SQLiteReviewRepository(factory)
    outbox_repo = SQLiteOutboxRepository(factory)

    return trace_repo, review_repo, outbox_repo, engine


st.title("⚡ TaskFlow — Customer Support AI Console")
st.caption("Human-in-the-Loop Review Operations & Production Observability")

tab1, tab2, tab3 = st.tabs(
    ["📝 Human Review Console", "🔍 Traces & Observability", "📊 System Health & Metrics"]
)

with tab1:
    st.header("Pending Human Review Queue")

    try:
        trace_repo, review_repo, outbox_repo, engine = run_async(_get_repos())
        pending_items = run_async(list_pending_reviews(review_repo))
    except Exception as e:
        st.error(f"Failed to connect to database: {e}")
        pending_items = []

    if not pending_items:
        st.success("🎉 Review queue is empty! No messages waiting for human approval.")
    else:
        st.info(f"📋 {len(pending_items)} items requiring human review.")

        item_options = {
            f"Review #{item.review_id} | Trace {item.trace_id[:8]} | Tenant {item.tenant_id}": item
            for item in pending_items
        }

        selected_label = st.selectbox("Select Pending Review Item:", list(item_options.keys()))
        selected_item = item_options[selected_label]

        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("Routing Decision Context")
            st.json(selected_item.decision.model_dump(mode="json"))

            if selected_item.draft and selected_item.draft.citations:
                st.subheader("Context Citations")
                st.json(selected_item.draft.citations)

        with col2:
            st.subheader("Response Draft Editor")
            original_draft = (
                selected_item.draft.response_text if selected_item.draft else "No draft available"
            )

            edited_text = st.text_area(
                "Review / Edit Outbound Response:",
                value=original_draft,
                height=250,
            )

            btn_col1, btn_col2, btn_col3 = st.columns(3)

            with btn_col1:
                if st.button("✅ Approve Original", type="primary", use_container_width=True):
                    success = run_async(
                        approve_review(
                            review_repo,
                            outbox_repo,
                            selected_item.review_id,
                            operator="streamlit_admin",
                        )
                    )
                    if success:
                        st.success("Approved and queued to outbox!")
                        st.rerun()
                    else:
                        st.error("Failed to approve item (may have already been actioned).")

            with btn_col2:
                if st.button("✏️ Save Edit & Approve", use_container_width=True):
                    success = run_async(
                        edit_and_approve_review(
                            review_repo,
                            outbox_repo,
                            selected_item.review_id,
                            edited_text=edited_text,
                            operator="streamlit_admin",
                        )
                    )
                    if success:
                        st.success("Saved edit and queued to outbox!")
                        st.rerun()
                    else:
                        st.error("Failed to edit item.")

            with btn_col3:
                if st.button("❌ Reject Draft", use_container_width=True):
                    success = run_async(
                        reject_review(
                            review_repo, selected_item.review_id, operator="streamlit_admin"
                        )
                    )
                    if success:
                        st.warning("Draft rejected.")
                        st.rerun()
                    else:
                        st.error("Failed to reject item.")

with tab2:
    st.header("Trace Explorer & Log Inspection")

    try:
        trace_repo, review_repo, outbox_repo, engine = run_async(_get_repos())
        recent_traces = run_async(trace_repo.recent(limit=50))
    except Exception as e:
        st.error(f"Failed to fetch traces: {e}")
        recent_traces = []

    if recent_traces:
        trace_data = []
        for t in recent_traces:
            trace_data.append(
                {
                    "Trace ID": t.trace_id,
                    "Started At": t.started_at.strftime("%H:%M:%S") if t.started_at else "",
                    "Intent": t.intent.value if t.intent else "N/A",
                    "Action": t.decision.action.value if t.decision else "N/A",
                    "Reason": t.decision.reason if t.decision else "N/A",
                    "Score": f"{t.confidence.score:.3f}" if t.confidence else "N/A",
                    "LLM Cost ($)": f"{sum(c.cost_usd for c in t.llm_calls):.5f}",
                }
            )

        st.dataframe(trace_data, use_container_width=True)
    else:
        st.info("No traces recorded yet.")

with tab3:
    st.header("System Health & LLM Metrics")

    try:
        trace_repo, review_repo, outbox_repo, engine = run_async(_get_repos())
        traces = run_async(trace_repo.recent(limit=200))
    except Exception as e:
        traces = []

    total_msg = len(traces)
    auto_cnt = sum(
        1 for t in traces if t.decision and t.decision.action.value == "auto_reply"
    )
    human_cnt = sum(
        1 for t in traces if t.decision and t.decision.action.value == "human_review"
    )
    total_cost = sum(sum(c.cost_usd for c in t.llm_calls) for t in traces)

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric("Total Messages Processed", f"{total_msg}")
    kpi2.metric(
        "Auto-Reply Rate", f"{(auto_cnt / total_msg * 100):.1f}%" if total_msg else "0.0%"
    )
    kpi3.metric(
        "Human Review Rate", f"{(human_cnt / total_msg * 100):.1f}%" if total_msg else "0.0%"
    )
    kpi4.metric("Total LLM Cost ($)", f"${total_cost:.4f}")
