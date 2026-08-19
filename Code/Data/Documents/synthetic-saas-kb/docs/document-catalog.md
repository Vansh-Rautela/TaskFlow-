# Document Catalog — AcmeFlow Knowledge Base

This catalog is the human-readable guide to every document in `knowledge_base/`.
It explains, one entry at a time, what each document establishes, which facts it
pins down, what worked examples it contains, and what kinds of customer
questions should retrieve it.

The source of truth for all company-wide facts is
`registry/document-registry.md`. This catalog never contradicts it.

## How to Use This Catalog

- **For RAG/retrieval engineers** — the *Retrieval cues* under each entry are
  example customer phrasings that should surface that document. They are
  illustrative, not exhaustive.
- **For reviewers** — the *Key facts pinned* column is a quick checklist to
  verify each document stays consistent with the registry and with the other
  documents.
- **For writers** — the *Type* field mirrors the front-matter
  `document_type`, so new documents can match the existing conventions.

Seven topic areas, 42 documents total:

| Area | Folder | Docs |
|---|---|---|
| Pricing & Plans | `knowledge_base/pricing/` | 7 |
| Billing & Payments | `knowledge_base/billing/` | 9 |
| Refunds & Credits | `knowledge_base/refunds/` | 6 |
| Cancellations & Account Management | `knowledge_base/cancellations/` | 6 |
| Invoices & Documentation | `knowledge_base/invoices/` | 5 |
| Enterprise & Custom Terms | `knowledge_base/enterprise/` | 5 |
| Troubleshooting | `knowledge_base/troubleshooting/` | 4 |

---

## Pricing & Plans

### KB-PRICING-001 — `plan-tiers-overview.md`

- **Type:** Billing Policy (entry point for pricing)
- **Purpose:** Introduces the three plans (Free, Pro, Enterprise), their pricing
  models, billing frequencies, support levels, and the major feature
  differences between tiers. This is the first document to land on for any
  "what plans exist / what do they cost" question.
- **Key facts pinned:**
  - Free: $0/month, never charged; up to 3 users; 2 active workflows; 500
    executions/month; community support; no SLA; no SSO/SAML; no custom invoices.
  - Pro: $24/user/month monthly, or $20/user/month effective rate billed
    annually in advance; unlimited workflows; up to 10,000 executions/month per
    workspace; email support; audit logs.
  - Enterprise: custom pricing per signed agreement, no published price;
    signed agreement takes precedence over self-service policy.
  - Monthly Pro renews same calendar day (or final day of month); annual Pro on
    anniversary. SLA only on Enterprise (standard target 99.9%).
- **Worked examples:** Free evaluation (Bright Spark Studio); Pro monthly 8
  seats = $192.00 (Northwind Labs); Enterprise example rate $18/user two-year
  150-seat commitment (Blue Harbor Logistics, labeled example).
- **Retrieval cues:** "What plans does AcmeFlow have?", "How much does AcmeFlow
  cost?", "Does the Free plan charge anything?", "What's the difference between
  your plans?"

### KB-PRICING-002 — `feature-matrix.md`

- **Type:** Billing Policy
- **Purpose:** Side-by-side feature comparison across Free / Pro / Enterprise,
  including limits (workflows, executions, seats), security, support, SLA, and
  billing features. Sets expectations when a customer is choosing a tier.
- **Key facts pinned:** full feature table (price, users, workflows,
  executions, permissions, audit logs, analytics, integrations, SSO/SAML, SCIM,
  support, SLA, custom invoices, billing frequency). Enterprise cells kept
  general — never quote an Enterprise feature as universal.
- **Worked examples:** Free vs Pro upgrade (Cedar Peak Consulting, 4 users =
  $96.00); Pro audit logs on 10 annual users = $2,400.00 (Meridian Health
  Group); Enterprise SSO/SAML/SLA capability (Ardent & Sons, labeled example).
- **Retrieval cues:** "What's included on each plan?", "Does Pro include
  SSO?", "Which plan has audit logs?", "Can I get custom invoices on Pro?"

### KB-PRICING-003 — `seat-limits-and-add-ons.md`

- **Type:** Billing Policy
- **Purpose:** Defines what a seat is, seat counts per plan, how additional
  seats are priced, mid-cycle proration for added seats, seat removal rules,
  minimum seats, and Enterprise seat commitments.
- **Key facts pinned:** seat = one active user; Free caps at 3 users with no
  add-ons (4th user requires Pro); Pro billed per user at the workspace's
  frequency; adding seats mid-cycle may generate a prorated charge (full rate
  from next renewal); removing seats affects future billing only (no automatic
  refund); no minimum seats on Free/Pro self-serve; Enterprise commitments are
  per agreement.
- **Worked examples:** Greenfield Media prorated seat add = $32.57 (2 seats,
  19/28 days); Cedar Peak Consulting seat removal (10 → 8 seats, next cycle
  $192.00); Blue Harbor 150-seat minimum commitment (labeled example).
- **Retrieval cues:** "How much to add a user?", "Can I add seats to the Free
  plan?", "Why was I prorated for new seats?", "Can I remove a user and get a
  refund?", "Is there a minimum number of seats?"

### KB-PRICING-004 — `annual-vs-monthly-pricing.md`

- **Type:** Billing Policy
- **Purpose:** Explains the two Pro billing frequencies, the effective annual
  rate, renewal timing, cost comparison, upgrade/downgrade behavior, and how to
  switch frequencies.
