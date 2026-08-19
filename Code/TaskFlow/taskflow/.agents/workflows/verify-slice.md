# /verify-slice

Verification procedure to run before every commit.

1. Run `make lint`.
2. Run `make typecheck` (includes `lint-imports` — architectural boundaries).
3. Run `make test`.
4. If files under `src/taskflow/adapters/` changed, run `make test-int`.
5. If gates, policies, or thresholds changed, run `make scenario S=refund_750` and confirm
   the decision is `HUMAN_REVIEW` with `reason_code=G1_policy_critical`.
6. Open `docs/03_IMPLEMENTATION_PLAN.md`, locate the current phase, and verify every item
   in its Definition of done. Report anything unmet instead of assuming it passed.
7. Tick completed checkboxes in that phase.
8. Update `docs/04_SCHEMAS.md` if any model or table changed.
9. Append an ADR to `docs/02_ARCHITECTURE_DECISIONS.md` if a non-obvious choice was made.
10. Review the staged diff against the deny rules and boundary rules in AGENTS.md.
11. Propose a commit message `P{n}: <what changed>`.

Stop and report at the first red step. Do not continue past a failing test.
