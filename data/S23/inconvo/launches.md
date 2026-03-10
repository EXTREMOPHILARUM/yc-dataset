# Launches

## 📶 Inconvo: Open source AI agent for customer-facing chat-with-data

# TLDR;

Inconvo helps companies add chat-with-data agents to their product. We provide a platform for configuring agent rules and directions and a simple API endpoint to call them. We’re open source — check out our repository [here](https://github.com/inconvoai/inconvo). We also offer Inconvo cloud — check it out at [app.inconvo.ai](https://app.inconvo.ai)

[**https://www.youtube.com/watch?v=sbDTAbVG-WQ**](https://www.youtube.com/watch?v=sbDTAbVG-WQ)

# The problem:

Today, many product teams are under pressure to add “data agents” to their apps that connect to live databases and answer user questions.

Chat-with-data demos are easy. Shipping one to real customers is hard.

Most teams start with “LLM generates SQL + prompts,” then run into three issues:

* **Data safety:** you can’t reliably stop the model from pulling the wrong rows, crossing tenants, or selecting sensitive columns.
* **Business correctness:** metric definitions, allowed filters/enums, join paths, and formats get split across prompts which can confuse the model and drift over time.
* **Boundaries:** because the model can generate arbitrary SQL, “only allow these joins/filters/columns” becomes brittle after-the-fact validation.

The result is a second system of guardrails and checks just to make it safe to ship.

### The solution:

Inconvo flips the approach: constrain the agent up front instead of trying to rein it in after.

* **A semantic model as the contract:** define approved tables/columns, metrics, filters/enums, and join paths in one place.
* **Constrained query plans (not SQL):** the model outputs structured query plans which are validated against your semantic model before execution.
* **Automatic access rules:** tenant scoping and field restrictions are enforced on every request with deterministic code not prompts.

You can call your data agent from your application in just a few lines of code:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97668&key=user_uploads/1151062/a427ef4c-552e-4a7e-8675-671a08023bbf)

# Our ask:

Check out our repo and leave us a ⭐ on Github: [**https://github.com/inconvoai/inconvo**](https://github.com/inconvoai/inconvo)

Run Inconvo OSS locally `npx inconvo@latest dev` Or sign up to our cloud for free [**https://app.inconvo.ai**](https://app.inconvo.ai)

## Inconvo ⚟: Build MCP servers for SaaS customers

# **TL;DR**

Connect your existing database + auth provider and launch an MCP server for your customers in a few minutes.

[Watch me ship an MCP server and connect it to ChatGPT in 2.5 minutes](https://www.youtube.com/watch?v=4G41AQJZMO0)

# The Problem

A few days ago OpenAI announced Apps for ChatGPT — a new generation of apps you can chat with, right inside ChatGPT.

**An MCP server is the foundation of every Apps SDK integration**. It exposes tools that the model can call, enforces authentication, and packages the structured data plus component HTML that the ChatGPT client renders inline.

You can build an MCP server in one of two ways:

A)

_Load all of your API endpoints into the MCP server as tools and have the client decide which aggregation of tools it should use to fulfil user requests._

This approach **works well if you already have a highly composable API** designed for data analysis — concretely the API expresses any combination of filters, sorts, and transformations in a structured way.

However, most SaaS APIs are designed for record management, not data analysis or flexible retrieval. These APIs break down when presented with the wide array of potential user queries which come with a natural language input.

B)

_Build an AI agent attached to your database which takes in natural language and dynamically generates queries based on the input  — then attach the agent to your MCP as a tool._

This is **hard to build** because you need to handle conversation state, schema introspection, agent observability, multi-tenancy and query safety.

**Luckily, with Inconvo we offer AI data agents as a service so you don’t need to worry about any of that.**

Overall option B outperforms option A in power and flexibility, while eliminating the need for new API endpoints as user input cases grow.

# Our Solution

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94541&key=user_uploads/1151062/8f7eac8d-448f-4808-b34b-e3c7d0158a4f)

With Inconvo you can build a powerful AI agent for data analysis on top of your database and make it available to your users in your own app or the AI apps they already use like ChatGPT.

### How it works

1) Connect your existing database

2) Link your existing authentication and set user data permissions scopes

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94541&key=user_uploads/1151062/9e056431-135c-4066-b637-5f48d58cd1db)

3) Launch a remote authenticated MCP server in a few clicks, which can be linked easily by your users to ChatGPT etc.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94541&key=user_uploads/1151062/0a85474a-2589-4033-afab-f8920ed79b61)

### Inconvo handles the Details

We give you agent traces and logs for out of the box observability

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94541&key=user_uploads/1151062/33078fb7-d7bf-43ea-9da1-bd7af1651e73)

And a semantic layer so you can improve the data agents performance through context engineering without needing to write any extra code.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94541&key=user_uploads/1151062/19a1ea68-0999-4876-8cdb-8992d9bce1e7)


# Ready to ship MCP servers for your customers?