- **Key facts pinned:** monthly $24/user/month; annual billed in advance at
  $20/user/month effective ($240/user/year); monthly renewal on same calendar
  day or final day of month; annual on anniversary; monthly→annual = upgrade
  (immediate, may prorate); annual→monthly = downgrade (takes effect next cycle,
  no auto-refund); Enterprise frequency per agreement.
- **Worked examples:** Brightpath 10 annual seats = $2,400.00; Meridian switch
  monthly→annual mid-cycle; Greenfield switch annual→monthly (takes effect at
  anniversary).
- **Retrieval cues:** "Is annual billing cheaper?", "Can I switch from monthly
  to annual?", "When does my annual plan renew?", "Why am I charged once a year?"

### KB-PRICING-005 — `currency-and-regional-pricing.md`

- **Type:** Billing Policy
- **Purpose:** Covers supported currencies, workspace-level currency selection,
  regional availability, market-rate conversion, tax interaction, and
  Enterprise contract currency exceptions.
- **Key facts pinned:** supported set = USD, EUR, GBP, CAD, AUD, INR, JPY, SGD;
  currency is set at the workspace level; not every currency available in every
  region; no fixed universal conversion rate (card networks/processors apply
  market rates); no single universal tax rate; India examples use GST
  terminology; Enterprise agreements may set contract currency.
- **Worked examples:** RheinMetrik GmbH EUR billing; Koshur & Co. INR billing
  with GST line; Pacific Ridge Ltd. CAD contract currency (labeled example).
- **Retrieval cues:** "Do you bill in EUR?", "Can I change my billing
  currency?", "Why is my charge in a different currency?", "What currencies do
  you support?"

### KB-PRICING-006 — `upgrade-downgrade-rules.md`

- **Type:** Billing Policy
- **Purpose:** Defines when upgrades/downgrades take effect, how charges and
  proration behave, how feature access changes, and how seat changes follow the
  same rules.
- **Key facts pinned:** upgrade = immediate with possible proration; downgrade
  = start of next billing cycle (unused time not auto-refunded); feature
  reverting on downgrade; seat adds may prorate, seat removals affect future
  billing only; for annual plans "next cycle" = next anniversary; Enterprise
  exceptions per agreement.
- **Worked examples:** Meridian upgrade Free→Pro proration = $76.00 (5 seats,
  19/30 days); Ardent & Sons downgrade Pro→Free effective next cycle; Northwind
  seat add proration = $25.60 (2 seats, 16/30 days).
- **Retrieval cues:** "When does my upgrade take effect?", "Can I get a refund
  when I downgrade?", "What happens to Pro features if I downgrade to Free?",
  "Why is my upgrade charge prorated?"

### KB-PRICING-007 — `trial-period-terms.md`

- **Type:** Customer Help Center Article
- **Purpose:** Explains the standard 14-day Pro trial: what it includes, how
  conversion works, how to cancel before being charged, payment-method capture,
  and promotional/Enterprise exceptions.
- **Key facts pinned:** standard trial = 14 days of Pro features, no charge;
  converts automatically to the selected paid plan at trial end (monthly $24 or
  annual $20 effective); cancelling before conversion = no charge and revert to
  Free limits; capturing a payment method does not charge during the trial;
  other trial durations are only documented promotional or Enterprise
  exceptions.
- **Worked examples:** Kettlehouse & Co. conversion (6 seats = $144.00);
  Northwind Labs cancel before conversion; 30-day promotional trial example.
- **Retrieval cues:** "How long is the trial?", "Will I be charged after the
  trial?", "Can I cancel the trial without paying?", "Why is my card on file
  during the trial?"

---

## Billing & Payments

### KB-BILLING-001 — `supported-payment-methods.md`

- **Type:** Customer Help Center Article
- **Purpose:** Lists the payment methods AcmeFlow accepts, how availability is
  determined, how a customer sees their own options, and what to do when an
  expected method is not shown.
- **Key facts pinned:** credit cards (Visa, Mastercard, Amex, Discover where
  supported); debit cards where supported; ACH for eligible US customers;
  PayPal where enabled; wire transfer for qualifying Enterprise customers.
  Availability depends on plan, region, and eligibility — never imply every
  method is available to everyone. Descriptor is `ACMEFLOW`. ACH refunds
  7–10 business days, PayPal 5–7 business days.
- **Worked examples:** Pro workspace paying monthly with a Visa card ending in
  4821; US Pro annual workspace paying by ACH; PayPal authorization failure
  entering dunning.
- **Retrieval cues:** "What payment methods do you accept?", "Can I pay by
  ACH?", "Why don't I see PayPal as an option?", "Can my Enterprise account pay
  by wire transfer?"

### KB-BILLING-002 — `billing-cycle.md`

- **Type:** Billing Policy
- **Purpose:** Explains how billing cycles work: renewal dates, monthly vs
  annual cycles, how plan and seat changes affect the cycle, and billing
  contact notifications.
- **Key facts pinned:** monthly renews same calendar day as original
  subscription date (fallback: final day of the month); annual renews on
  anniversary; upgrade immediate with possible proration; downgrade next cycle;
  seat adds may prorate, removals affect future billing only; cycle dates do
  not reset on plan change; invoice notification emailed to billing contact.
- **Worked examples:** January 31 subscription billed February 28; annual plan
  starting March 15 renews March 15 next year; 8 monthly seats = $192.00.
