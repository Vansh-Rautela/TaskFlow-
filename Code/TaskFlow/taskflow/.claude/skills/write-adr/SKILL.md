---
name: write-adr
description: Appends an architecture decision record. Use whenever a non-obvious technical choice is made, a dependency is added, or an existing decision is overturned.
---
# Write an ADR

Append to `docs/02_ARCHITECTURE_DECISIONS.md` using exactly this shape:

```markdown
## ADR-0NN — <short imperative title>

**Status.** Accepted | Superseded by ADR-0MM
**Date.** YYYY-MM-DD

**Context.** What forced a decision. Include the constraint that made it non-obvious
(budget, time, no Docker, no stable cloud key, must be explainable on stage).

**Options.** (a) ... (b) ... (c) ... — each with its real cost, not a strawman.

**Decision.** What we chose, in one sentence, in the active voice.

**Consequences.** What this makes easy, what it makes hard, and what would make us
revisit it. Name the migration path if there is one.
```

Rules:
- One decision per ADR. Never edit an accepted ADR — supersede it with a new one and
  mark the old one `Superseded by`.
- Any new dependency requires an ADR before the dependency is added to `pyproject.toml`.
- Re-introducing a rejected technology (Docker, Redis, Celery, Kafka, Elasticsearch,
  LangGraph, Slack) requires an ADR that explicitly supersedes the rejection.
- If the decision came from a measurement, paste the results table into the ADR.
