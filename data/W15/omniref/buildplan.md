# Build Plan: Omniref 2026

## Overview

The 2026 Omniref targets engineering teams of 10–75 developers shipping software with heavy open-source dependencies. It's a VS Code extension that surfaces AI-generated plain-English annotations for every third-party package in your dependency tree on first install, then lets teams layer persistent version-tracked notes on top. The product lives where developers already read code — inline in the editor — not in a separate web platform.

The viability shift is LLMs. In 2017, cold-starting a code annotation network required either massive manual effort or a critical mass of user-generated content. Now GPT-4o and Claude can generate accurate, contextual package documentation instantly. That solves the chicken-and-egg problem that killed the original product.

Go-to-market is freemium through the VS Code Marketplace (30M+ active users). Individual developers get AI annotations free. Teams pay $15/seat/month for persistent collaborative notes and version-aware anchoring. The wedge is dependency comprehension — a problem every growing engineering org has but no one has solved well. Sourcegraph owns monorepo search; Copilot owns code generation. This owns the knowledge layer between your code and the packages it depends on.34:T8bc,

## Why Now?

The single most important change since Omniref's failure is this: **LLMs have eliminated the cold-start problem that made the original product structurally unbuildable as a business.** Omniref's annotation layer was only valuable after a critical mass of developers contributed content — but those contributors were open-source developers who qualified for the free tier and had no incentive to pay. In 2026, Claude 3.5 Sonnet (June 2024) and GPT-4o (May 2024) can generate contextually accurate, line-level code annotations on day one, before any human community forms. The product ships useful. The cold-start problem is gone.

The second structural unlock is proven willingness to pay. GitHub Copilot reached 1.8 million paid subscribers by early 2024 at $10–$19/month (GitHub, 2024), and Cursor reported $100M ARR in 2024 at similar price points. These benchmarks directly refute the assumption that developers won't pay for workflow-embedded code intelligence tools. Omniref's $50/month tier failed partly because the value wasn't immediate enough to justify the price. At $15/month with AI-generated annotations available instantly, the conversion math changes fundamentally.

The underlying market has also grown materially. The npm registry expanded from ~600,000 package versions in 2015 to over 2.5 million packages as of 2024 (npm, 2024 — exact figure unverified independently). Navigating underdocumented dependencies is proportionally more painful. Sourcegraph's $225M raise and enterprise adoption validates that companies will pay substantial sums for codebase navigation tools — the exact problem Omniref addressed.

Distribution channels unavailable in 2015 now exist at scale: the VS Code Marketplace has over 50,000 extensions with 30M+ active users (Microsoft, 2024), and JetBrains Marketplace serves 12M+ developers. Embedding directly in the IDE — where developers already live — eliminates the context-switching friction that killed Omniref's browser plugin strategy.

Semantic search via pgvector (PostgreSQL extension, GA 2023) and Pinecone now enables intent-aware code retrieval that would have required years of ML infrastructure in 2015. A two-person team can implement this in weeks today.

---

## Current Market Analysis

**Market Size:** The global developer tools market was valued at approximately $6.8 billion in 2023 and is projected to reach $13.7 billion by 2028 (MarketsandMarkets, 2023 — treat as directional; independent verification recommended). The specific segment of code intelligence and documentation tooling is harder to isolate, but Sourcegraph's $2.6B valuation (2021) and GitBook's continued growth suggest the addressable market for "understanding code at scale" is well into the billions. In 2013–2015, this segment was nascent; today it is a recognized enterprise budget line item.

## Competition Map and Gaps:

- **Sourcegraph** — The most direct enterprise competitor. Strong on code search across large monorepos; weak on dependency-level annotation, package-specific knowledge, and per-developer pricing accessible to teams under 50 engineers. Minimum viable deal size is reportedly $50K+/year, leaving the mid-market exposed.
- **GitHub Copilot** — Dominant for inline code generation; does not surface persistent, version-aware annotations or community/team knowledge attached to specific library versions. It generates, it doesn't explain or remember.
- **Cursor** — IDE-native AI coding assistant with strong adoption; focused on generation and refactoring, not on annotating third-party dependencies or preserving institutional knowledge about external packages.
- **GitBook / Notion** — General documentation tools that developers use for internal wikis; not version-aware, not code-line-specific, not integrated with package registries.
- **Stack Overflow** — Still dominant for Q&A but structurally version-agnostic. A Stack Overflow answer about a Rails 6 bug is surfaced identically when you're running Rails 7.2. No version awareness. No attachment to source.

