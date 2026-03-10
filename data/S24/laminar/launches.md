# Launches

## Laminar – Understand why your agent failed. Iterate fast to fix it.

Hey everyone, Robert from Laminar (YC S24) here. The entire observability space was built for request-response LLM apps. Nobody was building for Agents that run for 40 minutes and fail in ways you can't reproduce. So we did.

## Tracing that actually helps you understand what happened

Most observability platforms just collect data and wait until you go look at it. And when you do, you get a tree of spans. You click into one, read it, go back, click the next one, try to hold the context in your head. For a simple LLM call, that's fine. For an agent that ran for 30 minutes and made 200 decisions, it's practically useless.

We built Laminar's tracing to give you as much information as quickly as possible.

Our trace timeline and **reader mode** lay out the agent's reasoning and actions as a clean, readable feed.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98606&key=user_uploads/1771812/73741d82-1719-4062-8cc2-9bd8de880010)

You open a trace and immediately see what the agent did, what it was thinking, and where things went wrong (we also capture and show application level exceptions). For browser agents, we record **full browser sessions synced with traces**. You literally see what the agent saw at every step → <https://laminar.sh/shared/traces/16fcd540-9583-8bcb-f8e0-8b15ec92c58d>.

If a trace is too complex to parse visually, you can **chat with it**: ask questions about what happened in natural language, instead of manually digging through hundreds of steps. We take into account the whole context of the trace, not just a single span.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98606&key=user_uploads/1771812/87cc29b4-f5c3-4924-ab96-5c52af1fae76)

We can confidently say that we have the best tracing DX on the market. It’s one line of code to integrate. Laminar SDK auto-patches vast majority of AI frameworks and SDKs, including **Claude Agent SDK, AI SDK, LiteLLM, Browser Use, Stagehand, OpenHands SDK**, and much [more](https://docs.laminar.sh/tracing/integrations/openai). We are the only platform that traces **Claude Agent SDK sub-agents**. When Claude delegates work to sub-agents, you get full visibility into that entire chain, not just the top-level call. Here’s an example of a trace <https://laminar.sh/shared/traces/3f9219d0-8691-daf7-836a-8874ca4c1d9f>.

## The debugger

This is the feature we wished existed when we were building agents ourselves. When your agent fails 15 minutes into a run, the normal workflow is: restart from scratch, wait for it to reach the same state, hope it reproduces the failure. That's insane.

Laminar starts a local dev server that connects to our platform. You can run your agent directly from our UI, and when a run fails, you go to the exact step where it went wrong. You tweak your prompt or tool definitions right in the UI. And you rerun from that step — with full context preserved.

Here's how it works under the hood: our tracing SDK sits right before the LLM call boundary. When you rerun from a step, we mock all the LLM calls that happened before that point, replaying their original responses. This means the agent walks through its prior steps instantly without actually calling any LLMs and spending any tokens — and crucially, it properly restores external state along the way. If your agent was controlling a browser, the browser gets back to the exact page and DOM state. If it was working in a sandbox, the sandbox is restored. By the time execution reaches your breakpoint, everything — conversation history, tool state, external environment — is exactly as it was. You tweak your prompt, hit rerun, and the agent picks up from there with the real world intact.

Here’s a demo of Laminar debugger.

<https://www.youtube.com/watch?v=iSw8MM6tRvY>

## Signals

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98606&key=user_uploads/1771812/19af455c-7dfa-46e7-aa40-fbac2b4696a6)

In development, you care about individual runs. In production, you have thousands of runs and the question changes — it's no longer "why did this run fail," it's "what's going wrong across all my runs and how often."

That's what Signals solve. You write a short natural language description of what you want to detect — something like "agent gets stuck in a retry loop" or "user gets frustrated and rephrases their request." Laminar runs this against every trace, extracts matching events, and then clusters them into patterns. So instead of manually sampling traces hoping to spot trends, you get a structured view of what's actually happening. We use this ourselves to monitor our own agents, and it catches things we'd never find by skimming through traces.

## SQL editor, evals, and more

All of your data lives is accessible with built-in SQL editor (both in UI and API). You can run arbitrary queries against your traces, spans, and events — build custom dashboards, do ad-hoc analysis, or bulk-create datasets from production traces. Those datasets plug directly into our evals pipeline, so you can run evaluations on real production data instead of synthetic test cases.

## Laminar

