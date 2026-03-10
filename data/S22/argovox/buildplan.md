# Build Plan: Argovox 2026

## Overview

The single most important change since Argovox's failure is the commoditization of conversational voice infrastructure. In 2022, building a reliable multi-turn voice AI agent required significant proprietary engineering — speech-to-text, natural language understanding, dialogue management, and text-to-speech had to be assembled and tuned by a small team with limited capital. In 2026, platforms like Bland AI, Vapi, and Retell AI offer sub-200ms latency conversational voice APIs at commodity pricing, with pre-built telephony integrations. What consumed the majority of Argovox's engineering capacity is now a vendor call.

Layered on top of that infrastructure, GPT-4o (May 2024) and Claude 3.5 Sonnet (June 2024) can handle genuinely nuanced multi-turn billing conversations — negotiating payment plans, processing hardship exceptions, responding to balance disputes — with reliability that rule-based systems and early LLMs in 2022 could not approach. The core product Argovox was attempting to build is now achievable by a two-person technical team in weeks, not months.

The regulatory environment has also clarified materially. The CFPB's Regulation F (effective November 2021) explicitly permitted text and email debt collection contact, and subsequent FCC TCPA guidance has established clearer safe harbors for AI-initiated calls with proper consent frameworks. The legal ambiguity that made healthcare billing automation risky in 2022 has been substantially reduced.

On the market side, high-deductible health plans have driven patient-pay balances to approximately 30% of hospital revenue (source: Healthcare Financial Management Association, 2024 — specific figure unverified independently). The problem Argovox identified has worsened, not stabilized.

EHR API access has expanded significantly. Athenahealth's open API program, Epic's App Orchard (now with 500+ certified partners), and Kareo's developer platform now allow a voice agent to read patient balances, post payments, and update records programmatically — integration work that required expensive custom development in 2022 is now largely standardized.

Distribution channels unavailable in 2022 now exist: the Epic App Orchard marketplace, Athenahealth's Marketplace with thousands of active practices, and MGMA (Medical Group Management Association) partner networks provide direct access to revenue cycle decision-makers without a cold outbound sales motion.

---

## Why Now?

### Current Market Analysis

The US healthcare revenue cycle management market was valued at approximately $47B in 2022 and is projected to exceed $240B by 2030 (source: research report rebuild signals — original source not independently verified). Even applying significant discount to that projection, the directional growth is unambiguous: rising patient-pay balances, staffing shortages in billing departments, and increasing regulatory complexity are all structural tailwinds.

The competitive landscape in 2026 has consolidated around several distinct tiers, each with identifiable weaknesses:

**Enterprise RCM platforms** — Waystar, R1 RCM, and Experian Health have added AI features to existing platforms but remain oriented toward large hospital systems. Their weakness is implementation timelines measured in quarters and contract minimums that exclude independent practices and mid-size physician groups. They are not competing for the sub-500-physician-group segment.

**Patient financial engagement platforms** — Cedar and Collectly focus primarily on digital (text/email/portal) patient communication and payment facilitation. Cedar raised $200M+ and targets large health systems. Collectly targets smaller practices but is primarily a digital-first platform without sophisticated voice AI. Neither company has a voice agent product with genuine multi-turn negotiation capability as of the research report date.

**Horizontal voice AI platforms** — Bland AI, Vapi, and Retell AI provide infrastructure but no healthcare-specific compliance layer, EHR integrations, or collections workflow logic. They are tools, not products.

**Thoughtful AI** — Competes in RCM automation but focuses on administrative tasks (prior authorization, claims processing) rather than patient-facing collections conversations.

The gap is specific and defensible: no well-capitalized competitor is currently offering a HIPAA-compliant, EHR-integrated, multi-turn voice AI collections agent purpose-built for mid-size physician groups (5–100 providers). Demand signals from adjacent products confirm appetite: Collectly's growth in the SMB practice segment and the rapid adoption of AI scribes (Abridge, Nabla) demonstrate that physician groups are now actively purchasing AI tools and have developed procurement muscle for them.

---

## Recommended MVP

### Core Feature 1: Pre-built multi-turn billing conversation engine

