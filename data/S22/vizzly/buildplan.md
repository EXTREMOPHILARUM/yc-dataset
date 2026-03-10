# Build Plan: Vizzly 2026

## Overview

Vizzly 2026 is a Postgres-native embedded analytics SDK for engineering teams at mid-market SaaS companies who need customer-facing dashboards without building analytics infrastructure. It's built for the developer who wants to ship a dashboard in hours, not months—using natural language queries and row-level security baked into the free tier.

The shift that makes this viable now is LLM-native text-to-SQL. When Vizzly first launched, this was experimental. Today it's production-grade, and semantic layers are table stakes. Simultaneously, the embedded analytics market validated at scale—Sigma raised $200M in 2024—proving customers will pay for this. The original Vizzly lost to distribution and capital constraints, not product-market fit.

The rebuild wins by going narrow and deep: target engineering leads at 50–500-person SaaS companies, ship a free tier that actually works (3 dashboards, full RLS, NL queries included), and distribute through Vercel and Railway marketplaces where thousands of active developers live. Charge for scale and white-label features. The goal is 80% of signups embedding their first dashboard in under 2 hours.34:T451,When James Bowers announced Vizzly's ChatGPT integration in June 2023, GPT-4 had been publicly available for only three months (March 2023). The model was capable but unreliable on complex schemas, and building a production-safe NL-to-chart pipeline required significant prompt engineering, schema introspection tooling, and output validation infrastructure that a four-person team could not prioritize alongside core product work. The feature never left alpha.

By 2026, the capability gap has closed materially. GPT-4o and Claude 3.5 Sonnet achieve greater than 90% accuracy on standard text-to-SQL benchmarks (Spider, BIRD) against defined schemas. More importantly, structured output APIs — OpenAI's JSON mode, Anthropic's tool use — allow a rebuilt product to constrain model outputs to valid SQL against a known semantic layer, making hallucinated queries catchable before they reach the database. This means natural language querying can ship as a core feature on day one, directly addressing the "rigid and forces compromise" criticism Vizzly leveled at the entire embedded analytics category.35:T776,

## Why Now?

### The single most important change: LLM-native text-to-SQL is now a shippable core feature, not a two-engineer research project.

*Well-capitalized incumbents:*
- **Looker (Google):** Dominant in enterprise, but the embedding experience is iFrame-based, requires LookML expertise, and minimum contract sizes effectively exclude mid-market SaaS teams. Weakness: too expensive and too complex for a 10–50 person SaaS company shipping its first analytics feature.
- **Sigma Computing:** Strong for internal analytics; embedding story is secondary to its core spreadsheet-like interface. Weakness: not developer-first, pricing is enterprise-only.
- **Metabase:** Excellent self-serve adoption (50,000+ organizations), but its embedding is iFrame-based and its white-labeling is limited on the free tier. Weakness: the open-source version requires self-hosting and lacks production RLS without significant configuration.

