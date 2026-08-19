---
document_id: KB-INVOICE-001
title: Invoice Line Item Breakdown
category: Invoices & Documentation
subcategory: Invoice Structure
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
  - invoice
  - line items
  - billing statement
  - proration
  - seat changes
  - tax
  - credits
  - billing policy
---

# Invoice Line Item Breakdown

This policy explains how an AcmeFlow Workspace invoice is structured and what each line item represents. It is intended for customers who want to understand their bill and for support and billing operations staff who verify charges with customers.

## What an Invoice Shows

At the close of each billing cycle, AcmeFlow Inc. generates an invoice for the workspace. Each invoice carries a unique invoice identifier in the format `AF-2026-XXXXXX`, where the six digits are a sequence number. Receipts issued for a payment use `AF-RCPT-XXXXXX` or `ORD-XXXXXXXX` references.

An invoice groups its amounts into line items. Invoice line items reflect the subscription base charge, any prorations, seat changes, taxes, and credits where applicable. Every amount on the invoice is associated with one of these categories, so the total is the sum of the line items.

## Standard Line Items

The line items you may see on an invoice are described below.

### Subscription Base Charge

The base charge is the recurring amount for your plan and seat count for the cycle.

- Pro pricing is **$24 per user per month** on monthly billing.
- Pro pricing on annual billing is an effective **$20 per user per month**, billed annually in advance.
- Free workspaces are **$0** and do not generate invoices.

The base charge line item states the seat count and the per-user rate used.

### Prorations

A proration appears when a change happens in the middle of an active billing cycle and only part of the cycle is affected.

- A plan upgrade takes effect immediately and any additional charge may be prorated.
- Added seats during an active cycle may generate a prorated charge from the effective date through the end of the cycle.
- Removed seats normally affect future billing only.

Prorated line items show the number of seats, the daily rate, and the number of days being charged.

### Seat Changes

Seat changes are recorded as their own line items when they occur mid-cycle.

- **Adding seats** may produce a prorated charge in the current cycle, with the full new seat count billed from the next cycle.
- **Removing seats** normally reduces the amount billed from the next cycle forward; the current cycle is not automatically credited unless a policy explicitly allows it.

When no mid-cycle change occurs, the invoice simply reflects the seat count in the base charge.

### Taxes

Taxes appear as a separate line item or items. AcmeFlow supports US sales tax, VAT, GST, and regional indirect taxes. Whether tax applies depends on the workspace's billing country, billing address, tax registration, customer tax status, and applicable jurisdiction. There is no single universal tax rate.

For workspaces billed in India, the tax line item uses **GST** terminology. The GST rate applied is determined by the workspace's jurisdiction and is not a universal value.

**Example (illustrative):** A workspace billed in INR receives an invoice showing the base subscription line item and a separate line item labeled `GST`. In this illustrative example the GST amount is ₹28,800.00, computed at the rate applicable to the workspace's jurisdiction. This figure is illustrative for this document only and is not a universal GST rate.

### Credits

Credits from a refund or goodwill grant are held as a workspace credit balance. They are applied automatically to future invoices, in order of invoice generation. A credit appears as a negative line item that reduces the invoice total. Credits are non-transferable, have no cash-out value, and are not exchangeable for a refund.

## How Line Items Are Combined

The invoice total is the sum of all line items: the base charge, plus or minus prorations, plus taxes, minus credits. Line items are listed individually so each part of the total can be reviewed. If a customer asks why a total does not match a simple seat-count multiplication, the difference is almost always a proration, a tax line item, or a credit on the same invoice.

## Example: Monthly Invoice with a Mid-Cycle Seat Addition

Brightpath Logistics is a Pro workspace on monthly billing. At the start of its March cycle it has 8 seats. On March 12 it adds 2 seats.

- Pro monthly rate: **$24.00 per user per month**
- Daily per-seat rate used for proration: $24.00 ÷ 30 days = **$0.80 per seat per day**
- Days charged for the added seats (March 12–31): **20 days**
- Prorated charge: 2 seats × $0.80 × 20 days = **$32.00**

The invoice generated at the cycle close is **AF-2026-004821**:

| Line item | Amount |
|---|---|
| Pro subscription — 8 seats @ $24.00/month | $192.00 |
| Prorated seat addition — 2 seats @ $0.80/day × 20 days | $32.00 |
| Sales tax (illustrative rate for the jurisdiction) | $16.80 |
| **Total** | **$240.80** |

The sales tax of $16.80 is an illustrative example for this document only; the actual rate is determined by the workspace's jurisdiction.

## Example: Annual Invoice with a Credit Applied

Northwind Studios is a Pro workspace on annual billing with 8 seats. Its annual renewal generates invoice **AF-2026-005131**. A workspace credit balance of $50.00 is applied automatically.

- Annual Pro rate: **$20.00 per user per month**, billed annually in advance
- Base charge: 8 seats × $20.00 × 12 months = **$1,920.00**

| Line item | Amount |
|---|---|
| Pro subscription (annual) — 8 seats @ $20.00/month × 12 | $1,920.00 |
| Credit applied | −$50.00 |
| Sales tax (illustrative rate on $1,870.00) | $140.25 |
| **Total** | **$2,010.25** |

## Example: Seat Removal Affects Future Billing

Harbor & Pine is a Pro workspace with 10 seats on monthly billing. It removes 2 seats mid-cycle. No credit is generated for the current cycle. Starting with the next billing cycle, the base charge reflects 8 seats:

- Next cycle base charge: 8 × $24.00 = **$192.00**

## Currency and Tax on the Invoice

The invoice is rendered in the workspace's billing currency. Supported currencies include USD, EUR, GBP, CAD, AUD, INR, JPY, and SGD. Currency is set at the workspace level and not every currency is available in every region. When a charge is made in a currency different from the payment method's currency, card networks and payment processors apply market exchange rates; there is no fixed conversion rate.

## Invoice and Receipt References

- Invoices use the `AF-2026-XXXXXX` format.
- Receipts use `AF-RCPT-XXXXXX` or `ORD-XXXXXXXX` references.
- An invoice and its associated receipt are separate documents with separate references.

## Invoice Availability

- Invoices are generated at each billing cycle close and are available in the Workspace Billing section.
- An invoice notification is emailed to the workspace billing contact.
- Monthly invoices are generally available the day the charge posts; the exact posting time varies.
- Receipts are available for payment; invoices remain available for the subscription lifetime.

## Agent Guidance: Verifying a Line Item

When a customer questions a line item, retrieve the actual invoice from the workspace's Billing section rather than estimating from memory. Confirm the plan, seat count, cycle dates, and any mid-cycle changes in the workspace's billing history before explaining a proration or credit. Account-specific charges are never answered from general knowledge; they are verified against the workspace's own invoice and payment records.

## Related Documentation

- Invoice Generation & Delivery
- Receipt Download & Access
- Billing Cycle Explanation
- Tax Calculation
- Credit Balance Application
- Annual vs Monthly Pricing
- Plan Upgrade & Downgrade Rules
- Seat Limits & Add-Ons
- Why Was I Charged?