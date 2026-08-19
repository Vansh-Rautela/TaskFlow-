---
document_id: KB-TROUBLE-004
title: Bank Statement Descriptor Mismatch
category: Troubleshooting
subcategory: Statement & Descriptor
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
  - bank statement
  - descriptor
  - unrecognized charge
  - ACMEFLOW
  - statement match
  - escalation
---

# Bank Statement Descriptor Mismatch

This runbook helps agents investigate customers who do not recognize the charge on their bank statement. In most cases the customer recognizes the amount and the merchant once the descriptor and the matching AcmeFlow invoice are explained. Follow the steps to confirm the charge is an AcmeFlow charge before doing anything else.

## Descriptor Facts to Establish First

- Charges for AcmeFlow Workspace appear on bank statements under the descriptor **`ACMEFLOW`**.
- The legal entity behind invoices is **AcmeFlow Inc.**
- The descriptor may include additional information such as the card's last four digits or merchant location.
- A descriptor is a short, fixed label set by the payment processor; it is not the full company name. This is why a statement entry can look different from "AcmeFlow Inc." on an invoice.

Never assume an unrecognized descriptor is not an AcmeFlow charge just because it does not spell out the full company name.

## What to Retrieve Before You Start

- Workspace ID and name
- The statement entry: date, amount, currency, descriptor text, and card last four digits
- All invoices in the matching date range, with invoice IDs (`AF-2026-XXXXXX`)
- The subscription plan, billing cycle, and renewal date
- Payment method on file and its status
- Whether the workspace is under an Enterprise agreement with custom invoice arrangements

## Step 1: Confirm the Charge Is from AcmeFlow

1. Ask the customer for the exact descriptor text, amount, date, and card last four digits shown on the statement.
2. Look for `ACMEFLOW` in the descriptor. Note that some banks truncate or reformat descriptors, so the full text may differ slightly.
3. Check whether the card last four digits in the statement match the card on file in the workspace Billing section.
4. Retrieve the invoices in the same date range and match one to the statement amount and date.

Verification requirement: do not proceed to explaining an unrecognized charge until either the descriptor contains `ACMEFLOW`, or the amount, date, and card last four digits match an AcmeFlow invoice. If neither matches, the charge may not be from AcmeFlow at all.

## Step 2: Explain What a Descriptor Contains

A bank statement descriptor typically contains:

- The merchant name as configured by the processor — here, `ACMEFLOW`.
- Optionally, the last four digits of the card used.
- Optionally, merchant location or city information.

The descriptor is set at the processor level and is intentionally short. The legal entity on invoices, **AcmeFlow Inc.**, is longer and may not appear on the bank statement at all. That difference is expected and does not indicate a wrong merchant.

## Step 3: Explain Why It Differs from the Company Name

- The descriptor `ACMEFLOW` is the processor-facing merchant label.
- The invoice references **AcmeFlow Inc.**, the legal entity that issues the invoice.
- Banks display what the processor supplies, which is the descriptor, not the legal entity name.
- Card networks and processors can also truncate or reformat the descriptor, so the exact text on the statement may not match the descriptor configured.

The customer may also be searching for the charge under a remembered brand name or a manager's name; the workspace name is not part of the descriptor.

## Step 4: Locate the Matching AcmeFlow Invoice

To prove the charge belongs to the customer's workspace:

1. Open the workspace Billing section.
2. Find the invoice whose charge date, amount, currency, and card last four digits match the statement entry.
3. Reference the invoice ID (`AF-2026-XXXXXX`) and its line items to the customer.
4. Confirm the payment status is settled; a pending entry may not yet have a corresponding invoice or may still be an authorization.

Invoice line items reflect the subscription base charge, prorations, seat changes, taxes, and credits where applicable, which helps the customer recognize the charge.

## Step 5: Confirm the Amount Is Expected

Confirm the charge amount matches the plan and cycle:

- Monthly Pro pricing is $24.00 per seat per month; annual Pro is $20.00 per seat per month effective, billed annually in advance.
- For example, a Pro workspace with 8 seats on monthly billing is charged $192.00 at each cycle close.
- Free plan workspaces are never charged.

If the amount, date, and card match an invoice, the charge is legitimate even if the descriptor looked unfamiliar.

## Worked Examples

### Example 1: Descriptor Looks Different from the Company Name

Cedar & Pine Design (workspace `wsp_77801`) has a Pro monthly subscription at $192.00 (8 seats × $24.00). The customer does not recognize `ACMEFLOW` on their statement and expected to see "AcmeFlow Inc." The agent confirms the card last four digits (4012) match the card on file and that the statement date and amount match invoice `AF-2026-003901` for $192.00. The agent explains that `ACMEFLOW` is the processor descriptor while AcmeFlow Inc. is the legal entity on the invoice, and that the two are expected to differ.

### Example 2: Truncated Descriptor on the Statement

Polaris Ventures (workspace `wsp_90220`) bills in USD. The statement shows a shortened entry that does not visibly contain the full `ACMEFLOW` text. The amount ($192.00) and date match invoice `AF-2026-004512`, and the card last four digits (8820) match the card on file. The agent confirms the charge is the Pro monthly renewal and notes that banks sometimes truncate descriptors; the matching invoice is the proof of origin.

## Escalation Criteria

Escalate to Billing Operations when any of the following applies:

- The statement entry contains no recognizable `ACMEFLOW` text and matches no AcmeFlow invoice, yet the customer believes it is an AcmeFlow charge.
- The amount, date, and card last four digits match an invoice but the descriptor belongs to a different merchant, suggesting a processor configuration or bank display issue.
- A charge for a Free plan workspace appears on a statement, since Free plan workspaces are never charged.
- The customer is under an Enterprise agreement with custom invoices and the statement entry must be reconciled against contract terms.
- A dispute or chargeback has been filed or is threatened; route to the invoice dispute flow rather than resolving unilaterally.

## Related Documentation

- Why Was I Charged?
- Double Charge Investigation
- Invoice Generation & Delivery
- Receipt Download & Access
- Billing Cycle Explanation
- Invoice Line Item Breakdown
- Supported Payment Methods
- Invoice Disputes