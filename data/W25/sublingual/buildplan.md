# Build Plan: Sublingual 2026

## Overview

The 2026 Sublingual is a compliance-first LLM observability platform for regulated industries. It's built for engineering teams at Series A–C fintech, healthtech, and defense contractors who need to prove their AI systems are safe and auditable—not just fast. The core product is a local OTel collector that captures every LLM trace without routing data to the cloud, paired with a dashboard for visualizing agentic workflows and a paid tier for encrypted team sync and compliance exports.

The market shift is regulatory: the EU AI Act's conformity assessment requirements went live in 2025, and U.S. financial regulators are now explicitly asking for LLM evaluation logs. Developers can no longer ship on vibes. Existing tools like LangSmith are cloud-only, which disqualifies them for teams handling sensitive data or operating under data residency rules.

The go-to-market is direct: land with compliance and security teams who control vendor selection, then expand to developers once the infrastructure is trusted. Pricing anchors on the paid sync tier—free local observability removes friction, but team collaboration and audit-ready exports drive revenue. This turns the old free-forever model into a freemium wedge that actually converts.32:T8d0,

## Why Now?

The single most important change since Sublingual's failure is regulatory: the EU AI Act's conformity assessment requirements took effect in 2025, and at least 12 U.S. states had enacted AI-specific legislation by early 2026 (exact count varies by source; confirm against current legislative trackers). For engineering teams building LLM applications in financial services, healthcare, and defense contracting, "where do your model traces go?" is now a procurement question with legal consequences, not a philosophical preference. Sublingual's local-first architecture — which the original company treated as a free differentiator — is now a compliance checkbox that enterprise buyers will pay to check.

The second structural change is technical standardization. OpenTelemetry (OTel) was adopted as the de facto LLM tracing standard by OpenAI, Anthropic, and LangChain between 2024 and 2025. This matters enormously for the rebuild: the original Sublingual had to build custom static and dynamic code analysis to achieve zero-code-change instrumentation, a fragile and expensive engineering approach. A rebuilt product can instrument via a single OTel collector sidecar — a solved infrastructure primitive — dramatically reducing engineering complexity and improving reliability across Python, TypeScript, and Go stacks simultaneously.

The third change is validated willingness-to-pay. When Sublingual launched, it assumed developers would eventually pay for LLM observability but had no market proof. That proof now exists: Braintrust raised a Series B in 2024 (exact amount not confirmed in research sources; verify independently), Langfuse raised a Series A, and Helicone's paid tiers are publicly documented at $200–$2,000/month. The "lazy devs" free-forever positioning Sublingual chose was a reasonable hypothesis in early 2025; it is an unnecessary concession in 2026.

Distribution has also matured. The AWS Marketplace and Azure Marketplace now have established procurement paths for developer security and compliance tooling, with pre-approved vendor categories that regulated-industry buyers use specifically to bypass lengthy procurement cycles. Neither channel existed as a meaningful path for a two-person team in early 2025.

---

## Current Market Analysis

**Market size:** The broader AI observability market was estimated at $1.5–2B by 2025 analyst projections (sources vary; no single authoritative figure was found in the research report). The specific segment relevant to this rebuild — LLM evaluation tooling for regulated industries — is smaller but higher-value per contract. No precise sizing for this vertical was found; founders should commission or synthesize primary research before fundraising.

## Competition map and gaps:

- **LangSmith (LangChain):** The structural incumbent for Python LLM developers. Its weakness is cloud-only architecture — all traces route through LangChain's servers — making it a non-starter for teams with data residency requirements. It also has limited support for non-LangChain stacks, creating a gap for teams using raw OpenAI or Anthropic SDKs.
- **Helicone:** Well-funded, strong on cost analytics and rate limiting. Cloud-first with a self-hosted option that requires significant DevOps overhead to deploy. Weak on structured evaluation workflows and human feedback loops.
- **Braintrust:** The strongest competitor on evaluation depth — dataset management, human review queues, scoring rubrics. Cloud-hosted, U.S.-based infrastructure. Weak on compliance documentation and data residency guarantees for EU or regulated-sector buyers.
- **Langfuse:** The closest architectural analog to the rebuild — open-source core, self-hosted option, growing enterprise tier. Its weakness is that self-hosting still requires a Postgres instance and Docker Compose setup, creating meaningful friction for teams without dedicated DevOps. The gap is a genuinely zero-friction local-first deployment with compliance documentation included.
- **Native provider tooling (OpenAI Traces, Anthropic):** Free, deeply integrated, and improving rapidly. These are the most dangerous competitors for single-provider teams. The rebuild's defensibility against them rests entirely on multi-provider support and the compliance audit trail — features that provider-native tools structurally cannot offer without creating antitrust exposure.

