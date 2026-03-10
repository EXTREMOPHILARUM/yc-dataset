# Launches

## Morphik: Open‑source multimodal RAG that works on technical docs

Hey YC! 👋 We’re Adi and Arnav, co-founders of Morphik (https://morphik.ai).

### **TL;DR**

* **Problem:** Knowledge workers spend a lot of their time searching complex documentation with diagrams, tables, or spreadsheets, just to find relevant information. Text‑only RAG misses details, hallucinates, and provides half-baked responses.
* **Solution:** Morphik embeds whole pages (image + text, no OCR), auto‑builds a knowledge graph, and serves it through a UI, SDK, or REST API. We have 90 % accuracy on arXiv QA (and we can fine-tune for your use case 🙂).

Watch our demo video: https://www.youtube.com/watch?v=3adZQhm5JZY

### **Problem**

RAG breaks the moment documents stop being blobs of text.

* Knowledge workers spend a lot of their time (people we spoke with said 50-70% time just in the research phase). eg. electrical engineers finding perfect PCB spec, pharma companies trying to search ELNs for similar experiments.
* 80% of enterprise knowledge lives in diagrams, tables, images, CAD, scanned pdfs, not .txt.
* “Multimodal” models still hallucinate or miss key context because the retrieval step sees only text, or they rely on tools to retrieve diagrams, or context. (https://docs.morphik.ai/blogs/gpt-vs-morphik-multimodal)
* Teams glue together OCR, vector DBs, and regex‑heavy ETL that becomes a brittle monstrosity.

### **Solution**

Directly embedding and search over page images

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdzvQJeEBmnvZI1Mkl2ZYCtsN0AG4Mx5JpcN4RtivMfndGshgTkj1uZcb8BkFAkXXNCpg9TPqeIKsqCXscaLzGDNO2e8TFn8naJPkJ_XtceDHlwNrAAcV69QGYlzSOwvdofI7FksQ?key=wmYsqYRKzN1ploJFaFpgwCeu)

When you ingest in Morphik, in addition to OCR, we create direct embeddings for the image of a page (or frames in a video). When you ask “Colpali comparison to standard RAG”, the LLM sees the actual page image, so multimodal models can reason over arrows, labels, scales, and colours just like a human.

### **Rules Engine**

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcOXXa3wTpZV26zi8kaucVOt2QuUgKKfrdvlyqlFfeHmDUudWpNaS-r6KNm5--4Joz4rE5tsiu_NDqlHnRE914l7ad4YtKRRLc_X1gm7BteBR0aMN446aia7LGA1l7b2UJMor97?key=wmYsqYRKzN1ploJFaFpgwCeu)

When ingesting, you can define rules for data extraction (which would again consider tables, diagrams), or define natural language rules for PII redaction, or content transformation.

### **Deployment ready, scalable**

Morphik comes built in with folder scoping, end user scoping, GPU accelerations, and fine grained permissions, so you can prototype and deploy with enterprise grade features. It’s end‑to‑end, so you don’t scramble to make duct tape fixes.

### **One more thing…Morphik Research Agent**

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcL9LvkrH861vRDhuFlYlBy0LsjlhMOYVBLRLdnj903G5L3QMgx12ziGZJhO_h2SzAakjD27e0Yeu4XZwmsE4Yv1BGNRj-OGc41i798xy_UW9MVHISzJy0GBrTsOWWqWBGdtGKhmg?key=wmYsqYRKzN1ploJFaFpgwCeu)

Our research agent uses Morphik’s retrieval, graph, and extraction APIs as tools. It chains them automatically, jumping from doc to doc, node to node, seeing figures, till it finds the needle in the haystack, or has enough context to answer your questions. “Describe the third pin on the USBC21 diagram” will get the diagram, find the pin, jump to the table with pin descriptions, jump to page 13 to “find more details on page 13”.

### **Why we might be interesting to you**

* Building an internal ChatGPT over messy manuals? Morphik is the fastest way to ship something users _trust_.
* Developing an AI product? Swap your vector‑DB‑plus‑duct‑tape stack for a single SDK call.
* Researching graph‑RAG? CAG? We have it all.

### **Our Ask 🙏**

1. **⭐ Star / watch** https://github.com/morphik-org/morphik-core – open source momentum matters.
2. **Introductions** to teams drowning in technical docs (healthcare, manufacturing, legal, electrical engineers).
3. Tell us **what still hurts in your RAG stack**, comment, **DM, or email** [founders@morphik.ai](mailto:founders@morphik.ai) or [book a call](https://cal.com/adityavardhan-agrawal-x6jyhq/30min).

Thanks for reading!

Adi & Arnav