- **Retrieval cues:** "When is my next renewal?", "Why was I billed on the last
  day of the month?", "When will I be charged each month?", "What does a billing
  cycle cover?"

### KB-BILLING-003 — `invoice-generation-and-delivery.md`

- **Type:** Customer Help Center Article
- **Purpose:** Explains when invoices are generated, how they are delivered,
  what they contain, where to find them, and the difference between invoices
  and receipts.
- **Key facts pinned:** invoices generated at each billing cycle close (also for
  prorations/seat changes); notification emailed to billing contact (no PDF by
  default); invoices available in Workspace Billing section; invoices contain
  base charge, prorations, seat changes, taxes, credits, number, period,
  address, payment method; invoices available for subscription lifetime;
  receipts confirm payment, invoices are the billing statement.
- **Worked examples:** mid-cycle upgrade 6→8 seats reflected as base + prorated
  line + tax; reading invoice AF-2026-004821 for 8 monthly seats.
- **Retrieval cues:** "Where can I find my invoices?", "How do I get an invoice
  email?", "Why don't I get a PDF invoice attached?", "When are invoices
  generated?"

### KB-BILLING-004 — `receipt-download-and-access.md`

- **Type:** Customer Help Center Article
- **Purpose:** Explains what a receipt shows, how to download one, receipt
  availability, multiple payments per cycle, and payment-method references on
  receipts.
- **Key facts pinned:** receipt issued for each payment, shows reference
  (`AF-RCPT-XXXXXX`), date, amount, currency, method, and related invoice;
  accessed from the invoice in Workspace Settings → Billing → Invoices;
  available as soon as the charge posts and for the subscription lifetime; a
  cycle can have multiple receipts (base, proration, dunning recovery); refunds
  get their own receipt.
- **Worked examples:** $192.00 payment receipt AF-RCPT-103482 linked to card
  ending in 4821; matching a `ACMEFLOW` statement line to a receipt.
- **Retrieval cues:** "How do I download a receipt?", "I need a receipt for my
  payment", "Why are there two receipts for one month?", "Can I get a receipt
  for a refund?"

### KB-BILLING-005 — `failed-payment-dunning.md`

- **Type:** Billing Policy
- **Purpose:** Defines the failed-payment lifecycle and the standard
  self-service schedule from first failure through retry, grace, past-due,
  restriction, and suspension.
- **Key facts pinned:** lifecycle steps (attempt → failure → notify → retry →
  update → grace → past-due → restriction/suspension); notified on first
  failure; automatic retries during grace period of up to 7 days from first
  failure; past-due if no valid method after grace; restriction then suspension
  typically around 14 days from first failure (approximate); updating the
  payment method during grace restarts collection; restriction/suspension do
  not cancel the subscription; agent must verify account state, never assume.
- **Worked examples:** $192.00 charge declined on cycle close, dunning walk
  through day 7 and day 14.
- **Retrieval cues:** "My payment failed — what happens next?", "Why is my
  account restricted?", "How long can I go without paying?", "I was suspended
  even though I updated my card."

### KB-BILLING-006 — `payment-method-update.md`

- **Type:** Customer Help Center Article
- **Purpose:** Explains how to add, update, or remove a payment method, when to
  do it, and how it interacts with the dunning process.
- **Key facts pinned:** steps in Workspace Settings → Billing → Payment Method;
  new method used for the next charge, no charge at update time; replacing a
  card (add, set default, remove old); pending retries use the valid method on
  file; update during grace period (up to 7 days) avoids past-due/suspension;
  availability depends on plan, region, eligibility.
- **Worked examples:** declined card 4821 replaced with 9034 and retry
  succeeds; failed $192.00 charge resolved on day 2 of grace.
- **Retrieval cues:** "How do I change my credit card?", "My card expired,
  what do I do?", "Can I switch to ACH?", "My payment failed — how do I fix it?"

### KB-BILLING-007 — `3ds-sca.md`

- **Type:** Customer Help Center Article
- **Purpose:** Explains 3D Secure / SCA authentication checks, when they appear,
  what to do if one interrupts a payment, and what they mean for support.
- **Key facts pinned:** 3DS/SCA is an extra cardholder verification step
  required by card issuers/regions; may apply on card add, cycle charge, or
  retry; controlled by issuer/processor, not AcmeFlow; completing the challenge
  then checking payment status; a 3DS check is not a decline by itself; if
  unresolved, standard dunning applies.
- **Worked examples:** new card 9034 approved in bank app; "disappeared"
  $192.00 charge explained by an uncompleted challenge.
- **Retrieval cues:** "I got a verification prompt from my bank", "My payment
  was blocked for security", "What is 3D Secure?", "Why do I need to approve
  charges?"

### KB-BILLING-008 — `tax-calculation.md`

- **Type:** Billing Policy
- **Purpose:** Explains how taxes are determined for AcmeFlow charges: which
  indirect taxes are supported, what factors drive them, how a tax registration
  is provided, and how tax appears on invoices.
- **Key facts pinned:** supports US sales tax, VAT, GST, and regional indirect
  taxes; tax depends on billing country, billing address, tax registration,
  customer tax status, jurisdiction; no single universal tax rate; tax shown as
  a separate invoice line item; India examples use GST terminology; tax
  calculated from billing address at invoice generation.
- **Worked examples:** India Pro workspace with GST line; US 8-seat workspace
  with sales tax on a $192.00 base.
