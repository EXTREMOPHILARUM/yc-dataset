# Build Plan: Queenly 2026

## Overview

Queenly was a San Francisco-based peer-to-peer formalwear resale marketplace founded in 2019 by Trisha Bantigue and Kathy Zhou-Patel, backed by Andreessen Horowitz with $7.1M in total funding, that shut down in late 2024 after burning approximately $273,000 per month against just $200,799 in annual revenue — a gap that made Series A fundraising structurally impossible regardless of its genuine product-market fit, 1 million users, and 2% return rate.

The rebuild thesis is not that the market changed — it is that the cost structure can. What killed Queenly was a 13–19 person team hand-building infrastructure that is now off-the-shelf: visual search, AR try-on, generative listing tools, and analytics. A 2026 rebuild runs the same product with 3 engineers, a 35% take rate on authenticated high-value gowns, and a subscription tier for pageant contestants — turning a business that needed 100,000 annual transactions to break even into one that can survive on 8,000.

---

## Why Now?

### The single most important change since Queenly's failure is that its entire technology stack is now commodity infrastructure.

Queenly's CTO Kathy Zhou-Patel built the iOS app, Android app, web platform, ML search engine, computer vision layer, AR try-on tool, and generative AI listing system largely herself — and then spent additional senior engineering time building analytics infrastructure in-house. In 2026, every one of those components can be sourced, assembled, or fine-tuned from existing APIs and platforms at a fraction of the original cost.

Specifically: GPT-4o (May 2024) and Claude 3.5 Sonnet (June 2024) can generate structured, SEO-optimized formalwear listings from a single photo with near-zero marginal cost. Queenly's own data showed that its generative AI integration raised listing completion rates from 60% to 85% and cut time-to-listing by 50% — a rebuild deploys this capability on day one without a custom engineering build. Google Vision API and AWS Rekognition now support fine-tuned visual classification for silhouette, neckline, embellishment, and color at commodity pricing. Apple's ARKit and Snap's Camera Kit (post-Vertebrae acquisition, 2021) offer plug-and-play AR try-on SDKs that eliminate the need for the proprietary AR system Queenly patented. Amplitude and Mixpanel handle analytics at $0–$1,000/month, eliminating the in-house build that consumed a senior engineer's full attention.

The market tailwind is also materially stronger. The secondhand apparel market grew from $28 billion in 2021 to a projected $82 billion by 2026, per ThredUp's 2024 Resale Report — a 193% increase in the period since Queenly raised its seed. Consumer willingness to buy pre-owned formalwear, which Queenly had to actively overcome in 2019, is now normalized by ThredUp, Depop, and Vestiaire Collective. The cultural friction is lower; the infrastructure cost is lower; the market is larger. The original failure was an engineering and burn-rate problem, not a demand problem.

Distribution channels unavailable at Queenly's founding now include TikTok Shop (launched US, 2023) with direct in-app purchasing, and Pinterest's shoppable pins with visual search integration — both highly indexed toward the formalwear buyer demographic.

---

## Current Market Analysis

### Market Size

The North American formalwear market was cited at $15 billion at the time of Queenly's a16z raise, with prom alone representing a $4 billion annual market. These figures are industry estimates, not audited data, and no updated vertical-specific figure for formalwear resale is available in the public record as of early 2026. However, the broader secondhand apparel market's growth from $28B (2021) to a projected $82B (2026) per ThredUp provides a directional signal that the resale subset of formalwear has grown meaningfully. The specific TAM for formalwear resale should be modeled conservatively at 5–8% of the primary formalwear market — approximately $750M–$1.2B annually in North America — until better data is available. Do not use the $15B primary market figure as a proxy for resale opportunity.

## Competition Map

*Poshmark* (acquired by Naver, 2023): 80M+ registered users, dominant in general apparel resale. Core weakness: no formalwear-specific search, sizing, or occasion filtering. A size-6 red ball gown search returns inconsistently tagged results across dozens of subcategories. Poshmark has not invested in vertical-specific tooling for formalwear as of early 2026.