An AI voice agent, built on Vapi or Retell AI infrastructure with GPT-4o as the reasoning layer, that conducts outbound patient billing calls — identifying the patient, explaining the balance, offering payment plan options within provider-defined parameters, and processing payment via Stripe. This directly replicates Argovox's original vision but is now achievable without proprietary voice infrastructure. Unlike Argovox's 2022 build, the conversation quality is grounded in a frontier LLM rather than rule-based dialogue management, enabling genuine handling of patient objections and disputes.

## Core Feature 2: Athenahealth and Kareo native integration

A pre-certified integration with Athenahealth's Marketplace API and Kareo's developer platform that reads patient account balances, posts payment records, and updates account status without manual data entry. This was the integration bottleneck that constrained Argovox's sales motion in 2022. Prioritizing these two platforms targets the mid-size independent practice segment specifically, where Waystar and Cedar are not competing.

## Core Feature 3: HIPAA compliance and TCPA consent management layer

A built-in consent verification step at the start of every call, audit logging of all conversations, BAA-ready vendor agreements with all infrastructure providers, and a configurable opt-out registry. This is not a differentiator — it is table stakes. Building it into the product from day one, rather than retrofitting it, eliminates the legal review delay that slowed Argovox's enterprise sales.

## Core Feature 4: Outcome dashboard with ROI reporting

A simple provider-facing dashboard showing calls attempted, calls completed, payment commitments made, payments collected, and estimated revenue recovered versus a baseline. Framed explicitly as ROI documentation for the CFO or practice administrator who approved the purchase. This addresses the sales education burden by making the value case self-evident at renewal.

**What we will NOT build:** Clinical documentation features, prior authorization automation, inbound patient support, claims processing, or any feature targeting large hospital systems. No custom EHR integrations beyond Athenahealth and Kareo in the first 12 months.

**Success metrics:** 10 paying physician group customers within 6 months of launch; average contract value of $1,500–$3,000/month; patient payment collection rate on AI-handled accounts ≥ 35% (industry benchmark for human agents is approximately 20–30% — specific benchmark source not independently verified); gross revenue retention ≥ 85% at 12 months.

---

## Go-to-Market Strategy

**Target customer segment:** Independent and group physician practices with 5–50 providers, $2M–$20M in annual patient billing, using Athenahealth or Kareo as their practice management system, with a dedicated billing coordinator or small billing team. This segment is large enough to generate meaningful revenue, small enough to have 30–60 day sales cycles rather than 6–12 month enterprise procurement processes, and is currently underserved by both Cedar (too large) and horizontal voice AI tools (no healthcare compliance).

**Primary distribution channel:** Athenahealth Marketplace and Kareo's partner directory, supplemented by direct outreach to MGMA regional chapter members. Marketplace listings provide inbound discovery from practices already searching for billing automation tools. MGMA chapter sponsorships and webinars provide credibility with the practice administrator persona who controls purchasing decisions in this segment. This is a distribution channel that did not exist for Argovox in 2022.

**Secondary channel:** Partnerships with healthcare-focused accounting firms and billing service organizations (BSOs) that serve independent practices. BSOs have existing trust relationships with the target customer and a financial incentive to offer AI augmentation to their client base.

**Pricing strategy:** $1,500/month base platform fee covering up to 500 outbound calls, plus $2.50 per call above that threshold. No percentage-of-collections pricing — this model creates revenue unpredictability and requires auditing patient payment data at a level of integration complexity that slows sales. Flat SaaS pricing with usage overage is easier to approve at the practice administrator level without CFO sign-off. At $1,500/month, payback is demonstrable within the first month of collections activity for any practice with >$50K in outstanding patient balances.

**Differentiation vs. 2026 competitors:** Against Cedar and Collectly — voice capability with genuine multi-turn negotiation, not just text/portal nudges. Against horizontal voice AI platforms — pre-built HIPAA compliance, EHR integrations, and collections-specific conversation logic that a practice can deploy without an internal technical team. Against Waystar and R1 RCM — implementation in days, not quarters, with no enterprise contract minimums. The rebuild's core advantage over the original Argovox is that the technical risk has been eliminated: the product can be demonstrated live in a sales call, which Argovox likely could not do reliably in 2022.
