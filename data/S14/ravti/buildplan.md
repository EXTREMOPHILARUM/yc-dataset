# Build Plan: Ravti 2026

## Overview

Ravti (2012–2020) built a platform to digitize, manage, and procure HVAC systems for commercial property owners — solving a real problem with genuine early traction — but ultimately sold to Building Engines in 2020 for an undisclosed sum after failing to break out of the point-solution trap in a market where Yardi, MRI, and Building Engines controlled distribution. The technology landed inside JLL ten months later via a $300M acquisition, confirming the thesis was right but the vehicle was wrong.

What has changed is structural: open APIs from incumbent platforms now allow integration rather than competition, computer vision eliminates the labor-intensive onboarding that killed unit economics, IoT sensor costs have dropped 80–90%, and SEC climate disclosure rules have converted HVAC data from a nice-to-have into a compliance requirement for publicly traded REITs. The rebuild is a compliance-first HVAC intelligence layer that plugs into Yardi and MRI as a native module — capturing the value Ravti created without fighting the distribution war that destroyed it.

---35:Tbac,

## Why Now?

The single most important change since Ravti's failure is that the incumbent property management platforms — Yardi, MRI Software, and AppFolio — now publish open APIs, transforming the competitive dynamic from confrontation to integration. In 2014–2020, Ravti had to convince institutional property managers to adopt a standalone tool outside their system of record. In 2026, a rebuilt Ravti can live inside Yardi Voyager or MRI Property Management as a certified module, surfacing HVAC intelligence directly in the workflow where building managers already spend their day. The distribution ceiling that forced the original company to sell is now a distribution channel.

The second structural shift is regulatory. The SEC's climate disclosure rules, finalized in 2024 for large accelerated filers, require publicly traded REITs and large property owners to report Scope 1 and Scope 2 emissions — of which HVAC systems are the dominant source in commercial buildings, accounting for roughly 40% of building energy consumption (U.S. DOE; specific 2026 figure not independently verified here). This converts HVAC equipment-level data from an operational convenience into a compliance obligation. Ravti was collecting exactly this data in 2017 with no regulatory tailwind; the rebuild launches into a mandatory market.

The Inflation Reduction Act (2022) adds a financial incentive layer: commercial HVAC upgrades meeting efficiency standards qualify for tax credits of up to 30% under Section 179D and related provisions, creating direct ROI for the capital expenditure planning use case Ravti's ASHRAE scoring module was designed to support.

On the technology side, three capability shifts matter:

- **Computer vision via Google Cloud Vision API and AWS Rekognition** (both reaching commercial-grade equipment classification accuracy by 2022–2023) can now auto-identify HVAC make, model, and approximate age from a smartphone photo, eliminating the manual barcode-tagging workflow that was Ravti's most expensive onboarding step.
- **IoT sensor hardware** has dropped from $150–300 per unit in 2015 to $15–40 per unit in 2024–2025 (industry estimates; specific vendor pricing varies), making real-time equipment monitoring economically viable for mid-market property owners previously priced out.
- **Large language models** (GPT-4, March 2023; Claude 3, March 2024) can parse unstructured service invoices, vendor contracts, and triple-net lease clauses to auto-populate equipment records and flag compliance violations — eliminating the manual data entry that made Ravti's tenant compliance module expensive to operate.

The Vertical SaaS market has also matured as a proof point: Procore's $10B+ market cap and Building Engines' $300M exit to JLL demonstrate that enterprise buyers in property management will pay for specialized workflow software at scale — a validation that was still being established when Ravti raised its last seed round in January 2017.

---

## Current Market Analysis

### Market Size

Ravti framed its addressable market at $1 billion in August 2014, representing approximately 32% of commercial real estate operating spend attributable to HVAC. The commercial real estate operations software market has grown substantially since then — the global proptech market was valued at approximately $18.2 billion in 2023 and is projected to reach $86.5 billion by 2032 (Grand View Research, 2023). The specific HVAC software sub-segment size in 2026 is not independently verified in the research report, and this plan will not fabricate a precise figure. What is documented: the regulatory and IRA incentive shifts described above have expanded the buyer universe beyond operational efficiency buyers to include compliance buyers — a structurally different and typically less price-sensitive customer category.

## Competition Map

The current competitive landscape has four meaningful players, each with a specific weakness:

