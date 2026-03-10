# Launches

## Unify: Notion for AI Observability 📊

**TL;DR** simple, lightweight, and _fully hackable_ observability + evals. Cut out the noise, and focus on the data + metrics that matter to **you** **🎯**

⬇️ [Clone our Open Source Framework](https://github.com/unifyai/unify)

📊 [Customize your Dashboard](https://console.unify.ai)

👋[Chat with us](https://calendly.com/unify-chat/general)

**🫠 Problem**\
Current LLM infra has **too many layers of abstraction**, with rigid schemas and several concepts to learn. This obfuscates **way too much** from users, making things _seem_ **much** **more complex** than they really are, and paradoxically it also makes these tools rigid and inflexible.

LLMs are also only a _part_ of a _broader product_, and so your observability and eval infra shouldn’t be exclusively obsessed with LLM abstractions. The product and **your users** are what really matter, and the needs can vary wildly from product-to-product. Your observability and eval tooling should reflect that!

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdzqWhv0KzWyx7DWhWVtZrw33obNeaKAD9bQo9QpFQBHUHeBgfad4mQy6ec-Ex7TAWc8DAxbZyPQAPRnExzIVjQQcV-gE4IG-oRTQkwzzTqyA0DjnIFmGZ6oiRk0VwagkG1GmrO?key=fZADz8ArxOyiJBgH0jhGFh02)

\
**🧘 Not Anymore**

The core building block is simple, just “unify.log”. This lets you store _any_ kind of data to your console for easy visualization, grouping, sorting, and plotting.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88744&key=user_uploads/949841/3a30c20b-5079-427b-8bc7-e82229263a51)

You can then hack together your own custom interface, for whatever you want using three basic tile types: **Tables 🔢**, **Views 🔍** and **Plots 📊**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88744&key=user_uploads/949841/5e3a7093-0583-4e39-a799-83a8897e1d30)

Use these **three primitives** to:

➕ create + visualize your datasets in a new tab\
➕ monitor and probe production traffic in a new tab, with or without LLMs\
➕ start an evaluation flywheel in a new tab, with or without LLMs\
📉 optimize your product for your users, with or without LLMs\
🧠 whatever else you can think of!

Check out our minimal demo, explaining how to use these building blocks to ship with speed and clarity ⚡\
<https://youtu.be/fl9SzsoCegw?si=GKDi4TLEUXNgfWy2>

**Getting Started 🛠️**

[Sign up](https://console.unify.ai/), check out [our repo](https://github.com/unifyai/unify), and you're ready to go!

```
from unify import Unify
unify = Unify("gpt-4o@openai")
msg = "hello"
response = unify.generate(msg)
unify.log(message=msg, response=response)
# visualize at https://console.unify.ai
```

\
🙏 **Our Ask**

Give [Unify](https://console.unify.ai/) a try, and let us know what you think! Check out our [walkthrough](https://docs.unify.ai/basics/welcome), and if you like it, then give [our repo](https://github.com/unifyai/unify) a star 😊 If you don’t think it’s useful, please tell us. We’d love to know!

## Unify - The best LLM on every prompt ✨

**TL;DR** Unify dynamically routes each prompt to the best LLM and provider so you can balance quality, speed, and cost with ease ✨

🔀 [Try out our router in the browser](https://unify.ai/chat?default=true)

💸 [Sign up now and get $50 free credits!](https://console.unify.ai/)

🧑‍💻 [Get a Demo](https://calendly.com/unify-chat/general)

**💥Problem** \
There is a new LLM emerging almost every week, and all LLM applications have unique requirements for output quality, cost, and speed. It’s also unclear which models provide the highest quality on your task. This results in lots of manual signups, testing different models, bespoke benchmarking, etc. It’s overwhelming, and the final solution is almost always sub-optimal.

![](https://t9015538723.p.clickup-attachments.com/t9015538723/65677e25-4ec6-4c1a-b235-56ff1fee6552/splash3.png)

Many people give up and just use the largest models for everything. However, you really don't need GPT4 to summarize simple documents. Llama 8B is more than capable and is **15 times faster** and **100 times cheaper**. LLM apps are currently _much_ slower and more expensive than needed 💵🔥⏱️, and also often underperform in output quality because of poorly selected models 📉 (Claude Opus vs. GPT4 vs. Gemni etc.) for your specific prompts.

**🤩 Not Anymore**

Unify automatically routes each prompt to the most suitable model based on your preferences for quality, speed, and cost. Simply tune these three dials and let Unify do all the hard work.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81027&key=user_uploads/949841/fa900ddd-6849-408f-9a6c-1ad5dcfb0872)

Your "easy" prompts will go to the fastest and cheapest models, and only the "hard" prompts will go to the most appropriate heavy lifters, like GPT-4o, Opus, and Gemini. You focus on building your LLM app, and we'll focus on providing the best models, with the fastest providers, at the lowest cost ⚡

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81027&key=user_uploads/949841/b59ee67a-6566-4728-b146-57b102cf3151)

Watch our [explainer video](https://youtu.be/15wgxK1Cw0E?si=5G04-7tGRKPyxiNa) to learn more about the solution at a high level.

**What Unify Offers ✨**

* **⚙️ Control**: Choose which models and providers to route to and adjust three sliders: quality, cost, and latency.
* 📈 **Self Improvement**: Unify automatically improves your LLM application over time as new models and providers emerge.
* 📊 **Observability**: [Compare all models and providers](https://console.unify.ai/dashboard) and see which are best for your needs.
* ⚖️ **Impartiality**: Unify treats all models and providers equally, ensuring unbiased quality, cost, and speed [benchmarks](https://console.unify.ai/dashboard).
* 🔑 **Convenience**: With a single API key, [access all models and providers](https://unify.ai/docs/api/first_request.html) behind a single endpoint, queryable individually or via the router.
* 🧑‍💻 **Focus**: Don't stress about updating models and providers; Unify handles it for you so you can focus on building great LLM products.

**Getting Started 🛠️**

[Sign up](https://console.unify.ai/), select your [router](https://unify.ai/chat?default=true), then `pip install unifyai` and you're ready to go!

```
from unify import Unify
unify = Unify(
    api_key="UNIFY_KEY",
    endpoint="router@q:1",
)
response = unify.generate(user_prompt="Hello there")
```

🙏 **Our Ask**

Give Unify a try, and let us know what you think! [Sign up](https://console.unify.ai/), `pip install unifyai`, take our [router](https://unify.ai/chat?default=true) for a spin, and check out our [product walkthrough](https://youtu.be/ZpY6SIkBosE). If you're excited about Unify, tell a friend about it 😊 If you don’t think it’s useful, please tell us. We’d love to know!
