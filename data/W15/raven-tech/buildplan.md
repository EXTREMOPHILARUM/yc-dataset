# Build Plan: Raven Tech 2026

## Overview

By 2026, Raven Tech 2.0 is a WeChat Mini Program that turns conversational requests into executed tasks—booking restaurants, arranging transportation, buying tickets, managing reservations—all without switching apps. It's built for urban Chinese professionals (25–40, Tier 1 cities) who live inside the WeChat ecosystem and are tired of context-switching across fragmented services.

The viability shift is LLMs. In 2014, the orchestration layer didn't exist; today, Claude and GPT-4 can reliably chain multi-step tasks with transparent logging and rollback. Combined with open-source Mandarin speech recognition and Model Context Protocol connectors, the core vision becomes technically sound and capital-efficient.

The go-to-market wins on distribution and trust. Launch inside WeChat (zero friction, 1B+ users) rather than as a standalone app. Charge RMB 68/month for unlimited tasks after a free tier. Differentiate against Rabbit R1 through native API integrations (not screen-scraping), Mandarin-first design, and software-only accessibility—no hardware requirement. The moat is ecosystem integration and user trust, not proprietary models.34:T9eb,

## Why Now?

## Current Market Analysis

## Market Size

The global voice assistant market was estimated at approximately $1.8B in 2017 (Voicebot.ai). By 2024, the broader conversational AI and intelligent assistant market is estimated at $14–20B globally, depending on scope definition — exact 2026 projections are unavailable, but the directional growth is unambiguous. The agentic AI software segment specifically is nascent and not yet cleanly sized by public research firms; this is a genuine data gap.

In China, the smart speaker market launched in earnest in 2017 alongside the Raven H, dominated by Alibaba's Tmall Genie and Xiaomi's AI Speaker at sub-RMB 500 price points. That market has since matured into a commoditized, low-margin hardware category — which paradoxically creates an opening for a software-first agentic layer that runs across existing devices rather than competing on speaker hardware.

## Competition Map and Gaps

Current competitors fall into three categories:

- **Rabbit Inc. (Rabbit R1, 2024):** The most direct heir to Raven Tech's vision, built by Jesse Lyu himself. Its specific weakness is that the Large Action Model (LAM) approach relies on screen-scraping rather than native API integration, making it brittle when service UIs change. Early reviews cited inconsistent task completion and limited service coverage. It also targets English-language Western markets primarily.

- **Apple Siri / Google Assistant / Amazon Alexa:** Platform-native assistants with massive distribution but architecturally constrained by legacy design decisions. None executes true multi-step agentic workflows reliably across third-party services as of early 2025. Their weakness is organizational inertia and the conflict of interest in routing users away from their own app ecosystems.

- **Perplexity AI and similar LLM-native assistants:** Strong at information retrieval, weak at action execution and transactional task completion. No dedicated hardware play.

- **Chinese incumbents (Baidu DuerOS, Alibaba AliGenie):** Deeply integrated into their respective ecosystems but siloed — DuerOS cannot natively orchestrate Alipay transactions; AliGenie cannot natively call DiDi. The cross-ecosystem orchestration gap is real and unaddressed.

**The gap:** No current product delivers reliable, cross-platform agentic task execution in Mandarin Chinese, optimized for China's super-app ecosystem, at a premium-but-accessible price point. Demand signals from adjacent products — including the explosive growth of AI coding agents (Cursor, GitHub Copilot) and the consumer enthusiasm for Rabbit R1 preorders — confirm that agentic task execution is the next consumer computing paradigm.

---

## Recommended MVP

## Core Features

## MCP-Native Cross-App Task Orchestration

The product's engine: an LLM agent (built on Claude 3.5 Sonnet or GPT-4o, with API costs declining monthly) that uses Model Context Protocol connectors to execute multi-step tasks across WeChat Mini Programs, Alipay, DiDi, Meituan, and Dianping through their documented APIs. A user speaks or types a single intent; the agent plans, executes, and confirms across services without the user switching contexts. Unlike Raven Tech's hand-coded integrations and unlike Rabbit's screen-scraping LAM, MCP connectors are maintainable and scalable. This is the core thesis, finally technically executable.

## On-Device Mandarin Voice Interface with Whisper-Class ASR

