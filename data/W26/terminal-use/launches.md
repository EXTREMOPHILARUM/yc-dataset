# Launches

## Terminal Use: Vercel for background agents

Hey!

We’re [Vivek](https://www.linkedin.com/in/v-raja/), [Stavros](https://www.linkedin.com/in/stavrosfilosidis/) and [Filip](https://www.linkedin.com/in/filip-balucha/), and we’re excited to officially launch [Terminal Use](https://www.terminaluse.com)!

## TL;DR:

Agent apps do not win on the model - they win on having a great harness. Terminal Use is agent hosting infrastructure that gives your coding agents the primitives they need to improve your agents.

* **Built for iteration**: fork filesystems and easily try multiple different agent configurations in parallel
* **Agent-friendly**: our platform is CLI-first which allows Claude Code to help you debug, improve, and analyze your agents
* Use **any SDK** & any custom dependencies

👉 **Ask**: Know someone deciding what infrastructure to use for their background agent? **Introduce them to us** ([founders@terminaluse.com](mailto:founders@terminaluse.com) or [book](https://terminaluse.cal.com/vraja/meet) a demo).

<https://youtu.be/iWHs5wOtbrk>

## ❌ The problem

Over the past year, we built and deployed multiple agents following the same loop: build, eval, deploy, A/B test, generate evals from prod. Two things made this painful.

First, the tooling was fragmented: you had to stitch together multiple point solutions to cover the full lifecycle.

Second, production-grade orchestration for agents that used filesystems was hard. When we tried the Claude Agent SDK for real workloads, we hit issues: memory usage varies wildly with subagent count (risking OOMs), crashes require retry logic for durability, and all state lives in \~/.claude and the local filesystem, meaning you have to manage storing the filesystem to make use of it downstream.

At the same time, we all got a new powerful co-worker: **Claude Code**. We became curious about how we could create an out-of-the-box solution for our pains, and also leverage our new co-worker to iterate and improve our agents. This led to Terminal Use.

## ⏩ Our solution

Terminal Use is infrastructure for background agents.

We provide a secure execution environment for your agent. We are framework agnostic - host agents built on Claude Agent SDK, Codex SDK, or your own framework. Bring your own dependencies too!

We handle messaging for you - our messaging SDK lets you persist and stream messages back to your UIs. We also have a Vercel AI SDK integration.

To trigger your agent, you can use our SDKs, or run it on a schedule.

We’re purpose-built for agents that use filesystems. You can share one filesystem across multiple agents, and even fork filesystems to test different agents in parallel on the same input. 

Finally, we know the pains of deploying agents to enterprises from our past experience, and we wanted to make it easy for you to develop agents for our businesses. We allow you to physically isolate data and compute between your customers, and to permission resources granularly.

### Try it out!

Sign up today at [terminaluse.com](http://terminaluse.com). Or [book a demo](https://terminaluse.cal.com/vraja/meet?duration=15)!

## 👷 How We’re Using Terminal Use

Internally, we use Terminal Use to ship Terminal Use! We believe in getting ourselves out of the coding loop so that we’re able to ship faster. But vanilla coding agents keep you in the loop. We found that multi-agent configs, such as actor-critique loops lead to higher quality code and reduce the need for reviews. 

Thus, we build an internal agent that spins up different coding harnesses that we request for on the fly. For example, we ask our agent to spin up a Claude Code harness with Ralph Wiggum Loop. We’re then able to implement a plan with multiple different agents and choose the best implementation.

We love it so much that we’re soon to release our internal agent as a [product](https://woz.terminaluse.com).

## The Team

Vivek and Filip went to University together, and we became close friends when we worked together at Palantir. 

Vivek led the technical delivery of a large agent use case across US hospitals at Palantir. Stavros worked on infrastructure for Palantir dev tooling. Filip worked on the frontend for Foundry’s most-used app.
