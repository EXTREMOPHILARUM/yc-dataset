# Launches

## 🧱 BricksAI Cloud - Simple cost control & monitoring for LLMs

**Tl;dr**: Are you finding it difficult to track your LLM costs per project/user? Do you want to set a custom rate/spend-limit for each project/user?

**Create a **[**free account**](https://www.trybricks.ai/sign-in)** and try us out today 😄**

Hey everyone, this is [**@Spike Lu**](http://linkedin.com/in/spike-lu-38227b105) and [**@Donovan So**](https://www.linkedin.com/in/donovanso/)! We're excited to share that we've launched [BricksAI Cloud](https://www.trybricks.ai/).

# **The Problem**

A lot of enterprise features are still missing from today's LLM providers, particularly:

1. there isn't a good way of controlling LLM spendings in a granular way (e.g. per user/project/env/feature etc.)
2. there isn't a good way of monitoring LLMs in a granular way

But building an LLM wrapper in-house takes away valuable engineering time from shipping features that actually drive business value.

# **The solution**

BricksAI Cloud is an [open-core](https://github.com/bricks-cloud/BricksLLM) SaaS solution that protects and monitors your LLM usage. We're a proxy, so instead of using API keys from your providers, you'd create and use Bricks API keys that come with custom limits (e.g. expiry date, rate-limit, or spend-limit).

[**Demo video**](https://www.loom.com/share/fe0553312e8a4378b3467c12f22e8714?sid=39bbbec1-da60-4054-899a-9ce991b068a9) ⭐

![uploaded image](https://www.ycombinator.com/media/?type=post&id=76778&key=user_uploads/1109574/8811f428-392d-4533-973d-516979be917d)

We currently have official support OpenAI and Anthropic, meaning you’ll be able to accurately track your token usage and cost without any configuration. We also support integrations with custom models.

Over the past few months, we have streamlined LLM operations for a wide range of clients, including a late-stage sustainability tech startup, a major leadership training nonprofit, a top European travel agency, and multiple AI startups.

Now, we're opening up our tool to the world with the launch of BricksAI Cloud. We'd love to see how it can transform your GenAI stack.

# **The ask**

1. Star us on [**Github**](https://github.com/bricks-cloud/BricksLLM) ⭐
2. Create a [free account](https://www.trybricks.ai/sign-in) and try us out today. _Heads up: we require a 15-min account activation call, this helps us get to know your use case better. Don’t worry, it’s super quick and casual!_
3. Questions? Feedback? Feature requests? [Book a call with us](https://calendly.com/spike-at-bricks/coffee-chat-with-spike) or email [founders@bricks-tech.com](mailto:founders@bricks-tech.com).

## BricksAI🔐: A simple OpenAI access manager for enterprises

**Tl;dr:** [BricksAI](https://www.trybricks.ai/) helps enterprises develop LLM apps more securely. We do this through an access manager that can set a spend limit, rate limit and expiration date on individual API keys. 

**The Problem: OpenAI does not provide enterprise level security features**

> _“You wouldn’t believe how many organizations are building OpenAI wrappers.”_
>
> _\- A machine learning director at a unicorn startup._

OpenAI does not have enterprise-level security features. A lot of companies need to build enhanced security features on top of what OpenAI offers before using them.

> “We simply assign each team an OpenAI key”
>
> \- A senior engineer working at a public fintech company.

Developing OpenAI applications often means that developers have to share OpenAI key credentials with each other to speed up development.

There are several risks and drawbacks associated with this approach:

* **Increased likelihood of security breaches**: more than 50% of breaches happen due to shared secrets
* **No cost visibility**: no way of knowing what constitutes a $20k OpenAI bill
* **No access control**: no source of truth for OpenAI access
* **Degraded production performance**: OpenAI has an organization-level rate limit. One team’s experimentation with OpenAI could impact the performance of production OpenAI applications if not properly rate limited.

Azure OpenAI service helps fill some of the gaps but this product is simply not available to users of GCP and AWS for competitive reasons.

**The Solution: A self-hosted OpenAI access manager**

[BricksAI](https://www.trybricks.ai/) checks all requests between your applications and different LLMs. We ensure every call is authorized, and does not exceed any traffic and cost limits.

You can create a custom API key with a **rate-limit**, **spend-limit**, and **expiration date** either programmatically or through our UI:

![](https://lh6.googleusercontent.com/2PBxx_RzNu9dsiySB2IXD4ySeziMayS-afN25SnUBofJEuRla9tBclCHbLg1OGdj_87mHcr3NSI4SMgTkEUtSRHIQr0yLgK1Ty0ZZWnvKSAi4tCEcktVTexY0RkVakz6krMl7mU2m2CO0tvGxJ3W_7g)

Then use the API key to access an LLM like you normally would. When a key reaches its limit (e.g. has expired), our gateway blocks off your requests:

![](https://lh3.googleusercontent.com/nJ4yb431KR5fhWm-5SHhrxEddPFtRWb5kUD4z7Gw2i3gnn3IO4_p7a2aeIqPQhLyW2l1XOx_0J-nv_rVmPv8KHR7adRa3uVd6bzgBbYPPmlfCOhjUoIZe9qIOqrEX3Kd4A8kOmcH9zqcC9yonuZich8)

In addition, our enterprise offering includes 

* **SSO**: SSO integration
* **Dashboard**: Dashboard view of the keys created
* **Analytics**: Analytics on usage and cost by team and service
* **Access Control**: Access control over who can view and create keys

![](https://lh6.googleusercontent.com/B1ecI3KdyzeqrdPU6JRoYflPXpt-y3YiRGuf3wE0_n6gJZxKZX6bxnHCFXFvSh4Rf5MsCTXNWpZEEIsXnsSiEyBqCJ9_GIVaRyWb8BoT6xjITG2pN1SMtiuDLJCryMENyfbPY_Y-2vAfW0fgUjMRuZg)

**Who are we?**

![](https://lh3.googleusercontent.com/QVEctbu3DQ5cZPDkK_P_-9KGBcMg64t7qzcFlEpbO_EpUefLvVcu5ApqHH6oZYx0x8hBDxZdX7PdngRjIkCXp_6ALUFsAn9ZCrB636TWAQ2o5pr1J7z-GVEoYgplvK__JBvVpVnXdnv7Fq5KQXqQJdI)

[Spike](https://www.linkedin.com/in/spike-lu-38227b105/) (on the right) was a senior software engineer at Unity for three years. He worked on an internal API gateway used by hundreds of developers.

[Donovan](https://www.linkedin.com/in/donovanso/) (on the left) was a software engineer at Credit Suisse, building internal tools dealing with financial instruments used by institutional investors.

While working on our previous [AI powered Figma to code idea](https://www.figma.com/community/plugin/1178847414663679049/Bricks---AI-Powered-Design-to-TailwindCSS-Code), we realized that developing applications using OpenAI credentials is easy to get started but poses huge security risks. After constantly hearing news about [leaked OpenAI keys](https://www.darkreading.com/application-security/cybercrooks-scrape-openai-keys-pirate-gpt-4), we are inspired to create a solution that helps make OpenAI development safer at enterprises.  \
\
**Interested in learning more?**

* 📅 [Book a call](https://calendly.com/spike-at-bricks/quick-chat?month=2023-09)
* ✉️ Email us at [spike@bricks-tech.com](mailto:spike@bricks-tech.com)
* 🤝 Connect with us on [LinkedIn](https://www.linkedin.com/in/spike-lu-38227b105/)
