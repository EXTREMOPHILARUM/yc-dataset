# Build Plan: Tech in Asia 2026

## Overview

Tech in Asia launched in 2010 as a student blog called Penn Olson, grew into the dominant English-language technology media brand for Southeast Asia across news, data, events, and recruitment, raised approximately $13 million from investors including SoftBank and Eduardo Saverin, and sold to legacy print incumbent SPH Media in January 2024 for a reported $30 million — a technically positive but modest outcome after thirteen years that reflected a structural mismatch between a media business model and venture capital return expectations.

The rebuild thesis is not to repeat the pivot treadmill. The original company proved that a paying audience exists for premium Southeast Asian tech intelligence; it simply priced that audience wrong, served it with the wrong product mix, and raised capital that forced it to chase scale it could never reach. The new version is a bootstrapped or lightly funded B2B intelligence platform — think Rhodium Group meets The Information, built for institutional investors and corporate strategists operating in Southeast Asia — that uses AI-assisted data infrastructure to deliver what Techlist never could, at a price point ($2,000–$5,000/seat/year) that makes the unit economics work with 300 subscribers instead of 3,500.

---

## Why Now?

### The single most important change since the original failure is the collapse in the cost of structured data collection across Asian markets.

Techlist's core problem was not product design — it was data economics. Asian founders refused to share company information openly, which meant every record in the database required expensive manual research. At $399/seat/month, the product needed to justify CB Insights-level data completeness it could not afford to build. That unit economics trap is now structurally different.

LLM-powered extraction pipelines — built on models like GPT-4 (March 2023) and its successors — can reconstruct a comprehensive Southeast Asian startup database from public sources: LinkedIn company pages, MAS and OJK regulatory filings, Google Play and App Store rankings, job board postings, government grant databases (Enterprise Singapore, MDEC), and local-language news sources. What required a team of manual researchers in 2015 can now be approximated by a small engineering team running structured extraction at scale. The cold-start data problem that made Techlist's unit economics unworkable is no longer the same problem.

The second critical change is payment infrastructure. Tech in Asia's 2014 subscription attempt failed explicitly because of "painful payment processes" in Southeast Asia. Stripe's full regional rollout — Singapore (2018), Malaysia, Thailand, and the Philippines (by 2022) — combined with the maturation of regional rails including GrabPay, GoPay, and PayNow, means a B2B subscription can be activated from day one without custom payment infrastructure.

The third change is the maturation of the addressable market itself. When Techlist launched in 2015, Southeast Asia's institutional investor base was thin. Today, Grab, Sea Group, GoTo, and Bukalapak have all completed public listings, creating a documented class of institutional investors, sell-side analysts, and corporate strategists who need systematic regional intelligence. The Monetary Authority of Singapore reported that assets under management in Singapore reached S$5.4 trillion in 2022 (MAS Annual Report 2023) — a meaningful portion of which is allocated to or tracking Southeast Asian technology. The paying audience is now provably large in a way it was not in 2015. Exact data on the subset specifically seeking Southeast Asian tech intelligence is not available, but the directional signal is clear.

Distribution channels available now that did not exist at scale in 2015 include LinkedIn Sales Navigator for direct outreach to fund analysts and corporate strategy teams, and Substack's network for building an initial free readership before converting to institutional tiers.

---

## Current Market Analysis

**Market size today vs. 2015:** The global B2B intelligence and market research market was valued at approximately $33 billion in 2023 (Grand View Research, 2024), growing at roughly 11% annually. The specific sub-segment — institutional-grade intelligence on Southeast Asian technology — has no clean market size estimate available. What is documentable: Singapore's AUM of S$5.4 trillion (MAS, 2023), a growing regional PE and VC base, and the post-IPO analyst coverage requirements for Grab, Sea Group, and GoTo all point to a materially larger institutional audience than existed when Techlist launched. The original Tech in Asia operated in a market where the institutional investor base for Southeast Asian tech was nascent; that base is now established.

## Competition map and gaps:

- **DealStreetAsia** (Reuters-backed): Strong on deal flow and M&A coverage, weak on startup-layer data and founder-facing content. Pricing is not publicly disclosed but is understood to be institutional. Its Reuters parentage gives it distribution but limits editorial agility.
- **KrASIA** (Caixin-backed): Strong China-Southeast Asia bridge coverage, weaker on pure Southeast Asian startup intelligence, and carries implicit editorial constraints from its Chinese institutional backer that limit coverage of sensitive topics.
- **Momentum Works**: Produces high-quality Southeast Asian tech research reports, but operates as a consulting firm rather than a subscription intelligence product. No continuous data layer.
- **CB Insights / PitchBook / Crunchbase**: Global coverage with improving Asian data, but Southeast Asia remains a secondary market for all three. Coverage of Series A and earlier rounds in Indonesia, Vietnam, and the Philippines is materially incomplete. These platforms charge $15,000–$50,000+/year for enterprise seats, creating a price gap for a regional specialist at $2,000–$5,000/year.
- **Tech in Asia (post-SPH)**: Now operating inside a legacy print media conglomerate. SPH's strategic rationale was content bolt-on for The Business Times, not independent scaling. Editorial agility and startup-community credibility are likely degrading under corporate ownership. This is the most important competitive gap: the brand that owned this space is now institutionally constrained.

**Demand signals from adjacent products:** The Information's success at $399/month for technology journalism, Rhodium Group's institutional pricing for China intelligence, and Caixin's tiered subscription model all validate that a narrow, expert audience will pay premium prices for regional intelligence they cannot get elsewhere.

