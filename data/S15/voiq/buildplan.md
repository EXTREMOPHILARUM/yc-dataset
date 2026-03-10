# Build Plan: VOIQ 2026

## Overview

By 2026, VOIQ is a lightweight CRM-native voicebot that lives inside HubSpot and Salesforce—not a standalone platform. It handles three specific outbound motions: lead follow-up, demo no-shows, and qualification calls. The product is built for Series A–C SaaS sales teams (10–50 reps) who need to compress response times and reclaim 10+ hours per rep per week from manual dialing.

The viability shift is simple: the AI voice stack is now commoditized. GPT-4, real-time speech APIs, and production-grade voice synthesis are available as APIs. VOIQ doesn't need to build the AI—it needs to build the workflow layer that makes it useful inside the tools sales teams already live in. That's a 6-month engineering problem, not a 3-year frontier research problem.

Go-to-market is land-and-expand through CRM integrations. Launch with a one-click workflow trigger that initiates calls without leaving the contact record, auto-logs outcomes, and transfers hot prospects to humans with full context. Sell directly to VP Sales at companies already paying for HubSpot. The product sells itself because it removes friction, not because it's magic.34:T866,

## Why Now?

The single most important change since VOIQ's failure is the commoditization of the entire conversational voice AI stack. In 2019–2021, VOIQ was attempting to assemble speech recognition, natural language understanding, and voice synthesis into a production system from scratch — with 21 people and $5M total. That engineering challenge broke the team. In 2026, every component is an API call.

Specifically: Deepgram's Nova-2 speech-to-text model (released 2023) delivers sub-300ms transcription latency with industry-leading accuracy across accents and background noise. ElevenLabs' voice cloning API (commercially available 2023) replicates VOIQ's "Clone-Your-Voice" differentiator at approximately $0.30 per 1,000 characters — a feature VOIQ treated as a competitive moat now costs pennies. Twilio's Programmable Voice with Media Streams enables real-time audio piping to LLM backends. Most critically, GPT-4 (March 2023) and its successors — including GPT-4o (May 2024) with native audio processing — provide the open-ended natural language understanding that VOIQ's pre-transformer NLU stack could never reliably deliver. Platforms like Vapi, Bland.ai, and Retell AI (all launched 2023–2024) have already assembled these components into orchestration layers specifically for outbound AI calling agents, meaning a rebuilt VOIQ can build *on top of* infrastructure rather than building the infrastructure itself.

The market has also been validated in ways it hadn't been by 2022. Gong reached a $7.25B valuation (per public reporting), and Outreach and Salesloft achieved unicorn status, confirming enterprise willingness to pay for AI-assisted sales workflows. The AI voice agent market specifically is projected to grow substantially through 2027, though precise figures for the outbound-only segment are not publicly available. Distribution is now cleaner too: the HubSpot App Marketplace serves 200,000+ businesses, and the Salesforce AppExchange hosts 7,000+ apps with direct access to enterprise procurement workflows — channels VOIQ listed as partners but could not fully leverage given immature API ecosystems in 2019.

---

## Current Market Analysis

The global conversational AI market was valued at approximately $17B in 2019 (the call center software segment VOIQ cited). By 2024, analyst estimates place the broader conversational AI market at $14–29B depending on scope definition — exact figures vary significantly by source and methodology, so treat these as directional rather than precise. The AI voice agent sub-segment is newer and not yet cleanly measured in public research.

What is measurable is competitive structure. The current landscape has bifurcated in a way that creates a specific gap:

**Infrastructure players** — Vapi, Bland.ai, and Retell AI provide developer-facing APIs for building AI calling agents. Their weakness is that they are tools, not products: they require engineering resources to configure, have no CRM-native workflows, and offer no industry-specific conversation templates. They serve technical buyers, not sales operations teams.

**Enterprise conversation intelligence** — Gong and Chorus (acquired by ZoomInfo) analyze calls made by *human* reps. They do not replace callers. Their weakness is that they assume a human is already on the phone — they do not address the cost of getting a human on the phone in the first place.

**Outbound sequencing platforms** — Outreach and Salesloft automate email and call *scheduling* but still require a human to execute the call. Both have added AI coaching features but have not moved into autonomous voice agents, likely due to enterprise risk aversion.

**Emerging direct competitors** — AiSDR, Artisan, and 11x.ai are building AI sales development representatives, primarily text-based (email/LinkedIn). Voice remains underserved in this category.

The gap is clear: no current product combines CRM-native workflow integration, pre-built outbound conversation templates for specific sales motions, and production-ready AI voice — packaged for a non-technical sales operations buyer. That is exactly the product VOIQ attempted to build and the market that remains unoccupied at the mid-market level.

Demand signals from adjacent products confirm pull: Calendly reports that automated meeting scheduling has become a default workflow for sales teams; HubSpot's Sequences product has millions of active users running outbound cadences — all of whom currently rely on humans to make the actual calls.

---

## Recommended MVP

