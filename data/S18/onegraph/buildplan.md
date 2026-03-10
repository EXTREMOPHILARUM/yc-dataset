# Build Plan: OneGraph 2026

## Overview

OneGraph (YC S18, founded July 2018) built a single GraphQL endpoint that unified dozens of SaaS APIs — Salesforce, Stripe, GitHub, Gmail, and more — behind one authenticated interface, handling parallelization, caching, and auth; it operated as a two-person team until Netlify acqui-hired it in November 2021, folding the technology into Netlify API Authentication.

The rebuild thesis is not that OneGraph was wrong — it was early. The two structural killers (manual integration maintenance and no distribution) are both solvable in 2026: LLMs can now auto-generate and self-heal API resolvers, and AI agents have created a new, enterprise-grade demand for exactly the unified API graph OneGraph was building. The new version is an **AI-native unified API layer for agentic workflows** — a managed MCP-compatible graph that lets AI agents and developers query hundreds of SaaS APIs through a single, self-maintaining endpoint, priced for the enterprise teams who are already paying for agent infrastructure.

---

## Why Now?

## The single most important change: LLMs can now write and maintain API integrations autonomously.

OneGraph's primary structural failure was that maintaining live integrations with dozens of third-party APIs was a headcount-scaling problem, not a revenue-scaling problem. A two-person team hit a hard ceiling. That ceiling is gone. GPT-4 (March 2023) and Claude 3 Opus (March 2024) can read API documentation, infer schema relationships, generate typed GraphQL resolvers, and detect breaking changes by diffing OpenAPI specs — tasks that previously required a human engineer per integration. A rebuilt OneGraph could plausibly support 500+ APIs with a team of five, where the original supported "a couple dozen" with two.

The second change is demand-side and structural: AI agents need unified API access more urgently than human developers ever did. When a human developer integrates Salesforce, they do it once and move on. An AI agent executing a workflow may call Salesforce, Stripe, GitHub, and Slack in a single reasoning step, repeatedly, at high volume, with no tolerance for auth failures or schema inconsistencies. This is OneGraph's original value proposition, but the customer is now an agent runtime rather than a developer — and the enterprise teams deploying those agents have budget.

The third change is the emergence of the Model Context Protocol (MCP), introduced by Anthropic in late 2024. MCP is structurally identical to OneGraph's thesis: a standardized protocol for connecting AI models to external services. The ecosystem is nascent and fragmented — as of early 2025, MCP server quality varies enormously, there is no managed hosting layer, and enterprise authentication is largely unsolved. This is the gap. (Specific MCP adoption metrics beyond Anthropic's announcement are not yet publicly available as of this writing.)

On the GraphQL side, Apollo Federation v2 (released 2022) has made federated GraphQL a mainstream enterprise pattern, expanding the pool of developers already fluent in the query paradigm OneGraph required customers to adopt cold in 2018.

