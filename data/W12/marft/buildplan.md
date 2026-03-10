# Build Plan: Marft 2026

## Overview

Marft 2026 targets full-stack developers and small engineering teams building B2B SaaS products that need classification or regression models—teams too small to hire data scientists, too pragmatic to adopt enterprise platforms. The 2026 product is a single-purpose pipeline: upload labeled data, get a production-ready model artifact you own and control, integrate it with one line of code. Models export as portable ONNX or containerized inference servers that run anywhere—your infrastructure, not ours.

The market shift is simple: in 2012, ML was exotic. By 2026, every developer knows what a model is, cloud infrastructure is commodity, and the pain point has crystallized. SageMaker dominates enterprise but requires DevOps expertise to configure. There's no fast path for a solo engineer or small team. Marft fills that gap by removing all the infrastructure decisions—just data in, model out, your control.

Go-to-market is organic and native to where developers already live: GitHub, Hacker News, Vercel marketplace. Free tier removes activation friction. Win on portability (models run in your stack, not locked to our platform) and simplicity (no architecture design, no tuning knobs, no DevOps overhead). Charge when teams scale to multiple models and production monitoring.2f:T7af,

## Why Now?

## Current Market Analysis

The market Marft attempted to pioneer in 2012 — ML tooling for application developers — did not have a measurable commercial size at the time. By 2026, the MLaaS category is a multi-billion dollar segment within a broader AI infrastructure market. Precise 2026 market size figures are not available in the research report, but the trajectory from $1.58 billion (2017) toward a projected $200+ billion (early 2030s) places the current market in the tens of billions of dollars range. Exact 2026 figures should be verified against current analyst reports before fundraising.

## Competition map and gaps:

- **AWS SageMaker**: Dominant in enterprise, but notoriously complex to configure. Requires IAM expertise, VPC setup, and significant DevOps overhead. Weak for individual developers and small teams.
- **Google Vertex AI**: Strong AutoML capabilities but tightly coupled to GCP infrastructure. Vendor lock-in is a documented friction point; poor portability of trained models.
- **Hugging Face**: Excellent model discovery and community, but deployment tooling (Inference Endpoints) is expensive at scale and requires meaningful ML knowledge to configure fine-tuning pipelines correctly.
- **Roboflow**: Strong in computer vision specifically, but narrow in scope — not a general-purpose embeddable ML platform.
- **Obviously AI**: Targets business analysts, not developers. No API-first integration path; output is dashboards, not embeddable model artifacts.
- **Teachable Machine (Google)**: Prototype-grade only. No production deployment path, no custom data pipelines, no pricing model.

**The gap**: No current competitor offers a developer-first, framework-agnostic, bring-your-own-data pipeline that outputs a portable, embeddable model artifact (not just an API endpoint) with a sub-30-minute path from raw data to production integration. The hyperscalers own enterprise; the no-code tools own analysts. The working developer building a production app in 2026 is underserved.

**Demand signals**: Hugging Face's growth to 100,000+ public models and millions of monthly active developers confirms the self-serve ML workflow Marft attempted is now a high-demand pattern. Stack Overflow's 2024 developer survey (specific figures not available in research report) consistently shows AI/ML tooling as a top-priority investment area for engineering teams.

---

## Recommended MVP

## Core Features:

## Bring-Your-Own-Data Training Pipeline

Developers upload labeled datasets (CSV, JSON, or via API) through a web interface or CLI; the platform automatically selects and fine-tunes an appropriate base model from a curated set of open-weight options (Llama 3, Mistral 7B, or task-specific models from Hugging Face). This directly executes Marft's original vision — "Users submit data by we..." — but with 2026 infrastructure making it technically and economically viable. Unlike SageMaker, no cloud configuration is required; unlike Hugging Face Endpoints, the developer does not choose the model architecture.

## Portable Model Export (the "Embeddable" Differentiator)

Trained models are exported as self-contained artifacts: ONNX format for cross-framework compatibility, or as a Docker container with a pre-built inference server. Developers can run inference locally, in their own cloud account, or at the edge — without a runtime dependency on the Marft platform. This restores Marft's original "embeddable" distinction (models that run *within* the developer's application, not via a third-party API call at runtime), which no current competitor prioritizes.

## One-Line SDK Integration

A lightweight SDK (Python, JavaScript, Go) that wraps the exported model artifact and exposes a single `.predict()` method. The SDK handles input preprocessing, model loading, and output formatting. This reduces integration from hours to minutes and is the primary developer experience differentiator versus Hugging Face's Inference Endpoints, which require custom API call construction.

## Evaluation Dashboard with Drift Alerts

A simple web dashboard showing model accuracy metrics on held-out test data, plus automated alerts when production prediction distributions shift significantly from training distributions. This is a minimum viable MLOps feature that prevents the most common post-deployment failure mode for small teams without dedicated ML engineers.

## What we will NOT build (MVP scope):

- Custom model architecture design or neural architecture search
- Multi-modal pipelines (text + image + audio) — text and tabular data only at launch
- Real-time streaming inference
- On-premise enterprise deployment tooling
- A model marketplace or community hub

## Success Metrics (6-month thresholds):

- 500 developers complete a full training-to-export cycle (activation metric)
- 100 paying customers at any tier
- Median time from data upload to embeddable model export: under 20 minutes
- Month-3 retention of activated users: ≥ 40%
- Zero critical inference errors (model returns wrong output type) in production exports

---

## Go-to-Market Strategy

## Target Customer Segment:

Full-stack developers and small engineering teams (2–8 engineers) at B2B SaaS companies with $500K–$10M ARR, building products that require classification, ranking, or prediction features (e.g., lead scoring, content moderation, churn prediction, anomaly detection) but lack a dedicated ML engineer. These teams have budget, a clear use case, and active frustration with the complexity of SageMaker and the runtime dependency of pure API solutions. They are not data scientists and do not want to become one.

## Primary Distribution Channel:

Developer-led organic growth via GitHub and Hacker News, supplemented by the Vercel marketplace for reach into the full-stack developer community. Launch with a Show HN post featuring a live demo: "Submit a CSV, get a portable model in 15 minutes." Publish open benchmarks comparing export time and integration complexity against SageMaker and Hugging Face Endpoints. Marft's 2012 failure included zero community signal — this rebuild treats early Hacker News and GitHub traction as the primary leading indicator, not a vanity metric.

## Pricing Strategy:

- **Free tier**: 3 model training runs/month, up to 10,000 training rows, ONNX export included. Designed to eliminate friction for first-time activation.
- **Builder tier ($49/month)**: Unlimited training runs, up to 1M rows, Docker export, drift alerts. Targets the individual developer or small team.
- **Team tier ($299/month)**: 5 seats, priority GPU queue, SLA on training completion time, Slack support. Targets the small engineering team with a production use case.

Usage-based pricing is explicitly deferred until Series A — complexity kills self-serve conversion at the MVP stage. Flat-rate pricing mirrors the Stripe/Twilio early playbook that proved effective for B2D products.

## Differentiation vs. 2026 Competitors:

The rebuild wins on two axes no current competitor owns simultaneously: *portability* (models run in the developer's infrastructure, not ours) and *simplicity* (no ML knowledge required, no cloud configuration, one-line SDK). SageMaker owns complexity; Hugging Face owns community; Roboflow owns vision. The rebuilt Marft owns the "I just need this to work in my app by Friday" developer — the exact customer Marft identified in 2012 but could not reach.