### Core Feature 1: CRM-Native Voicebot Launcher

A one-click workflow trigger inside HubSpot and Salesforce that initiates an AI outbound call to a contact record without leaving the CRM interface. The voicebot pulls contact data (name, company, prior interactions) from the CRM to personalize the opening. This matters because VOIQ's biggest friction point was the separate platform login — embedding directly into existing workflows eliminates the adoption barrier that kept customer counts flat. Unlike VOIQ's 2019 implementation, this is built on HubSpot's 2024 App Marketplace APIs with native webhook support, requiring no custom middleware engineering.

## Core Feature 2: Conversation Playbooks with Guardrails

Pre-built, editable conversation flows for three specific outbound motions: inbound lead follow-up (sub-5-minute response), demo no-show re-engagement, and trial expiration conversion. Each playbook uses GPT-4o (May 2024) for natural language handling but constrains the AI to a defined topic boundary — preventing off-script hallucinations that would have plagued VOIQ's open-ended approach. This differs from VOIQ's original design, which attempted fully open-ended conversation; guardrailed playbooks trade flexibility for reliability, which is the correct tradeoff for a 2026 MVP.

## Core Feature 3: Live Transfer with Context Handoff

When a prospect expresses strong buying intent, the AI immediately transfers the call to a human rep and simultaneously pushes a real-time summary — prospect's stated objections, expressed interest level, confirmed availability — to the rep's screen via CRM activity log. This preserves the human-in-the-loop model that enterprise buyers require for high-value deals, and directly addresses the quality-control failure mode that drove VOIQ's churn.

## Core Feature 4: Call Outcome Auto-Logging

Every call result — connected, voicemail left, objection raised, meeting booked — is automatically written back to the CRM contact record with a transcript and AI-generated next-step recommendation. This closes the reporting loop that sales managers require to justify the tool's ROI and creates the retention stickiness VOIQ lacked.

**What you will NOT build:** Custom voice synthesis infrastructure (use ElevenLabs API), proprietary speech-to-text (use Deepgram), inbound call handling, website voice widgets, or any non-sales vertical (no healthcare, no government, no fundraising). VOIQ's opportunistic pivots into COVID response and nonprofit fundraising diluted engineering focus without generating revenue. Every sprint targets the outbound B2B sales motion exclusively.

## Success Metrics:

- 50 paying customers within 6 months of launch (VOIQ reached 700 but likely inherited them from a prior product; 50 net-new SaaS customers is the honest benchmark)
- Net Revenue Retention ≥ 110% at month 6 (flat NRR was VOIQ's silent warning signal)
- Average calls-to-meeting-booked conversion rate ≥ 8% across customer accounts (below this threshold, customers will not renew)
- Median time-to-first-call after signup ≤ 20 minutes (measures onboarding friction, the primary churn driver for sales tools)

---

## Go-to-Market Strategy

**Target Customer Segment:** Series A–C B2B SaaS companies with 10–50 person sales teams running outbound prospecting motions, using HubSpot or Salesforce as their CRM, with a minimum of 500 outbound call attempts per month per rep. This is narrow by design. VOIQ's 700-customer base included enterprises like AB-InBev and Aflac alongside small businesses — a spread that made it impossible to optimize the product for any single workflow. The target segment above has a specific, measurable pain (cost and inconsistency of SDR outbound calls), a defined tech stack (HubSpot/Salesforce), and sufficient call volume to generate ROI data within 30 days of deployment.

**Primary Distribution Channel:** HubSpot App Marketplace (200,000+ businesses) combined with direct outbound to HubSpot Solutions Partners — the agency network that implements HubSpot for mid-market companies. Solutions Partners are a force multiplier: a single partner firm manages 20–50 client accounts and will recommend tools that reduce their implementation workload. VOIQ listed HubSpot as a distribution channel but did not document a partner-led motion. Prioritize 10 Solutions Partner relationships in the first 90 days before investing in paid acquisition.

**Pricing Strategy:** Usage-based with a monthly minimum. $0.08–0.12 per connected minute (industry-standard range for AI voice APIs with margin; exact competitive pricing should be validated against Bland.ai and Vapi current published rates, which were not available at time of writing) plus a $500/month platform fee covering CRM integration, playbook management, and reporting. This structure mirrors Twilio's successful model — low barrier to start, costs scale with value delivered — and avoids the flat-subscription trap that made VOIQ's unit economics fragile when customers reduced call volume.

**Differentiation vs. 2026 Competitors:** Against Vapi and Bland.ai: zero engineering required to deploy (they require developers; this product requires a sales ops manager). Against Outreach and Salesloft: the call is executed autonomously, not just scheduled. Against AiSDR and Artisan: voice-first rather than email-first, targeting the 40–60% of prospects who do not respond to email sequences but will engage on a well-timed phone call. The positioning statement is precise: *the only AI outbound calling tool that a sales operations manager can deploy in 20 minutes inside the CRM they already use.*
