---
document_id: KB-TROUBLE-001
title: Why Was I Charged?
category: Troubleshooting
subcategory: Unexpected Charges
document_type: Support Runbook
audience:
  - Customer Support
  - Billing Operations
status: active
version: "1.0"
effective_date: "2026-01-01"
last_reviewed: "2026-07-01"
owner: Billing Operations
product: AcmeFlow Workspace
tags:
  - unexpected charge
  - charge investigation
  - proration
  - renewal
  - additional seats
  - invoice
  - escalation
---

# Why Was I Charged?

This runbook helps agents investigate why a customer was charged when they did not expect to be. Follow the steps in order. Every conclusion must be grounded in records retrieved for the customer's workspace, never assumed from the customer's description alone.

## What to Retrieve Before You Start

Open the workspace's Billing section and retrieve the following before classifying anything:

- Workspace ID and name
- Subscription plan and billing cycle (monthly or annual)
- Subscription start date and next renewal date
- All invoices in the relevant window, with invoice IDs
- Charge date, amount, and currency for each invoice
- Payment method on file and the last four digits of the card charged
- Payment status per invoice (pending, settled, failed, refunded)
- Seat count now and at each point in the billing cycle
- Any plan changes, seat changes, or credits applied in the window

Do not begin an explanation until you can identify a specific invoice. Without an invoice ID, the investigation has not started.

## Step 1: Identify the Charge

Confirm exactly which charge the customer is asking about.

1. Ask the customer for the amount, the charge date, and the last four digits of the card charged. Ask for the currency shown on their bank statement.
2. Locate the matching invoice in the workspace Billing section. Invoice IDs use the format `AF-2026-XXXXXX`.
3. Confirm the charge date, amount, and currency on the invoice match the customer's statement. Note any mismatch for Step 3.
4. Confirm which subscription and workspace the invoice belongs to. A customer may have more than one workspace.
5. Record the payment status: pending, settled, failed, or refunded.

Verification requirement: you must have an invoice ID, charge date, amount, currency, and card last four digits before proceeding. If any are missing, retrieve them first.

## Step 2: Classify the Charge

Place the charge into one of the following categories. Most unexpected charges fall into one of these.

- **Recurring subscription charge** — The normal monthly or annual renewal for the workspace's plan.
- **Renewal** — A subsequent cycle charge on the same plan.
- **Prorated upgrade** — An upgrade that took effect immediately, with the additional charge prorated for the remainder of the cycle.
- **Additional seat** — Seats added mid-cycle, which generate a prorated charge.
- **Tax** — Sales tax, VAT, GST, or regional indirect tax added to a charge. There is no single universal tax rate; the applicable tax depends on the customer's jurisdiction.
- **Usage charge** — Only possible where the plan or Enterprise agreement defines usage-based billing. Self-service plans do not add usage charges for workflow executions.
- **One-time Enterprise charge** — A charge defined by the signed Enterprise agreement, such as a setup fee or a contract-specific billing event. Do not invent a universal price for these.
- **Credit reversal** — A credit applied to a previous invoice being reversed, or a credit re-applied to a future invoice.

Assign exactly one classification, and note the evidence that supports it (invoice line items, proration records, or agreement terms).

## Step 3: Investigate the Cause

Work through the checks below in order until the charge is fully explained.

### Check the Billing Cycle

Monthly subscriptions renew on the same calendar day as the original subscription date. If that day does not exist in a month, the workspace is billed on the final day of that month. Annual subscriptions renew on the anniversary date.

Confirm the charge date matches the expected renewal date for the cycle. A charge on the correct renewal date is expected, not an error.

### Check Seat Changes

- Seats added during an active cycle generate a prorated charge for the remainder of the cycle.
- Seats removed normally affect future billing only.

Compare the seat count at cycle start with the seat count now. A prorated seat charge explains a mid-cycle charge that the customer did not expect.

### Check Plan Changes

- Plan upgrades take effect immediately; additional charges may be prorated.
- Plan downgrades take effect at the start of the next billing cycle, and unused time on the higher plan is not automatically refunded unless a policy explicitly allows it.

Confirm whether any plan change occurred and whether a prorated line item was generated.

### Check for Proration

