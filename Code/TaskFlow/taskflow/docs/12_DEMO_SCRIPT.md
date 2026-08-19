# 12 — Demo Script

18 minutes. Rehearse twice, on different days, from a cold start.

## Pre-flight (before anyone is in the room)

```bash
make demo-reset && make preflight     # must exit 0
```

Checks: Qdrant point count · database at head revision · classifier artifact version
matches expected metrics · dataset manifest hashes · models warm (< 1 s first call) ·
**Gmail token valid** · Ollama reachable · Claude reachable · today's spend under cap ·
all five scenarios pass · all breakers closed.

## Running order

| # | Time | Do | Say |
|---|---|---|---|
| 0 | 0:00 | Show the architecture on one slide, then close it | "Eleven components. The interesting one is the decision layer — I'll come back to it." |
| 1 | 1:00 | Web chat: *"How do I reset my password?"* → instant reply | "Fast path. Zero LLM calls, zero cost — about 30% of real support volume is repeat questions and they should never reach a model." |
| 2 | 3:00 | Email the demo inbox: *"I was charged twice for my Pro subscription"* → auto-sent with citations | "Classified, retrieved, drafted, validated, sent. Under four seconds." |
| 3 | 6:00 | **Open the trace for #2.** Walk all five panes slowly | "This is the actual product. Every score, every validator, every gate." |
| 4 | 10:00 | Email: *"We want a $750 refund for our Enterprise plan"* → blocked. Point at score **0.91** and gate G1 red | **"The score is 0.91. It still didn't send. Safety is a veto, not a weighted average — if policy were a 0.15 weight, this email goes out."** |
| 5 | 12:00 | Approve it with an edit in Streamlit; show the `EditRecord` row | "Both texts stored. That's the training data for the fine-tuning I deliberately deferred." |
| 6 | 14:00 | **Unplug the network.** Send another message → Ollama drafts it | "Same pipeline, local 7B model, no internet. My API key is temporary, so the system had to work without it." |
| 7 | 15:30 | Show the Claude draft and the local draft side by side | "The local prose is worse. I don't hide that — and the gates catch it: degraded mode produces more escalations, not worse emails." |
| 8 | 16:30 | Edit `thresholds.yaml` 0.80 → 0.95, re-run #2 → now escalates | "Config, not code. No restart." |
| 9 | 17:00 | Classifier metrics slide: 0.94 synthetic / 0.81 golden | "The gap is what synthetic evaluation costs. 0.81 is the number I'd defend." |
| 10 | 17:30 | `13_PRODUCTION_READINESS_GAP.md` | "What I'd build next, and roughly what each costs." |

**Steps 4 and 6 are the two moments that decide whether you're taken seriously.**
Rehearse those specifically, out loud, until they're smooth.

## The five scenarios and what each proves

| Scenario | Expected action | reason_code | LLM calls | Proves |
|---|---|---|---|---|
| `faq_password` | TEMPLATE_SENT | `fastpath_hit` | **0** | deterministic fast path, cost discipline |
| `billing_double` | AUTO_SEND | `auto_send` | 2 | the full grounded RAG path |
| `refund_750` | HUMAN_REVIEW | `G1_policy_critical` | 2 | **governance is a veto** |
| `spam_iphone` | REJECTED_SPAM | `spam_filter` | **0** | filtering before spend |
| `complaint_rant` | HUMAN_REVIEW | `G4_intent` | **0** | knowing when not to generate |

E2E tests assert exactly this table. They never assert generated prose — model output
isn't deterministic, decisions are.

## Questions you will be asked, and the honest answers

- *"How do you know the classifier is any good?"* → both numbers, the gap, the abstain rate.
- *"What happens if the LLM hallucinates a refund?"* → gate G1, deterministic, here's the test.
- *"What if someone puts instructions in an email?"* → routing is a classifier, not a
  model; policy is regex on the output; the model has no tools. Injection changes the
  prose, never the decision.
- *"Why no Docker / Kubernetes / Kafka?"* → sized to the problem; here's the migration path.
- *"Why not LangGraph?"* → ADR-005, with the threshold at which I'd add it back.
- *"What did you get wrong?"* → **the confidence formula.** Policy started as a 0.15
  weight; a violating draft scored 0.85 against an 0.80 threshold and would have sent.
  Lead with this if it doesn't come up.

## Insurance

- Backup recording of a full clean run (`scripts/record_demo.py`)
- `TASKFLOW_LLM_MODE=local_only` — the entire demo works with no network
- `make demo-reset` rehearsed: recovery from a broken state in under 30 seconds
- Phone hotspot ready; venue network tested in advance
