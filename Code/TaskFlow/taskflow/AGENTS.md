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
- Claude API (primary LLM) with Ollama running locally as fallback
- Two processes total: `make api` (:8000) and `make dash` (:8501)

## Before implementing anything

1. Read `docs/03_IMPLEMENTATION_PLAN.md` and identify the current phase.
2. Read the phase's **Interfaces** and **Definition of done** sections.
3. Read `docs/04_SCHEMAS.md` for any object you will touch.
4. State the files you will create or modify, and wait for approval before writing code.

Do not implement more than one phase step at a time. Do not write code for a later
phase because it seems convenient.

## Code standards

- Full type annotations on every public function. `X | None`, not `Optional[X]`.
- Pydantic v2 models for anything crossing a module boundary.
- `async` for all I/O. No blocking calls in request or worker paths.
- `structlog` for logging, never `print`.
- No bare `except:`. Adapters translate SDK errors into `taskflow.domain.errors` types.
- Model names, thresholds, policy rules and prompts live in `config/`, never in Python.

## Architecture constraints (non-negotiable)

- `domain/` and `services/` must not import `adapters/`, `api/`, or any vendor SDK.
  Enforced by `lint-imports` in `make typecheck`.
- Safety checks (policy, PII, citations, intent class, abstention, validator health,
  suspicious context) are **conjunctive gates evaluated before the weighted score**.
  Never convert a gate into a score weight. See ADR-001 in `docs/02_ARCHITECTURE_DECISIONS.md`.
- The model's self-reported `draft_confidence` is logged and never used for routing.
- Every failure path routes to human review. Never auto-send on uncertainty.
- Every pipeline stage writes to the trace.

## Rejected technologies — do not introduce

Docker, Redis, Kafka, RabbitMQ, Celery, Elasticsearch, LangGraph, Slack, LangChain,
a second database, a hosted deployment. Each has a written rejection in
`docs/02_ARCHITECTURE_DECISIONS.md`. Adding one requires overturning an ADR first.

## Deny rules (safety — auto-execution is on)

- Never read, edit, or print `.env`, `secrets/**`, or `data/snapshots/**`.
- Never run `rm -rf`, `git push --force`, `git reset --hard`, or `alembic downgrade`
  without explicit confirmation in the current turn.
- Never edit an Alembic revision that has already been applied — add a new one.
- Never commit generated datasets, `*.db` files, or model artifacts.
- Never call a live LLM API inside a unit test. Live calls belong in `-m live` tests only.
- Never delete or weaken a test to make a build pass. Report the failure instead.

## Verification (run before claiming a step is done)

```bash
make check          # ruff + mypy + lint-imports + unit tests
make test-int       # when adapters changed
make scenario S=refund_750   # when gates or policy changed
```

A step is only complete when its Definition of Done in `docs/03_IMPLEMENTATION_PLAN.md`
is fully satisfied, the docs are updated in the same change, and `make check` is green.

## Tool surface

- Workflows: `.agents/workflows/` — `/verify-slice`, `/start-phase`, `/demo-rehearsal`
- Rules: `.agents/rules/` — path-scoped constraints, applied by glob
- Skills: `.claude/skills/` (Claude Code) — verify-slice, run-eval, write-adr
- MCP: none required. Do not add MCP servers for this project.
