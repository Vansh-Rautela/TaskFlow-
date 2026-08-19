# TaskFlow AI Support Agent — project kit

Everything an agent (Claude Code, Antigravity, Codex, Cursor) needs to start building.
Drop this into an empty repository and run `/start-phase` or point your agent at
`docs/03_IMPLEMENTATION_PLAN.md`.

## What's here

```
CLAUDE.md                  Claude Code project memory — hard rules + index
AGENTS.md                  cross-tool context (Antigravity, Codex, Cursor, Gemini CLI)
.claude/                   settings.json (permissions + hooks), rules/, agents/, skills/
.agents/                   rules/ (glob-scoped) and workflows/ for Antigravity
docs/00-13                 the full documentation set, written — not skeletons
config/                    providers, thresholds, policies (10 rules), prompts
src/taskflow/domain/       models.py + enums.py + errors.py — IMPLEMENTED
src/taskflow/ports/        six Protocol files — IMPLEMENTED
tests/unit/test_gates.py   the six canonical tests — write the code to make them pass
tests/fixtures/fakes.py    FakeLLMProvider, FakeVectorStore
pyproject.toml             deps + ruff + mypy + the import-linter boundary contract
Makefile                   every command you will run
```

## Start

```bash
cp .env.example .env        # ANTHROPIC_API_KEY, Gmail paths, optional Teams webhook
uv sync
ollama pull qwen2.5:7b-instruct
make check                  # green on an empty project
```

Then open `docs/03_IMPLEMENTATION_PLAN.md` at **P-1** (credentials) and work forward.
`domain/` and `ports/` are already done, so P1 is mostly persistence.

## Agent entry points

| Tool | Reads | Start with |
|---|---|---|
| Claude Code | `CLAUDE.md`, `.claude/rules/`, `.claude/agents/`, `.claude/skills/` | "Read docs/03_IMPLEMENTATION_PLAN.md, plan phase P0, don't write code yet" |
| Antigravity | `AGENTS.md`, `.agents/rules/`, `.agents/workflows/` | `/start-phase` |
| Anything else | `AGENTS.md` | same as Antigravity |

## The two rules that matter most

1. `domain/` and `services/` never import an SDK or an adapter. `make typecheck` runs
   `lint-imports` and fails the build if they do.
2. Safety checks are **conjunctive gates evaluated before the weighted score**, never
   weights inside it. `tests/unit/test_gates.py::test_critical_policy_violation_never_auto_sends`
   is the guard. See ADR-001.
