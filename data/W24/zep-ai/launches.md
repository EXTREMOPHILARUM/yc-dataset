# Launches

## Graphiti by Zep AI : A library for building dynamic Knowledge Graphs

Hey! We're Paul, Preston, and Daniel from Zep AI. We've just [open-sourced Graphiti](https://git.new/graphiti), a Python library for building temporal Knowledge Graphs using LLMs.

<https://youtu.be/sygRBjILDn8>

Graphiti helps you create and query graphs that evolve over time. Think of a knowledge graph as a network of interconnected facts, such as _“Kendra loves Adidas shoes.”_ Each fact is a “triplet, represented by two entities, or nodes (_”Kendra,” “Adidas shoes”_), and their relationship, or edge (_”loves”_). Knowledge Graphs have been explored extensively for information retrieval. What makes Graphiti unique is its ability to autonomously build a knowledge graph while handling changing relationships and maintaining historical context.

At Zep, we build a [memory layer for LLM applications](https://www.getzep.com). Developers use Zep to recall relevant user information from past conversations without including the entire chat history in a prompt. Accurate context is crucial for LLM applications. If an AI agent doesn't remember that you've changed jobs or confuses the chronology of events, its responses can be jarring or irrelevant, or worse, inaccurate.

# Zep’s Suboptimal Fact Pipeline

Before Graphiti, our approach to storing and retrieving user “memory” was, in effect, a specialized RAG pipeline. An LLM extracted “facts” from a user’s chat history. Semantic search, reranking, and other techniques then surfaced facts relevant to the current conversation back to a developer for inclusion in their prompt.

Unfortunately, this approach became problematic. Reconciling facts from increasingly complex conversations challenged even frontier LLMs such as gpt-4o. We saw incomplete facts, poor recall, and hallucinations. Our RAG search also failed at times to capture the nuanced relationships between facts, leading to irrelevant or contradictory information being retrieved.

We tried fixing these issues with prompt optimization but saw diminishing returns on effort. We realized that a graph would help model a user’s complex world, potentially addressing these challenges.

# Building Graphiti

We were intrigued by Microsoft’s GraphRAG, which expanded on RAG text chunking with a graph to better model a document corpus. However, it didn't solve our core problem: GraphRAG is designed for static documents and doesn't natively handle temporality.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83738&key=user_uploads/808515/db4712c7-1171-4115-ad7b-67896c754a65)

So, we built Graphiti, a [temporal Knowledge Graph](https://github.com/getzep/graphiti) library, which is designed from the ground up to handle constantly changing information, hybrid semantic and graph search, and scale:

* **Temporal Awareness**: Tracks changes in facts and relationships over time. Graph edges include temporal metadata to record relationship lifecycles.
* **Episodic Processing**: Ingests data as discrete episodes, maintaining data provenance and enabling incremental processing.
* **Hybrid Search**: Semantic and BM25 full-text search, with the ability to rerank results by distance from a central node.
* **Scalable**: Designed for large datasets, parallelizing LLM calls for batch processing while preserving event chronology.
* **Varied Sources**: Ingests both unstructured text and structured data.

# Getting Started

Graphiti is open-source and available on GitHub: <https://git.new/graphiti>

Quick Start: `pip install graphiti-core`

While we developed Graphiti for our needs at Zep, we believe it could be useful for any application dealing with evolving, interconnected data, such as:

* Personal AI assistants that need to maintain user context over time
* Knowledge management systems for rapidly changing domains
* Social network analysis tools
* Financial systems tracking changing relationships and transactions

If you try, we'd love to hear your thoughts, questions, and experiences. Please also consider contributing!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83738&key=user_uploads/808515/3d306962-fad2-44fd-9232-862ddd961d0d)

## Zep: Fast, accurate structured data extraction for AI assistant apps

Many business and consumer apps must extract structured data from conversations between an LLM-powered Assistant and a human user. Often, the extracted data is the objective of the conversation. Consider completing a sales order, making a reservation, or requesting leave. All of these tasks require progressively collecting data from the conversation.

Latency and correctness are important. You will often want to identify the correct data values you have collected and those you still need. You’ll then prompt the LLM to request the latter.

<https://youtu.be/k8e8NsoVzFo>

If you’re making multiple calls to an LLM to extract and validate data on every chat turn, you’re likely adding significant latency to your response. This can be a slow and inaccurate exercise, frustrating your users.

Zep’s new Structured Data Extraction feature is a low-latency, high-accuracy tool for extracting the data you need from Chat History stored in Zep's Long-term Memory service.

> **Up to 10x faster than gpt-4o.** For many multi-field extraction tasks, you can **expect latency of under 400ms,** with the addition of fields increasing latency sub-linearly.

## Comparing Zep with LLM JSON Mode

Many model providers offer a JSON inference mode that guarantees the output will be well-formed JSON.

However:

* There are no guarantees that the field values will conform to the JSON Schema you define or that they are correct (vs. being hallucinated).
* All fields are extracted in a single inference call, with additional fields adding linearly or greater to extraction latency.

#### Preprocessing, Guided LLM Output, and Validation

To ensure that the extracted data is in the format you expect and is valid given the current dialog, Zep uses a combination of:

* dialog preprocessing, which, amongst other things, improves accuracy for machine-transcribed dialogs;
* using guided output inference techniques on LLMs running on our own infrastructure;
* and post-inference validation.

You will not receive back data in an incorrect format when using a Zep field type such as email, zip code, or date time.

While there are limits to the extraction accuracy when the conversation is very nuanced or ambiguous, carefully crafting field descriptions can achieve high accuracy in most cases.

#### Up to 10x Faster than OpenAI gpt-4o

When comparing like-to-like JSON Schema model extraction against gpt-4o, Zep is up to 10x faster.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81733&key=user_uploads/808515/7adc0720-a2ed-43d9-88ed-1bd883f819c7)

Zep's extraction latency scales sub-linearly with the number of fields in your model. That is, you may add additional fields with a low marginal increase in latency.

## Support for Partial and Relative Dates

Zep understands various date and time formats, including relative times such as _“yesterday”_ or _“last week.”_ It can also parse partial dates and times, such as _“at 3pm”_ or _“on the 15th.”_

## Extracting from Speech Transcripts

Zep can understand and extract data from machine-transcribed transcripts. Spelled-out numbers and dates will be parsed as if they were written language. Utterances such as “uh” or “um” are ignored.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81733&key=user_uploads/808515/8ab99f7f-0672-42dc-9d35-b06c37a33c7a)

