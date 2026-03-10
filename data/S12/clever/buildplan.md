# Build Plan: Clever 2026

## Overview

By 2026, Clever 2.0 is a district-first data integration and analytics platform for mid-market K-12 systems (10–50 schools) in the UK and North America. It's built for IT directors who need real-time visibility into which edtech tools are actually being used—and by whom—without the integration headaches that plagued the original Clever. The insight: LLM-assisted SIS parsing has collapsed the technical moat that once required years of hand-coded integrations. What took Clever's engineers months now takes hours.

The rebuild wins on speed and insight, not just plumbing. Instead of positioning as "the SSO layer," it leads with a district-pays analytics dashboard that shows usage patterns, teacher adoption, and student engagement across the entire edtech stack. That visibility is what districts will pay for. SSO and AI-powered app recommendations are table stakes—the analytics layer is the revenue engine.

Go-to-market targets IT directors at mid-market multi-academy trusts in the UK first, where fragmentation is acute and budget cycles are predictable. Free tier for adoption, premium tier for analytics depth. The original Clever owned the infrastructure but couldn't monetize it. This version owns the insight.33:Ta0d,

## Why Now?

## The single most important change: LLM-assisted SIS integration has collapsed the cost of Clever's core technical moat.

## Current Market Analysis

**Market size today vs. 2012:** The US K-12 edtech software market was approximately $8.38B in 2023 and is projected to reach $32B globally by 2030, per Grand View Research — though these figures should be treated as directional rather than precise. In 2012, the comparable US market was a fraction of that size. The international K-12 edtech market (UK, EU, Australia) is large but specific infrastructure-layer market sizing is not available in public sources.

## Competition map:

- **Clever (Kahoot!-owned):** The incumbent in US K-12 SSO/API infrastructure, now operating as a subsidiary. Its weakness is strategic drift — Kahoot!'s core business is game-based learning content, and Clever's infrastructure mission is not Kahoot!'s primary focus. Post-acquisition integrations have reportedly been slow (specific performance data not publicly available), and Clever's product roadmap is now subordinated to a Norwegian entertainment company's priorities. This is a classic acqui-hire risk: the infrastructure layer gets maintained but not meaningfully advanced.

- **ClassLink:** The primary US SSO competitor, with meaningful penetration in districts that chose not to adopt Clever. ClassLink's weakness is that it competes on the same free-to-districts model without Clever's developer ecosystem density — a smaller network effect with no obvious path to differentiation.

- **PowerSchool:** The vertically integrated incumbent that EdSurge analysts identified as the more financially successful model. PowerSchool (IPO 2021, ~$3.5B market cap at IPO) bundles SIS + SSO + analytics + curriculum management and charges districts directly. Its weakness is lock-in resentment: districts that feel trapped in PowerSchool's bundle are actively seeking alternatives, particularly for analytics and AI features that PowerSchool has been slow to develop.

- **Wonde (UK):** The closest international analog to Clever, with UK SIS integrations but limited EU and Australia presence. No public penetration figures available.

**Demand signals from adjacent products:** The growth of AI tutoring platforms (Khanmigo, Synthesis, Century Tech) and the proliferation of LMS integrations (Canvas, Schoology, Google Classroom) all generate demand for the same underlying infrastructure — roster data, SSO, and usage analytics — that Clever provides.

**Defensibility analysis:** The rebuild's primary defensibility concern is PowerSchool, not Google or Microsoft. Google Classroom and Microsoft Teams for Education have adjacent SSO capabilities but have historically declined to own SIS integration complexity — a pattern that held throughout Clever's entire independent life and shows no signs of reversing. The structural reason is that SIS integration is a low-margin, high-support, district-by-district negotiation problem that platform giants do not want to own. PowerSchool is the genuine threat: it already owns the district budget relationship and could bundle a Clever-equivalent as a zero-marginal-cost add-on. The rebuild's defense against this is (a) international markets where PowerSchool has limited presence, and (b) AI-native analytics features that PowerSchool has been slow to develop. This is a real risk, not a solved problem, and founders should enter with clear eyes about it.

---

## Recommended MVP