- **JLL's Building Engines (Prism HVAC module):** The direct heir to Ravti's technology. Its weakness is captivity — it is only accessible to Building Engines customers, and JLL's enterprise sales motion means it is effectively unavailable to mid-market property managers managing portfolios under 5 million square feet. It also carries JLL's conflict of interest: JLL sells facilities management services, creating buyer skepticism about whether the software is optimizing for the owner or for JLL's service revenue.
- **Yardi Energy:** Covers utility and energy management broadly but lacks equipment-level HVAC inventory and vendor procurement functionality. Strong on reporting; weak on operational workflow.
- **ServiceChannel / Corrigo (JLL subsidiary):** Facilities management and work order platforms with HVAC work order capability but no equipment inventory intelligence, no ASHRAE-based CapEx scoring, and no tenant compliance tracking.
- **UpKeep / Limble CMMS:** Computerized maintenance management systems with HVAC asset tracking, but built for in-house maintenance teams rather than third-party property managers, and lacking procurement marketplace and compliance reporting features.37:T4cb,Maintain Ravti's per-square-foot SaaS model, priced at $0.03–0.06 per square foot annually (specific pricing requires market validation; this range is illustrative based on comparable proptech SaaS benchmarks). For a 5M square foot portfolio, this implies $150,000–$300,000 ARR per customer — consistent with enterprise SaaS expectations.

Stress-testing against free alternatives: the primary free alternative is a property manager's existing Yardi or MRI work order module, which tracks HVAC work orders but does not provide equipment inventory intelligence, ASHRAE scoring, or SEC-formatted emissions reporting. The compliance reporting feature is the critical differentiator here — a REIT facing SEC disclosure requirements cannot accomplish that with a work order log. Group chats and spreadsheets are the real free alternative for smaller operators, but the target segment (institutional REITs) has already moved past spreadsheet tolerance for compliance workflows. The IRA tax credit optimizer provides a calculable ROI: for a portfolio replacing 50 units annually at $8,000 average cost, a 25% tax credit represents $100,000 in savings — exceeding the annual software cost at the low end of the pricing range.38:Ta6c,

## Demand Signals from Adjacent Products

The growth of ESG reporting platforms (Measurabl, Deepki, Arcadia) targeting commercial real estate owners signals that institutional property managers are actively purchasing compliance-adjacent software. These platforms need equipment-level data that none of them generate natively — creating a potential integration and data-supply relationship for a rebuilt Ravti.

## Defensibility Analysis

The honest answer to platform commoditization risk is: partial. Yardi and MRI could build HVAC intelligence modules natively. The structural argument against them doing so is threefold: (1) their development roadmaps are driven by their largest customers' requests, and HVAC-specific intelligence has historically not been a top-10 request from enterprise property managers; (2) the computer vision and LLM-based onboarding workflow requires AI product expertise that is not core to either company's engineering culture; and (3) the procurement marketplace layer — aggregating vendor pricing across a portfolio — requires vendor network development that platform companies have consistently declined to build because it creates channel conflict with their existing vendor integrations. The risk is real and should be monitored; the rebuild's defensibility depends on building the vendor network and compliance data layer faster than incumbents are willing to prioritize it.

---

## Recommended MVP

## Core Features

### Photo-First Equipment Inventory (Computer Vision Onboarding)

A mobile app that allows a building technician to photograph any HVAC unit and receive an auto-populated equipment record — make, model, estimated age, and condition flag — within seconds, using Google Cloud Vision API or AWS Rekognition. This directly eliminates Ravti's most expensive onboarding step: the manual barcode-tagging workflow that required field technicians and drove up customer acquisition cost. The original Ravti required physical site visits with barcode equipment; the rebuild requires only a smartphone already in every technician's pocket. Success threshold: onboarding a 500,000 square foot portfolio should require no more than one day of field time.

## Compliance Reporting Dashboard (SEC / ESG Output)

An automated reporting layer that aggregates equipment-level data into the emissions and energy efficiency formats required by SEC climate disclosure rules and common ESG frameworks (GRESB, ENERGY STAR). This feature did not exist in the original Ravti and is the primary reason compliance buyers — publicly traded REITs and institutional asset managers — will pay for the rebuild where they would not have paid for the original. It transforms the product from an operational tool into a regulatory necessity. Target output: a one-click GRESB-ready HVAC emissions report.

## IRA Tax Credit Optimizer (CapEx Planning)

An ASHRAE-based equipment scoring module — inherited from Ravti's original product — augmented with IRA Section 179D eligibility analysis. For each unit flagged for replacement, the module calculates the net cost after applicable tax credits and surfaces vendor quotes from the procurement network. This directly monetizes the IRA incentive shift and gives property managers a data-driven replacement decision rather than a vendor-driven one. Unlike the original Ravti's CapEx module, this version integrates tax credit calculations that can reduce effective replacement costs by 20–30%.

## Yardi / MRI Native Integration

A certified module integration with Yardi Voyager and MRI Property Management, surfacing all three features above inside the property manager's existing system of record. This is the architectural decision that most directly addresses Ravti's original failure mode. It is not a feature in the traditional sense — it is the distribution strategy expressed as a product decision.

## What We Will NOT Build (MVP)

- IoT hardware. Sensor costs have dropped, but hardware manufacturing is execution complexity the original team acknowledged was "really challenging." Partner with existing IoT vendors (Disruptive Technologies, Samsara) via API rather than manufacturing sensors.
- Tenant compliance tracking. This is a valuable feature but requires legal workflow integration that adds scope without accelerating the compliance buyer acquisition thesis. Build in Year 2.
- A consumer-facing marketplace. Vendor procurement is a Year 2 revenue layer after inventory data reaches critical mass.