*ThredUp*: Focuses on everyday apparel, not occasion-specific formalwear. Consignment model with long processing times (2–4 weeks) is structurally incompatible with time-sensitive formalwear purchases (prom in 3 weeks, pageant next month).

*Vestiaire Collective*: Luxury resale, authentication-focused, average price point well above the $200 formalwear AOV. Does not serve the prom or pageant segment.

*Facebook Marketplace / Depop*: Zero vertical infrastructure, no trust layer, no size-specific search. Serve as the fragmented status quo that a vertical platform can outcompete on buyer experience.

*StockX*: Sneakers and streetwear. No formalwear presence.

**The gap is clear**: no current competitor offers formalwear-specific visual search, occasion-based filtering, size-range matching, or an authentication tier for gowns above $300. The category remains fragmented across general platforms.

## Defensibility Against Platform Incumbents

This is the honest answer: Poshmark or eBay *could* build formalwear-specific category pages and filters. They have not, despite Queenly operating for five years and demonstrating demand. The structural reason is that formalwear is high-AOV, low-frequency, and requires domain-specific curation investment that does not move the needle for a platform with 80M+ users across all categories. A rebuild is defensible not because incumbents *can't* copy it, but because the category is too small to prioritize at their scale — the same logic that has kept vertical marketplaces like 1stDibs (furniture), Reverb (instruments), and Whatnot (collectibles) alive alongside eBay. If the rebuild reaches $20M+ GMV in the formalwear vertical, it becomes an acquisition target before it becomes a competitive threat.

## Demand Signals

Depop's formalwear listings consistently rank among its highest-engagement categories. TikTok's #promdress hashtag has accumulated billions of views. These are demand signals the research report does not quantify precisely, but they are directionally consistent with Queenly's own 100,000+ daily website visitors at launch.

---

## Recommended MVP

## Core Features

### AI-Powered Listing in Under 2 Minutes

Sellers photograph their dress (3–5 photos); GPT-4o generates a structured listing including style category, silhouette, embellishment detail, condition grade, and SEO-optimized description. The seller confirms or edits, then publishes. This directly replicates Queenly's proven result — 85% listing completion, 50% reduction in time-to-listing — but deploys it from day one using off-the-shelf LLM APIs rather than a custom engineering build. Unlike Queenly's implementation, which required dedicated engineering effort to build, this version costs approximately $0.02–$0.05 per listing in API fees.

## Occasion-Specific Visual Search

Fine-tuned computer vision (Google Vision API or AWS Rekognition, with a formalwear-specific training layer) enables search by silhouette, neckline, color family, embellishment type, and size range — not keyword tags. This is the core buyer-side differentiator that Queenly built in-house at significant cost; a rebuild achieves equivalent functionality using foundation model fine-tuning at a fraction of the original engineering investment. The key difference from the original: no custom ML infrastructure to maintain.

## Tiered Authentication for Gowns Above $300

Sellers of gowns priced above $300 submit a structured photo set (front, back, label, condition details) reviewed by a contracted authenticator — not a full QA warehouse operation. Authentication is outsourced to a per-item contract model (estimated $8–$15 per item, not a disclosed figure) rather than Queenly's in-house QA operation, which required physical handling infrastructure. Buyers of authenticated gowns receive a condition guarantee. This tier supports a 35% take rate (vs. Queenly's implied 20%), justified by the trust premium. Gowns below $300 remain peer-to-peer with photo verification only, at a 20% take rate.

## Pageant Contestant Subscription ($19.99/month)

Recurring revenue for the highest-frequency buyer segment: pageant contestants who need unique gowns for multiple competitions per year. Subscribers receive priority search placement for their listings, early access to new inventory, and a reduced take rate of 15% on sales. This directly addresses Queenly's fatal flaw — near-zero transaction frequency per user — by converting the highest-LTV segment to a recurring revenue model before the first transaction.

## What We Will NOT Build

