# Launches

## Nuvi – The AI Agent Builder for Software 3.0

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91726&key=user_uploads/983988/7e12281e-7f3b-4f82-b803-dd815931d5c8)

### **TL;DR**

Everyone wants to build AI agents. But doing it right is still way too hard.

You can build a website with natural language in tools like Lovable. But if you want to build AI agents, you're stuck dragging blocks or writing code.

[**Nuvi**](https://www.nuvi.dev) is the AI agent builder for Software 3.0: Write specs in plain English. Get testable, verifiable behavior — out of the box.

---

## **❌ The Problem**

Building AI agents still means building behavior manually — whether you’re writing code, dragging blocks, or tweaking prompts.

* **Tools like n8n** let you create agents without code, but you’re still wiring up logic step by step.
* **Tools like Cursor** help you code faster, but you still need to know what code to write.

At the same time, **tools like Lovable have shown what’s possible with natural language** — you can build and launch a polished UI in minutes.

Karpathy called it years ago: _“English is the hottest new programming language.”_ But while we’ve embraced it for websites and weekend projects, there’s still no reliable Lovable for building AI agents.

**Intelligent software still lacks a way to go from natural language to tested, trusted behavior.**

We need a system where intent becomes implementation — with structure, simulation, and shared understanding built in.

---

## **🎯 The Solution: Nuvi**

Nuvi lets anyone define, build, and deploy intelligent agents using natural language — with the **structure and guarantees** of real software development.

What makes us different:

🧠 **All in Natural Language**

If you can explain what you want, Nuvi helps you build it. No coding, no frameworks, no LLM know-how required.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91726&key=user_uploads/983988/e8536123-efac-4c99-8924-a3798a077a15)

**🤝 Built for Collaboration**

Specifications are readable, editable, and versioned — so people across different teams stay aligned.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91726&key=user_uploads/983988/2b0f6f88-9d1d-473b-8e76-6e8c3ad190eb)

🧪 **Fully Tested by Default**

User stories become behavioral tests. You can simulate how your agent behaves _before_ launch — and continuously validate after. Using only language.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91726&key=user_uploads/983988/d18df70f-0181-4ec0-83f0-208bab3379aa)

⚙️ **One-Click Deployment**

Click to deploy. Built-in access control and integrations mean you go from idea to agent in minutes.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91726&key=user_uploads/983988/7c089cfe-87e5-44c6-9472-e81963a1431f)

---

## **✅ Nuvi Agents at Work**

Agents built with Nuvi are already transforming how real work gets done — here are a few examples:

* A legal SaaS company built a custom BDR agent that scans hundreds of court filings daily, flags high-complexity cases, and drafts tailored outreach directly in HubSpot.
* A mortgage brokerage built a fulfillment agent that processes messy loan documents, checks them against underwriting rules, and saves hours of manual review on every application.
* An international nonprofit built an AI coach that interviews underserved small business owners, generates detailed financial forecasts, and dramatically scales personalized support.

---

## **💡Our Secret sauce: Specification-as-Source**

In his recent AI Startup School keynote, Andrej Karpathy revamped the idea of **Software 3.0** — where we write software using English instead of code.

But English alone isn’t a programming language. If it were, we wouldn’t have invented C or Python. For English to work as code, it needs structure (but we can now relax how much structure we need). That’s what Nuvi provides.

**🧠 1. AI Specification Assistant**

Describe the agent in plain English. Nuvi helps you clarify goals, cover edge cases, and remove ambiguity — like a linter for intent.

**🧾 2. Specification-as-Source**

The spec _is_ the agent’s source code. It’s structured, complete, and readable by both humans and machines.

**⚙️ 3. One-Click Agent Compilation**

We compile your spec into a live agent. Just like devs once implemented PRDs — but this time, the AI does it.

**🧪 4. Simulation & Continuous Testing**

User stories become test cases. You can simulate the agent’s behavior before launch — and verify it keeps working after.

Nuvi is the behavioral compiler for Software 3.0. Not another prompt wrapper. Not another no-code toy. Real behavior. From real specs. Written in plain English.

---

## **🙌 Our Ask**

