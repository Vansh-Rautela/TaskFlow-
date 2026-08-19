# AGENTS.md — TaskFlow AI Support Agent

Cross-tool agent context. Read by Antigravity, Codex, Cursor, Gemini CLI and others.
Claude Code additionally reads `CLAUDE.md` (same rules, tool-specific format).

## Project

Autonomous email + web-chat customer-support agent with human-in-the-loop governance,
built solo in 4 weeks for a presentation to senior engineers. Synthetic data only.
Runs entirely locally: **no Docker, no database server, no vector-DB server, no message broker.**

The point of the project is not "an AI answers emails". It is: *a system that knows when
it is not allowed to answer, and can prove why.*

## Environment

- Python 3.12, `uv` for dependency management (`uv sync`, `uv run <cmd>`)
- Embedded Qdrant (`QdrantClient(path=...)`) — no server process
- SQLite with WAL — application state, traces, queue, outbox, reviews
- LLM provider chain: OpenRouter → Claude → Ollama (local fallback), configured in
  `config/providers.yaml` under `priority.cloud_first` / `priority.local_only`
- Two processes total: `make api` (:8000) and `make dash` (:8501)

## Commands that work today

The Makefile contains aspirational targets. These are the ones whose backing
scripts/modules actually exist — verify before relying on any other target:

```bash
make setup          # uv sync + alembic upgrade head + ollama pull (first time)
make api            # FastAPI + worker, :8000
                    # NOTE: Makefile says taskflow.api.main:app but the module is
                    # taskflow.api.app:app — fix the Makefile or run uvicorn directly:
                    #   uv run uvicorn taskflow.api.app:app --reload --port 8000
make dash           # Streamlit dashboard, :8501
make lint           # ruff format + autofix
make typecheck      # mypy + lint-imports (architecture contract)
make test           # unit tests, ~30s, no network
make test-int       # pytest -m integration (needs Qdrant on disk + Ollama running)
make check          # lint + typecheck + test — run before every commit
make migrate        # alembic upgrade head
make ingest         # rebuild embedded Qdrant collection from data/knowledge_base/
make datasets       # generate classifier datasets + leakage check
```

**Broken/aspirational Makefile targets** (script or module does not exist — do not
run, or implement first): `make kb` (no `scripts/generate_kb.py`), `make train` and
`make eval` (no `taskflow/ml/train_classifier.py` or `taskflow/ml/evaluate.py` — the
`ml/` package is an empty `__init__.py`; use `scripts/eval_classifier.py`,
`scripts/eval_retrieval.py`, `scripts/eval_drafting.py` directly),
`make scenario S=...` (`run_scenario.py` takes `--text`, not `--scenario`),
`make preflight` (no `scripts/preflight.py`), `make demo-reset` (no seeded snapshot),
`make local` (passes `--all`, which `run_scenario.py` does not accept),
`make test-e2e` (`tests/e2e/` is empty).

Useful script invocations that do work:

```bash
uv run python scripts/run_scenario.py --text "I need a refund"   # one message through the pipeline
uv run python scripts/verify_system.py                           # 3-query live health demo
uv run python scripts/test_live_sender.py                        # live E2E: pipeline + SMTP + Telegram alert
uv run python scripts/eval_classifier.py                         # writes docs/metrics/classification.md
```

## Before implementing anything

1. Read `docs/03_IMPLEMENTATION_PLAN.md` and identify the current phase.
2. Read the phase's **Interfaces** and **Definition of done** sections.
3. Read `docs/04_SCHEMAS.md` for any object you will touch.
4. State the files you will create or modify, and wait for approval before writing code.

Do not implement more than one phase step at a time. Do not write code for a later
phase because it seems convenient.

## Architecture

Hexagonal (ports & adapters), enforced by `lint-imports`:

