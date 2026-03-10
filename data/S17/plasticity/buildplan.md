# Build Plan: Plasticity 2026

## Overview

By 2026, Plasticity is a focused API layer for extracting structured data from long-form documents—contracts, clinical notes, intelligence reports—with guaranteed accuracy and compliance-grade auditability. It's built for legal tech companies, healthcare systems, and federal agencies that can't afford hallucinations or data leakage. The product is language-agnostic, works offline, and integrates with existing LLM stacks rather than replacing them.

The shift that makes this viable now: LLMs are commodity infrastructure, but they're unreliable for high-stakes extraction. The market has moved from "can we do NLP?" to "can we do it safely and provably?" Plasticity solves the extraction layer that every enterprise LLM deployment actually needs—the part that turns raw model output into structured, auditable, legally defensible data.

The go-to-market angle is direct: sell to legal operations teams and compliance officers who are already buying LLM tools but can't deploy them without a guardrail layer. Start with contract extraction—the highest-ROI, lowest-risk entry point—then expand into healthcare and federal. Win by being the extraction standard that enterprises trust enough to put in production.34:T842,

## Why Now?

## Current Market Analysis

**Market Size:** The global NLP market exceeded $18 billion in 2023 (source: research report). No comparable figure exists for 2017 in the research report, though the report characterizes the 2017 commercial market as immature and not yet ready for paid developer API adoption at scale. The directional shift is unambiguous; precise CAGR figures are not available in the source material.

**The Specific Gap:** The current market is crowded at the general-purpose layer but thin at the domain-specific structured extraction layer. Hugging Face (valued at $4.5B, source: research report) dominates model hosting and open-source tooling but does not offer opinionated, production-ready extraction pipelines for specific verticals. Cohere and AI21 Labs compete on general LLM APIs. OpenAI's API is the default entry point for most developers but provides no vertical-specific structure, compliance tooling, or on-premise deployment for regulated industries.

## Named Competitor Weaknesses:

- **OpenAI API:** No structured output guarantees for complex multi-entity extraction; data retention policies disqualify it for most federal and healthcare use cases; no fine-tuning transparency.
- **Hugging Face:** Excellent model repository, weak on managed inference, enterprise SLAs, and opinionated vertical pipelines; requires significant developer assembly.
- **AWS Comprehend:** Strong distribution, weak on semantic depth; still relies on pattern-based entity recognition that underperforms LLM-based extraction on complex documents.
- **Cohere:** Strong on enterprise search and RAG; limited on structured information extraction and dialogue management for regulated verticals.

**Demand Signals:** The disinformation detection vertical — a documented Plasticity use case — now has confirmed buyers at DARPA and CISA (source: research report). Legal document analysis and clinical NLP are adjacent markets with demonstrated willingness to pay, consistent with Plasticity's reported "hundreds of companies in technology, law, and medicine" customer description (unverified, source: research report).

---36:T976,

## Recommended MVP

## Core Features:

## Go-to-Market Strategy

**Target Customer Segment:** Mid-market legal technology companies and legal operations teams at enterprises with 500–5,000 employees, specifically those processing high volumes of contracts, discovery documents, or regulatory filings. This segment was identified in Plasticity's own customer description (source: research report) as a high-value vertical where keyword matching clearly fails. It has a documented willingness to pay for accuracy, is reachable without a large enterprise sales team, and has procurement cycles faster than federal government.

**Primary Distribution Channel:** Hugging Face Hub as top-of-funnel, with a permissively licensed open-source extraction library (following the Magnitude playbook from EMNLP 2018, source: research report) that drives developer discovery. The commercial tier — managed API, fine-tuning interface, SLA guarantees, on-premise deployment — sits behind a paid tier. Hugging Face's 500,000+ model community provides organic distribution that Plasticity's 2017 press-and-Demo-Day strategy could not replicate. Secondary channel: AWS Marketplace listing for enterprise procurement teams who require vendor approval workflows.

**Pricing Strategy:** Usage-based API pricing at the entry tier (per 1,000 pages processed), with annual enterprise contracts for the fine-tuning interface and on-premise deployment. Justification: usage-based pricing matches the Twilio analogy Plasticity originally pitched and aligns cost with customer value delivery. Annual contracts for enterprise features provide the revenue predictability that Plasticity's commercial phase lacked, without requiring the government contract dependency that foreclosed the original mission.

**Differentiation vs. 2026 Competitors:** The rebuild wins on three axes that current competitors do not simultaneously address: domain-specific accuracy (not general-purpose), on-premise deployment (not cloud-only), and no-code fine-tuning (not raw API). OpenAI cannot offer on-premise. AWS Comprehend cannot offer LLM-grade semantic depth. Hugging Face cannot offer opinionated vertical pipelines with enterprise SLAs. The combination is the moat.
