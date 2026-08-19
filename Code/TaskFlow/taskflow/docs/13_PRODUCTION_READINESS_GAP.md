# 13 — Production Readiness Gap

What v1 deliberately does not do, why, and what each would cost. This is the closing
slide: it turns "what we didn't build" into a roadmap.

## Deliberate v1 limits

| Gap | Why deferred | Effort | Unblocks |
|---|---|---|---|
| **Containerization** | no Docker experience; embedded services made it unnecessary | 2 days | any hosted deployment |
| **Postgres** | SQLite is correct for one writer and one user | 1 day | concurrent workers, PITR |
| **Qdrant server** | local mode covers ~20k points; we have ~200 | 0.5 day | larger corpora, replication |
| **Hosted deployment** | demo is local + screen share | 3 days | anyone else using it |
| **Gmail push (Watch → Pub/Sub → webhook)** | polling is fine at demo volume | 2 days | sub-second latency, no polling cost |
| **LLM fine-tuning** | needs a larger training set and real budget; `EditRecord` pipeline already collects the data | 1–2 weeks | better first-draft quality, fewer escalations |
| **Scheduled retraining** | manual script demonstrates the mechanism | 1 day | continuous improvement |
| **Real PII detection (NER)** | regex is adequate for synthetic data | 2 days | actual customer data, compliance |
| **Multi-tenancy** | `tenant_id` columns exist; isolation is not enforced end-to-end | 1 week | more than one customer |
| **Inbound Teams/Slack** | tenant admin and public endpoints required | 2–3 days each | real chat channels |
| **Load testing** | single-user demo | 2 days | capacity planning |
| **RBAC on review queue** | one reviewer | 2 days | a real support team |
| **Rate limiting / CSRF on web chat** | localhost only | 1 day | public exposure |
| **Secret management** | `.env` on a local machine | 1 day | anything non-local |
| **KB provenance and signing** | the residual prompt-injection risk in `10_SECURITY.md` | 3 days | untrusted KB editors |
| **Distributed tracing (OpenTelemetry)** | the trace table answers the domain questions | 2 days | infra-level debugging |

## Migration path

```
v1  local        : 2 processes · embedded Qdrant · SQLite · Ollama fallback
v1.5 hosted      : containerize · Postgres · Qdrant server · Gmail push · secret manager
v2  production   : N API replicas · M workers · managed Postgres/Redis/Qdrant ·
                   OTel to Grafana · per-tenant isolation · load tested
```

Three v1 decisions make this boring rather than a rewrite: repository Protocols (database
swap), the `EventBus` port (queue swap), and the `ChannelConnector` port (poll → push, and
new channels). **Nothing in the migration requires touching `services/`.**

## What I would do first with another two weeks

1. **Fine-tune on the collected edits.** The data pipeline exists and is populated by every
   human edit; this is the highest-leverage quality improvement available.
2. **Calibrate the confidence score.** Today the weights are heuristics — stated as such,
   never presented as probabilities. With a few thousand labelled outcomes, learn them.
3. **Postgres and containerization together.** One day of work that unblocks everything else.

## What I would not do

Add more components. The system is deliberately small: eleven parts, each with a
one-sentence justification. Every addition costs explainability, and explainability is
what makes the governance argument credible in the first place.
