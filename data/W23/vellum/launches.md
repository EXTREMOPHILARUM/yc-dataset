# Launches

## Vellum for Agents

**TL;DR: Today, we’re launching Vellum for Agents;** an agent builder that takes a plain description of what you want to automate and asks follow up questions to understand your needs. It connects to your tools, handles the logic, and shows you exactly what the agent is doing so you are never guessing why or how it works. To celebrate our launch we’ll be giving away free credits for everyone who signs up today (worth $100). Launch video [here](https://www.youtube.com/watch?v=72TU43fauo4).

We’re a W23 company with deep experience running AI in production. We’ve built AI tooling used by teams at Drata, Redfin, Seeking Alpha, Headspace, and Swisscom to launch and operate real AI solutions.

_That experience led us here._

Today, we’re sharing a new version of Vellum, an agent builder for ops teams. You describe the task you want to automate, and Vellum gives you a working agent in minutes. It asks follow up questions, connects to your tools, handles the logic, and shows you exactly what the agent is doing at every step, so there is no guesswork.

## Common problems on using AI agents

In 2025 I watched as our engineering team gained superpowers. Coding agents like Devin, Claude Code, Cursor seemed to move them to a whole new level. By end of year, 40% of the work was done by agents and their productivity is up 2.5x.

That impact never really reached the rest of the company.For those of us who are not engineers, getting started with agents is still hard.

While the models are good enough to help with Ops, Finance, Sales, and Marketing tasks, there are frequent challenges that we’ve observed:

* Too many off-the-shelf tools that almost work, but break in specific edge cases
* Prompts you tweak over and over, but still do not fully trust
* Logic that becomes hard to manage in drag and drop builders
* Little guidance on what is actually possible with agents
* A lot of technical setup, before anything feels useful

**_There is a huge drop off in the agent adoption funnel and we’re here to fix it._**

## The solution

Today we’re excited to launch the new version of Vellum.

Just explain the task you want to automate and Vellum turns it into a working agent (like Lovable for agents). Vellum will ask follow-up questions to understand what you need and connect to your tools. It handles the logic and makes the agent’s behavior visible, so you’re never guessing what it’s doing or why.

### Agent: Getting from 0 to 1

Once you give Vellum your prompt, it asks a few follow up questions and builds a plan. For some use cases, it will ask which apps to connect and confirm access. When it has everything it needs, it creates the first version of the workflow:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96757&key=user_uploads/1020427/aea05991-1a72-42a9-9f21-f803c82a3616)

### Console: Access run and output details

After you have the first version of your agent, you get a UI that shows exactly how it works and what it does on each run. You can keep refining it with help from the agent itself, whether that’s improving prompts, adding new tools, or adjusting the logic.

To then test your changes, you can run the agent directly from the UI and inspect every decision it makes, like which tools it calls, when it decides to run a web search, and how it arrives at the final output.

We believe our agent logic is among the most reliable out there, and teams reach a working setup much faster compared to other agent builders.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96757&key=user_uploads/1020427/8c4b97e9-0e04-4920-9719-2ef967d6c74e)

### Interact: Run manually, via triggers, API or code

Once you’re happy with how your agent works, you have a few ways to use it. Depending on your use case, you can choose one of the following:

* run the agent through a ready made UI
* vibe code your own UI with one of our integrations (e.g. Lovable)
* run it on a schedule or trigger it through APIs or app events

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96757&key=user_uploads/1020427/77309dfb-ba7c-406d-b4ed-a38aa9d440f2)

## Most common use-cases

If you want to try Vellum today, here are the common agent automations we’ve seen ops teams build:

* **Content generation:** Agents around SEO and GEO keyword research, content analysis, and daily content creation.
* **Sales ops automation:** This is where we’ve seen the most use cases in the last few months. From automated demo prep, to pulling account intelligence from CRMs, to analyzing sales calls and deals.
* **Product ops:** Agents can reliably analyze support tickets and Linear issues, then ping the right DRIs to move things forward.
* **Customer support:** This is where agents really shine today. They can classify all incoming tickets and surface insights, like the best timing for renewals, automatically.

## What we ask

1. **If you have one gnarly task that you’ve been putting out** we ask you to login to Vellum and try to automate it. Share your feedback in this thread or text me at [akash@vellum.ai](mailto:akash@vellum.ai)
2. **Do any of these problems resonate with you?** Please share your experience in creating agents to automate your tasks. We would love to learn more!

## Vellum Workflows – Quickly prototype and deploy AI chains

