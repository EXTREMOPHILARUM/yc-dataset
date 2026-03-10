# Build Plan: Sqreen 2026

## Overview

Sqreen was a Paris-founded application security platform (2015–2021) that embedded a lightweight microagent inside web applications to detect and block attacks at runtime — a technically superior approach to traditional perimeter-based WAFs — but was acquired by Datadog for a reported ~$220M when the market converged observability and security into unified platforms, making Sqreen's standalone agent distribution model structurally uncompetitive against incumbents who could extend existing agents to existing customers at near-zero marginal cost.

The rebuild thesis is not to fight that convergence — it is to exploit the gap it created. Datadog's acquisition validated the CNAPP category and set enterprise pricing that leaves the mid-market underserved; eBPF-based instrumentation now eliminates the per-language SDK burden that constrained Sqreen's original addressable market; and new regulatory mandates (SEC cybersecurity disclosure rules, EU AI Act) have converted "security nice-to-have" into "compliance necessity" for exactly the engineering-led companies Sqreen served best. The new version is a zero-agent-install, eBPF-native application security platform built for platform engineering teams, distributed through the Internal Developer Platform layer rather than competing head-on with Datadog for agent real estate.

---

## Why Now?

### The single most important change since Sqreen's failure: eBPF has made language-specific agent distribution obsolete.

Sqreen's original architecture required maintaining separate SDK integrations for six language runtimes (Ruby, Node.js, PHP, Go, Java, Python). Each integration was an engineering liability, a sales friction point, and a ceiling on addressable market — a company running Elixir or Rust was simply out of scope. eBPF (Extended Berkeley Packet Filter), now production-stable in Linux kernel 5.8+ (released August 2020) and battle-tested in tools like Cilium, Falco, and Pixie, enables kernel-level instrumentation of any application regardless of language, without modifying application code or deploying a language-specific library. A rebuilt Sqreen can instrument a polyglot microservices fleet — Go services, Python ML pipelines, Node.js APIs — with a single kernel-level probe. This is not an incremental improvement; it eliminates the primary engineering and sales bottleneck that constrained Sqreen's growth.

**Regulatory tailwinds have created a new buying trigger that did not exist in 2021.** The SEC's cybersecurity disclosure rules (effective December 2023) require public companies to disclose material cybersecurity incidents within four business days and to describe their cybersecurity risk management processes in annual filings. The EU AI Act (phased enforcement 2024–2026) imposes security and auditability requirements on AI-integrated applications. These mandates convert application-layer security monitoring from an engineering preference into a compliance obligation with board-level visibility — a fundamentally different sales motion than Sqreen faced.

**Market sizing:** The global CNAPP market — the Gartner-defined category that now encompasses what Sqreen called "Application Security Management" — was valued at approximately $7.9B in 2023 and is projected to reach $28.4B by 2030 (MarketsandMarkets, 2023; exact figures should be independently verified). Sqreen had to invent its category; a rebuild enters a validated, analyst-covered market with established buyer vocabulary.

**Distribution infrastructure now exists.** The AWS Lambda Layers marketplace, Kubernetes admission controller ecosystem, and Helm chart repositories provide pre-existing instrumentation pathways that Sqreen had to build from scratch. The CNCF landscape lists 40+ security tooling projects with active contributor communities that a rebuild can integrate with rather than compete against.

---

## Current Market Analysis

**Market size today vs. 2021:** The application security market Sqreen operated in was loosely defined; the CNAPP category that replaced it carries more precise sizing. Gartner named CNAPP a distinct category in its 2021 Hype Cycle. Current market estimates range from $7–10B (2023) to $25–30B (2030 projections), depending on scope definition. These figures are from analyst reports and should be treated as directional — independent verification is recommended before using them in investor materials.

## Competition map and gaps:

- **Datadog Application Security Management:** The direct heir to Sqreen's technology. Strong on correlation with observability data; weak on mid-market pricing (Datadog's per-host pricing model becomes expensive at scale for companies not already on the Datadog observability stack) and on developer-native UX for teams not already Datadog customers. Datadog's ASM is a feature of a $38/host/month platform — a company that wants only application security pays for the entire observability suite.
- **Wiz:** Dominant in cloud security posture management (CSPM) and agentless cloud scanning. Weak on runtime application-layer protection — Wiz sees infrastructure configuration, not in-application attack behavior. Acquired by Google for $32B (2024), which raises integration uncertainty for mid-market buyers wary of Google's product lifecycle history.
- **Snyk:** Strong on developer-native SAST and SCA (software composition analysis); weak on runtime protection. Snyk catches vulnerabilities before deployment but has no runtime blocking capability — it cannot stop a zero-day exploit against a dependency it didn't flag.
- **Contrast Security:** The closest architectural analog to Sqreen still operating independently. Targets enterprise security teams, not developers; complex deployment model; pricing and sales motion mismatched to mid-market engineering-led buyers. This is the gap.
- **Falco (CNCF):** Open-source eBPF-based runtime security for containers. Strong community adoption; weak on application-layer context (Falco sees syscalls, not HTTP request semantics or SQL query intent) and has no commercial support tier that mid-market buyers can purchase.

**Demand signals from adjacent products:** The explosive growth of platform engineering as a discipline (the CNCF Platform Engineering working group was formalized in 2022; Gartner predicts 80% of large software engineering organizations will have platform engineering teams by 2026) signals that security tooling embedded in the IDP layer has a natural buyer who did not exist at scale in 2021.

## Defensibility analysis — why won't Datadog simply win this market?

