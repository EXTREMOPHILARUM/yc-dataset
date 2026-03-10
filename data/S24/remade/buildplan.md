# Build Plan: Remade 2026

## Overview

Remade was a San Francisco-based YC S24 company that built AI-powered video ad automation for lifestyle brands and delivery platforms, raised $500K, and was acqui-hired by generative media platform fal in November 2025 after approximately 12–15 months of operation — with strong developer traction (250K+ LoRA downloads, millions of generations) but thin commercial revenue and only one named paying customer.

The rebuild thesis is not to retry the canvas product that killed Remade's focus, but to go narrower and lower in the stack: a TikTok Shop-native video creative engine for SMB sellers, built on the same open-source I2V infrastructure Remade proved out, priced per generation, and distributed where the buyers already are. The original failure was a distribution problem dressed up as a product problem — and TikTok Shop's $20B+ US GMV has since created a buyer pool large enough to solve it.

---

## Why Now?

The single most important change since Remade's failure is the emergence of TikTok Shop as a mass-market commerce channel with an urgent, unmet demand for short-form video creative at scale. TikTok Shop reached $20B+ GMV in the US in 2024 (per the rebuild signals in the research report), and the seller base — predominantly SMBs and individual merchants — cannot afford agency video production and lacks the technical sophistication to use a canvas tool. This is a fundamentally different buyer than the enterprise CMOs Remade was targeting. The demand is real, the urgency is high, and the willingness to pay per output (rather than per seat) aligns with how SMB merchants already think about cost.

The second critical change is inference economics. GPU costs for video generation dropped approximately 10x between mid-2024 and late 2025, driven by H100 availability and model efficiency improvements including Wan2.1's 480p variant (per the research report). fal's current API pricing runs $0.003–$0.009 per second of video, making a per-generation model with meaningful gross margin calculable in a way it was not during Remade's operating period.

On the model capability side, Wan2.1 (released publicly in early 2025) and CogVideoX now enable sub-$0.10 per video inference for short-form clips. IP-Adapter and portrait-consistent image-to-video models have made consistent character and product rendering a solved problem as of 2025 — removing the technical barrier that frustrated Remade's enterprise customers needing brand-consistent creative. These are not incremental improvements; they are the difference between a product that works reliably and one that requires manual correction.

Distribution channels that did not exist or were immature in 2024 now provide direct access to the target buyer: TikTok Shop's seller center (exact merchant count not publicly confirmed, but US GMV scale implies hundreds of thousands of active sellers), Shopify's App Store with 2M+ merchants, and the TikTok for Business ad platform. These are pull channels — merchants are already looking for video creative solutions inside these environments.

Adjacent validation has also arrived: Yelp, DoorDash, and Instacart have all launched internal AI-generated menu and product photography tools (per the research report), confirming that the demand Remade was pitching to delivery platforms is real and that the category has been de-risked by platform investment.

---

## Current Market Analysis

### Market Size

The research report does not cite a precise market size figure for AI video ad creation tools. What is documented: global digital advertising spend exceeded $600B annually by 2024, with social media video advertising representing a fast-growing share. TikTok Shop reached $20B+ US GMV in 2024. The addressable market for the rebuild — SMB sellers needing TikTok-ready product video — is a subset of this, and a precise TAM figure is not available from the research. What is clear is that the buyer pool is orders of magnitude larger than the enterprise delivery platforms Remade was targeting.

## Competition Map and Gaps

The research report names Spyne.ai, PhotoRoom, and Blend as Remade's primary competitors at the time of operation. In 2026, the competitive landscape has evolved:

- **PhotoRoom** has strong mobile distribution and AI background removal, but its core product is still image-focused. Its video capabilities are limited, and it is not purpose-built for TikTok Shop workflows. Its weakness is depth of video generation, not reach.
- **Spyne.ai** has established enterprise relationships in automotive and e-commerce, but targets large catalog operations, not SMB TikTok sellers. Its onboarding and pricing are not SMB-accessible.
- **Canva** and **Adobe Firefly** have absorbed generative image features into their platforms, but neither has a TikTok Shop-native workflow or per-generation pricing that maps to how SMB merchants buy. Their weakness is workflow specificity and pricing model mismatch.
- **CapCut** (ByteDance) is the most dangerous adjacent competitor: it is free, TikTok-native, and has AI features. The rebuild must account for this directly (addressed in GTM).35:T89b,

## Demand Signals from Adjacent Products

DoorDash, Instacart, and Yelp building internal AI photography tools confirms platform-level demand. TikTok Shop's seller growth and the explosion of creator-commerce hybrids signal that the product-to-video workflow is becoming a baseline requirement, not a premium feature.

## Defensibility Analysis

The honest answer is that platform commoditization risk remains real. ByteDance (CapCut/TikTok) could add a product-image-to-video feature to CapCut's seller tools at any time. The structural defense is not technical — it is workflow depth and distribution specificity. A tool embedded in Shopify's App Store with TikTok Shop API integration, trained on e-commerce product data, and priced per generation creates switching costs that a generic CapCut feature does not replicate. The rebuild is not defensible against a determined ByteDance product investment; it is defensible against the neglect that large platforms apply to SMB-specific workflows. That is a real but limited moat, and founders should model an acqui-hire or platform partnership exit as a likely outcome, not a failure scenario.