- **Retrieval cues:** "Why is there tax on my invoice?", "Can I provide my VAT
  number?", "What tax rate applies to me?", "Why does my tax amount look wrong?"

### KB-BILLING-009 — `billing-address-changes.md`

- **Type:** Customer Help Center Article
- **Purpose:** Explains why the billing address matters, how to update it, how
  changes affect invoices, tax, payments, and country changes, and how billing
  address differs from billing contact.
- **Key facts pinned:** billing address used for invoice display, tax
  calculation, payment matching, compliance; update path in Workspace Settings →
  Billing; new address applies to invoices generated after the change (past
  invoices not re-issued); changing country can change currency, methods, and
  tax treatment; billing address ≠ billing contact.
- **Worked examples:** US workspace moving New York → Texas; workspace moving
  US → India with GST terminology.
- **Retrieval cues:** "How do I change my billing address?", "My invoice shows
  the wrong address", "I moved countries — what changes?", "Will changing my
  address change my tax?"

---

## Refunds & Credits

### KB-REFUND-001 — `standard-refund-policy.md`

- **Type:** Billing Policy
- **Purpose:** Defines when a charge is eligible for a standard refund and how
  the 30-day window is measured; establishes that cancellation does not create
  a refund.
- **Key facts pinned:** window = 30 days from the **original charge date** (not
  invoice open, subscription start, or bank clearing); cancellation does not
  create a refund; unused time not automatically refundable; eligible = Pro seat
  charges and prorated seat-add charges posted within 30 days; not eligible =
  charges over 30 days old, already refunded, tax treatment, Enterprise charges
  with different terms; refunds return to original method or become credit.
- **Worked examples:** request 17 days after charge = eligible (Northwind
  Consulting, $192.00); request 41 days after = outside window (Long Tail Labs).
- **Retrieval cues:** "I want a refund", "Can I get my money back?", "I was
  charged last month", "If I cancel, do I get a refund?"

### KB-REFUND-002 — `prorated-refund-calculation.md`

- **Type:** Billing Policy
- **Purpose:** Defines the prorated refund formula and when proration applies.
  Proration is the exception, not the default.
- **Key facts pinned:** formula `Eligible Unused Period ÷ Original Billing
  Period × Eligible Charge`; applies only where explicitly permitted (approved
  exception, Enterprise agreement, defined scenario); cancelling, seat removal,
  and downgrades never create prorated refunds on their own; assumptions: month
  = 30 days, year = 365 days, charge before tax, two-decimal rounding.
- **Worked examples:** monthly $120.00 charge, 15/30 days = $60.00 (Meridian
  Systems); annual $1,920.00 charge, 292/365 days = $1,536.00 (Blue River
  Analytics).
- **Retrieval cues:** "How is a prorated refund calculated?", "I want a partial
  refund for unused time", "Money back for the rest of my year?"

### KB-REFUND-003 — `refund-exception-approval.md`

- **Type:** Billing Policy
- **Purpose:** Governs refund/credit requests outside the standard policy and
  goodwill grants; requires appropriate approval.
- **Key facts pinned:** exceptions include late refunds, prorated refunds not
  otherwise permitted, partial refunds outside defined scenarios, goodwill
  credits; agents may not issue exceptions on their own; approval by a Billing
  Operations manager; higher-value and Enterprise exceptions escalated; approved
  exceptions recorded with reason; goodwill credits case-by-case; one approval
  does not entitle repeat exceptions.
- **Worked examples:** approved one-time $192.00 exception 41 days after charge
  (Long Tail Labs); goodwill credit of $96.00 after an invoice dispute
  (Cobalt & Co.).
- **Retrieval cues:** "I missed the 30-day window", "Can you make an
  exception?", "Will I get a goodwill credit?"

### KB-REFUND-004 — `credit-balance-application.md`

- **Type:** Billing Policy
- **Purpose:** Defines how credit balances are created, held, applied, and
  forfeited.
- **Key facts pinned:** credits from refunds or goodwill grants are held as a
  workspace credit balance; associated with the workspace, not a user or
  payment method; no cash-out value, not transferable, not exchangeable for a
  refund; applied automatically to future invoices in order of invoice
  generation; credits reduce amount due without changing the original charge
  date; balance forfeited on cancellation unless a contract says otherwise.
- **Worked examples:** $96.00 credit reduces a $192.00 invoice to $96.00
  (Cobalt & Co.); $120.00 credit applied across two successive invoices
  (Northwind Consulting); $96.00 forfeited on cancellation.
- **Retrieval cues:** "I have a credit — how is it used?", "Can I cash out my
  credit balance?", "Why was my credit applied here?", "What happens to my
  credit if I cancel?"

### KB-REFUND-005 — `refund-processing-timeframes.md`

- **Type:** Billing Policy
- **Purpose:** Describes typical refund appearance times by payment method;
  reinforces that these are estimates, not guarantees.
- **Key facts pinned:** cards 5–10 business days; PayPal 5–7 business days; ACH
  7–10 business days; wire (Enterprise) per agreement, may be 10–15 business
  days; counted in business days from when AcmeFlow processes the refund (not
  the request date); timing affected by issuer/bank processing and whether the
  original method is still valid.
- **Worked examples:** card refund processed Feb 3 typically appears Feb 9–16;
  ACH refund processed Mar 4 typically Mar 13–18; PayPal refund Apr 6 typically
  Apr 13–15.
