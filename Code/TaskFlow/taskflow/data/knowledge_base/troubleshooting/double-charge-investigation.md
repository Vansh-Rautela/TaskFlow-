---
document_id: KB-TROUBLE-002
title: Double Charge Investigation
category: Troubleshooting
subcategory: Duplicate Charges
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
  - double charge
  - duplicate charge
  - pending
  - settled
  - pre-authorization
  - split billing
  - escalation
---

# Double Charge Investigation

This runbook helps agents determine whether a customer was genuinely charged twice, whether one of the charges was a pending authorization that will fall off, or whether the two charges simply belong to different billing periods. Most reported "double charges" turn out to be something else, so do not conclude duplication until the evidence says so.

## What to Retrieve Before You Start

Gather the following for the workspace before comparing anything:

- Workspace ID and name
- Both invoice IDs involved, or the statement entries the customer is referring to
- Charge dates, amounts, and currencies for each
- Payment status of each: pending, settled, failed, or refunded
- Subscription plan, billing cycle, and cycle start/end dates
- Whether the workspace is self-service or under an Enterprise agreement
- Any Enterprise split billing configuration (for example, charges split by legal entity or cost center)

Verification requirement: a genuine double charge requires two distinct settled charges for the same invoice or the same covered period. Everything else is a different finding.

## Step 1: Verify Two Distinct Charges Exist

1. Ask the customer for the amount, date, and card last four digits for each entry on their bank statement.
2. In the workspace Billing section, locate every invoice in the date range. Invoice IDs use the format `AF-2026-XXXXXX`.
3. Confirm each statement entry maps to exactly one invoice, or document any statement entry that maps to no invoice.
4. Compare dates, amounts, currencies, and card last four digits between the statement entries and the invoices.
5. Record each charge's status: pending or settled.

Only proceed to duplication when two separate settled charges exist. One settled charge plus one pending entry is not a double charge.

## Step 2: Check Pending vs Settled Status

Cards are charged by the processor, and pending entries can appear before a charge settles.

- A **pending** entry on the customer's bank statement is an authorization that has not completed settlement.
- A pending authorization can sit on the card for several days and may fall off automatically if it is not settled.
- If one of the two entries is still pending, instruct the customer to wait for the pending entry to settle or expire before any refund decision is made.

**Example:** A customer sees two entries on their card for the same day. One is settled and matches invoice `AF-2026-004812`. The other is still marked pending on the bank statement and matches no invoice. This is one settled charge plus one pending authorization, not a double charge.

## Step 3: Check Whether One Charge Is a Pre-Authorization

A pre-authorization is a temporary hold placed on a card, often at the time a payment method is added or a 3D Secure / SCA step is triggered, or by the processor as part of a payment attempt.

- A pre-authorization may appear as a small or full amount on the statement and can differ from the eventual settled amount.
- Pre-authorizations that are not settled are released by the card issuer, typically within a few business days.
- Verify whether a pending hold exists on the customer's card and whether it has been released.

A charge that was authorized but never settled does not need a refund; it needs to be released by the issuer.

## Step 4: Check for Overlapping Billing Cycles

Two charges on a monthly subscription can look like a duplicate when one invoice covers an earlier failed cycle.

- Monthly subscriptions renew on the same calendar day as the original subscription date; if that day does not exist in a month, the workspace is billed on the final day of that month.
- If a charge failed, retries continued during a grace period of up to 7 days, after which the subscription could move to past-due, with restriction and suspension possible around 14 days from the first failure (approximate).
- When the customer later pays, the outstanding balance from the failed cycle and the current cycle's renewal can settle close together, producing two statement entries for two different billing periods.

Confirm each invoice covers a distinct period. If the covered periods do not overlap and each amount is correct for its period, the charges are two separate cycles, not a duplicate.

**Example:** Blue Oak Media's monthly charge for the January cycle failed. The subscription moved through the grace period and past-due, then the customer updated their card. The processor settled the outstanding January invoice (`AF-2026-001109`, $192.00) and the current February invoice (`AF-2026-002215`, $192.00) within a day of each other. Both invoices are for different periods; no duplication exists.

## Step 5: Check Enterprise Split Billing

Enterprise agreements may define custom billing, including quarterly billing and split billing by legal entity, cost center, or purchase order.

- A single Enterprise agreement can produce multiple invoices and multiple charges in a billing period by design.
- Split billing charges are not duplicates; they are separate contract obligations.

Compare the invoices to the signed Enterprise agreement before classifying split charges as duplicates. The signed agreement takes precedence over the standard self-service policy where the two differ.

## Step 6: Document What You Found

Record the conclusion in the ticket with the supporting evidence:

- Both invoice IDs and the periods they cover
- Payment status of each entry (pending or settled)
- Whether a pre-authorization or pending hold was involved
- Whether the charges cover the same or different billing periods
- Whether Enterprise split billing applies
- The final classification: genuine duplicate, pending authorization, pre-authorization, or different billing periods

## Verification Checklist

Before closing the ticket, confirm all of the following:

- [ ] Every statement entry was mapped to an invoice ID or documented as unmapped.
- [ ] Payment status (pending vs settled) was recorded for each entry.
- [ ] Pending authorizations and pre-authorizations were identified and their release was explained.
- [ ] Covered billing periods were compared and found to be overlapping or non-overlapping.
- [ ] Enterprise split billing was considered where an Enterprise agreement exists.
- [ ] A genuine duplicate was confirmed only when two settled charges covered the same invoice or period.

## Escalation Criteria

Escalate to Billing Operations, or to the dedicated account manager for Enterprise, when any of the following applies:

- Two settled charges are confirmed for the same invoice or the same covered period, with no valid explanation.
- A settled charge maps to no invoice and no Enterprise agreement term.
- The customer's card was charged more than once for the same period and a refund is required; refunds follow the standard 30-day window and refund processing timeframes.
- Pending or pre-authorized amounts remain on the card beyond a reasonable release window and the customer needs issuer-level assistance.
- Enterprise split billing terms are unclear and the signed agreement must be reviewed.

## Related Documentation

- Why Was I Charged?
- Billing Cycle Explanation
- Invoice Line Item Breakdown
- Failed Payment & Dunning Process
- 3D Secure / SCA
- Enterprise Contract Billing
- Standard 30-Day Refund Policy
- Refund Processing Timeframes
- Invoice Disputes