# Launches

## Lytix - A single solution for the full lifecycle of LLM applications

**TL;DR: Lytix is one control panel to observe, manage and optimize your E2E LLM stack. From early model experimentation to guardrails and specific evaluations, lytix helps teams at any stage save money, move faster, and minimize tech debt.**

⚠️ **The Problem**

1. You want to use and experiment with multiple models, but setting up interfaces per provider/model is painful and slows you down.
2. As your product gets more specific, tracking performance becomes more challenging as off-the-shelf metrics lack the domain context to evaluate the unique attributes _you_ care about.
3. You want to protect your inference calls against known failures, but finding + integrating the right guardrails for your use case is time-consuming and confusing.
4. Simple logging is great, but it gets hard to interpret and find bugs quickly, especially if you have multiple LLM tasks all being logged in a single place.

**⚡ Our Solution**

Lytix helps teams of all sizes build faster, save money, and minimize tech debt.

**Single Gateway For All Models & Providers.**

1. Integrate [seamlessly](https://docs.lytix.co/Quickstart/openai-integration) with your existing stack to quickly get started.
2. Instantly gain access to 25+ models; switching between models becomes a 1-line change.
3. Our code is open-source, so you can always add more providers and models that are specific to you.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83820&key=user_uploads/1639132/3018a6a5-f5e6-494c-9b87-e4c320e89c54)

**Guardrails & Alerts**

1. An intuitive and flexible framework for adding SOTA guardrails to your inference calls, and set up real-time fallback logic
2. Configure alerts in **seconds**, to instantly get alerted when guardrails fail

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83820&key=user_uploads/1639132/c5e44af3-d41d-4013-8b1e-98db8c663e46)

**Build Specific Evaluations**

1. Easily build new eval metrics bespoke to _your_ product, factoring specific domain knowledge and context.
2. Track how your specific evals perform over time, and easily find anomalous sessions or problematic users.
3. Move beyond ‘feelings’, and start to quantify your results as you experiment with different configurations, model combinations and prompts.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83820&key=user_uploads/1639132/9c7e0c81-06d9-4954-9036-466639cefadd)

**Grouping LLM events by task**

1. Instead of a single stream of logs, lytix divides your logs by the task they belong to.
2. Debug errors faster by viewing them in the right context.
3. Cut critical metrics (like cost, latency, error rates) by task, to answer questions like ‘what is our most expensive task?’ or “which tasks are failing the most?”

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83820&key=user_uploads/1639132/767653cb-a38a-4df9-a154-3f981a9246f2)

**Product + LLM Insights**

* Identify themes and patterns in your LLM interactions
* Export that LLM events, with evals, to product analytic tools (such as Posthog) to combine product and LLM metrics into a single insight (i.e., cut conversation length by prompt).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83820&key=user_uploads/1639132/adcfbfeb-5f0b-4560-917c-d8bcfc4c5e76)

**And much more…**

* Bring your own cache: own your data and save money on requests by hosting your own cache
* Playground to test new or existing events against 25+ models
* Cost + Token usage tracking
* Datasets to collect events for fine-tuning

🪩 **The Team**

We’ve both worked in the tech, and have known each other since high school.

Sahil worked as a product manager at Intuit, working on teams all over the world. For QuickBooks international, he launched localized sales tax and “send invoice via WhatsApp” increasing 91d retention, subscription rates, and invoice sends for emerging markets. He also worked on complex machine learning systems, working on matchmaking models for QuickBooks Live.

Sid worked at a verity of startups after college working on a breath of tasks from cybersecurity to infrastructure and devops. He was cited as an author on a state of the art cryptography [white-paper](https://eprint.iacr.org/2023/296.pdf) and has helped teams containerize and migrate infrastructure while maintaining 50,000+ active users.

We are builders at heart and believe that lytix is the future of how to build and scale LLM products.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83820&key=user_uploads/1639132/feb330f8-8a93-401b-b5d2-8df9b4bf4afb)

**🚀 Lytix can be used today!**

