# Launches

## BrowserOS – The Open Source Agentic Browser

**TL;DR:** **BrowserOS is an open-source, AI-native browser that automates your tedious web tasks**. Just describe what you want in plain English—like "find software engineers from my LinkedIn requests and add them to a google sheet"—and watch an AI click, type, and navigate on your behalf, all running locally with your logged-in sessions. We're an open-source and privacy-first alternative to Comet, Dia, Chrome.

We are grateful for all our early supporters — 4.3k+ Github ⭐, 25,000+ downloads and an active discord community of 1000 folks!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93960&key=user_uploads/105063/b11e5c5f-8e15-4375-a62e-ed1ddbaa428b)

### **🤔 Why Now**

AI coding tools made developers 10x faster. But a billion knowledge workers still grind through browser busywork. Copy-paste. Click. Repeat. Even we spend half our engineering time on mindless browser tasks. It's ridiculous—AI writes our entire codebase but can't click a button.

So what’s blocking the browser’s ‘Cursor moment’?

### **🧨 The Problem**

We think it comes down to three big problems preventing mass adoption of AI agents for knowledge workers, especially at enterprises:

**1. Can't access your logged-in sessions.** Most agentic solutions today (like ChatGPT Operator, Manus) run on remote computers. They can't log into your Gmail, LinkedIn, or company tools. So they fail at every real task you actually need help with.\
**2. Tools are fragmented.** You've got agent builders that use MCP servers. Others that only do browser automation. Some that just call APIs like Zapier. There's no single solution that lets you build an agent using all these approaches together.\
**3. Closed source:**  Most other popular browsers come from search/ad companies who want to track you and sell ads. They lock you into their LLMs, hide how things work, and send your data to their servers. That's a dealbreaker for enterprises who can't send sensitive data to third parties.

## **🥳 Our Solution**

BrowserOS is an open-source, privacy-first browser built to solve these problems by design.

1. It's just a normal browser you download and run on your machine. You log into websites like you always do. But now agents can use those logged-in sessions to actually do useful work - they can browse the web just like you would, using your existing logins.
2. We support both MCP servers and browser automation. You can stitch them together to build agents that handle complex workflows. Need to pull data from a website, process it through an API, then update a spreadsheet? One agent can do it all.
3. We're fully open source. You can see our system prompts, change them if you want. Bring your own API keys or run models locally with Ollama. Your data stays on your computer.

Key features of BrowserOS:

* **Build agents with plain English** - Just describe what you want. No coding required.
* **Use any LLM you want** - Bring your own API keys, switch between models, or run everything using local LLMs
* **Still a normal browser** - It's Chromium underneath. All your Chrome extensions work.

### **🚀 The future**

Here's what excites us: a billion knowledge workers spend 60-80% of their day in browsers. Every enterprise runs on web apps—Salesforce, SAP, Workday, internal tools. These workers waste hours on tasks that make them miserable. Filing expense reports. Extracting data from dashboards. Setting up ad campaigns.

**We think browsers will become new operating system where AI employees live and work alongside humans.** Imagine a world where IT builds an “expense report agent” once, every employee benefits. Someone shares their “Facebook Ads agent” publicly. You fork it, tweak it for your workflow. The mundane work gets automated while humans focus on what matters.

This kind of automation only works in browsers. Not everything has APIs, but everything has a web UI. If an agent can click and type like a human, it can automate any web app—from legacy enterprise software to the latest SaaS tools.

We're building the best browser for this future!

### **🏋️‍♂️ Team**

We're twin brothers who've been building products together for years. We spent the last 6 years as engineers at Google and Meta.

Nikhil worked on Instagram Reels and Facebook Feed Ranking backend—deep C++ and systems work. Nithin was an ML engineer on YouTube Recommendations and worked on building Youtube’s first Large Recommender Model (LRM).

We feel this gives us the perfect mix of experience to tackle a massive C++ codebase like Chromium while building a powerful agent and AI layer on top.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93960&key=user_uploads/105063/5b10f1a2-86df-4154-a02b-52ae465cea00)

### **🙏 Our Ask**

* **Star us on [GitHub](https://git.new/browseros)** to support our mission.
* **Download [BrowserOS](https://www.browseros.com/)**; it’s available for macOS, Windows, and Linux!
* **Join our [Discord](https://discord.gg/YKwjt5vuKr)** to help shape our roadmap.

## Felafax: Expanding AI Infra beyond NVIDIA

**TL;DR:** We are building an open-source AI platform for non-NVIDIA GPUs. Today, we are launching one of the pieces, a seamless UI to spin up a TPU cluster of any size and providing an out-of-box notebook to fine-tune LLaMa 3.1 models. **Try us at **[**felafax.ai**](https://felafax.ai?utm_source=yc&utm_medium=post&utm_campaign=launch-yc)** or check out our **[**github**](https://github.com/felafax/RoadRunnerX)**!**

## 👋 Introduction

Hi everyone, we're Nikhil and Nithin, twin brothers behind Felafax AI. Before this, we spent half a decade at Google and Meta building AI infrastructure. Drawing on our experience, we are creating an ML stack from the ground up. Our goal is to deliver high performance and provide an easy workflow for training models on non-NVIDIA hardware like TPU, AWS Trainium, AMD GPU, and Intel GPU.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82653&key=user_uploads/105063/96b92f10-55b4-4137-a100-23bea3e5c4c6)

## 🧨 The Problem

* The ML ecosystem for non-NVIDIA GPUs is underdeveloped. However, alternative chipsets like Google TPUs offer a much better price-to-performance ratio; **TPUs are 30% cheaper** to use.
* The cloud layer for spinning up AI workloads is **painful**. Training requires installing the right low-level dependencies (infamous CUDA errors), attaching persistent storage, waiting 20 minutes for the machine to boot up… the list goes on.
* Models are getting bigger (like Llama 405B) and don't fit on a single GPU, requiring complex **multi-GPU** orchestration.

## 🥳 The Solution

Today, we're launching a cloud layer to make it easy to spin up AI training clusters of any size, from 8 TPU cores to 2048 cores. We provide:

* **Effortless Setup:** Out-of-the-box templates for PyTorch XLA and JAX to get you up and running quickly.
* **LLaMa Fine-tuning, Simplified:** Dive straight into fine-tuning LLaMa 3.1 models (8B, 70B, and 405B) with pre-built notebooks. We've handled the tricky multi-TPU orchestration for you.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82653&key=user_uploads/1765/d34757cd-a366-4dcb-9491-0d03f46520a7)

In the coming weeks, we will also launch our open-source AI platform built on top of JAX and OpenXLA (an alternative to NVIDIA's CUDA stack). We will support AI training across a variety of non-NVIDIA hardware (Google TPU, AWS Trainium, AMD and Intel GPU) and offer the same performance as NVIDIA at 30% lower cost. **Follow us on **[**Twitter**](https://x.com/nikhil_sonti)**, **[**LinkedIn**](https://www.linkedin.com/company/felafax/)** and **[**Github**](https://github.com/felafax/RoadRunnerX)** or updates!**

## 🙏 How You Can Help

1. Try our seamless cloud layer for spinning up VMs for AI training – **you get $200 credits** to start off - [app.felafax.ai](https://app.felafax.ai/)
2. Try fine-tuning LLaMa 3.1 models for your use case.
3. If you are an ML startup or an enterprise that would like a seamless platform for your in-house ML training, reach out to us ([calendar](https://cal.com/nikhilsv/felafax)).