## Core Feature 1: LLM-Assisted SIS Integration Builder

A toolchain that uses GPT-4-class models to parse a new district's SIS data export, map it to a standard schema, and generate a working integration in days rather than months. This directly addresses the core technical moat that made Clever hard to replicate — and makes it possible to enter international markets (UK, EU, Australia) where Clever never built its integration library. Unlike Clever's hand-coded integrations, this system improves with each new SIS encountered, compounding the speed advantage over time.

## Core Feature 2: District-Pays Analytics Dashboard

A real-time usage analytics layer that shows district administrators which edtech tools are being used, by which students, at what frequency — and flags underutilized licenses. This is the product Clever attempted and discontinued. The difference in 2026 is that (a) districts now have dedicated edtech budget line items and demonstrated willingness to pay for ROI visibility, and (b) LLM-powered natural language querying makes the analytics accessible to non-technical administrators without a BI team. Priced as a district-pays subscription, this is the monetization surface Clever never successfully captured.

## Core Feature 3: SSO Portal with AI-Powered App Recommendations

A standard SSO portal (table stakes for district adoption) augmented with an AI layer that recommends relevant apps to teachers based on their curriculum, grade level, and peer usage patterns. This creates a new value surface for developers — not just access to districts, but qualified discovery — and justifies a higher developer-side fee than Clever's $5–$25/school/month ceiling.

**What we will NOT build:** A content or curriculum layer, a learning management system, or any product that competes with the edtech developers who are our paying customers. The neutral intermediary position is the asset; abandoning it to become a content company is the Kahoot! mistake.

**Success metrics:** 500 schools in a single international market (UK preferred) within 12 months of launch; 20% of connected districts paying for the analytics tier within 18 months; developer NPS above 50.

**Cold-start problem:** The SSO portal requires a minimum of 3–5 integrated apps to feel useful to a district. The go-to-market strategy (see below) seeds this by pre-integrating the 20 most widely used edtech tools in the target market before approaching the first district. Unlike a social network, the core SSO value (eliminating password friction) delivers immediately for a single user — the cold-start threshold is low on the district side. The analytics dashboard requires at least 6 months of usage data before it generates meaningful insights; this should be disclosed to districts at onboarding.

---

## Go-to-Market Strategy

**Target customer segment:** District IT Directors and Directors of Technology in UK local authority multi-academy trusts (MATs) with 10–50 schools. MATs are the structural equivalent of US school districts — centralized IT decision-making, shared procurement, and a single administrator who feels the SIS integration pain across multiple schools simultaneously. The UK is the priority market because Wonde has demonstrated that the Clever model is viable there without achieving dominant penetration, English-language sales removes localization friction, and GDPR compliance (required in the UK) becomes a competitive differentiator in subsequent EU expansion.

**Primary distribution channel:** Direct outreach to MAT IT Directors via the BETT conference ecosystem (the UK's dominant EdTech trade event, held annually in London) and the National Association of School Business Management (NASBM) network. These are the specific channels where district-equivalent decision-makers in the UK are reachable in concentrated form — the analog to the US district IT director conferences that Clever used in its early growth.

**Pricing strategy:** Free SSO portal for districts (preserving Clever's adoption mechanism), with a paid Analytics tier at £2,000–£5,000 per MAT per year depending on school count. Developer fees of £8–£30 per school per month (above Clever's US ceiling, justified by the analytics and discovery value-add). The free SSO tier stress-tests well against alternatives: Google Workspace for Education provides SSO for Google apps but does not solve multi-SIS integration across non-Google tools — the core problem remains. Microsoft Entra ID (formerly Azure AD) similarly requires per-app configuration that the rebuild eliminates. The analytics tier is priced against the cost of a single underutilized edtech license (typically £500–£2,000/year per tool), making the ROI case straightforward for a MAT managing 10+ app contracts.

**Differentiation vs. 2026 competitors:** Against Wonde: AI-powered analytics and app recommendations, not just data piping. Against Clever/Kahoot!: international-first focus, district-pays monetization, and a product roadmap not subordinated to a content company's priorities. Against PowerSchool: neutral intermediary positioning — we do not compete with the apps our districts use, and we never will.
