# Build Plan: Struct 2026

## Overview

Struct was a Y Combinator-backed (W23) startup that built a multilingual, real-time AI voice agent platform for phone-based business automation across fintech, legaltech, SaaS, and CRM — it raised $500K, claimed tens of thousands of daily calls, and quietly shut down in 2024 after failing to raise a follow-on round in one of the most crowded AI sub-categories of the 2023 boom.

The rebuild thesis is not to retry the horizontal platform play that killed the original — it is to take Struct's only genuine differentiator, multilingual voice, and drive it into a single underserved vertical where incumbents are weakest and switching costs are highest: AI-powered outbound and inbound call automation for Latin American fintech companies serving Spanish- and Portuguese-speaking customers. The new Struct is a vertical SaaS product, not infrastructure; it ships with compliance posture, pre-built call flows, and CRM integrations baked in from day one. In one line: **Struct 2.0 is the AI voice agent platform built specifically for LATAM fintech — the only one that speaks the language, knows the regulation, and closes the loop on collections, onboarding, and support without a human on the line.**

---33:Ta26,

## Why Now?

The single most important change since Struct's failure is the collapse of the infrastructure burden that consumed its runway. In 2023, a three-person team building a real-time multilingual voice platform had to independently integrate and maintain ASR (speech recognition), TTS (text-to-speech), LLM inference, and telephony stacks — each a full engineering problem in its own right. In 2026, that entire stack is commodity infrastructure available via API. Vapi, Retell AI, and LiveKit provide programmable voice orchestration. Cartesia's Sonic model achieves sub-300ms end-to-end latency. ElevenLabs Turbo v2.5 supports 30+ languages with production-grade voice quality. OpenAI's Realtime API (launched October 2024) handles multilingual conversation natively. A three-person team in 2026 can build what Struct attempted in 2023 in weeks, not months — and spend the remaining runway on vertical depth and GTM rather than infrastructure R&D.

The market Struct was targeting has since been validated by well-funded survivors. Bland AI has raised $22M; Retell AI raised $4.5M; Vapi has established a paying developer community. These companies proved that B2B buyers will pay for programmable voice infrastructure — a fact that was genuinely unproven in early 2023 when Struct was selling. The question is no longer "will enterprises buy AI voice?" but "which vertical-specific player will own each segment?"

The LATAM fintech vertical specifically has reached an inflection point. The region's digital lending and neobank sector grew at a compound rate exceeding 25% annually between 2021 and 2024 (source: Finnovista Fintech Radar, 2024 — specific 2026 figures unavailable at time of writing). Companies like Nubank, Konfio, Kueski, and hundreds of smaller lenders are processing millions of customer interactions monthly in Spanish and Portuguese — languages where Bland AI, Retell, and Vapi have minimal vertical depth and no compliance-specific tooling. The FTC's 2024 guidance on AI in debt collection and Brazil's BACEN regulatory framework for AI-assisted financial communications have both clarified the compliance landscape, reducing the enterprise sales friction that would have paralyzed Struct's fintech vertical in 2023.

Distribution channels unavailable to Struct in 2023 now exist: the Salesforce AppExchange (150,000+ business customers), HubSpot's App Marketplace, and direct partnerships with LATAM-focused CRM providers like Zoho (which has significant LATAM penetration) provide warm inbound channels that a horizontal platform could never access efficiently.

---

## Current Market Analysis

## Market Size

The global AI voice agent market is estimated at approximately $3.4 billion in 2024, projected to reach $11.2 billion by 2028 (MarketsandMarkets, 2024 — 2026-specific figures unavailable). The LATAM call center and collections automation sub-segment is not independently sized in available public research; this is a data gap the rebuild team should validate through primary customer interviews before committing capital. What is documented: LATAM fintech companies collectively process hundreds of millions of customer calls annually, and collections call automation alone — a single use case — represents a multi-hundred-million-dollar addressable market in the region. The broader global call center market exceeds $300 billion annually, and LATAM represents an estimated 8–10% of that figure (source: Grand View Research, 2023).

## Competition Map and Gaps

The current competitive landscape has three tiers:

*Horizontal voice AI platforms (Bland AI, Retell AI, Vapi):* All three are English-first in their go-to-market, developer documentation, and support infrastructure. None has documented LATAM-specific compliance tooling, Spanish/Portuguese call flow templates, or partnerships with LATAM CRM or collections software providers. Their weakness is precisely the vertical depth and language specificity that Struct 2.0 would lead with.

*Contact center incumbents (Twilio, Genesys, Five9, NICE):* These platforms have LATAM enterprise relationships but are slow to ship AI-native features and price at enterprise tiers that exclude the mid-market LATAM fintech companies (50–500 employees) that represent the highest-growth segment. Twilio's AI layer (launched 2024) is English-dominant and requires significant custom development to localize.

