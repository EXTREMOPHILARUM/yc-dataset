# Build Plan: Goodybag 2026

## Overview

The 2026 Goodybag targets mid-market ops teams (100–500 employees) who are exhausted by ezCater's pricing and clunky UX. It's a lightweight, AI-native catering marketplace that makes booking restaurant catering as frictionless as ordering lunch — no manual menu uploads, no enterprise sales cycles, just search-compare-book in under five minutes. The product lives where ops managers already work: Slack, email, calendar integrations.

The market shift is simple: ezCater proved the category works at scale, but proved equally that customers hate paying 25–35% markups on top of restaurant prices. There's now a clear opening for a modern, transparent alternative that undercuts on cost while overdelivering on speed and UX. AI handles the operational complexity that killed the original Goodybag — automatic menu parsing, dietary filtering, logistics coordination — so the unit economics work without needing massive sales teams.

Go-to-market is bottoms-up: land ops managers at 50–100 tech and professional services companies in major metros, build word-of-mouth through Slack communities and LinkedIn, then expand to finance and healthcare verticals once the playbook is proven. Win on speed, transparency, and the fact that you're not a legacy enterprise vendor.34:T7d4,

## Why Now?

The single most important change since Goodybag's 2016 exit is the empirical validation of the market itself. ezCater — Goodybag's best-funded competitor at the time — reached a $1.6 billion valuation in 2019 and processed over $1 billion in annual gross merchandise volume by 2022. The demand Goodybag assumed existed is now proven at scale. More importantly, the consolidation wave that made independent survival untenable for Goodybag has since reversed: Waitr, which acquired Bite Squad (which acquired Goodybag), filed for bankruptcy in 2023. The enterprise catering segment is now underserved by the surviving national platforms, creating a genuine re-entry window.

Three infrastructure changes make the rebuild materially cheaper and faster than the original:

**LLM-based menu ingestion** is the most operationally significant. GPT-4 (March 2023) and Claude 3 (March 2024) can now parse restaurant menus from PDFs, websites, and images with high accuracy and minimal human review. In 2016, manual menu onboarding was a key cost driver for supply acquisition. That cost is now close to zero-marginal.

**Stripe Connect**, now mature and widely adopted, makes marketplace payment splitting, automated restaurant payouts, and take-rate collection nearly zero-marginal-cost to implement. In 2016, this required significant custom engineering that consumed runway.

**Modern B2B sales tooling** — HubSpot, Apollo.io, Outreach — has reduced enterprise customer acquisition costs dramatically. Goodybag's estimated $100,000 per-market launch cost could realistically be cut by 40–60% today (exact figure unknown, but directionally supported by the research).

Finally, hybrid work has created a structurally new use case: companies now need to cater distributed team events, off-site meetings, and return-to-office incentive meals across multiple locations simultaneously. This multi-location catering workflow did not exist at scale in 2016 and remains underserved by current platforms.

---

## Current Market Analysis

**Market Size:** Goodybag cited a $30 billion U.S. corporate catering TAM in 2016. The current figure is not independently verified in available sources, but the category has expanded meaningfully — hybrid work has increased demand for catered off-sites, team events, and return-to-office programming. ezCater's $1B+ GMV by 2022 represents a single platform's slice; the broader market is substantially larger.

## Competition Map:

- **ezCater** is the dominant incumbent, with national coverage and deep enterprise integrations. Its weakness is pricing: enterprise buyers report high take rates (estimated 15–20% per industry commentary, though exact figures are not publicly confirmed) and a vendor catalog that skews toward large chain caterers over local restaurants. It also has limited capability for multi-location, same-day distributed orders.

- **Cater2.me and ZeroCater** have narrowed their focus to managed meal programs (recurring office lunches) rather than event-driven catering. They serve a different use case and are not direct competitors for the ad-hoc enterprise catering workflow.

- **DoorDash for Business and Uber Eats for Business** have added group ordering features but remain structurally optimized for individual consumer delivery. Their average order economics, driver networks, and product interfaces are not designed for 50-person catered events with advance scheduling requirements.