---

## Recommended MVP

## Core Features

### Product Image → TikTok Video Pipeline (the original wedge, rebuilt)

Upload a product image; the system generates a 9:16, 5–15 second video clip with AI-generated background, motion, and a text overlay hook — optimized for TikTok Shop and Reels. This is Remade's original three-click pipeline, now running on Wan2.1 or CogVideoX at sub-$0.10 inference cost. Unlike the original, it is not a canvas product — there is no freeform editing surface. The output is a finished, exportable video, not a workspace. This differs from the original by being narrower, faster, and priced per output rather than per seat.

## TikTok Shop-Native Export and Listing Integration

Direct export to TikTok Shop's product listing format, with auto-generated caption suggestions and hashtag sets based on product category. This is the distribution hook that Remade lacked — the product lives where the buyer already is, not in a standalone canvas. This feature did not exist in Remade's product and is only possible because TikTok Shop's seller API has matured since 2024.

## Brand-Consistent Product Character Rendering

Using IP-Adapter-based portrait-consistent I2V models (available as of 2025), the system maintains product appearance — color, shape, label — across multiple generated videos without per-product LoRA training. This solves the character consistency problem that was technically immature during Remade's operation and was a documented friction point for enterprise customers. For SMB sellers with multiple SKUs, this is the feature that makes the product usable at catalog scale rather than one-off.

## Effect Library (Squish, Zoom, Hero Run, etc.)

A curated set of cinematic motion effects — directly derived from the Wan2.1 LoRAs that Remade open-sourced and that accumulated 250K+ downloads. These are now freely available, so the rebuild does not own them; the value is in surfacing them through a one-click interface calibrated for product video, not in the model weights themselves.

## What We Will NOT Build

No freeform canvas. No real-time collaboration. No inpainting or 4K upscaling. No enterprise API in the first six months. No desktop application. The canvas product killed Remade's focus; this rebuild does not repeat that mistake.

## Success Metrics

- 500 paying SMB sellers within 90 days of launch (threshold for validating willingness to pay, not just free usage)
- Gross margin per video generation ≥ 60% at scale
- 30-day retention ≥ 40% among paying users
- At least one Shopify App Store or TikTok Shop seller center distribution partnership signed within 6 months

## Cold-Start Problem

This product does not depend on network effects or local density. Each seller generates value independently from their first video. There is no minimum user threshold before the core feature delivers value — a single merchant uploading a product image gets a finished video. The cold-start risk is not density; it is trust (will the output quality be good enough to publish?). The mitigation is a free-tier generation limit (3 videos free, no credit card) that lets merchants validate output quality before paying.

---

## Go-to-Market Strategy

### Target Customer Segment

SMB sellers on TikTok Shop with 1–50 SKUs, monthly GMV of $5K–$100K, who are currently producing video content manually (filming on phone, using CapCut templates) or not at all. This is not the enterprise delivery platform CMO that Remade targeted. It is a merchant who makes buying decisions in minutes, not procurement cycles, and who measures value in sales lift per video, not brand consistency scores.

## Primary Distribution Channel

Shopify App Store (2M+ merchants) and TikTok Shop Seller Center integration. The go-to-market motion is app store listing plus targeted outreach to TikTok Shop seller communities on Reddit (r/TikTokShop), Discord servers for TikTok sellers, and TikTok itself via demo content showing before/after product videos. Secondary channel: affiliate partnerships with TikTok Shop "coaches" and e-commerce educators who already have audiences of SMB sellers.

## Pricing Strategy

Pay-per-generation: $0.99 per finished video, with a bundle of 20 videos for $14.99/month. No seat-based subscription in the MVP phase.

The stress test against free alternatives: CapCut is free and TikTok-native. The rebuild's answer is not that it is better than CapCut for editing — it is that it eliminates the need to film anything. A seller with a product photo and no video equipment cannot use CapCut to produce a product video; they can use this. The free alternative for that use case is hiring a UGC creator ($150–$500 per video) or a production agency. At $0.99 per video, the price-to-alternative ratio is not a hard sell. The $14.99/month bundle is justified for sellers producing 5+ videos per week — a threshold that active TikTok Shop sellers routinely exceed. The risk is that sellers use the free tier (3 videos) and churn; the mitigation is making the bundle the default CTA after the first successful generation.

## Differentiation vs. 2026 Competitors

Against CapCut: no filming required, product-image-native workflow, e-commerce-specific motion effects.
Against PhotoRoom: video output, not image output; TikTok Shop export integration.
Against Canva/Adobe: no design skills required, per-generation pricing, SMB-accessible onboarding in under 2 minutes.
Against Spyne.ai: SMB pricing and self-serve onboarding vs. enterprise sales motion.

The rebuild does not win on breadth. It wins on being the fastest path from a product photo to a published TikTok Shop video, priced so that a seller making $10K/month GMV can justify it on a single incremental sale.
