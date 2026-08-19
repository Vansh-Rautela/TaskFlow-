---
document_id: KB-PRICING-005
title: Currency & Regional Pricing
category: Pricing & Plans
subcategory: Currency & Regions
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
  - currency
  - regional pricing
  - conversion
  - taxes
  - USD
  - EUR
  - INR
  - billing currency
---

# Currency & Regional Pricing

AcmeFlow Workspace supports billing in multiple currencies, with availability varying by region. This document explains which currencies are supported, how a workspace selects its billing currency, how conversion works, and how taxes interact with pricing.

## Supported Currencies

AcmeFlow supports the following billing currencies:

- **USD** (US Dollar)
- **EUR** (Euro)
- **GBP** (British Pound)
- **CAD** (Canadian Dollar)
- **AUD** (Australian Dollar)
- **INR** (Indian Rupee)
- **JPY** (Japanese Yen)
- **SGD** (Singapore Dollar)

This is the supported set used across the AcmeFlow Knowledge Base. Additional currencies may be offered over time; availability depends on the workspace's region and eligibility.

## Currency Selection at the Workspace Level

- Currency is set at the **workspace level**, in the Workspace Billing settings.
- **Not every currency is available in every region.** A workspace can only select a currency that is supported for its billing country and eligibility.
- When the billing country or billing address changes, the applicable currency and tax treatment may change. See "Billing Address Changes".

Agents should ask the customer which currency they selected at the workspace level rather than assume one from the region.

## Regional Availability

Availability of a currency and of certain features varies by region. For example:

- ACH is only available to eligible US customers.
- Payment methods such as PayPal are available where enabled.
- Certain plans and payment methods may not be available in every region.

See "Supported Payment Methods" for details on payment methods and their regional availability.

## Conversion and Exchange Rates

- AcmeFlow does **not** publish a fixed universal conversion rate between currencies.
- When a workspace bills in a non-USD currency, card networks and payment processors apply **market rates** at the time the charge posts.
- The reference price is the standard plan price in USD; the billed amount in another currency is derived from the market rate in effect at billing time.

Because rates move, the amount a customer sees in their bank statement can differ slightly from what they expected. See "Currency Conversion Discrepancies" if a customer questions the converted amount.

## Tax Interaction

Taxes are calculated based on the workspace's billing country, billing address, tax registration, customer tax status, and the applicable jurisdiction. Supported taxes include US sales tax, VAT, GST, and regional indirect taxes.

- There is **no single universal tax rate**.
- India-based billing examples use **GST** terminology.
- Tax lines appear on invoices separately from the base subscription charge and any proration.

For full detail, see "Tax Calculation". If tax on an invoice looks wrong, refer to that document rather than quoting a rate.

## Enterprise Exceptions

- Enterprise agreements may define a **contract currency** and contract-specific rates for conversion.
- Where the signed agreement specifies a currency or rate, it takes precedence over the standard self-service policy.
- Any Enterprise rate used in an example must be labeled as an example and never treated as published pricing.

## Examples

**Example — EUR billing.** RheinMetrik GmbH bills in EUR at the workspace level. Their 5-seat monthly Pro workspace is billed based on the market rate applied by their card network when the charge posts. The invoice `AF-2026-004821` shows the base subscription charge, a prorated seat line item, and any VAT applicable to their billing country. AcmeFlow does not publish a fixed EUR-per-USD rate.

**Example — INR billing with GST.** Koshur & Co. bills in INR. Their invoice includes GST per Indian indirect tax rules, shown as a separate line item. No universal GST percentage applies; the rate depends on the workspace's registration and jurisdiction.

**Example — Enterprise contract currency (labeled example only).** Under an example agreement, Pacific Ridge Ltd. contracts in CAD at a negotiated rate with no conversion applied. This contract-specific arrangement overrides the standard market-rate conversion for that workspace.

## Related Documentation

- Plan Tiers Overview
- Feature Matrix by Plan
- Tax Calculation
- Billing Address Changes
- Supported Payment Methods
- 3D Secure / SCA
- Currency Conversion Discrepancies
- Enterprise Contract Billing