You can **try inconvo today for free** by visiting [**https://inconvo.com**](https://inconvo.com) and creating an account.

Or book a call: [**https://inconvo.com/demo**](https://inconvo.com/demo)

## Inconvo: AI agents for customer-facing analytics

# **TL;DR:**

Inconvo makes it easy to build and deploy AI analytics agents into your SaaS products, so your customers can quickly interact with their data.

# **Problem**

SaaS products typically offer dashboards and reports, which work for high-level metrics but are clunky for drill-downs and slow for ad-hoc questions. 

Modern users, shaped by tools like ChatGPT, now expect a similar degree of speed and flexibility when getting insights from their data. 

To meet these expectations, you need to ship an AI analytics agent, but these are painful to develop and manage.

# **Solution**

Inconvo is a platform built from the ground up for developers building AI agents for customer-facing analytics.

We make it simple for agents to access data by connecting to SQL databases.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93332&key=user_uploads/1151062/a56e965c-a51e-42ad-b63b-a8cdae08d317)

We provide a semantic model to create a layer that governs data access and defines business logic.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93332&key=user_uploads/1151062/8f7567c1-2926-4a1d-915d-5fb52444a9a6)

We support multi tenant databases by scoping the data an agent can see to specific tenants on a conversation basis.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93332&key=user_uploads/1151062/1ddec989-a3aa-4e3e-b2dd-0cc525fdc80b)

We offer a chat playground making it easy to test agents offline.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93332&key=user_uploads/1151062/edfcd6cf-e3b6-4157-9acf-6949259e1f6b)

We expose a developer-friendly API for easy integration and conversation logs to track user interactions. For observability we show a trace for each agent response, making agent behaviour easily debuggable.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93332&key=user_uploads/1151062/bd2f2ae8-a30f-4131-bb89-eac30a0a5821)

Here’s a deeper dive demo video for interested developers showing how we create and call an agent via the API in \~5 minutes.

https://youtu.be/4wlZL3XGWTQ

# Ask

If this problem is one you face, try us out!

[Book a demo](https://inconvo.com/demo) or [Sign up for free](https://auth.inconvo.ai/en/signup).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93332&key=user_uploads/1151062/14c14e6a-af3a-4ebf-a99f-79829304ec03)

## Inconvo: Ask-AI for customer-facing analytics

# **TLDR;**

Inconvo **makes it easy for developers to add Ask AI for customer-facing analytics** so that users can ask questions on their data in natural language. 

[Watch our demo!](https://youtu.be/1kpS48ifOAY)

With Inconvo, shipping AI-first analytics is easy. Just send a user question to our API, and it will respond with a chart, table, or text.

# **The Problem**

**Ask-AI for customer-facing analytics should deliver on its promise of being intelligent**, capable of answering dynamic user questions and not limited to a set of basic canned prompts.

But, **building genuinely intelligent Ask-AI for customer-facing analytics is hard.**

You need…

**An AI Agent** to dynamically retrieve relevant data that:

* Automatically connects to your database.
* Intelligently queries, joins, filters, and transforms data based on user questions.
* Responds with answers in human-readable formats (text, chart, table).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88017&key=user_uploads/1151062/2afe2960-8150-4296-95e6-9c522ac7381d)

**AI Evaluations** to measure you agent’s performance before and after deployment that:

* Allows you to build a dataset of conversation-answer pairs for evaluation.
* Assess your agent's ability to answer these evaluation pairs.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88017&key=user_uploads/1151062/0dec4f67-821f-46b1-af8a-bad3d9896a5a)

**A Semantic Layer** to ensure accurate data retrieval that:

* Maps user terminology to database field names.
* Facilitates the creation of computed fields and alternative field labels.

**Data Access Control** to restrict your AI agent’s database access that:

* Allows you to turn off access to whole tables or individual columns.
* Allows you to set if a table can be queried directly or only joined into.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88017&key=user_uploads/1151062/1b92ea04-f968-4ecb-b419-9495ae2b328b)

**Multi-tenancy support to** ensure results are scoped to the requestor’s access that is:

* Configurable on a per-request basis.
* Defined by you based on your existing data structures.

# **Our Solution**

**Inconvo provides a single API call to power genuinely intelligent Ask AI for customer-facing analytics.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88017&key=user_uploads/1151062/50ba0c22-7d2e-4ff4-bd4f-8ff457adb212)

Behind [this API call](https://inconvo.ai/docs/api-reference/ask), Inconvo handles all the hard problems of Ask AI for customer-facing analytics.

[Inconvo connects to your database](https://inconvo.ai/docs/guides/connect/) to automatically retrieve the right data to answer your users’ questions. Then, you’re in charge of presenting the API responses to your users in a way that fits your design.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88017&key=user_uploads/1151062/d9f04fae-8c25-4146-b940-f012a65b890c)

**Inconvo is purpose-built to overcome the challenges of Ask-AI for customer-facing analytics**, providing tools that handle multi-tenancy, database access control, [AI evaluation](https://inconvo.ai/docs/guides/evaluate/), and a semantic layer.

# **Our Asks**

**Share** - talk to your friends and colleagues about Inconvo.

**Connect** - ping [eoghan@inconvo.ai](mailto:eoghan@inconvo.ai) if you want to chat more or make an intro.

**Engage** - [book a demo call](https://inconvo.ai/request-demo).
