# Launches

## Metal - Your deal team assistant 🤘

⚡**TLDR**

* [Metal](https://www.getmetal.io/) is relaunching as a SaaS application for financial services and funds, with a focus on buy-side deal teams and portfolio monitoring for fund managers 🤘
* We make deal teams 10x faster by parsing data and assisting in diligence across relevant file types - transcripts, 10-Ks/Qs, financial statements, board decks, CIMs, and more
* Portfolio data is structured and made queryable for fund managers to better understand their investments – from running instant comps to extracting quotes from a board meeting
* We’re rolling out Metal on a fund by fund basis – if this sounds like you, please get in touch! [founders@getmetal.io](mailto:founders@getmetal.io) or [submit your contact info here](https://www.getmetal.io/contact) 🎸

**👎The problem**

Deal teams are overloaded with data, yet deals remain highly competitive and are lost with an inefficient diligence process. In early diligence alone, analysts spend days reading through expert call transcripts, 10-Ks, or financial statements just to get a basic understanding of a company. This is a highly manual process – and funds are paying analysts $200k/year and up to do it. 

On top of this, fund managers lack insights into their portfolio company’s historic performance, areas of focus, and if they’re deviating from plan. Tracking this data down internally is often infeasible, so managers are left in the dark and their investments are put at risk.

**👍Our solution**

Metal accelerates fund workflows by integrating them with the advanced capabilities of LLMs. Here’s how:

**1\. Purpose built ingestion pipelines for financial documents.** Funds can upload documents and specify the values they want extracted from datasets. Metal does the heavy lifting from there.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77440&key=user_uploads/1212950/591aea10-3d61-4c10-be1f-4b47ea9f7930)

**2\. Diligence workflows rebuilt with generative AI.** Metal extracts relevant quotes, cites sources, browses the web and more when generating responses.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77440&key=user_uploads/1212950/71312968-12bc-4380-8b3e-4c37d8aadc8d)

**3\. Fully searchable portfolios.** We structure and make all fund data queryable – from memos to board decks to financials. Spot patterns across collections of data and query for deeper insights.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77440&key=user_uploads/1212950/29e0a3b7-250f-4071-9aad-30c7f54d7e83)

**🙏 Asks**

Today’s launch is an exciting first step, but we’ve got a lot planned for the next 6 months!

We are rolling out Metal on a per fund basis so we can dedicate more of our resources to each implementation – we’ll work side by side with your team to ensure success.

