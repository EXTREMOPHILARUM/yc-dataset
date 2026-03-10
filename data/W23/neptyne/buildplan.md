# Build Plan: Neptyne 2026

## Overview

By 2026, Neptyne returns as a focused AI-powered formula layer for Google Sheets—not a replacement spreadsheet, but a productivity multiplier for the 1.2 billion existing sheet users who hit Python-shaped problems daily. The product targets operations and finance analysts at mid-market SaaS companies who already live in Google Workspace and need to automate recurring analysis without leaving the sheet.

The timing window is real: Microsoft shipped Python in Excel last year, proving the market exists and validating the core thesis. But their implementation is sandboxed, Azure-locked, and requires manual code writing. Neptyne's insight is simpler—use LLMs to bridge the gap. A natural-language formula bar that converts "calculate cohort retention" or "flag anomalies in this column" directly into executable Python functions, cached and reusable, solves the actual friction point: analysts spend 40% of their time on repetitive transformations that live nowhere between spreadsheet formulas and full Python scripts.

The go-to-market is direct: land through Google Workspace procurement (lower friction than Excel enterprise sales), charge per-sheet or per-user, and let the product's speed advantage—turning a 20-minute Python script into a one-sentence formula—drive expansion into finance and ops teams that already have budget for tools.

## Why Now?

The single most important change since Neptyne's failure is that **Microsoft shipped Python in Excel in August 2023** — and rather than killing the market, it validated and expanded it. Enterprise users who had never considered Python in a spreadsheet context are now being trained to expect it. Microsoft's implementation, however, is constrained: it runs in a sandboxed Azure cloud environment via Anaconda, does not support arbitrary pip installs, has limited real-time interactivity, and critically, does not work inside Google Sheets — which holds an estimated 900 million users as of 2024 (source: Google, unverified by independent analyst). The gap Microsoft opened is now a distribution opportunity, not a competitive threat.

The second structural change is LLM code generation quality. GPT-4 (March 2023) could write passable Python; Claude 3.5 Sonnet (June 2024) and GPT-4o (May 2024) write production-quality pandas, NumPy, and API-integration code reliably enough that a non-programmer can describe a task in plain English and receive runnable Python. This collapses Neptyne's original adoption barrier: users no longer need to know Python to benefit from Python-in-spreadsheets.

Third, serverless Python execution infrastructure has matured dramatically. Modal Labs (launched 2022, production-ready by 2024) and Google Cloud Run now spin up isolated Python kernels in under 500ms at costs below $0.001 per invocation — making per-session compute economically viable at freemium scale in a way it was not in 2023.

Distribution is also cleaner. The Google Workspace Marketplace now hosts 5,000+ add-ons with established enterprise IT procurement workflows, and the Microsoft AppSource marketplace provides parallel access to Excel's commercial user base. Both channels were less mature when Neptyne operated.

---

## Current Market Analysis

**Market Size:** The global spreadsheet software market was valued at approximately $1.85 billion in 2023 and is projected to reach $3.2 billion by 2030 (source: Grand View Research — treat as directional, not precise). The more relevant segment — analyst-facing data tools including BI, notebooks, and spreadsheet-adjacent SaaS — is larger: Hex, Observable, and Mode Analytics have collectively raised over $300 million, confirming VC-scale demand exists for the Python-analyst bridge. When Neptyne operated in 2023, this segment was earlier-stage; enterprise procurement for notebook tools is now normalized.

## Competition Map:

