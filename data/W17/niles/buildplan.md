# Build Plan: Niles 2026

## Overview

By 2026, Niles is a Slack-native AI assistant that answers employee questions in real time by searching across Slack history, Google Drive, and Notion—with automatic knowledge capture and staleness detection built in. It targets operations and enablement teams at 25–200 person B2B SaaS companies where institutional knowledge is actively created but constantly scattered.

The viability shift is LLMs. GPT-4 and Claude 3 now deliver the semantic search accuracy that didn't exist in 2017–2020. Questions get answered correctly on the first try, not buried in false positives. Combined with Slack's mature Block Kit API, the product can now verify knowledge freshness with one-click buttons, turning passive indexing into an active knowledge maintenance system.

The go-to-market angle is surgical: land with ops and enablement teams who already own knowledge workflows, solve their immediate pain (answering repetitive questions), then expand to the broader org. Price as a per-seat SaaS product, not enterprise search. Win by being 10x faster to deploy and 100x cheaper than Glean, with zero implementation overhead.

## Why Now?

The single most important change since Niles failed is the arrival of production-quality large language models. GPT-4 (March 2023) and Claude 3 (March 2024) can perform reliable semantic question-answering over unstructured Slack conversations and documents with accuracy that simply did not exist between 2017 and 2020. This directly eliminates what the research identifies as Niles' primary failure cause: the NLP technology was not capable of delivering correct answers consistently enough to retain users. A knowledge bot that answers wrong trains users to stop asking — that loop is now broken.

The supporting infrastructure has matured in parallel. Retrieval-Augmented Generation (RAG) architectures, available today through open-source libraries like LangChain and LlamaIndex (both reaching production maturity in 2023), allow a small team to build a high-quality knowledge retrieval system in weeks. Vector databases — Pinecone (GA 2021), Weaviate, and pgvector — make semantic search over large Slack message corpora cost-effective as managed services. In 2017, this stack would have required months of custom ML engineering that a two-person team with $120K could not sustain.

Distribution has also matured significantly. Slack's App Directory now hosts 2,600+ apps serving 20M+ daily active users (Slack, 2023), and enterprise buyers have normalized purchasing Slack-native tools — a trust threshold that was not cleared when Niles launched. Microsoft Teams has added a parallel ecosystem with 320M+ monthly active users (Microsoft, 2023), doubling the addressable distribution surface.

Finally, the problem has gotten materially worse. Post-2020 remote and hybrid work has dramatically increased the volume of institutional knowledge buried in async Slack threads, making the core pain point Niles identified more acute and the willingness-to-pay more demonstrable than it was during the company's operating years.

---

## Current Market Analysis

The enterprise knowledge management market has grown substantially since Niles operated. The global knowledge management software market was valued at approximately $4.9 billion in 2022 and is projected to reach $13.4 billion by 2030 (Grand View Research — specific Niles-era baseline figure is not available for direct comparison). More relevant as a demand signal: Glean raised $200M at a $1B+ valuation in 2023 specifically for AI-powered workplace search, and Guru — Niles' most direct 2017 competitor — raised $30M+ in total funding and relaunched with AI features in 2023. These outcomes validate that the exact problem Niles identified carries massive enterprise willingness-to-pay.

## Current competitor map:

- **Glean** ($1B+ valuation, 2023): Targets large enterprises with broad workplace search across 100+ integrations. Weakness: expensive, complex deployment, minimum contract sizes that exclude SMBs and mid-market teams. Not Slack-native.
- **Guru**: Established knowledge base with browser extension and AI features. Weakness: requires deliberate content creation; the blank-page problem persists. Not conversational-first.
- **Notion AI** (launched February 2023): Strong document creation with AI assist. Weakness: still requires users to leave Slack; adoption depends on teams already living in Notion.
- **Confluence + Atlassian Intelligence** (2023): Deep enterprise penetration but notorious for the exact UX friction Niles was built to solve. Weakness: context-switching, poor search, stale content.
- **Microsoft Copilot for Teams** (GA 2024): Powerful but locked to Microsoft 365 ecosystem. Weakness: unavailable to Slack-native organizations; high per-seat cost.