**Demand signals:** The success of privacy-first developer tools broadly — Mintlify's on-premise tier, Cursor's local model options, GitHub Copilot's enterprise data isolation guarantees — confirms that "your data stays yours" is a purchasing criterion, not just a marketing claim, for engineering teams at scale.

**Defensibility against platform incumbents:** OpenAI and Anthropic cannot credibly offer multi-provider observability — it would require them to ingest and store traces of competitor API calls, which creates both competitive and legal exposure. This is the structural moat the rebuild must occupy and defend. If a customer's stack is 100% OpenAI, the rebuild has no defensibility; the ICP must be multi-provider or multi-model teams specifically.

---

## Recommended MVP

### Feature 1: OTel-native local collector with compliance export

A single-binary OTel collector sidecar that intercepts LLM traces from any provider (OpenAI, Anthropic, Mistral, local models via Ollama) without code changes, storing all data locally in a structured SQLite format. Unlike the original Sublingual's custom static/dynamic analysis approach, this uses the standardized OTel instrumentation libraries already shipping with major SDKs, making it reliable across framework updates. The compliance export feature generates a signed, timestamped audit log in formats accepted by SOC 2 and EU AI Act conformity documentation — this is the paid unlock.

## Feature 2: Agentic trace visualization

A local dashboard purpose-built for multi-step agentic workflows — showing tool call chains, retry loops, token spend per agent node, and failure points — rather than the flat input/output logs that most incumbents display. This addresses the specific gap Matthew Tang's post-Sublingual "zbench" work pointed toward: agentic evaluation is where incumbents have the least coverage and developers have the most acute debugging pain in 2026.

## Feature 3: Open-core team sync (paid tier)

The local agent is free and open-source. The paid tier adds encrypted team sync: traces can be selectively shared to a hosted dashboard with SSO, RBAC, and retention policies — the exact features enterprise procurement requires. This is the Langfuse open-core model applied to a compliance-first positioning. Self-hosted team sync (for air-gapped environments) is an enterprise add-on, not a free feature.

**What you will NOT build (MVP):** No LLM-as-judge automated scoring, no dataset management UI, no prompt playground, no cost optimization recommendations. These are Braintrust's strengths; competing there in MVP is a distraction.

**Success metrics:** 500 active local installs within 90 days of launch (measured by opt-in telemetry ping, not download count); 10 paying team accounts at $300+/month within 6 months; at least 3 customers in regulated industries (financial services, healthcare, or defense) with documented compliance use cases by month 9.

**Cold-start note:** This product does not depend on network effects or local density. A single developer gets full value from the local collector on day one. The team sync feature requires at least 2 users per account, which is trivially achievable and not a cold-start risk.

---35:T8c1,

## Go-to-Market Strategy

**Target customer:** Engineering teams of 5–50 developers at Series A–C companies in financial services, healthcare technology, or defense contracting who are building multi-provider LLM applications and have already received a security review comment or procurement blocker about third-party data transmission. This is narrow by design — these teams have budget, have already identified the pain, and cannot use the free alternatives.

**Primary distribution channel:** Direct outreach through compliance-adjacent communities — specifically, engineers who have posted in the OWASP LLM Top 10 GitHub discussions, the AI security Slack communities (e.g., MLSecOps Community), and the AWS Financial Services Competency partner network. Secondary channel: AWS Marketplace and Azure Marketplace listings, which regulated-industry buyers use specifically to find pre-vetted tooling with existing procurement pathways.

**Pricing:** Free tier — local collector, unlimited traces, single-user dashboard, open-source. Paid team tier — $299/month for up to 10 seats, hosted encrypted sync, SSO, audit export. Enterprise — custom pricing, air-gapped self-hosted sync, SLA, compliance documentation package.

**Stress-testing the price against free alternatives:** A developer can accomplish basic LLM logging with OpenAI's native traces (free), a local SQLite logger (30 minutes of engineering), or Langfuse's free self-hosted tier. The $299/month price is not justified by logging alone — it is justified by the compliance audit export, the SSO/RBAC that makes it a team tool rather than an individual tool, and the agentic trace visualization that free alternatives do not offer. If a prospect says "I can do this with Langfuse free," the correct response is: "Can your security team sign off on Langfuse's self-hosted deployment for a SOC 2 audit? Here's our pre-written compliance documentation." That is the actual purchase.

**Differentiation vs. 2026 competitors:** Braintrust wins on evaluation depth; LangSmith wins on LangChain integration; Helicone wins on cost analytics. The rebuild wins on one axis only: regulated-industry teams who cannot send traces to any third-party cloud. Own that axis completely before expanding.
