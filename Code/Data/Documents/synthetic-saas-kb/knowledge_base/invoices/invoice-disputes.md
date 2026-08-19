---
document_id: KB-INVOICE-005
title: Invoice Disputes
category: Invoices & Documentation
subcategory: Support Runbook
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
  - invoice dispute
  - charge dispute
  - billing support
  - runbook
  - escalation
  - verification
---

# Invoice Disputes

This runbook is for internal use by Customer Support and Billing Operations when a customer disputes an invoice or a charge. It covers initial triage, diagnostic steps, verification requirements, common causes, escalation criteria, and resolution follow-up.

## Purpose

An invoice dispute is a customer claim that an invoice is wrong, unexpected, or does not match what was agreed. The goal is to verify the invoice against the workspace's records, explain the charge, and resolve it correctly. Never confirm or dismiss a disputed amount from memory; always verify against the workspace's invoice and payment records.

## Initial Triage

1. Acknowledge the customer's concern and confirm which invoice or charge they are asking about. Ask for the invoice identifier (for example, `AF-2026-XXXXXX`) or the receipt reference (`AF-RCPT-XXXXXX` or `ORD-XXXXXXXX`).
2. Confirm the workspace name, plan, and billing cycle.
3. Identify the type of dispute:
   - Amount does not match expectation.
   - Duplicate or unexpected charge.
   - Proration or seat change question.
   - Tax amount question.
   - Missing or incorrect invoice document.
   - Refund request tied to the invoice.
4. Retrieve the invoice from the Workspace Billing section before proceeding.

## Diagnostic Steps

1. Open the workspace's Billing section and pull the disputed invoice.
2. Check the invoice identifier, cycle dates, plan, and seat count on the invoice.
3. Sum the line items: subscription base charge, prorations, seat changes, taxes, and credits where applicable. Confirm the total matches the invoice total.
4. Compare the invoice to the workspace's billing history to confirm whether the charge was posted, and whether any additional payments or receipts exist.
5. For Pro workspaces, verify the math using standard pricing: $24 per user per month (monthly) or $20 per user per month effective (annual). For example, 8 Pro seats monthly = 8 × $24 = $192.00.
6. For Enterprise workspaces, verify against the signed agreement: billing period, contract currency, seat commitment, net terms, and any contract rate. The signed Enterprise agreement takes precedence over standard self-service policy where the two differ.
7. If a tax amount is questioned, confirm the workspace's billing country, billing address, tax registration, customer tax status, and jurisdiction. There is no single universal tax rate.
8. If a refund or credit is requested, apply the refund policy and credit rules rather than granting it in the course of the dispute.
9. If the charge appears as a duplicate, cross-check the invoice against its associated receipt before concluding anything. See the double-charge investigation guidance for the full procedure.

## Verification Requirements

Before responding to a dispute, verify all of the following:

- The invoice identifier and generation date exist in the workspace's Billing section.
- The line items reconcile to the invoice total.
- The plan, seat count, and cycle dates match the workspace's billing history.
- Any proration is supported by a dated seat or plan change in the billing history.
- Any credit is consistent with the workspace's credit balance.
- For Enterprise, the amounts match the signed agreement's terms.

Account-specific charges are never fabricated or assumed; they are read from the workspace's own invoice and payment records. If the record is unclear, escalate rather than guess.

## Common Dispute Causes

- A proration from a mid-cycle upgrade or seat addition that the customer did not expect.
- A change that takes effect at the next cycle (for example, a plan downgrade or seat removal), where the current invoice still reflects the previous configuration.
- A tax line item added for the workspace's jurisdiction.
- A credit reducing the total, which the customer may not have noticed.
- Confusion between an invoice and its receipt, or between separate invoice identifiers.
- A renewal date that shifted to the final day of the month when the original day does not exist.

## Escalation Criteria

Escalate to Billing Operations when:

- The invoice cannot be reconciled after completing the diagnostic steps.
- The dispute involves Enterprise contract terms or a signed agreement.
- The customer is requesting a refund outside the standard 30-day refund window, or a prorated refund that standard policy does not permit.
- A credit or goodwill grant is being considered.
- The customer disputes the same invoice repeatedly after a verified explanation.
- The dispute involves a possible billing system error rather than an account configuration.

Escalations should include the invoice identifier, the workspace name, the diagnostic steps already taken, and the customer's stated concern.

## Resolution and Follow-Up

1. Provide the verified explanation with the relevant line items, showing the math where possible.
2. If a correction is needed (for example, a billing system error), record it and coordinate the correction with Billing Operations.
3. If a refund is granted under policy, follow the applicable refund process and timeframes. Card refunds typically appear in 5–10 business days, PayPal in 5–7 business days, and ACH in 7–10 business days. These are estimates; do not guarantee exact dates.
4. If a credit is granted, confirm it will be applied automatically to future invoices in order of invoice generation.
5. Document the resolution on the ticket and note any follow-up owed to the customer.

## Example: Duplicate Charge Concern

A customer at Brightpath Logistics reports two charges for March. The agent asks for the references. The customer provides invoice **AF-2026-004821** and receipt **AF-RCPT-003418**. The agent pulls both documents:

- The invoice total is $240.80, which includes a prorated seat addition.
- The receipt references the same invoice and matches the posted charge.
- There is a second invoice, **AF-2026-004822**, which is a separate invoice for the April cycle at the new seat count.

The two documents are different cycles, not a duplicate. The agent explains both invoices and their line items, confirming each payment matches its invoice.

## Example: Disputed Proration Amount

A customer at Northwind Studios questions a prorated charge on invoice **AF-2026-006209**. The agent pulls the invoice and the workspace's billing history.

- The history shows 2 seats were added on the 12th of the month.
- The invoice shows the prorated line item for 2 seats × the daily rate × 20 days.
- The total reconciles when the proration is added to the base charge.

The agent shows the calculation, confirms the seat-change date in the billing history, and closes the ticket with the explanation.

## Related Documentation

- Why Was I Charged?
- Double Charge Investigation
- Invoice Line Item Breakdown
- Invoice Generation & Delivery
- Tax Calculation
- Standard 30-Day Refund Policy
- Credit Balance Application
- Billing Cycle Explanation
- Enterprise Contract Billing