**The gap**: No current competitor delivers a Slack-native, conversational knowledge layer that automatically captures answers from existing chat history without requiring manual content creation — at a price point accessible to teams of 20–500 people. That is the exact wedge Niles identified, now technically executable.

---

## Recommended MVP

### Core Feature 1: Conversational Q&A in Slack

A Slack bot that accepts natural language questions in any channel or DM and returns answers sourced from the team's indexed knowledge base, with citations linking to the source message or document. This is the original Niles core interaction, now powered by GPT-4 or Claude 3 via RAG over a vector database (Pinecone or pgvector). Unlike the original, accuracy is no longer the bottleneck — the MVP ships with a confidence threshold that routes low-confidence queries to a human expert rather than returning a wrong answer.

## Core Feature 2: Automatic Knowledge Capture from Slack History

On onboarding, the bot indexes the team's existing Slack message history (configurable lookback window, default 90 days) and identifies question-answer pairs using LLM classification. New answers posted in monitored channels are automatically added to the knowledge base without any manual action. This directly addresses the blank-page problem that defeated traditional wikis and was the original Niles insight — now technically reliable via LlamaIndex document loaders and GPT-4 classification.

## Core Feature 3: Staleness Alerts with One-Click Verification

Using Slack Block Kit (matured 2021+), the bot sends weekly digest messages to knowledge owners with inline "Still accurate / Needs update" buttons. This preserves Niles' original staleness detection feature but replaces email notifications with native Slack interactions, reducing the friction to near zero and making compliance measurable.

## Core Feature 4: Google Drive and Notion Integration

Index documents from Google Drive and Notion workspaces alongside Slack history, creating a unified semantic search layer. This matches Niles' original Google Drive integration but adds Notion (now a dominant knowledge repository) and uses vector embeddings rather than keyword search.

**What we will NOT build at MVP**: Salesforce integration, HR policy workflows, custom enterprise SSO, multi-workspace federation, or a standalone web interface. No horizontal expansion until one vertical is retained.

**Success metrics**: 40%+ weekly active usage rate among onboarded teams at 90 days; answer acceptance rate (thumbs up / no follow-up question) above 70%; net revenue retention above 100% at 6 months; 10 paying teams at $200+/month within 90 days of launch.

---

## Go-to-Market Strategy

**Target customer segment**: Operations, enablement, or team leads at Slack-native B2B SaaS companies with 25–200 employees — specifically teams experiencing onboarding friction or repetitive question fatigue in high-velocity Slack environments. This is the narrowest viable wedge: these buyers feel the pain acutely, have budget authority without lengthy procurement cycles, and are already comfortable purchasing Slack apps. Apartment List's sales operations team — Niles' one documented reference customer — is the archetype.

**Primary distribution channel**: Slack App Directory (2,600+ apps, 20M+ DAU). Tactics: optimize App Directory listing for "knowledge base," "wiki," and "onboarding" search terms; launch on Product Hunt targeting Slack-native operators; pursue placement in Slack's curated "Top Apps for Remote Teams" editorial lists. Secondary channel: targeted LinkedIn outreach to RevOps and Sales Enablement titles at Series A–C SaaS companies, where onboarding and knowledge decay pain is acute and documented.

**Pricing strategy**: $199/month flat for teams up to 50 Slack users; $399/month up to 150 users; $699/month up to 500 users. No per-seat pricing — team-level pricing reduces friction for the buyer and mirrors how Slack itself is evaluated. This is 8x Niles' original Starter price, justified by the dramatically higher answer accuracy and the validated willingness-to-pay demonstrated by Guru and Glean's growth. A 14-day free trial (no credit card) drives self-serve conversion through the Slack App Directory.

**Differentiation vs. 2026 competitors**: Glean is priced for enterprises and requires IT deployment. Guru requires manual content creation. Notion AI requires leaving Slack. The rebuild's differentiation is the combination of zero-setup knowledge capture (automatic indexing of existing Slack history), Slack-native conversational UX (no context switching), and SMB-accessible pricing — a combination no current competitor offers at this price point.
