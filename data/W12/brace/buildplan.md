# Build Plan: Brace 2026

## Overview

Brace 2026 is a deployment platform for AI-generated websites. You paste HTML/CSS/JS output from Claude or Cursor, hit deploy, and get a live URL in under 60 seconds—no Git, no CLI, no infrastructure knowledge required. It's built for the 2M+ developers and designers now using AI to prototype and ship, but stuck in a gap between generation and production.

The market shift is real: AI coding tools have made static site generation frictionless, but deployment hasn't caught up. Vercel and Netlify assume Git fluency and React expertise. Brace assumes nothing except "I have working code and need it live." The insight is that AI-native workflows don't fit Git-first platforms—they need Git-optional platforms.

Go-to-market is direct: target Cursor and Claude communities, position as "the deploy button AI forgot," and win through speed and simplicity. Free tier gets you to 500 deployed sites in 60 days. Paid tier ($20/mo) unlocks custom domains, form handling, and analytics. The unit economics work because infrastructure costs are now negligible and the TAM is massive.33:T79f,

## Why Now?

## Current Market Analysis

**Market Size:** The research report cites the Jamstack market at $2B+, validated by Netlify's $105M raise and Vercel's $2.5B valuation. Webflow, the closest analog to Brace's designer-targeting pivot, has reached $100M+ ARR at $23–$212/month pricing. Precise 2026 market size figures beyond these benchmarks are not available in the research report.

## Competitive Map:

- **Vercel** dominates Git-native deployment for React/Next.js developers. Its weakness is complexity: onboarding requires Git familiarity, CLI comfort, and framework-specific configuration. It is explicitly not designed for AI-generated or designer-produced static output.
- **Netlify** targets professional development teams with CI/CD pipelines and enterprise features. Its weakness is the same: the product assumes Git-literate users. Netlify's pricing starts at $19/month for teams, pricing out casual or early-stage users.
- **Cloudflare Pages** offers free-tier static hosting with strong performance. Its weakness is a developer-first interface with no workflow tooling for non-technical users.
- **Webflow** targets designers who want visual editing, not code-first workflows. Its weakness is that it locks users into a proprietary CMS and doesn't serve users who already have HTML/CSS output from AI tools or design software.
- **GitHub Pages** remains free but requires Git knowledge — the same barrier Brace identified in 2013, still unresolved for the vibe-coder segment.

**The Gap:** No current competitor serves the AI-assisted developer who has a working static site or SPA but no deployment infrastructure knowledge. This is Brace's original thesis, now with a dramatically larger addressable population.

**Demand Signals:** Formspree — built directly from Brace's forms.brace.io tool — is a viable independent business, confirming that the "free utility as paid hosting funnel" model works at market maturity.

---

## Recommended MVP

## Core Features:

## Drag-and-Drop or Folder-Upload Deployment

Accept a ZIP file, folder upload, or direct paste of AI-generated HTML/CSS/JS output and deploy it to a live URL in under 60 seconds. This replicates Brace's "Ship It" interaction without any Dropbox dependency, using Cloudflare Pages or Vercel's deployment API as the underlying layer. Unlike the original Brace, the deployment target is infrastructure the founder controls — no third-party deprecation risk.

## Instant Preview + One-Click Promotion

Every upload generates a private Draft URL for review and sharing, with a single button to promote to a Production URL with a custom domain. This preserves Brace's signature Draft/Production workflow — its most praised UX feature per Gizmodo's 2013 coverage — while adding shareable preview links for client collaboration, a workflow gap none of the current Git-native competitors address for non-technical users.

## AI-Output Compatibility Layer

Detect and auto-fix common issues in AI-generated HTML output: broken relative paths, missing meta tags, inline script conflicts, and missing viewport declarations. Claude (March 2023) and GPT-4 (March 2023) produce deployable but often imperfect static output. This feature turns a frustrating debugging step into a zero-effort deployment, differentiating from Vercel and Netlify which surface raw errors with no remediation guidance.

## Integrated Form Handling

Include a Formspree-compatible form endpoint automatically on every deployed site, activated by adding a single `action` attribute. This replicates forms.brace.io — the tool that outlasted Brace itself and became Formspree — as a built-in feature rather than a free companion product, creating immediate utility and a natural upsell path.

**What We Will NOT Build:** Custom CMS, visual site editor, database hosting, serverless functions, Git integration, or CLI tooling. These are Vercel and Netlify's territory. The MVP serves users who have output, not users who need a development environment.

## Success Metrics:

- 500 sites deployed within 60 days of launch (Brace hit 2,000 in beta; this is a conservative floor)
- 10% free-to-paid conversion within 90 days
- $5,000 MRR within 6 months
- Average time-to-live-URL under 90 seconds

---

## Go-to-Market Strategy

**Target Customer:** AI-assisted developers and designers who use Claude, Cursor, or ChatGPT to generate static sites and SPAs but have no DevOps background. Specifically: freelance designers charging $500–$5,000 per client site, indie hackers building landing pages for side projects, and non-technical founders who can now produce working HTML with AI assistance but cannot configure Vercel. This is narrower than Brace's 2013 designer-and-agency target and more precisely matched to the 2026 distribution environment.

**Primary Distribution Channel:** GitHub Marketplace and Cursor's extension ecosystem, where the target customer already lives. Tactics: (1) a one-click "Deploy to Brace" button embeddable in AI chat outputs and GitHub READMEs, modeled on Netlify's "Deploy to Netlify" button; (2) direct outreach to Cursor power-user communities on X and Discord, where vibe-coding workflows are actively discussed; (3) a free tier that deploys unlimited sites with Brace-branded subdomains, using the free tool as the acquisition funnel Brace never fully executed.

**Pricing:** Free tier (Brace subdomain, 3 sites, form handling included) to replicate the organic growth Brace achieved in beta. Paid tiers at $9/month (custom domain, 10 sites) and $29/month (unlimited sites, client collaboration links, priority support). This is calibrated against Webflow's $23 entry point and Netlify's $19 team tier, with a lower floor to capture the freelancer and indie hacker segment. Pricing is introduced at launch — not deferred 20 months as Backlift did.

**Differentiation:** Every current competitor assumes Git literacy. Brace 2026 assumes none. The positioning is explicit: "Deploy what your AI built." This is a message no Vercel, Netlify, or Cloudflare Pages campaign is running, and it maps directly to the gap the research report identifies as Brace's original unmet thesis — now finally matched to a market large enough to sustain it.
