# Launches

## Zenbase: Continuous prompt optimization from DSPy core contributors

**TL;DR:** Zenbase helps developers focus on programming by automating prompt engineering and model selection. We’re building developer tools and cloud infrastructure for teams to save time, never get stuck in prompt hell, and create AI apps that get smarter over time.

Hey there! We're [Cyrus](https://linkedin.com/in/knouroozi/) & [Amir](https://www.linkedin.com/in/amir--mehr/). In the past, we've both been lead engineers and founding CTOs. We became contributors to [DSPy](https://github.com/stanfordnlp/dspy) and discovered the future of programming with language models.

This is the story of how we came to this insight, our glimpse into the future, and 2 case studies on how Zenbase has helped companies escape prompt hell and scale prompt engineering.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83751&key=user_uploads/121365/4f26ad68-3d25-4e10-8573-3b8937b0f8b4)

## Problem

Prompt “engineering” is the most time-consuming, stressful, and uncertain part of programming with LLMs. With DSPy, we had found something profound. It promised to save us from the all-too familiar user journey we — like so many others — had experienced.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83751&key=user_uploads/121365/900890e2-d8f5-4a1f-a7db-34d528534de9)

DSPy kept growing. It became Stanford NLP's #1 GitHub repo with 16K stars. We started hearing of folks in Microsoft, Amazon, Google, and 40+ other companies using DSPy to prototype apps with it.

We began hearing the same things all over again. Although many found DSPy elegant and intuitive, countless folks found it impossible to grok. Those who managed to build something with it had headaches productionizing it; finding it difficult to scale, make reliable, and make performant.

So, we set out to create the productionized DSPy.

## Solution

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83751&key=user_uploads/121365/95d2ad6e-9ce2-4903-b2d9-9715958d3064)

Zenbase lets you optimize your prompts and models. We offer:

1. [zenbase/core](https://github.com/zenbase-ai/core/tree/main/py) is an open-source Python library that you can use to optimize your existing LLM pipelines using DSPy’s optimizers (versus having to rewrite your pipelines in DSPy)
2. A hosted API for creating AI functions that get smarter with time. We ingest user feedback to continuously optimize the prompt and model.

   We use the latest tricks from DSPy, our own custom optimizers, and fine-tuning as appropriate to execute your intents in a way that's good, fast, and at a reasonable price.
3. An on-prem API for businesses with data privacy requirements.

## Use Cases

### How Zenbase saved Vera from Prompt Hell

> **Zenbase came into the trenches with us to improve our evals from 10% to 80%.** It really felt like they were a part of our team.
>
> — Taeib, Cofounder @ [Vera-Health.ai (YC S24)](http://Vera-Health.ai)

They were staying up until 3am on multiple nights trying to prompt engineer their RAG query generator to retrieve the correct documents. Their progress was uncertain. It was stressful. We call this prompt hell.

Prompt engineering is the most uncertain, risky, and stressful part of programming with LLMs. There didn’t seem to be a way out, but with Zenbase, they saw the light at the end of the tunnel.

Zenbase makes prompting systematic and peaceful. **We helped Vera go from demo to production, by optimizing the prompt of their query generator.** With a product that could handle doctors’ stress tests, they could focus on selling, and go to bed at a good time.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83751&key=user_uploads/121365/985b0550-7421-4890-8696-30201f7c4793)

### How Zenbase helped Superfilter create an AI that’s personalized to its users

> I’ve seen a lot of AI Devtools and Zenbase is solving a problem that everyone building with AI will have when going to production. **The best part is their product is so easy to use that it’s a no brainer.**\
> \
> — Scott, CEO @ [Superfilter.ai](http://Superfilter.ai) (YC S24)

It was all going great. Superfilter had just tested their AI email copilot with their beta users of investors and startup founders, and their users were excited. They onboarded a new cohort, and their prompts broke down. It worked well for the investors and startup founders, but not everyone.

Scott and his cofounder Travis realized that prompt engineering wasn’t going to scale to accurately categorize user emails into important, action required, or ignore.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83751&key=user_uploads/121365/694abf71-1e59-4dc5-bbfe-1d33209e0d2e)

Superfilter used our hosted API to create email categorizers that learned from users’ existing behaviour. With automatic prompt engineering, they were able to scale personalized experiences for every user.

**Zenbase makes personalized AI apps easier to build and scale with automated prompt engineering.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83751&key=user_uploads/121365/340719d4-94dc-4a3f-82f0-08c9a046ff1a)

## Asks

1. Are you in prompt hell, and do you want to feel the Zen? Are you trying to scale the personalization of prompts for every account?\
   \
   Learn more [on our website](https://zenbase.ai) and [schedule a demo](https://zenbase.typeform.com/early-access) with us so we can understand where you are and where you want to be. Let us be your LLM doctors and wizards as we guide you to where you want to go.
2. Use our [MIT-licensed Python SDK](https://github.com/zenbase-ai/core/tree/main/py) to optimize your existing prompts with DSPy’s optimizers.
3. Kindly share this post with anyone you know who could benefit 🙏
