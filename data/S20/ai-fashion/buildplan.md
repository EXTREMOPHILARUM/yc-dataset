# Build Plan: AI.Fashion 2026

## Overview

AI.Fashion was a Los Angeles-based YC S20 company that built a generative AI platform for fashion brands — converting CAD design files into photorealistic product photography without physical samples or traditional photoshoots — before quietly winding down in 2025 after raising only $3.725M total across nearly five years, having been commoditized by 111 competitors in a category it helped pioneer.

The rebuild thesis is not to re-enter the crowded AI fashion photography market — it is to own the compliance infrastructure layer that sits beneath it. New EU AI Act enforcement, US state-level model consent laws, and SAG-AFTRA-adjacent fashion model union pressure are creating a regulatory forcing function that will make unmanaged AI model imagery legally untenable for enterprise brands by 2026–2027; a rebuilt AI.Fashion wins not by generating better images than Midjourney, but by being the only platform where a brand's legal team will actually sign off on using them.

---

## Why Now?

The single most important change since AI.Fashion's failure is the arrival of enforceable AI model consent regulation — a shift that transforms compliance from a growth-limiting friction (as it was for the original company) into a structural moat.

The EU AI Act entered full enforcement in August 2024, with provisions directly relevant to synthetic likenesses of real people. Tennessee's ELVIS Act (effective July 2024) was the first US state law explicitly protecting individuals' voices and likenesses from unauthorized AI replication; as of early 2025, at least 10 additional US states had introduced comparable legislation. These are not theoretical risks for fashion brands — they are the same legal exposure that forced SAG-AFTRA's 2023 AI provisions into film and television contracts, and fashion model agencies are actively watching the same playbook unfold in their industry. A major brand running an AI campaign built on an unmanaged image generator is now carrying real legal liability, not just reputational risk.

The second critical change is technical. ControlNet (released January 2023) and IP-Adapter techniques now enable precise garment identity preservation across model swaps and pose changes — the core fidelity problem that would have required enormous proprietary model investment in 2020 can now be solved by a small team using open-weight infrastructure. FLUX.1 (Black Forest Labs, August 2024) and Stable Diffusion 3 (Stability AI, mid-2024) produce photorealistic fabric drape and texture at near-zero marginal cost per image.

On the distribution side, Shopify's native AI imagery tools (launched 2023–2024) have validated at scale that fashion brands will adopt AI photography workflows — but Shopify's feature set serves the long tail of small merchants, not the mid-market and enterprise brands managing registered model relationships, multi-regional compliance requirements, and brand-standard audits. That gap is the addressable market.

The global fashion e-commerce market exceeded $700 billion in 2023 (exact AI imagery sub-segment size is not publicly available from a single authoritative source, though analyst estimates for AI creative tools in fashion range from $1–4 billion by 2027 — treat these figures with appropriate skepticism). What is verifiable: 14 funded competitors existed in this category as of February 2024, and none have publicly announced a compliance-layer product as their primary positioning.

---

## Current Market Analysis

**Market size:** The global fashion e-commerce market exceeded $700 billion in 2023. The addressable sub-market — AI-assisted product imagery for fashion brands — does not have a single authoritative size estimate available in public records; analyst projections vary widely and should not be treated as reliable. What is observable is category velocity: 111 active competitors by February 2024, up from near-zero in 2020, indicating rapid perceived opportunity even if total market size is unverified.

## Competition map and gaps:

- **PhotoRoom** (the best-funded direct competitor, with reported $19M+ raised as of 2023): Strong on self-serve background removal and basic AI imagery for small-to-mid merchants; weak on enterprise compliance tooling, model consent management, and CAD-native workflows. Primarily serves the Shopify long tail, not enterprise fashion houses.
- **Botika / Zyler / Veesual**: Mid-market virtual try-on and model swap tools; none have publicly disclosed compliance infrastructure or model consent audit trails. Competing primarily on image quality, not legal defensibility.
- **Adobe Firefly (generative fill for fashion)**: Broad distribution through Creative Cloud (30M+ subscribers), but explicitly a general-purpose tool with no fashion-specific model consent management, no CAD ingestion, and no brand-model registry. Adobe's enterprise customers in fashion are exactly the buyers who need the compliance layer Adobe does not provide.
- **Shopify Magic (AI imagery)**: Validated demand at scale but serves small merchants; no registered model management, no multi-regional compliance, no CAD workflow.
- **Amazon AI product imagery (launched 2023)**: Seller-focused, not brand-focused; no model consent infrastructure.

**Demand signals from adjacent products:** Levi's publicly piloted AI-generated model diversity imagery in 2023. The backlash it received — not for the technology, but for the absence of a clear model consent and compensation framework — is the most important demand signal in this market. It demonstrated that enterprise brands *want* this capability and *will not deploy it at scale* without a defensible compliance wrapper. That is the gap.

**Defensibility analysis:** The honest answer is that Adobe, Shopify, and Amazon could build a compliance layer. The structural reason they probably won't, at least not first: compliance infrastructure for AI model likenesses requires active legal and contractual relationships with modeling agencies, individual models, and regional regulatory bodies — this is not a software feature, it is a network of agreements. Adobe builds tools; it does not manage model consent registries. Shopify serves merchants; it does not negotiate with IMG Models. The rebuilt AI.Fashion's moat is the registry itself — the signed consent agreements, the usage-rights database, the audit trail infrastructure — not the image generation. Platform incumbents can copy the generation layer in weeks; they cannot copy a signed network of model consent agreements without years of relationship-building. This is a real but narrow moat, and it requires moving fast to sign model agencies before a better-funded competitor does. If a well-capitalized player (Adobe, Getty Images, Shutterstock) decides to build this as a strategic priority, the moat collapses. That risk should be stated plainly.