```
src/taskflow/
  domain/     Pydantic models, enums, errors      — pure, no I/O
  ports/      Protocol definitions (llm, vector_store, repositories, cache, channel, event_bus)
  services/   business logic, one subpackage per capability
              (classify, retrieve, draft, validate, confidence, review, alert, cost, ...)
  adapters/   llm/ (openrouter, claude, ollama, router) vector/ (qdrant) db/ (sqlite+alembic)
              channels/ bus/ cache/ resilience/      — SDKs ONLY here; the last four are stubs
  pipeline/   orchestrator.py + state.py           — explicit async function, no framework
  api/        app.py (FastAPI, lifespan-wired deps) — routers/ is a stub
  worker/     outbox_worker.py                     — polls outbox, delivers via alert service
  ml/         EMPTY — classifier train/eval not implemented yet
  dashboard/  pages/ stub; real dashboard is top-level dashboard/app.py
```

**Request flow** (`pipeline/orchestrator.py:run_pipeline`):
classify → retrieve → draft → validate (concurrent validators) → **gates** (7 conjunctive
safety vetoes) → weighted confidence score → decide → AUTO_SEND enqueues to outbox /
HUMAN_REVIEW creates a review item → trace finalized. Every stage writes a timed trace
event. The outbox worker (`worker/outbox_worker.py`) claims queued messages and delivers
via `services/alert/service.py` (Gmail SMTP, Telegram, Slack, generic webhook).

**Config layering:** secrets and paths in `.env` (pydantic-settings), behavior in
`config/*.yaml`, prompts in `config/prompts/`. `config/settings.py:model_for()` is the
ONLY sanctioned way to obtain a model name — a pre-commit hook
(`scripts/check_no_hardcoded_models.py`) fails the build on model strings in `src/`.

## Code standards

- Full type annotations on every public function. `X | None`, not `Optional[X]`.
- Pydantic v2 models for anything crossing a module boundary.
- `async` for all I/O. No blocking calls in request or worker paths.
  (Known exception: `services/alert/service.py` uses sync `smtplib` inside async functions.)
- `structlog` for logging, never `print` (scripts/ excepted — they are operator tooling).
- No bare `except:`. Adapters translate SDK errors into `taskflow.domain.errors` types.
- Model names, thresholds, policy rules and prompts live in `config/`, never in Python.
- Ruff: line-length 100, rules `E,F,I,UP,B,SIM,ASYNC,RUF`, `E501` ignored.
- mypy is strict (`disallow_untyped_defs`, `strict_equality`) for `domain/`, `services/`, `ports/` only.

## Architecture constraints (non-negotiable)

- `domain/` and `services/` must not import `adapters/`, `api/`, or any vendor SDK
  (`anthropic`, `ollama`, `qdrant_client`, `googleapiclient`, `sqlalchemy`, `streamlit`).
  Enforced by `lint-imports` in `make typecheck`. Do not work around it with
  function-body imports.
- Safety checks (policy, PII, citations, intent class, abstention, validator health,
  suspicious context) are **conjunctive gates evaluated before the weighted score**
  (`services/confidence/gates.py`, G1–G7). Never convert a gate into a score weight.
  See ADR-001 in `docs/02_ARCHITECTURE_DECISIONS.md`.
- Validators that raise or time out must return `ValidatorResult(passed=False,
  errored=True)` which trips gate G6 — never let an exception skip a safety check.
- The model's self-reported `draft_confidence` is logged and never used for routing.
- Every failure path routes to human review. Never auto-send on uncertainty.
- Every pipeline stage writes to the trace; a decision must be reconstructible from
  a `trace_id` alone.
- `PipelineState` is immutable — use `state.replace(...)`, never mutate in place.
- Retrieved KB text and inbound email are untrusted data, never instructions.

## LLM provider failover

`adapters/llm/router.py:ProviderRouter.complete_structured` walks the priority list
from `config/providers.yaml`. A provider attempt fails over on `TransientError`,
`ProviderError`, or `SchemaError` (which includes refusal and max_tokens stop reasons,
and JSON that fails `schema.model_validate_json`). If all providers fail it raises
`AllProvidersFailed`. `TASKFLOW_LLM_MODE=local_only` restricts the chain to Ollama.