- **Retrieval cues:** "When will I see my refund?", "How long do refunds take?",
  "Why hasn't my refund arrived yet?"

### KB-REFUND-006 — `partial-refund-scenarios.md`

- **Type:** Billing Policy
- **Purpose:** Clarifies when a partial refund may be issued and which common
  scenarios (seat removal, downgrade, cancellation) do **not** create one.
- **Key facts pinned:** partial refunds only where explicitly permitted
  (policy, exception, Enterprise agreement); scenarios that do not create a
  partial refund: removing seats, plan downgrade, cancellation; partial amount
  uses the prorated formula unless the agreement defines its own; partial
  refund covers only the eligible portion, remainder stays billed.
- **Worked examples:** downgrade with no partial refund (Meridian Systems);
  approved half-refund of $96.00 on a $192.00 charge (Cobalt & Co.); mid-cycle
  seat add then remove with no refund (Blue River Analytics).
- **Retrieval cues:** "Can I get a partial refund?", "I removed a user — do I
  get part of my money back?", "I downgraded — will I be refunded?"

---

## Cancellations & Account Management

### KB-CANCEL-001 — `self-serve-cancellation.md`

- **Type:** Customer Help Center Article
- **Purpose:** Walks through the self-serve cancellation flow, what happens
  after cancelling, and clarifies that cancellation is not a refund and not
  account deletion.
- **Key facts pinned:** path = Workspace Settings → Billing → Manage Subscription
  → Cancel Subscription → review → confirm; confirmation shown in Billing and
  emailed to the billing contact; subscription will not renew at the end of the
  current billing period; paid access continues to end of current period;
  cancellation does not create a refund; cancellation is not account deletion;
  if the option is missing, the account may be governed by an Enterprise
  agreement.
- **Worked examples:** Nordwind Logistics cancels June 2 on a monthly plan from
  the 15th — access through July 14, terminates July 15.
- **Retrieval cues:** "How do I cancel my subscription?", "Where is the cancel
  button?", "Can you cancel my plan for me?", "I can't find the cancel option."

### KB-CANCEL-002 — `cancellation-effective-date.md`

- **Type:** Billing Policy
- **Purpose:** Defines when cancellation takes effect, how access and billing
  behave during the current period, and interaction with downgrades and
  refunds.
- **Key facts pinned:** cancellation takes effect at the **end of the current
  billing period**, not the confirmation date; paid access continues until
  period end; monthly = current month, annual = current year; no prorated
  credit between confirmation and period end under standard policy; renewal
  dates align to the monthly same-day / final-day rule; annual cancellation
  stops the next anniversary charge.
- **Worked examples:** cancelling June 18 on a June 1–30 cycle stops access
  July 1; annual workspace charged $2,400 on Jan 15 cancelled Sep 3 keeps access
  through Jan 14, no next renewal.
- **Retrieval cues:** "When does my cancellation take effect?", "Do I lose
  access immediately?", "Will I be charged again after I cancel?", "Do I get
  credit for the rest of the month?"

### KB-CANCEL-003 — `data-retention-after-cancellation.md`

- **Type:** Billing Policy
- **Purpose:** Defines the 60-day data retention window after subscription
  termination, what it covers, and what happens after it ends.
- **Key facts pinned:** workspace data retained 60 days from subscription
  termination (end of current billing period for self-serve); retention covers
  workflows, configurations, associated data; deletion after the window may be
  irreversible; cancellation ≠ deletion; reactivating within the window restores
  data; Enterprise contracts may define different retention periods; agents must
  retrieve actual termination date rather than answer from memory.
- **Worked examples:** monthly workspace terminating July 15 retained through
  ~September 13; export on August 1.
- **Retrieval cues:** "How long do you keep my data after I cancel?", "Can I
  get my data back?", "When will my data be deleted?", "Can you restore my old
  workspace?"

### KB-CANCEL-004 — `account-deletion-vs-subscription-cancellation.md`

- **Type:** Customer Help Center Article
- **Purpose:** Distinguishes cancellation (stops renewal, keeps data) from
  account deletion (removes the account and data, irreversible) and gives the
  recommended order of actions.
- **Key facts pinned:** cancelling stops renewal and keeps workspace/data;
  deleting closes the account and removes data permanently; data retained 60
  days after termination; recommended order: cancel → export → delete; deletion
  after retention may be irreversible; agents must retrieve actual termination
  and deletion status, never guess about recovery.
- **Worked examples:** Bluepeak Design cancels but keeps the workspace;
  Harbor & Co. cancels, exports, deletes.
- **Retrieval cues:** "Difference between cancelling and deleting?", "I want to
  close my account completely", "How do I delete my workspace?", "I deleted my
  account by accident — can I get it back?"

### KB-CANCEL-005 — `reactivation-and-price-locking.md`

- **Type:** Billing Policy
- **Purpose:** Defines how a customer returns to a paid plan after
  cancellation, when data is preserved, and when the previous per-user price is
  locked.
- **Key facts pinned:** reactivation restores paid access and, within the
  retention window, restores retained data; price lock = re-purchase Pro within
  60 days of cancellation at the previous per-user price; monthly lock holds the
  monthly per-user price, annual lock holds the effective annual rate; lock
  applies only to Pro; more than 60 days → current standard pricing; price lock
  does not create a refund; 60-day lock aligns with the 60-day retention window.