Distribution is also solved differently now. The Vercel Marketplace and the emerging AI agent app stores (e.g., OpenAI GPT Store, Anthropic's partner ecosystem) provide direct access to the developer and enterprise audiences that OneGraph had to build from scratch.

---

## Current Market Analysis

**Market size:** The API management market was valued at approximately $5.1 billion in 2023 and is projected to reach $13.7 billion by 2028 (MarketsandMarkets, 2023). The adjacent iPaaS (Integration Platform as a Service) market — which includes MuleSoft, Boomi, and Workato — was valued at $6.6 billion in 2023 (Grand View Research). Neither figure existed at OneGraph's 2018 founding in its current form. More directly relevant: the AI agent infrastructure market has no clean sizing yet, but enterprise spending on LLM tooling and agent orchestration is the fastest-growing line item in software budgets as of 2025 — specific figures are not yet reliably published.

## Competition map:

- **Zapier / Make (Integromat):** Serve non-technical users with workflow automation. Zapier's 2021 valuation was $5B. Their weakness is that they are not developer-native, not queryable programmatically, and not designed for agent consumption. They are not competitors for the agentic use case.
- **MuleSoft / Boomi / Workato:** Enterprise integration platforms with sales-led motions, six-figure contracts, and XML/REST-era architectures. Their weakness is that they are not GraphQL-native, not LLM-friendly, and not designed for the latency and query flexibility that agent workflows require.
- **Hasura:** Provides a GraphQL layer over databases and REST APIs. Strong for data access; weak for SaaS API aggregation and agent-oriented auth flows. Does not natively address MCP.
- **Apideck:** A unified API layer for specific verticals (HRIS, CRM, accounting). Closer to OneGraph's model but vertically narrow and not AI-agent-oriented.
- **Raw MCP server ecosystem:** Fragmented, unmaintained, no enterprise auth, no SLA. This is the clearest gap.

**Demand signals from adjacent products:** Cursor, Windsurf, and Claude's computer use feature all require structured, reliable access to external APIs. LangChain's tool-use integrations and OpenAI's function-calling ecosystem show high developer demand for exactly the kind of typed, schema-defined API access OneGraph provided — but the existing solutions are DIY.

**Defensibility analysis:** The honest answer is that this is a real risk. Anthropic could extend MCP into a managed hosting layer. OpenAI could build a unified tool registry. Vercel or Netlify could rebuild what Netlify dismantled. The structural defense is not technical moat — it is **integration depth and reliability SLA**. The platform incumbents (Anthropic, OpenAI, Vercel) are building horizontal infrastructure; they will not maintain 500 live API integrations with enterprise-grade uptime guarantees. That is an operational commitment, not a feature. The second defense is **enterprise auth and compliance** — SOC 2, HIPAA-compatible credential vaulting, and audit logging are things agent platform incumbents will not prioritize in their first versions. A focused company can own this layer before the platforms catch up, then sell to those platforms as an acquisition target — which is, notably, exactly what OneGraph did successfully once already.

---

## Recommended MVP

## Core features:

**1. LLM-maintained API resolver engine.** On ingestion of an OpenAPI or GraphQL spec, the system auto-generates typed resolvers, maps authentication requirements, and schedules weekly spec-diff checks to detect breaking changes — triggering automated resolver updates with human review flagged only for ambiguous cases. This directly solves OneGraph's primary failure mode: the two-person maintenance ceiling. The original OneGraph required a human engineer to write and maintain each integration; this version treats integration maintenance as a background job.

**2. MCP-compatible unified endpoint.** Every connected API is exposed both as a standard GraphQL endpoint and as an MCP tool definition, so AI agent runtimes (LangChain, LlamaIndex, Claude, OpenAI Assistants) can discover and call APIs without custom integration code. OneGraph's original endpoint was GraphQL-only; the MCP layer is the new primitive that makes the same architecture relevant to the agent ecosystem that did not exist in 2018.

**3. Enterprise credential vault with per-user OAuth delegation.** Developers register their OAuth apps once; the platform handles token storage, refresh, and per-end-user credential scoping with audit logs. This was the limitation that plagued even Netlify's post-acquisition implementation — the initial beta could not proxy site visitor credentials. Solving this cleanly, with SOC 2 compliance, is the enterprise differentiator.

**4. Schema explorer and query builder (visual + LLM-assisted).** A modernized graphiql-explorer with an LLM co-pilot that suggests cross-API joins and generates queries from natural language. The original explorer was OneGraph's most widely adopted open-source contribution; this version is the paid product's primary onboarding surface.

**What you will NOT build:** workflow automation (that is Zapier's market), a no-code UI for non-technical users, or a database layer (that is Hasura's market). No mobile SDKs in year one.

**Success metrics:** 50 active developer accounts within 90 days of launch; 5 paying enterprise customers (>$2K/month) within 6 months; API resolver auto-generation accuracy >90% on first-pass for APIs with published OpenAPI specs (measured by test suite pass rate); <0.5% resolver breakage rate per month across all connected APIs.

**Cold-start / network effects:** This product does not depend on user-to-user network effects or local density. Value is delivered to a single developer on day one — they connect one API and query it. The network effect is on the supply side: each new API integration benefits all users. The cold-start strategy is to launch with 50 pre-built, LLM-maintained integrations covering the highest-frequency SaaS APIs (Salesforce, Stripe, GitHub, Slack, HubSpot, Linear, Notion, Jira) and let the resolver engine handle expansion from there.

---

## Go-to-Market Strategy

**Target customer segment:** AI engineering teams at Series A–C B2B SaaS companies building internal or customer-facing agent workflows. Specifically: teams of 3–15 engineers who have already deployed at least one LLM-powered feature and are now hitting the "our agent needs to read from Salesforce and write to Jira simultaneously" problem. This is narrow enough to have a repeatable sales motion and large enough to build a business on.

**Primary distribution channel:** Developer-led, community-seeded. Launch on the Vercel Marketplace (access to Vercel's 1M+ developer accounts) and publish an open-source MCP server registry as a community asset — the graphiql-explorer playbook, but with a deliberate conversion funnel this time. Sponsor LangChain and LlamaIndex community channels, where the target customer is already asking "how do I give my agent access to Salesforce without managing OAuth myself?"

**Pricing strategy:** Free tier (up to 3 connected APIs, 10K queries/month) to seed developer adoption and generate the open-source community signal. Paid tiers at $299/month (up to 20 APIs, 500K queries, standard SLA) and $1,500/month (unlimited APIs, enterprise auth, SOC 2 audit logs, dedicated support). Enterprise contracts negotiated above $2K/month for custom SLAs and on-premise credential vault options.

*Stress test against free alternatives:* The free alternative for this use case is writing custom integration code — which is genuinely free but costs 2–5 engineer-days per API integration plus ongoing maintenance. The $299/month tier needs to be cheaper than one hour of a senior engineer's time per month to justify itself, which it is at typical 2026 engineering compensation rates. The harder comparison is against raw MCP servers, which are free but unmaintained and lack enterprise auth. The pitch is reliability and compliance, not capability — a distinction that matters to enterprise buyers and not at all to hobbyists, which is why the free tier exists to serve the latter without trying to convert them.

**Differentiation vs. 2026 competitors:** Apideck is vertically narrow; raw MCP servers have no SLA; MuleSoft is priced for the Fortune 500 and architected for the 2010s. The rebuild's differentiation is the combination of LLM-maintained breadth (500+ APIs), MCP-native output format, and enterprise-grade credential management — no single competitor offers all three as of early 2026. The risk is that Anthropic or OpenAI builds this; the response is to be the acquisition target when they do, which is a viable outcome given OneGraph's prior art.
