# AcmeFlow Knowledge Base — Company Fact & Document Registry

This file is the single source of truth for AcmeFlow company-wide facts.
Every document in `knowledge_base/` MUST be consistent with this registry.
If a new document requires a new company-wide fact, update this registry **first**,
then use that fact consistently everywhere.

---

## 1. Company Identity

| Fact | Value |
|---|---|
| Company name | AcmeFlow |
| Legal entity (invoices) | AcmeFlow Inc. |
| Product | AcmeFlow Workspace |
| Industry | B2B SaaS — workflow automation & team productivity |
| Product category | Workflow automation, project management, approvals, integrations, reporting, APIs |
| Customer segments | Startups, small businesses, mid-market, enterprise |
| Bank statement descriptor | `ACMEFLOW` |
| Billing/support email (support agent only) | billing@acmeflow.example |

## 2. Plans

### Free
- **$0 / month** (never charged)
- Up to **3 users**
- **2 active workflows**
- **500 workflow executions / month**
- Community support
- Standard integrations
- No SLA
- No SSO/SAML
- No custom invoices

### Pro
- Monthly billing: **$24 per user / month**
- Annual billing: **$20 per user / month** (effective rate, billed annually in advance)
- Unlimited workflows
- Advanced permissions
- Audit logs
- Standard integrations
- Email support
- Standard analytics
- Up to **10,000 workflow executions / month per workspace**

### Enterprise
- **Custom pricing — never invent a universal price.**
- May include: volume discounts, contract-specific seat commitments, annual or
  quarterly billing, purchase orders, custom invoices, SSO/SAML, SCIM,
  advanced audit controls, dedicated account manager, custom SLA, security
  reviews, contract-specific payment terms.
- If a synthetic example needs a number, it MUST be labeled explicitly as an
  example, never as a published/standard price.

## 3. Billing Rules

| Rule | Value |
|---|---|
| Monthly renewal | Same calendar day as original subscription date; if that day does not exist in a month, bill on the final day of that month. |
| Annual renewal | Anniversary date. |
| Plan upgrade | Takes effect immediately; additional charges may be prorated. |
| Plan downgrade | Takes effect at the start of the next billing cycle; unused time is not automatically refunded unless a policy explicitly allows it. |
| Adding seats | During an active cycle may generate a prorated charge. |
| Removing seats | Normally affects future billing only. |
| Enterprise override | Signed Enterprise agreement takes precedence over standard self-service rules where the two differ. |

## 4. Trial

| Fact | Value |
|---|---|
| Standard Pro trial | **14 days** |
| Conversion | Converts to the selected paid subscription at the end of the trial per signup terms. |
| Cancellation | Customer may cancel before conversion (no charge). |
| Other durations | Only describe as a documented Enterprise or promotional exception — never as standard. |

## 5. Refunds

| Fact | Value |
|---|---|
| Standard refund window | **30 days from the original charge** |
| Cancellation ≠ refund | Cancelling does not automatically create a refund. |
| Monthly unused time | Not automatically refundable. |
| Prorated refunds | Only where the applicable policy explicitly permits them. |
| Exceptions | Require appropriate approval (see refund-exception-approval.md). |
| Enterprise | Contracts may contain different refund terms; signed agreement takes precedence. |
| Refund formula | `Refund Amount = Eligible Unused Period ÷ Original Billing Period × Eligible Charge` |

## 6. Cancellation & Data Retention

| Fact | Value |
|---|---|
| Self-serve path | Workspace Settings → Billing → Manage Subscription → Cancel Subscription → review details → confirm |
| Effect | Prevents future renewal. |
| Access after cancel | Paid access continues until the end of the current billing period. |
| Cancellation vs deletion | Cancellation is different from account deletion. |
| Data retention | Workspace data retained **60 days after subscription termination**. |
| Data export | Customers should export required data before deletion. |
| Post-retention deletion | May be irreversible. |
| Enterprise | Contracts may define different retention periods. |

## 7. Payment Methods

Supported (availability depends on plan, region, and eligibility):

- Credit cards (Visa, Mastercard, American Express, Discover where supported)
- Debit cards where supported
- ACH (eligible US customers)
- PayPal where enabled
- Wire transfer (qualifying Enterprise customers)

Never imply every method is available to every plan/customer/region.

## 8. Taxes