Hello hello! We’re Noa Flaherty, Akash Sharma, and Sidd Seethepalli from [Vellum](https://www.vellum.ai/).

**Tl;dr** "Workflows" is a new product in Vellum's LLM dev platform that helps you quickly prototype, deploy, and manage complex chains of LLM calls and the business logic that tie them together. We solve the "whack-a-mole" problem encountered by companies that use popular open source frameworks to build AI applications, but are scared to make changes for fear of introducing regressions in production.

**The Problem 😰: Many AI use-cases require chains of prompts, but experimentation and productionization of complex chains is hard.**

We have helped dozens of customers take their AI prototypes to production by delivering tools for efficient prompt engineering, tightly integrated semantic search, prompt versioning, and performance monitoring. However, as the AI industry matures, we’ve found that more and more real-world use-cases require multi-step flows across actions like semantic search, multiple prompts/LLM calls, and bespoke business logic.

For example, if building a customer-support chatbot, you may want to:

1. Use a fast, low-cost, model to categorize an incoming user question
2. Depending on the categorization, query against a different index in a vector store to return relevant context about how to answer the question
3. Feed that context into a prompt that’s been tuned to answer accurately about that topic
4. Feed the output of that prompt into another that rephrases using your brand voice
5. Finally, return the answer to your end user

Unfortunately, existing tools and frameworks don’t make it easy to:

1. Rapidly experiment with these chains both step-by-step and end-to-end – especially if you’re non-technical
2. Make changes with confidence once in production and avoid regressions
3. Gain visibility into the performance of the system both as a whole, and at each step in the chain

**The Solution 🤤: A fully managed platform for experimenting with, deploying, and managing AI workflows that power your app**

Vellum Workflows provides a low-code UI for experimenting with and deploying LLM workflows to power features in your app.

You can construct a workflow using different “Nodes,” define “Input Variables” to the workflow, their values across different “Scenarios” and run with a single click to see the output at each step along the way.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=74014&key=user_uploads/1213437/1d62e723-3e99-4eb5-b4bd-5b4eef082579)

_Shown here is one of the workflows used in production by a customer of ours, Miri Health, for powering their health & wellness AI chatbot._

You get immediate feedback on whether your chain/prompts perform the way you expect without having to edit code, inspect console logs, or hop between browser tabs. You can validate that your workflow does what it should across a variety of scenarios / test cases.

Once you’re happy, you can deploy the Workflow directly in Vellum and invoke it through an API via Vellum’s python/node SDKs. Events for nodes that you subscribe to are streamed back using [Server-Sent Events](https://www.w3schools.com/html/html5_serversentevents.asp).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=74014&key=user_uploads/1213437/18a82c70-6ee8-4cde-af75-183014f838a0)

_Invoke a workflow via a simple API. Use our officially supported python and node sdks, or roll your own._

By deploying your Workflow through Vellum, you can:

* Mix and match models from different providers without having to integrate with each. Use the best prompt/mode for the job!
* Have a production-ready backend in minutes without having to write, maintain, and host complex code and orchestration logic
* Version your Workflow, see changes over time, and revert with one click
* Get full observability into the production system, viewing inputs, outputs, timestamps, and more for the workflow as a whole, as well as each Node along the way.
* Use role-based access control to determine which team members are allowed to experiment vs update production deployments

Monitor how your workflows are performing in production, with the ability to inspect the inputs/outputs of the workflow as a whole, as well as each step in the chain.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=74014&key=user_uploads/1213437/da276020-b865-472f-a569-c767320a5667)

**Looking Ahead**

This is just the beginning! Our beta customers are already asking for things like:

* A/B testing workflows for live experimentation
* Test suites for evaluating that workflows are doing what they should and don’t break after an “improvement” is made
* Composability via nested workflows
* More node types for executing code, making calls to 3rd party APIs, etc.

**Why Vellum?**

Our focus to date has been to provide robust building blocks for creating production-ready AI applications. We’ve seen our customers assemble Vellum-powered Prompts and Semantic Search to create incredible products, version control and debug them using Vellum Deployments, and validate them when making changes using Vellum Test Suites.

Now that we have the building blocks, we’re well-positioned to help you assemble them. Workflows has been in closed-beta for a few weeks now and we already have customers using them to power their entire AI backend in production.

> Vellum Workflows give us the opportunity to really tailor different parts of our product to the end users’ needs without having to invest in tons of custom development, which has dramatically decreased our time to market. As a technical, but non-engineering stakeholder, I’m able to truly participate in the development of the product experience and help deliver personalized AI-powered experiences to customers faster than I could have ever imagined.
>
> **Adam Daigian, Product Lead at Miri Health**

We firmly believe that the best AI-powered products out there will be the result of close collaboration between technical and non-technical team members. We’ve repeatedly seen engineers set up the initial scaffolding, integrations, and guard-rails, while non-technical folks run experiments and tweak prompts/chains. No other platform facilitates this collaboration as well as Vellum.

**Ask: How you can help**