**Defensibility against platform incumbents:** Bloomberg and Reuters could theoretically expand Southeast Asian tech coverage. The structural defense is not technology — it is editorial trust and community embeddedness. Bloomberg covers markets; it does not cover the Series A round in a Jakarta fintech startup or the regulatory shift affecting Vietnamese e-commerce. The rebuild's defensibility comes from the same source as the original's: on-the-ground sourcing relationships that global platforms cannot replicate cost-effectively for a market this size. This is a real but not impregnable moat. If Southeast Asian tech becomes a top-five global investment theme, Bloomberg will invest. The window is real but time-bounded.

---

## Recommended MVP

### Core Feature 1: The Intelligence Brief

A daily or three-times-weekly email brief covering funding rounds, regulatory developments, and market moves across Singapore, Indonesia, Vietnam, Thailand, and the Philippines — written for institutional readers, not general tech enthusiasts. Each brief is 600–900 words, sourced from original reporting and AI-assisted monitoring of regulatory filings, job postings, and local-language sources. This differs from the original Tech in Asia in that it is explicitly B2B-priced from day one, not a free editorial product seeking advertising revenue. It differs from DealStreetAsia in editorial voice: analyst-grade framing, not news wire framing.

## Core Feature 2: The Southeast Asia Startup Database (AI-Assisted)

A continuously updated database of funded startups across the five core markets, drawing from public sources — regulatory filings, app store rankings, LinkedIn, job boards, and local news — processed through structured LLM extraction pipelines. Coverage targets Series A and later, with best-effort coverage of seed rounds where public data exists. This directly addresses Techlist's failure: the data is not dependent on founder self-reporting, eliminating the cultural barrier that killed the original. The database is not positioned as a competitor to PitchBook on data completeness — it is positioned as the most current and accurate source for Southeast Asian companies that PitchBook undercounts.

## Core Feature 3: Institutional Tier with Analyst Access

At the $5,000/seat/year tier, subscribers receive quarterly analyst calls, custom data pulls, and the ability to submit research questions answered within 48 hours. This is the product that Rhodium Group and Trivium China sell to institutional investors covering China — applied to Southeast Asia. It converts the editorial team from a cost center into a revenue-generating research function and creates switching costs that a pure media subscription does not.

**What we will NOT build:** Events infrastructure, a recruitment product, a marketing agency, a community platform, or any product requiring significant headcount to deliver. No advertising sales team. No open data marketplace. These were the pivots that consumed Tech in Asia's capital without producing scalable returns.

## Success metrics with concrete thresholds:

- 150 paid subscribers at an average of $2,500/year = $375K ARR within 12 months of launch
- 400 paid subscribers at an average of $3,000/year = $1.2M ARR within 24 months
- Gross margin above 70% (achievable with a lean editorial team of 4–6 and AI-assisted data infrastructure)
- No single subscriber accounting for more than 10% of ARR

**Cold-start note:** This product does not depend on network effects or local density. A single subscriber in London covering Southeast Asian venture capital receives full value on day one. The cold-start problem is a data quality problem, not a user density problem — addressed by the AI-assisted database approach described above.

---

## Go-to-Market Strategy

**Target customer segment:** Institutional investors with Southeast Asian exposure — specifically, analysts and portfolio managers at Asia-focused venture funds, family offices with regional allocations, and corporate strategy teams at companies with Southeast Asian operations or M&A mandates. Secondary segment: sell-side analysts at banks covering Grab, Sea Group, GoTo, and regional fintech. This is a narrower target than Tech in Asia's original "anyone interested in Asian tech" framing, and that narrowness is the point. These buyers have budget authority, clear ROI framing (intelligence that informs investment decisions), and no adequate free substitute.

**Primary distribution channel and tactics:** Direct outreach via LinkedIn Sales Navigator to fund analysts and corporate strategy leads at firms with documented Southeast Asian exposure. Complement with a free weekly brief distributed via Substack or Beehiiv to build a top-of-funnel readership of 5,000–10,000 before the institutional paywall converts. Conference presence at SuperReturn Asia and Milken Institute Asia Summit — not as an events organizer, but as a media partner with a booth and sponsored research distribution. Target 20 institutional trial conversions in the first six months through direct outreach before relying on inbound.

**Pricing strategy:** $2,000/year (Basic: database access + brief archive), $5,000/year (Institutional: adds analyst access and custom pulls). Free tier: weekly brief, no database access, no archive.

The stress test against free alternatives: The free alternative for this audience is a combination of Google Alerts, LinkedIn, Crunchbase's free tier, and occasional TechCrunch coverage. That combination is meaningfully worse — it misses local-language sources, undercounts Southeast Asian rounds, and provides no analyst interpretation. The question is whether the delta is worth $2,000–$5,000/year to an institutional buyer. For a fund analyst whose firm manages $200M+ in Southeast Asian exposure, a $5,000 intelligence subscription is a rounding error on the research budget. The price is justified by the buyer profile, not by the product's superiority to free alternatives for a general reader. This is why the target segment must stay narrow: the same product is not worth $2,000/year to a startup founder or a journalist.

**Differentiation vs. 2026 competitors:** Against DealStreetAsia — faster, more founder-proximate, cheaper. Against CB Insights/PitchBook — deeper Southeast Asian coverage at a fraction of the enterprise price. Against Tech in Asia post-SPH — editorially independent, institutionally priced, not constrained by a legacy print parent's editorial priorities. The rebuild's core claim is simple: it is the only product built specifically for institutional buyers who need Southeast Asian tech intelligence and are currently underserved by global platforms and over-served by general tech media.
