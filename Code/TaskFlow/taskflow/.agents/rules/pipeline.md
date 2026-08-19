---
activation: glob
glob: "src/taskflow/pipeline/**"
---
# The pipeline is explicit, not a framework

We deliberately do not use LangGraph (ADR-005). The orchestrator is a plain async
function with explicit branching, and it should stay readable end-to-end on one screen.

- Each stage calls exactly one service function and records one trace event.
- No business logic in the orchestrator — branching conditions are one-line calls into
  services or the confidence module.
- Never mutate `PipelineState` in place; build and return a new state.
- Validators run concurrently with `asyncio.gather`; a validator that raises or times out
  must produce `ValidatorResult(passed=False, errored=True, reason="validator_error")`,
  which trips gate G6. Never let an exception skip a safety check.
- If this file grows past ~120 lines, logic has leaked in from services. Move it back.