- Supports US sales tax, VAT, GST, and regional indirect taxes.
- Treatment depends on: billing country, billing address, tax registration,
  customer tax status, applicable jurisdiction.
- No single universal tax rate.
- India examples use **GST** terminology; never invent a universal GST percentage
  unless a document explicitly uses a labeled synthetic example.

## 9. Failed Payments / Dunning

Lifecycle:

```
Payment Attempt → Payment Failure → Customer Notification → Automatic Retry
→ Payment Method Update → Additional Retry / Grace Period → Past-Due State
→ Restriction / Suspension
```

Standard (self-service) schedule, defined in KB-BILLING-005:

- Customer notified on first failure.
- Automatic retries continue during a grace period of up to **7 days** from the
  first failure.
- If no valid payment method is available after the grace period, the
  subscription enters a **past-due** state.
- Continued non-payment may lead to **restriction then suspension**, typically
  around **14 days** from the first failure (approximate; subject to plan and
  agreement).
- Enterprise agreements may define different schedules.

Exact retry timings are documented only where the relevant document defines them.

## 9a. Credits

- Credits created by a refund or goodwill grant are held as a **workspace credit
  balance**.
- Applied automatically to future invoices, in order of invoice generation.
- Non-transferable, no cash-out value, and not exchangeable for a refund.
- If a subscription is cancelled, any remaining credit balance is forfeited
  unless a contract says otherwise.

## 9b. Refund Processing Timeframes

- Credit/debit card refunds: typically **5–10 business days** to appear,
  depending on the card issuer.
- PayPal refunds: typically **5–7 business days**.
- ACH: typically **7–10 business days**.
- Wire transfers (Enterprise): per agreement; may be **10–15 business days**.
- Timeframes are estimates; the agent must not guarantee exact dates.

## 10. Currencies & Regional

| Fact | Value |
|---|---|
| Supported currencies | USD, EUR, GBP, CAD, AUD, INR, JPY, SGD (minimum set used across the KB) |
| Currency selection | Set at the workspace level; not every currency is available in every region. |
| Conversion | No fixed universal conversion rate; card networks / payment processors apply market rates. |
| Enterprise exceptions | Enterprise agreements may define contract currency and rates. |

## 11. Enterprise Override

> The customer's signed Enterprise agreement takes precedence over the standard
> self-service policy where the two differ.

## 11a. SLA Facts

- Standard Enterprise SLA target: **99.9% monthly uptime** for AcmeFlow Workspace.
- Service credits for missed uptime are defined **per agreement** (never invent a
  universal credit percentage without labeling it as an example).
- Self-service plans (Free/Pro) have **no SLA**.
- Downtime measured in whole minutes; scheduled maintenance and force-majeure
  are excluded per agreement.

## 11b. Invoice Delivery Facts

- Invoices are generated at each billing cycle close and are available in the
  Workspace Billing section.
- An invoice notification is emailed to the workspace billing contact.
- Monthly invoices are generally available the day the charge posts; exact
  posting time varies.
- Receipts are available for payment; invoices remain available for the
  subscription lifetime.
- Invoice line items reflect: subscription base charge, prorations, seat
  changes, taxes, and credits where applicable.

## 12. Document IDs

One authoritative document per topic. Duplicate documents are not created to
inflate corpus size.

### Pricing & Plans (`knowledge_base/pricing/`)

| ID | File | Title |
|---|---|---|
| KB-PRICING-001 | plan-tiers-overview.md | Plan Tiers Overview |
| KB-PRICING-002 | feature-matrix.md | Feature Matrix by Plan |
| KB-PRICING-003 | seat-limits-and-add-ons.md | Seat Limits & Add-Ons |
| KB-PRICING-004 | annual-vs-monthly-pricing.md | Annual vs Monthly Pricing |
| KB-PRICING-005 | currency-and-regional-pricing.md | Currency & Regional Pricing |
| KB-PRICING-006 | upgrade-downgrade-rules.md | Plan Upgrade & Downgrade Rules |
| KB-PRICING-007 | trial-period-terms.md | Trial Period Terms |

### Billing & Payments (`knowledge_base/billing/`)

