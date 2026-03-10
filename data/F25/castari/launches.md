# Launches

## Castari – The runtime for agents that need a computer

### TL;DR

Castari is hosting infrastructure for agents that need more than an API call. Run `cast deploy` and your agent gets a secure sandbox, auto-scaling endpoint, and full observability.

Public beta is live today.

<https://youtu.be/2fpCTj051kY>

---

### The problem

Serious agents aren’t just “call an API and done.”

They execute code, hit tools and browsers, run for minutes to hours, and touch sensitive systems. Every team ends up rebuilding the same fragile setup:

* homegrown agentic harnesses
* stitched-together sandboxes/microVMs/containers/queues
* logs and traces scattered everywhere
* hacky snapshots and suspect secret handling

So:

* every agent needs its **own** mini-runtime
* debugging one run is detective work
* adding a new agent feels like starting a new infra project

Deploying agents that work great locally turns into wrangling infrastructure.

---

### **The problem**

Serious agents aren't chatbots. They execute code, call tools, touch filesystems, and run for hours. They need a computer.

But there's no good way to put them in production. You end up stitching together containers, queues, and compute layers — rebuilding the same infrastructure every team rebuilds. The agent works on your laptop. Getting it to work reliably for users takes weeks.

We hit this ourselves. We built an AI consumer app to 2M+ members while at RunPod (scaled to $100M revenue). The hardest part was never the model — it was the harness. Every time we shipped a new agent, we were rebuilding sandboxing, scaling, secrets, and monitoring from scratch.

### **What we built**

Castari wraps your agent in a secure sandbox and gives you back a production endpoint.

```
npm install -g @castari/cli
cast login
cast deploy
```

Your agent now has:

* **Secure sandbox** — full isolation. Your agent can safely execute code, use browsers, and access filesystems
* **Auto-scaling endpoint** — scales with demand, no capacity planning
* **Observability** — trace every tool call, decision, and output in real time
* **Multi-model support** — Claude, OpenAI, xAI, open source. Your code stays the same
* **Zero lock-in** — remove Castari and your agent still runs on vanilla Claude Agent SDK

---

### **How we're different**

Most tools give you primitives — a sandbox API, a container runtime, a compute layer. You still stitch it together yourself.

Castari wraps around your agent. You define it declaratively, we manage the lifecycle: provisioning, versioning, execution, scaling, teardown. You write agent logic, not infrastructure code.

### **What's next**

* Better tracing and observability — debug agent behavior in production, not after the fact
* Higher sandbox concurrency limits — run more agents in parallel
* Forever-running sandboxes — agents that stay alive indefinitely

---

### Why we’re working on this

While I was leading the FDE team at RunPod:

* Built and shipped AI infrastructure and agents for **Fortune 500s and fast-growing startups**
* Watched the same loop repeat: agent works in a notebook → weeks disappear into infra glue → nobody trusts the system, production release gets delayed (over and over again).