---

## Recommended MVP

### Core Feature 1: Model Consent Registry

A structured database of professional models who have provided explicit, jurisdiction-specific consent for AI likeness use, with defined usage parameters (brand categories, geographic markets, campaign types, duration). This is the foundational layer — without it, every other feature is legally exposed. Unlike the original Persona product, which gated access at the brand level, this registry gates at the model level and generates a machine-readable consent record attached to every image output. This is the feature AI.Fashion was moving toward but never fully built.

## Core Feature 2: CAD-to-Image Pipeline with ControlNet Garment Fidelity

Ingest industry-standard CLO3D and Browzwear file formats (both now widely adopted across mid-to-large fashion brands) and generate photorealistic on-model imagery using FLUX.1 or SD3 with ControlNet garment identity preservation. The key difference from the original: because 3D garment simulation standards (USD, glTF) have matured since 2020, this pipeline can be built in months rather than years, and the output fidelity is substantially higher than what was achievable with 2020-era GAN approaches.

## Core Feature 3: Compliance Audit Trail and Export

Every generated image is tagged with a consent record ID, model identity hash, usage rights scope, and generation timestamp — exportable as a structured report for brand legal teams. This is the feature that converts the product from "AI photography tool" to "enterprise-grade AI photography infrastructure." It directly addresses the gap that caused Levi's and other brands to hesitate on AI model imagery deployment.

## Core Feature 4: Brand Model Persona Management

Brands can register and manage their own contracted models (with those models' signed consent) as persistent personas — enabling consistent model identity across campaigns without re-shooting. This is the Persona product rebuilt with proper consent infrastructure underneath it.

**What you will NOT build:** General-purpose AI image generation for non-fashion use cases. Self-serve consumer or small-merchant tiers. Video generation. Virtual try-on for end consumers (a separate market with different unit economics). Social media content tools.

## Success metrics:

- 10 enterprise fashion brands (>$50M annual revenue) with active paid contracts within 12 months of launch
- Model consent registry with 500+ signed models across at least 3 major modeling agencies within 18 months
- Net revenue retention >110% at 12-month cohort (indicating expansion within accounts)
- Zero material legal complaints related to model consent in the first 24 months of operation

**Cold-start note:** This product does not have a consumer network effect problem — it is B2B enterprise software. The cold-start challenge is the registry: a brand will not pay for a compliance layer if the registry contains 12 models. The go-to-market strategy (see Section 4) must prioritize signing modeling agency partnerships before or concurrent with the first brand sales conversations.

---

## Go-to-Market Strategy

**Target customer segment:** Mid-to-large fashion brands ($50M–$2B annual revenue) with existing model relationships, in-house legal or compliance teams, and active e-commerce operations — specifically those who have already experimented with AI imagery tools and encountered legal or brand-standards friction. Secondary target: the legal and creative operations teams at these brands, not the CMO. The buyer is the person who got nervous about the Levi's backlash, not the person who was excited by the Midjourney demo.

**Primary distribution channel:** Direct enterprise sales, with a deliberate sequencing strategy. Before approaching brands, sign 2–3 major modeling agencies (IMG, Wilhelmina, or equivalents) as registry partners. Agency partnerships serve two functions: they populate the registry with enough models to make the product usable, and they function as a distribution channel — agencies have a direct financial interest in ensuring their models are compensated for AI likeness use, making them motivated co-sellers into the brand accounts they already serve.

**Tactics:** Target the 20–30 brands that publicly piloted AI imagery in 2023–2024 and faced backlash or internal legal pushback (Levi's is the named example; others exist but are not confirmed in public records). These are warm leads — they have already validated the demand internally and already know the compliance problem firsthand.

**Pricing strategy:** Annual SaaS contract, $60,000–$120,000 per brand per year, usage-tiered by image volume and number of registered model personas. This price is justified against the alternative: a single traditional photoshoot for a mid-size fashion brand costs $15,000–$50,000 per day (industry estimates; exact figures vary). A brand running 4–6 shoots per season is spending $60,000–$300,000 annually on photography alone — the SaaS price is a fraction of that, with the compliance infrastructure included.

**Stress-test against free alternatives:** Brands can use Midjourney, Adobe Firefly, or Shopify Magic for free or near-free. The rebuild does not compete on price against these tools — it competes on legal defensibility. A brand's legal team will not approve a Midjourney-generated campaign image for a national ad buy. They will approve an image with a consent record ID, a signed model agreement on file, and a jurisdiction-specific usage rights export. The free alternative is not actually free when the legal review cost, the compliance risk, and the potential litigation exposure are included. If a brand's legal team is not involved in their AI imagery decisions, this product is not for them — and that is fine.

**Differentiation vs. 2026 competitors:** Every current competitor competes on image quality. This rebuild competes on legal infrastructure. The positioning is explicit: "The only AI fashion photography platform your legal team will approve." That is a narrow claim, but it is a defensible one — and it is the claim that no current competitor is making, because none of them have built the model consent registry that would allow them to make it honestly.
