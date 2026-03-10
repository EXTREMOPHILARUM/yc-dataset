# Launches

## Superagent — Defender of AI agents 🥷

Hi YC 👋 We’re Alan and Ismail, founders of **Superagent (YC W24)**.

We’re building open-source **defense for AI agents**. Our product protects agents from prompt injections, malicious tool calls, and customer data leaks — in production, in CI/CD, and wherever they run.

# The Problem

AI agents introduce new attack surfaces that traditional security practices don’t cover:

* **At runtime**: users can inject adversarial prompts that hijack an agent or force it to run harmful commands.
* **At the model** layer: unsafe or poisoned outputs can embed backdoors into your stack.
* **In CI/CD**: AI-generated code can contain harmful logic that slips through review and ships to production.

Without protection, agents can leak customer data or trigger destructive actions that impact your product and your users.

# How Superagent Works

At the core is **SuperagentLM**, our small language model trained specifically for agentic security. Unlike static rules or regex filters, it reasons about inputs and outputs to catch subtle and novel attacks.

Superagent integrates at three key points:

1. **Inference providers** — filter requests and responses at the API layer
2. **Agent frameworks** — run runtime checks on every input, output, and tool call
3. **CI/CD pipelines** — fail risky builds before unsafe code ships

Here’s a quick example of how to use it with Exa (YC S21):

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94188&key=user_uploads/1367556/35562a1a-829f-4fc0-bcc2-03952e3f58f6)

Every request is inspected in real time. Unsafe ones are blocked. Safe ones go through — with reasoning logs you can audit later.

# Why We’re Building This

We’ve been working closely with builders of AI agents for the last couple of years, building tools for them. What we noticed is that many teams are basically trying to system-prompt their way to security. Vibe security (VibeSec) obviously doesn’t work.

Some of the most popular agentic apps today are surprisingly unsafe in this way. So we decided to see if we could fix it. That’s the motivation behind Superagent: giving teams a real way to ship fast **and** ship safe.

# Get Involved