**The gap:** No current tool combines (a) AI-generated, version-aware annotations on third-party dependencies, (b) team-layer knowledge that persists across package upgrades, and (c) IDE-native delivery at mid-market pricing. That gap is the rebuild opportunity.

**Demand signals:** Obsidian reached 1M+ users paying for sync and publish features, demonstrating annotation-as-product willingness to pay among technical users. Developer experience (DevEx) has become a formal engineering budget category at companies over 50 engineers, creating a procurement path that didn't exist in 2015.

---

## Recommended MVP

## Core Features:

## AI-Generated Dependency Annotations (Powered by GPT-4o / Claude 3.5 Sonnet)

On first install, the product automatically generates plain-English annotations for every third-party package in a project's dependency tree — explaining what each package does, flagging known deprecation patterns, and surfacing version-specific behavioral changes. This directly eliminates Omniref's cold-start problem: the product is useful before a single human annotation exists. Unlike Omniref's community-dependent model, value is immediate and individual.

## Version-Aware Team Annotation Layer

Engineers can attach persistent notes to specific lines of third-party source code, anchored to a package version. When a dependency upgrades, the system flags affected annotations and prompts the team to review or migrate them. This is Omniref's core technical differentiator — version-tracking annotation — rebuilt with modern infrastructure (pgvector for semantic anchoring, not brittle line-number matching). Unlike GitHub comments, these annotations travel with the dependency version, not with a PR.

## IDE-Native Delivery via VS Code Extension

All annotations — AI-generated and team-authored — surface as inline decorations inside VS Code, the editor used by approximately 73% of professional developers (Stack Overflow Developer Survey, 2023). Developers see relevant annotations without leaving their editor. This solves the context-switching problem that made Omniref's browser plugin a secondary habit rather than a primary one.

## What We Will NOT Build (MVP):

- Public community annotation layer (the original Omniref model — reintroduce only after team-layer proves willingness to pay)
- Support for more than three package ecosystems at launch (npm, PyPI, RubyGems)
- Mobile or web-only interfaces
- Custom documentation hosting

## Success Metrics:

- 500 paying teams (≥3 seats) within 12 months of launch
- 40%+ week-4 retention among activated teams
- Average annotation engagement rate ≥ 60% (annotations viewed per active user per week)
- $15K MRR within 6 months

---

## Go-to-Market Strategy

## Target Customer Segment:

Engineering teams of 10–75 developers at Series A–C software companies with significant open-source dependency surface area — specifically teams shipping Node.js, Python, or Ruby applications who have experienced at least one production incident caused by an undocumented dependency behavior or surprise breaking change. This is narrow by design. These teams have a DevEx budget, a technical decision-maker (Staff Engineer or Engineering Manager), and a visceral memory of the pain the product solves.

## Primary Distribution Channel:

VS Code Marketplace (30M+ active users, Microsoft 2024) as the top-of-funnel acquisition channel, with a freemium individual tier (AI annotations only, no team layer) converting to a paid team tier. The install-to-trial flow must be under 90 seconds. Secondary channel: targeted outreach via developer communities on Discord servers for major frameworks (Next.js, FastAPI, Rails) where dependency pain is actively discussed.

## Pricing Strategy:

- **Free:** AI-generated annotations for individual developers, single-user, read-only team annotations
- **Team:** $15/seat/month (minimum 3 seats, $45/month floor), includes team annotation layer, version-change alerts, and Slack/Linear integration

Justification: $15/seat benchmarks directly against GitHub Copilot's proven conversion price point. The 3-seat minimum ensures the team-layer value proposition is experienced from day one and filters out individual users unlikely to convert. This avoids Omniref's fatal error of pricing at $50/month for a product whose value wasn't yet self-evident.

## Differentiation vs. 2026 Competitors:

Against Sourcegraph: accessible pricing for teams under 50, dependency-specific focus rather than monorepo search. Against Copilot/Cursor: persistent institutional memory, not ephemeral generation — the product remembers what your team learned about a library six months ago. Against GitBook: version-aware, code-line-specific, zero-documentation-effort (AI generates the baseline). The positioning line: *"Copilot writes the code. Omniref explains the dependencies."*