- **Worked examples:** Northwind Logistics re-purchases 8 users within 60 days
  at $24/user/month; Meridian Studio annual re-purchase locked at $20 effective.
- **Retrieval cues:** "Can I come back after cancelling?", "Do I keep my old
  price?", "Will my data still be there if I reactivate?", "How long is the
  price lock?"

### KB-CANCEL-006 — `data-export-before-cancellation.md`

- **Type:** Customer Help Center Article
- **Purpose:** Explains why customers should export data before cancelling or
  deleting, what can be exported, how to export, and the recommended order.
- **Key facts pinned:** data retained 60 days but not forever; export is the
  only way to keep your own copy; cancellation does not automatically produce an
  export; export options depend on plan (confirm per workspace); recommended
  order: cancel → export → delete; export before deletion, not after; agents
  must not fabricate account-specific details about recovery or exports.
- **Worked examples:** Ridgefield Accounting exports workflows/reports before
  cancelling; Cascade Goods workflow unrecoverable after retention window ended.
- **Retrieval cues:** "How do I export my data?", "What data can I export
  before cancelling?", "Can I recover data after deleting?", "I need a backup
  of my workflows."

---

## Invoices & Documentation

### KB-INVOICE-001 — `invoice-line-items.md`

- **Type:** Billing Policy
- **Purpose:** Explains how an invoice is structured and what each line item
  represents, for customers and for support/billing staff verifying charges.
- **Key facts pinned:** invoice ID format `AF-2026-XXXXXX`; receipt references
  `AF-RCPT-XXXXXX` / `ORD-XXXXXXXX`; line items = base charge, prorations, seat
  changes, taxes, credits; base charge for Pro = $24/user/month monthly or $20
  effective annual; Free = $0 and no invoices; proration uses a daily per-seat
  rate ($24 ÷ 30 = $0.80/seat/day in the example); credits appear as negative
  line items; total = base ± prorations + taxes − credits; invoice rendered in
  workspace billing currency; agents verify line items against the actual
  invoice, never from memory.
- **Worked examples:** March invoice AF-2026-004821 with base $192.00, prorated
  2-seat add $32.00, tax, total $240.80; annual invoice with $50.00 credit;
  seat removal affecting the next cycle.
- **Retrieval cues:** "Why is my total different from seat count × price?",
  "What is this prorated line?", "What does this invoice line mean?", "Why was
  tax added?"

### KB-INVOICE-002 — `enterprise-custom-invoice-requirements.md`

- **Type:** Enterprise Policy
- **Purpose:** Defines how custom invoices work for Enterprise workspaces:
  required information, PO/remittance handling, net payment terms, custom
  billing periods, and contract currency.
- **Key facts pinned:** custom invoices apply only to Enterprise workspaces
  whose agreement includes custom invoicing; required info = invoice ID, AcmeFlow
  Inc., customer legal entity/address, agreement reference, PO number, line
  items, net terms/due date, contract currency; net terms (e.g. net 30/45)
  replace automatic card charges; annual and quarterly billing per agreement;
  contract currency may differ from workspace currency; no fixed universal
  conversion rate; signed agreement takes precedence.
- **Worked examples:** quarterly invoice with PO-88213 and Net 30 at an example
  $18/user/month for 25 committed seats = $1,350.00; annual EUR invoice for an
  example €48,000.00 contract.
- **Retrieval cues:** "Can you make an invoice for my procurement team?",
  "We need net 30 terms", "Our invoice must show our PO number", "We bill in a
  different currency."

### KB-INVOICE-003 — `purchase-order-numbers.md`

- **Type:** Billing Policy
- **Purpose:** Explains how PO numbers work on invoices, when one appears, how
  to provide or update it, and how PO references support remittance matching.
- **Key facts pinned:** PO number prints on invoices generated after it is
  saved; it does not change what is billed; add/update via Workspace Settings →
  Billing; existing invoices keep the reference they were created with;
  Enterprise POs provided via billing contact or account manager; include PO
  reference with wire payments to speed matching; Free workspaces need no PO.
- **Worked examples:** Brightpath Logistics PO-2026-8841 on monthly invoice
  AF-2026-005812; Northgate Manufacturing PO-88213 on quarterly invoice
  AF-2026-002517.
- **Retrieval cues:** "How do I add a PO number to my invoice?", "My invoice is
  missing the PO number", "Do I need a purchase order?", "How do I match my
  payment to an invoice?"

### KB-INVOICE-004 — `billing-contact-updates.md`

- **Type:** Customer Help Center Article
- **Purpose:** Explains what a billing contact is, how to change it, and what to
  expect after the change.
- **Key facts pinned:** billing contact receives invoice notification emails;
  separate from admins and from the billing address; managed in Workspace
  Settings → Billing; needs permission to change billing settings; new contact
  used for notifications going forward; past invoices are not re-sent (available
  in the Billing section); a change near a renewal may still notify the old
  address for that cycle.
- **Worked examples:** Brightpath moves invoices from finance@ to
  billing@brightpath.example; Northwind updates the contact in May before a
  June 1 annual renewal.
- **Retrieval cues:** "Who gets the invoice emails?", "How do I change the
  billing contact?", "I'm not receiving invoice notifications", "Can past
  invoices be emailed to someone new?"

### KB-INVOICE-005 — `invoice-disputes.md`

- **Type:** Support Runbook
- **Purpose:** Internal runbook for handling a customer dispute of an invoice or
  charge: triage, diagnostics, verification, common causes, escalation, and
  resolution.