A dedicated voice layer running on-device speech recognition achieving >95% Mandarin accuracy (using open-source Whisper large-v3 or equivalent), with cloud fallback for complex parsing. Privacy-sensitive audio never leaves the device unprocessed — a meaningful differentiator in China's regulatory environment post-2021 data localization rules. Unlike Raven Tech's 2014-era NLU, this layer is reliable enough to be the primary input modality rather than a demo feature.

## Persistent Context Memory Across Sessions

The agent maintains a structured memory of user preferences, frequent services, saved locations, dietary restrictions, and past task patterns — enabling it to anticipate rather than just respond. "Book the usual" becomes a valid command. This directly addresses the context re-entry problem that Lyu identified as the fundamental flaw of the app-grid model. No current Chinese voice assistant offers persistent cross-service contextual memory at this depth.

## Transparent Task Execution Log with One-Tap Rollback

Every action the agent takes is logged in plain language in real time, with a single-tap cancel or rollback at any step. This addresses the trust deficit that agentic AI products face — users are reluctant to grant autonomous action authority without visibility. Rabbit R1's opacity on task execution was a cited criticism; this feature directly differentiates on trust architecture.

## Software-First, Hardware-Optional

Launch as a smartphone app for iOS and Android (China App Store distribution + direct APK for Android). Hardware — a dedicated device co-developed with Teenage Engineering's established pipeline — is a 12-to-18-month roadmap item, not an MVP dependency. This inverts Raven Tech's fatal sequencing error of betting on hardware before proving software demand.

## What We Will NOT Build

- Proprietary LLM or ASR models (use best-available APIs; model training is not the moat)
- Smart speaker hardware at MVP stage
- English-language market features before achieving product-market fit in China
- Social or content features (music streaming, news feeds) — Music Flow was a distraction from the core thesis

## Success Metrics

- 10,000 monthly active users within 6 months of launch, with 40%+ 30-day retention
- Average of 3+ agentic tasks completed per user per week (indicating habitual use, not novelty)
- Task completion rate ≥ 75% across the five core integrated services
- Net Promoter Score ≥ 50 among active users at month 3

---

## Go-to-Market Strategy

## Target Customer Segment

Primary: Urban Chinese professionals aged 25–40 in Tier 1 cities (Beijing, Shanghai, Shenzhen, Hangzhou), earning RMB 20,000+/month, who are heavy users of at least three of the five core integrated services (WeChat, Alipay, DiDi, Meituan, Dianping) and who already use voice input on WeChat. This segment is tech-comfortable, time-constrained, and already habituated to delegating tasks to digital services — they are one step away from delegating the delegation itself. Estimated addressable population: data unavailable at precise segment definition, but China's urban professional class exceeds 100 million people by broad measures.

## Primary Distribution Channel and Tactics

Launch through WeChat Mini Program first — not the App Store. This eliminates the app download friction barrier entirely, reaches users inside the ecosystem the product integrates with, and allows viral sharing of completed task logs ("My AI just booked dinner and a taxi in 8 seconds — try it"). Secondary distribution via Xiaohongshu (Little Red Book) influencer seeding targeting the productivity and tech-lifestyle communities, which have demonstrated strong conversion for premium software tools. Paid acquisition deferred until organic retention metrics are validated.

## Pricing Strategy

Freemium with a hard usage cap: 20 agentic tasks per month free, then RMB 68/month (~$9.50) for unlimited tasks. This price point is calibrated against WeChat's own premium services and positions the product as a professional productivity tool rather than a consumer gadget. Annual plan at RMB 588 (~$82) offered at launch for early adopters, providing 12 months of runway signal and reducing churn. Hardware, when launched, priced at RMB 1,299–1,499 — premium but below the Raven H's fatal RMB 1,699 ceiling, and justified by proven software value rather than design alone.

## Differentiation vs. 2026 Competitors

Against Rabbit R1: native API integration over screen-scraping, Mandarin-first, China-ecosystem-native, software-accessible without hardware purchase. Against Baidu DuerOS and AliGenie: cross-ecosystem orchestration that neither incumbent can offer without cannibalizing their own platform lock-in. Against Apple Siri and Google Assistant: depth of task execution and persistent memory versus breadth of surface-level integration. The moat is not the LLM — it is the MCP connector library for China's super-app ecosystem, the trust architecture of the execution log, and the user memory graph that deepens with every completed task. Each of these compounds over time in ways that a platform assistant optimizing for general-purpose use cannot replicate.
