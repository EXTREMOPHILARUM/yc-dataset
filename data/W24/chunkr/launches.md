# Launches

## Chunkr: Open Source Document Parsing You Can Own

Hi all, we’re Mehul, Ishaan and Akhilesh - co-founders of [Chunkr](https://chunkr.ai/). 

**TLDR:** We built Chunkr to solve the one-size-doesn't-fit-all problem in document parsing for RAG/LLM applications. **Get granular control over your pipeline to balance speed, quality and features - like a tool you built in-house, minus the headache.**

<https://www.youtube.com/watch?v=2Iy5ssyeneA>

We were initially building Lumina, the AI search engine for scientific literature. The biggest undertaking was developing a document ingestion pipeline that could process \~600M pages of scientific literature and extract everything we needed to build a great RAG experience. The OG "deep research".

Document processing solutions on the market couldn't deliver the performance, observability and features needed to win our trust. So we built parsing in-house - and spent so much time fighting foundational problems that we pivoted to solve the underlying challenge itself. **That's how Chunkr was born - with a singular goal to build document ingestion infra that devs can love.**

# **The Problem**

We released an API and easy to self-host pipeline in October 2024 as a test and didn’t expect much. What we ended up with was a very viral launch (400K impression) - and a year worth of learnings condensed down to 2 weeks. 

By Nov 2024 - we had processed documents across verticals like healthcare, finance, research, government, education and hardware for RAG/LLM use-cases. Beyond common issues like bounding boxes for citations, accurate HTML/MD extraction, and chunking - it became clear that document parsing isn’t one size fits all.  Some of the cases we ran into: 

"I just need fast, simple full page OCR - leave out the rest"

"We need custom VLM processing for specific pages/segments (formulas, chart-to-table conversion)"

"Give us high-res crops of specific document sections"

"Everything must run in our self-hosted VPC"

“Can we apply our own chunking strategy”

# **The Solution**

Chunkr gives you “knobs” to balance **speed**, **quality**, and **features** depending on your use case - like a tool you built in-house, minus the headache. Being open source means minimal lock-in, and a variety of integration options. 

**_🧩 Working at the segment level_**

This is where layout analysis really shines. Break a page into bounded titles, tables, formulas, captions etc (we call these segments) - and the downstream processing options are vast. 

Each segment can be configured differently: fast OCR for text, VLMs for complex elements like tables and formulas, optional high-res image cropping, custom prompts for charts and image descriptions.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88079&key=user_uploads/1371678/766f2d65-e01b-43ff-acb6-ffed1df4b697)

Abstractions have been kept to a minimum while maintaining a smooth DX. It’s everything you could need for generating great RAG data on your own terms. 

At a higher level - you can configure a host of other options like layout analysis provider and chunking strategy. No matter how gnarly the document is, there’s a config that can work! Another great advantage is a pipeline that can stand the test of progress. As VLMs improve every week - Chunkr gets better as well. 

**_🛠️ Production ready API / Self-host_**

The pipeline comes with all the last-mile engineering you need for production use-cases. We’ve built it all in Rust to offer great performance & reliability. Tasks like image conversions, page parallelization, reading order, failure handling and batching are taken care of. 

Self-hosting is simple with ready to go dockers + helm charts. Processing speed is  around 4 pages per second on a single RTX 4090, which is enough to handle over 11 million pages per month. Renting that hardware on Runpod costs about $249/month, so the math is pretty compelling. 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88079&key=user_uploads/1371678/22a8f22e-ee67-43d7-b82e-808374f382dc)

# **Asks**

**Try out **[**Chunkr (https://chunkr.ai/)**](https://chunkr.ai/)** - and **[**share feedback**](https://cal.com/mehulc/30min)** with us.** We support PDFs, office file types (docx, ppt, excel), and images. Get started for free with our no-code playground, raw post requests, or use our python package! Our dashboard gives you all the visibility needed to evaluate quality in seconds. 

[**Give our repo a star! (https://github.com/lumina-ai-inc/chunkr)**](https://github.com/lumina-ai-inc/chunkr)

**Email: **[**team@chunkr.ai**](mailto:team@chunkr.ai)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88079&key=user_uploads/1371678/ee3ebfdf-2f3b-4321-b249-e8a99abb8ccc)

## ⚛️  Lumina - Accelerating Research with AI  🚀

👋 Hi everyone, we’re Mehul, Ishaan & Akhilesh - the founding team behind [Lumina.](https://www.lumina-chat.com) Our research suite leverages LLM’s to help >8000 researchers discover, validate and curate scientific literature.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77459&key=user_uploads/1371678/0483ddd4-8e6a-4b50-a672-daa952488356)

Mehul is a Materials Scientist and worked in Atom Probing R&D, Akhilesh is a national robotics champion and has experience as a Cloud Solutions Architect, and Ishaan studied AI and worked as a Data Engineer. 

❓ **The Problem:** _Why does research take so long?_

[Science is slow.](https://www.lumina-chat.com/share/chat/91c1d8d7-a68b-489e-8818-b2f24a5d1625) Most research, whether academic or in industry, takes months or years to do. Researchers have to dig through 100s, if not 1000s of scientific papers during this process, and have to vet and extract key insights that are relevant to their project. 

As of now, a majority of the community depends on basic key-word search and manual skimming processes to do so - while wrestling paywalls. This can take anywhere from weeks to years.

💡 **The Solution:** _An AI-powered Research Suite_

We want to give researchers more time to do what's important. Lumina helps them cut the discovery and validation process down to minutes.

<https://youtu.be/uX-Y7_LcWhI?si=LwZ8JgcExuwcjz4V>

Some key features are:

* 📚 **Mini Lit-Reviews:** Our answers find the most relevant sources for your query, and cite the key sections used from each journal article.
* 📊 **Tables:** Extract key information from every source from the search - create a custom query, or use a preset to speed things up.
* 🤖 **Agents:** Query multiple papers at once - connect our library and your collection for complex research tasks.

🌟 **Vision:** _Speed up the entire scientific process_

We will be augmenting the entire scientific process with AI. We’re building tools that will speed up data analysis, simulate experiments to generate data, bring multimodality and even write entire systematic reviews in one-click. The goal is to create an AGI-like experience for scientific research.

🙏 **Our Ask:**

📢 Try Lumina and let us know your thoughts!

🤝 Connect us to academic and private research groups.

Here’s a Calendly link for a short 15 min convo:

📅 <https://calendly.com/mehul-yem/lumina-experience-interview>

📧 You can reach us at [mehul@lumina-chat.com](mailto:mehul@lumina-chat.com)

We’re also providing a 50% discount for Lumina Plus to celebrate our launch! Simply use this code on checkout: LAUNCHYC24
