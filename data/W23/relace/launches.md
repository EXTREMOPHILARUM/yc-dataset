# Launches

## Relace - Cheaper, faster, and more reliable AI code generation.

Hey everyone 👋 -- we're Preston and Eitan, the cofounders of [Relace](https://relace.ai).

**TL;DR:**

Relace models are designed to slot naturally into most AI codegen products, making them faster, cheaper, and more reliable. We already have SOTA:

* Embedding + Code Reranker models to retreive the relevant context from million-line codebases in \~1-2s.
* Instant Apply model that merges code snippets at &gt;4300 tok/s.

We're in production with **Lovable**, **Magic Patterns**, **Codebuff**, **Create**, **Tempo Labs**, and 20+ other AI codegen startups. Watch our Instant Apply model race against full file rewriting with Claude 3.7 Sonnet:

https://www.youtube.com/watch?v=J0-oYyozUZw

**Problem:**

Agentic coding systems are easy to prototype, but hard to make robust. As users succeed at creating more complex designs/applications, you hit bottlenecks:

* Larger codebases require efficient context management -- you can't pass everything to the AI agent.
* Slow and expensive full file rewrites need to be replaced with abbreviated diff formats.

Frontier models (like Claude 3.7, o3, etc.) are powerful, but overkill for these auxiliary functions like retrieval and merging. Costs start to add up, especially when every agent action hits an API with thousands of tokens in and out. Plus, non-technical users are easily frustrated by high latency, especially if they are trying to refine small aspects of the code they created.

**Solution:**

Relace models are trained to achieve order-of-magnitude improvements in both latency and cost without compromising on accuracy.

_Instant Apply_

Released in February, this model merges semantic code snippets at 4,300 tokens/sec with an average end-to-end latency of \~900ms across our users.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90339&key=user_uploads/1187298/38144690-e758-43dd-b591-be0481a47c33)

Inspired by Cursor's Fast Apply, the semantic diff format is chosen to be natural for all models to output. A simple prompt change combined with Instant Apply can reduce Claude 3.5/3.7 token usage by \~40%.

We train on hundreds of thousands of code merges across dozens of different coding languages to achieve SOTA accuracy:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90339&key=user_uploads/1187298/3ed1d45b-1f70-4cc2-836e-d7c4a3dae817)

_Embeddings and Reranker_

Our embedding model + reranker can determine the relevance score for a user request against million-line codebases in \~1-2s. By training on hundreds of thousands of query/code pairs, we can effectively filter out irrelevant files and cut input token usage by over 50%.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90339&key=user_uploads/1187298/884ed0af-04c3-49e1-a92b-7e53ca81ad1b)

Not only does this save on cost, but cleaning up the context window significantly improves generation quality of the AI agent.

**Try It Out:**

Both of these models are battle tested and running millions of times a week in production. You can read more and try it out for yourself with the links below.

App: [https://app.relace.ai](https://app.relace.ai%5C) Docs: https://docs.relace.ai

We have a free tier for small projects, and we offer discounted rates for open source partners like our friends at Continue.

Don't hesitate to reach out if you're optimizing your coding agent — we would love to hear your thoughts, feedback, and what you're building!
