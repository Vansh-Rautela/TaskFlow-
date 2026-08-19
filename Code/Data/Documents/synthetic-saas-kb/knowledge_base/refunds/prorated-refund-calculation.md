---
document_id: KB-REFUND-002
title: Prorated Refund Calculation
category: Refunds & Credits
subcategory: Refund Calculation
document_type: Billing Policy
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
  - refund
  - prorated refund
  - calculation
  - formula
  - pro-rata
---

# Prorated Refund Calculation

## Purpose

This policy explains how a prorated refund amount is calculated when a prorated refund is explicitly permitted. Proration is the exception, not the default: unused time is not automatically refundable unless a policy explicitly allows it.

## Refund Formula

The refund amount is calculated as:

`Refund Amount = Eligible Unused Period ÷ Original Billing Period × Eligible Charge`

## Definitions

- **Eligible Unused Period** — the portion of the original billing period that has not been consumed at the point the prorated refund applies, measured in days.
- **Original Billing Period** — the full billing period the Eligible Charge covered (for example, a 30-day month or a 365-day annual cycle), measured in days.
- **Eligible Charge** — the charge being partially refunded, before any proration. Taxes are not included in the calculation unless a specific policy or agreement states otherwise.

## When Proration Applies

A prorated refund is calculated using this formula only when the applicable policy explicitly permits one, such as:

- An exception approved under the Refund Exception Approval policy.
- A refund provision in a signed Enterprise agreement.
- A specific refund scenario defined in the Partial Refund Scenarios policy.

Cancelling a subscription does not create a prorated refund on its own. Removing seats or downgrading a plan does not create a prorated refund on its own either; those changes normally affect future billing only.

## Calculation Assumptions

Worked examples apply the following assumptions unless stated otherwise:

- A monthly billing period is treated as 30 days.
- An annual billing period is treated as 365 days.
- Day counts are measured from the start of the billing period to the effective date of the refund, inclusive of the start date.
- The Eligible Charge is the base charge before tax.
- Rounding is to two decimal places.

## Worked Examples

### Example 1 — Prorated refund on a monthly charge

Meridian Systems subscribes to 5 Pro seats billed monthly at $24 per user, so the monthly charge is $120.00 (5 × $24). Invoice AF-2026-004821 posted on Mar 1, 2026. A prorated refund is approved, effective Mar 16, 2026, covering the unused remainder of the March cycle.

- Eligible Unused Period: 15 days (Mar 16–30 in a 30-day month)
- Original Billing Period: 30 days
- Eligible Charge: $120.00
- Refund Amount: 15 ÷ 30 × $120.00 = **$60.00**

### Example 2 — Prorated refund on an annual charge

Blue River Analytics subscribes to 8 Pro seats on annual billing at $20 per user per month effective, billed annually in advance. The annual charge is $1,920.00 (8 × $20 × 12). Invoice AF-2026-000310 billed on Jan 1, 2026. A prorated refund is approved on Mar 15, 2026 — 73 days into the annual cycle.

- Eligible Unused Period: 292 days (365 − 73)
- Original Billing Period: 365 days
- Eligible Charge: $1,920.00
- Refund Amount: 292 ÷ 365 × $1,920.00 = **$1,536.00**

In this example, 292 ÷ 365 equals 0.8, so the refund is 80% of the annual charge; no credit is given for the 73 days already consumed.

## Information Required to Calculate a Refund

To apply the formula to a specific case, an agent must retrieve:

- Invoice ID and the Eligible Charge amount
- The original charge date and billing period (monthly or annual)
- The effective date of the prorated refund
- The plan and seat count on the charge

Proration eligibility itself must be confirmed against the applicable policy before any calculation is presented.

## Related Documentation

- Standard 30-Day Refund Policy
- Refund Exception Approval
- Partial Refund Scenarios
- Plan Upgrade & Downgrade Rules
- Refund Processing Timeframes
- Invoice Line Item Breakdown