📖 [Read the docs](https://docs.superagent.sh/)

📅 [Book a call](https://www.superagent.sh/)

We’d love your feedback: what’s your biggest concern about running agents in production? Book a call or drop a comment!

Alan & Ismail 🥷🥷\
[Superagent](https://www.superagent.sh/) (YC W24)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94188&key=user_uploads/1367556/22c8addf-151e-4bf5-ade5-18f253df2bc4)

## Superagent — the AI Firewall 🥷🔥

Hi everyone, we’re Alan and Ismail, founders of **Superagent** (YC W24).

We built the world’s first **AI Firewall** — powered by a model that sits between you and your models, protecting every request and response in real time.

---

## The Problem

AI is quickly becoming the foundation of how software is built and used. But every time you send a prompt or receive a response, you take a risk:

* Models can be tricked with prompt injections or jailbreaks
* Sensitive data like API keys and PII can leak out
* Malicious code or backdoors can slip through responses

If you’re building with AI or adopting third-party AI tools, you’re exposed.

---

## Our Solution

Superagent introduces **NinjaLM** — a small language model fine-tuned for security and safety. It runs in runtime (tens of milliseconds) and reasons about every prompt and response before it reaches your system.

✅ Stops prompt injections and jailbreaks\
✅ Prevents secret leaks (API keys, credentials, PII)\
✅ Blocks malicious code before it reaches your system\
✅ Full audit logs, traces, and observability for compliance

From internal apps to tools like Claude Code or ChatGPT, Superagent protects your AI without slowing you down.

## https://youtu.be/GBTAs9yZiPM

## Backstory

Before Superagent, we built plenty of AI apps ourselves. Each time, we ran into the same problem: adding even the most basic kind of protection was incredibly hard.

Traditional firewalls are built for static rules — not reasoning. But AI isn’t static. It thinks, it adapts, and that creates a completely new class of security challenges.

We realized the only way forward was to fight fire with fire: build a model that could reason about other models, catching attacks, leaks, and malicious behavior in real time. That’s how the AI Firewall was born.

---

## Try It

We just launched our hosted service, and the open-source repo is live. Engineers can get started in minutes, and executives get the auditability and compliance they need.

👉 [superagent.sh](http://www.superagent.sh)\
👉 [github.com/superagent-ai/superagent](https://github.com/superagent-ai/superagent)

---

## Call to Action

If you’re building or adopting AI:

* Engineers — run your apps through Superagent today
* Security teams — add prevention and compliance controls
* Partners — we’re exploring integrations and distribution

We’d love your feedback. Links in comments.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93541&key=user_uploads/1367556/b76c2ef1-9036-484d-9564-73cecff2c9ff)

---

## VibeKit 🖖 The Safety Layer for Your Coding Agent

Hey YC! 👋\
We’re building **VibeKit**, an open-source safety layer for Claude Code, Gemini CLI, and other coding agents.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92929&key=user_uploads/1367556/58ed677f-4f55-4d10-a0ef-b32fb2508117)

## ❌ The Problem

We love coding with AI agents — until the day Anthropic emailed us to say they had found our API keys in a public GitHub repo and revoked them.

The leak came from our own coding agent. That’s when we realized most developers have no way to see — let alone control — what their AI agents are doing:

* Which files they read or write
* What shell commands they run
* What data leaves their machine
* Whether secrets get exposed in API calls

## 🖖 The VibeKit Solution

VibeKit is a **universal CLI wrapper** that runs any coding agent in a **local, isolated Docker sandbox**,

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92929&key=user_uploads/1367556/76cf29ec-d566-42e9-861b-fad1a9bd4889)

It comes with:

* **Secret redaction** before anything leaves your machine
* **Full observability** into file changes, commands, API calls, and outbound data
* **Offline-first**, open-source (MIT), and works with any agent — Claude, GPT-4o, Gemini, etc.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92929&key=user_uploads/1367556/20caa134-7f4a-434d-acac-6e5405eeb82b)

## 💻 Try it out

```
# Install globally
npm install -g vibekit

# Run Claude Code with VibeKit
vibekit claude
```

Then watch _everything_ your AI is doing — safely.

🎥 **Demo video:** [https://youtu.be/vDwJ4xcdRBM\\](https://youtu.be/vDwJ4xcdRBM%5C)

📂 GitHub: [https://github.com/superagent-ai/vibekit\\](https://github.com/superagent-ai/vibekit%5C)

📖 Docs: [https://docs.vibekit.sh](https://docs.vibekit.sh/)

## 🙏 Our Ask

If you use coding agents day-to-day:

* **Run them through VibeKit** — see what they’re _really_ doing.
* Share your weirdest or most alarming finds with us — we’re building a public library of “agent fails.”

💌 Contact: [founders@vibekit.sh](mailto:founders@vibekit.sh)

---

## VibeKit 🖖 Run coding agents in a secure sandbox

## **Launch YC: VibeKit – Run coding agents in a secure sandbox**

**Hi YC** 👋 We’re Alan and Ismail, the founders of Superagent (YC W24). We build tools for developers working with agents — especially **coding agents**.

Today, we’re launching **VibeKit**, our open-source SDK that lets you run coding agents like OpenAI Codex or Claude Code safely in secure sandboxes.

Local setups work great for developing with coding agents — we’ve used them ourselves. But as soon as you want to **embed agents into your app**, **automate GitHub workflows**, or **run tasks in isolated environments**, you need something more flexible and secure.

**VibeKit makes this possible.** It supports multiple sandbox providers (E2B today; Daytona, Modal, and [Fly.io](http://Fly.io) coming soon) and gives you:

* ✅ Safe, isolated code execution
* ✅ Live output streaming
* ✅ Async run handling
* ✅ Full prompt + code history
* ✅ Telemetry and tracing
* ✅ GitHub-safe automations

With VibeKit, coding agents can install packages, modify files, or create PRs — all without touching your local or production systems.

https://youtu.be/GQaOSEbvOxM

We originally built VibeKit for internal use while developing Superagent. Since then we’ve used it to:

* Embed coding agents inside apps
* Build GitHub bots that open issues and PRs
* Automate internal workflows (e.g. adding PostHog)

Now it’s fully open source (MIT licensed) and available for anyone to use.

🌐 [vibekit.sh](http://vibekit.sh) 

💻 [github.com/superagent-ai/vibekit](http://github.com/superagent-ai/vibekit) 

### 🙏 **Our Ask**

* ⭐️ Star the repo
* 🧪 Try embedding a coding agent in your app
* 💬 Tell us what use cases it unlocked for you — email [founders@superagent.sh](mailto:founders@superagent.sh)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91137&key=user_uploads/1367556/d5bc1c0b-6a66-42b4-b75d-b28d6237e1a6)

## 🥷 Superagent - Run any workflow using AI

_**Tl;dr:** [_Superagent_](https://superagent.sh/) makes it easy for anyone to use AI to do complex tasks. Enterprises and startups already use it for things like managing R&D projects, customer support, and market research. It's open-source, and it's designed for everyone - not just AI experts. With Superagent, businesses can save money and work smarter. [_Learn more about Superagent_](https://superagent.sh/?utm_source=yc&utm_medium=blog&utm_campaign=launch-yc)._

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79352&key=user_uploads/89898/db78152a-35a4-497e-acac-55556a095c07)

👋 Hello, we're [Alan](https://linkedin.com/in/alanzabihi) and [Ismail](http://se.linkedin.com/in/pelaseyed/en). Our path to Superagent started while working on an AI app, where we faced the reality of needing to build the entire tech stack and become AI experts just to perform one basic workflow. This experience led us to create Superagent, aiming to simplify AI use for everyone.

## 🚨 The Problem: AI integration is complex

The reality is, integrating AI into business processes is a complex task. It usually demands teams of machine learning engineers, which is a significant barrier for many companies. Consider a business executive who sees AI as an almost unachievable goal; this perspective can lead them to miss out on the benefits AI could bring to their operations.

## 🚀 Our Solution: Easy-to-build AI-agents

With Superagent, companies can build their own AI agents to perform whatever workflow they have in their business operations:

* **No coding or infrastructure needed**: Configure AI agents using simple markup.
* **Integration with Airtable**: Ideal for managing data-heavy tasks like market research.
* **API and SDKs**: Allows embedding AI agents into any app or third-party system, including task management tools like Jira.

By choosing Superagent, companies can:

* Automate complex tasks that would typically require manual effort or sophisticated programming.
* Reduce operational costs by spending less time and fewer resources on routine tasks.
* Gain a competitive edge by doing better work internally, but also by creating new customer experiences.

## 💡 Opportunity in Enterprise

Technology, healthcare, and banking are massive sectors with data-heavy operations. Superagent's open-source model has led to bottom-up adoption from these sectors, showing validation of our approach. Join us as we tap into this massive opportunity.

## 👋 How you can join in

\- Fork us on [GitHub](https://github.com/homanp/superagent)

\- Join our community on [Discord](https://discord.com/invite/mhmJUTjW4b) 

\- Create your first AI workflow on our [cloud service](https://superagent.sh/?utm_source=yc&utm_medium=blog&utm_campaign=launch-yc)

\- [Contact us](mailto:alan@superagent.sh) for custom advice on your workflows