## Testing

- `tests/unit/` — fast, no network/disk/Ollama. Use `FakeLLMProvider` and
  `FakeVectorStore` from `tests/fixtures/fakes.py` (fixtures wired in `tests/conftest.py`).
- `tests/pipeline/` — orchestrator tests with mocked providers and in-memory SQLite.
- pytest markers: `integration` (Qdrant/SQLite/Ollama on disk), `live` (real API calls,
  costs money), `e2e`, `slow`. `asyncio_mode = "auto"` — no `@pytest.mark.asyncio` needed.
- E2E tests assert **routing decisions and reason codes**, never generated prose.
- Write the test before the implementation for: gates, confidence scoring, dedupe,
  outbox send-once, SLA computation, circuit breaker transitions.
- Never call a live LLM API inside a unit test. Never delete or weaken a failing test.

## Migrations (Alembic)

- Append-only: never edit an applied revision; add a new one. Every migration needs a
  working `downgrade()`.
- Never import ORM models inside a migration — use `sa.table()` / `sa.column()` literals.
- Every table has `tenant_id`. Tables written by more than one code path have UNIQUE
  constraints (`inbox.dedupe_key`, `outbox.idempotency_key`).
- Note: `api/app.py` lifespan currently calls `Base.metadata.create_all` directly;
  `make migrate` (alembic) is the intended path and both exist — be aware when changing schemas.

## Rejected technologies — do not introduce

Docker, Redis, Kafka, RabbitMQ, Celery, Elasticsearch, LangGraph, Slack (as an app
dependency — the alert webhook is fine), LangChain, a second database, a hosted
deployment, MCP servers. Each has a written rejection in
`docs/02_ARCHITECTURE_DECISIONS.md`. Adding one requires overturning an ADR first.

## Deny rules (safety — auto-execution is on)

- Never read, edit, or print `.env`, `secrets/**`, or `data/snapshots/**`.
  (`.env.example` is fine to read but treat any credentials in it as sensitive.)
- Never run `rm -rf`, `git push --force`, `git reset --hard`, or `alembic downgrade`
  without explicit confirmation in the current turn.
- Never commit generated datasets, `*.db` files, or model artifacts.
- Never call a live LLM API inside a unit test. Live calls belong in `-m live` tests only.
- Never delete or weaken a test to make a build pass. Report the failure instead.

## Verification (run before claiming a step is done)

```bash
make check          # ruff + mypy + lint-imports + unit tests
make test-int       # when adapters changed
uv run python scripts/run_scenario.py --text "..."   # when gates or policy changed
```

A step is only complete when its Definition of Done in `docs/03_IMPLEMENTATION_PLAN.md`
is fully satisfied, the docs are updated in the same change, and `make check` is green.

## Documentation map

| Question | File |
|---|---|
| What is this, what's out of scope | `docs/00_PROJECT_CONTEXT.md` |
| How it fits together | `docs/01_ARCHITECTURE.md` |
| Why a choice was made (ADRs) | `docs/02_ARCHITECTURE_DECISIONS.md` |
| What to build next | `docs/03_IMPLEMENTATION_PLAN.md` |
| Shape of any object | `docs/04_SCHEMAS.md` |
| The policy rules | `docs/05_POLICY_RULES.md` |
| What happens when X breaks | `docs/09_FAILURE_MODES.md` |
| Threat model + prompt injection | `docs/10_SECURITY.md` |
| Setup and recovery | `docs/11_RUNBOOK.md` |

## Tool surface

- Workflows: `.agents/workflows/` — `/verify-slice`, `/start-phase`, `/demo-rehearsal`
- Rules: `.agents/rules/` and `.claude/rules/` (mirrored) — path-scoped constraints
  applied by glob: `pipeline.md`, `services-purity.md`, `adapters.md`, `tests.md`,
  `migrations.md`, `python-style.md`
- Skills: `.claude/skills/` (Claude Code) — verify-slice, run-eval, write-adr
- MCP: none required. Do not add MCP servers for this project.