Datadog will win the enterprise segment of this market. That is not the target. The structural gap is mid-market companies (50–500 engineers) that are not already Datadog customers or are actively avoiding Datadog's pricing model. Datadog's per-host pricing creates a cost cliff for companies running large Kubernetes clusters; its sales motion is enterprise-oriented; and its ASM product requires the full Datadog agent stack as a prerequisite. A rebuild targeting eBPF-native, Kubernetes-native deployment with per-application pricing can serve this segment without competing for Datadog's existing customer base. The honest caveat: if Datadog introduces a standalone ASM SKU with competitive mid-market pricing, this defensibility argument weakens significantly. The rebuild must build distribution and customer lock-in faster than Datadog's product team can respond.

---

## Recommended MVP

### Core Feature 1: eBPF-Native Runtime Protection

A kernel-level security probe that instruments any application — regardless of language or framework — by attaching to Linux syscalls and network events, with no code changes required. It detects and blocks SQL injection, command injection, SSRF, and path traversal attacks by observing actual execution context, not traffic patterns. Unlike Sqreen's language-specific agents, this works across polyglot microservices fleets and requires a single Kubernetes DaemonSet deployment — one `helm install` command for the entire cluster.

## Core Feature 2: LLM-Augmented SAST in the CI/CD Pipeline

A GitHub Actions / GitLab CI integration that runs static analysis on pull requests using a fine-tuned code analysis model (built on top of capabilities like those in Claude 3.5 Sonnet or GPT-4o, both available as of 2024) to identify business-logic vulnerabilities — not just known CVE patterns — with natural-language explanations and suggested fixes inline in the PR. This combines Sqreen's runtime strength with pre-deployment detection in a single workflow, a combination Sqreen could not offer. Unlike generic SAST tools, the LLM layer understands application context: it can flag "this authentication bypass is exploitable given your specific session management logic," not just "this function matches a known vulnerable pattern."

## Core Feature 3: Compliance-Ready Audit Trail

Automatic generation of SEC-disclosure-ready incident reports and EU AI Act audit logs from runtime security events, mapped to the specific regulatory language of each framework. This converts the platform from a security tool into a compliance tool — a different budget line, a different buyer (legal and compliance teams alongside engineering), and a different sales motion. No competitor currently offers this as a native feature; most require manual export and reformatting.

## Core Feature 4: IDP-Native Distribution

Pre-built integrations with Backstage (the dominant open-source IDP, used by Spotify, American Airlines, and 1,000+ organizations as of 2024) and Port, enabling security posture to surface as a component in the developer portal without a separate security dashboard login. This is the distribution channel Sqreen did not have — security visibility embedded where developers already work.

**What we will NOT build:** A network-layer WAF. A standalone CSPM product. Mobile application security. A proprietary observability stack. These are either commoditized, dominated by well-capitalized incumbents, or outside the developer-native positioning.

## Success metrics:

- 50 paying customers within 6 months of GA launch, with ≥80% on Kubernetes
- Average time-to-first-value (first attack blocked or vulnerability flagged) ≤ 15 minutes from `helm install`
- Net Revenue Retention ≥ 110% at 12 months
- ≥ 30% of new customers acquired through Backstage plugin marketplace or IDP referral (validates distribution thesis)

**Cold-start note:** This product has no network effects — it delivers value to a single customer on day one. The eBPF agent blocks attacks and the SAST integration flags vulnerabilities regardless of how many other customers are on the platform. There is no cold-start problem to solve.

---

## Go-to-Market Strategy

**Target customer segment:** Platform engineering teams at Series B–D SaaS companies (200–2,000 employees, $10M–$100M ARR) running Kubernetes in AWS or GCP, with 5–50 engineers on the platform team, who are responsible for developer tooling and security posture but do not have a dedicated application security team. These buyers control the IDP, own the CI/CD pipeline, and have a mandate to reduce security friction for product engineers — exactly the buyer profile Sqreen served, but with a more defined job title and budget in 2026.

**Primary distribution channel:** The CNCF ecosystem and Backstage plugin marketplace. Backstage has 1,000+ organizational adopters as of 2024 (CNCF survey; exact current figure should be verified). A free Backstage plugin that surfaces security posture in the developer portal creates a pull motion — platform engineers discover the tool while solving a portal problem, not a security problem. Secondary channel: GitHub Marketplace for the SAST integration, targeting the moment a developer installs a new CI/CD action.

**Pricing strategy:** $500/month per cluster (up to 50 nodes) for the runtime protection layer, plus $200/month per 10 developers for the SAST integration. Estimated ACV for a 20-developer team on a 3-cluster deployment: ~$18,000 — meaningfully above Sqreen's implied ~$10,000 ACV, justified by the compliance audit trail feature that addresses a board-level mandate.

*Stress test against free alternatives:* Falco (open-source eBPF runtime security) is the most direct free competitor. Falco requires significant engineering effort to deploy, tune, and maintain — it produces syscall-level events that require custom rules and a SIEM to interpret. The rebuild's value proposition against Falco is not "better detection" but "zero tuning time, compliance-ready output, and CI/CD integration." A platform engineering team that values its time at $200/hour needs to spend fewer than 2.5 hours per month on the paid tool vs. Falco to justify $500/month — a threshold most teams will clear in the first week of Falco tuning. Against Snyk's free tier (which covers SAST for open-source projects), the differentiation is runtime blocking and compliance reporting, which Snyk does not offer at any tier.

**Differentiation vs. 2026 competitors:** Against Datadog ASM — no observability stack prerequisite, 60–70% lower cost for mid-market Kubernetes deployments (estimated; exact Datadog pricing varies by contract). Against Wiz — runtime application-layer protection that Wiz's agentless model cannot provide. Against Contrast Security — developer-native UX, IDP distribution, and eBPF deployment simplicity vs. Contrast's enterprise-oriented agent model.
