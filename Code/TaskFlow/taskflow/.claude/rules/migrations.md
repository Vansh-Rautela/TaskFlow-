---
paths:
  - "src/taskflow/adapters/db/migrations/**"
---
# Migrations are append-only

- Never edit a revision that has been applied. Add a new revision instead.
- Every migration needs a working `downgrade()`.
- Never import ORM models inside a migration — use `sa.table()` / `sa.column()` literals
  so old revisions keep working after the models change.
- Every table has `tenant_id`. Every table that is written by more than one code path has
  an appropriate UNIQUE constraint: `inbox.dedupe_key`, `outbox.idempotency_key`.
- Never run `alembic downgrade` against `data/taskflow.db` without explicit confirmation.
