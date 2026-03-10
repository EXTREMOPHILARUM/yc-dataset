# Build Plan: Anchor Health 2026

## Overview

Anchor Health 2026 targets independent home health agencies (50–200 Medicare patients) with a platform that turns compliance into revenue. The core insight: CMS Remote Patient Monitoring reimbursement codes (CPT 99453/99454/99457) now pay agencies $50–150 per patient monthly for connected vitals monitoring — but legacy platforms don't automate the billing. We do.

The product is a cellular-connected vitals hub (BP cuff, pulse ox, scale) paired with AI-generated clinical documentation and automated RPM claims submission. Agencies get a new $2,500–7,500 monthly revenue stream per 50 RPM patients with minimal operational lift. We're not selling a cost center; we're selling profit.

Go-to-market is direct outbound to agency administrators in high-reimbursement states (Texas, Florida, Ohio) plus referral partnerships with home health billing consultants. At $299/month base plus $49 per RPM patient, we hit unit economics that work for both sides immediately. The win: agencies see revenue impact in 90 days, not years.32:T8b9,

## Why Now?

## Current Market Analysis

## Market Size

The U.S. home health care market exceeded $150B in 2023, up from approximately $103B in 2018 (source: research report). The addressable technology layer — scheduling, EVV, billing, RPM, and clinical documentation software — is a subset of this figure; a precise current estimate is not available in the sources reviewed and should not be invented. What is documented is that vertical SaaS incumbents serving this market have achieved significant scale, validating the technology spend.

## Competition Map and Gaps

The current competitive landscape is dominated by legacy vertical SaaS players:

- **WellSky** (formerly Kinnser): Broad clinical and operational platform, strong Medicare billing compliance, but built on aging architecture with poor mobile UX and no native AI documentation layer. Agencies report slow implementation timelines.
- **Homecare Homebase**: Deep EVV and scheduling functionality, dominant in larger agency chains, but expensive for small-to-midsize agencies and not designed for RPM billing workflows.
- **AlayaCare**: Modern cloud architecture with mobile-first design, stronger in Canada than the U.S., limited CMS billing depth for American Medicare/Medicaid rules.
- **Axxess**: Targets smaller agencies with lower price points but offers minimal automation and no connected hardware integration.

**The Gap**: No current competitor combines RPM-enabled connected hardware, LLM-powered clinical documentation, and Medicare RPM billing automation in a single platform designed for independent agencies (10–200 patients). The incumbents were built before RPM reimbursement existed at scale and have not natively integrated it.34:T894,

## Demand Signals

Adjacent products confirm demand: Withings, iRhythm, and Best Buy Health's Current Health platform have all demonstrated that home-based connected monitoring generates patient and payer willingness to pay. The EVV mandate enforcement (2019–2021) proved agencies will adopt technology under compliance pressure. RPM billing is the next compliance-adjacent forcing function.

---

## Recommended MVP

## Core Features

## RPM-Integrated Connected Vitals Hub

A pre-configured, cellular-connected device kit (blood pressure cuff, pulse oximeter, weight scale) that automatically transmits readings to the agency dashboard, with CMS-compliant time-tracking built in to satisfy CPT 99457 billing requirements. This differs from the original Anchor Health hardware vision by using off-the-shelf FDA-cleared peripherals assembled into a branded kit via a contract manufacturer (Fictiv or equivalent), eliminating custom hardware development entirely. It matters because it converts the hardware layer from a cost into a direct Medicare billing line item — the structural change that makes the model viable.

## AI-Generated Clinical Documentation

Using GPT-4 or Claude 3 APIs, the platform auto-drafts OASIS assessments, care plans, and visit notes from structured intake data and caregiver voice inputs captured on mobile. Clinicians review and sign rather than author from scratch. This directly replaces the "operating solutions" layer Anchor Health could never staff, and reduces documentation time per visit by an estimated 40–60% (no agency-specific data available; figure based on analogous LLM documentation studies in adjacent clinical settings — verify with pilot data).

## RPM Billing Automation

Automated generation of CPT 99453/99454/99457 claims from device data logs, with eligibility checking and denial management workflows. This feature did not exist in any form in 2016 because the billing codes did not exist. It is the primary monetization engine and the clearest differentiation from incumbents who have bolted RPM onto legacy billing systems as an afterthought.

## Caregiver Mobile App with EVV

GPS-verified check-in/check-out satisfying state EVV mandates, integrated with the vitals hub and documentation layer. Keeps the platform compliant without requiring agencies to run a separate EVV vendor.

## What We Will NOT Build

No custom hardware silicon, no hospital-facing care coordination portal, no staffing marketplace, no proprietary telehealth video infrastructure, no Medicaid managed care contracting tools. These are scope expansions that killed the original company.

## Success Metrics

- 10 paying agencies within 6 months of launch (minimum $500/month per agency)
- RPM billing activation rate ≥ 70% of enrolled patients within 90 days
- Clinical documentation time reduction ≥ 30% validated by pilot agency time logs
- Gross margin ≥ 60% by month 12 (hardware kit sold/leased at cost; margin driven by software subscription)

---

## Go-to-Market Strategy

## Target Customer Segment

Independent home health agencies with 50–200 active Medicare patients, operating in states with high RPM reimbursement uptake (Texas, Florida, and Ohio are documented high-volume Medicare home health states — CMS data). These agencies are large enough to have a dedicated administrator making technology decisions but small enough to be underserved by WellSky and Homecare Homebase's enterprise sales motions. Owner-operators in this segment are actively looking for revenue diversification because Medicare reimbursement rate pressure is compressing margins; RPM billing is a concrete answer to that problem.

## Primary Distribution Channel and Tactics

The primary channel is direct outbound to agency administrators, supplemented by referral partnerships with home health billing consultants and Medicare compliance advisors — the trusted intermediaries these owners already pay for guidance. Tactics: (1) Publish a free "RPM Billing Readiness Calculator" that shows an agency's estimated monthly RPM revenue based on patient census — generates qualified inbound leads with demonstrated intent. (2) Exhibit at the National Association for Home Care & Hospice (NAHC) annual conference, where the target buyer concentrates. (3) Offer a 90-day pilot with one cohort of 10 patients at no software cost, agency pays only for hardware kit — removes adoption risk for a risk-averse buyer.

## Pricing Strategy

## Differentiation vs. 2026 Competitors

WellSky and Homecare Homebase sell compliance infrastructure; this platform sells a new revenue line. That reframe — from cost center to profit center — is the primary sales narrative and is not available to incumbents whose architecture predates RPM reimbursement. AlayaCare lacks U.S. Medicare billing depth. Axxess lacks RPM hardware integration. No current competitor owns the full loop: device → data → AI documentation → Medicare claim.
