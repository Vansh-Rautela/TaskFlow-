---
document_id: KB-TROUBLE-003
title: Currency Conversion Discrepancies
category: Troubleshooting
subcategory: Currency & Conversion
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
  - currency conversion
  - conversion rate
  - foreign transaction
  - settlement
  - authorization
  - workspace currency
  - escalation
---

# Currency Conversion Discrepancies

This runbook helps agents investigate why a charge in the customer's local currency differs from the amount shown in the workspace currency. The short answer is usually conversion timing and processor fees, not an AcmeFlow error. Follow the steps to confirm that, and to identify the rare cases that need escalation.

## Currency Facts to Establish First

- AcmeFlow supports USD, EUR, GBP, CAD, AUD, INR, JPY, and SGD, set at the workspace level. Not every currency is available in every region.
- The amount shown in the workspace is in the **workspace currency**. That is the amount AcmeFlow invoices.
- The customer's bank charges in the **card currency** — the currency of the card they paid with.
- There is **no fixed universal conversion rate**. Card networks and payment processors apply market rates.
- Differences between the workspace amount and the statement amount come from conversion timing (authorization vs settlement) and processor or network fees.

The workspace amount and the statement amount are different numbers in different currencies; a difference alone is not a discrepancy in need of correction.

## What to Retrieve Before You Start

- Workspace ID and name
- Invoice ID (`AF-2026-XXXXXX`), charge date, workspace currency amount, and workspace currency
- Card currency and the amount shown on the customer's bank statement
- The payment status of the charge
- Whether the card is a debit card or credit card, and any foreign transaction fee the customer's bank applies
- Whether the payment involved 3D Secure / SCA

## Step 1: Identify Both Amounts

1. Ask the customer for the statement amount and the currency it is in. Ask for the charge date and card last four digits.
2. Retrieve the matching invoice from the workspace Billing section.
3. Record the invoice amount and its workspace currency.
4. Confirm the two amounts refer to the same charge: same date range, same card, same invoice.

Verification requirement: never compare two amounts unless you have confirmed they come from the same charge. Comparing a renewal to a different month's invoice will always produce a difference.

## Step 2: Check the Currencies Involved

- If the card currency differs from the workspace currency, a conversion is expected.
- If the card currency is the same as the workspace currency, there should be no conversion. A difference in that case points to a processor fee, a bank fee, or a different charge — not conversion.

Identify the workspace currency, the card currency, and the billing country. Currency selection is set at the workspace level, so confirm the workspace currency rather than assuming it from the customer's location.

**Example:** A workspace set to EUR is invoiced EUR 200.00 for invoice `AF-2026-004118`. The customer pays with a GBP card. The statement shows £172.40. The GBP amount is a conversion of the EUR invoice at the market rate applied by the card network or processor, plus any bank fee. The EUR 200.00 invoice amount is correct in the workspace.

## Step 3: Check Whether 3D Secure / SCA Applied

Payments may trigger 3D Secure / SCA (strong customer authentication).

- 3D Secure / SCA verifies the cardholder and does not by itself add a charge.
- It can, however, separate the authorization step from settlement in time, which can make the timing of a converted amount differ from what the customer expects.

If 3D Secure / SCA applied, note it in the ticket, but treat it as a timing factor, not a cause of an incorrect amount.

## Step 4: Explain Authorization vs Settlement Rates

The market rate at the time the payment is **authorized** can differ from the rate at the time it is **settled**. Card networks and processors apply their market rate at the point of conversion, so:

- The workspace currency amount is fixed by the invoice.
- The card currency amount depends on the exchange rate at conversion time, which moves between authorization and settlement.
- Processor and network fees can also be added at the bank's side.

The workspace amount and the statement amount will rarely convert to exactly the same value. A difference within a few percent is normal market movement, not a billing error.

## Step 5: Reconcile and Explain

Explain to the customer, referencing the invoice ID:

1. The workspace currency amount is what AcmeFlow charged for the subscription (for example, Pro monthly at $24.00 per seat, or 8 seats for $192.00).
2. The bank charged in the card currency, converting at the market rate at the time of authorization or settlement.
3. Any bank foreign transaction fee is charged by the card issuer, not by AcmeFlow.
4. No universal conversion rate exists; the customer's bank and processor decide the applied rate.

If the customer provides a bank statement snippet, use it to confirm the card currency, the converted amount, and any fee line.

## Worked Examples

### Example 1: Card Currency Differs from Workspace Currency

Harborline Consulting (workspace `wsp_51280`) has a Pro workspace billed monthly in USD. Invoice `AF-2026-006211` is $192.00 (8 seats × $24.00). The customer pays with a card denominated in EUR. Their statement shows €176.20, which is the $192.00 invoice converted at the network's market rate near the payment date, plus a small bank fee. The USD invoice amount is correct; no adjustment is made.

### Example 2: Same Currency, Difference from a Bank Fee

Kitsune Labs (workspace `wsp_20455`) bills in GBP and pays with a GBP card. Invoice `AF-2026-007001` is £168.00. The statement shows £170.94. Because the card currency and workspace currency are both GBP, no conversion is involved; the £2.94 difference is the card issuer's foreign or processing fee. The agent confirms the workspace amount and directs the customer to their bank for fee details.

## Escalation Criteria

Escalate to Billing Operations when any of the following applies:

- The settled statement amount differs from the invoice amount by more than what a market conversion rate plus reasonable processor or bank fees could explain, and a processor-side error is suspected.
- The card currency and workspace currency are the same, yet the statement amount differs by more than an explainable bank fee.
- The charge was settled twice at different rates for the same invoice (see Double Charge Investigation).
- An Enterprise agreement defines a contract currency and rate, and the charge does not match the agreement; the signed agreement takes precedence over the standard self-service policy.
- The customer disputes the applied rate and requests a conversion-rate adjustment; never invent a universal rate or promise a specific outcome.

## Related Documentation

- Why Was I Charged?
- Double Charge Investigation
- Billing Cycle Explanation
- Invoice Line Item Breakdown
- 3D Secure / SCA
- Currency & Regional Pricing
- Enterprise Contract Billing
- Invoice Disputes