* Try Nuvi and build your first agent — all in plain English.
* Want to join the mission, collaborate, or write about us? Reach out at [nuvi.dev](https://www.nuvi.dev/)

## Relari - Testing and simulation stack for GenAI systems

# **TL;DR**

[Relari](https://www.relari.ai/) is an open-source platform to simulate, test, and validate complex Generative AI (GenAI) applications. With 30+ open-source metrics, synthetic test-set generators, and online monitoring tools, we help AI app developers achieve a high degree of reliability in mission-critical use cases such as compliance copilot, enterprise search, financial assistance, etc.

# **⭐ Meet the Relari Team**

Hi everyone, [Yi](https://www.linkedin.com/in/yizhang0123/) and [Pasquale](https://www.linkedin.com/in/pasquale-antonante-5306524a/) from [Relari](https://www.relari.ai/) here. We both spent years building safety-critical AI applications, particularly in autonomous driving and robotics. Pasquale has a PhD from MIT where he researched fault detection in complex AI systems. Yi has an MBA from Harvard and led multiple AI products from concept to production including robo-taxis, self-driving trucks, and warehouse robots.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79322&key=user_uploads/983988/a8982b08-9cda-4741-bc17-eb3df31679e1)

# **💡 Our Inspiration: Autonomous Vehicles**

Just like autonomous vehicles promise to change how we move, GenAI applications promise to revolutionize the way we work. However, ensuring these systems are safe and reliable requires a shift in the development process. Autonomous vehicles need to drive billions of miles to ensure that they are safer than human drivers. This would take decades, so the industry relies on simulation and synthetic data to efficiently test and validate each iteration of the self-driving software stack.

We see a strong parallel in the world of GenAI. At [Relari.ai](https://www.relari.ai/), we are building towards a future where a similar infrastructure will enable complex and powerful applications based on large language models (LLMs).

# **🔴 Problem: GenAI Apps are Unreliable**

LLM-based applications can be inconsistent and unreliable. This blocks GenAI’s adoption in mission-critical workflows and hurts user confidence and retention once deployed to production. Good testing infrastructure is paramount to achieving the quality users demand, but GenAI app developers across startups and enterprises struggle to define the right set of tests and quality-control standards for deployment.

The main challenges the AI teams face are:

* **Complex Pipelines:** GenAI pipelines are getting increasingly more complex and it is often difficult to pinpoint where problems originate.
* **Gap from Evaluation to Reality:** There is a huge gap between the metrics used in offline evaluation and user feedback, leading to distrust in offline evaluation results.
* **Lack of Relevant Datasets:** Public datasets are overfitted by models and often not relevant to specific applications. However, manual curation of custom datasets is extremely time-consuming and costly.

# **🚀 Solution: Harden AI Systems with Simulation**

Relari offers a complete testing and simulation stack for GenAI pipelines designed to directly address the problems above. Relari allows you to:

* **Pinpoint problem root causes with modular evaluation:** Define your pipeline and flexibly orchestrate modular tests to quickly analyze performance issues. Our open source framework offers 30+ metrics covering text generation, code generation, retrieval, agents, and classification with more coming soon.

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=79322&key=user_uploads/983988/04a313af-1bb9-4469-a9d3-4f89c5132aa5)

* **Simulate user behavior with close-to-human evaluators:** Leverage user feedback to train custom evaluators that are 90%+ aligned with human evaluators (backed by our research). Introduce a feedback loop connecting your production system and the development process.

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=79322&key=user_uploads/983988/908218e2-4462-43d5-a23d-7c005c927a29)

* **Accelerate development with synthetic data:** Generate large-scale synthetic datasets tailored to your use case and stress test your AI pipeline. Ensure coverage of all the corner cases before shipping to users.

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=79322&key=user_uploads/983988/d78bb49e-ec9d-4519-909b-b46532751380)


# **❤️ Our Ask**

* ⭐ Star us on Github ([link](https://github.com/relari-ai/continuous-eval))
* 📅 Book a demo with us ([link](https://cal.com/pasquale/relari-demo))
* 👉 Introduce us to AI / ML / Data Science teams building mission-critical GenAI applications ([founders@relari.ai)](mailto:founders@relari.ai)
