# Build Plan: Atmos 2026

## Overview

Atmos was a San Francisco-based custom homebuilding marketplace that operated from 2018 until March 2025, raising $20 million from Khosla Ventures, Sam Altman, and others before shutting down after completing only ~50 homes — killed by a human-designer cost structure it never automated and a rate shock that collapsed its pipeline of in-progress clients who could no longer afford to close.

The rebuild thesis is simple: the one thing Atmos needed to work — AI that could replace human designers in translating buyer preferences into buildable, code-compliant floor plans — did not exist when Atmos was burning through its Series A, but it does now. The new version is a builder-facing SaaS platform that sells AI-generated, permit-ready home design packages directly to small regional builders, flipping the original model's fatal dependency on rate-sensitive consumer demand into a B2B subscription business that generates revenue whether or not any individual buyer closes.

---

## Why Now?

The single most important change since Atmos failed is that generative AI can now produce architecturally coherent, spatially valid residential floor plan variations in minutes — without a human designer in the loop. This is the precise capability Donahue identified as missing when he described Atmos as a "glamorized architecture firm" that "never replaced the humans." His own successor company, Drafted, launched in December 2025 with AI-generated floor plans and zero designers on staff, providing direct proof-of-concept that the automation gap has closed.

The specific enabling technologies are: diffusion models fine-tuned on architectural drawing datasets (commercially available since late 2023), GPT-4-class spatial reasoning (GPT-4, March 2023) for translating natural-language buyer preferences into structured design constraints, and AI-assisted code compliance tools like Symbium and Archistar that have matured sufficiently to flag zoning and setback violations before a plan reaches a permit office. Together, these compress what previously required 40–80 hours of designer time per engagement into a workflow measurable in minutes.

On the macro side, the Federal Reserve began cutting rates in September 2024. The 30-year fixed mortgage rate, while still elevated above 6.5% as of early 2026 (exact current figure unavailable at time of writing), has declined meaningfully from its 2023 peak above 8%, partially restoring affordability for the $400K–$800K buyer segment Atmos targeted. More durably, the National Association of Realtors estimated a U.S. housing deficit of 5.5 million units as of 2023 — a structural undersupply that makes demand for new construction less cyclical than it appeared in 2020.

Distribution channels unavailable to Atmos also now exist at scale. The Autodesk Construction Cloud marketplace, Procore's app marketplace (serving 16,000+ construction firms as of 2024, per Procore's investor materials), and BuilderTrend's integration ecosystem provide direct access to the small regional builder segment — the same builders Atmos paid $20,000 to acquire as marketplace participants — without requiring Atmos-style consumer marketing spend.

---

## Current Market Analysis

## Market Size

The U.S. residential construction market generates approximately $900 billion in annual activity (Census Bureau, 2023). The custom and semi-custom segment — the addressable slice for this rebuild — represents roughly 20–25% of new single-family starts, or approximately 180,000–220,000 homes per year at current start rates. The design services layer within that segment is not cleanly sized in public data; the most defensible estimate is that design, permitting, and pre-construction coordination represent 8–12% of total project cost, implying a $15–25 billion addressable market for the services layer alone. This is larger than when Atmos launched in 2020, driven by the deepening housing shortage and continued Sun Belt in-migration.

## Competition Map and Gaps