* Sign up for a free 14-day trial if the problems we aim to solve resonate with you. [Click here](https://vellum.ai/landing-pages/14-day-trial).
* Share your thoughts and feedback on our direction in the comments below 👇
* Spread the word with others you think this may help

## Vellum - Build production-worthy LLM applications

**TL;DR** [Vellum](http://vellum.ai) (W23) is a developer platform for building production-worthy applications on LLMs like @OpenAI’s GPT-3 or @Anthropic’s Claude. Use Vellum to save hours on prompt engineering, iterate on prompts in production confidently, and continuously fine-tune for better results (we helped one customer save 94% of their LLM costs through fine-tuning!). Request early access [here](https://www.vellum.ai/landing-pages/request-early-access).

—

Hi everyone,

Akash, Noa and Sidd here. We worked together at Dover (YC S19) for 2+ years where we built production use-cases of Large Language Models (LLMs). Noa and Sidd are MIT engineers who previously worked at DataRobot’s MLOps team and Quora’s ML Platform team respectively.

We decided to work on Vellum after realizing that while the MLOps industry has matured rapidly for traditional ML, companies using LLMs don’t have any of this tooling available. Engineering teams spend many hours building custom internal tooling to tame LLMs, taking away time from building their core product.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69757&key=user_uploads/1020427/c77e40f4-74d7-49b8-89cf-650548274362)

# 

# **The LLM Management Problem**

We’ve seen companies building production applications with Large Language Models experience challenges at all stages:

1. **Going from 0 → 1:** ”Prompt engineering” has become an important role in working with LLMs. Today, most people experiment with various prompts across browser tabs and the more diligent track the results of their experimentation in spreadsheets. Rarely do people take the time to test each variant across a sufficient number of test cases, let alone try different parameter combinations and LLM providers. Most settle for a sub-optimal configuration because the testing process is so tedious. Querying for semantically relevant context against a corpus of text to inject in the prompt is another large barrier for many people just getting started.
2. **Managing changes once live in production:** Tracking model & prompt versions, keeping an audit log of inputs/outputs, testing changes to prompts/models before going into production, and measuring aggregate quality metrics are all critical for a production-worthy system, but all require custom code and non-trivial internal tooling. Engineers don’t have time to build out this tooling and instead, fly blind – never sure what their current baseline for quality is or whether “improvements” made to their prompts will in fact break existing behavior.
3. **Post-MVP optimization:** Most people find a semi-reasonable prompt for _text-davinci-003_ and move on. But, they also acknowledge that with more time, they could set up a fine-tuning pipeline, experiment with other models/LLM providers, and try out new foundation models as they’re released to maximize output quality while dramatically reducing LLM provider spend. They’re paying a premium for sub-optimal quality and risk falling behind as new models are released.

# 

# **The Vellum Product**

We have 3 products – each aimed to solve the problems we identified when building production LLM apps ourselves.

### **Vellum Playground: Super powers for prompt engineers**

Create one “sandbox” per LLM use-case. In each, you can try as many prompt variants as you like across as many test cases as you wish. These prompt variants may differ in their text, underlying model, model parameters (e.g. “temperature”), and even LLM provider! Each run is saved as a history item and has a permanent url you can use share with teammates and track results.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69757&key=user_uploads/1020427/3a844278-c463-456f-ae0a-566ecbd29153)

## **Vellum Manage: Confidently iterate on models in production**

Once you’ve settled on a prompt you like, you “deploy” it through Vellum. Vellum acts as a high-reliability, low-latency proxy layer between you and LLM providers. Every request is captured and persisted in one-place, providing observability into your model’s performance. Because the API interface doesn’t change, you can update your prompt (and even the underlying LLM provider!) without making any code changes. Previously made requests can be replayed against proposed changes to gain confidence prior to updating a deployment. All updates are version-controlled and you can revert to prior versions at any time.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69757&key=user_uploads/1020427/437adec7-b675-459c-8148-fe7600c20c41)

## **Vellum Optimize: Continuously fine-tune to improve quality and lower cost**

Once you’ve collected data in production for some time through Vellum Manage, these input/output pairs (minimum 100, but depends on the use case), can be used to fine-tune your own proprietary models for better quality, lower cost, or lower latency. Your data and your models become a powerful competitive moat. Vellum periodically runs model evaluation jobs in the background to see if we can find a different model that works even better for your use case. If one is identified, you can swap models under-the-hood – no code changes needed!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69757&key=user_uploads/1020427/72d1eb55-ddc8-4512-b674-1e409c4eb608)

P.S: If you’re curious, we recently published a blog where you can learn more about the benefits of fine-tuning and how to do it. Check it out [here](https://www.vellum.ai/blog/what-is-fine-tuning-and-when-to-use-it).

### **Trusted by companies on the bleeding edge of AI**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69757&key=user_uploads/1020427/f3a6ea0a-6b88-4b9c-81a6-8a4770e42e0f)


## **Our ask**

* Visit [our website](http://vellum.ai) to learn more, [request early access](https://www.vellum.ai/landing-pages/request-early-access) if any of these problems resonate with you!
* Spread the word! Share this post if you know of others looking to build applications using LLMs who would likely benefit from our platform
* If you’re thinking about using LLMs and would like to discuss your use-case with us, please reach out through our website!
