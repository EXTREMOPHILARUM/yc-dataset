# Quality Checklist

Run through this checklist BEFORE writing any files. If any item fails, fix it first.

---

## Research Report

### Citations & Sources
- [ ] Every factual claim has a superscript citation `<sup><a href="URL">[N]</a></sup>`
- [ ] Minimum 8 unique sources cited
- [ ] All URLs are real and verifiable (not made up)
- [ ] Sources are numbered sequentially by first appearance
- [ ] Primary sources preferred (founder interviews, company blog, SEC filings, patent filings)
- [ ] No "[citation needed]" or placeholder citations

### Content Quality
- [ ] Overview can stand alone — reader understands the company after just this section
- [ ] Founding story includes at least one direct founder quote with attribution
- [ ] Timeline has minimum 8 dated entries with citations
- [ ] "What They Built" describes technical architecture, not marketing pitch
- [ ] Market size numbers have cited sources with dates
- [ ] Business model includes specific pricing or revenue model details
- [ ] Traction section uses hard numbers, not qualitative descriptions
- [ ] Post-mortem identifies structural root cause, not surface-level "ran out of money"
- [ ] Key lessons are company-specific — none could apply to any random startup
- [ ] No adjectives without evidence ("rapidly growing" → grew from X to Y)

### Tone
- [ ] Reads like investigative journalism, not a press release
- [ ] No marketing language ("innovative," "revolutionary," "disruptive," "cutting-edge")
- [ ] Skeptical of founder narratives — verifies claims against evidence
- [ ] When information is unavailable, says so explicitly rather than filling with generalities

---

## Build Plan

### Strategic Coherence
- [ ] Build plan directly addresses the failure mode identified in the report
- [ ] "Why Now" shifts are dated and named (specific technologies, regulations, events)
- [ ] No shift is vaguely "AI is better now" — each names specific tools/changes
- [ ] Competitor analysis names real companies with specific weaknesses
- [ ] The gap between competitors is the exact position the rebuild occupies
- [ ] MVP features counter the original company's structural weaknesses

### Specificity
- [ ] Target customer is specific enough to find on LinkedIn
- [ ] Pricing is in exact dollar amounts (not "competitive pricing")
- [ ] Success metrics have specific thresholds AND rationale for those thresholds
- [ ] Each MVP feature references the specific technology/API that enables it
- [ ] Go-to-market names specific distribution channels, not categories
- [ ] "What we will NOT build" explains strategic reasoning for each exclusion

### Feasibility
- [ ] All named technologies and services actually exist and are available
- [ ] Pricing assumptions are grounded in real comparable products
- [ ] Timeline and milestones are realistic for a small team
- [ ] No feature requires technology that doesn't exist yet

---

## Technical Specs

### Completeness
- [ ] Every MVP feature from the build plan has corresponding: API routes, database tables, and UI pages
- [ ] User flows cover: onboarding, core value loop, and at least one edge case
- [ ] All external services from the tech stack have environment variables listed
- [ ] Getting Started steps use commands matching the chosen tech stack

### Technical Accuracy
- [ ] Database schema is valid SQL that could be pasted into psql
- [ ] API routes use correct HTTP methods (GET for reads, POST for creates, etc.)
- [ ] Project structure matches the chosen framework's conventions
- [ ] Auth strategy matches the product type (B2B → SSO, B2C → OAuth, API → API keys)
- [ ] No deprecated or unmaintained technologies recommended

### Consistency
- [ ] Tech stack choices in section 4 are reflected throughout (database type matches schema syntax, framework matches project structure)
- [ ] API routes match database tables (every core table has CRUD endpoints)
- [ ] Pages match user flows (every flow step has a corresponding page)
- [ ] Environment variables cover every external service in the tech stack

---

## Cross-Document Consistency

- [ ] Company name is spelled identically across all three files
- [ ] Batch code matches `data/index.json`
- [ ] If report says company was a B2B SaaS, build plan and tech specs reflect B2B architecture
- [ ] Competitors named in the report's market position appear in the build plan's competition map (with updated status)
- [ ] The core technical thesis from the report informs the build plan's product direction
- [ ] If the report identifies a specific technical limitation, the tech specs address it