*Drafted* (Donahue's successor, December 2025): The most direct competitor and the clearest proof that the market exists. Drafted is consumer-facing — buyers generate floor plans directly — which means it competes for the same end-user attention Atmos chased. Its weakness is the same one Atmos had: it still depends on consumers converting to construction, which requires financing. No public evidence of a builder-facing revenue model.

*Homebound* (raised $70M, 2022): Vertically integrated construction manager, not a design tool. Operates in California and Texas. Weakness: high fixed costs from employed construction managers; no AI design layer publicly disclosed; geographically concentrated.

*Higharc* (Series B, ~$30M raised as of 2023): Builder-facing platform for production homebuilders, focused on large-volume builders like D.R. Horton. Weakness: explicitly targets enterprise production builders, not the small regional builder (10–50 homes/year) segment. Pricing and integration complexity are prohibitive for smaller operators.

*Archistar / Symbium*: AI-assisted feasibility and zoning tools. Weakness: they solve the regulatory layer only; they do not generate full design packages or connect to builder workflows.

**The gap**: No current competitor serves the small regional builder (10–50 homes/year) with an integrated AI design-to-permit package at a price point accessible to a firm without a dedicated technology budget.

## Defensibility Against Platform Incumbents

Autodesk is the most credible platform threat. Its AEC Collection already includes Revit and FormIt for residential design, and it has the distribution to reach builders. The structural reason Autodesk will not simply add this feature: its product motion is toward enterprise AEC firms and large production builders, not the sub-50-homes-per-year regional contractor who lacks Revit-trained staff. The workflow complexity of Autodesk's tools is itself the moat — a small builder cannot use Revit without hiring someone who can. The rebuild's advantage is radical simplicity for an underserved operator tier. This is a real but not permanent advantage; Autodesk could acquire its way into this segment. Honest assessment: if this rebuild reaches meaningful scale, acquisition by Autodesk, Procore, or BuilderTrend is a more likely outcome than a durable standalone moat.

---

## Recommended MVP

## Core Features

## AI Floor Plan Generator with Builder Constraints Input

A builder inputs lot dimensions, local zoning parameters, target square footage, and style preferences; the system outputs 3–5 buildable floor plan variations with room-level specifications within minutes. This directly replaces the human designer bottleneck Atmos never automated. Unlike Atmos's consumer-facing design tool, this is calibrated to what a builder can actually construct — not what a buyer dreams about — eliminating the 85% design-to-build drop-off that made Atmos's funnel a cost center.

## Automated Zoning and Setback Compliance Check

Each generated plan is run against municipal zoning data (via Symbium or Archistar API integration) to flag violations before the builder presents the design to a buyer. This compresses what previously required a permit expediter or architect's review into an automated pre-screen. The original Atmos required human experts for this step; the rebuild does not.

## Shareable Buyer-Facing Design Package

The builder can generate a branded PDF and 3D walkthrough link to share with prospective buyers — a sales tool, not a consumer product. The buyer never touches the platform directly. This inverts Atmos's model: the builder is the customer, the buyer is the builder's customer. This eliminates the consumer acquisition cost that made Atmos's CAC unsustainable.

## What We Will NOT Build (MVP)

No construction financing coordination. No builder marketplace or matching layer. No project management or post-permit workflow. No consumer-facing interface. These were the operationally heavy layers that made Atmos a staffing agency; they can be added after the design tool has proven unit economics.

## Success Metrics

- 50 paying builder accounts within 6 months of launch
- Average of 3+ design packages generated per builder per month (indicating active use, not shelfware)
- Net Revenue Retention > 100% at 12 months (builders expanding seat count or plan volume)
- Zero human designer hours per completed design package

## Cold-Start Note

This product has no network effects and no local density requirement. A builder in Raleigh generates value from the tool on day one, independent of how many other builders are using it. The cold-start problem does not apply.

---

## Go-to-Market Strategy

## Target Customer Segment

Small regional homebuilders doing 10–50 custom or semi-custom homes per year in Sun Belt metros (Raleigh-Durham, Charlotte, Atlanta, Austin, Tampa). These firms have no dedicated design staff, rely on freelance architects or draftspeople for floor plans, and spend $2,000–$8,000 per plan in external design fees. They are underserved by enterprise tools like Higharc and ignored by consumer platforms like Drafted. Estimated U.S. population of this builder tier: tens of thousands of firms (exact figure not available in public data).

## Primary Distribution Channel

Procore's app marketplace and BuilderTrend's integration ecosystem are the highest-leverage entry points. Both platforms have established trust with the small-to-mid builder segment and active developer partner programs. Secondary channel: direct outreach through National Association of Home Builders (NAHB) chapter events in target metros, where small regional builders concentrate. This is the same builder network Atmos tried to build from scratch; the rebuild accesses it through existing software distribution rather than relationship-by-relationship sales.

## Pricing Strategy

## Differentiation vs. 2026 Competitors

Against Drafted: B2B vs. B2C — the rebuild never depends on a consumer financing a home to generate revenue. Against Higharc: radical simplicity and price accessibility for sub-50-home builders vs. enterprise complexity. Against Archistar/Symbium: full design output, not just feasibility screening. The rebuild's durable differentiation is the combination of AI design generation *and* automated compliance in a single workflow priced for operators who cannot afford enterprise software.
