# Build Plan: SimpleCitizen 2026

## Overview

By 2026, SimpleCitizen is an AI-powered case management API for immigration law firms—not a consumer product. The target is small and mid-sized firms (5–50 attorneys) drowning in document intake and manual form-filling. The insight: immigration lawyers will never be replaced by software, but they will pay for software that makes them 40% faster. The market has matured enough that LLM document extraction and direct USCIS e-filing integration are now table stakes, not moonshots.

The go-to-market is embedded: native integrations with Rippling and Greenhouse put visa sponsorship workflows directly inside the HR tools where hiring decisions happen. Cases route to the law firm's SimpleCitizen portal automatically. Firms see immediate ROI through attorney time savings and higher throughput per headcount. Distribution is direct sales to firms already using legacy case management (Tracker Corp, INSZoom, spreadsheets) who are desperate for a modern alternative.

This is the B2B version of the original insight—the paperwork is solvable—aimed at the customer who actually has budget and decision-making power.

## Why Now?

The single most important change since SimpleCitizen's failure is this: **the correct B2B customer has been publicly identified, and they have already proven they will pay.** Fragomen's 2020 acquisition of SimpleCitizen was not a distressed exit — it was a strategic purchase by the world's largest immigration law firm to compete against Big 4 accounting firms encroaching on immigration services. That acquisition is a public proof-of-concept that immigration workflow technology has a willing, paying buyer in law firms themselves. A rebuilt SimpleCitizen can skip the five-year detour of trying to displace attorneys and go directly to selling to them.

The second structural unlock is LLM-based document understanding. GPT-4 (March 2023) and Claude 3 Opus (March 2024) can now parse unstructured immigration documents — foreign-language birth certificates, passports, employment records — with high accuracy. SimpleCitizen's original workflow required routing every application through a single attorney partnership (Jacob Sapochnick's firm) for document review, which constrained throughput and compressed margins. That bottleneck is now automatable, enabling a rebuilt product to process dramatically more cases per attorney hour.

The market context has also shifted materially. The H-1B visa denial rate rose from 6% in FY2015 to 24% in FY2018 (USCIS data), creating sustained employer demand for error-reduction tools that did not exist at SimpleCitizen's B2B launch in 2017. Remote work normalization post-2020 has expanded the pool of US companies hiring internationally — Deel, Remote.com, and Rippling have collectively raised over $1.5B validating that employers will pay for global employment infrastructure at scale (exact current market size for immigration legal tech in 2026 is not available in the research report; independent verification recommended).

USCIS's expanded e-filing via myUSCIS, now covering more form types than during SimpleCitizen's operating years, creates a direct API integration opportunity that did not exist in 2015–2020. A rebuilt product can submit applications programmatically rather than generating paper packets for attorney review — eliminating the single most time-consuming step in the original workflow.

Distribution channels unavailable to the original SimpleCitizen now include: Rippling's App Shop (HR/payroll platform with built-in immigration module demand), Greenhouse's integration marketplace (ATS used by 7,500+ companies), and Workday's partner ecosystem — all of which sit directly inside the HR workflows where visa sponsorship decisions are made.

---

## Current Market Analysis

**Market size:** The US immigration legal services market was estimated at approximately $8.5B in 2020 (IBISWorld, cited in adjacent research — exact 2026 figure not available in the research report). The employer-sponsored segment, where SimpleCitizen was pivoting at acquisition, has grown structurally since 2020 due to remote hiring normalization. Deel alone reported $500M+ ARR in 2023 serving global employment, validating the employer willingness-to-pay thesis at scale.

## Competition map and gaps:

