# Launches

## LanceDB 🍢 - serverless, low-latency vector database for AI applications

🙋 Are you building a generative AI app using an LLM or API? Are you working on a new recsys, a modern search engine, or a new analytical tool for unstructured data? Good news: you no longer have to struggle with Pinecone’s high cost, over the top complexity, or data privacy concerns.

🚀 [LanceDB](https://lancedb.com/) is a free and open-source vector database that you can run locally or on your own server. It’s lightning fast and is easy to embed into your backend server. Check out our [github repo](https://github.com/lancedb/lancedb) or pip install lancedb to get started.

For a quick demo, you can take a look at our sample [youtube transcript search app](https://github.com/lancedb/lancedb/blob/main/notebooks/youtube_transcript_search.ipynb). We’ll be adding a lot more soon. For more details on the API, take a look at [LanceDB docs](https://lancedb.github.io/lancedb/).

![](https://lancedb.com/images/eto-splash-arrow.png)


### **❓ Why we built LanceDB**

As we spoke to builders of ML/AI applications, a common refrain from users was struggling to get services like Pinecone even running. After a while, we realized that the retrieve-filter-hydrate workflow was often time a big bottleneck in productivity and app latency.

So we put our heads together. I was one of the original co-authors of the pandas library. Lei was a core-contributor to HDFS and led ML infrastructure at Cruise. Using our experience building data/ML tooling, we’ve built something totally new.

![uploaded image](https://bookface.ycombinator.com/media/?type=post&id=71382&key=user_uploads/858308/435bcc86-88ef-4c62-9f14-ba9d84c5c48f)


### **LanceDB ❤️ builders**

We’ve reimagined vector search from the ground up for better developer productivity, scalability, and performance. LanceDB is backed by [Lance format](https://github.com/eto-ai/lance) — a modern columnar data format that is an alternative to parquet. It’s optimized for high speed random access and management of AI datasets like vectors, documents, and images.

We then added our own Rust implementations of a number of SOTA ANN-index algorithms to support low-latency vector search. These indices are SSD-based and can easily scale wayyyy beyond memory.

What’s more, LanceDB allows you to store and filter other features along with vectors. Our users have been able to replace 3–4 different data stores with LanceDB alone and achieve a speedup at the same time.

### **🛣️ Roadmap**

Since our launch, the community has added LangChain support. Our integration for LlamaIndex is also under review. Our current focus is building a TypeScript implementation with a native-level experience. 

Currently, we provide a python package called lancedb which is pip installable and delivers a great local workflow. Beyond what we’re working on right now, here’s what you can expect:

* Ecosystem **integrations** into OpenAI plugin / AutoGPT etc
* Richer set of **embedding functions** and **document processing** conveniences
* **Gallery** of generative AI apps powered by LanceDB
* Solutions for **cloud** deployment

### **🙏 How to get started**

To get started with LanceDB head over to our [repo](https://github.com/lancedb/lancedb). If you have questions, feedback, or want help using LanceDB in your app, don’t hesitate to drop us a line at [contact@lancedb.com](mailto:contact@lancedb.com).
