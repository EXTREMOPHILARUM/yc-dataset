# Launches

## Superpowered AI - API for Retrieval Augmented Generation 🌐

### TLDR

We’re excited to announce the release of The SuperStack alongside our new Chat endpoint. Now, you can easily deploy conversational LLM applications with knowledge retrieval built-in. Our SuperStack suite of technologies directly targets common RAG failure modes, like hallucinations caused by out-of-context search results. Dive in and test it using our [Playground](https://superpowered.ai/), [Python SDK](https://github.com/SuperpoweredAI/superpowered-python-sdk), or [clone these examples](https://github.com/SuperpoweredAI/superpowered-examples).

### Problem 🤔

Many uses for LLMs, including most customer support and employee productivity applications, require effectively connecting LLMs to external knowledge sources. Doing this well is very hard. Current retrieval augmented generation (RAG) methods just take existing information retrieval methods and stuff the results into an LLM prompt. This works for simple demos, but usually isn’t reliable enough for real-world production applications.

### Solution 🧠

Superpowered AI offers a simple API that lets you connect external data sources (like product documentation, for example) to LLMs. We leverage proprietary RAG technology we’ve developed (we call it the [SuperStack](https://superpowered.ai/blog/the-superstack)) to dramatically improve performance and reliability for a wide variety of use cases.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=76118&key=user_uploads/733585/063e897c-eaa8-4a3a-874c-f0bad5249909)

Our solution is end-to-end, so you don’t have to worry about stringing together different APIs for different parts of the retrieval and generation pipeline. Here are some key features:

* Support for uploading various types of text files, PDFs, website content, and audio files
* 94 languages supported
* Use our knowledge retrieval pipeline on its own with our Query endpoint, or take advantage of our Chat endpoint for a fully end-to-end solution for building conversational applications connected to external knowledge sources.
* Usage-based pricing, so you only pay for what you use, and $50 in free credits to all new users!

### The SuperStack 🦸

The SuperStack has three components that directly tackle the problems with standard RAG pipelines:

[**AutoQuery**](https://superpowered.ai/blog/introducing-auto-query) → Convert user inputs into well-formed search queries for better retrieval results.

[**Relevant Segment Extraction (RSE)**](https://superpowered.ai/blog/introducing-relevant-segment-extraction) → Dynamically group clusters of relevant results into longer sections of contiguous text to provide better context to the LLM. This is especially useful for more complex questions, where the answer isn’t contained in a single sentence or paragraph.

[**AutoContext**](https://superpowered.ai/blog/introducing-auto-context) → Automatically inject descriptive context into text chunks and embeddings, to capture the full context of each chunk of text, reducing the likelihood of poor search results and hallucinations.

### Chat Endpoint 💬

Given that LLM applications often involve conversational interactions, we recently launched our Chat endpoint to make it easy to configure and deploy chat applications that utilize our knowledge retrieval pipeline. We currently support GPT-3.5-Turbo and GPT-4, with more models coming soon.

<https://youtu.be/3bnS3ppoRtM?feature=shared>

### Custom Solutions 🌐

For companies that don’t have the resources or expertise to build their own LLM-based solutions, we’re here to help. Whether you're looking to enhance internal productivity or launch innovative new products with LLMs, we will work with you to bring your vision to life. Our team is dedicated to helping businesses of all sizes leverage the potential of AI to drive efficiency and customer love.

### Ask 🙏

* Test it out and share your feedback. If it isn’t working well for your use case, please let us know! We love diving in and solving difficult problems for our customers.
* If you know developers/founders who are looking to build an LLM-based app, please send intros. We love learning about different use cases and the challenges developers are facing.
* [Retweet](https://twitter.com/superpowered_ai/status/1722691291891298586)

## Superpowered AI - Knowledge Base as a Service for LLM applications

Hey everyone! We are Zach McCormick, Dillon Martin, Justin Clark, and Nick McCormick from [Superpowered AI](https://superpowered.ai/).

### **TLDR**

Superpowered AI is an end-to-end knowledge retrieval solution designed specifically for LLM applications (i.e. retrieval-augmented generation). We turn complex infrastructure into a few simple API calls, making it easy to retrieve the right information and deliver highly relevant responses to your users. 

### 🦉 Who is it for?

Whether you’re using LLMs to improve your customer experience, increase efficiency within your company, or launch an LLM-based application for end-users, **Superpowered AI can provide your app with external knowledge and long-term memory without requiring you to be an AI expert** – all at a low cost. How low? We’ve set our pricing at half the cost of popular alternatives like OpenAI embeddings + Pinecone. Please note, our product is completely free for now, so feel free to query your heart out!

### 💡 How does it work?

Simply upload files (including audio) to a Knowledge Base, and then you can begin querying! We handle the text splitting, embeddings calculation, vector database uploading, etc. for you. **When you query your Superpowered AI Knowledge Bases, we return a list of the most relevant snippets of text from your Knowledge Bases, along with an LLM-generated summary of the results (with citations).** This output can then be added to the prompt of your LLM-based application to dramatically improve your LLM responses. Accepted file types: .pdf, .docx, .txt, .md, .mp3, .m4a, .wav

You can check this out in our web app right now[!](https://www.youtube.com/watch?v=4R_qoQvuNL8&ab_channel=ArtForYourTVBy%3A88Prints)

Or, you can use our [SDK](https://github.com/SuperpoweredAI/superpowered-python-sdk/blob/main/README.md) 🤓 :

**Step 1**: Install Superpowered SDK

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71445&key=user_uploads/733585/bc0b3af2-2a71-4e13-abfd-31c6f952e913)

**Step 2**: Create a Knowledge Base

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71445&key=user_uploads/733585/1d26ab88-cd54-42af-9d61-4064109a9835)

**Step 3**: Query from Knowledge Base

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71445&key=user_uploads/733585/bdc760ee-8337-4dc2-86e7-2cc496c7a47c)

### 👊 Why we built Superpowered AI

LLMs have emerged as a groundbreaking new technology and we are thrilled to be part of this revolution! But when LLMs are used on their own they have major shortcomings. For real-world use cases, we could see the importance of integrating additional functionality into them to overcome these issues.

1. **Access to external knowledge**. LLMs lack reliable knowledge and have none of your files to work with, but providing them access to knowledge will change your LLM app from a “neat toy” to a powerful tool for real-world use.
2. **Long-term memory**. Want to build a chatbot that remembers users’ preferences over long periods of time? You’ll need to store conversations and retrieve them later on.

### 🙏 Our Ask

1. Check out [Superpowered AI](https://superpowered.ai/) and join our [Discord](https://discord.gg/s2bE3MfG)!
2. Talk to us about your use case. If you’re building any kind of LLM application, there’s a very good chance we can help!

### 🚀 Sign up & chat with us:

Create your account and/or book a demo at [superpowered.ai](http://superpowered.ai), or email me at [dillon@superpowered.ai](mailto:dillon@superpowered.ai)
