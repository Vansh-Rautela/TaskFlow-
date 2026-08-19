"""0001_initial — create all nine tables.

Generated: 2026-08-18
Revision ID: 0001
Revises: (none — this is the initial revision)

Every table carries tenant_id (indexed).
Two UNIQUE constraints are critical:
  - inbox.dedupe_key        (deduplication gate at ingest)
  - outbox.idempotency_key  (send-once guarantee at delivery)
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ------------------------------------------------------------------ inbox
    op.create_table(
        "inbox",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("message_id", sa.String(64), nullable=False),
        sa.Column("dedupe_key", sa.String(256), nullable=False),
        sa.Column("tenant_id", sa.String(64), nullable=False),
        sa.Column("channel", sa.String(16), nullable=False),
        sa.Column("sender", sa.String(320), nullable=False),
        sa.Column("subject", sa.Text(), nullable=True),
        sa.Column("body_text", sa.Text(), nullable=False),
        sa.Column("body_redacted", sa.Text(), nullable=False),
        sa.Column("thread_ref", sa.String(256), nullable=True),
        sa.Column("provider_message_id", sa.String(256), nullable=False),
        sa.Column("provider_thread_headers", sa.JSON(), nullable=False),
        sa.Column("received_at", sa.DateTime(), nullable=False),
        sa.Column("raw_ref", sa.String(512), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("dedupe_key", name="uq_inbox_dedupe_key"),
    )
    op.create_index("ix_inbox_message_id", "inbox", ["message_id"])
    op.create_index("ix_inbox_tenant_id", "inbox", ["tenant_id"])

    # ----------------------------------------------------------------- traces
    op.create_table(
        "traces",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("trace_id", sa.String(64), nullable=False),
        sa.Column("conversation_id", sa.String(64), nullable=False),
        sa.Column("message_id", sa.String(64), nullable=False),
        sa.Column("tenant_id", sa.String(64), nullable=False),
        sa.Column("source_channel", sa.String(16), nullable=False),
        sa.Column("started_at", sa.DateTime(), nullable=False),
        sa.Column("finished_at", sa.DateTime(), nullable=True),
        sa.Column("intent", sa.String(32), nullable=True),
        sa.Column("intent_confidence", sa.Float(), nullable=True),
        sa.Column("classifier_version", sa.String(64), nullable=True),
        sa.Column("retrieval_json", sa.JSON(), nullable=True),
        sa.Column("draft_json", sa.JSON(), nullable=True),
        sa.Column("validators_json", sa.JSON(), nullable=True),
        sa.Column("confidence_json", sa.JSON(), nullable=True),
        sa.Column("decision_json", sa.JSON(), nullable=True),
        sa.Column("llm_calls_json", sa.JSON(), nullable=True),
        sa.Column("delivery_result", sa.String(64), nullable=True),
        sa.Column("errors_json", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("trace_id", name="uq_traces_trace_id"),
    )
    op.create_index("ix_traces_trace_id", "traces", ["trace_id"])
    op.create_index("ix_traces_conversation_id", "traces", ["conversation_id"])
    op.create_index("ix_traces_message_id", "traces", ["message_id"])
    op.create_index("ix_traces_tenant_id", "traces", ["tenant_id"])

    # ----------------------------------------------------------- trace_events
    op.create_table(
        "trace_events",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("trace_id", sa.String(64), nullable=False),
        sa.Column("tenant_id", sa.String(64), nullable=False),
        sa.Column("stage", sa.String(64), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("elapsed_ms", sa.Integer(), nullable=False),
        sa.Column("at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_trace_events_trace_id", "trace_events", ["trace_id"])

    # ---------------------------------------------------------------- reviews
    op.create_table(
        "reviews",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("review_id", sa.String(64), nullable=False),
        sa.Column("trace_id", sa.String(64), nullable=False),
        sa.Column("conversation_id", sa.String(64), nullable=False),
        sa.Column("tenant_id", sa.String(64), nullable=False),
        sa.Column("state", sa.String(16), nullable=False, default="pending"),
        sa.Column("draft_json", sa.JSON(), nullable=True),
        sa.Column("decision_json", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("sla_deadline", sa.DateTime(), nullable=False),
        sa.Column("escalated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("review_id", name="uq_reviews_review_id"),
    )
    op.create_index("ix_reviews_review_id", "reviews", ["review_id"])
    op.create_index("ix_reviews_trace_id", "reviews", ["trace_id"])
    op.create_index("ix_reviews_tenant_id", "reviews", ["tenant_id"])

    # ------------------------------------------------------------- edit_records
    op.create_table(
        "edit_records",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("review_id", sa.String(64), nullable=False),
        sa.Column("tenant_id", sa.String(64), nullable=False),
        sa.Column("original_draft", sa.Text(), nullable=False),
        sa.Column("edited_draft", sa.Text(), nullable=False),
        sa.Column("editor", sa.String(256), nullable=False),
        sa.Column("edited_at", sa.DateTime(), nullable=False),
        sa.Column("reason", sa.Text(), nullable=True),
        sa.Column("char_diff", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_edit_records_review_id", "edit_records", ["review_id"])

    # ----------------------------------------------------------------- outbox
    op.create_table(
        "outbox",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("outbound_id", sa.String(64), nullable=False),
        sa.Column("conversation_id", sa.String(64), nullable=False),
        sa.Column("tenant_id", sa.String(64), nullable=False),
        sa.Column("channel", sa.String(16), nullable=False),
        sa.Column("recipient", sa.String(320), nullable=False),
        sa.Column("subject", sa.Text(), nullable=True),
        sa.Column("body_text", sa.Text(), nullable=False),
        sa.Column("reply_headers", sa.JSON(), nullable=False),
        sa.Column("state", sa.String(16), nullable=False, default="queued"),
        sa.Column("idempotency_key", sa.String(256), nullable=False),
        sa.Column("retry_count", sa.Integer(), nullable=False, default=0),
        sa.Column("last_error", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("outbound_id", name="uq_outbox_outbound_id"),
        sa.UniqueConstraint("idempotency_key", name="uq_outbox_idempotency_key"),
    )
    op.create_index("ix_outbox_outbound_id", "outbox", ["outbound_id"])
    op.create_index("ix_outbox_conversation_id", "outbox", ["conversation_id"])
    op.create_index("ix_outbox_tenant_id", "outbox", ["tenant_id"])

    # --------------------------------------------------------------- llm_calls
    op.create_table(
        "llm_calls",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("trace_id", sa.String(64), nullable=False),
        sa.Column("tenant_id", sa.String(64), nullable=False),
        sa.Column("purpose", sa.String(32), nullable=False),
        sa.Column("provider", sa.String(32), nullable=False),
        sa.Column("model", sa.String(64), nullable=False),
        sa.Column("prompt_tokens", sa.Integer(), nullable=False),
        sa.Column("completion_tokens", sa.Integer(), nullable=False),
        sa.Column("cost_usd", sa.Float(), nullable=False),
        sa.Column("latency_ms", sa.Integer(), nullable=False),
        sa.Column("attempts", sa.Integer(), nullable=False, default=1),
        sa.Column("repaired", sa.Boolean(), nullable=False, default=False),
        sa.Column("failed_over", sa.Boolean(), nullable=False, default=False),
        sa.Column("called_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_llm_calls_trace_id", "llm_calls", ["trace_id"])

    # ------------------------------------------------------------------ audit
    op.create_table(
        "audit",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("tenant_id", sa.String(64), nullable=False),
        sa.Column("actor", sa.String(256), nullable=False),
        sa.Column("action", sa.String(64), nullable=False),
        sa.Column("entity_type", sa.String(64), nullable=False),
        sa.Column("entity_id", sa.String(64), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_audit_tenant_id", "audit", ["tenant_id"])
    op.create_index("ix_audit_entity_id", "audit", ["entity_id"])

    # ----------------------------------------------------------------- alerts
    op.create_table(
        "alerts",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("tenant_id", sa.String(64), nullable=False),
        sa.Column("alert_type", sa.String(64), nullable=False),
        sa.Column("entity_id", sa.String(64), nullable=True),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("channel", sa.String(32), nullable=False),
        sa.Column("sent", sa.Boolean(), nullable=False, default=False),
        sa.Column("error", sa.Text(), nullable=True),
        sa.Column("at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_alerts_tenant_id", "alerts", ["tenant_id"])


def downgrade() -> None:
    op.drop_table("alerts")
    op.drop_table("audit")
    op.drop_table("llm_calls")
    op.drop_table("outbox")
    op.drop_table("edit_records")
    op.drop_table("reviews")
    op.drop_table("trace_events")
    op.drop_table("traces")
    op.drop_table("inbox")
