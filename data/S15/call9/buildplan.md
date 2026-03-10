# Build Plan: Call9 2026

## Overview

The 2026 rebuild targets mid-size skilled nursing facilities (100–250 beds) in Medicare Advantage-dense markets with a hybrid subscription + shared-savings model. The core product is a clinical care specialist (paramedic/nurse) embedded on-site, connected to remote ER physicians via AI-assisted triage and real-time diagnostic hardware—reducing unnecessary hospital transfers while automating billing for remote patient monitoring and avoided admissions.

The market shift is permanent: CMS removed its rural-only telehealth restriction in 2020, and Medicare Advantage now covers 50+ million seniors with financial incentives to keep patients out of hospitals. Call9's clinical model was never the problem—its reimbursement strategy was. This rebuild locks in value-based contracts with MA payers upfront, eliminating the fee-for-service trap that killed the original company.

Go-to-market is direct enterprise sales to SNF operators, with MA payer referrals as a secondary channel. Differentiation comes from capital-efficient staffing (marketplace-integrated paramedics, not W-2 employees from day one), AI-powered documentation that reduces clinician burden, and a standardized outcomes dashboard that makes avoided-hospitalization savings visible and contractible. Win by being the only player that's both clinically rigorous and financially aligned with how nursing homes actually get paid in 2026.

## Why Now?

The single most important change since Call9's 2019 failure is the permanent removal of Medicare's rural-only telehealth restriction. CMS's March 2020 COVID-19 emergency waivers eliminated the geographic billing cap that Timothy Peck explicitly identified as making Call9's unit economics unworkable. The Consolidated Appropriations Act of 2023 extended most of these telehealth flexibilities through at least 2024, and subsequent legislation has continued to preserve urban SNF telehealth billing. Call9 shut down nine months before this change. A rebuilt company launches into a fundamentally different reimbursement environment.

Three additional regulatory shifts compound this opening. First, CMS clarified and expanded Remote Patient Monitoring CPT codes (99453, 99454, 99457, 99458) between 2019 and 2022, creating a direct billing pathway for the connected device data — EKG readings, vitals, point-of-care labs — that Call9's hardware kits generated but could not monetize. Second, the ACO REACH model (launched 2023) and expanded CMMI value-based care programs now provide the legislative infrastructure for shared-savings contracts in post-acute settings that the never-passed RUSH Act was meant to create. Third, CMS's Minimum Staffing Rule for nursing homes (finalized 2024) is intensifying facility-level demand for supplemental clinical coverage.

Market size has moved decisively in this direction. The U.S. telehealth market grew from approximately $3 billion in 2019 to over $28 billion in 2023 (per McKinsey & Company estimates), with post-acute and SNF telehealth now a validated sub-category. SNF registered nurse vacancy rates exceeded 20% in many markets per CMS workforce data, creating facility willingness to pay for embedded clinical staffing that did not exist at the same intensity during Call9's 2015–2019 operation. Competitors like DispatchHealth and Medically Home have raised $200 million-plus rounds validating the at-home and post-acute acute care model. The demand Call9 assumed but could not commercially validate at scale is now empirically confirmed.

Distribution infrastructure has also matured. Curve Health — Peck's own 2020 rebuild — demonstrated that the SNF telehealth category can attract Lightspeed-caliber capital and close payer contracts post-waiver. That proof of concept is the clearest possible signal that the original thesis was correct and the timing was wrong.

---

## Current Market Analysis

### Market Size

The U.S. skilled nursing facility market encompasses approximately 15,000 licensed facilities housing roughly 1.3 million residents at any given time, a figure that has remained relatively stable since Call9's operation. The financial opportunity has expanded significantly: the broader post-acute telehealth addressable market is estimated in the tens of billions annually in avoidable Medicare hospitalization costs, though a precise 2026 figure specific to SNF telehealth is not available in the research provided. What is documented is that the telehealth market overall grew roughly 9x between 2019 and 2023, and SNF-specific telehealth has moved from experimental to reimbursable.

## Competition Map and Gaps

The competitive landscape in 2026 is meaningfully more crowded than 2019, but no single player has replicated Call9's full model at scale.

- **Curve Health** (founded April 2020, $6M seed from Lightspeed): The most direct successor, built on Call9's own technology by Peck himself. Its specific weaknesses are not fully documented in available research, but as a seed-stage company in 2020, it likely remains subscale relative to the full SNF market opportunity.
- **DispatchHealth** (raised $200M+): Focuses on in-home acute care rather than SNF-embedded staffing; lacks the 24/7 on-site presence model and SNF-specific payer contracting expertise.
- **Medically Home** (raised $110M+): Targets hospital-at-home, not nursing home emergency response; different customer and reimbursement structure.
- **Traditional telemedicine platforms (Teladoc, Amwell)**: Offer physician video access without on-site clinical presence; clinically insufficient for SNF emergencies requiring hands-on assessment.
- **The 911 system**: Still the default incumbent behavior; free, familiar, and legally defensible for facility administrators.

The gap that remains open: no competitor has combined 24/7 on-site clinical staffing, connected diagnostic hardware, AI-assisted triage, and a pure value-based shared-savings contract structure at meaningful national scale. The original Call9 insight — that the clinical and economic value requires physical presence plus remote physician oversight — has not been commoditized.

## Demand Signals from Adjacent Products