- **The gap:** No current platform is purpose-built for the multi-location, hybrid-workforce catering workflow — a company ordering catering for simultaneous team lunches in Austin, Seattle, and Nashville on the same day. This is the specific demand signal that adjacent products (corporate travel platforms, event management tools like Cvent) are beginning to surface but not yet fulfilling.

---

## Recommended MVP

### Core Features:

**1. AI-Powered Restaurant Onboarding.** Using GPT-4-class LLM parsing, the platform automatically ingests restaurant catering menus from PDFs, websites, and images, structures them into a standardized catalog, and flags items for human review only when confidence is low. This directly eliminates the manual onboarding labor that constrained Goodybag's supply acquisition speed. Unlike the original, supply-side scaling is no longer gated by headcount.

**2. Multi-Location Order Coordination.** A single order interface allows a corporate buyer to place catering orders across multiple cities simultaneously — selecting local vendors in each market, setting per-location budgets, and receiving consolidated invoicing. This is the feature that did not exist in Goodybag's original product and is the primary unmet need created by hybrid work. It is not available in ezCater's current interface at this level of workflow integration (based on publicly available product documentation).

**3. Corporate Expense and Procurement Integration.** Native integrations with Concur, Coupa, and Bill.com for PO-based purchasing, consolidated invoicing, and spend reporting. Enterprise procurement teams now expect this as table stakes; it was an afterthought in 2016. This feature directly addresses the sales objection that blocked Goodybag from moving upmarket to larger enterprise accounts.

**4. Reorder and Vendor Relationship Management.** A lightweight CRM layer for the office manager — saved vendor preferences, dietary restriction profiles by team, one-click reorder from past events, and delivery reliability scores by vendor. This builds the switching cost that produced Goodybag's 93% retention and makes it structurally harder for ezCater to poach accounts.

**What we will NOT build:** delivery infrastructure, consumer-facing ordering, a managed meal subscription product, or a restaurant-side POS integration. No drivers, no recurring meal programs, no B2C surface.

**Success Metrics:** 85%+ customer retention at 6 months; $400+ average order value (inflation-adjusted from Goodybag's $350); 3+ orders per active account per month; first market profitable within 5 months of launch.

---

## Go-to-Market Strategy

**Target Customer:** Operations managers and executive assistants at technology and professional services companies with 100–500 employees, operating across 2+ office locations, in markets where Waitr/Bite Squad's bankruptcy has left a supply vacuum. Initial focus: Austin and Nashville, Goodybag's two strongest original markets, where local restaurant relationships and brand memory may still carry residual value.

**Primary Distribution Channel:** Direct outbound via Apollo.io-enriched lists of office managers and EAs at target companies, sequenced through Outreach. Secondary channel: LinkedIn Sales Navigator targeting "Office Manager," "Executive Assistant," and "Workplace Experience" titles at companies with 100–500 employees and multi-city footprints. Tertiary: partnerships with commercial real estate operators (WeWork, Industrious, local coworking networks) who have direct relationships with the exact buyer persona and a structural incentive to offer catering as an amenity.

**Pricing:** Transaction fee model at 12–13% of gross order value, consistent with Goodybag's original SXSW 2015 pricing. No monthly subscription for the base tier. An enterprise tier at $299/month unlocks multi-location coordination, procurement integrations, and dedicated account support — justified by the vertical SaaS pricing norms that enterprise food/hospitality buyers now understand and accept, reducing the sales education burden Goodybag faced in 2016. Restaurants pay no onboarding fee, preserving the supply-side flywheel.

**Differentiation vs. 2026 Competitors:** Against ezCater — lower take rate, local restaurant depth, and the only platform with a native multi-location hybrid-work workflow. Against DoorDash/Uber for Business — purpose-built for advance-scheduled, high-value catering rather than on-demand individual delivery. The positioning is explicit: "Built for the way your team actually works now, not the way offices worked in 2016."
