---
paths:
  - "src/taskflow/services/classify"
  - "src/taskflow/services/confidence"
  - "src/taskflow/services/cost"
  - "src/taskflow/services/delivery"
  - "src/taskflow/services/draft"
  - "src/taskflow/services/preprocess"
  - "src/taskflow/services/retrieve"
  - "src/taskflow/services/review"
  - "src/taskflow/services/route"
  - "src/taskflow/services/sla"
  - "src/taskflow/services/tracing"
  - "src/taskflow/services/validate"
  - "src/taskflow/domain/__init__.py"
  - "src/taskflow/domain/enums.py"
  - "src/taskflow/domain/models.py"
---
# Services and domain must stay pure

No vendor SDK imports here — not anthropic, ollama, qdrant_client, googleapiclient,
sqlalchemy, or streamlit. Dependencies arrive as Protocols from `taskflow.ports` and are
injected through the constructor.

Every public function is fully typed and must be unit-testable with no network, no disk
services, and no running Ollama. If you need an external call, add a port first, then an
adapter, then inject it.

`make typecheck` runs `lint-imports` and fails the build on violations. Do not work
around it by importing inside a function body.

Safety signals (policy violations, PII, citation validity, intent class, abstention,
validator health, suspicious context) are conjunctive gates evaluated before the weighted
score. Never turn a gate into a score weight — see ADR-001.