## Using Progressive Data Extraction To Guide LLMs

Your application may need to collect several fields to accomplish a task. Since Zep's SDE is so fast, you can guide the LLM through this process by calling the extractor on every chat turn. This enables you to identify which fields are still needed and then direct the LLM to collect the remaining data.

```
You have already collected the following data:
- Company name: Acme Inc.
- Lead name: John Doe
- Lead email: john.doe@acme.com

You still need to collect the following data:
- Lead phone number
- Lead budget
- Product name
- Zip code

Do not ask for all fields at once. Rather, work the fields 
into your conversation with the user and gradually collect the data.
```

## Next Steps

1. Learn more in the [Zep Structured Data Guide](https://help.getzep.com/structured-data-extraction).
2. Sign up for Zep's [Long-term Memory Service for AI Assistants](https://www.getzep.com/).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81733&key=user_uploads/808515/0a1d48ed-3bde-4b77-b3e7-08ffe0fa3deb)

## Zep - Long-term memory for AI assistants

[Zep](https://www.getzep.com/) is the easiest way to add long-term memory to your AI Assistant. With Zep, you can recall, understand, and extract data from chat histories, enabling you to build rich, personalized experiences. 

**Sign up for the **[**Zep Cloud**](https://www.getzep.com/)** and get a Zep Bot T-Shirt when you go live!**

tl;dr

* Zep ensures your Assistant **remembers relevant facts and nuance** from historical conversations, no matter how distant in the past.
* **Zep makes dialog useful**: Control program flow, extract structured data, select the right prompts or tools, build customer segments, and more.
* **Fast**! Minimize the number of LLM calls keeping your users waiting. Zep completes tasks in a 1/10 of the time compared to similar functionality built with OpenAI.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79302&key=user_uploads/808515/c1ac513c-7ef4-4406-b98a-3e3b4ff94134)

<https://www.youtube.com/watch?v=qVspUE_R-iI>

**Zep In Action: The Amazing ShoeStoreBot**

Managing sales, returns, and order inquiries is all in a day’s work for this hard-working ShoeStoreBot. It remembers past customers, their budgets, brand preferences, shoe size, and more.

<https://www.youtube.com/watch?v=AC4VTqLYYhM>

**Perpetual Memory:  Your Assistant will never forget a user.**

Automagically populate prompts with relevant facts and summaries extracted from past conversations, no matter how distant.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79302&key=user_uploads/808515/6672d796-e8c6-46de-9f65-53dcae5b54ea)

**Dialog Classifier: Instantly and accurately understand chat dialog.**

Identify user intent, emotion, segmentation, and more. Control program flow with semantic context, using the right prompts, tools, and agents depending on the current dialog.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79302&key=user_uploads/808515/5967ab25-86e6-4526-8fc0-aba4c87c6c58)

**Extract Structured Data from Dialog**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79302&key=user_uploads/808515/89656e21-5687-4d6d-a8b8-f4a728e19562)

Quickly extract business data from chat conversations. Understand what your Assistant should ask for next to complete its task.

**Support for Your Favorite Languages and Frameworks**

Are you a Python, TypeScript, LangChain, LangChain.js, Chainlit, or FlowWise person? We got you covered.

**The Zep Team**

Zep was founded by [Daniel](https://www.linkedin.com/in/danielchalef/) (hi!), who was recently joined by 2 engineers he worked with previously (Peter & Paul!). Daniel led ML at SparkPost (acquired by MessageBird), and previously founded KnowledgeTree (another popular open source project from the 2000s). Despite taking on marketing and corp dev roles in previous lives, he remains an engineer at heart.

Daniel accidentally started Zep when he got frustrated that no delightful software existed to do what Zep does today. He built an early version and stuck it up on GitHub, and one thing led to another.
