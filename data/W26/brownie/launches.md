# Launches

## IncidentFox. The AI SRE who never drops context.

Hey everyone 👋

We're [Long](https://www.linkedin.com/in/long-yi-b221b2183/) and [Jimmy](https://www.linkedin.com/in/chiehmin-wei/) — co-founders of IncidentFox.

**TL;DR**

AI SRE tools fail without deep context about _your_ systems — and that context lives in integrations nobody has time to build. IncidentFox auto-discovers what each team needs, generates the integrations, and ships with 300+ tools built in. Setup takes less than a day, not months.

👉 Try it: <https://incidentfox.ai>

👉 Open source (Apache 2.0): <https://github.com/incidentfox/incidentfox>

👉 Launch video: <https://youtu.be/TaTpN0JwNYE>

**❌ The Problem: Without the right integrations, your AI has no context**

Every AI SRE tool connects to Slack, reads your Confluence, queries your Datadog. That part is solved.

Here's what isn't: when the AI actually needs to debug something, it doesn't have the right tools.

Your payments team runs a custom Kafka pipeline with internal dashboards. Your infra team uses a homegrown deployment system. Your ML team has proprietary model serving. Each team's stack is different — and the AI has no way to query any of it.

The traditional fix? Hand-build integrations (MCP servers) for every team.

But this creates a new problem:

* Who decides what integrations each team needs? You might know your own team's stack — but when you're debugging another team's service at 3 AM, you don't know theirs.
* So every team needs to sacrifice an engineer to build and maintain their own integrations. That's expensive, slow, and doesn't scale.
* Most teams never get around to it. The AI stays half-useful.

**Integration is the bottleneck.** Not the AI model. Not the monitoring data. The integrations.

**🦊 IncidentFox: We auto-build the integrations for you**

IncidentFox is an AI SRE that lives where your team already works — Slack, Microsoft Teams, or Google Chat. It doesn't just connect to your existing tools — it figures out what tools each team needs and builds them automatically.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97928&key=user_uploads/1146198/102ebfb0-a3c9-45c5-b993-89e39b94e13b)

**1. Auto-discovers and generates integrations**

IncidentFox analyzes your codebase, infrastructure, and incident history to identify gaps — then auto-generates the tools to fill them. No engineer needs to hand-build MCP servers. No team needs to sacrifice headcount on integration work.

A new team onboards? IncidentFox studies their stack and proposes tools specific to their services — with human approval before anything goes live.

**2. Per-team configuration — because every team is different**

Your payments team and your ML team don't use the same stack. Why would they use the same AI SRE config?

Each team gets their own:

* Tools — enable only what's relevant; disable what isn't
* Prompts — fully open source and exposed to engineers. Inject your domain knowledge directly
* Knowledge base — learned from that team's incidents, runbooks, and services

One team's "config drift" is another team's "model drift." IncidentFox understands the difference.

**3. Continuously evaluates and self-improves**

After every incident, IncidentFox:

* Detects gaps — "I couldn't query service X's health endpoint"
* Auto-generates the missing tool
* Evaluates its own investigation quality against the actual resolution
* Updates prompts and knowledge — with human review

It gets measurably better every week. Not because you tuned it — because it tuned itself.

**4. 300+ integrations included on day one**

While it auto-builds what's missing, you're not starting from zero. Kubernetes, AWS, Grafana, Prometheus, Datadog, Elasticsearch, PagerDuty, GitHub — all built in. Integration time is under a day, not months.

**🧠 Why this matters**

**Integrations** — Traditional: Hand-built per team. Each team sacrifices an engineer. IncidentFox: Auto-discovered and auto-generated. Human approves.

**Multi-team scaling** — Traditional: Breaks — you can't know every team's stack. IncidentFox: Per-team config. Each team's AI knows their stack.

**Domain knowledge** — Traditional: Black box prompts, hope it works. IncidentFox: Open source prompts. Engineers inject and edit freely.

**Over time** — Traditional: Stagnates unless manually updated. IncidentFox: Self-evaluates, finds gaps, improves continuously.

**Setup** — Traditional: Months of custom integration work. IncidentFox: &lt; 1 day. 300+ tools out of the box.

**📊 Results**

* 85–95% reduction in alert noise through intelligent correlation
* Hours → minutes for incident investigation
* Zero-config onboarding — Docker in 5 min, production K8s in 30 min

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97928&key=user_uploads/1146198/844d70ec-e308-472c-9bc4-f212cd954153)

**🔒 Enterprise-ready, open-source**

* Open source — Apache 2.0, no vendor lock-in
* SOC 2 compliant, SSO/OIDC, RBAC, audit logs
* Self-hosted, on-prem, or managed SaaS
* Bring your own LLM keys (OpenAI, Claude, Gemini, etc.)

**👬 The Team**

[**Jimmy (CEO)**](https://www.linkedin.com/in/chiehmin-wei/) — Previously at Roblox, where he built social communication features (in-experience calling for 100M+ DAU). Before that, worked at Meta FAIR on multiparty conversational AI, with published research. Cornell CS. Serial founder — previously CTO at a startup in Outlier Ventures' DeFi accelerator.

[**Long (CTO)** ](https://www.linkedin.com/in/long-yi-b221b2183/)— Previously at Roblox, where he built database infrastructure supporting 100M+ daily active users on the Stateful Infra team. Experienced the chaos of on-call firsthand — which is why we're building this. Brandeis CS + Neuroscience + Business.

We've lived on both sides: Jimmy built the AI systems, Long was the SRE drowning in incidents. IncidentFox is what happens when you combine both.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97928&key=user_uploads/1146198/261f0711-50aa-4a0f-b6c9-9cdc7c853dbc)


**🙏 Our Asks**

* Try IncidentFox — self-serve at [incidentfox.ai](https://incidentfox.ai) or star us on [GitHub](https://github.com/incidentfox/incidentfox)
* Intros to engineering teams spending too much time on on-call
  * [Book a demo with us](https://calendly.com/d/cxd2-4hb-qgp/30-minute-demo-call-w-incidentfox)
* Feedback from SREs and infra engineers — [founders@incidentfox.ai](mailto:founders@incidentfox.ai)

Thanks for reading ❤️