## Success Metrics

- 10 paying customers (institutional property managers, minimum 1M sq ft each) within 6 months of launch
- 50M square feet of equipment inventory digitized within 12 months (exceeding Ravti's reported all-time figure)
- Net Revenue Retention > 110% at 12 months
- Average onboarding time < 2 days per 1M square feet

## Cold-Start Problem

This product does not depend on local density or network effects in the traditional sense — a single property manager with a 2M square foot portfolio derives full value from the inventory and compliance features on day one. The procurement marketplace layer (Year 2) will require vendor network density, but the MVP deliberately defers that feature to avoid the cold-start problem entirely.

---

## Go-to-Market Strategy

### Target Customer Segment

Publicly traded REITs and institutional asset managers managing commercial portfolios of 2–20 million square feet, with a primary focus on retail and industrial property types where HVAC represents 30% of operating budgets and triple-net lease structures create tenant compliance complexity. These buyers are subject to SEC climate disclosure requirements, making HVAC data a compliance obligation rather than a discretionary purchase. Secondary target: mid-market property management firms (500K–2M sq ft) that manage portfolios on behalf of institutional owners who are imposing ESG reporting requirements downstream.

## Primary Distribution Channel

The Yardi and MRI partner marketplaces are the primary distribution channel. Both platforms maintain certified partner programs (Yardi Marketplace, MRI's partner ecosystem) with direct access to their customer bases. A rebuilt Ravti should pursue Yardi certification in the first six months — Yardi's customer base includes the majority of institutional property managers in the U.S. (specific customer count not independently verified). Secondary channel: direct outreach to REIT sustainability officers and CFOs, who are now the economic buyers for compliance-driven software purchases — a buyer persona that did not exist for Ravti in 2017.

## Pricing Strategy

# Ducter

## 1. Overview

Ducter is a compliance-first HVAC intelligence platform for commercial property managers — a modern revival of Ravti — that digitizes equipment inventory via computer vision, generates SEC/ESG-ready emissions reports, and calculates IRA tax credit savings for equipment replacement decisions. It serves institutional property managers and publicly traded REITs who face mandatory climate disclosure requirements and need equipment-level HVAC data to satisfy SEC Scope 1/2 reporting, GRESB submissions, and ENERGY STAR benchmarking. Unlike standalone point solutions, Ducter integrates natively with Yardi Voyager and MRI Property Management so property managers never leave their existing system of record.

---

## 2. Core Features

**Equipment Inventory**
- Photo-based onboarding: upload smartphone photo of any HVAC unit → computer vision auto-populates make, model, estimated age, refrigerant type, tonnage, and condition flag
- Manual entry fallback with structured form (make/model lookup from curated equipment database)
- Barcode/QR code generation and printing per unit for future field scans
- Bulk CSV import for existing inventory records
- Equipment detail page: full history log (service events, photos, notes), ASHRAE life expectancy score, replacement priority flag
- Portfolio-level equipment map view (building → floor → unit hierarchy)

**Properties & Portfolio Management**
- Create and manage properties with address, square footage, property type (retail, industrial, office), and ownership structure (fee simple, triple-net)
- Assign buildings to portfolios; support multi-portfolio organizations
- Tenant assignment per unit for triple-net lease tracking
- Role-based access: Organization Admin, Portfolio Manager, Property Manager, Field Technician

**Compliance Reporting**
- One-click GRESB-ready HVAC emissions report (Scope 1 refrigerant leakage, Scope 2 energy consumption per unit)
- SEC climate disclosure export (CSV + PDF) aligned with final 2024 SEC climate rules
- ENERGY STAR Portfolio Manager data export format
- Scheduled auto-generation: monthly, quarterly, annual
- Report history with download archive

**IRA Tax Credit Optimizer (CapEx Planning)**
- ASHRAE Standard 180-based equipment scoring: remaining useful life estimate per unit
- Replacement priority queue: units ranked by age, condition score, and energy inefficiency
- IRA Section 179D eligibility calculator: net cost after 30% tax credit per qualifying replacement
- Portfolio-level CapEx projection: 1-year, 3-year, 5-year replacement cost with and without tax credits
- Export CapEx plan as PDF for board/investor reporting

## Differentiation vs. 2026 Competitors

Against JLL/Building Engines: vendor-neutral positioning. A rebuilt Ravti has no facilities management services revenue to protect, eliminating the conflict of interest that makes Building Engines' HVAC module suspect to sophisticated buyers. Against Yardi Energy: equipment-level granularity and procurement functionality that Yardi Energy does not offer. Against CMMS platforms (UpKeep, Limble): compliance reporting output and institutional property manager workflow integration that CMMS tools are not designed to produce.
