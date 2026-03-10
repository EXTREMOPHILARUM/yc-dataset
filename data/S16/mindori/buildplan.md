# Build Plan: Mindori 2026

## Overview

By 2026, Mindori is a lightweight voice-search widget for Shopify merchants—not a platform play, not a custom ASR vendor. It's a $49/month app that sits in the search bar, lets shoppers refine products by voice across multiple turns, and requires zero technical setup. The target: fashion and home-goods sellers with 1K–50K monthly sessions who are losing conversion on mobile because typing is friction.

The market shift is simple: ASR is now a commodity. Google's speech-to-text API is accurate enough for e-commerce, and LLMs handle conversational refinement. In 2016, building voice search meant building ASR from scratch—impossible for a three-person team competing against Amazon. Today, the moat is gone. What matters is distribution and UX. Shopify merchants are actively searching for search tools (Searchie, Boost Commerce rank top-10 in the App Store). Voice is still rare enough to be a differentiator, but common enough that users expect it.

The play is pure Shopify App Store: freemium entry, usage-based scaling, and a 90-day target of 100 active merchants. Win on simplicity and price against Shopify's native search (which has no voice) and enterprise tools like Algolia (which cost 10x more and require engineering). Conversion lift32:T813,

## Why Now?

The single most important change since Mindori's failure is the collapse of the custom ASR moat. In 2016, building accurate voice recognition for a specific product catalog required original neural network research — the kind Lengerich and Hannun published at NeurIPS. That work was Mindori's core technical differentiator and also its most expensive bottleneck: every new customer required retraining models on their catalog data, creating a per-customer labor cost that a three-person team could not scale. OpenAI's Whisper (September 2022) eliminated this problem entirely. Whisper provides high-accuracy, domain-adaptable transcription at near-zero marginal cost as an open-source model. The hard part of Mindori's stack is now a commodity.

What replaced the ASR moat is a genuinely new capability: conversational query understanding via large language models. GPT-4 (March 2023) and Claude 3 (March 2024) can interpret multi-turn voice queries — "Show me trail runners," then "What about in red, under $90?" — with contextual coherence that Mindori's RNN-based system could only approximate. Critically, this works against any product catalog without catalog-specific model training, because the LLM reasons over structured product data at inference time rather than encoding catalog knowledge into model weights.

The distribution problem that killed Mindori has also structurally reversed. The Shopify App Store now serves 2M+ merchants (Shopify, 2024 annual report) and represents a self-serve acquisition channel that requires no enterprise sales motion. In 2016, reaching mid-market e-commerce companies meant cold outreach to engineering teams. In 2026, it means publishing an app that merchants install in three clicks.

Voice commerce adoption is no longer a thesis — it is documented behavior. Global smart speaker installed base exceeded 500M units by 2023 (data source: Statista; specific 2025–2026 figures unavailable at time of writing). Consumer willingness to shop by voice, which Mindori had to assume, is now a validated premise.

---

## Current Market Analysis

## Market Size

Global e-commerce reached approximately $5.8 trillion in 2023 (eMarketer), compared to roughly $1.9 trillion in 2016 when Mindori operated — a 3x expansion of the underlying market. The e-commerce search software segment specifically is harder to isolate; precise 2026 figures are not available at time of writing. The voice commerce sub-segment was estimated at $19.4 billion globally in 2023 by Juniper Research, though this figure aggregates smart speaker commerce, in-app voice, and voice-assisted browsing in ways that make direct comparison to Mindori's original TAM difficult.

## Competition Map

The current competitive landscape has three distinct tiers, each with exploitable weaknesses:

*Platform-bundled search* (Shopify Search & Discovery, Amazon's native search): These tools are text-first and optimized for the median merchant. They offer no voice interface and no conversational follow-up capability. Their weakness is deliberate genericness — they cannot be customized for catalog-specific terminology or shopping behavior patterns.

*Enterprise AI search* (Coveo, Algolia NeuralSearch, Constructor.io): These are sophisticated products targeting enterprise retailers with six-figure annual contracts and multi-month implementation timelines. Coveo's entry price is publicly estimated above $30,000/year; Algolia's AI search tier is similarly positioned. Their weakness is inaccessibility to the 100,000+ mid-market Shopify merchants who need better search but cannot justify enterprise procurement cycles.

*General-purpose voice assistants* (Siri, Google Assistant, Alexa): Still present, still powerful, still not embeddable in a merchant's branded app with catalog-specific context. The structural limitation Mindori identified in 2016 — that platform voice lives inside the platform's ecosystem, not inside a retailer's branded experience — remains true in 2026.34:T738,

## Demand Signals

Shopify's own search app category shows consistent top-chart presence for products like Searchie and Boost Commerce Search, indicating sustained merchant demand for search improvements beyond native functionality. The headless commerce movement (commercetools, Hydrogen) explicitly decouples search from platform defaults, signaling that mid-market merchants are actively seeking composable best-of-breed search solutions — the exact market posture that makes a voice search plugin viable.

---

## Recommended MVP

## Core Features

*Voice-to-conversational-search widget.* A lightweight JavaScript widget (plus Shopify App Block) that captures voice input via browser microphone, transcribes it using Whisper API, and passes the transcript to an LLM-powered search layer that queries the merchant's existing product catalog via Shopify's Storefront API. Unlike Mindori's catalog-specific model training, this requires zero onboarding customization — the merchant installs the app and the widget is live within minutes. This is the fundamental architectural difference from the original: inference-time reasoning over catalog data rather than catalog-encoded model weights.

*Multi-turn query refinement.* The system maintains a session-scoped conversation context, allowing shoppers to say "Show me running shoes" and follow with "What about waterproof ones under $120?" without re-stating the full query. GPT-4o (May 2024) handles this reliably in under 500ms at current API pricing. The original Mindori product attempted this with RNN-based state management; the 2026 version achieves it with dramatically higher accuracy using off-the-shelf LLM context windows.

*Multimodal product matching.* Using GPT-4V or Gemini 1.5 Pro (both available as of 2024), the system can match voice queries against product images and text descriptions simultaneously — enabling queries like "Find me something that looks like a Chelsea boot but in suede." This capability was technically impossible for Mindori in 2016 and represents a genuinely new product surface that no current mid-market Shopify search app offers.

*Merchant analytics dashboard.* A simple interface showing top voice queries, zero-result queries, and conversion rates by query type. This is not a differentiator — it is table stakes for merchant retention and the primary mechanism for demonstrating ROI at renewal.

## What We Will NOT Build

No custom ASR model training per merchant. No native iOS/Android SDK (browser-based only for MVP). No chatbot or messaging platform integrations (the 2016 bet that failed). No enterprise sales motion or custom implementation services.

## Success Metrics

- 100 active Shopify merchants within 90 days of App Store launch
- ≥15% of store sessions using the voice widget at least once (among merchants with >500 monthly sessions)
- Voice-initiated sessions converting at ≥80% of the merchant's baseline text-search conversion rate
- Month-2 merchant retention ≥70%

---

## Go-to-Market Strategy

## Target Customer Segment

Shopify merchants on the Basic or Shopify plan (not Plus) with 1,000–50,000 monthly sessions and a product catalog of 200–5,000 SKUs. Specifically: fashion, footwear, outdoor gear, and home goods merchants where product discovery is attribute-rich (color, size, material, style) and where voice's ability to express multi-attribute queries in natural language provides the clearest UX advantage over text search. This segment is large enough to build meaningful revenue but small enough to be ignored by Coveo and Constructor.io.

## Primary Distribution Channel

Shopify App Store, exclusively for the first 12 months. Tactics: (1) optimize App Store listing for "voice search," "AI search," and "conversational search" keywords; (2) target the Shopify Partners program to recruit agency partners who install apps on behalf of merchants; (3) publish benchmark data comparing voice-initiated vs. text-initiated conversion rates using anonymized aggregate data from early merchants — this is the primary content marketing asset. No outbound sales until 500 active merchants.

## Pricing Strategy

Freemium with usage-based scaling. Free tier: up to 500 voice queries/month (sufficient for a merchant to validate the product). Paid tier: $49/month for up to 10,000 queries, $149/month for up to 50,000 queries, custom pricing above. Justification: Shopify merchants are accustomed to app subscription pricing in the $20–$200/month range; usage-based tiers align cost with merchant scale and create natural expansion revenue. This pricing is deliberately inaccessible to enterprise (no annual contracts at launch), which keeps the sales motion self-serve.

## Differentiation vs. 2026 Competitors

Against Shopify's native search: voice input and multi-turn refinement, unavailable natively. Against Algolia/Coveo: 10x lower price, zero implementation time, self-serve. Against general voice assistants: lives inside the merchant's branded storefront, not inside Apple's or Amazon's ecosystem — the same positioning Mindori identified correctly in 2016, now executable through a distribution channel that actually reaches the target customer.
