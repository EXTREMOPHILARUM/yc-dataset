# Build Plan: Storyline 2026

## Overview

Storyline (YC W18) built a drag-and-drop, no-code editor for Amazon Alexa skills — the "Weebly for voice apps" — that attracted 3,000 users and published over 5,000 skills before shutting down in April 2019, killed by a platform whose consumer engagement never materialized, a user base of hobbyists structurally unwilling to pay, and a pivot to voice UX prototyping that introduced a fatal retention problem.

The rebuild thesis is not to bet on Alexa again — it is to bet on the underlying insight that was always correct: non-technical creators cannot build good conversational AI experiences without help. What has changed is that LLMs have collapsed the hardest part of that problem. The new version is a no-code conversational AI builder for small businesses and content creators that generates production-ready, multi-turn AI agents from natural language descriptions — deployable across voice, chat, and messaging channels simultaneously, with usage-based pricing that monetizes proportionally to value delivered rather than demanding a flat subscription from hobbyists.

---34:Tb1d,

## Why Now?

The single most important change since Storyline's failure is that the NLP/NLU quality ceiling — explicitly cited by the Invocable farewell post as a root cause of shutdown — has been structurally demolished. In 2018, Alexa's intent recognition degraded rapidly for anything beyond scripted, single-turn commands. Every Storyline-built skill was only as good as Alexa's ability to parse natural speech variation, and that ability was brittle. Users hit dead ends, abandoned skills, and never returned. No amount of better tooling could fix an underlying platform that couldn't understand open-ended human speech.

GPT-4 (March 2023) and Claude 3 (March 2024) changed this at the infrastructure level. A conversational agent built on top of these models can handle ambiguous inputs, maintain context across multi-turn exchanges, recover gracefully from misunderstandings, and generate responses that feel genuinely intelligent — not because a developer hand-crafted every branch of a decision tree, but because the model handles the long tail of user intent automatically. The tree-based design model that analysts identified as Storyline's core product ceiling is no longer the only architecture available. A rebuilt tool can let creators describe their agent's purpose in plain English and generate the underlying dialogue logic automatically.

The second structural change is platform diversification. Storyline's fatal dependency was single-platform: if Alexa failed, the business failed. In 2026, a rebuilt product can deploy the same conversational agent to Alexa+ (now powered by Claude, per Amazon's 2024 partnership announcement), Google Assistant with Gemini, WhatsApp Business API (2 billion monthly active users), SMS via Twilio, and website chat widgets — all from a single build. No single platform's consumer adoption curve determines the business's survival.

On market size: the global conversational AI market was valued at approximately $10.7 billion in 2023 and is projected to reach $29.8 billion by 2028 (MarketsandMarkets, 2023 — exact figures should be independently verified before fundraising). The no-code AI builder segment specifically is harder to isolate, but Voiceflow's continued operation and reported growth into enterprise accounts confirms durable category demand. The small business segment — the specific target here — is large and underserved: the U.S. alone has approximately 33 million small businesses (SBA, 2023), the majority of which have no conversational AI presence of any kind.

Distribution channels unavailable in 2018 now exist at scale: the Shopify App Store (2M+ merchants), the HubSpot App Marketplace (200,000+ customers), and the Zapier integration ecosystem (6,000+ connected apps) all provide direct access to the small business operators who are the target customer.

---

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

*Natural Language Agent Builder*
A creator describes their agent's purpose, personality, and knowledge base in plain English — "I run a yoga studio and want an agent that answers questions about class schedules, handles new student inquiries, and books intro sessions" — and the system generates a working conversational agent with appropriate dialogue logic, fallback handling, and knowledge retrieval. This directly addresses the root cause Storyline's post-mortem identified: the product thinking barrier was higher than the technical barrier. LLM-generated agent scaffolding lowers the product thinking barrier for the first time, not just the coding barrier. Unlike Storyline's tree-based editor, creators are not required to map every conversational branch manually.

*Multi-Channel Deployment (Website Chat + WhatsApp, Voice Deferred)*
The MVP deploys to two channels: an embeddable website chat widget and WhatsApp Business API. Voice (Alexa+, Google) is explicitly deferred to v2. This is the single most important constraint relative to the original Storyline. The 2018 failure was caused by single-platform dependency on a channel with unproven consumer engagement. Website chat and WhatsApp have proven, high-volume consumer engagement today. Voice is a real opportunity given Alexa+'s Claude integration, but it is not the beachhead — it is the expansion.

*Business Knowledge Integration*
Creators connect their agent to existing business data: a Google Calendar for availability, a Notion page for FAQs, a Shopify product catalog, or a simple document upload. The agent uses retrieval-augmented generation (RAG) to answer questions accurately from this knowledge base rather than hallucinating. This is the feature that separates the product from generic chatbot builders and creates stickiness: the agent becomes more valuable as the business's data grows.

*Usage-Based Analytics and Billing*
Session counts, conversation completion rates, handoff-to-human rates, and unanswered question logs — surfaced in a dashboard the creator can act on without a developer. Billing is usage-based (per 1,000 messages processed), not flat subscription, directly addressing the freemium conversion failure that killed Storyline's unit economics. Power users pay proportionally more; hobbyists are not forced to commit to $49–99/month upfront.

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
