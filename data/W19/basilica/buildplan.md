# Build Plan: Basilica 2026

## Overview

Basilica (YC W19, incorporated December 2018) built an embedding API that converted images and text into numerical vectors, enabling developers to train accurate ML classifiers from ~1,000 labeled examples rather than millions — but was killed within a year by platform aggregation, as Google (BERT), Hugging Face, and OpenAI absorbed its core value proposition into free offerings before Basilica could build the domain-specific moats it promised at Demo Day.

The rebuild thesis is not to re-enter the general-purpose embedding market — that market is closed — but to exploit the one structural gap the incumbents cannot fill: regulated industries where sensitive data cannot leave a controlled environment, and where R-native data scientists in pharma, clinical research, and financial compliance need domain-specific embedding and fine-tuning pipelines that run entirely within their own infrastructure. The new Basilica is a **private-deployment fine-tuning platform for regulated data scientists** — think Hugging Face Inference API, but air-gapped, R-native, and pre-configured for GxP and SOC 2 environments.

---32:T8d3,

## Why Now?

The single most important change since Basilica's failure is the emergence of parameter-efficient fine-tuning (LoRA/QLoRA), which first became practically accessible to small teams with the release of the `peft` library by Hugging Face in early 2023 and was validated at production quality by Meta's LLaMA 2 fine-tuning ecosystem (July 2023). This changes the rebuild calculus entirely. In 2019, building domain-specific embeddings that outperformed BERT required retraining large models — a compute and research problem a two-person team with $150K could not solve. In 2026, a small team can fine-tune a domain-specific embedding model on a customer's own hardware using QLoRA in hours, not weeks, at a fraction of the GPU cost. The technical barrier Basilica could not clear has collapsed.

The second structural change is data residency regulation. The EU AI Act (effective August 2024) and expanding state-level U.S. privacy laws (CPRA, state biometric statutes) have created hard legal constraints on sending regulated data — clinical trial records, financial PII, pharmaceutical formulation data — to third-party APIs. OpenAI's enterprise data processing agreements and Google's Vertex AI BAAs exist, but they do not satisfy the requirements of organizations operating under FDA 21 CFR Part 11, EMA GxP guidelines, or FINRA data handling rules, where auditability of the model training pipeline itself is required. This is not a preference gap; it is a compliance gap. OpenAI cannot solve it by adding a checkbox.

On market size: the global MLaaS market was estimated at $21.1B in 2024 and is projected to reach $113B by 2029 (MarketsandMarkets, 2024 — exact figures should be independently verified). The regulated-industry AI tooling sub-segment does not have a clean public estimate, but the pharma AI market alone was estimated at $1.5B in 2023 (Grand View Research). Specific distribution channels now available that did not exist in 2019 include the AWS Marketplace (with HIPAA-eligible listing infrastructure), Posit Package Manager (formerly RStudio Package Manager, serving R-heavy enterprise environments), and the Databricks Partner Connect ecosystem, which provides direct access to data science teams in regulated enterprises.

---

## Current Market Analysis

**Market size.** The general embedding API market in 2019 was nascent and unquantified. By 2026, it has consolidated around OpenAI (text-embedding-3-small/large, launched January 2024), Cohere (Embed v3, October 2023), and Voyage AI (acquired by Anthropic, 2024). The regulated-industry fine-tuning segment has no dominant player and no clean market size estimate — this should be stated honestly. Proxy signals: the clinical NLP market is estimated at $300M–$500M (various analyst reports, figures should be independently verified), and the demand for on-premise LLM deployment in pharma and finance is evidenced by the rapid growth of private LLM deployment tools like Ollama (1M+ downloads as of late 2024) and the enterprise traction of Anyscale and Modal for private inference.

## Competition map and gaps.

- **OpenAI Embeddings API**: Dominant for general use. Cannot be used for data that cannot leave the customer's environment. No R client. No fine-tuning pipeline for embeddings specifically. Weakness: compliance ceiling.
- **Hugging Face Inference API + AutoTrain**: Closest functional analog to the rebuild. Has an on-premise option (Hugging Face Enterprise Hub, launched 2023) but is Python-first, requires significant MLOps expertise to configure for regulated environments, and has no GxP-ready deployment templates. Weakness: implementation complexity for non-ML-specialist data scientists.
- **Cohere**: Offers private deployment via Cohere for Enterprise. Strong NLP focus. No R client. No image embedding. Weakness: not R-native, limited regulated-industry go-to-market.
- **AWS SageMaker**: Covers the infrastructure layer but requires customers to assemble the fine-tuning pipeline themselves. HIPAA-eligible. Weakness: not a product, it's a platform — the data scientist still does all the work.
- **Vertex AI (Google)**: Similar to SageMaker. BAA available. Weakness: same assembly-required problem, no R-native tooling.

**The gap**: No current product offers a turnkey, R-native, GxP-ready fine-tuning and embedding pipeline that runs entirely within a customer's VPC or on-premise environment. This is the gap.

