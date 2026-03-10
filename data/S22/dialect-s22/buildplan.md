# Build Plan: Dialect 2026

## Overview

## Why Now?

## Current Market Analysis

**Market Size:** The RFP and proposal automation software market was valued at approximately $1.5B in 2022 (source: Grand View Research; exact 2026 figure not available in research materials). The adjacent compliance automation market—where Vanta, Drata, and Secureframe compete—has attracted $500M+ in venture funding alone, suggesting the combined security questionnaire and RFP workflow market is meaningfully larger than the standalone RFP category implies.

## Incumbents and Their Specific Weaknesses:

- **Responsive (formerly RFPIO):** Raised $100M+; deep enterprise integrations and large content library features. Weakness: legacy UX built around content library search rather than generative drafting; AI features bolted onto a pre-LLM architecture; expensive ($30K–$100K+ ACV), locking out mid-market buyers.
- **Loopio:** Similar profile to Responsive; strong in mid-market but AI response quality is reported by users (per G2 reviews, publicly available) as inconsistent; no native compliance platform integration.
- **Vanta/Drata/Secureframe questionnaire modules:** Questionnaire automation is a secondary feature, not a core product. Answer quality is limited by shallow knowledge base ingestion; no support for RFP or DDQ formats outside security questionnaires.
- **Microsoft Copilot / Salesforce Einstein:** Broad enterprise AI assistants with no questionnaire-specific workflow, citation grounding, or compliance content awareness.

**Competitive Gap:** No current competitor combines (a) best-of-breed generative response quality with (b) native integration into compliance platforms where the source-of-truth security content already lives, at (c) mid-market pricing accessible without an enterprise sales cycle.

**Demand Signals:** Guru, Glean, and Notion AI have each reported strong adoption for internal knowledge retrieval use cases, confirming enterprise appetite for AI-grounded Q&A. The security questionnaire workflow is the highest-stakes, most time-sensitive instance of exactly this use case.

---

## Recommended MVP

## Core Features:

**1. Compliance Platform Knowledge Sync:** Integrates directly with Vanta, Drata, and Secureframe via their published APIs to pull structured security controls, evidence documents, and prior questionnaire responses into a continuously updated knowledge base. This matters because it eliminates the manual content ingestion step that was a key time-to-value barrier for Dialect—customers already have their security content organized inside these platforms. Unlike Dialect's original browser extension, which required users to manually connect help center articles and documents, this integration makes the knowledge base self-maintaining.

**2. Generative Draft Engine with Inline Citations:** Uses Claude 3.5 or GPT-4o (both available as of mid-2024) with full-document context to draft responses to entire questionnaires in batch, not question-by-question. Every answer includes a citation linking to the specific control or document it drew from. This directly addresses the hallucination risk that was Dialect's original citation feature—but now operates at 10x the scale and quality enabled by 200K+ token context windows unavailable in 2022.

**3. Native Web Application with SOC 2 Type II Certification:** A standalone web app—not a browser extension—that passes enterprise security review. Dialect's browser extension model was structurally incompatible with enterprise IT policies. SOC 2 Type II certification, pursued in the first six months, is the minimum requirement to be approved by the same security teams that are the product's primary users.

**What We Will NOT Build:** A content library or knowledge management system (Guru and Glean do this better); a compliance monitoring or evidence collection platform (Vanta/Drata own this); a proposal generation tool for non-security RFPs in the first 12 months; a browser extension of any kind.

**Success Metrics:** 50 paying customers within 6 months of launch; average questionnaire completion time reduced by ≥70% (verified via in-product telemetry); net revenue retention ≥110% at month 12; SOC 2 Type II report issued within 6 months.

---

## Go-to-Market Strategy

**Target Customer Segment:** Series B–D B2B SaaS companies (50–500 employees) that are already Vanta or Drata customers and have a dedicated security or compliance function. This segment is narrow and specific: they receive enough security questionnaires to feel the pain acutely (typically 20–100 per year at this scale), they already have structured security content inside a compliance platform, and they have demonstrated willingness to pay for compliance tooling. They are large enough to have a security budget but small enough to adopt software without a 6-month procurement cycle.

**Primary Distribution Channel:** The Vanta Integration Marketplace and Drata Partner Ecosystem. Both platforms have published partner programs and app marketplaces with thousands of installed customers. A listing in Vanta's marketplace places the product in front of the exact ICP at the moment of highest intent—when a Vanta customer receives a new security questionnaire and opens their compliance platform to find the answers. This is a distribution channel that did not exist when Dialect operated.

**Tactics:** (1) Launch as a Vanta-certified integration on day one; (2) offer a free tier covering 3 questionnaires per month to drive PLG adoption within Vanta's customer base; (3) target Vanta customer Slack communities and LinkedIn groups where security engineers discuss questionnaire pain.

**Pricing:** $299/month for up to 20 questionnaires; $799/month unlimited, with annual prepay discount of 20%. Justified by the ROI math: a single security questionnaire requiring 8 hours of a $150K/year security engineer's time costs the company approximately $600 in labor. The product pays for itself in one questionnaire per month.

**Differentiation vs. 2026 Competitors:** Responsive and Loopio compete on breadth of integrations and enterprise features at $30K+ ACV. This rebuild competes on depth of compliance platform integration, response quality grounded in live security controls, and mid-market pricing accessible without a sales call—a segment the incumbents have structurally abandoned.