- **Key facts pinned:** never confirm/dismiss from memory — verify against the
  workspace's invoice and payment records; ask for invoice ID or receipt
  reference; classify the dispute type; sum line items to reconcile the total;
  verify plan math ($24 monthly / $20 effective annual, e.g. 8 seats = $192.00);
  Enterprise verified against the signed agreement; tax verified against
  jurisdiction details; escalation criteria include unreconcilable invoices,
  Enterprise terms, out-of-window refunds, goodwill credits, repeated disputes,
  and suspected system errors; refunds/credits follow the refund policy, not the
  dispute itself.
- **Worked examples:** "duplicate charge" resolved as two different cycles
  (AF-2026-004821 vs AF-2026-004822); disputed proration explained by a dated
  seat addition.
- **Retrieval cues:** "This invoice is wrong", "I was double-charged", "Why is
  this charge on my statement?", "My proration doesn't look right." (retrieves
  together with the troubleshooting runbooks)

---

## Enterprise & Custom Terms

### KB-ENT-001 — `enterprise-contract-billing.md`

- **Type:** Enterprise Policy
- **Purpose:** Foundation document for Enterprise accounts: pricing is custom,
  billing and payment terms come from the signed agreement, and the agreement
  overrides self-service policy wherever they differ.
- **Key facts pinned:** no published universal Enterprise price; agreements may
  include volume discounts, seat commitments, annual/quarterly cycles, POs and
  custom invoices, net terms, refund terms, SLA/uptime credits, SSO/SAML/SCIM,
  dedicated account manager, security reviews; agents must retrieve contract
  price, billing cycle, seat commitments, payment terms, refund/credit/retention
  terms, and invoice/PO requirements from the agreement; if the agreement is
  silent, standard policy is the default and Billing Operations confirms.
- **Worked examples (all labeled):** BlueSky Analytics example rate $18/user/
  month for 150 committed seats billed annually; Meridian Health Partners
  quarterly billing with Net 30 and wire transfer; Lumina Financial Solutions
  90-day retention override.
- **Retrieval cues:** "What does our contract say about billing?", "We're on an
  Enterprise contract — how are we billed?", "Does our agreement have net
  terms?", "Can you confirm our contract pricing?"

### KB-ENT-002 — `volume-discount-tiers.md`

- **Type:** Enterprise Policy
- **Purpose:** Explains how volume discounts are structured and why there is no
  universal tier schedule.
- **Key facts pinned:** volume discounts are negotiated in the signed agreement
  (discount table); structures vary: stepped seat thresholds, annual
  commitment minimums, base-charge vs seat-add-on discounts, one-time rates;
  AcmeFlow maintains no fixed threshold schedule; discount figures come from the
  agreement or are labeled examples; discounts may be locked for the term and
  conditioned on a minimum committed seat count; no volume-discount provision →
  contracted rate without adjustment.
- **Worked examples (labeled):** Optivus Manufacturing 5% at 200 seats and 10%
  at 500 seats (MSAA-2026-0551); 220 committed seats keeping the 5% discount,
  reverting if below 200.
- **Retrieval cues:** "Do we get a discount at a certain seat count?", "What
  volume discount applies to us?", "Is there a standard discount schedule?",
  "Why doesn't my invoice show a discount?"

### KB-ENT-003 — `dedicated-account-manager.md`

- **Type:** Enterprise Policy
- **Purpose:** Describes the dedicated account manager (DAM) role where the
  agreement provides for it, and how support agents route work on these
  accounts.
- **Key facts pinned:** DAM is a single point of contact for onboarding,
  adoption, and operational coordination; scope is set by the agreement, not a
  standard package; DAM does not replace support channels for incidents,
  disputes, and product issues; agents should check for a DAM, coordinate before
  committing to billing/seat/contract changes, and involve the DAM for
  escalations and renewals.
- **Worked examples (labeled):** BlueSky's DAM leads quarterly business reviews;
  Meridian's DAM covers onboarding and renewal only.
- **Retrieval cues:** "Who is our account manager?", "Can I speak to our
  account team?", "Who handles our renewal?", "Escalate this to our account
  manager."

### KB-ENT-004 — `sla-uptime-credits.md`

- **Type:** Enterprise Policy
- **Purpose:** Explains the SLA structure, the 99.9% standard target, how uptime
  is measured, and how service credits for missed uptime are handled.
- **Key facts pinned:** standard Enterprise target = 99.9% monthly uptime; self-
  service plans (Free/Pro) have no SLA; downtime measured in whole minutes;
  scheduled maintenance and force-majeure excluded per agreement; service credit
  rates are per agreement, never universal; credits may be applied to the credit
  balance or a future invoice; agents must retrieve the target, exclusions,
  credit rate, and claim process from the agreement; no signed SLA → no credits.
- **Worked examples (labeled):** Meridian 99.9% target; Optivus tighter 99.95%;
  BlueSky example 5% monthly credit rate; Meridian 45-minute outage credit
  example.
- **Retrieval cues:** "What is our SLA?", "We had an outage — do we get a
  credit?", "What's your uptime guarantee?", "How are uptime credits
  calculated?"

### KB-ENT-005 — `security-questionnaire-soc2.md`

- **Type:** Enterprise Policy
- **Purpose:** Explains how security questionnaires and SOC 2 documentation
  requests are handled as part of Enterprise due diligence.