**Defensibility against platform incumbents.** The honest answer is that AWS, Google, and Microsoft could build this. The structural reason they have not — and are unlikely to prioritize — is that the regulated-industry segment requires compliance certifications (FDA 21 CFR Part 11 validation documentation, SOC 2 Type II, HIPAA BAA with audit trail support) that are expensive to maintain and represent a small fraction of their total addressable market. A focused rebuild can achieve these certifications as a core product feature, not an afterthought, and build the domain-specific model library (clinical NLP, pharmaceutical document classification, financial regulatory text) that incumbents have no incentive to curate. The moat is compliance depth plus domain specificity — not raw model quality.

---

## Recommended MVP

### Core Feature 1: Private VPC Deployment with One-Command Setup

A Helm chart and Terraform module that deploys the embedding and fine-tuning stack entirely within the customer's AWS, Azure, or GCP environment — no data leaves the customer's perimeter. This matters because it is the hard compliance requirement that OpenAI and Cohere cannot satisfy for regulated customers. Unlike Basilica's hosted API, this is an on-premise-first product; the hosted option is secondary.

## Core Feature 2: R-Native Client with Posit Integration

A first-class R package (submitted to CRAN and Posit Package Manager) that wraps the fine-tuning and embedding API with tidyverse-compatible interfaces. This directly addresses the underserved segment Basilica's R client hinted at but never pursued as a go-to-market wedge. Unlike Basilica's R client, which was a thin wrapper on a hosted API, this client works against the customer's own deployed instance.

## Core Feature 3: Domain-Specific Base Model Library

Pre-packaged fine-tuned embedding models for three initial verticals: clinical/biomedical text (built on BioBERT and PubMedBERT foundations), pharmaceutical regulatory documents (FDA submissions, EMA dossiers), and financial compliance text (SEC filings, FINRA communications). Each model ships with benchmark accuracy on public domain datasets so customers can evaluate before deploying. Unlike Basilica's generic embeddings, these are vertical-specific from day one — the moat Basilica claimed but never built.

## Core Feature 4: Managed QLoRA Fine-Tuning Pipeline

A UI and API for customers to upload labeled examples (target: functional with 500–2,000 examples) and trigger a fine-tuning run on their own GPU infrastructure, with experiment tracking and model versioning built in. This is the "1,000 examples instead of 1,000,000" value proposition from Basilica, now technically achievable via QLoRA (validated by the `peft` library, 2023) without requiring the customer to understand the underlying method.

**What we will NOT build:** A general-purpose hosted embedding API competing with OpenAI. Image embeddings (Phase 1). A Python-first product. Consumer-facing tooling.

**Success metrics:** 10 paying enterprise customers within 12 months of launch, each paying ≥$2,000/month. Average fine-tuning job accuracy improvement of ≥15% over generic base models on customer-provided held-out test sets (this validates the domain-specific moat). Net Revenue Retention ≥110% at month 12.

**Cold-start note:** This product does not depend on network effects or local density. Each customer deployment is independent. The domain model library improves with more customers only if customers consent to federated learning — which should be offered but not required, and not promised as a moat until demonstrated.

---35:Tacb,

## Go-to-Market Strategy

**Target customer segment:** Data scientists and computational biologists at mid-sized pharmaceutical companies (200–5,000 employees), CROs (contract research organizations), and financial compliance teams at regional banks and asset managers — specifically teams that already use R as their primary analytical environment, have labeled datasets they cannot send to external APIs, and are blocked from adopting commodity embedding tools by their IT security or compliance function. This is narrow by design. The R-user constraint alone filters to an estimated 2–3 million active R users globally (TIOBE, 2024 — verify independently), with the regulated-industry subset being a small but high-willingness-to-pay fraction.

**Primary distribution channel:** Posit (formerly RStudio) ecosystem — specifically CRAN submission, Posit Package Manager listings, and sponsorship of posit::conf (the primary R conference, ~2,000 attendees annually). Secondary: AWS Marketplace listing with HIPAA-eligible designation, which surfaces the product to procurement teams already evaluating AWS for regulated workloads. Direct outreach to R user groups in pharma (R/Pharma conference, ~500 attendees, highly targeted) is the highest-leverage early channel.

**Pricing strategy:** $2,000–$5,000/month per deployment (VPC-deployed, unlimited users within the customer environment), with a one-time onboarding and validation fee of $5,000–$15,000 for customers requiring GxP validation documentation. Stress-test against free alternatives: a data scientist at a pharma company can use Hugging Face `transformers` locally for free. The rebuild's price is justified by three things the free alternative does not provide: (1) GxP validation documentation that satisfies FDA audit requirements — this alone can cost $50,000+ to produce internally; (2) R-native interfaces that eliminate Python environment setup for R-primary teams; (3) domain-specific base models that demonstrably outperform generic alternatives on regulated-industry text. The subscription is not competing with a free tool that does the same thing — it is competing with a $50,000+ internal IT project to achieve the same compliance posture.

**Differentiation vs. 2026 competitors:** Hugging Face Enterprise Hub is the closest competitor and should be named directly in sales conversations. The differentiation is compliance depth (pre-built GxP validation packages vs. DIY), R-first UX (vs. Hugging Face's Python-first design), and domain model library (vs. Hugging Face's general model zoo requiring customer curation). Cohere for Enterprise is a secondary competitor; differentiation is on-premise deployment (Cohere still requires data to reach Cohere's infrastructure) and R-native tooling.
