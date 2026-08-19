# TaskFlow AI Support Agent

Autonomous email + web-chat support agent with human-in-the-loop governance.
Solo build, 4 weeks, synthetic data only, local-first, **no Docker, no servers**.
Demo to senior engineers — every component must be explainable in one sentence.

**Before starting work, read `docs/03_IMPLEMENTATION_PLAN.md` and find the current phase.**

## Commands

```bash
make setup       # uv sync + migrations + ollama pull   (once)
make api         # FastAPI + worker + SLA + pollers  :8000
make dash        # Streamlit review queue + traces   :8501
make check       # lint + typecheck + unit tests     (before every commit)
make test-int    # integration tests
make ingest      # rebuild the embedded Qdrant collection
make train       # train + evaluate the intent classifier
make scenario S=refund_750
make preflight   # demo readiness — must exit 0
```

## Layout

```
src/taskflow/
  domain/     Pydantic models, enums, errors     — pure, no I/O
  ports/      Protocol definitions               — the seams
  adapters/   llm/ vector/ db/ channels/ alerts/ resilience/   — SDKs ONLY here
  services/   all business logic                 — pure-ish, ports injected
  pipeline/   the explicit async orchestrator    — ~60 lines, no framework
  api/        FastAPI routers + web chat page    — no business logic
  ml/         embeddings, classifier train/eval
  dashboard/  Streamlit
config/       providers.yaml thresholds.yaml policies.yaml prompts/
data/         knowledge_base/ datasets/ manifests/ snapshots/ qdrant/
docs/         00-13 — see docs/README section in 00_PROJECT_CONTEXT.md
tests/        unit/ integration/ pipeline/ e2e/
```

## Hard rules

1. **`domain/` and `services/` never import `adapters/`, `api/`, or any vendor SDK.** Dependencies arrive as `ports.*` Protocols. `make typecheck` runs `lint-imports` and fails the build if this is violated.
2. **No model names, thresholds, policy rules, or prompts in Python.** They live in `config/*.yaml` and `config/prompts/`. There is a pre-commit hook that fails on hardcoded model strings.
3. **Safety is a veto, not a weight.** Critical policy violations, PII leaks, unresolvable citations, complaint intent, classifier abstention, validator errors, and suspicious context are *conjunctive gates* evaluated **before** the weighted score. Never move a safety signal into the weighted average. See ADR-001.
4. **`draft_confidence` from the model is logged and never used for routing.**
5. **Fail closed.** Any error, timeout, or ambiguity routes to human review. Never auto-send on uncertainty.
6. **No new dependencies without an ADR.** The dependency list in `docs/02_ARCHITECTURE_DECISIONS.md` is deliberate and small.
7. **Do not add Docker, Redis, Kafka, Celery, Elasticsearch, or LangGraph.** Each was considered and rejected with a written reason. Re-adding one requires overturning an ADR.
8. **Retrieved KB text and inbound email are untrusted data, never instructions.** Context goes in a delimited block; instruction-like patterns set `suspicious_context` and force human review.
9. **Every persisted row carries `tenant_id`.** Migrations are append-only.
10. **Every pipeline stage writes to the trace.** If a decision can't be reconstructed from a `trace_id` alone, the stage isn't finished.
11. **Tests before implementation** for gates, dedupe, outbox, and SLA logic.

## Working agreement

- One phase step = one commit = one reviewable diff. Diffs over ~400 lines mean the step was too big.
- Plan first (files + interfaces), get approval, then implement one step at a time.
- Run the `verify-slice` skill at the end of every step.
- Update `docs/` in the same commit as the code that changed.
- Never edit `.env`, `secrets/`, or `data/snapshots/` without being asked.

## Where things are explained

| Question | File |
|---|---|
| What is this, what's out of scope | `docs/00_PROJECT_CONTEXT.md` |
| How it fits together | `docs/01_ARCHITECTURE.md` |
| Why a choice was made | `docs/02_ARCHITECTURE_DECISIONS.md` |
| What to build next | `docs/03_IMPLEMENTATION_PLAN.md` |
| Shape of any object | `docs/04_SCHEMAS.md` |
| The policy rules | `docs/05_POLICY_RULES.md` |
| Dataset generation + leakage | `docs/06_DATA_GENERATION.md` |
| How metrics are measured | `docs/07_EVAL_METHODOLOGY.md` |
| Trace schema + dashboard | `docs/08_OBSERVABILITY.md` |
| What happens when X breaks | `docs/09_FAILURE_MODES.md` |
| Threat model + prompt injection | `docs/10_SECURITY.md` |
| Setup and recovery | `docs/11_RUNBOOK.md` |
| Demo narration | `docs/12_DEMO_SCRIPT.md` |
| What production still needs | `docs/13_PRODUCTION_READINESS_GAP.md` |

## Current state

Phase **P0** — nothing implemented except `domain/` and `ports/`.
Do not assume a module exists. Check first.
