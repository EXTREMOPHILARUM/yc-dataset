# Build Plan: Storyline 2026

## Overview

Storyline (YC W18) built a drag-and-drop, no-code editor for Amazon Alexa skills — the "Weebly for voice apps" — that attracted 3,000 users and published over 5,000 skills before shutting down in April 2019, killed by a platform whose consumer engagement never materialized, a user base of hobbyists structurally unwilling to pay, and a pivot to voice UX prototyping that introduced a fatal retention problem.

The rebuild thesis is not to bet on Alexa again — it is to bet on the underlying insight that was always correct: non-technical creators cannot build good conversational AI experiences without help. What has changed is that LLMs have collapsed the hardest part of that problem. The new version is a no-code conversational AI builder for small businesses and content creators that generates production-ready, multi-turn AI agents from natural language descriptions — deployable across voice, chat, and messaging channels simultaneously, with usage-based pricing that monetizes proportionally to value delivered rather than demanding a flat subscription from hobbyists.

---34:Tb1d,

## Why Now?

## Current Market Analysis

## Market Size

The addressable market in 2018 was structurally capped by the Alexa Skills ecosystem — a platform with tens of millions of devices but consumer behavior concentrated in native functions. The 2026 addressable market is categorically different: it is the small business conversational AI market, not the Alexa tooling market. Exact TAM figures for the no-code conversational AI builder segment are not available in the research report and should not be invented here; the MarketsandMarkets $10.7B–$29.8B range for the broader conversational AI market is the best available proxy.

## Competition Map

*Voiceflow* — The direct survivor of the 2018 consolidation. Voiceflow absorbed Storyline's user base, raised $4.7M CAD in 2019, and has since pivoted toward enterprise conversational AI design. Its specific weakness in 2026 is that it has followed the money upmarket: its pricing, feature complexity, and sales motion are now oriented toward enterprise design teams, not the small business operator or solo content creator. The hobbyist and SMB segment that Storyline originally served is effectively unaddressed by Voiceflow's current positioning.

*Botpress* — An open-source conversational AI builder with a strong developer community. Its weakness is the inverse of Voiceflow's: it is deeply technical, requiring familiarity with JavaScript, NLU configuration, and self-hosting. It is not a credible option for a non-technical small business owner.

*Manychat* — A no-code chatbot builder focused on Instagram and Facebook Messenger, with strong SMB adoption. Its weakness is channel narrowness (Meta-platform-dependent) and limited AI sophistication — it is primarily a rule-based flow builder, not an LLM-powered agent builder. It does not support voice channels.

*Tidio, Intercom, Drift* — Customer support chat tools with AI features bolted on. Their weakness is that they are support-first products, not creator-first tools. They do not support voice deployment, and their AI features are oriented toward deflecting support tickets, not enabling creators to build original conversational experiences.

## Demand Signals

The strongest demand signal is Voiceflow's own survival and upmarket pivot: a company that absorbed Storyline's displaced users and raised capital in the same month Invocable shut down has now moved away from the SMB segment, creating a gap. Manychat's reported 1M+ business users on Meta channels signals that small businesses will adopt no-code conversational tools when the channel has proven consumer engagement — the key condition that Alexa failed to meet in 2018.

## Defensibility Against Platform Incumbents

This is the honest hard question. Amazon (Alexa+), Google (Gemini-powered Assistant), and Meta (WhatsApp Business) all have adjacent products and could theoretically build no-code agent creation tools. The structural argument for defensibility is threefold: (1) these platforms are incentivized to grow their own ecosystems, not to build neutral multi-channel tools that deploy to competitors; (2) the SMB segment requires integrations with third-party business tools (CRMs, booking systems, e-commerce platforms) that platform incumbents have no incentive to prioritize; and (3) the original Storyline failure was platform dependency, not platform competition — Amazon never built a no-code skill builder that killed Storyline; the platform's consumer adoption failed. The rebuild's multi-channel architecture is the primary structural defense. If the product is genuinely platform-agnostic, no single platform's strategic decision can replicate the 2019 failure mode. This defense is real but not airtight: if OpenAI, Google, or Amazon builds a sufficiently good no-code agent builder and bundles it with their existing SMB products, the competitive position weakens. This risk should be disclosed to investors.

---37:T934,

## Recommended MVP

## Core Features

## What We Will NOT Build

No voice channel at launch. No enterprise team collaboration features. No white-label reseller tier. No custom LLM fine-tuning. No native mobile app. These are v2 decisions, not MVP decisions.

## Success Metrics

- 500 active agents deployed (not just created) within 90 days of launch
- 20% of users generating at least 1,000 messages/month (the threshold at which usage-based billing produces meaningful revenue)
- 60-day retention rate of 40% or higher among users with connected business data integrations
- Average revenue per active user of $30+/month within 6 months

## Cold-Start Problem

This product does not depend on network effects or local density. An agent delivers value to its creator from the first conversation it handles. There is no minimum user threshold before the core feature works.

---

## Go-to-Market Strategy

## Target Customer Segment

The beachhead customer is the solo operator or two-to-five person small service business — yoga studios, tutoring centers, independent consultants, local restaurants, real estate agents — that receives repetitive inbound inquiries it cannot staff to answer consistently. This is deliberately narrower than Storyline's "content creators and hobbyists" framing. These customers have a clear, recurring pain (missed inquiries = missed revenue), an existing willingness to pay for tools that solve operational problems, and no technical staff to build a custom solution.

## Primary Distribution Channel

The Shopify App Store (2M+ merchants) and the HubSpot App Marketplace (200,000+ customers) are the primary distribution channels. Both provide direct access to small business operators who are already paying for software tools and have demonstrated willingness to adopt new ones. Secondary channel: direct outreach to local business communities via Alignable (4M+ small business members) and niche Facebook Groups for specific verticals (yoga studio owners, tutoring center operators). Content marketing targeting "how to add AI to my [business type]" search queries is a lower-cost acquisition channel that compounds over time.

## Pricing Strategy

Free tier: up to 500 messages/month, one active agent, website chat only. This is not a hobbyist tier — it is a trial tier designed to let a small business validate that the agent works before committing to payment. Paid tiers: $29/month (5,000 messages, two channels), $79/month (25,000 messages, three channels, business data integrations), usage overage at $0.01/message above tier limits.

Stress test against free alternatives: A small business owner can handle inbound inquiries via WhatsApp manually (free), set up a Manychat flow (free tier available), or use a basic Tidio chatbot (free tier available). The rebuild's price is justified if and only if the LLM-powered agent demonstrably handles a wider range of questions without manual intervention — reducing the owner's time cost, not just adding a feature. The $29/month entry price is below the threshold where a solo operator will scrutinize ROI carefully; the $79/month tier requires a clear demonstration that the agent is handling inquiries that would otherwise require a part-time hire or result in lost business. Pricing should be tested against this framing explicitly in early sales conversations.39:T8e9,

## Differentiation vs. 2026 Competitors

Against Voiceflow: dramatically simpler, SMB-priced, no design team required. Against Manychat: LLM-powered open-ended conversation vs. rule-based flows; multi-channel including non-Meta channels. Against Tidio/Intercom: creator-first tool for building original agent experiences, not a support ticket deflection layer. The single clearest differentiation claim: "Describe your business in plain English. Your AI agent is live in 10 minutes."

---

*Note: All market size figures cited from third-party sources (MarketsandMarkets, SBA) should be independently verified before use in investor materials. Revenue and user figures for current competitors (Voiceflow, Manychat) are not confirmed in the research report and have not been invented here.*
