---
name: verify-slice
description: The end-of-step verification procedure. Run before every commit, after implementing any part of a phase.
---
# Verify a slice

Run in order. Stop at the first failure and report it rather than continuing.

1. `make lint`
2. `make typecheck` — includes `lint-imports`, which enforces the architectural boundary
3. `make test`
4. If adapters changed: `make test-int`
5. If gates, policy, or thresholds changed: `make scenario S=refund_750` and confirm the
   decision is `HUMAN_REVIEW` with `reason_code=G1_policy_critical`
6. Open `docs/03_IMPLEMENTATION_PLAN.md`, find the current phase, and check the
   **Definition of done** list item by item. Report anything unmet.
7. Tick the completed checkboxes in the phase.
8. If a non-obvious decision was made, append an ADR to
   `docs/02_ARCHITECTURE_DECISIONS.md` using: Context / Options / Decision / Consequences.
9. If any Pydantic model or DB table changed, update `docs/04_SCHEMAS.md`.
10. Delegate to the `diff-reviewer` subagent.
11. Propose a commit message of the form `P{n}: <what changed>` and stage the files.

Never commit with steps 1-4 red.