*Direct embedded analytics competitors (Vizzly's former competitive set):*
- **Explo:** Actively solicited Vizzly's customers post-acquisition, indicating real market presence. Weakness: no publicly documented LLM-native querying as of the research report; pricing starts at $995/month, which is a high floor for early-stage SaaS teams.
- **Embeddable:** Published a dedicated Vizzly alternatives page, confirming competitive overlap. Weakness: developer-heavy setup; the semantic layer configuration requires significant upfront engineering investment.
- **Cube:** Strong semantic layer, but it is infrastructure, not a complete embedded analytics product. Weakness: requires assembling a visualization layer separately; not a one-stop solution.

**Demand signals from adjacent products:** The explosive growth of tools like Retool (internal tools), Hex (collaborative notebooks), and Observable (data apps) confirms that SaaS teams want to ship data experiences faster than they can build them. The specific gap — customer-facing, white-labeled, AI-queryable — remains underserved at the sub-$500/month price point.

## Specific market validation since Vizzly's operation:

- Sigma Computing raised $200M at a $1.5B valuation in 2024 (source: Sigma press release), confirming enterprise willingness to pay at scale.
- Cube raised $100M in 2022 (source: Crunchbase), validating the semantic layer as a standalone investable category.
- Metabase crossed 50,000 organizations (source: Metabase blog, date of exact milestone not confirmed in research report — flagging as approximate).

## Distribution channels now available that did not exist or were immature in 2022:

- The Vercel Marketplace and Railway's template ecosystem give developer-tool startups direct access to tens of thousands of active Next.js and Node.js projects with one-click deploy paths.
- The Supabase ecosystem — with over 1 million developers as of 2024 (source: Supabase blog) — provides a warm distribution channel for a product built natively on Postgres RLS, since Supabase users already have the data infrastructure the rebuilt Vizzly would sit on top of.
- Linear, Retool, and Vercel's developer communities on Discord collectively represent hundreds of thousands of self-serve SaaS builders who are the exact buyer persona.

**PLG execution is no longer a resource constraint.** Usage-based billing via Stripe Billing, Lago (open-source), or Orb can be configured in days. Transparent self-serve pricing — the specific friction point cited by Vizzly's own users — is now a one-day implementation decision, not a weeks-long engineering project.

---

## Current Market Analysis

**Market size:** The global embedded analytics market was valued at approximately $67B in 2023 and is projected to reach $115B by 2030 at a CAGR of roughly 8% (source: Grand View Research — note that embedded analytics market sizing varies significantly across research firms; treat this as directional). The market was already multi-billion dollars when Vizzly operated; the structural change is not market size but buyer sophistication and the AI capability floor.

## Competition map and gaps:

### Defensibility analysis — why won't Google, Salesforce, or Microsoft simply add this feature?

This is the honest answer: platform incumbents are a real threat, and there is no structural moat that makes the rebuild categorically safe from them. Google already owns Looker. Microsoft has Power BI Embedded. The defensible position is not "platforms can't do this" — they can and do. The defensible position is **speed-to-value for the mid-market SaaS team that cannot afford Looker's minimum contract and cannot wait six months for a Power BI Embedded integration.** The moat is go-to-market focus and onboarding speed, not technology. This is a real but narrow moat, and the rebuild must be honest about it: if the product does not achieve significant distribution within 18–24 months, platform commoditization is a genuine kill risk.

---

## Recommended MVP

## Core Features:

### AI-native query interface (NL-to-chart)

The user types a question in plain English ("Show me revenue by customer segment for the last 90 days") and receives a rendered chart within the embedded dashboard. Built on GPT-4o structured outputs with a schema-constrained prompt layer that prevents SQL injection and validates queries against the host application's defined semantic model before execution. This differs from Vizzly's original approach in that it ships on day one as a core feature, not an alpha — and it is the primary reason a SaaS team chooses the rebuild over a drag-and-drop competitor.

## RLS-native multi-tenant embedding on the free tier

Row-level security is enforced at the database layer via Supabase or Neon's built-in RLS policies, not as an application-layer add-on. Each end-user of the host SaaS application sees only their own data, enforced by signed JWT tokens passed at embed time. This directly removes the hard blocker that made Vizzly's free Lite plan unsuitable for production deployments — and it makes the free tier genuinely useful for real customers, not just developer evaluation.

## Headless React component SDK with Tailwind-compatible theming

A set of composable React components (chart, table, filter bar, date picker, NL query input) that inherit the host application's design system via CSS variables and Tailwind tokens. No iFrames. This is table stakes in 2026 — not a differentiator — but it must be executed correctly to avoid the integration friction that plagued iFrame-based competitors.

## One-click semantic layer from existing Postgres schema

The host developer points the SDK at their Postgres connection string, and the product auto-generates a human-readable semantic layer (table names, column descriptions, join paths) using an LLM schema introspection step. The developer reviews and edits the layer in a web UI before publishing. This reduces the time-to-first-dashboard from days to under two hours — the specific metric that Vizzly's Product Hunt reviewer praised ("replaced weeks of our engineering time") and that must be the core onboarding promise.

**What you will NOT build in MVP:** Custom visualization types beyond the standard set (bar, line, table, pie, scatter), a no-code dashboard builder for end-users (deferred to v2), multi-database support beyond Postgres, and any mobile SDK.

## Success metrics:

- Time-to-first-embedded-dashboard under 2 hours for 80% of new signups (measured via onboarding telemetry)
- 40% of free-tier signups upgrade to paid within 60 days
- Net Revenue Retention above 110% at 6 months
- 25 paying customers within 6 months of public launch

**Cold-start problem:** This product does not depend on network effects or local density. Each customer deployment is independent. There is no cold-start threshold — the first customer gets full value from day one.

---

## Go-to-Market Strategy

**Target customer segment:** Engineering leads (typically a senior full-stack engineer or a small engineering team of 2–5) at B2B SaaS companies in the marketing technology, revenue operations, or sales enablement verticals, with 50–500 customers of their own, who have received repeated requests for better reporting from their customers and have estimated the internal build at 4–8 weeks of engineering time. This is narrower than Vizzly's horizontal "all B2B SaaS" positioning — the vertical focus enables case studies, word-of-mouth, and integration partnerships within a specific ecosystem.

**Primary distribution channel:** The Supabase ecosystem. The rebuilt product is architected natively on Postgres RLS, which means Supabase users can integrate it with near-zero database configuration. A Supabase integration listing, a featured template in the Supabase template gallery, and active participation in the Supabase Discord (100,000+ members as of 2024, source: Supabase blog) provide a warm, developer-qualified top-of-funnel. Secondary channel: a public GitHub repository with a Next.js + Supabase starter template, optimized for organic search on queries like "embed analytics dashboard Next.js."37:T5b9,

## Pricing strategy:

- **Free tier:** Up to 3 embedded dashboards, 1,000 end-user queries/month, full RLS, NL querying included. This is the critical difference from Vizzly's Lite plan — the free tier is production-deployable.
- **Growth tier:** $199/month — unlimited dashboards, 25,000 queries/month, custom theming, priority support.
- **Scale tier:** $599/month — unlimited queries, dedicated query cache, SLA, SSO.

**Stress-test against free alternatives:** A SaaS team could use Metabase (self-hosted, free) or build a custom Chart.js implementation. Metabase self-hosted requires DevOps overhead, lacks NL querying, and has limited white-labeling. Chart.js requires 4–8 weeks of engineering. The $199/month price is justified if — and only if — the onboarding promise holds: a working, production-grade embedded analytics layer in under two hours. If that promise fails, the free alternatives win. The pricing is therefore contingent on the MVP's onboarding metric (2-hour time-to-dashboard) being achieved before charging begins.

**Differentiation vs. 2026 competitors:** Against Explo ($995/month floor), the rebuild wins on price for early-stage teams. Against Metabase (self-hosted), it wins on NL querying and zero DevOps. Against Embeddable, it wins on onboarding speed via the auto-generated semantic layer. The rebuild does not claim to win on enterprise features, breadth of visualization types, or non-Postgres databases — those are explicitly deferred.
