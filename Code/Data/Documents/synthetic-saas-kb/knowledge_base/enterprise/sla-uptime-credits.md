---
document_id: KB-ENT-004
title: SLA & Uptime Credits
category: Enterprise & Custom Terms
subcategory: SLA & Uptime
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
  - SLA
  - uptime
  - service credit
  - 99.9
  - availability
---

# SLA & Uptime Credits

Service level agreements (SLAs) are available to Enterprise customers and are defined in the signed agreement. The standard Enterprise SLA target for AcmeFlow Workspace is 99.9% monthly uptime. Self-service plans do not include an SLA, so the SLA only applies where the agreement provides for it.

This document explains the SLA structure, how uptime is measured, and how service credits for missed uptime are handled.

## The Standard Enterprise SLA Target

The standard Enterprise SLA target is 99.9% monthly uptime for AcmeFlow Workspace. This target is defined per agreement, and the agreement may set a different target where negotiated.

Self-service plans (Free and Pro) have no SLA. Uptime credit requests apply only to accounts with a signed SLA.

**Example (labeled):** Meridian Health Partners' agreement sets an SLA target of 99.9% monthly uptime, matching the standard Enterprise target. The agreement for Optivus Manufacturing sets a tighter 99.95% monthly uptime target as a negotiated term of MSAA-2026-0551.

## How Uptime Is Measured

Uptime is measured against the AcmeFlow Workspace service. Downtime is measured in whole minutes, meaning partial minutes are not counted toward a downtime total.

Scheduled maintenance and force-majeure events are excluded from uptime calculations per the agreement. Customers should confirm which maintenance windows and exclusion events apply by reviewing their agreement.

## Service Credits Are Defined Per Agreement

Service credits for missed uptime are defined in each agreement. AcmeFlow does not publish a universal credit percentage. A credit amount is meaningful only in the context of the signed SLA.

If a customer reports missed uptime, the agent must consult the agreement to determine whether a credit applies and at what rate.

**Example (labeled):** Under the SLA in MSAA-2026-0417, BlueSky Analytics Inc. is entitled to a service credit equal to 5% of the monthly subscription charge for each full month the uptime target is missed. The 5% figure is an example of a negotiated credit rate for that contract; it is not a standard rate. In this example, the request would be recorded under the account's SLA terms rather than a generic credit policy.

## Requesting an Uptime Credit

The process for requesting an uptime credit is governed by the agreement. Generally:

- The customer reports the period of downtime with dates and times.
- AcmeFlow validates the reported downtime against uptime monitoring.
- If the downtime qualifies, a service credit is issued per the agreement's credit terms.
- The credit may be applied to the workspace credit balance or to a future invoice, depending on the contract.

**Example (labeled):** In this example, Meridian Health Partners reports a 45-minute outage on March 18, 2026. Because downtime is measured in whole minutes and the outage clears the monthly target, a credit under the agreement's terms is applied to invoice AF-2026-003877 issued the following billing cycle. Whether a credit applies in a real case must be verified against the account's SLA.

## What an Agent Must Retrieve From the Agreement

For any SLA question, retrieve from the signed agreement:

- The applicable uptime target, if different from the 99.9% standard.
- Exclusions such as scheduled maintenance and force-majeure events.
- The credit rate and how it is calculated.
- The claim and validation process, including any reporting deadlines.

If the account has no signed SLA, no uptime credits apply, and the customer should be directed to the appropriate plan documentation.

## Related Documentation

- Enterprise Contract Billing
- Volume Discount Tiers
- Dedicated Account Manager
- Plan Tiers Overview
- Credit Balance Application
- Invoice Generation & Delivery