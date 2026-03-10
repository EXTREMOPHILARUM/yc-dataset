# Build Plan: Iris Automation 2026

## Overview

Iris Automation was a drone safety software company founded in 2015 that built Casia, a computer vision-based detect-and-avoid (DAA) system enabling drones to sense and evade non-cooperative aircraft — the critical missing piece for commercial beyond visual line of sight (BVLOS) operations. Backed by Bessemer, Sony, and Verizon Ventures, the company raised $23M–$35M, achieved regulatory approvals in nine countries, and was acquired by uAvionix in October 2023 at an undisclosed price after the FAA's BVLOS rulemaking delays kept its addressable market artificially small and the 2023 capital contraction closed off its Series C runway.

The rebuild thesis is this: the FAA's 2023 BVLOS NPRM has transformed the regulatory environment from an indefinitely closed door into an actively opening one, modern edge AI chips deliver 10–100x more inference performance per watt than 2019 hardware, and foundation vision models slash the training data burden that cost Iris Automation 7,000+ test flights — meaning a new entrant can build a software-defined, subscription-priced DAA compliance layer that reaches profitability before the next capital contraction, not after it.

---34:T9e6,

## Why Now?

### The single most important change: the FAA published its BVLOS NPRM in 2023.

Iris Automation's entire commercial life was spent waiting for a regulatory window that never opened. The FAA's Notice of Proposed Rulemaking for BVLOS operations, published in 2023, fundamentally changes that calculus. For the first time, the agency is moving toward standardized, scalable BVLOS rules rather than the case-by-case waiver process that kept Iris Automation's addressable market structurally tiny. A DAA company founded in 2026 is building into an opening regulatory window — the exact inverse of Iris Automation's position. The final rule timeline remains uncertain (this is the FAA; caution is warranted), but the direction is unambiguous and the rulemaking machinery is now in motion rather than stalled.

**Hardware and AI capability have leapfrogged the 2019 baseline.** NVIDIA's Jetson Orin (released 2022) delivers up to 275 TOPS of AI inference performance at under 60W — roughly 10–100x the compute density available when Casia launched commercially. Qualcomm's Flight RB5 5G platform (2021) was purpose-built for drone autonomy at drone-compatible size, weight, and power (SWaP) constraints. These chips make real-time computer vision DAA feasible on commodity hardware without the custom silicon investment Iris required.

**Foundation vision models eliminate the 7,000-flight training data moat.** Meta's SAM 2 (July 2024) and DINOv2 (April 2023) are pre-trained on massive visual datasets and can be fine-tuned for aircraft detection with dramatically less proprietary flight data than Iris Automation needed to accumulate. The training data barrier that took Iris four years to clear can now be cleared in months.

**Demand-side validation is no longer speculative.** Wing (Alphabet) surpassed 1 million commercial deliveries by 2023. Amazon Prime Air received FAA Part 135 approval. Zipline operates at commercial scale across multiple countries. AUVSI estimated that routine BVLOS operations could generate $34.4B in U.S. economic impact over the decade following rule publication — and that decade is now beginning. The use case Iris was building toward is proven; the market is real.

**Sensor costs have collapsed.** High-resolution camera sensors and supporting optics have dropped 60–80% in cost since 2019, driven by automotive AV programs (source: rebuild signals from research report). A Casia-equivalent sensor stack that cost thousands of dollars per unit in 2019 can now be sourced at a fraction of that price, enabling a lower hardware price point and improved unit economics.

---

## Current Market Analysis

**Market size.** The commercial drone services market has grown substantially since Iris Automation's founding. AUVSI projects that routine BVLOS operations will generate $34.4B in U.S. economic impact and 100,000 jobs over the decade following rule publication. McKinsey estimated the drone delivery market alone at $13B by 2030. Precise current market size figures for the DAA subsegment specifically are not publicly available — any number cited here would be an estimate, not a fact. What is clear is that the addressable market for DAA compliance tools expands dramatically as BVLOS rules move from waiver-by-exception to standardized approval, and that transition is now underway.

**Competition map and gaps.** The primary incumbent is uAvionix itself, which now holds Iris Automation's Casia IP alongside its ADS-B cooperative detection stack. uAvionix's weakness is integration complexity: it is a hardware-first company selling a combined cooperative/non-cooperative stack that requires significant per-aircraft certification work. It is not positioned to serve the long tail of smaller commercial operators who need DAA compliance but cannot absorb enterprise-level hardware costs or integration timelines. Daedalean (Swiss, well-funded) is focused on piloted aircraft autonomy and DO-178C/DO-254 certified avionics — a different regulatory track, higher-cost, and not optimized for the commercial drone operator segment. Percepto and Skydio have onboard autonomy capabilities but are vertically integrated into their own airframes, not selling DAA as a platform-agnostic compliance layer. No current competitor is offering a software-defined, subscription-priced DAA solution designed specifically for the mid-market commercial drone operator seeking BVLOS approval under the new NPRM framework.

**Demand signals from adjacent products.** The growth of drone-in-a-box platforms (Percepto, Skydio Dock, DJI Dock) signals that operators are investing in persistent autonomous operations — all of which require BVLOS compliance at scale. DroneUp, which partnered with Iris Automation, continues to expand its delivery network. These operators need DAA compliance as a recurring operational requirement, not a one-time hardware purchase.