**If you’re on a PE or VC deal team, or managing a fund** – here’s how you can reach us: [founders@getmetal.io](mailto:founders@getmetal.io) or [submit your info here](https://www.getmetal.io/contact)!

🤘Taylor + James + Sergio🤘

## Motörhead - LLM memory server built in Rust

## Overview

[Motörhead](https://github.com/getmetal/motorhead) is an open-source memory and information retrieval server for LLMs. Built and supported by [Metal](https://getmetal.io/).

As LLM usage becomes more widely adopted, modern software products must handle users' LLM interactions, chat sessions, and retrieval for relevant prompting context at scale. With much of the performance cost being on the prompting to APIs like OpenAI and other LLMs, contextual data retrieval is ideally as fast as possible.

## Features

* 🪄 Modern strategies to stay within the prompt window
* 💬 Chat session management out of the box
* 🦜 [Langchain integration](https://python.langchain.com/en/latest/modules/memory/examples/motorhead_memory.html)
* 🧠 Automatic Embedding generation via OpenAI ADA
* 🕸️ Redis Vector DB forto utilize RedisSearch (semantic)
* 💽 Short-term & long-term storage
* 🔥 Built in Rust for performance

## Roadmap

* User Authentication
* Knowledge Graph Memory handling
* Additional support for other Embedding Models
* [Create an issue!](https://github.com/getmetal/motorhead/issues)

## Resources

* Check out [Motörhead on Github](https://github.com/getmetal/motorhead)
* Join the [Motörhead Discord](https://discord.gg/sxbFX5dsQY)
* Suggest a [feature for Motörhead](https://github.com/getmetal/motorhead/issues)

## Metal: Helping developers easily implement machine learning embeddings

tl;dr

_Metal makes it easy for developers to implement machine learning embeddings. With embeddings, we help businesses create value from unstructured data like images, text documents, videos and more._

Hey everyone! We’re Taylor, James, and Sergio and we’re building [Metal.](https://www.getmetal.io/?utm_campaign=pre-launch&utm_medium=newsletter&utm_source=YC)

![](https://lh4.googleusercontent.com/BAmRW6DjuFBKZwKTqlBZ3usUOyMeRtO_c34yip0WO65CQX-VCS3IeNXKPOE57AdV-HApI_CC0QjqVgurwEDxHJSDo9BxV5Pve7VXz20yulLPBNYbSKHQXqSxhLowmbYOUlQ7c3sln6lJ4eRTuVMRmL0)

**What’s the problem?**

Embeddings are super powerful but they’re too hard to use. We learned this the hard way while building machine learning products at companies like Spotify and Meta. Getting to production for simple features (or so we thought) was incredibly painful.

The team would put weeks into offline training only for the data to be stale in production. It was difficult to iterate on models without versioning. Fine-tuning was highly inefficient. When we finally did get a model deployed there were immediate scaling concerns. It once took us 6 frustrating months to ship a simple embedding classification feature 🤦

Companies shouldn’t need to reinvent the wheel to use embeddings.

**What’s the solution?**

Metal gives you all the tools you need to quickly and easily implement embeddings against your data in production. 

* We integrate with your data sources
* We generate and store your embeddings
* We provide real time indexing and search APIs
* We provide versioning
* And we make it easier to fine tune embeddings via Metal’s API or SDKs

You can get started in as little as five minutes.

![](https://lh5.googleusercontent.com/izlgcDfSdm-FgMwj8Cns-nsnN2GmkAuUtdsSCQKuLawBY0fcv3KZjgkjiwxa7yiOpbPOnNZs_uN9ERNmCS8ZVVP3IC-NY-qHBe1cuipof9D7JKskIn6FvN-BSuYULjJGJPb6xYyi3e47OUDZ2qm9c4U)

![](https://lh4.googleusercontent.com/nOmwv8oD-qYgxa_m6enimIFMTirXP1olznsJv1UrojbT2lf69WdR0vxc2xLkX8TceIfAusPKPFopsM2vjXcGXIJMDMHQz9lgJhmxPr2qcOI3uS5_b7LI44k1HvaYeFSF2uGvHp1fpgMzuqVsU31sNaA)

**Ok so it’s easy to use, but what about some real world use cases?**

* Better personalization for your users through behavioral clustering
* Search and compare similarities between data types, such as images or videos
* Understand how your customers feel by classifying their free text reviews
* Make the most of internal resources by supporting semantic search of text documents, PDFs, call notes and more

**Our ask:**

1. [**Sign up for early access**](https://www.getmetal.io/?utm_campaign=pre-launch&utm_medium=newsletter&utm_source=YC) and we will get in touch! [You can also book a time here to learn more](https://calendly.com/metal-taylor/metal-30-minutes-landing?utm_campaign=pre-launch&utm_medium=newsletter&utm_source=YC).
2. **Introduce us to companies** who could use Metal. We mostly work with small to medium size companies (10-200 people) who have raised a series A. These companies have an embeddings use case but don’t want to spend the time/resources to build it from scratch.
3. **Help us build the future** :) If you’re experienced with embeddings and want them to be simpler, then we’d love to hear from you. Please get in touch: [founders@getmetal.io](mailto:founders@getmetal.io)

You can also follow us on [Twitter](https://x.com/metal__ai) or [Linkedin](https://www.linkedin.com/company/getmetal?utm_campaign=pre-launch&utm_medium=newsletter&utm_source=YC) :) 🤘

Thank you!