- **Microsoft Python in Excel (2024):** Dominant distribution, but sandboxed Anaconda environment, no arbitrary pip installs, Azure-only execution, zero Google Sheets support. Weakness: locked to Microsoft's infrastructure decisions.
- **Hex (raised ~$52M as of 2023):** Excellent collaborative notebooks, but notebook-first UX requires Python fluency. No spreadsheet grid interface. Targets data scientists, not analysts.
- **Google AppSheet / Duet AI in Sheets:** AI formula suggestions, but no Python execution. Weakness: formula-only, no programmable logic layer.
- **Equals.app:** Strong financial modeling with SQL connectivity, but no Python runtime. Targets finance teams specifically.
- **Anaconda (powering Excel's Python):** Infrastructure provider, not a product competitor.

**Demand Signals:** Retool's 2024 State of Internal Tools report (source: Retool, unverified independently) noted spreadsheets remain the #1 internal tool at companies under 500 employees. The persistence of spreadsheet-first workflows despite better alternatives signals that switching cost, not awareness, is the barrier — which an add-on model directly addresses.

---

## Recommended MVP

**Core Feature 1 — AI-to-Python Formula Engine:** A natural-language input bar inside Google Sheets that generates and executes Python functions in cells using plain English descriptions (e.g., "pull last 30 days of Stripe revenue and calculate 7-day rolling average"). Unlike Neptyne's original implementation, which required users to write Python themselves, this feature requires zero Python knowledge. It uses Claude 3.5 Sonnet or GPT-4o for code generation and Modal Labs for sandboxed execution. This directly addresses Neptyne's core adoption barrier.

**Core Feature 2 — Persistent Python Kernel per Sheet:** Each Google Sheet gets a persistent, stateful Python environment (pandas, NumPy, requests, scikit-learn pre-installed) that survives between sessions and is shared across collaborators in real time. Unlike Microsoft's Python in Excel, arbitrary pip installs are supported. Unlike Neptyne's original product, this runs as a Workspace add-on — no tool switch required.

**Core Feature 3 — Scheduled Python Runs with Alerting:** Users can schedule any Python function to run on a cron schedule (hourly, daily, on data change) and push results back to the sheet or trigger a Slack/email alert. This targets the "living dashboard" use case — the single highest-retention workflow identified in Neptyne's original power-user cohort (trading systems, trackers).

**Core Feature 4 — One-Click Template Library:** Ten pre-built templates covering the highest-frequency analyst use cases: Stripe revenue pull, Google Analytics summary, stock price tracker, SQL query runner, OpenAI batch classifier. Reduces time-to-value from hours to minutes.

**What We Will NOT Build:** A standalone spreadsheet application, a Jupyter notebook interface, an Excel add-on (Phase 2 only), or a visual drag-and-drop workflow builder.

**Success Metrics:** 500 weekly active add-on installs within 90 days of launch; 8% free-to-paid conversion within 6 months; $10K MRR within 9 months; <2% weekly churn among paid users.

---

## Go-to-Market Strategy

**Target Customer:** Operations analysts and finance analysts at B2B SaaS companies with 50–500 employees who already use Google Workspace, run recurring reporting workflows in Google Sheets, and have heard of Python but do not write it themselves. This is narrower than Neptyne's original target (which included Python-native data scientists) and specifically excludes enterprise IT-gated environments in the first 12 months.

**Primary Distribution Channel:** Google Workspace Marketplace, supported by a Product Hunt launch and a targeted Hacker News "Show HN" post. The Marketplace's 5,000+ add-on ecosystem and established enterprise procurement workflows mean IT approval friction is lower than in 2023. Secondary channel: a YouTube tutorial series targeting "Google Sheets automation" search queries, which consistently rank high-intent and low-competition (source: anecdotal SEO observation — verify with Ahrefs before committing budget).

**Pricing Strategy:** Three tiers. Free: 50 Python executions/month, 3 templates, community support. Pro ($29/user/month): unlimited executions, scheduled runs, all templates, email support. Team ($79/user/month, minimum 3 seats): shared kernels, admin controls, priority support, SSO. Pricing is anchored below Hex ($24–$48/user/month) and above Google Workspace add-on median (~$10/user/month), justified by the execution infrastructure cost and the "analyst, not data scientist" positioning that commands less price sensitivity than developer tools.

**Differentiation vs. 2026 Competitors:** Microsoft Python in Excel requires Excel and sandboxes execution. Hex requires Python fluency. Google Duet AI offers no Python runtime. The rebuilt product is the only Google Sheets-native, AI-generated, unrestricted Python execution environment — occupying a gap none of the 2026 incumbents have closed.
