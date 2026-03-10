# Launches

## Srcbook: TypeScript notebooks

**TLDR**: We recently launched a new open-source application for prototyping in TypeScript: [**Srcbook**](https://srcbook.com/) (pronounced “source-book”). Srcbook is a notebook-style programming environment and the best way to prototype code, explore libraries, learn concepts, and rapidly iterate on your ideas with TypeScript. It runs locally, has powerful AI features, and exports to markdown for maximum portability.

[**https://www.loom.com/share/f0ea7257d9c544848f4128cf0ccba8ae?sid=d5a51920-8c37-4b10-90ee-414170dfeb5d**](https://www.loom.com/share/f0ea7257d9c544848f4128cf0ccba8ae?sid=d5a51920-8c37-4b10-90ee-414170dfeb5d)

### Origin story

We are very bullish on AI moving from being a Python discipline in the ML era to a TypeScript discipline in the Generative AI era. We previously tried building multiple products to serve this new TypeScript-AI wave, but we quickly realized that most teams don’t want low-code GUI tools to do evals or build agents with drag-and-drop. What they actually want is to write code but do so with rapid iterations. In Python, they automatically reach out to Jupyter for such workflows, but in TypeScript? We found that there was a large gap… We realized that a TypeScript notebook would be useful for many use cases, not just applied gen-AI, and so we started building.

### The product

Srcbook is a beautiful, open-source, local-first application to write and iterate on TypeScript code. It’s available today on npm: `npx srcbook start`

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83310&key=user_uploads/1399285/1af6e324-e52a-4d49-8e35-27af1b5dd4b5)

Some key features:

* Full npm ecosystem access
* AI-assisted coding (OpenAI, Anthropic, or local models), with notebook-specific advantages and a natural “pair-programmer” UX
* Exports to valid markdown for easy sharing and version control

We recently [launched on HN](https://news.ycombinator.com/item?id=41291700) and devs really seem to like it, all our graphs started looking like this!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83310&key=user_uploads/1399285/a040cd03-a61f-4767-b524-50b285aa9bd3)

### Demo

In this video, you can see Nick using the genAI features to bootstrap a CLI-based chess game in a few minutes.

<https://www.loom.com/share/a212e1fd49a04c548c09125a96a1836f>

### Asks

Try Srcbook out! It’s free, just `npm srcbook start` in any terminal.

Starring us on [GitHub](https://github.com/srcbookdev/srcbook/tree/main) also helps, although what we really want is for you to build cool stuff with Srcbook. If you make a good Srcbook, send it our way, and we will showcase it in the [Hub](https://hub.srcbook.com).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83310&key=user_uploads/1399285/8bab03fa-f71f-43bb-9639-152a83cfb733)

PS: We’re [Ben](https://linkedin.com/in/bereinhart) and [Nick](https://linkedin.com/in/nicholas-charriere), been building together for 5+ years at Cruise and other startups, and we love TypeScript. If you do too, reach out and let’s chat!

## Axilla — an AI framework for TypeScript

**tl;dr** Axilla is a framework for the AI engineer of the future: a product-focused TypeScript developer. Axilla provides a family of modular libraries, which can be incrementally adopted, and together form an **end-to-end opinionated framework for LLM development**.

### The team

Hey there 👋, we’re [**@Ben Reinhart**](https://linkedin.com/in/bereinhart) and [**@Nicholas Charriere**](https://linkedin.com/in/nicholas-charriere).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73588&key=user_uploads/1399285/8bda8bff-dc8a-4979-9c4b-a73b4c49a5f1)

We first started working together on ML platforms at Cruise, a leading self-driving car company, where we spent 4 years on the ML platform team. This is also where we became great friends!

At Cruise, we’ve seen the productivity losses that result from a fragmented ML organization. We then spent years designing and building a standardized framework and personally experienced the productivity superpowers that resulted from the framework’s adoption.

### 🤨 The problem

An accelerating trend in the AI landscape is the shift from in-house model training to foundational models abstracted away behind APIs (chatGPT, Midjourney, llama2…).

A consequence of this trend is that AI teams are morphing from Python-focused data scientists to resemble typical product engineering teams: full-stack web developers increasingly coding AI applications in TypeScript.

We’ve spoken to a number of enterprise customers who’ve confirmed their product teams are now responsible for designing and launching new AI initiatives, especially ones involving LLMs. However, given how recent the explosion of LLMs is, **these product engineers don’t yet have the tools** **to ship AI features quickly and with confidence**.

### 💡 The solution

[**Axilla**](https://www.axilla.io/) provides a family of modular and coherent libraries which together form an end-to-end opinionated framework for LLM development. It is aimed at TypeScript developers who want to build and operate production-grade AI applications.

It’s early, but in the last three weeks we launched our first two modules:

1. [**axgen**](https://github.com/axilla-io/ax/tree/main/packages/axgen) is focused on data ingestion and retrieval
2. [**axeval**](https://github.com/axilla-io/ax/tree/main/packages/axeval) is focused on continuous evaluation & quality monitoring

Next, we are excited to begin work on model serving and monitoring, which are two of our most critical components. Together, these integrate production data back into the continuous evaluation pipelines, enable enterprises to run open-source models internally, and **allow developers to stop flying blind** when it comes to their AI applications.

### Demo

As part of our first release, we built a proof of concept that demonstrates how to build a “chat with your documents” application using axgen.

<https://youtu.be/8KEbP7LL_sM>

### Asks

[**Try axilla**](https://github.com/axilla-io/ax) today! It’s open source and available on npm. If you like it, **give it a star** ⭐️, and come join the conversation on [twitter](https://twitter.com/axilla_io).

Are you a product engineer building AI applications (especially with TypeScript)? We’d love to [chat](https://calendly.com/nichochar/15min-chat-with-nicholas)!
