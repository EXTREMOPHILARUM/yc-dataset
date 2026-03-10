# Build Plan: Jasmine Energy 2026

## Overview

Jasmine Energy was a Washington, DC-based climate tech startup (YC S22) that attempted to modernize the Renewable Energy Certificate market — first through a blockchain/DeFi trading marketplace, then through an AI-powered compliance automation platform — before quietly winding down by mid-2025 after exhausting its $2.5–3M seed round without achieving meaningful commercial traction or raising follow-on capital.

The rebuild thesis is not to retry the consumer play that killed Jasmine, but to go B2B from day one: the same AI document-extraction and form-filling capability that Jasmine built for homeowners is far more valuable — and far more monetizable — when sold as an embedded API layer to the solar installer and developer software platforms that already own the customer relationship. The new Jasmine is a compliance infrastructure company that solar software vendors plug in, not a consumer brand that has to explain what a REC is.

---

## Why Now?

The single most important change since Jasmine's failure is the maturation of multimodal large language models capable of reliably extracting structured data from unstructured documents and completing regulatory webforms at near-zero marginal cost. GPT-4o (May 2024) and Claude 3.5 Sonnet (June 2024) can read scanned PDFs, utility interconnection agreements, and CRM notes with accuracy sufficient for production compliance workflows — without requiring a custom OCR pipeline or a team of compliance specialists. In 2022, building this capability required significant engineering investment; in 2026, it is an API call. This directly enables the core technical product Jasmine was attempting to build, at a fraction of the original cost.

The second critical change is distribution. Aurora Solar, the dominant solar design and sales platform, serves over 10,000 installation companies and has processed proposals for more than 10 million homes (Aurora Solar, 2024 — exact current figures not independently verified by this report). Scanifly, OpenSolar, and similar platforms collectively reach thousands more installers. None of these platforms have natively integrated REC registration and compliance workflows as of 2024, per the rebuild signals identified in the research. This is a genuine integration gap, not a speculative one.

The third change is demand-side urgency. The Inflation Reduction Act (2022) and subsequent Treasury guidance have materially increased corporate procurement of clean energy certificates. While specific IRA-driven REC demand figures are not available in this report, the directional signal is clear: large corporations now face more rigorous documentation requirements for clean energy claims, creating institutional buyers who need verified, registered RECs — and who will pay a premium for them. This increases the per-REC value available to generators and improves the unit economics that made Jasmine's residential commission model structurally insufficient.