| ID | File | Title |
|---|---|---|
| KB-BILLING-001 | supported-payment-methods.md | Supported Payment Methods |
| KB-BILLING-002 | billing-cycle.md | Billing Cycle Explanation |
| KB-BILLING-003 | invoice-generation-and-delivery.md | Invoice Generation & Delivery |
| KB-BILLING-004 | receipt-download-and-access.md | Receipt Download & Access |
| KB-BILLING-005 | failed-payment-dunning.md | Failed Payment & Dunning Process |
| KB-BILLING-006 | payment-method-update.md | Payment Method Update |
| KB-BILLING-007 | 3ds-sca.md | 3D Secure / SCA |
| KB-BILLING-008 | tax-calculation.md | Tax Calculation |
| KB-BILLING-009 | billing-address-changes.md | Billing Address Changes |

### Refunds & Credits (`knowledge_base/refunds/`)

| ID | File | Title |
|---|---|---|
| KB-REFUND-001 | standard-refund-policy.md | Standard 30-Day Refund Policy |
| KB-REFUND-002 | prorated-refund-calculation.md | Prorated Refund Calculation |
| KB-REFUND-003 | refund-exception-approval.md | Refund Exception Approval |
| KB-REFUND-004 | credit-balance-application.md | Credit Balance Application |
| KB-REFUND-005 | refund-processing-timeframes.md | Refund Processing Timeframes |
| KB-REFUND-006 | partial-refund-scenarios.md | Partial Refund Scenarios |

### Cancellations & Account Management (`knowledge_base/cancellations/`)

| ID | File | Title |
|---|---|---|
| KB-CANCEL-001 | self-serve-cancellation.md | Self-Serve Cancellation |
| KB-CANCEL-002 | cancellation-effective-date.md | Cancellation Effective Date |
| KB-CANCEL-003 | data-retention-after-cancellation.md | Data Retention After Cancellation |
| KB-CANCEL-004 | account-deletion-vs-subscription-cancellation.md | Account Deletion vs Subscription Cancellation |
| KB-CANCEL-005 | reactivation-and-price-locking.md | Reactivation & Price Locking |
| KB-CANCEL-006 | data-export-before-cancellation.md | Data Export Before Cancellation |

### Invoices & Documentation (`knowledge_base/invoices/`)

| ID | File | Title |
|---|---|---|
| KB-INVOICE-001 | invoice-line-items.md | Invoice Line Item Breakdown |
| KB-INVOICE-002 | enterprise-custom-invoice-requirements.md | Enterprise Custom Invoice Requirements |
| KB-INVOICE-003 | purchase-order-numbers.md | Purchase Order Numbers |
| KB-INVOICE-004 | billing-contact-updates.md | Billing Contact Updates |
| KB-INVOICE-005 | invoice-disputes.md | Invoice Disputes |

### Enterprise & Custom Terms (`knowledge_base/enterprise/`)

| ID | File | Title |
|---|---|---|
| KB-ENT-001 | enterprise-contract-billing.md | Enterprise Contract Billing |
| KB-ENT-002 | volume-discount-tiers.md | Volume Discount Tiers |
| KB-ENT-003 | dedicated-account-manager.md | Dedicated Account Manager |
| KB-ENT-004 | sla-uptime-credits.md | SLA & Uptime Credits |
| KB-ENT-005 | security-questionnaire-soc2.md | Security Questionnaire & SOC 2 Requests |

### Troubleshooting (`knowledge_base/troubleshooting/`)

| ID | File | Title |
|---|---|---|
| KB-TROUBLE-001 | why-was-i-charged.md | Why Was I Charged? |
| KB-TROUBLE-002 | double-charge-investigation.md | Double Charge Investigation |
| KB-TROUBLE-003 | currency-conversion-discrepancies.md | Currency Conversion Discrepancies |
| KB-TROUBLE-004 | bank-statement-descriptor-mismatch.md | Bank Statement Descriptor Mismatch |

## 13. Synthetic Example Conventions

- Use fictional customer/workspace names, invoice IDs, dates, amounts.
- Invoice ID format: `AF-2026-XXXXXX` (6-digit sequence).
- Order/receipt reference format: `AF-RCPT-XXXXXX` or `ORD-XXXXXXXX`.
- Do not use real personal information.
- Account-specific facts (a specific customer's charge) are never fabricated as
  real answers — documents explain what an agent must retrieve instead.
- Amounts in examples must be consistent with plan math
  (e.g., 8 Pro seats monthly = 8 × $24 = $192).