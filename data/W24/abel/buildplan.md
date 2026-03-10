# Build Plan: Abel 2026

## Overview

Abel 2026 is a specialized extraction engine for plaintiff-side mass tort litigation—not a general eDiscovery platform. The target is boutique firms (10–75 attorneys) drowning in medical records, depositions, and regulatory documents across hundreds of cases. The insight: law firms now have AI procurement budgets and trust frameworks that didn't exist in 2024. Relativity and legacy platforms still treat documents as searchable objects, not structured data. Abel extracts entities, timelines, and causal relationships automatically—turning chaos into a queryable case map.

The go-to-market is vertical and distribution-first. Launch via Clio's App Marketplace (one-click integration into the practice management tool these firms already use daily), then land through referrals from mass tort defense counsel who see the advantage and recommend it to opposing counsel. Price as a per-case subscription, not per-seat, so adoption scales with case volume. Win by being the only tool that makes a 500-document medical record set instantly navigable—and by being boring enough (SOC 2, private processing, no data sharing) that risk-averse partners sign the contract.34:T7b6,

## Why Now?

## Current Market Analysis

The global eDiscovery market has grown from approximately $14.5B in 2023 to an estimated $17–18B in 2026 (exact 2026 figure not confirmed in available sources), on a trajectory toward $28B+ by 2028 per the research report. The broader legal AI market has expanded dramatically: Harvey's fundraising trajectory, EvenUp's growth in personal injury AI, and the Thomson Reuters–Casetext integration all confirm that law firms are allocating real budget to AI document tools.

## Competition map and gaps:

- **Relativity** dominates enterprise eDiscovery but remains a search-and-retrieval platform. Its AI features (RelativityOne AI) are bolt-ons to a legacy architecture; structured relationship mapping across entities is not a core capability. Weakness: expensive, slow to deploy, built for IT-managed environments.
- **Everlaw** is the strongest cloud-native challenger, with genuine AI summarization features added in 2024–2025. Weakness: still primarily a litigation support tool; entity extraction pipelines are not user-configurable by practice area.
- **Harvey** has raised $100M+ and targets large BigLaw firms with broad legal AI capabilities. Weakness: priced and positioned for Am Law 100 firms; minimal workflow depth for mass tort or insurance defense document review specifically.
- **Casetext (Thomson Reuters)** excels at legal research augmentation. Weakness: document review and entity extraction are secondary to its research core; limited customization for case-specific entity schemas.

**The gap:** No current competitor offers configurable, practice-area-specific entity extraction pipelines with relationship mapping, priced and packaged for mid-market litigation boutiques (50–200 attorney firms). Harvey serves BigLaw; Logikcull serves small firms needing simplicity. The mid-market litigation specialist is underserved.

**Demand signal:** EvenUp's reported $50M+ ARR in AI-generated demand letters for personal injury firms confirms that plaintiff-side litigation practices will pay for AI document intelligence when it maps directly to billable output.

---

## Recommended MVP

## Core Features:

## Mass Tort Entity Extraction Pipeline

Ingests PDFs, emails, and medical records common to mass tort cases and extracts a pre-configured entity schema: plaintiffs, defendants, exposure events, medical diagnoses, damages, and key dates. This matters because mass tort litigation involves thousands of near-identical documents with high-value pattern recognition across claimants — exactly the depth-vs.-breadth problem Abel identified. Unlike Abel's fully custom pipelines, this ships with a pre-built schema that works out of the box, reducing onboarding time from weeks to hours.

## Relationship-Aware Chronology Builder

Automatically generates a structured timeline linking extracted entities — connecting a plaintiff to their exposure events, medical records, and damages documentation — exportable as a Word or PDF chronology ready for deposition prep. This directly addresses the "weeks to months" synthesis work Garry Tan described at Abel's launch. The original Abel product produced relationship maps; this version produces a specific, attorney-ready deliverable that maps to a billable work product.

## SOC 2–Compliant Private Processing

All document processing runs within a customer-dedicated AWS environment with no cross-client data sharing, with SOC 2 Type II certification obtained via Vanta before the first sales conversation. This is the compliance infrastructure Abel almost certainly lacked. It converts the privacy objection from a deal-stopper into a checkbox.

## Clio Integration for Case Import

One-click document import from Clio Manage, the dominant practice management platform for mid-market firms, via Clio's App Marketplace. This eliminates the manual upload friction of Abel's onboarding and provides a distribution channel to 150,000+ firms.

**What we will NOT build:** M&A due diligence features, insurance claims workflows, custom pipeline builders for non-litigation use cases, or a general-purpose legal research assistant. No horizontal expansion until mass tort is dominant.

**Success metrics:** 10 paying law firms within 6 months of launch; $15K average annual contract value; 80%+ document processing accuracy on plaintiff medical record extraction validated by attorney review; SOC 2 Type II certification before first enterprise sales call.

---

## Go-to-Market Strategy

**Target customer:** Plaintiff-side mass tort litigation boutiques with 10–75 attorneys, handling pharmaceutical, medical device, or environmental tort cases. These firms process thousands of near-identical plaintiff documents per case, have acute associate-hour cost pressure, and make software decisions at the partner level without multi-year IT procurement cycles. They are large enough to pay meaningful SaaS fees but small enough to move in weeks, not months.

**Primary distribution channel:** Clio App Marketplace, supplemented by direct presence at the Mass Torts Made Perfect conference (the dominant gathering for plaintiff mass tort attorneys, held twice annually) and targeted outreach through the American Association for Justice (AAJ) member network. These are the channels Abel never used. Legal conference presence builds the domain credibility that cold outreach cannot.

**Pricing:** $2,500/month per matter (active case), with a $500/month platform fee covering up to 3 concurrent matters. This maps to eDiscovery pricing conventions attorneys already understand (per-matter billing), avoids per-seat friction in firms with variable staffing, and targets $15K–$30K ACV per firm. At 10 customers, this generates $150K–$300K ARR — sufficient to demonstrate traction for a seed raise. Pricing is justified by the associate hours displaced: a single mass tort chronology that takes a junior associate 20 hours at $200/hour costs $4,000 in labor; Abel's rebuild delivers it in minutes.

**Differentiation vs. 2026 competitors:** Harvey is priced for Am Law 100 and does not offer mass tort–specific entity schemas. Everlaw requires IT-managed deployment. The rebuild wins on three axes: practice-area depth (pre-built mass tort schema vs. generic AI), compliance-first architecture (SOC 2 before sales, not after), and mid-market pricing that BigLaw-focused competitors structurally cannot match.