Additionally, while [@Cambree Bernkopf](https://bookface.ycombinator.com/user/1372064) and I scaled our AI consumer app to 2m+ users, our biggest issues were getting our agents to work reliably in production.

The pattern is clear: **agents deserve a first-class runtime, the way frontends got one.**

Castari is our bet that:

* Sandboxing & safety should be built-in, not bolted on
* Going from “prototype” to “production-safe” should be one config file, not a quarter-long project
* AI teams should ship agents, not infrastructure.

---

### Try it

Docs: [docs.castari.com](http://docs.castari.com)

Website: [castari.com](http://castari.com)

CLI: `npm install -g @castari/cli`

Or email [jacob@castari.com](mailto:jacob@castari.com) — happy to get you deployed.

— Jacob & Cambree

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97921&key=user_uploads/1070542/1e7ef564-ad96-4b4e-aa0e-80212ee05604)

## Castari - Vercel for AI Agents

Hey! We’re Jacob Wright & Cambree Bernkopf, founders of [Castari](https://castari.com).

### **TL;DR**

**Castari lets teams deploy AI agents to secure, autoscaling sandboxes in seconds.**

You write agent logic with the **Claude Agent SDK (other frameworks coming soon)**. We turn it into a production-grade endpoint.

We’re especially focused on:

* Teams building **internal agents** (ops, support, data, eng workflows).
* Companies whose **core product is an agent** built on Claude Agent SDK and need a safe, reliable way to run it.

### Launch Video:

https://youtu.be/81K80OivtAc

### The Problem:

Serious agents are not just a single API call. [Agents need a computer.](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)

They execute code, call tools and browsers, run for minutes instead of milliseconds, and touch sensitive systems. Most teams end up rebuilding the same fragile setup:

* Homegrown agent harnesses
* Sandboxes, file systems, and queues stitched together
* Logs and traces scattered across many services
* Ad hoc snapshots and risky secret handling

The result:

* Every agent needs its own mini runtime
* Debugging one agent run feels like detective work
* Adding a new agent feels like starting a new infra project

Good agents stall at “cool demo” instead of reaching production. Deploying agents becomes a full-time infrastructure problem.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95573&key=user_uploads/89898/44917ba7-819c-4c41-a80f-ef359054b19e)

### How Castari solves it

We’re building Castari to be the **natural runtime for AI agents built on Claude Agent SDK**. We wrap the entire agent in a sandbox, deploy it, and provide you with an endpoint url that auto-scales as requests come in. No need to write code in your tools to manage your sandbox lifecycle.

#### **1. Drop in a config file → get a production runtime**

In your Claude Agent SDK repo:

* Add a `castari.yaml` (entrypoint, tools, env vars)
* Run `castari deploy`

That’s it. Your agent is now running in a secure sandbox with an endpoint, UI, and observability.

Whether that agent is:

* an **internal system** your team uses
* a **customer-facing agent** that _is_ your product

the deployment workflow is identical and boring (in the good way).

#### **2. Sandboxing & safety, built-in**

* Every run executes in an isolated sandbox designed for tool-using agents
* You design the behavior; we handle isolation and scaling
* No more duct-taping together sandbox primitives for specific tools

**Bottom line:** You keep building on **Claude Agent SDK** the way you already are — for internal workflows or core products. Castari turns that into a safe, observable, production-ready runtime.

### Why Castari is different

**E2B, Modal, Daytona, Cloudflare** (and friends) give you powerful sandbox and compute primitives.

**Castari sits one layer up:**

Castari wraps around your Claude Agent SDK-based agents so you can define them declaratively and run them in secure sandboxes, without owning the underlying sandbox lifecycle.

* **Agent-first semantics**: runs, sessions, tools, snapshots are native concepts we manage.
* **Zero framework lock-in**: remove Castari and your agent still runs on vanilla Claude Agent SDK; keep Castari and your infra team gets its life back.
* **Focused start**: deeply integrated with **Claude Agent SDK** today, with the same “drop-in config” experience coming to other frameworks next.

We’re building the runtime we wish existed for agents.

### Why we’re working on this

While I was leading the FDE team at RunPod:

* Built and shipped AI infrastructure and agents for **Fortune 500s and fast-growing startups**
* Watched the same loop repeat: agent works in a notebook → weeks disappear into infra glue → nobody trusts the system, production release gets delayed (over and over again).

Additionally, while [**@Cambree Bernkopf**](https://bookface.ycombinator.com/user/1372064) and I scaled our AI consumer app to 2m+ members, our biggest issues were getting our agents to work reliably in production.

The pattern is clear: **agents deserve a first-class runtime, the way frontends got one.**

Castari is our bet that:

* Sandboxing & safety should be built-in, not bolted on
* Going from “prototype” to “production-safe” should be one config file, not a quarter-long project
* AI teams should ship agents, not infrastructure.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95573&key=user_uploads/1070542/5fbe422a-1cc4-49e3-95ce-8740164b600e)

### Ask: early pilot access

We are opening a limited pilot for:

* Teams building internal agents who need a safer, more reliable runtime
* Companies building agent centric products that need to run in production without bespoke infra

If that is you and you are tired of wrestling with sandboxes, observability, and brittle tooling:

→ Email [**jacob@castari.com**](mailto:jacob@castari.com) with subject “Castari Pilot” and 2 to 3 sentences about your agent stack and use case.\
→ Check out our open source repo for using any model with Claude Agent SDK on [GitHub](https://github.com/castar-ventures/castari-proxy).\
→ Join the waitlist on [**castari.com**](http://castari.com) to hear about our first releases.

Jacob, Cambree, and the Castari team
