# Build Plan: Demo Gorilla 2026

## Overview

## Why Now?

## Current Market Analysis

**Market size:** The sales enablement market was approximately $2.6 billion in 2022 with projected 15%+ CAGR through the mid-2020s, per the research report. A precise 2026 figure is not available in the provided data. The presales and interactive demo tooling sub-segment remains smaller but has grown substantially given the collective fundraising of Navattic, Reprise, Walnut, and Storylane since 2022.

## Competition map and gaps:

*Conversation intelligence (Gong, Chorus/ZoomInfo):* These platforms dominate post-call analysis and have expanded into pre-call coaching. Their weakness is timing — they analyze what happened after the deal is won or lost, not during the live moment. Gong's enterprise pricing (typically $100K+ ACV at scale) also leaves mid-market teams underserved.

*Sales content management (Highspot, Seismic):* Both are valued at $3B+ and serve large enterprises with deep content libraries. Their weakness is activation — content sits in a repository and relies on reps to retrieve it manually before or during a call. Neither delivers contextual, real-time surfacing during a live demo.

*Interactive demo tools (Navattic, Reprise, Walnut, Storylane):* These tools create polished, shareable product tours for async or prospect-facing use. Their weakness is that they serve the buyer experience, not the rep experience — they do not help a live rep navigate an unscripted conversation.

*AI sales coaching (Second Nature, Quantified):* These platforms focus on pre-call practice and simulation. They do not operate during live calls.

**The gap that remains:** No current competitor specifically addresses the live, in-call moment for the rep — real-time, contextual talking point surfacing during an unscripted enterprise demo. This is the same gap Demo Gorilla identified in 2022, and it remains unfilled by any well-funded incumbent.

**Demand signals:** The rise of AI SDR and AI AE tools (Artisan, 11x, Piper) signals that enterprise buyers are actively seeking AI tools that reduce rep cognitive load during live interactions — making Demo Gorilla's core value proposition more immediately legible to buyers than it was in 2022.

---

## Recommended MVP

## Core Feature 1: LLM-Powered Live Talking Point Engine

A browser extension overlay that surfaces persona-specific talking points in real time as a rep navigates a live browser-based SaaS demo. Unlike Demo Gorilla's 2022 version — which relied on GPT-3-class generation with unreliable accuracy — this version uses GPT-4o or Claude 3.5 Sonnet to generate content grounded in the company's own product documentation, uploaded battlecards, and CRM deal context, dramatically reducing hallucination risk. The rep sees three to five concise, sourced talking points per product screen, not a wall of AI-generated prose.

## Core Feature 2: CRM-Synced Deal Context Loader

At call start, the extension automatically pulls the relevant opportunity record from Salesforce or HubSpot via their modern APIs — deal stage, persona, known pain points, previous objections — and uses that structured data to personalize the talking point set for that specific meeting. This replaces the manual pre-call configuration that was a friction point in the original product and was not feasible at scale with 2022 API infrastructure.

## Core Feature 3: Objection Response Library with AI Retrieval

A searchable, team-maintained library of approved objection responses and competitive differentiators, surfaced by the extension when the rep types a keyword or the meeting transcript (via Otter.ai or Fireflies integration) detects a known objection phrase. This is a human-in-the-loop layer that Demo Gorilla's original product lacked — ensuring that the most sensitive content (competitive claims, pricing responses) is human-authored and reviewed, not purely AI-generated.

## What we will NOT build (MVP scope):

- Native desktop app or mobile demo support
- Post-call analytics or call recording (Gong owns this; do not compete)
- Async or prospect-facing interactive demo creation (Navattic's territory)
- Custom AI model training or fine-tuning infrastructure

## Success metrics with thresholds:

- 25 paying teams within 90 days of launch
- Net Revenue Retention > 110% at 6 months (indicating reps are expanding seats)
- Weekly active usage rate > 60% among licensed reps (the core adoption signal Demo Gorilla likely could not demonstrate)
- Average onboarding time < 30 minutes per rep (critical for sales team adoption)

---

## Go-to-Market Strategy

**Target customer segment:** Mid-market B2B SaaS companies (100–1,000 employees) with a dedicated sales engineering function of two to ten SEs supporting an AE team. This segment has enough deal complexity to need persona-specific talking points, enough budget to pay for tooling ($10K–$40K ACV range), and enough organizational structure that a VP of Sales or Head of Sales Engineering can approve a purchase — without the enterprise IT procurement gauntlet that blocked browser extension adoption at large enterprises. Specifically prioritize companies that have already purchased Gong or Chorus, signaling an established budget for sales intelligence tooling.

**Primary distribution channel:** The Chrome Web Store combined with a direct outbound motion targeting Sales Engineering leaders on LinkedIn. Browser extension distribution has been validated at enterprise scale by Apollo.io's Chrome extension and Grammarly (30M+ users), per the research report. The install-to-value loop is fast: a rep installs the extension, connects their HubSpot or Salesforce account, and sees live talking points in their next demo within 30 minutes. This PLG motion — which Demo Gorilla appears not to have built — is the primary conversion mechanism. Supplement with a free 14-day trial tier requiring no credit card.

**Pricing strategy:** $49 per seat per month (billed annually), with a minimum of five seats, yielding a floor ACV of approximately $2,940. Team plans at 10+ seats unlock the objection library and CRM sync at $39/seat. This is deliberately below Gong's pricing tier to avoid being evaluated as a Gong replacement, and above the free tools (Otter.ai) to signal enterprise-grade reliability. Pricing is justified by the per-rep productivity framing: one additional closed deal per quarter per rep pays for the annual subscription many times over.

**Differentiation vs. 2026 competitors:** The rebuild's core differentiation is specificity of moment — it operates exclusively during the live demo, a workflow gap that Gong (post-call), Highspot (pre-call), and Navattic (async) all explicitly do not address. The human-in-the-loop objection library differentiates from pure AI generation tools by giving sales leaders control over the most sensitive content, addressing the enterprise trust barrier that likely limited Demo Gorilla's original adoption.
