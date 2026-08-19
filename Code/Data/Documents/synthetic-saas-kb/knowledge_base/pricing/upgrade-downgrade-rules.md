---
document_id: KB-PRICING-006
title: Plan Upgrade & Downgrade Rules
category: Pricing & Plans
subcategory: Plan Changes
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
  - upgrade
  - downgrade
  - proration
  - feature access
  - seat changes
  - effective date
---

# Plan Upgrade & Downgrade Rules

This document defines how plan changes work on AcmeFlow Workspace: when an upgrade or downgrade takes effect, what happens to charges, and how features and seats are affected.

## Upgrades Take Effect Immediately

An **upgrade** (for example, from Free to Pro, or from Pro to a higher tier) takes effect **immediately**:

- New features are available right away.
- Additional charges may be **prorated** for the remainder of the current billing cycle.
- The new plan's full price applies starting at the next renewal.

## Downgrades Take Effect at the Next Billing Cycle

A **downgrade** (for example, from Pro back to Free) takes effect at the **start of the next billing cycle**:

- The customer keeps the higher-tier features until the end of the current cycle.
- **Unused time is not automatically refunded** unless the applicable policy explicitly permits it.
- The new (lower) plan's terms begin at the next renewal.

For annual plans, "next billing cycle" means the next annual anniversary date.

## Feature Access Changes

- **On upgrade**: the features of the new plan (for example, audit logs and advanced permissions on Pro) are enabled immediately.
- **On downgrade**: features of the higher tier remain available until the effective date of the downgrade, then revert. For example, a Pro workspace that downgrades to Free loses Pro-only features such as audit logs and advanced permissions at the start of the next billing cycle.

## Seat Changes

Seat changes follow the same general rules as plan changes:

- **Adding seats** during an active cycle may generate a **prorated charge** for the rest of the cycle; the new seat count is billed in full from the next renewal.
- **Removing seats** normally affects **future billing only**; the current cycle is not adjusted and no refund is issued for unused seat time unless a policy explicitly permits it.

See "Seat Limits & Add-Ons" for seat-specific detail.

## Proration on Upgrades

When an upgrade happens mid-cycle, the additional charge is prorated for the remaining days of the current billing cycle. The prorated amount appears as a line item on the next invoice. Exact proration is based on the number of days remaining in the cycle.

## Enterprise Exceptions

- Enterprise terms are set in the signed agreement, including any differences in upgrade, downgrade, or seat rules.
- The customer's signed Enterprise agreement takes precedence over the standard self-service policy where the two differ.
- Enterprise plans are custom-priced; any Enterprise figure used in an example must be labeled as an example.

## Examples

**Example — upgrade with proration.** Meridian Health Group upgrades from Free to monthly Pro with 5 seats on June 12. The cycle renews on the 1st. The prorated charge covers the 19 days remaining in June (June 12–30 of a 30-day month): 5 × $24 × (19 ÷ 30) = **$76.00**. From July 1, the full charge of 5 × $24 = **$120.00** applies each cycle. Invoice `AF-2026-004821` shows the prorated line item.

**Example — downgrade effective next cycle.** Ardent & Sons downgrades from Pro to Free on July 8. The downgrade takes effect at the start of the next billing cycle on August 1. Until then they keep Pro features, and no refund is issued for the unused portion of July under the standard policy.

**Example — seat add on Pro.** Northwind Labs, on monthly Pro with 8 seats, adds 2 seats on the 15th of a 30-day cycle. The prorated charge for the 16 remaining days is 2 × $24 × (16 ÷ 30) = **$25.60**; the next renewal bills 10 seats at $240.00.

## Related Documentation

- Plan Tiers Overview
- Feature Matrix by Plan
- Annual vs Monthly Pricing
- Seat Limits & Add-Ons
- Standard 30-Day Refund Policy
- Cancellation Effective Date
- Self-Serve Cancellation
- Enterprise Contract Billing