# Synthetic SaaS Knowledge Base — AcmeFlow

A realistic, consistent, **synthetic company knowledge base** for the fictional
B2B SaaS company **AcmeFlow** (product: **AcmeFlow Workspace**), built as the RAG
corpus for a customer-support POC.

The corpus is designed to look and read like real documentation a SaaS company
would publish — not a synthetic retrieval benchmark. It is paired with a
separate, machine-readable evaluation dataset so a RAG system can be measured
objectively.

---

## Table of contents

1. [What's in this project](#1-whats-in-this-project)
2. [The fictional company](#2-the-fictional-company)
3. [Knowledge base design principles](#3-knowledge-base-design-principles)
4. [Document catalog](#4-document-catalog)
5. [Evaluation dataset](#5-evaluation-dataset)
6. [Suggested POC pipeline](#6-suggested-poc-pipeline)
7. [Consistency guarantees](#7-consistency-guarantees)

---

## 1. What's in this project

```text
synthetic-saas-kb/
├── knowledge_base/            ← the RAG corpus (Markdown, one authoritative doc per topic)
│   ├── pricing/               ← 7 documents
│   ├── billing/               ← 9 documents
│   ├── refunds/               ← 6 documents
│   ├── cancellations/         ← 6 documents
│   ├── invoices/              ← 5 documents
│   ├── enterprise/            ← 5 documents
│   └── troubleshooting/       ← 4 internal support runbooks
│
├── docs/
│   └── document-catalog.md    ← in-depth guide to every document (what it pins, examples, retrieval cues)
│
├── evaluation/                ← machine-readable ground truth (JSONL)
│   ├── tier-1.jsonl           ← 126 direct queries
│   ├── tier-2.jsonl           ← 126 conditional / boundary queries
│   ├── tier-3.jsonl           ← 57 ambiguous queries (clarification required)
│   ├── tier-4.jsonl           ← 42 multi-turn threads
│   └── adversarial.jsonl      ← 127 adversarial & negative queries
│
├── queries/                   ← human-readable copy of the queries (Markdown)
│   ├── tier-1.md  tier-2.md  tier-3.md  tier-4.md  adversarial.md
│
└── registry/
    └── document-registry.md   ← single source of truth: company facts + document IDs
```

**Totals: 42 authoritative documents, 478 evaluation queries.**

| Area | Folder | Docs |
|---|---|---|
| Pricing & Plans | `knowledge_base/pricing/` | 7 |
| Billing & Payments | `knowledge_base/billing/` | 9 |
| Refunds & Credits | `knowledge_base/refunds/` | 6 |
| Cancellations & Account Management | `knowledge_base/cancellations/` | 6 |
| Invoices & Documentation | `knowledge_base/invoices/` | 5 |
| Enterprise & Custom Terms | `knowledge_base/enterprise/` | 5 |
| Troubleshooting | `knowledge_base/troubleshooting/` | 4 |

## 2. The fictional company

| | |
|---|---|
| Company | AcmeFlow (legal entity: AcmeFlow Inc.) |
| Product | AcmeFlow Workspace — workflow automation & team productivity |
| Segment | Startups → SMB → mid-market → enterprise |
| Statement descriptor | `ACMEFLOW` |

### Plans at a glance

| | Free | Pro | Enterprise |
|---|---|---|---|
| Price | $0 / mo | $24 / user / mo; $20 effective annual | Custom (per agreement) |
| Users | up to 3 | per seat | per agreement |
| Workflows | 2 active | Unlimited | Unlimited |
| Executions / mo | 500 | up to 10,000 / workspace | per agreement |
| Support | Community | Email | Dedicated AM |
| SLA / SSO / custom invoices | No | No / No / No | Optional per agreement |

### Pinned facts (excerpt — full list in the registry)

- **Trial:** 14 days (Pro), converts to the selected paid plan.
- **Refund:** 30 days from the original charge; cancellation ≠ refund.
- **Retention:** 60 days after subscription termination.
- **Monthly renewal:** same calendar day (last day of month if that day doesn't exist).
- **Upgrades** immediate (prorated); **downgrades** effective next cycle.
- **Dunning:** notify on first failure → retries ≤ 7-day grace → past-due → restriction/suspension ~14 days.
- **Payment methods:** cards, ACH (eligible US), PayPal (where enabled), wire (qualifying Enterprise).
- **Enterprise override:** the signed agreement takes precedence where it differs.

## 3. Knowledge base design principles

1. **One authoritative document per topic.** No near-duplicate articles. Query
   diversity lives in the evaluation set, not in duplicated documents.
2. **Real document types.** Help Center articles, billing policies, enterprise
   policies, and internal support runbooks — each written in the style a real
   company would use.
3. **Explicit facts.** Documents state numbers, dates, and conditions directly so
   the retriever can surface the exact fact a query needs.
4. **Chunk-friendly sections.** Meaningful `##` sections that stay self-contained
   when chunked; no walls of text. Chunking decisions are left to the ingestion
   pipeline.
5. **No evaluation leakage.** No ground-truth labels, complexity tiers, or
   retrieval hints inside any knowledge-base document.
6. **No fabricated account data.** Documents explain *what an agent must
   retrieve* (invoice ID, charge date, amount, plan, seats, payment status)
   instead of inventing customer transactions.
7. **Enterprise terms are per-agreement.** Any number is explicitly labeled as an
   example; no universal Enterprise price, discount, credit, or tax rate.

## 4. Document catalog

For a readable, in-depth walkthrough of every document — what each one
establishes, which facts it pins, its worked examples, and what customer
phrasings should retrieve it — open:

**`docs/document-catalog.md`**

It covers all 42 documents across the 7 topic areas, grouped by section, and is
kept consistent with `registry/document-registry.md`.

## 5. Evaluation dataset

Every query is generated **from the actual documents** and carries ground truth:

```json
{
  "query_id": "Q-BILL-001",
  "query": "How do I download my invoice?",
  "complexity_tier": 1,
  "expected_intent": "invoice_download",
  "expected_routing": "answer",
  "ground_truth_documents": ["KB-INVOICE-001"],
  "required_facts": ["invoice location", "download procedure"],
  "requires_account_lookup": false,
  "requires_thread_context": false,
  "requires_human_review": false,
  "potential_negative_documents": ["KB-BILLING-003"],
  "missing_information": null
}
```

- **Tier 1 — Direct:** answerable straight from one document (many paraphrases, terminology variants).
- **Tier 2 — Conditional:** requires applying a policy — boundary cases, exceptions, proration math.
- **Tier 3 — Ambiguous:** missing critical information; correct behavior is *clarification*, not guessing (`expected_routing: "clarify"`, `missing_information` populated).
- **Tier 4 — Multi-turn:** the final message is not answerable without prior thread context (`requires_thread_context: true`).
- **Adversarial:** keyword overlap, negation, temporal language, ambiguous references, contradictory requests, and misrouted/out-of-scope queries (empty ground truth, routing `out_of_scope`).

Query text is deliberately messy and human: typos, grammar slips, non-native
English, frustrated and polite language, short messages, long explanations,
relative and exact dates, amounts, card-ending digits, seat counts, and plan names.

## 6. Suggested POC pipeline

```text
knowledge_base/*.md
      │
      ▼
  Chunk (by section) ──▶ Embed ──▶ Qdrant
      │
      ▼
  Customer query ──▶ RAG retrieval ──▶ Rerank ──▶ Draft
      │                                       │
      └──── evaluation/*.jsonl ──▶ measure    ┘
```

1. Ingest `knowledge_base/**/*.md`.
2. Chunk on `##` section boundaries (YAML front matter can be stripped or kept as metadata).
3. Embed and store chunks in Qdrant, keeping `document_id` and section headers as payload.
4. Retrieve against `evaluation/*.jsonl` queries; score hits against `ground_truth_documents`.
5. For Tier 3, evaluate whether the system asks a clarifying question; for Tier 4, whether it uses thread context; for adversarial/misrouted queries, whether it refuses or redirects instead of answering.

## 7. Consistency guarantees

All documents were checked against `registry/document-registry.md`:

- Identical plan prices, trial (14d), refund window (30d), retention (60d), dunning, and cancellation rules across all 42 documents.
- All 42 cross-references ("Related Documentation") resolve to real documents.
- All document IDs are unique and match the registry.
- All 478 evaluation queries reference only valid document IDs.
- No evaluation labels, ground-truth IDs, or retrieval hints appear inside any knowledge-base document.
- Every synthetic example uses fictional companies, invoice IDs (`AF-2026-XXXXXX`), and mathematically correct amounts.
- The document catalog (`docs/document-catalog.md`) matches the registry's facts and document IDs.