SNF staffing platforms Clipboard Health and IntelyCare have demonstrated that flexible, on-demand placement of paramedics and EMTs into nursing facilities is operationally viable at scale — directly addressing the cost structure that required Call9 to employ 200 people to serve 12 facilities. RPM platform adoption in post-acute settings has accelerated since 2022, validating facility and payer appetite for connected device data. Medicare Advantage enrollment surpassed 50% of all Medicare beneficiaries in 2023 (per KFF), expanding the payer base most aligned with avoided-hospitalization incentives.

---

## Recommended MVP

## Core Features

### Flexible On-Site Clinical Care Specialist Staffing via Marketplace Integration

Rather than directly employing all CCS staff as W-2 employees from day one, the rebuilt platform integrates with existing SNF staffing marketplaces (Clipboard Health, IntelyCare) to source and credential paramedics and EMTs for on-site shifts, transitioning high-performing staff to direct employment as facilities scale. This directly addresses the cost structure that required 200 employees for 12 facilities — the original's most economically punishing feature. The CCS role remains the clinical core of the product; the staffing model becomes variable rather than fixed.

## Connected Diagnostic Hardware Kit with RPM Billing Integration

Each facility receives a standardized kit: EKG, pulse oximeter, point-of-care lab panel, and video-enabled tablet. Critically, the platform automatically generates CPT code documentation for RPM billing (99453, 99454, 99457, 99458) from device data, creating a reimbursement stream that did not exist at scale during Call9's operation. The original had the hardware; it lacked the billing infrastructure to monetize the data it generated.

## AI-Assisted Triage and Clinical Decision Support

Ambient documentation via tools comparable to Nuance DAX (Microsoft, available at scale since 2023) captures encounter notes in real time, reducing physician documentation burden and enabling a smaller remote physician panel to handle higher encounter volume. Structured triage scoring surfaces automatically before the physician joins the call, compressing time-to-decision. The original relied entirely on physician cognitive load; this layer improves revenue-per-physician economics.

## Value-Based Shared-Savings Contract Engine

A standardized contract template and outcomes dashboard designed specifically for Medicare Advantage payers, presenting avoided-hospitalization data in the format payers need to execute shared-savings agreements. This directly addresses the failure mode where Aetna and UnitedHealthcare declined to create value-based contracts because Call9 lacked the reporting infrastructure to make the case compellingly at their scale.

## Family and Care Team Communication Layer

Real-time encounter notifications and post-encounter summaries delivered to designated family members and the facility's attending physician. This was present in the original but undermonetized; in 2026 it serves as a retention and differentiation feature for facility administrators managing family satisfaction scores.

## What We Will NOT Build

- Community paramedicine division (distraction from core SNF market)
- Transportation partnerships (Lyft integration was a premature adjacency)
- Direct-to-consumer telehealth features
- Proprietary staffing recruitment infrastructure before reaching 20 facilities

## Success Metrics

- 10 SNF contracts signed within 12 months of launch
- ≥70% hospital transfer avoidance rate (below Call9's validated 80% to set a conservative threshold)
- RPM billing revenue covering ≥30% of per-facility operating costs within 6 months of go-live
- At least 2 signed Medicare Advantage shared-savings contracts within 18 months
- CCS staffing cost per facility ≤60% of Call9's implied ratio at shutdown

---

## Go-to-Market Strategy

### Target Customer Segment

The initial target is mid-size skilled nursing facilities (100–250 beds) in markets with Medicare Advantage penetration above 40% — specifically the Sun Belt states (Florida, Texas, Arizona) where SNF density is high, MA enrollment is above the national average, and the rural-only restriction that trapped Call9 in New York is irrelevant. This is a deliberate departure from Call9's New York concentration, which maximized clinical density but minimized reimbursement eligibility. Facility administrators at chains of 3–10 facilities are the primary buyer, because a single signed agreement can deploy across multiple sites, improving sales efficiency.

## Primary Distribution Channel and Tactics

The primary channel is direct enterprise sales through SNF regional and corporate operations directors, supplemented by referrals from Medicare Advantage plan medical directors who have financial incentives to reduce hospitalization rates. Call9's original sales motion — founder living in a nursing home — was the right instinct; the rebuilt company should hire 2–3 former SNF operators as clinical sales leads who can navigate facility administrator trust dynamics. Secondary channel: present outcomes data at the American Health Care Association (AHCA) annual conference, the primary SNF industry gathering, to build category credibility.

## Pricing Strategy

A hybrid model, structured to avoid the strategic ambiguity that destroyed Call9. The base layer is a per-facility subscription fee covering platform access, hardware kit, and CCS coordination — priced to cover direct costs with modest margin. The growth layer is a shared-savings arrangement with Medicare Advantage payers, structured as a percentage of documented avoided-hospitalization costs. RPM billing revenue flows to the company, not the facility, as compensation for device management. This structure means the company is never dependent on a single revenue stream and never has to choose between fee-for-service and value-based positioning — the subscription is fee-for-service, the payer contract is value-based, and they serve different stakeholders.

## Differentiation vs. 2026 Competitors

Against Curve Health: deeper AI-assisted clinical decision support and a more capital-efficient staffing model. Against DispatchHealth and Medically Home: SNF-specific payer contracting expertise and 24/7 on-site presence rather than episodic dispatch. Against traditional telemedicine: the physical CCS presence that makes emergency encounters clinically meaningful. The core differentiation is the same as Call9's — no one else has the full stack — but the 2026 version is built on a reimbursement foundation that can actually support it.