- **Key facts pinned:** security reviews cover data handling, access control,
  audit controls, subprocessors, incident response; questionnaires coordinated
  through the account team (DAM primary or Enterprise Operations); SOC 2
  documentation shared through a controlled channel under confidentiality
  obligations, never posted publicly; agents confirm Enterprise agreement
  coverage, coordinate through DAM/Enterprise Ops, and never forward SOC 2
  reports or completed questionnaires from standard support channels.
- **Worked examples (labeled):** Northwind Logistics questionnaire during
  renewal of MSAA-2026-0833; Meridian Health Partners SOC 2 request under an
  evaluation agreement's confidentiality terms.
- **Retrieval cues:** "Do you have a SOC 2 report?", "We need to send you a
  security questionnaire", "Can you fill out our vendor assessment?", "Where do
  I request security documentation?"

---

## Troubleshooting

### KB-TROUBLE-001 — `why-was-i-charged.md`

- **Type:** Support Runbook
- **Purpose:** Ordered investigation of an unexpected charge: identify the
  charge, classify it, check cycle/seat/plan/tax/balance/math, explain, and
  escalate when needed.
- **Key facts pinned:** every conclusion grounded in records, never the
  customer's description alone; requires an invoice ID before the investigation
  starts; classification categories (recurring, renewal, prorated upgrade,
  additional seat, tax, usage, one-time Enterprise, credit reversal); checks in
  order — billing cycle, seat changes, plan changes, proration, tax, previous
  balance and credits, math ($24 monthly, e.g. 8 seats = $192.00; Free never
  charged); escalation criteria (unreconcilable, currency mismatch beyond market
  rate, suspected duplicate, out-of-window refunds, Enterprise terms unclear,
  contested tax).
- **Worked examples:** prorated 2-seat addition (Nimbus Logistics, +$30.40);
  previous balance collected with renewal after dunning (Apex Studio).
- **Retrieval cues:** "Why was I charged this month?", "I didn't expect this
  charge", "There's an extra amount on my invoice", "Why is my card being
  charged again?"

### KB-TROUBLE-002 — `double-charge-investigation.md`

- **Type:** Support Runbook
- **Purpose:** Determines whether a customer was genuinely charged twice, whether
  one entry is a pending authorization or pre-authorization, whether the charges
  are from different billing periods, or whether Enterprise split billing
  applies.
- **Key facts pinned:** genuine duplicate = two distinct settled charges for the
  same invoice or covered period; one settled + one pending is not a double
  charge; pending authorizations can sit for several days and may fall off;
  pre-authorizations not settled are released by the issuer and need no refund;
  overlapping cycles (failed month + current renewal settling together) are not
  duplicates; Enterprise split billing is by design; document the final
  classification.
- **Worked examples:** settled charge + pending authorization matching no
  invoice; Blue Oak Media's January and February invoices settling a day apart.
- **Retrieval cues:** "I was charged twice!", "There are two charges on my
  card", "Why do I have two charges for the same amount?", "Is this a duplicate
  charge?"

### KB-TROUBLE-003 — `currency-conversion-discrepancies.md`

- **Type:** Support Runbook
- **Purpose:** Investigates why a charge in the card currency differs from the
  workspace currency amount; explains conversion timing and processor/bank fees.
- **Key facts pinned:** workspace amount is in workspace currency; bank charges
  in card currency; no fixed universal conversion rate (market rates); a
  difference alone is not a discrepancy; if card and workspace currency are the
  same, a difference points to bank/processor fees, not conversion; 3D Secure /
  SCA is a timing factor, not a cause; authorization vs settlement rates can
  differ; escalate only when the difference exceeds a market rate + reasonable
  fees, or a contract currency term is violated.
- **Worked examples:** EUR card on a USD invoice (Harborline, $192.00 vs
  €176.20); GBP card on a GBP invoice with a £2.94 bank fee (Kitsune Labs).
- **Retrieval cues:** "Why is my charge different from the invoice?", "The
  currency conversion looks wrong", "There's a foreign transaction fee on my
  card", "The amount on my statement doesn't match."

### KB-TROUBLE-004 — `bank-statement-descriptor-mismatch.md`

- **Type:** Support Runbook
- **Purpose:** Investigates customers who don't recognize an AcmeFlow charge on
  their bank statement; confirms the charge is AcmeFlow's before anything else.
- **Key facts pinned:** descriptor is `ACMEFLOW`; legal entity is AcmeFlow Inc.;
  descriptor is a short processor label that can differ from the full company
  name and may be truncated/reformatted by banks; never assume an unrecognized
  descriptor is not an AcmeFlow charge; verification requires `ACMEFLOW` text OR
  matching amount + date + card last four digits against an invoice; workspace
  name is not part of the descriptor; escalation for no match, wrong merchant,
  Free plan charge, or chargeback risk.
- **Worked examples:** Cedar & Pine Design matching `ACMEFLOW` by card ending
  in 4012 and invoice AF-2026-003901; Polaris Ventures truncated descriptor
  matched by amount/date/card.
- **Retrieval cues:** "I don't recognize this charge on my statement", "What is
  this ACMEFLOW charge?", "My statement shows a different name", "Is this charge
  from you?"

---

*42 documents cataloged. Facts and figures are consistent with
`registry/document-registry.md` (effective date 2026-01-01, reviewed
2026-07-01). Any Enterprise figure referenced here is a labeled example, not a
published price.*