Leading agent companies like Browser Use, OpenHands, Rye.com, Alai and many more use Laminar in production. Laminar is fully open source and extremely fast (written in Rust). Self-host it anywhere or use our managed platform (<https://laminar.sh>).

**Our ask:**

* If you're shipping agents and debugging is painful, we'd love to help — [founders@lmnr.ai](mailto:founders@lmnr.ai)
* Intros to teams running long running agents would be huge
* Star us on GitHub: <https://github.com/lmnr-ai/lmnr>

🔗 <https://laminar.sh>

## Laminar: The Missing Developer Tool for Browser Agents

Robert and Din from Laminar here. We created a new type of observability, which enabled us to build the SOTA open-source browser agent.

# The Problem

Browser agents are powerful but notoriously difficult to develop and debug. When your agent fails, traditional traces just show a wall of text logs without context. You can't see what the agent was looking at when it made decisions, why it chose certain actions, or what exactly went wrong. It's like trying to debug a self-driving car without any camera footage – practically impossible.

This lack of proper observability tools has been the biggest barrier to building reliable browser agents.

# The Solution

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89930&key=user_uploads/1771812/0da20a73-6dc1-4d3d-8561-dc38dd8cb624)

Laminar created the missing piece in browser agent development: complete visual context for every agent action and decision. Our platform records high-quality browser sessions and perfectly synchronizes them with agent traces. Now developers can:

1. **See what the agent sees** - Watch the complete visual journey of your agent as it navigates websites
2. **Pinpoint exact failure points** - Identify precisely where and why agents make mistakes
3. **Debug with context** - Understand agent decisions with full visual and trace context

# Results

Using our own tools, we built Index - open-source browser agent that achieves 92% on WebVoyager benchmark, setting a new state of the art. Index can handle everything from research tasks to complex automations in apps like Google Sheets. In other words, we created a reliable **API layer to any website** that you can simply prompt with natural language.

# Integrations

Laminar seamlessly integrates with AI browser frameworks like **Stagehand** and **Browser Use** - integration takes just 2 lines of code.

# Ask

* **Build better agents:** Try Laminar today for your browser and AI agent development => <https://lmnr.ai>
* **Explore our open source agent:** Check out Index at [github.com/lmnr-ai/index](https://github.com/lmnr-ai/index)
* **Dive into docs:** Comprehensive guides at <https://docs.lmnr.ai>

We're looking for early adopters and feedback! Reach out to us at [founders@lmnr.ai](mailto:founders@laminar.ai) and join our [discord](https://discord.com/invite/nNFUUDAKub).

## Laminar - Open-source observability and analytics for complex LLM apps

**tldr: Laminar is an open-source developer platform that provides full instrumentation of LLM applications and combines trace data with event-based analytics.**

**—**

Hey everyone, we’re Robert, Din, and Temirlan. Previously, we built infrastructure at Palantir, Amazon, and Bloomberg — now, we’re building an open-source platform to help developers understand how their LLM apps perform in production.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83572&key=user_uploads/1771812/e4140bd4-1ae9-453d-8457-2564c3820cbc)

# Why do LLM apps need observability from day 0?

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83572&key=user_uploads/1771812/81e46417-9b77-4368-ab0f-c04b8b84556e)

LLMs are stochastic, and designing robust software around them (e.g., RAG, Agents) is an iterative process. A great observability platform not only facilitates this process, but actually makes it more productive. Hence, many AI developers adopt observability tools early on.

Laminar goes beyond single LLM call tracing and provides tools for entire app instrumentation and powerful UI for full trace visualization, trace search, and session grouping.

## What is different about analytics for LLM apps?

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83572&key=user_uploads/1771812/29d881c9-de4c-416a-be18-d17638d67135)

LLM apps produce traces, which are essentially very rich text. Traditional event-based analytics tools are not built for extracting metrics from this kind of data.

Currently, AI devs spend a good chunk of their time manually inspecting traces to understand usage patterns of their LLM apps. As they scale, manual inspection is not feasible anymore.

Laminar tackles this problem by using other LLMs to process rich text outputs in the background. With Laminar, developers can define custom events, such as “USER SENTIMENT,” to collect user sentiments and track this metric at scale as they deploy their LLM apps into production.

Each event is linked to the trace that produced it, and developers can understand when and why certain semantic events have happened. It gives developers deeper understanding of the performance and usage of their LLM apps.

## Our ask