The U.S. residential solar installed base has grown from approximately 1.7 million homes (Jasmine's 2022 figure) to over 4 million homes (SEIA, 2024), expanding the addressable pool without requiring the rebuild to solve the consumer acquisition problem directly.

---

## Current Market Analysis

**Market size:** The voluntary and compliance REC market was estimated at $5–10 billion annually when Jasmine operated; current market size figures broken down by segment are not available in this report. The IRA-driven increase in corporate clean energy procurement has likely expanded the institutional REC buyer base, but specific 2025–2026 market size data should be independently verified before fundraising.

## Competition map:

- **3Degrees and RECs International** are the incumbent REC brokers with established utility and corporate relationships. Their weakness is that they are labor-intensive, focused on utility-scale and large commercial accounts, and have no automation layer for small commercial or residential generators. They are not building software products.
- **Renewable Choice Energy (acquired by Schneider Electric)** operates at the enterprise sustainability consulting layer — relevant to corporate buyers, not generator-side automation.
- **Arcadia** aggregates utility data and offers some REC-adjacent services for residential customers, but its core product is utility bill data access, not end-to-end REC lifecycle management. It does not offer installer-embedded compliance workflows.
- **Evident (formerly RECx)** focuses on REC tracking and retirement for corporate buyers, not generator-side registration automation. No evidence of installer platform integrations found.
- **General-purpose AI workflow tools** (Zapier AI, Make, Microsoft Copilot Studio) could theoretically automate REC registration webforms, but they lack the domain-specific compliance logic, regional tracking system knowledge (WREGIS, PJM-GATS, M-RETS, NEPOOL-GIS), and pre-built integrations that a purpose-built tool would offer.

**Demand signals from adjacent products:** Aurora Solar's expansion into financing and incentive management signals that installer platforms are actively looking to add post-installation value services. The existence of dedicated solar permitting automation companies (e.g., SolarApp+, a DOE-backed initiative) confirms that the installer workflow automation category is real and growing.

**Defensibility analysis:** The honest answer is that this rebuild faces genuine platform risk. Aurora Solar or Enphase could build REC registration as a native feature. The structural defense is that REC compliance spans 8+ regional tracking systems with different APIs, data formats, and regulatory requirements — a fragmented integration surface that is unattractive for a platform company to maintain as a core feature but is exactly the kind of specialized infrastructure a focused vendor can own. The moat is built through proprietary integration depth and a growing corpus of registration histories across thousands of systems — data that improves compliance accuracy over time and is difficult for a late-entering platform to replicate quickly. This is a real but not impenetrable moat; the rebuild must move fast to establish integration partnerships before installer platforms decide to build natively.

---

## Recommended MVP

### Feature 1: Installer-Embedded REC Registration API

A single API endpoint that installer platforms (Aurora Solar, Scanifly, OpenSolar) can call at project completion to automatically initiate REC generator registration across the relevant regional tracking system (WREGIS, PJM-GATS, M-RETS, or NEPOOL-GIS based on project location). The API accepts structured project data already present in the installer's system — system size, location, interconnection date, owner information — and handles the tracking system submission without human intervention. This differs from Jasmine's original approach by targeting the installer's existing workflow rather than requiring homeowners to discover and onboard to a separate platform. The cold-start problem is solved structurally: value is delivered on the first registration, with no network density required.

## Feature 2: AI Document Extraction for Unstructured Compliance Inputs

Using GPT-4o or Claude 3.5 Sonnet (both available as of mid-2024), the platform reads unstructured inputs — scanned interconnection agreements, utility approval letters, PDF system specs — and extracts the structured fields required for tracking system registration. This directly addresses the workflow pain point Jasmine identified: compliance filings fail because required data is buried in documents that vary by utility and state. The difference from Jasmine's implementation is that this capability is now available at API cost rather than requiring a custom-built pipeline, dramatically reducing the engineering investment required.

## Feature 3: REC Lifecycle Dashboard for Installer Partners

A white-labeled dashboard that installer platforms can surface to their customers showing registration status, REC generation, and payout history. This is a retention and upsell surface for the installer platform, not a standalone consumer product. It explicitly does not require the rebuild to acquire homeowners directly.

**What we will NOT build:** A consumer-facing mobile app, a blockchain trading layer, a speculative REC marketplace, or a direct-to-homeowner marketing funnel. These were Jasmine's failure modes.

## Success metrics:

- 3 signed installer platform integration agreements within 6 months of launch
- 500 REC registrations processed through the API within 12 months
- API error/rejection rate below 5% across all supported tracking systems
- At least 1 TPO or commercial portfolio account (100+ systems) live within 12 months

**Cold-start:** Not applicable in the traditional sense — the B2B API model delivers value on the first transaction. The threshold for proving the product works is a single installer partner processing their first 10–20 registrations successfully.

---

## Go-to-Market Strategy

**Target customer segment:** Solar installation companies with 200–2,000 installations per year that use Aurora Solar, Scanifly, or OpenSolar as their primary project management platform, operating in states with active REC markets (Pennsylvania, New Jersey, Massachusetts, Illinois, and WREGIS-covered western states). This is narrow enough to execute with a small team and large enough to generate meaningful registration volume.

**Primary distribution channel:** Direct integration partnerships with 2–3 installer software platforms, pursued through their developer/partner programs. Aurora Solar's partner ecosystem and OpenSolar's open API architecture are the most accessible entry points based on publicly available documentation. The pitch to these platforms is straightforward: adding REC registration as a native workflow feature increases their product stickiness and creates a new revenue-sharing opportunity without requiring them to build compliance infrastructure.

**Pricing strategy:** Charge installer platforms a per-registration fee of $15–$25 per system registered, with volume discounts for platforms processing 1,000+ registrations per year. This is a B2B infrastructure price, not a consumer subscription. The stress-test against free alternatives: a solar installer can register systems manually with WREGIS or PJM-GATS for free, but the process takes 2–4 hours per system and requires compliance knowledge most installers lack. At $15–$25 per registration, the rebuild is pricing below the labor cost of manual registration (at any reasonable hourly rate) while delivering faster, more accurate results. There is no free automated alternative that handles multi-registry compliance with AI document extraction. The commission model that capped Jasmine's residential revenue is explicitly abandoned here — a flat per-registration fee scales with installer volume rather than with low REC spot prices.

**Differentiation vs. 2026 competitors:** The rebuild's advantage over general-purpose AI workflow tools is pre-built tracking system integrations and domain-specific compliance logic. The advantage over incumbent REC brokers is automation speed and the ability to serve small commercial and residential systems economically. The advantage over installer platforms building natively is specialization: maintaining 8+ regional tracking system integrations is a distraction for a design software company and a core competency for a compliance infrastructure company.