Proration produces a partial-period charge. Verify the prorated amount by checking the invoice line items, the effective date of the change, and the end of the cycle. The invoice line items reflect the subscription base charge, prorations, seat changes, taxes, and credits where applicable.

### Check Tax

Taxes are added where applicable and depend on the customer's billing country, billing address, tax registration, and customer tax status. There is no universal tax rate. A tax line item on the invoice explains a charge slightly higher than the base subscription amount.

### Check the Previous Balance and Credits

A workspace may carry a previous balance from a failed payment or a dunning cycle. Verify whether any outstanding balance from earlier cycles was collected on the current charge. Also check whether credits were applied; credits apply automatically to future invoices in order of invoice generation and are not cash-outable.

### Confirm the Math

Confirm the amount with plan math. For example, a Pro workspace on monthly billing with 8 seats charges $192.00 (8 × $24.00). Free plan workspaces are never charged; a Free plan should produce no charge at all.

## Step 4: Explain and Resolve

Once the cause is confirmed, explain it plainly to the customer, referencing the invoice ID and the specific line item. Be clear that:

- Cancellation prevents future renewals; it does not automatically create a refund for the current period.
- Paid access continues until the end of the current billing period after cancellation.
- Standard refunds fall under the 30-day refund window from the original charge, and prorated refunds exist only where the applicable policy explicitly permits them.

Do not promise a refund. Route refund requests to the refund policy and its approval flow.

## Verification Checklist

Before closing the ticket, confirm all of the following:

- [ ] The specific invoice was identified by invoice ID (`AF-2026-XXXXXX`).
- [ ] Charge date, amount, currency, and card last four digits were verified against the invoice.
- [ ] The charge was classified into exactly one category.
- [ ] The billing cycle, seat changes, plan changes, proration, tax, and previous balance were all checked.
- [ ] The amount was reconciled with plan math or the Enterprise agreement.
- [ ] The customer received an explanation tied to a specific invoice and line item.

## Worked Examples

### Example 1: Prorated Seat Addition

Nimbus Logistics (workspace `wsp_44712`) is on Pro monthly billing with 6 seats at $24.00 per seat per month. On June 12, 2026, the workspace adds 2 seats. The cycle runs from June 1 to June 30.

- 8 seats are billed for the full cycle at the next renewal: 8 × $24.00 = $192.00.
- The 2 added seats are prorated from June 12 through June 30 (19 of 30 days): 2 × $24.00 × 19 / 30 = $30.40.

Invoice `AF-2026-004821` on June 30 shows a base charge of $144.00 (6 seats) plus a prorated seat charge of $30.40, for a subscription total of $174.40 before tax. The customer queried the extra $30.40; the cause is the prorated seat addition, confirmed by the invoice line items.

### Example 2: Previous Balance Collected at Renewal

Apex Studio (workspace `wsp_88103`) is on Pro annual billing. The February renewal charge failed and entered the dunning cycle; retries continued during the grace period of up to 7 days, then the subscription moved to past-due, with restriction and suspension possible around 14 days from the first failure. The customer updated the card before suspension.

The next charge includes the outstanding balance from the failed cycle plus the current renewal, collected together once the valid card was charged. Invoice `AF-2026-005304` lists the overdue period as a separate line item. The customer expected a single renewal charge; the two line items explain the higher amount.

## Escalation Criteria

Escalate to Billing Operations, or to the dedicated account manager for Enterprise, when any of the following applies:

- The charge cannot be reconciled to any invoice, plan change, proration, tax, balance, or agreement term.
- The amount charged differs from the invoice amount by more than the card network's or processor's market conversion rate, where currencies differ.
- A duplicate settled charge is suspected (see Double Charge Investigation).
- The customer disputes a charge, a refund request exceeds the standard 30-day window, or a prorated refund is requested where the policy does not permit it.
- An Enterprise charge is involved and the signed agreement terms are unclear or conflict with the self-service policy.
- Tax treatment is contested and jurisdiction rules are ambiguous; never invent a tax rate.

## Related Documentation

- Billing Cycle Explanation
- Invoice Line Item Breakdown
- Invoice Generation & Delivery
- Plan Upgrade & Downgrade Rules
- Failed Payment & Dunning Process
- Tax Calculation
- Double Charge Investigation
- Standard 30-Day Refund Policy
- Prorated Refund Calculation
- Invoice Disputes