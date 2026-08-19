---
document_id: KB-ENT-001
title: Enterprise Contract Billing
category: Enterprise & Custom Terms
subcategory: Enterprise Billing
document_type: Enterprise Policy
audience:
  - Billing Operations
  - Account Management
  - Enterprise Support
status: active
version: "1.0"
effective_date: "2026-01-01"
last_reviewed: "2026-07-01"
owner: Enterprise Operations
product: AcmeFlow Workspace
tags:
  - enterprise
  - contract billing
  - custom pricing
  - purchase order
  - net terms
  - wire transfer
  - master subscription agreement
---

# Enterprise Contract Billing

Enterprise customers subscribe to AcmeFlow Workspace under a signed agreement rather than the standard self-service plans. Billing for these accounts is defined in the contract: pricing, billing frequency, payment terms, and related conditions can all be customized. This document explains how enterprise contract billing works and what an agent must check before answering billing questions for an enterprise account.

Enterprise terms are never universal. Every detail on an enterprise account is governed by the signed agreement, so the agreement is the primary reference for any billing question.

## Enterprise Pricing Is Custom

Enterprise pricing is custom and set at contract signing. There is no published universal Enterprise price, and AcmeFlow does not maintain a standard Enterprise rate list.

An enterprise agreement may include any combination of the following, as negotiated:

- Volume discounts.
- Contract-specific seat commitments.
- Annual or quarterly billing cycles.
- Purchase orders (POs) and custom invoices.
- Annual upfront billing and minimum commitments.
- Net payment terms.
- Contract-specific refund terms.
- Uptime credits and a custom SLA.
- Additional services such as SSO/SAML, SCIM, and advanced audit controls.
- A dedicated account manager.
- Security reviews, security questionnaires, and SOC 2 documentation requests.

Because the configuration varies by customer, an agent should never state a default Enterprise price, discount, or billing frequency. If a number is needed, it must be retrieved from the agreement, or presented as an explicit example.

**Example (labeled):** BlueSky Analytics Inc. signed a Master Subscription Agreement (MSAA-2026-0417) for 150 committed seats billed annually in advance at a contract-specific per-seat rate. The rate of $18 per user per month in this example is a negotiated figure for that contract only, not a standard Enterprise price.

## Billing Frequency and Payment Terms

Enterprise billing cycles are defined in the agreement. Common structures include monthly, quarterly, annual, and annual upfront billing. The agreement also defines the payment terms for invoices.

Net payment terms are common on enterprise accounts. For example, an invoice may be payable within 30 or 45 days of issue. The specific net terms are contract-specific.

Wire transfer is available for qualifying Enterprise customers. Whether a given account qualifies, and the exact remittance details, are confirmed with the account's billing arrangement.

**Example (labeled):** The agreement for Meridian Health Partners, a qualifying Enterprise customer, specifies quarterly billing with Net 30 payment terms and payment by wire transfer. The payment schedule and remittance instructions are recorded in the contract, not in the standard billing settings.

## Invoices and Purchase Orders

Invoices for enterprise accounts are generated at each billing cycle close and are available in the Workspace Billing section. An invoice notification is emailed to the workspace billing contact.

Enterprise agreements frequently require custom invoices and purchase order references. When an agreement calls for a PO, the PO number appears on the invoice, and invoice line items reflect the subscription base charge, prorations, seat changes, taxes, and credits where applicable.

**Example (labeled):** After the annual renewal for BlueSky Analytics Inc. on February 1, 2026, AcmeFlow issued invoice AF-2026-004821, referencing purchase order PO-8821-GH. The invoice reflects the committed seat count for the new contract year.

For details on how PO numbers are handled and what a custom invoice must contain, see Purchase Order Numbers and Enterprise Custom Invoice Requirements.

## Enterprise Override of Self-Service Policies

Standard self-service policies apply to Free and Pro accounts. Enterprise accounts are different: the customer's signed Enterprise agreement takes precedence over the standard self-service policy where the two differ.

Practical implications:

- Cancellation and access end dates may follow the agreement rather than the self-service cancellation flow.
- Refund terms may differ from the standard 30-day refund window, including prorated refunds where the contract explicitly permits them.
- Data retention may be longer or shorter than the standard 60 days after subscription termination.
- Dunning schedules may differ from the standard grace and suspension timeline.

An agent handling any of these for an enterprise account should retrieve the applicable terms from the signed agreement before committing to an answer.

**Example (labeled):** Lumina Financial Solutions' agreement defines a 90-day data retention period after termination, which overrides the standard 60-day retention. The retention figure for this contract is contract-specific and does not change the standard policy for other customers.

## What an Agent Must Retrieve From the Agreement

For any enterprise billing question, verify against the signed agreement:

- The contracted price and any negotiated discounts or rates.
- The billing cycle, including whether billing is upfront, annual, quarterly, or monthly.
- Seat commitment levels and how seat changes are billed.
- Payment terms, including net terms and allowed payment methods such as wire transfer.
- Refund, credit, and retention terms that differ from standard policy.
- Invoice and purchase order requirements, including the PO number format used.

If the agreement is silent on a point, treat the standard self-service policy as the default and confirm with Billing Operations before finalizing the answer.

## Related Documentation

- Volume Discount Tiers
- Dedicated Account Manager
- SLA & Uptime Credits
- Security Questionnaire & SOC 2 Requests
- Enterprise Custom Invoice Requirements
- Purchase Order Numbers
- Plan Tiers Overview
- Supported Payment Methods
- Data Retention After Cancellation