* Star our repo → <https://github.com/lmnr-ai/lmnr>
* Start tracing and tracking events with a managed version of our open-source platform here → <https://www.lmnr.ai>
* [Join our Discord](https://discord.com/invite/nNFUUDAKub)
* Connect us with anyone who builds software around LLMs and would greatly benefit from a tool like this!

## Laminar - Developer platform to ship reliable LLM agents 10x faster

# tl;dr: Laminar is a developer platform that combines orchestration, evaluations, data, and observability to empower AI developers to ship reliable LLM applications 10x faster. Get started for free → [lmnr.ai.](https://www.lmnr.ai)

Hey everyone, we’re Robert, Din and Temirlan. Previously, we built infrastructure at Palantir, Amazon, and Bloomberg— now our goal is to help AI developers ship reliable LLM applications faster.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82294&key=user_uploads/1771812/1a4a4a99-7e50-4bcd-86ff-8d2a5474a091)

# ❌ The Problem

LLMs are stochastic, and designing robust software around them (e.g. LLM agents) demands rapid iteration on core logic and prompts, constant monitoring and a structured way of testing new changes. Existing solutions are vertical and the burden of maintaining “glue” between them is still on the developers, which inevitably slows them down.

# ✅ Our Solution

Laminar is a dev platform that combines orchestration, evaluations, data, and observability to help AI devs to ship reliable LLM applications 10x faster. We provide:

* a GUI to build LLM applications as dynamic graphs with seamless local code interfacing.
* an [open-source package](https://github.com/lmnr-ai/lmnr-python) to generate abstraction-free code from these graphs directly into developers' codebases.
* a state-of-the art evaluation platform that lets devs build fast and custom evaluators without managing evaluation infrastructure themselves.
* a data infrastructure with built-in support for vector search over datasets and files. Data can be easily ingested into LLMs and LLMs can write to the datasets, creating a self-improving data flywheel.
* a low latency logging and observability infrastructure.

# Orchestration

As devs, we love to code everything ourselves, but we’ve realized the fastest way of iterating on LLM application logic is via graph UI. So, we’ve built the ultimate LLM “IDE”, where you build your LLM applications as dynamic graphs. You can build cyclical flows, route to different tools, and collaborate with your teammates in real-time!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82294&key=user_uploads/1771812/be5a68c2-4440-4fd3-92e7-71c7436e13c8)

Graphs can seamlessly interface with local code. “Function node” can call local functions on your server, right from our UI or our SDK. It’s a huge game changer for testing of LLM agents which call different tools and then circle the response back to LLMs. In the gif below, local function “save_result_to_db“, which runs on a server on my computer, is directly called from our UI.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82294&key=user_uploads/1771812/17ade57e-5551-4db3-a036-0bed9956a79e)

Using our [open-source package](https://github.com/lmnr-ai/lmnr-python), you can generate zero-abstraction code from graph definition, which exactly replicates the graph functionality. Code is generated as pure functions right inside your repo, and you have total freedom to modify it however you want. It is extremely valuable for the devs who are tired of frameworks with myriads of layers of abstraction.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82294&key=user_uploads/1771812/6955178c-ef6a-4b26-bac9-39fdebe6f1ac)

You can also deploy LLM pipelines as API endpoints on our infrastructure and easily call them via our Python/TS sdks.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82294&key=user_uploads/1771812/d071c79f-9b3c-4376-9de1-c9cccd401e6b)

# Evaluations

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82294&key=user_uploads/1771812/799c93b7-c273-4b65-ac0c-50a3e360952c)

Laminar pipeline builder can be used to build custom and flexible evaluation pipelines that seamlessly interface with local code. You can start from something simple like exact matching and then build a custom LLM-as-a-judge pipeline tailored to your specific use case. You can upload large datasets and run evaluations on thousands of data points at the same time, and get all statistics about the run in real time. All of this without the pain of managing evaluation infrastructure yourself.

# Observability

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82294&key=user_uploads/1771812/f6d0e26d-60d7-4371-a558-a36006d8cd43)

Whether you decide to host LLM pipelines on our platform or generate code from graphs, all pipeline runs are logged and you can easily inspect the traces in the convenient UI.

# Conclusion

Laminar aims to deliver the best developer experience for AI developers. We remove unnecessary friction and burden of managing infrastructure. We let you focus on building the best AI products and ship them 10x faster!

# Our ask

* Start building reliable LLM agents right now for free → <https://www.lmnr.ai>
* Check out [open-source code gen package](https://github.com/lmnr-ai/lmnr-python)
* Connect us with anyone who builds software around LLMs and would greatly benefit from a tool like this!
* [Join our Discord](https://discord.com/invite/nNFUUDAKub)
