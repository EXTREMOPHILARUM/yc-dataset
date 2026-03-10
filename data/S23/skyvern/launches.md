# Launches

## Skyvern: Asking AI to build scrapers should be easy right?

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94724&key=user_uploads/1120458/6473b24c-3925-48bf-80c8-00430f81e5ef)

**TL;DR - We just gave Skyvern the ability to write and maintain its own code, making it 2.7x cheaper and 2.3x faster. Give it a prompt (or a series of prompts), and the AI will generate and maintain playwright code while it runs. Try out the via [Open Source](https://github.com/Skyvern-AI/Skyvern?ref=skyvern.com) or [Cloud](http://app.skyvern.com/?ref=skyvern.com)**

💡 **Recap: What is Skyvern?** It’s [an open source tool](https://github.com/Skyvern-AI/Skyvern?ref=skyvern.com) that helps companies automate things in the browser with AI. We use computer vision + LLMs to turn prompts into automations that run. We serve both technical and non-technical customers, and have helped them automate things like applying to jobs, fetching invoices or utility bills, filling out government forms, and purchase products from hundreds of different websites.

# **Asking AI to build scrapers should be easy right? Right??**

![](https://www.skyvern.com/blog/content/images/2025/10/image---2025-10-17T132106.418.png)

Some of you may remember our [Hackernews launch](https://news.ycombinator.com/item?id=39706004&ref=skyvern.com) from last year. All of the discussion circled around the same idea: “Building the automation is the hard part… we just want Skyvern to write the code”.

We agreed. Keeping the agent in the loop means invoking an expensive and non-deterministic LLM call on every run. If Skyvern could compile its reasoning into code and run that instead of keeping an LLM in the loop, automations would become **faster, cheaper, and more reliable.**

So we tried to teach Skyvern to do exactly that… but it turns out, asking AI to write code the same way you and I would wasn’t easy. We ran into two big problems:

1. Requirements for automations are ambiguous at best, and misleading at worst — even humans struggle to define them clearly
2. The internet is messy: drop-downs masquerade as textboxes, checkboxes that are always checked, and search bars that are secretly buttons.

Getting an agent to navigate that chaos, understand intent, and still produce maintainable code came through one major breakthrough: **reasoning models**.

Reasoning models unlock two important capabilities:

1. They [boosted the agent accuracy](https://www.skyvern.com/blog/web-bench-a-new-way-to-compare-ai-browser-agents/) enough for production use
2. They let the agent leverage its trajectory to write a script resembling something an engineer would write

# **This is too abstract. When does this matter?**

Before we dive into the solution, let’s look at a real-world example: Registering new companies for payroll with [Delaware.gov](http://Delaware.gov)

![](https://www.skyvern.com/blog/content/images/2025/10/image---2025-10-17T132100.688.png)

Here’s a simple prompt that reliably powers the workflow:

> _Your goal is to fill out the EIN registration form. Fill out the form until you're at the form confirmation page with a summary of all information. Your goal is complete once you see a summary of all of the information._

ein_info: {{ein_info}}

Writing deterministic code should be easy right?

Here’s what a naive AI Generated implementation looks like:

![](https://www.skyvern.com/blog/content/images/2025/10/image-1.png)

And here’s where it falls apart almost immediately.

1. Coupled interactions. Choices on this form aren’t independent. Sometimes radio buttons are linked together, but aren’t represented as such in the DOM. Other times, different buttons trigger different follow-up questions, so a static script breaks as soon as you pick something unexpected.

![](https://www.skyvern.com/blog/content/images/2025/10/image---2025-10-17T132055.697.png)

**Random failures.** Government websites love to go down at night, change field layouts between sessions, or throw you a “try again later” page mid-run.

![](https://www.skyvern.com/blog/content/images/2025/10/image---2025-10-17T132051.371.png)

### **Coupled interactions**

Consider the radio button example above. Any seasoned developer would know that these legal structures are linked together. You’d instinctively model them as a finite set of entity types, and create a tree-like script that branches into different paths based on the input.

But that abstraction doesn’t exist for an agent. To agents like Skyvern, this is just a list of buttons. The relationship between the users’ input and the available set of legal structures doesn’t exist ahead of time — it must be discovered at runtime.

The agent has to infer, from the DOM and the page transitions, which choices lead where.

### **Random non-deterministic failures**

Agents shine when things don’t go as planned. We don’t want to hard code every single edge case when compiling an agent into a deterministic script.. because we’re back to writing brittle scripts. Instead, we want to leverage agents for these situations.

Take this government form: Delaware’s portal is unavailable at night or over the weekend. Or sometimes, it’ll require you to call the IRS or sending them a fax / mail to proceed with the form. You want some intelligence in the loop to handle these scenarios gracefully.

# **So.. how can you codify this in an agent?**

After a few runs like the ones above, we realized “have the agent write code” wasn’t enough. We needed to copy how developers actually work: figure out the flow, add logic where it breaks, and bake that behavior into Skyvern.

So we split its job into two:

1. Explore mode, where the agent learns how to navigate a website for a given flow, generating any metadata necessary for it to operate in subsequent runs

Replay mode, it compiles those learnings into deterministic Playwright and runs fast and cheap, only falling back to the agent when something new or weird happens

![](https://www.skyvern.com/blog/content/images/2025/10/image---2025-10-17T132046.901.png)

### **Explore once: get the agents’ trajectory**

Let’s start with a plain prompt for Skyvern. The `ein_info` field is just a json blob with all of a company’s metadata (entity type, responsible party, etc). The goal of this explore run isn’t to finish fast, it’s to learn the flow and record a trajectory we can compile later.

> _Go to [https://sa.www4.irs.gov/modiein/individual/index.jsp](https://sa.www4.irs.gov/modiein/individual/index.jsp)\
> and generate an SS4 with the following information: {{ ein_info }}_

### **Step 1: generate a naive script**

From that trajectory, the agent can spit out a basic Playwright script. It runs, but it’s brittle—no context, no fallbacks:

![](https://www.skyvern.com/blog/content/images/2025/10/image-2.png)

**What’s missing:** it doesn’t know _why_ it’s clicking “Corporation,” what should appear next, or how to recover if the DOM shifts (or the portal is down). That’s the gap we close in the next section (intent metadata + deterministic replay with targeted fallbacks).

### **Step 2: Ask the agent to write down its intention so we can re-use it later**

Exploration gives us a working script, but it’s brittle because it only knows _what_ to click, not _why_. The fix was to capture **intents** to every action so the run can recover when the page shifts.

![](https://www.skyvern.com/blog/content/images/2025/10/image---2025-10-17T132041.611.png)

To get to this intention, we generate 2 additional parameters at runtime: `user_detail_query` and `user_detail_answer` to capture the **essence** of the action (beyond the interaction itself)

![](https://www.skyvern.com/blog/content/images/2025/10/image-3.png)

Then, we pass it through another LLM call to reverse engineer the action into the following:

![](https://www.skyvern.com/blog/content/images/2025/10/image-4.png)

If this fails at replay time, we don’t blindly guess a new selector—we reuse the **intention** to recover:

1. Try an alternate selector for the same intention (looser match, nearby label, aria text)
2. If the flow changed, ask the model **once**: “How do I ‘Select legal structure: Corporation’ on this page?”
3. If we hit a dead end (downtime/error), fallback to the original prompt to decide what to do next

At this point, we have generated code that looks like this:

![](https://www.skyvern.com/blog/content/images/2025/10/image-5.png)

### **Step 3 - Run it on the cheap**

Now that we have a plan and a fallback in place, subsequent runs are all using plain playwright — no LLM in the loop.

We benchmarked this across our customers and saw:

* Average automation run time goes from 278.95s → 119.92s (2.3x faster)
* Average run cost goes from $0.11 → $0.04 (2.7x cheaper)
* And maybe more important than either: **runs are now deterministic.**

![](https://www.skyvern.com/blog/content/images/2025/10/Screenshot-2025-10-16-at-14.18.17.png)

![](https://www.skyvern.com/blog/content/images/2025/10/Screenshot-2025-10-16-at-14.18.07-1.png)

# **How is this being used in the wild?**

Skyvern’s “explore → replay” pattern is already running quietly inside a bunch of workflows that used to require brittle, human-maintained scripts. A few examples:

1. **Invoice Downloading**

Agents log into vendor or utility portals with 1000s of different accounts, navigate to the right billing period, and pull invoices. When layouts or date filters change, the intent metadata lets them recover automatically instead of failing.

2. **Purchasing**

Teams use it to automate repeat purchases — think renewing software licenses or buying supplies through the same vendor dashboard each month. The first run learns the checkout path, the fallbacks handle the variety of products, and the replays run deterministically, flagging if a price or SKU changes.

3. **Data Extraction from Legacy Systems**

Skyvern navigates authenticated dashboards, scrapes tables or PDFs, and pushes the structured output into into a database via Webhooks. If the DOM shifts, Skyvern reuses the same intention (“extract transaction rows”) to remap selectors.

4. **Government Form Filling**

From payroll registration to business license renewals, Skyvern handles long, multi-step government forms that occasionally break static scripts. Explore mode figures out the flow once replay mode repeats it safely.

## **What’s next? Is it perfect today?**

Not quite. The architecture works well, but there are still a few places where we can make it smarter and cheaper:

1. **Analyze groups of runs when generating code**.

Right now, we don’t aggregate insights across failures. Each replay fixes itself in isolation. If we could analyze _many_ runs together, spotting which selectors break, which flows diverge, we could automatically generalize better code and reduce the need for fallbacks. That’s especially useful for workflows that branch like trees (different inputs → different paths).

2. **Cache data extractions**.

During data extraction, we still rely on the LLM to “read” the page each time because many of our users want to both extract and summarize information at the same time. For example, if you ask Skyvern to pull the summaries of the top five posts on Hacker News, it currently parses the DOM from scratch. We’d like to trace _how_ the model found those elements (which selectors, which substrings) and reuse that mapping. That alone could make scraping and data-harvesting flows an order of magnitude cheaper.

3. **Expose everything through the SDK.**

We think it will be valuable for developers using the Skyvern SDK to auto-generate these scripts for any ai actions / workflows they run, and use them automatically for subsequent runs. It currently requires a Skyvern server running, but soon it will be the default behaviour.

## **Give it a try!**

Run it via our [Skyvern Open Source](https://github.com/Skyvern-AI/Skyvern?ref=skyvern.com) or [Skyvern Cloud](http://app.skyvern.com/?ref=skyvern.com) versions and let us know what you think!

## 📊 Web Bench - A new way to compare AI Browser Agents

**TL;DR:** [Web Bench](https://www.webbench.ai) is a new dataset to evaluate web browsing agents that consists of 5,750 tasks on 452 different websites, with [2,454 tasks being open sourced.](https://github.com/Halluminate/WebBench/tree/main) Anthropic Sonnet 3.7 CUA is the current SOTA, with the detailed [results here](https://eval.skyvern.com/?evaluation_target=skyvern_final_eval_skyvern_2_0&page=1).

Over the past few months, Web Browsing agents such as [Skyvern](https://www.skyvern.com), [Browser-use](https://browser-use.com/) and [OpenAI's Operator (CUA)](https://operator.chatgpt.com/) have taken the world by storm. These agents have been used in production for a variety of tasks, from helping people apply to jobs, downloading invoices, and even doing SS4 filings for newly incorporated companies.

![](https://blog.skyvern.com/content/images/2025/05/onlayer-gif.gif)

_Skyvern attempting to purchase a product_

![](https://blog.skyvern.com/content/images/2025/05/irs_demo.gif)

_Skyvern attempting to fill out the IRS form_

Most agents report state of the art performance, but we find that browser agents still struggle with a wide variety of tasks, particularly ones involving authentication, form filling and file downloading.

This is because the standard benchmark today ([WebVoyager](https://arxiv.org/abs/2401.13919)) focuses on read-heavy tasks and consists of **only** **643 tasks across only** **15 websites (out of 1.1 billion possible websites!).** While a great starting point, the benchmark does not capture the internet’s adversarial nature towards browser automation and the difficulty of tasks involving mutating of data on a website.

![](https://blog.skyvern.com/content/images/2025/05/chase3-ezgif.com-video-to-gif-converter--1-.gif)

_Can’t access [chase.com](http://chase.com)_

![](https://blog.skyvern.com/content/images/2025/05/2025-05-08T02_12_10.137717_a_390786750312029848_recording-ezgif.com-video-to-gif-converter--1-.gif)

_Can’t close a pop-up dialog_

As a result, we partnered with [Halluminate](https://www.halluminate.ai) and created a new benchmark to better quantify these failures. Our goal was to create a new consistent measurement system for AI Web Agents by expanding the foundations created by [WebVoyager](https://arxiv.org/abs/2401.13919) by:

1. Expanding the number of websites from 15 → 452, and tasks from 642 -&gt; 5,750 to test agent performance on a wider variety of websites
2. Introduce the concept of READ vs WRITE tasks
3. READ tasks involve navigating websites and fetching data
   * WRITE tasks involve entering data, downloading files, logging in, solving 2FA, etc, and were not well represented in the WebVoyager dataset
4. Measure the impact of browser infrastructure (eg, access the websites, solve captchas, not crash, etc)

We’re excited to announce Web Bench, a new dataset to evaluate web browsing agents that consists of 5,750 tasks on 452 different websites, with [2,454 tasks being open sourced.](https://github.com/Halluminate/WebBench/tree/main)

# Results TL;DR

![](https://blog.skyvern.com/content/images/2025/05/Screenshot-2025-05-26-at-6.13.00---PM--1-.png)

* All agents performed surprisingly poorly on write-heavy tasks (eg, logging in, filling out forms, downloading files), which implies that this is the area for the highest opportunity for growth
* Skyvern 2.0 has the best performance for tasks in this category

![](https://blog.skyvern.com/content/images/2025/05/Screenshot-2025-05-25-at-11.54.34---AM.png)

* Agent performance for read-heavy tasks (eg, extracting information out of websites) was better than we expected
* Anthropic’s CUA had the highest performance
* The [entire run is **open source**](https://eval.skyvern.com/) and can be viewed to see the specific performance of each task

# Dataset Creation

![](https://blog.skyvern.com/content/images/2025/05/Screenshot-2025-05-25-at-11.49.12---AM.png)

The 452 websites are distributed across 17 primary categories. We sampled the benchmark websites from the [top 1000 websites in the world](https://dataforseo.com/free-seo-stats/top-1000-websites) measured by web traffic. We then cleaned this dataset of sites by removing:

* repeat domains
* sites without English translations
* sites blocked by paywall

# Results

## Initial conditions

* We ran OpenAI Operator with a human in the loop to establish a baseline for performance
* We used consistent browser infrastructure (Skyvern’s infrastructure) when comparing the API-only models without a runtime to eliminate variables
* We also ran Skyvern 2.0 on Browserbase to compare the impact of infrastructure, but found (surprisingly) that Skyvern’s infrastructure was able to reliably access more websites and encountered fewer anti-bot issues during navigation
* Each agent was allowed a max of 50 steps per execution
* Each result was validated by a human in the loop to assert evaluation data quality

## Accuracy (Overall)

![](https://blog.skyvern.com/content/images/2025/05/Screenshot-2025-05-25-at-11.53.34---AM--1-.png)

These results were a little bit surprising, so we decided to cut the data along 2 dimensions to understand where agents may falter:

1. Read-only tasks (ie, extracting visible data from a particular website)
2. Write heavy tasks (ie, logging into websites, filling out forms, downloading files)

## Accuracy (Read-only tasks)

![](https://blog.skyvern.com/content/images/2025/05/Screenshot-2025-05-25-at-11.54.34---AM--1-.png)

Read-only tasks constitute tasks that involve agents going to different websites and navigating the sitemap until a particular answer/state has been found.

Unsurprisingly, these results matched the WebVoyager dataset more closely, as the WebVoyager dataset was largely curated to help agents navigate websites and answer questions.

The biggest 2 sources of failures for read-heavy tasks are:

* Navigation Issues (cannot figure out how to navigate a page, can’t solve popups)
* Information extraction issues (doesn’t pull the correct information)

## Accuracy (Write-heavy tasks)

![](https://blog.skyvern.com/content/images/2025/05/Screenshot-2025-05-26-at-6.13.00---PM--2-.png)

Tasks involving:

* filling out forms
* logging in
* solving 2FA
* downloading files

had a much lower pass rate across the board.

Digging a bit deeper into the failures, there were two culprits for the failures that popped up:

* Incomplete execution (hallucinating that it’s achieved the goal when it has not)
* Unable to identify the correct element to interact with (eg can’t close a popup dialog)

![](https://blog.skyvern.com/content/images/2025/05/ezgif.com-speed-1.gif)

_Can’t close subscription pop-up_

![](https://blog.skyvern.com/content/images/2025/05/error2-ezgif.com-speed-1.gif)

_Unable to find and click coupon buttons_

These issues manifest as agents making adverse changes when filling out forms, or optimistically assuming that clicking a “Submit” button completes the task, when in reality, a captcha appeared that now needs to be solved.

This issue is very similar to the phenomenon observed in coding agents, where smarter models try to “overhelp” with code changes by either making changes to unrelated parts of the codebase or repeatedly suggesting incorrect things because they’re missing some important context.

## Agent Failure Modes - Deepdive

![](https://blog.skyvern.com/content/images/2025/05/Screenshot-2025-05-25-at-11.56.30---AM.png)

Digging deeper, we were able to qualify the overall failures into two buckets:

1. Agent Failures (eg, Agents hallucinated/made poor decisions or didn’t interact with important elements)
2. Infrastructure failures (eg, Agent can’t access the website, solve a captcha to log in)

### Agent issues

The 4 biggest categories of agent errors are:

* Navigation Issue (cannot figure out how to navigate a page, can’t solve popups)
* Incomplete execution (hallucinating that it’s achieved the goal when it has not)
* Time-outs (exceeds step limits)
* Information extraction issue (doesn’t pull the correct information)

### **Infrastructure issues**

The 3 biggest categories of infrastructure issues are:

* Proxy (Failed to access website/website blocked)
* Captcha (Verification required to proceed and the infrastructure is unable to solve it)
* Login/Authentication (Google Auth detecting you’re a bot)

These findings imply that the browser infrastructure powering the agents is equally as important as the quality of the agent itself.

# Other interesting characteristics

While accuracy is the most important characteristic of a web browsing agent, there is also a desire to get “faster” and “cheaper” agents.

Fast and cheap agents can be characterized by tracking the following metrics:

1. Runtime duration
2. Number of steps

While the right pricing model for browser agents hasn’t emerged yet, this data gives an important insight into whether pricing per hour (common amongst hosted browsers + older robotic process automation) and pricing per step (common amongst computer use APIs) is the right methodology.

## Agent Runtime Duration

![](https://blog.skyvern.com/content/images/2025/05/Screenshot-2025-05-28-at-10.14.41---AM.png)

This metric is important for a few latency-sensitive market segments/situations:

1. Copilot-like products where a human is supervising 1 or many agents executing in parallel
2. Phone agents referencing information / doing real-time lookups while a user is talking
3. Websites aggregating information in real-time to show to the user(e.g., looking up flight or domain name availability)

## Steps

![](https://blog.skyvern.com/content/images/2025/05/Screenshot-2025-05-25-at-10.47.56---PM.png)

Most web browsing agents’ costs scale with the number of steps (i.e., page scans) required to complete a specific task.

Agents may use a varied number of steps for a few reasons:

1. Most agents use different architectures to batch actions together to minimize the number of steps
2. Agents eager to solve the problem may use a lot of steps in error situations to try to independently resolve their issues (e.g., chatting with support for solutions instead of terminating early)
3. Agents using pessimistic approaches to reduce hallucinations may invalidate batches of actions whenever the website changes after a particular action (i.e., filling in an address field might invalidate the action plan for the rest of the page)

# Next Steps

* We intend to benchmark [Claude 4](https://www.anthropic.com/news/claude-4), [Operator O3](https://openai.com/index/o3-o4-mini-system-card-addendum-operator-o3/), [UI-TARs](https://github.com/bytedance/UI-TARS), and [Mariner API](https://deepmind.google/models/project-mariner/)
* We intend to expand the benchmark to cover more categories of websites beyond the top 1000 websites in the world
* We intend to expand this dataset to include other languages to assert multi-lingual browser agent performance

# FAQ

### Why not include a bigger cohort of websites?

The goal of the first version of Web Bench was to start with a reasonably large number of websites + tasks.

The next few versions will expand: (1) the number of websites encompassed by this benchmark, (2) the language of websites, and (3) the categories of websites

### Why were only a subset of vendors benchmarked?

The overall cost to run this benchmark was approximately $3,000 per agent for human evaluations. This cost is high enough to be prohibitive of testing every single agent on the market.

The halluminate team plans to release an open-source automated evaluation harness to allow teams to self-serve testing against [Web Bench](https://www.webbench.ai). We leave this for future work.

If you’d like to submit benchmark results for your own agent, please [contact the Halluminate team](mailto:jerry@halluminate.ai)

### Where can I read the technical deepdive?

For a comprehensive technical debrief on the dataset creation and evaluation methodology, check out the Halluminate team writeup [here](https://halluminate.ai/blog/benchmark).

### Did anything funny happen along the way?

Yes.

We had examples of Skyvern chatting with GitHub’s AI Support bot

![](https://blog.skyvern.com/content/images/2025/05/image--67-.png)

Browser Use googled how to evade Cloudflare captchas

![](https://blog.skyvern.com/content/images/2025/05/image--68-.png)

## 🐉 Skyvern MCP Server: let agents control your browser

We were playing around with MCPs over the weekend and thought it would be cool to build an MCP that lets Claude / Cursor / Windsurf control your browser: <https://github.com/Skyvern-AI/skyvern/tree/main/integrations/mcp>

Just for context, we’re building Skyvern, an open-source AI Agent that can control and interact with browsers using prompts, similar to OpenAI’s Operator.

The MCP Server can:

* This allows Claude to navigate to docs websites/stack overflow and look up information like the top posts on hackernews

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89234&key=user_uploads/1120458/9a0259b8-ebb7-44c4-9f4d-a881c31c8d10)

* This allows Cursor to apply for jobs, fill out contact forms, log in and download files, etc.

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=89234&key=user_uploads/1120458/f9c936a8-88de-47cc-8209-7983754fcb8a)

* Connect Windsurf to take over your Chrome while running Skyvern in “local” mode

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89234&key=user_uploads/1120458/40ca033c-fa32-4c7f-bda0-7cd072ae9212)

We built this mostly for fun, but we can see this being integrated into AI agents to give them custom access to browsers and execute complex tasks like booking appointments, downloading your electricity statements, looking up freight shipment information, etc.

## Skyvern 2.0 - State-of-the-art web navigation with 85.8% on WebVoyager Eval

We’ve been working hard, cooking up something new to share with you all!

Skyvern 2.0 **scored state-of-the-art 85.85%** on the WebVoyager Eval.

This is the best-in-class performance of all WebAgents, giving advanced closed-source web agents like Google Mariner a run for their money.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=86895&key=user_uploads/1120458/4f04949f-e01d-42cb-b568-a2460f7ac7f5)

### TL;DR

* **Real-World Tests:** We ran all of the tests in Skyvern Cloud to get a better representation of autonomous browser operations (ie, they didn’t run on any local machines)
* **Open-Sourced Results:** All of the runs can be [seen here](https://eval.skyvern.com/) through our UI.
* **We’re just getting started**. Try [Skyvern Cloud](https://app.skyvern.com/) or [Skyvern Open Source](https://github.com/Skyvern-AI/Skyvern) out for yourself and see Skyvern in action!

## Agent Architecture

Achieving this SOTA result required expanding Skyvern’s original architecture. Skyvern 1.0 involved a single prompt operating in a loop both making decisions and taking actions on a website. This approach was a good starting point but scored \~45% on the WebVoyager benchmark because it had insufficient memory of previous actions and could not do complex reasoning.

To solve this problem, we created a self-reflection feedback loop within Skyvern. This resulted in 2 main changes:

1. We added a “Planner” phase, which could decompose very complex objectives down into smaller achievable goals
2. This allowed Skyvern to have a working memory of things it had completed and things that were still waiting to be finished
   * This allows Skyvern to work with long, complex prompts without increasing the hallucination rate
3. We added a “Validator” phase, which confirmed whether or not the original goals the “Planner” generates are successfully completed
4. This acts as a supervisor function to confirm that the Task executor is achieving its objectives as expected and report any errors/tweaks back to the Planner so it can make adjustments in real-time as needed

![](https://blog.skyvern.com/content/images/2025/01/architecture.png)

## Test Setup

All tests were run in [Skyvern Cloud](https://app.skyvern.com/) with an **async cloud browser** and used a combination of GPT-4o and GPT-4o-mini as the primary decision-making LLMs. The goal of this test is to assert real-world quality — the quality represented by this benchmark is the same as what you would experience with [Skyvern](https://app.skyvern.com/)’s browsers running asynchronously.

💡 **Why is this important?** Most benchmarks are run on local browsers with a relatively safe IP address and an impressive browser fingerprint. This is not representative of how Autonomous agents will run in the cloud, and we wanted our benchmark to represent how agents would behave in production

In addition to the above, we’ve made a few minor tweaks to the dataset to bring it up to date:

1. We’ve removed 8 tasks from the dataset because the results are no longer valid. For example, one of the tasks asked to go to [apple.com](http://apple.com) and check when the Apple Vision Pro will be released — in 2025, it’s already been released and forgotten
2. Many of the flight/hotel booking tasks referenced old dates. We updated both the prompt and the answer to more modern dates for this evaluation

🔍 **For the curious**:

The full dataset can be seen here: <https://github.com/Skyvern-AI/skyvern/tree/main/evaluation/datasets>

The full list of modifications can be seen here: <https://github.com/Skyvern-AI/skyvern/pull/1576/commits/60dc48f4cf3b113ff1850e5267a197c84254edf1>

## Test Results

We’re doing something out of the ordinary. In addition to the results, we’re making our entire benchmark run public.

💡 **Why is this important?** Most benchmarks are run behind closed doors, with impressive results being published without any accompanying material to verify the results. This makes it hard to understand how things like hallucinations or website drift over time play an effect on agent performance

We believe this isn’t aligned with our open source mission, and have decided to publish the entire eval results to the public.

📊 All individual run results can be seen here: <https://eval.skyvern.com>

🔍 The entire Eval dataset can be seen here: <https://github.com/Skyvern-AI/skyvern/tree/main/evaluation/datasets>

## Limitations of the WebVoyager benchmark

The WebVoyager benchmark is a comprehensive benchmark testing a variety of prompts on 15 different websites. While this acts as a good first step in testing Web agents, this only captures 15 hand-picked websites of the millions of active websites on the internet.

We think there is tremendous opportunity here to better evaluate web agents against one another with a more comprehensive benchmark similar to SWE-Bench.

## What’s on the horizon

Browser automation is still a nascent space with tons of room for improvement. While we’ve achieved a major milestone in agent performance, a few important issues are next to be solved:

1. Can we improve Skyvern’s reasoning to operate efficiently in situations with more uncertainty? Examples include vague prompts, ambiguous or highly complex websites/tools, websites with extremely poor UX (legacy portals)
2. Can we give Skyvern access to more tools so it can effectively log into websites, make purchases, and behave more like a human?
3. Can we have Skyvern better memorize things it has already done in the past so it can do them again at a lower price point?

## References

* [Google Mariner Report](https://deepmind.google/technologies/project-mariner/)
* [Claude Computer Use Report](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
* [WebVoyager Report](https://arxiv.org/html/2401.13919v4)
* [WILBUR Report](https://arxiv.org/html/2404.05902v1)
* [AgentE Report](https://arxiv.org/html/2407.13032v1)
* [HCompany Report](https://www.hcompany.ai/blog/a-research-update)

## 🐉 Skyvern's Contact Form Agent: Automate contact form submissions with AI

Companies use [Skyvern](https://www.skyvern.com/) to automate browser-based workflows, doing tasks like form-filling, invoice downloading, and more. One emerging use case for Skyvern has been navigating to thousands of different websites and filling out contact forms... to scale a new untapped outbound channel.

And this strategy blew our minds. Why:

1. Companies with contact forms often, guess what, want to be contacted
2. Contact form submissions often go to a specific team dedicated to help with inquiries
3. You avoid all of the craziness that comes with setting up email infrastructure: buying up domains, warming inboxes, worrying about bounce rates and other email nuisances
4. You can send as many as you want whenever you want—forget limiting the number you send per day to increase deliverability

The demand and success of this use case led us to create a dedicated agent tailored to it: Skyvern Contact Forms. And this is why I’m here, to share this sick outbound strategy and let you know we can help :)

Try it out at [**https://app.skyvern.com/forms**](https://app.skyvern.com/forms), let us know what you think!

Like what you see and want bulk pricing? [**I’d love to chat.**](https://meetings.hubspot.com/skyvern/demo)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=86198&key=user_uploads/1120458/2e37309e-035e-41cd-b89a-c8552a5019d6)

## 🐉 Skyvern Cloud - Open source AI Agent to automate browser based workflows

### TL;DR

[Skyvern](https://skyvern.com/) helps companies automate browser-based workflows using AI. We provide a simple API endpoint to fully automate manual workflows, replacing brittle or unreliable scripts. We’re open source — check out [our repository here](https://github.com/Skyvern-AI/Skyvern). **We just launched Skyvern Cloud — check it out at **[**app.skyvern.com**](https://app.skyvern.com)**.**

**—**

### 🧙‍♂️🐉 Skip the boring explanation, show me the magic!

**We have good news!** We just launched Skyvern Cloud. You can go to [app.skyvern.com](http://app.skyvern.com) and try playing around with it! You’ll get $5 of credit when signing up and setting up a payment method

Here’s an example of it filling out the job application form and applying to Lever’s job demo website:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81634&key=user_uploads/1120458/b3e666b8-5e36-4e7e-91ac-1120de55cd39)

### 🤔 What are browser workflows?

Most companies we’ve talked to have manual or semi-automated workflows that support their core product. Many of these workflows started manually as companies were getting off the ground, [doing things that don’t scale](https://paulgraham.com/ds.html), and evolved to occupy a larger amount of human capital or automated with unreliable scripts.

**Example 1 — Downloading invoices on a large number of websites**

Let’s say it’s the end of the month, and your accountant is hounding you for invoices for all your transactions this month. Traditionally, you would have to log into each portal and download it yourself. Skyvern can help automate this for you! **PS: If you’d like to automate a complex flow like this, we’d [love to help get you set up.](https://meetings.hubspot.com/suchintan)**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81634&key=user_uploads/1120458/49e1d569-5a46-4728-a3ec-6a0a4d8c40aa)

**Example 2 — Filling out forms + uploading documents on Government websites**

Let’s say you’re an accounting company or a law firm, and you want to help your clients get set up for Payroll in California — you wouldn’t want to go get registered for EDD manually for each potential customer.. and in each state! Call in a favor from Skyvern to help automate this.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81634&key=user_uploads/1120458/66682edb-bdc4-4a03-b157-235501356bfc)

**Example 3 — Automating materials procurement from commerce websites**

Let’s say you’re a B2B marketplace for car parts, and your users submit orders from multiple vendors with you. A subset of vendors you work with don’t support ordering via an API, so you have a human in the loop to transact orders for those vendors. Here’s an example of Skyvern navigating to [finditparts.com](http://finditparts.com/) and ordering an airbag — all via an API call!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81634&key=user_uploads/1120458/f4630123-b7d1-4fff-aedb-31dd3ea11f05)

**Example 4 —** **Completing dynamic multi-step workflows**

Let’s say that you’re trying to automate complex workflows, such as generating insurance quotes. Skyvern is able to navigate each step until its specified goal is achieved — even if the steps change depending on the user’s situation. Here’s an example of Skyvern navigating to [Geico.com](http://geico.com/) and generating an auto insurance quote with your personalized information.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81634&key=user_uploads/1120458/f800fef8-1a6d-4345-ba5a-043a154ad488)

### 🤩 How does it work??

Skyvern uses LLMs to become an AI Agent capable of interacting with websites like you or I would — all via a simple API call.

Traditional approaches required writing custom scripts for websites, often relying on [DOM parsing](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) and [XPath-](https://en.wikipedia.org/wiki/XPath)based interactions, which would break whenever the website layouts changed.

Skyvern’s prompt → automation breaks these constraints and relies on multi-modal LLMs to parse items in the viewport and interact with them the way a human would.

This approach gives us a few advantages:

1. Skyvern can take a single prompt (i.e., “Download an invoice from the order history page”) and repeat it across a large number of similar websites. This would traditionally require one script per website — making tackling the long tail of website interactions very challenging
2. Skyvern is able to operate on websites it’s never seen before, as it’s able to map visual elements to actions necessary to complete a workflow without any customized code
3. Skyvern is resistant to website layout changes, as there are no pre-determined XPaths or other selectors our system is looking for while trying to navigate
4. We’re able to circumvent or navigate through many bot detection methods, as many of them rely on looking for outlier behavior
5. We rely on LLMs to reason through interactions to make sure we can cover complex situations. Examples include:
   * If you wanted to get an auto insurance quote from Geico, the answer to a common question, “Were you eligible to drive at 18?” could be inferred from the driver receiving their license at age 16
   * If you were doing competitor analysis, it’s understanding that an Arnold Palmer 22 oz can at 7/11 is almost definitely the same product as a 23 oz can at Gopuff (even though the sizes are slightly different, which could be a rounding error!)

### 😮 And you’re open source?

Yes! You can [check out our code here](https://github.com/Skyvern-AI/Skyvern). We’re open source for two big reasons:

1. It allows developers to be able to look at, understand, and dive deep into Skyvern’s implementation details to (1) expand their capabilities by adding support for new functionality and (2) decode why they’re doing what they’re doing.
2. It allows security-minded enterprises to escape “security theater” and keep data on-prem by self-hosting Skyvern.
   1. If this is at all interesting to you, [let’s chat](https://meetings.hubspot.com/suchintan?uuid=9cb375c0-cb2c-4900-b22d-f52baa74dfb2).

### Our Ask

Do you have any complex workflows that you’d love to automate? We’d love to chat! Shoot me an email at [suchintan@skyvern.com](mailto:suchintan@skyvern.com) or grab some time via [my calendar.](https://meetings.hubspot.com/suchintan)

## 🐉 Skyvern - Automate Browser-based workflows with AI

### TL;DR

Skyvern helps companies automate browser-based workflows using LLMs and computer vision. We provide a simple API endpoint to fully automate manual workflows, replacing brittle or unreliable scripts.

### 🤔 What are browser workflows?

Most companies we’ve talked to have manual or semi-automated workflows that support their core product. Many of these workflows started manually as companies were getting off the ground, [doing things that don’t scale](https://paulgraham.com/ds.html), and evolved to occupy a larger amount of human capital or automated with unreliable scripts.

**Example 1 — Automating materials procurement from commerce websites**

Let’s say you’re a B2B marketplace for car parts, and your users submit orders from multiple vendors with you. A subset of vendors you work with don’t support ordering via an API, so you have a human in the loop to transact orders for those vendors. Here’s an example of Skyvern navigating to [finditparts.com](http://finditparts.com) and ordering an airbag — all via an API call!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77665&key=user_uploads/1120458/055a1d70-8ed2-428d-8104-740f7632d3e7)

**Example 2 —** **Completing complex multi-step workflows**

Let’s say you’re trying to automate complex workflows such as generating insurance quotes. Skyvern can navigate each step until its specified goal is achieved — even if the steps change depending on the user’s situation. Here’s an example of Skyvern navigating to [Geico.com](http://Geico.com) and generating an auto insurance quote with your personalized information.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77665&key=user_uploads/1120458/747160ae-eb91-48c0-977d-830074a5b93b)

### 🤩 How does it work??

Our focus is bringing stability to browser-based workflows. We leverage LLMs to create an AI Agent capable of interacting with websites like you or I would — all via a simple API call.

Traditional approaches required writing custom scripts for websites, often relying on [DOM parsing](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) and [XPath-](https://en.wikipedia.org/wiki/XPath)based interactions which would break whenever the website layouts changed.

Skyvern operates like a human — increasing reliability by not relying on fragile scripts, instead relying on computer vision to parse items in the viewport and interact with them the way a human would.

This approach gives us a few advantages:

1. Skyvern can operate on websites it’s never seen before, as it’s able to map visual elements to actions necessary to complete a workflow, without any customized code
2. Skyvern is resistant to website layout changes, as there are no pre-determined XPaths or other selectors our system is looking for while trying to navigate
3. We’re able to circumvent or navigate through many bot detection methods as many of them rely on allowing people to access the websites
4. We rely on LLMs to reason through interactions to ensure we can cover complex situations. Examples include:
   * If you wanted to get an auto insurance quote from Geico, the answer to a common question “Were you eligible to drive at 18?” could be inferred from the driver receiving their license at age 16
   * If you were doing competitor analysis, it’s understanding that an Arnold Palmer 22 oz can at 7/11 is almost definitely the same product as a 23 oz can at Gopuff (even though the sizes are slightly different, which could be a rounding error!)

### Our Ask

Do you have any complex workflows that you’d love to automate? Were you [doing things that don’t scale](https://paulgraham.com/ds.html) that you now need to scale? We’d love to chat! Shoot me an email at [suchintan@skyvern.com](mailto:suchintan@skyvern.com) or grab some time via [my calendar.](https://meetings.hubspot.com/suchintan)

## 🐉 Wyvern AI - Increase revenue in marketplaces with better product ranking

**TL;DR:** [Wyvern.ai](https://www.wyvern.ai?utm_source=yc&utm_medium=yc_launch_email&utm_campaign=launch_yc&utm_id=10) is a machine learning platform for marketplaces to help them optimize their product ranking. We do this by providing an API that’s integrated with their product catalog, that optimizes product ranking based on factors such as popularity, relevance, and personalization. In addition, we also provide a framework where customers can fine-tune their product ranking models with custom insights and tailor them to their business. We built this exact platform before, and it unlocked over $100M of value.

## 💸 Product Ranking: **Unleashing Growth Potential**

Marketplaces, such as Amazon, eBay, or Etsy, often have millions of products listed by various sellers, making it crucial to determine how to present these products to users effectively. These companies have teams of data scientists dedicated to improving the quality of product ranking, factoring in things like personalization (ie individual user preferences), relevance, and general product popularity.

Our experience building Faire and Gopuff’s machine learning platform highlighted the value that product ranking derives for the business. Through successive iterations of machine learning models, we witnessed impacts exceeding 10% (equivalent to over $100 million) for these businesses.

A notable portion of these impactful iterations involved providing machine learning models with access to unique insights into user behaviour. For instance, at Faire, gaining a better understanding of what products their retailers stocked in their stores enabled tailoring the shopping experience to suit each store's distinct characteristics.

Other larger marketplaces had their own insights. At eBay, incorporating buyer-seller shipping logistics information into their product ranking models produced notable improvements. Similarly, at Etsy, the users' initial interactions with the site indicate their shopping intention, allowing their product ranking models to transform the entire homepage to deliver a personalized experience.

## 💣 Challenges to navigate along the way

While larger marketplaces have the leverage to iterate on their product ranking, smaller marketplaces tend to buy off-the-shelf solutions, allowing them to bootstrap and search for product-market-fit.

Once a marketplace establishes product-market-fit, transitioning from an off-the-shelf product ranking solution to a highly customizable one is deceptively challenging and requires substantial engineering investment:

1. **Latency:** Effective product ranking models perform better when they can evaluate a large number of products. However, as the number of products increases, so does the user-facing latency. Maintaining fast browsing experiences while running machine learning models on hundreds of products in under 100 milliseconds is a demanding technical hurdle.
2. **Customizability:** The value derived from machine learning models in product ranking heavily relies on incorporating unique user behavior within the marketplace. Therefore, the system needs to be highly flexible, enabling data science teams to explore and implement new insights they acquire about users.
3. **Observability:** The importance of data quality and accuracy cannot be overstated in machine learning. Ensuring that that the data used for model training and evaluation is reliable, enabling effective decision-making and accurate product ranking.

## 🐉 Solution: [Wyvern AI](https://www.wyvern.ai?utm_source=yc&utm_medium=yc_launch_email&utm_campaign=launch_yc&utm_id=10)

Wyvern’s machine learning platform solves these problems. Not only do we give marketplaces a model that immediately improves their product ranking, we also provide:

1. The ability to iterate on and fine-tune the model by expanding its inputs, such as relevance, personalization, popularity, and more.
2. The ability to adjust the model's objective, allowing it to optimize conversion, GMV, revenue, profit, or a combination thereof, based on the current focus of the business.
3. An observability layer is provided to marketplaces, offering essential capabilities for debugging and evaluate historic predictions. This layer also facilitates transforming the data into a feedback loop, enabling continuous improvement of the performance of real-time machine learning models.

This allows our customers to dedicate data scientists to iterate on models within their marketplace, allowing them to continually improve the quality of product ranking across all of their surfaces.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72744&key=user_uploads/1120458/639a4715-c00e-430a-94c3-f5b122dfe255)

## 🙏 Our asks

* Are you a marketplace company? We would love to chat.
* Do you know anyone working at growing marketplaces? We’d love an introduction.
* If you have any questions, you can reach us at [suchintan@wyvern.ai](https://mailto:suchintan@wyvern.ai)