* [Free to start](http://lab.lytix.co/home/login/) and use up to 100k messages.
* We love learning about problems, if you have any in the LLM space we’d love to be helpful and [chat](https://book.vimcal.com/p/sahilsinha/30minutes-8347b)!
* Check out our [open-source](https://github.com/Lytix-Labs/optimodel) work and get 24/7 support on our [Discord](https://discord.com/invite/u2MFEnhmv3)
* Follow our socials on [LinkedIn](https://www.linkedin.com/company/103001009/) and [X](https://x.com/lytixai)

## Lytix - Everything you need to monitor, improve and scale your LLM applications

**Everything LLM teams need, to build something your users love. Get started **[**here**](https://www.lytix.co/)**.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81849&key=user_uploads/547106/e9646020-5b9d-4c28-bcf8-6dfa602e31de)

# The Problem ❌

Monitoring and testing LLMs is notoriously challenging. Specifically:

1. **Product insights & monitoring** - how can I see how different customers are using my LLM stack?

   > What are users talking to my bot about? What questions are users asking my search system?
2. **Testing** - I just made a change to my code. How can I confirm it’s making the change I intended? How can I make sure I haven’t introduced unexpected side effects?

   > _Will making my bot faster make it less reliable? Will switching LLM providers make our system too slow for our customers_
3. **E2E analytics** - Product 🤝 LLM metrics. How can I see how changes to my LLM stack are impacting my primary product metrics?

   > _I just changed my RAG pipeline, is that improving my conversion rates? Which prompt gives us the best activation rate? What are high vs. low value customers talking to my bot about?_
4. **Errors** - I’m using 4+ providers across my LLM stack, each with its own logging system and dashboard. How can I quickly view the root cause of my errors and get all the context I need in one place?

**We’ve seen teams waste weeks of dev time building internal tools to solve these problems instead of building what their users want.**

# The Solution 🛠️

Lytix brings insights, testing, and E2E analytics to your LLM stack with minimal changes to your existing codebase.

# Product insights 🔎 & monitoring 👀

1. Add a tracer function to any aspect of your LLM stack you’d like monitored

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=81849&key=user_uploads/547106/dc47d9d9-39f5-47ed-8fd5-035063e4ade4)

2. _\[Optional\]_ - in the Lytix dashboard, define some ‘themes’ you’d like Lytix to start tagging your sessions as. For ex. ‘questions about math’

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=81849&key=user_uploads/547106/c660f875-f0f5-4189-b7c5-408bb2ee4b99)

3. If you do not define an intent - Lytix will auto-tag each session with an intent that best summarizes the session.
4. You can always explore previous sessions and re-configure your themes to change how they appear in your analytics stack

# E2E analytics 📊 ( for ex. PostHog 🦔)

1. Save your PostHog API key in your Lytix account (under settings)
2. Whenever Lytix sees a new session, we’ll tag it (with the intents you’ve configured), and import them into Posthog with all the associated metadata
3. In PostHog, you’ll see a “lytix_event” → this event describes your users’ sessions with your LLM stack. **Bring this into your funnel analysis, retention charts, etc., to include your LLM sessions in your product insights**

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=81849&key=user_uploads/547106/90a58a3c-03e4-4e81-9ae2-33a8d61eb6ea)


# Errors 🚨

1. Wherever you throw an error, use the new Lytix LError class.

   ```
   async def backgroundProcess():
       logger = LLogger("background-logger", {"userId": '124'})
       logger.info("Some process is starting")
       raise LError("An unexpected error")
   
   ```
2. Anytime the error is thrown in production, you’ll find all relevant logs and metadata in your Lytix dashboard

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=81849&key=user_uploads/547106/b4373adc-92ec-487b-bef4-90e3dae98cc0)


To try it out yourself, head over to <https://docs.lytix.co/introduction>. You’ll also get 2 founders on deck as analysts to ask any questions about how your customers are using your products 🚀.

And get in touch if you:

1. Are about to launch - and would like to chat about best practices
2. Recently launched - and are thinking about effective analytics and monitoring
3. Or have a hair-on-fire problem you need to be taken care of!