No proprietary AR try-on (use Snap Camera Kit SDK if try-on is added post-MVP). No in-house analytics infrastructure (Amplitude from day one). No acquisition of adjacent marketplaces (no Mi Padrino equivalent). No Canada or international expansion in year one. No boutique or designer channel until peer-to-peer GMV exceeds $500K/month.

## Success Metrics

- 500 active listings within 60 days of launch in the first target market
- Listing completion rate ≥ 80% (Queenly's post-AI benchmark)
- 50 completed transactions in month 3
- Subscription conversion rate ≥ 5% of registered pageant-identified users by month 6
- Monthly burn rate ≤ $30,000 (3-person team, no warehouse)

## Cold-Start Problem

The core feature — visual search across a deep formalwear inventory — requires approximately 2,000–3,000 active listings in a single category (e.g., pageant gowns, size 0–12) before search results feel meaningfully better than Poshmark. The path to that threshold: launch exclusively at 3–5 regional pageant circuits (Miss Teen USA state competitions, Miss America preliminaries) where contestants are concentrated, self-identified, and have immediate resale supply. Queenly reached 50,000 listings before public launch by seeding supply through the pageant community — the rebuild replicates this by partnering with pageant coaches and state directors as supply-side ambassadors before the app is publicly listed.

---

## Go-to-Market Strategy

### Target Customer Segment

Primary: Active pageant contestants in the United States, specifically women competing in Miss America Organization, Miss USA, and Miss Teen USA state-level circuits. This segment has the highest purchase frequency in the formalwear category (multiple gowns per competition season), the strongest peer network for word-of-mouth distribution, and a documented cultural norm of wearing unique, non-repeated dresses. Queenly's a16z lead Connie Chan identified this segment explicitly as "a really great wedge." The rebuild uses the same wedge, but does not expand beyond it until the core unit economics are proven.

Secondary (year 2): Prom buyers in the top 10 US markets by high school enrollment density.

## Primary Distribution Channel

Direct community partnerships with pageant coaches, state directors, and titleholder networks — not paid acquisition. Pageant coaches manage 10–50 contestants each and are trusted advisors on dress sourcing. A referral program offering coaches 2% of GMV generated by their referred contestants costs less than $5 CPL at the expected AOV, compared to estimated $15–$40 CAC on paid social for general apparel resale (industry estimate; Queenly-specific CAC not disclosed). Secondary channel: TikTok organic content featuring before/after listing transformations using the AI listing tool, targeting #pageantlife and #promdress communities.

## Pricing Strategy

- Peer-to-peer listings (under $300): 20% take rate. Stress test: Poshmark charges 20% on items over $15 with no formalwear-specific features. The rebuild's visual search and occasion filtering justify equivalent pricing with a better buyer experience.
- Authenticated gowns (over $300): 35% take rate. Stress test: Vestiaire Collective charges 25–38% with full authentication on luxury items. A 35% rate on a $600 pageant gown ($210 platform revenue) is defensible if authentication reduces buyer hesitation on high-value purchases — Queenly's 2% return rate suggests it does.
- Pageant Subscription ($19.99/month): Stress test against free alternatives — a contestant currently manages resale via Facebook groups and Poshmark at zero subscription cost. The $19.99 is justified only if the subscriber saves meaningfully on take rates (15% vs. 20% on a $400 gown saves $20 per transaction) and gets faster inventory access. At one sale per month, the subscription pays for itself. If a contestant sells fewer than one gown per month, the subscription does not pencil — which is why it should be positioned as a seasonal offering (3-month competition season pass at $49.99) rather than a perpetual monthly charge.

## Differentiation vs. 2026 Competitors

The rebuild's differentiation is not technology — visual search and AI listings are table-stakes by 2026. The differentiation is community density: a platform where every listing is a formalwear item, every buyer has a specific occasion in mind, and every search result is relevant. Poshmark will never prioritize this. ThredUp's consignment timeline is incompatible with pageant season urgency. The rebuild wins not by being more technologically sophisticated than incumbents, but by being the only place where a contestant can find 3,000 pageant gowns in her size, authenticated, with a 48-hour shipping guarantee — and sell her last competition dress to someone exactly like her.