**Defensibility against platform incumbents.** The honest answer is that uAvionix is the most direct platform threat, and it already holds the Casia IP. The rebuild's structural advantage is not technology secrecy — it is go-to-market positioning. uAvionix is selling upward to large enterprise operators and drone manufacturers. The rebuild targets the mid-market commercial operator segment that uAvionix's hardware-first model cannot serve economically. A software-defined, flight-hour subscription model creates switching costs through regulatory documentation history and approval records that accumulate over time — the longer an operator uses the platform, the more their compliance record is embedded in it. Additionally, the new NPRM framework will likely require ongoing DAA compliance documentation, not just one-time hardware certification, which structurally favors a SaaS model over a hardware sale. If uAvionix decides to build a competing SaaS tier, that is a real risk and should be monitored closely.

---

## Recommended MVP

### Core Feature 1: Software-Defined DAA on Commodity Hardware

A computer vision DAA application running on NVIDIA Jetson Orin or equivalent edge AI hardware, using DINOv2-fine-tuned models (April 2023) for non-cooperative aircraft detection. The operator purchases commodity hardware at cost; the DAA capability is delivered as a software subscription. This differs from the original Casia by decoupling the margin structure from hardware manufacturing — Iris Automation sold a proprietary hardware unit; the rebuild sells a software license that runs on hardware the operator can source independently, dramatically lowering the entry price and eliminating supply chain risk.

## Core Feature 2: BVLOS Compliance Documentation Engine

Automated generation of the safety case documentation required for BVLOS approval under the FAA NPRM framework, populated from the system's own flight logs and detection event records. This is the feature Iris Automation never built explicitly — the company provided the safety technology but left operators to assemble their own regulatory submissions. A compliance documentation layer creates direct, recurring value tied to the regulatory process itself, and it accumulates operator-specific data that becomes a switching cost. This feature does not exist in any current competitor's offering at the mid-market price point.

## Core Feature 3: Flight-Hour Subscription Billing

Pricing tied to flight hours rather than per-unit hardware sales, with a base platform fee plus per-hour usage. This aligns the company's revenue with operator activity — operators pay more when they fly more, which is when they are generating revenue — and creates a recurring revenue model that supports a SaaS valuation multiple rather than a hardware multiple. Iris Automation's hardware model meant revenue was lumpy and tied to new customer acquisition; this model generates revenue from the existing customer base as BVLOS operations scale.

**What we will NOT build:** Proprietary hardware, ground-based monitoring systems (Casia G's use case), piloted aircraft avionics, or cooperative ADS-B detection. The rebuild is a software layer on commodity hardware for non-cooperative detection. Cooperative detection is uAvionix's domain; the rebuild integrates with it rather than competing with it.

**Success metrics:** 50 paying commercial operators within 12 months of launch; $500K ARR within 18 months; average flight-hour subscription retention above 80% at 12 months; at least one operator using the compliance documentation engine to obtain BVLOS approval under the new NPRM framework.

**Cold-start note:** This product does not depend on network effects or local density. Each operator's DAA system functions independently. The cold-start problem is a sales problem, not a network problem — addressed in GTM below.

---

## Go-to-Market Strategy

**Target customer segment:** Mid-market commercial drone operators in the U.S. with 5–50 aircraft, operating in infrastructure inspection (utility lines, pipelines, cell towers) or precision agriculture, who are actively pursuing BVLOS approval under the new NPRM framework and cannot afford uAvionix's enterprise hardware stack or Daedalean's avionics-grade certification process. These operators have real revenue at stake from BVLOS operations, a clear regulatory compliance need, and no current solution priced for their scale.

**Primary distribution channel:** Direct outreach through AUVSI membership and the FAA's BEYOND program participant list — both of which are public records identifying operators already invested in BVLOS operations. The AUVSI Xponential conference (annual, ~10,000 attendees) is the single highest-density venue for this customer segment. Secondary channel: partnerships with drone airframe manufacturers (Wingtra, senseFly, Freefly) who sell into the same infrastructure inspection and agriculture segments and need a DAA compliance layer to offer their customers.

**Pricing strategy:** $500/month platform fee plus $15/flight hour, with a 12-month minimum commitment. At 20 flight hours per month — a conservative estimate for an active commercial operator — this is $800/month or $9,600/year. The stress test: operators currently accomplish basic airspace awareness through ADS-B receivers (~$500 one-time) and manual FAA coordination (free but slow). The rebuild's price is justified not by replacing those free tools but by providing the non-cooperative detection capability and compliance documentation that those tools cannot provide at any price — because the capability does not exist in a software-defined, mid-market form today. Operators who need BVLOS approval under the new NPRM cannot get there with a group chat and a $500 ADS-B receiver. The $9,600/year price is a rounding error against the revenue a BVLOS-approved operator generates from commercial contracts.

**Differentiation vs. 2026 competitors:** uAvionix sells hardware to enterprises; the rebuild sells software subscriptions to mid-market operators. Daedalean targets piloted aircraft certification; the rebuild targets commercial drone BVLOS compliance. No current competitor offers automated BVLOS compliance documentation generation at this price point. The rebuild's moat is the compliance record that accumulates in the platform over time — an operator's two-year flight history and safety case documentation is not portable to a competitor without significant re-certification work.
