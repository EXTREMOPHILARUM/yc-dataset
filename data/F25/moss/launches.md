# Launches

## Moss: Real-time Semantic Search for Conversational AI

Hello YC! We’re [**Sri Raghu Malireddi**](https://www.linkedin.com/in/r4ghu) and [**Harsha Nalluru**](https://www.linkedin.com/in/imharshanalluru/) from [**Moss**](https://usemoss.dev/).

### **TL;DR**

Moss is a high-performance runtime for real-time semantic search. It delivers sub-10 ms lookups, instant index updates, and zero infra overhead. Moss runs where your agent lives - cloud, in-browser, or on-device - so search feels native and users never wait. You connect your data once; Moss handles indexing, packaging, distribution and updates.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95036&key=user_uploads/2412081/c21db6f6-b453-40b6-a15d-5654971ab2ab)

### **The Problem**

If you’ve ever built a conversational or voice AI product, you’ve felt it - that awkward pause when your agent lags or hesitates. The illusion of conversation breaks, and suddenly it feels less like talking to intelligence and more like waiting for a page to load.

The culprit is almost always retrieval. Every query hops across networks and cloud databases, adding seconds of delay. As usage scales, those small lags snowball into lost users, rising infra and egress costs. Teams spend weeks rebuilding embeddings and indexes, tuning search infra just to get “good enough” answers instead of focusing on what actually matters: building great AI experiences!

### **Solution**

Moss puts real-time semantic search in the same runtime as your agent and application, so you can -

* **Keep retrieval close** - embed & index right alongside your agents (docs, chat history, telemetry).
* **Answer in &lt;10 ms** - local lookups, zero network hops.
* **Manage at scale** - store, sync, and distribute indexes with our managed data layer at [**https://usemoss.dev**](https://usemoss.dev)
* **Drop-in SDKs** - [**JavaScript**](https://www.npmjs.com/package/@inferedge/moss) and [**Python**](https://pypi.org/project/inferedge-moss/).

### **Our Story**

Moss founding team knew each other for 8+ years and bring deep expertise in machine learning, high-performance computing and developer experience.

Sri was an ML Lead at Grammarly and Microsoft, where he shipped LLMs and personalization systems used by millions of users across Office, Bing, and Grammarly. His work on personalization drove 300% retention growth for Grammarly Keyboard and scaling models to 40M+ DAUs. He has published at top ML conferences such as ACL and holds multiple patents in real-time ML.

Harsha was a Tech Lead @ Microsoft, where he architected the core stack of the Azure SDK, powering 400+ cloud services and 100M+ weekly downloads on npm. He also built foundational open-source tools and large-scale test automation systems. Earlier, ranked among the nation’s best in the Olympiads like the IMO and UCO, he combines analytical rigor with large-scale engineering expertise.

The idea for Moss came from our deep frustration with how slow “intelligent” systems actually felt in practice. While building large-scale agentic systems at Microsoft and Grammarly, we kept hitting the same wall - retrieval lag that made even the smartest models feel lifeless. Through evolution, humans are wired to expect instant replies; when AI hesitates, it breaks the illusion of intelligence. We started Moss to fix that by collapsing the multi-hop retrieval stack into a real-time, local-first runtime that lets AI think and respond at the speed of thought.

https://www.youtube.com/watch?v=7-PrunZVXTo

### **Who is it for?**

* **Platform/Founding Eng:** Drop in realtime semantic search. No new service to run.
* **Infra Leads:** Local retrieval to slash p95 and egress.
* **Agent/Voice PMs:** Hit &lt;10 ms so conversations feel natural.
* **Security/Compliance:** Keep sensitive context local (offline-ready).
* **Data/ML Eng:** A/B embeddings & index configs on your corpus - fast.

### **How to onboard?**

* Login to the portal - https://usemoss.dev 
* Start a new Project, create an index either through the portal or [JavaScript](https://www.npmjs.com/package/@inferedge/moss) and [Python](https://pypi.org/project/inferedge-moss/) SDKs

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=95036&key=user_uploads/2412081/ecd79cf8-972e-4233-9987-e015ad49abd8)

* Using our SDKs - **init**, **load** and **query** indexes in **sub-10ms**.

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=95036&key=user_uploads/2412081/60e783b7-d7d3-411a-91fd-05cbd678130a)


### **Our Progress**

We’re seeing strong inbound pull from the market with 6 enterprise design partners and 3 paying customers actively building their products around Moss’s core tech, with 7 more actively evaluating. We’re working closely with Voice AI orchestration companies like Pipecat ([Daily.co](http://Daily.co)) and LiveKit, embedding Moss at the core of their real-time retrieval and context pipelines. Usage and revenue have been growing \~100% week over week, and Moss is quickly becoming the foundational layer teams rely on to make AI feel instant, contextual, and truly responsive.

### **Ask**

* Building in Conversational AI and Voice AI?[ **Use Moss**](https://usemoss.dev) to bring real-time semantic search inside your agents to production
* Developers -[ **Get free access**](https://form.typeform.com/to/XWeuMaar) to experiment with Moss and help shape the future of real-time conversational AI.

Our contact information -

* Email - [**founders@usemoss.dev**](mailto:founders@usemoss.dev)
* Website - [**https://usemoss.dev**](https://usemoss.dev)
* Book a demo - [**Calendar Link**](https://cal.com/srimalireddi/30min)
