# Queries — Human-Readable Index

This folder is a human-readable mirror of the machine-readable evaluation set in
`../evaluation/`. Each query is derived from the actual knowledge-base documents
and carries the expected intent, routing, and ground-truth document.

- [tier-1.md](./tier-1.md) — Direct queries (answerable from one document)
- [tier-2.md](./tier-2.md) — Conditional / policy-boundary queries
- [tier-3.md](./tier-3.md) — Ambiguous queries (clarification required)
- [tier-4.md](./tier-4.md) — Multi-turn threads
- [adversarial.md](./adversarial.md) — Keyword overlap, negation, temporal,
  ambiguous references, contradictions, and misrouted/out-of-scope queries

For the authoritative JSONL ground truth (including `required_facts`,
`missing_information`, and `potential_negative_documents`), use
`../evaluation/`.