*LATAM-specific BPO operators:* Companies like Atento and Teleperformance operate large Spanish/Portuguese call center operations in the region but are human-labor businesses with structural cost disadvantages versus AI automation. They are potential partners or acquirers, not direct competitors.35:T4f9,Usage-based pricing anchored to call volume: $0.08–$0.12 per minute of AI-handled call, with a platform fee of $500–$1,000/month for compliance features, CRM integrations, and support. A company running 10,000 collections calls/month at an average of 3 minutes per call generates $2,400–$3,600/month in usage revenue plus the platform fee — a $3,000–$4,600/month contract. This competes directly against a human collections agent at LATAM BPO rates ($8–12/hour fully loaded), where 10,000 calls at 3 minutes each requires approximately 500 agent-hours, costing $4,000–$6,000/month. The AI solution is cheaper, faster, and available 24/7.

The stress test against free alternatives: WhatsApp Business API (Meta) handles text-based collections outreach for near-zero marginal cost and has dominant penetration in LATAM. The rebuild must be honest that WhatsApp is a real competitive pressure for low-complexity collections nudges. The defensible position is that voice outperforms text for high-stakes collections conversations — payment arrangements, dispute resolution, and hardship negotiations — where tone, negotiation, and real-time response matter. This claim should be validated with A/B data from design partners before it becomes a sales argument.36:T864,

## Demand Signals from Adjacent Products

Nubank's public disclosures indicate it handles over 80% of customer interactions digitally — but voice remains the dominant channel for collections and dispute resolution in markets with lower digital literacy. Konfio and Kueski have both publicly discussed AI investment in customer operations. This is a demand signal, not confirmed purchase intent.

## Defensibility Analysis

The platform incumbents — OpenAI, Google, Amazon — will not build LATAM fintech-specific voice compliance tooling, Spanish-language collections call flow libraries, or integrations with regional CRM providers. This is not a technology gap; it is a go-to-market and domain expertise gap. OpenAI's Realtime API is infrastructure; it does not ship with BACEN-compliant call recording, Portuguese-language dispute resolution scripts, or pre-built Salesforce Financial Services Cloud integrations. Vertical depth, compliance certification, and regional distribution relationships are the moat — and they are moats that platform incumbents structurally cannot prioritize. The honest caveat: if Bland AI or Retell AI decides to pursue LATAM fintech specifically with dedicated resources, they have more capital and developer brand than a seed-stage rebuild. The rebuild must move fast enough to establish reference customers before that happens.

---

## Recommended MVP

## Core Feature 1: Pre-Built LATAM Collections Call Flows

A library of configurable outbound collections call flows in Spanish and Portuguese, compliant with LATAM regulatory frameworks (Brazil's BACEN guidelines, Mexico's CONDUSEF requirements). Each flow handles the full call arc: greeting, debt identification, negotiation, payment arrangement, and call recording with compliant disclosure. This differs from the original Struct in that it is not a blank-canvas platform — it ships opinionated, vertical-specific logic that a LATAM fintech collections team can deploy in days, not months. This matters because collections is the highest-ROI use case for voice automation in LATAM fintech: the cost per resolved account drops dramatically versus human agents, and the compliance risk of getting it wrong is high enough that buyers will pay a premium for a vendor who has already solved it.

## Core Feature 2: Multilingual Voice Quality with Regional Accent Support

Built on ElevenLabs Turbo v2.5 and Cartesia Sonic (both available as of 2025), the platform ships with voice personas tuned for Mexican Spanish, Brazilian Portuguese, Colombian Spanish, and Argentine Spanish — the four largest LATAM fintech markets. Regional accent matching is a meaningful trust signal in collections calls; a caller who sounds like a local is significantly more likely to achieve a positive resolution than a generic "neutral Spanish" voice. The original Struct claimed multilingual support but had no documented regional specificity. This feature makes that claim concrete and measurable.

## Core Feature 3: CRM-Native Integration with Salesforce Financial Services Cloud and HubSpot

Out-of-the-box bidirectional sync with the two CRM platforms most commonly used by LATAM fintech companies at the 50–500 employee scale. Call outcomes, payment arrangements, and contact updates write back to the CRM automatically. This closes the loop that horizontal platforms leave open — Bland AI and Retell require custom API work to achieve the same result. This is the feature that makes the product sticky: once call outcomes are flowing into a customer's CRM, switching costs are high.

## What We Will NOT Build:

- Inbound customer support automation (save for Phase 2 — collections is the wedge)
- English-language call flows (English is where competition is fiercest and differentiation is lowest)
- A self-serve developer API (the original Struct's likely model; the rebuild sells to operations and collections managers, not developers)
- Proprietary ASR or TTS infrastructure (use Cartesia/ElevenLabs; do not rebuild what is now commodity)

## Success Metrics:

- 10 paying LATAM fintech customers within 6 months of launch, each processing a minimum of 1,000 calls/month on the platform
- Average contract value ≥ $2,000/month
- Call resolution rate (payment arrangement reached or dispute resolved without human escalation) ≥ 40% — a threshold that demonstrates ROI versus human agents at LATAM BPO rates (~$8–12/hour)

## Cold-Start Problem:

This product does not depend on network effects or local density. Each customer deployment is independent. The cold-start risk is reputational: the first 3–5 customers are reference customers, and LATAM fintech is a relationship-driven market where a warm introduction from a shared investor or accelerator (e.g., ALLVP, Kaszek, or QED portfolio companies) is worth more than any inbound marketing. The founding team must secure 2–3 design partners before writing a line of product code.

---

## Go-to-Market Strategy

## Target Customer Segment

LATAM fintech companies at the 50–500 employee scale with active lending or BNPL portfolios — specifically those with collections teams of 5–50 human agents who are already spending $15,000–$100,000/month on collections labor or BPO contracts. This segment has a clear, quantifiable pain point, a budget already allocated to the problem, and a decision-maker (VP of Collections or COO) who can sign a contract without a 12-month procurement cycle. Nubank-scale companies are not the initial target — they have internal engineering teams and will build custom solutions. The target is Konfio, Kueski, Addi, Creditas, and the 200+ companies at similar scale across Mexico, Brazil, Colombia, and Argentina.

## Primary Distribution Channel

Direct outbound sales through warm introductions via LATAM fintech investor networks (Kaszek, ALLVP, QED Investors, Monashees). These funds have portfolio companies with exactly the collections automation problem the product solves, and a portfolio company introduction compresses the sales cycle from months to weeks. Secondary channel: LATAM fintech conferences (Finnosummit, Fintech Americas) where the target buyer persona concentrates. The Salesforce AppExchange listing is a medium-term channel (6–12 months post-launch) once the Salesforce FSC integration is production-ready.

## Pricing Strategy

# Velo

## 1. Overview

Velo is a vertical SaaS platform for AI-powered outbound and inbound call automation built specifically for Latin American fintech companies — a modern revival of Struct's multilingual voice agent vision, rebuilt with vertical depth instead of horizontal breadth. Operations and collections managers at LATAM lending companies (50–500 employees) deploy pre-built, compliance-ready Spanish and Portuguese call flows against their loan portfolios without writing a line of code. Velo connects to Salesforce Financial Services Cloud and HubSpot, writes call outcomes back automatically, and replaces $4,000–$6,000/month BPO contracts with AI agents that run 24/7 at a fraction of the cost.

---

## 2. Core Features

**Call Flow Management**
- Library of pre-built LATAM collections call flows in Mexican Spanish, Brazilian Portuguese, Colombian Spanish, and Argentine Spanish
- Visual call flow builder: drag-and-drop nodes for greeting, debt identification, negotiation, payment arrangement, objection handling, and compliant disclosure
- Flow versioning with rollback; A/B test two flows against the same contact list
- Configurable escalation rules: hand off to human agent via warm transfer when sentiment score drops below threshold
- Compliance mode per country: BACEN (Brazil), CONDUSEF (Mexico), SFC (Colombia), BCRA (Argentina) — injects required disclosures automatically

**Voice Agent Configuration**
- Voice persona library: 8 pre-tuned regional voices (2 per market: male/female) built on ElevenLabs Turbo v2.5
- Custom voice cloning: upload 30-second sample, generate brand voice in 24 hours
- Adjustable speech rate, pause duration, and retry cadence per flow
- Real-time sentiment analysis displayed in live call monitor dashboard

**Campaign Management**
- Upload contact lists via CSV or pull directly from CRM integration
- Schedule campaigns: one-time, recurring (daily/weekly), or trigger-based (loan X days past due)
- Concurrency controls: max simultaneous calls per campaign (1–500)
- DNC (Do Not Call) list management with automatic suppression
- Time-zone-aware dialing windows per country

## Differentiation vs. 2026 Competitors

Bland AI, Retell AI, and Vapi sell infrastructure to developers. Struct 2.0 sells outcomes to collections managers. The pitch is not "here is an API to build your voice agent" — it is "here is a compliant, Spanish-language collections agent that is live in your Salesforce instance in two weeks." That positioning difference determines the buyer, the sales motion, the support model, and the pricing — and it is the structural lesson the original Struct never learned.
