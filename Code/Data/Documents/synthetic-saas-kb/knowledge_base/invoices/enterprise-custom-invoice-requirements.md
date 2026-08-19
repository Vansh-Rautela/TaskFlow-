---
document_id: KB-INVOICE-002
title: Enterprise Custom Invoice Requirements
category: Invoices & Documentation
subcategory: Enterprise Billing
document_type: Enterprise Policy
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
  - enterprise
  - custom invoice
  - purchase order
  - net terms
  - quarterly billing
  - contract currency
  - enterprise policy
---

# Enterprise Custom Invoice Requirements

This policy defines how custom invoices work for Enterprise workspaces, including the information required on a custom invoice, purchase order and remittance handling, net payment terms, custom billing periods, and contract currency.

## Purpose and Scope

Enterprise customers often need invoices that fit their own procurement, accounting, and legal requirements. AcmeFlow Inc. supports custom invoices for Enterprise workspaces under a signed Enterprise agreement. Custom invoice terms are contract-specific and may differ from standard self-service billing.

The customer's signed Enterprise agreement takes precedence over the standard self-service policy where the two differ. If anything in this policy appears to conflict with a signed agreement, the signed agreement governs.

## When Custom Invoices Apply

Custom invoices apply to Enterprise workspaces whose signed agreement includes custom invoicing. Typical triggers include:

- The customer requires a purchase order (PO) number on the invoice.
- The customer needs net payment terms instead of automatic card charges.
- The agreement defines annual or quarterly billing rather than monthly.
- The agreement sets a contract currency different from the workspace's default currency.
- The customer requires specific invoice fields, formatting, or references for its accounts payable process.

Self-service Pro and Free workspaces do not receive custom invoices. Pro workspaces follow the standard self-service invoice format.

## Required Information on a Custom Invoice

A custom invoice must include the information needed to process the payment and match it to the agreement. This typically includes:

- The invoice identifier (`AF-2026-XXXXXX` format).
- The billing entity, **AcmeFlow Inc.**.
- The customer's legal entity name and billing address as recorded on the account.
- The contract or agreement reference.
- The purchase order number, where the customer has provided one.
- The line items for the period, including the base charge, prorations, seat changes, taxes, and credits where applicable.
- The net payment terms and due date, where the agreement defines them.
- The contract currency and amounts in that currency.

The invoice reflects the contract's seat commitment and rate. Rates are per agreement and are never universal published prices.

## Purchase Orders and Remittance Information

Where the agreement requires it, the invoice includes the customer's PO number and any remittance details needed for payment matching. The customer should provide the PO number before invoice generation so it appears on the correct document. Remittance references help the customer's accounts payable team match the payment to the invoice.

## Net Payment Terms

Enterprise agreements may define net payment terms (for example, net 30 or net 45) instead of automatic card charges. The due date is computed from the invoice date per the agreement. Payment may be made by wire transfer for qualifying Enterprise customers, per the agreement. Refund processing timeframes for wire transfers follow the agreement and may take 10–15 business days.

## Custom Billing Periods: Annual and Quarterly

Enterprise agreements may define billing periods beyond the standard monthly cycle:

- **Annual billing** — billed annually in advance, renewing on the anniversary date.
- **Quarterly billing** — billed for each three-month period in advance per the agreement.

Monthly renewal rules for standard plans do not apply where the agreement sets a different cadence. The agreement defines the renewal schedule.

## Contract Currency

Enterprise agreements may define a contract currency for invoicing, which can differ from the workspace's default billing currency. Where a contract currency is set, invoice amounts are rendered in that currency. Conversion, where it occurs, follows the rates and terms in the agreement; there is no fixed universal conversion rate.

## Signed Agreement Precedence

The customer's signed Enterprise agreement takes precedence over the standard self-service policy where the two differ. This includes differences in billing period, payment terms, currency, seat commitments, refund terms, and invoice formatting. Agents should confirm the agreement terms before answering questions that fall under a contract.

## Example: Quarterly Invoice with Purchase Order and Net 30

Northgate Manufacturing is an Enterprise workspace under a signed agreement. The agreement defines quarterly billing, net 30 payment terms, and a contract rate of $18.00 per user per month (an example contract rate for this document only, not a published price). The contract commits 25 seats.

- Quarterly base: 25 seats × $18.00 × 3 months = **$1,350.00**
- Purchase order number on file: **PO-88213**

The quarterly invoice is **AF-2026-002517**:

| Line item | Amount |
|---|---|
| Enterprise subscription (quarterly) — 25 committed seats | $1,350.00 |
| Sales tax (illustrative rate for the jurisdiction) | $101.25 |
| **Total** | **$1,451.25** |

The invoice prints the customer's PO number **PO-88213**, the agreement reference, and the due date 30 days from the invoice date. The sales tax amount is illustrative for this document only.

## Example: Annual Invoice in Contract Currency

Kessler Financial Group is an Enterprise workspace whose agreement sets EUR as the contract currency with annual billing in advance. The example contract value is €48,000.00 per year, payable per the agreement.

- Invoice **AF-2026-003899** is rendered in EUR.
- The invoice line items reflect the annual contract value and any taxes applicable to the jurisdiction.
- Payment is made by wire transfer per the agreement, with the remittance reference shown on the invoice.

The €48,000.00 figure is an example for this document only and is not a published or standard Enterprise price.

## Agent Guidance

When a customer asks about a custom invoice, retrieve the signed agreement terms and the workspace's billing record rather than relying on standard pricing. Confirm the contract currency, billing period, PO number, and net terms for the specific account. Contract-specific amounts are never quoted from general knowledge; they are verified against the account's agreement and invoices.

## Related Documentation

- Invoice Line Item Breakdown
- Purchase Order Numbers
- Enterprise Contract Billing
- Invoice Generation & Delivery
- Billing Cycle Explanation
- Supported Payment Methods
- Tax Calculation