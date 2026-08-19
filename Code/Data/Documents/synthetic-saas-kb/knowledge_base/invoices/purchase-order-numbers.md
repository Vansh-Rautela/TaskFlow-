---
document_id: KB-INVOICE-003
title: Purchase Order Numbers
category: Invoices & Documentation
subcategory: Invoice References
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
  - purchase order
  - PO number
  - invoice
  - remittance
  - accounts payable
  - billing policy
---

# Purchase Order Numbers

This policy explains how purchase order (PO) numbers work on AcmeFlow Workspace invoices, when a PO number is required, how to provide or update one, and how PO references support payment and remittance matching.

## Overview

A purchase order number is a reference a customer's accounts payable team uses to track and approve spending. When a PO number is attached to an AcmeFlow workspace, it can be printed on invoices generated for that workspace so the invoice can be matched to the customer's PO.

PO numbers are supported on both standard self-service invoices and Enterprise custom invoices. For Enterprise workspaces, PO handling is typically defined in the signed agreement.

## When a PO Number Appears on an Invoice

A PO number appears on an invoice when:

- The workspace has a PO number on file, and
- The invoice is generated after the PO number was recorded.

A PO number on file does not change what you are billed for; it only adds a reference to the invoice. The invoice amounts are still based on the workspace's plan, seat count, and billing cycle.

## Providing a PO Number

To add or update a PO number on a self-service Pro workspace:

1. Sign in to AcmeFlow Workspace.
2. Open **Workspace Settings → Billing**.
3. Locate the purchase order field under invoice or billing details.
4. Enter the PO number and save.

Invoices generated after the PO number is saved will include it. If the PO number is added after an invoice is generated, the reference appears on the next invoice; the customer can also match the payment manually using the invoice identifier.

For Enterprise workspaces, provide the PO number through the billing contact or account manager so it can be included on custom invoices, along with any remittance details the agreement requires.

## Updating or Correcting a PO Number

If a PO number changes or was entered incorrectly, update the field in the Workspace Billing section. Invoices already generated keep the PO number they were created with. For Enterprise agreements, the account manager or billing operations can coordinate issuing a corrected or replacement invoice where the agreement allows.

## PO Numbers on Remittance and Payments

PO numbers and remittance references help the customer's accounts payable team match a payment to the correct invoice. When paying by wire transfer, include the invoice identifier and PO reference with the payment so it can be applied to the right invoice. A payment without the correct references may take longer to match.

## Example: PO on a Standard Self-Service Invoice

Brightpath Logistics is a Pro workspace on monthly billing with 8 seats. The billing contact saves PO number **PO-2026-8841** in the Workspace Billing section on March 20.

- Monthly base charge: 8 × $24.00 = **$192.00**
- Invoice **AF-2026-005812**, generated at the March cycle close, prints the line items and the reference **PO-2026-8841**.
- The payment amount is unchanged by the PO reference.

## Example: PO on a Custom Enterprise Invoice

Northgate Manufacturing is an Enterprise workspace whose agreement requires a PO number on every invoice. The PO number on file is **PO-88213**.

- The quarterly invoice **AF-2026-002517** prints the base charge, tax, total, and the reference **PO-88213**.
- The invoice also shows the remittance details and net payment terms from the agreement.
- Northgate's accounts payable matches the wire payment to the invoice using the PO reference.

## Common Questions

**Does adding a PO number change my charges?**
No. A PO number is a reference only and does not affect amounts billed.

**Will my existing invoices get the new PO number?**
No. The PO number appears on invoices generated after it is saved. Existing invoices keep the reference they were created with.

**Do Free workspaces need a PO number?**
Free workspaces are not charged and do not generate invoices, so no PO number is needed.

## Agent Guidance

When a customer asks where their PO number should appear, confirm whether the workspace is Pro or Enterprise, whether the PO number is on file, and which invoice they are looking at. A PO reference is verified against the account's billing settings and the generated invoice; it is never answered from general knowledge.

## Related Documentation

- Enterprise Custom Invoice Requirements
- Invoice Line Item Breakdown
- Invoice Generation & Delivery
- Billing Address Changes
- Supported Payment Methods
- Enterprise Contract Billing