- **Boundless Immigration** (consumer-focused, ~$995–$1,495 per application): Closest spiritual successor to SimpleCitizen's consumer product. Weakness: still consumer-only, no law firm infrastructure play, no API layer.
- **Envoy Global**: Enterprise immigration management platform targeting HR teams directly. Weakness: positions as attorney replacement (the same objection that killed SimpleCitizen's B2B product), not as law firm infrastructure. Pricing is opaque and enterprise-sales-heavy.
- **Tracker Corp / INSZoom**: Legacy case management software used by immigration law firms. Weakness: built pre-LLM, no AI document parsing, clunky UX described by users as "built in 2005." No modern API layer for HR platform integrations.
- **Deel / Rippling immigration modules**: Embedded in broader global employment platforms. Weakness: immigration is a secondary feature, not a core competency; both rely on third-party attorney networks with no proprietary workflow automation.
- **Fragomen Technologies** (the acquirer of SimpleCitizen): Internal tool, not sold externally. Weakness: not available to competing law firms — creating an explicit gap in the market for a neutral infrastructure vendor.

**The gap:** No current competitor offers an LLM-powered, API-first immigration workflow layer designed explicitly for immigration law firms as the primary customer, with HR platform integrations as the distribution channel. Tracker Corp and INSZoom own the law firm software market but are technically stagnant. That is the opening.

**Demand signals:** Rippling's immigration module, Greenhouse's partnership with Envoy Global, and Deel's attorney network all confirm that HR platforms are actively seeking immigration infrastructure — and currently stitching together inadequate solutions.

---

## Recommended MVP

**Core positioning:** An AI-powered immigration case management API for small and mid-sized immigration law firms (5–50 attorneys), with native integrations into Rippling and Greenhouse as the primary distribution wedge.

## Feature 1: LLM Document Extraction and Form Pre-Population

The system ingests uploaded documents — passports, birth certificates, I-94 records, foreign-language employment letters — and uses GPT-4o (May 2024) to extract structured data, flag inconsistencies, and pre-populate USCIS form fields. This directly replaces the manual document review step that constrained SimpleCitizen's throughput and required a single attorney partnership to function. Unlike SimpleCitizen's original workflow, the attorney reviews exceptions flagged by the AI rather than every document from scratch — reducing attorney time per case by an estimated 60–70% (exact figure requires validation with pilot law firm customers).

## Feature 2: USCIS e-Filing Integration

The platform connects directly to myUSCIS's expanded e-filing system to submit completed applications programmatically, replacing SimpleCitizen's original paper-packet generation workflow. This eliminates the physical submission step entirely for supported form types and creates a real-time status tracking layer that law firms can expose to their corporate clients. The original SimpleCitizen had no such integration because USCIS e-filing was not available at scale during its operating years.

## Feature 3: Law Firm White-Label Client Portal

Immigration law firms get a branded client-facing portal where corporate HR contacts upload documents, answer intake questions, and track case status — without the law firm building or maintaining the technology. This directly addresses the "we're not firing the lawyers" objection by making the law firm the product's face, not a competitor to it. SimpleCitizen never built this layer; it always presented itself as the consumer-facing brand.

## Feature 4: Rippling and Greenhouse Integration

Native integrations that surface visa sponsorship workflows inside the HR tools where hiring decisions are made, routing cases to the law firm's SimpleCitizen-powered portal automatically. This is the distribution mechanism, not just a feature.

## What we will NOT build:

- A direct-to-consumer product (the $249 green card application). The consumer market is real but not venture-scale at that price point, and it creates channel conflict with law firm customers.
- A full legal practice management suite (billing, calendaring, trust accounting). That is Clio's market. Stay focused on immigration workflow.
- Proprietary attorney network. Partner with existing firms; do not compete with them.

## Success metrics:

- 10 paying immigration law firms within 6 months of launch (at minimum $500/month each)
- Average attorney time per H-1B case reduced by ≥40% (measured via pilot firm time-tracking)
- USCIS application approval rate ≥95% across processed cases (matching SimpleCitizen's "near-perfect" benchmark)
- At least 1 signed integration partnership with Rippling or Greenhouse within 12 months

---

## Go-to-Market Strategy

**Target customer segment:** Small and mid-sized US immigration law firms with 5–50 attorneys that currently use Tracker Corp, INSZoom, or spreadsheets for case management, process at least 100 employer-sponsored visa cases per year (H-1B, L-1, O-1), and have at least one corporate client relationship. This segment is large enough to generate meaningful revenue, underserved by legacy software vendors, and does not have the internal engineering resources to build LLM tooling themselves. Fragomen is explicitly excluded — they have their own technology. The Big 4 immigration practices are also excluded as initial targets (too complex a sales cycle).

**Primary distribution channel:** Direct outreach to immigration attorneys through the American Immigration Lawyers Association (AILA), which has 15,000+ members and hosts an annual conference where legal tech vendors have established presence. Secondary channel: inbound via Rippling App Shop and Greenhouse integration marketplace, where HR teams searching for immigration solutions will encounter the product and route their law firm to it. This inverts SimpleCitizen's failed enterprise sales motion — instead of selling to HR teams and asking them to fire their lawyers, the HR platform integration generates warm inbound leads for law firms already using the product.

**Pricing strategy:** $800–$1,500/month per law firm (5–15 attorney seats), plus $15–$25 per case processed above a monthly volume threshold. This is SaaS-plus-usage pricing, justified by the recurring nature of law firm case volume and the clear ROI: if the platform saves 3 attorney hours per H-1B case at a $300/hour billing rate, a firm processing 20 cases/month captures $18,000/month in recovered capacity against a $1,500 software cost. Specific pricing should be validated with pilot customers before public launch.

## Differentiation vs. 2026 competitors:

- vs. Tracker Corp / INSZoom: Modern LLM document parsing and USCIS e-filing integration they do not have
- vs. Envoy Global: Sells *to* law firms rather than *around* them — no channel conflict
- vs. Deel/Rippling immigration modules: Purpose-built for immigration attorneys, not a secondary feature of a payroll platform
- vs. Boundless: Entirely different customer (B2B law firm infrastructure vs. B2C consumer)

The core differentiation is structural, not feature-based: this product treats immigration attorneys as the customer and corporate HR as the distribution channel — the exact inverse of every mistake SimpleCitizen made in its enterprise pivot.
