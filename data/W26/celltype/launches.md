# Launches

## CellType: The Agentic Drug Company

We're David and Ivan — we built this technology at Yale and are now turning it into a company.

AI is fundamentally changing how software gets built. Drug discovery is next.

# TL;DR

We're building an agentic drug company: **foundation models that learn human biology + AI agents that run the full discovery pipeline**. Instead of mice and cell lines, we simulate what will happen in patients — before you run the trial.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97885&key=user_uploads/1493577/d81c7718-831b-4ed3-8b76-c1f050d31193)

Our core technology, Cell2Sentence ([ICML 2024 paper](https://proceedings.mlr.press/v235/levine24a.html) · [C2S-Scale paper](https://www.biorxiv.org/content/10.1101/2025.04.14.648850v4)), was [featured by Google](https://blog.google/technology/ai/google-gemma-ai-cancer-therapy-discovery/) and shared by **Google CEO Sundar Pichai** (7M+ views). It teaches LLMs to understand cellular biology, and we've already used it to **discover and validate a new cancer treatment signal**.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97885&key=user_uploads/1493577/0b848ed1-640a-4601-bd61-54ab7d22f4f1)

# The Problem

90% of drugs fail in clinical trials. Most of that failure traces back to one thing: our preclinical models don't match humans. Mice and cell lines don't represent what actually happens in patients, so teams spend years and billions optimizing against the wrong reality.

And the process itself is broken: massive teams, manual workflows, siloed data, and painfully slow iteration. A typical drug takes 10+ years and $2B+ to develop. Most fail anyway.

[https://www.youtube.com/watch?v=MBlSLzVBnH8](https://img.youtube.com/vi/MBlSLzVBnH8/0.jpg\)%5C%5D\(https://www.youtube.com/watch?v=MBlSLzVBnH8\))

# Our Approach: AI Agents + A Virtual Human

We're building a new type of drug company from scratch around AI.

**The vision: AI agents do the work, humans steer the science.** Today, drug R&D means hundreds of scientists manually digging through literature, analyzing data, generating hypotheses, designing experiments, and coordinating with contract labs. We're replacing that with autonomous agents that execute end-to-end.

**The technology:** we taught LLMs to understand biology. Our core insight is that biology has structure, like language — gene expression profiles are sentences, cellular states encode meaning, drug responses are transformations. We built Cell2Sentence to convert single-cell biology into a form that foundation models can learn from. Unlike protein-centric approaches (AlphaFold, Boltz, ESM), we model the whole biological system — cells, tissues, microenvironments, and drug-cell interactions. **Proteins are parts; we model the machine.**

**The product:** a virtual human — a computational model of human biology you can test drugs on before touching a real patient. At every stage of development, you can ask "what will happen in humans?" and get an answer grounded in real human data, not proxies. Target discovery, toxicity prediction, translational prediction, patient stratification, virtual trials.

Our work is published at ICML 2024.

# Validation: We Discovered a New Cancer Treatment Signal

We didn't just build a model, we used it to find something real.

We screened 4,000+ drugs and predicted a novel hit: a drug that could help turn "cold" tumors "hot" (more visible to the immune system) — something that wasn't previously known. We then validated it in the lab — both in cell lines and in intact human tumor microenvironments that mirror what happens in patients. **The prediction held up.**

This is the kind of result that takes traditional R&D teams years.

# Traction

We're **already working with Top 10 pharma** — and every deal has been **100% inbound**. They saw the work and reached out to us.

# Our Team

We're two founders with deep expertise in biology + AI who invented the underlying technology together at Yale.

**David van Dijk, PhD:** Yale Professor, 11,000+ citations, published in Cell, Nature, ICML, and NeurIPS, turned down Google to build CellType.\
**Ivan Vrkic:** co-built the core tech at Yale (published at ICML), built software to control CERN's Large Hadron Collider, and led large-scale foundation model training at a biotech company.

# Our Ask

If you're a pharma or biotech team that wants to de-risk discovery and development — especially around translational and clinical prediction — we'd love to talk. We're also looking for data partners and exceptional bio and ML builders who want to help build an agentic drug company from scratch.

[david@celltype.com](mailto:david@celltype.com)
