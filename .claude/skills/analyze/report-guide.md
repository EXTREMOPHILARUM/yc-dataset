# Research Report Guide

Write as `# Research Report: <Company Name>`. The tone is analytical, specific, and citation-heavy — like a long-form investigative piece by a journalist who has done extensive primary research. NOT a marketing summary, NOT a Wikipedia article.

## Citation Format

Every factual claim must have a superscript citation:
```
This is a fact.<sup><a href="https://example.com">[1]</a></sup>
```

Sources are numbered sequentially and listed in full at the end.

---

## Section 1: Overview (## Overview)

**Length:** 3-4 paragraphs minimum

**Paragraph structure:**
1. **Identity sentence:** One sentence: what the company was/is, who founded it, when, and the core technical thesis. Keep it tight — this is the lead.
2. **Product specifics:** What they built in concrete terms. Name the technology, the technical approach, the key differentiator. Avoid abstractions like "innovative platform" — say what it actually does.
3. **Traction:** Revenue, users, funding, partnerships, contracts. Specific numbers with citations. If numbers aren't public, say so: "Revenue figures were not publicly disclosed, but the company reported [X customers/contracts]."
4. **Outcome:** What happened. For dead companies: when, how, and why (one sentence preview — the full analysis comes later). For active: current trajectory and position.

**Checklist:**
- [ ] Every paragraph has at least one citation
- [ ] No adjectives without evidence ("rapidly growing" → "grew from X to Y in Z months")
- [ ] Company's actual product is described, not its marketing pitch
- [ ] Reader can understand what the company does after reading just this section

---

## Section 2: Founding Story (## Founding Story)

**Length:** 3-5 paragraphs

**What to cover:**
- **Founders' backgrounds:** What were they doing before? Be specific — institution, role, years. Not "experienced engineer" but "spent 4 years at Google working on TensorFlow's distributed training infrastructure."
- **How they met:** The actual story, not "they shared a vision." Conference? Same lab? Previous company? College roommates?
- **The insight:** What specific experience, frustration, or observation led to the company? The best founding stories trace back to a concrete moment.
- **Initial thesis vs. reality:** What did they originally plan to build, and how did it differ from what they shipped?
- **Team dynamic:** Who was technical, who was business? Both technical? What was the working relationship? Were they full-time from day one or moonlighting?
- **Founder quotes:** Pull directly from interviews, podcasts, blog posts, HN comments. Attribute with source.

**Checklist:**
- [ ] At least one direct founder quote with source
- [ ] Specific pre-founding credentials (institutions, companies, roles)
- [ ] The "why this, why now, why us" is answered through narrative, not stated explicitly
- [ ] Reader understands why these specific people were suited to build this

---

## Section 3: Timeline (## Timeline)

**Format:** Chronological bullet list
```
- **Month Year** — Event description with specifics.<sup><a href="URL">[N]</a></sup>
```

**Required entries (include all that apply):**
- Founding date and circumstances
- YC batch entry
- Each funding round (amount, lead investor, valuation if known)
- Major product launches or pivots
- Key hires (CTO, first sales hire, etc.)
- Notable press coverage or HN frontpage moments
- Partnerships or major customer wins
- Signs of trouble (layoffs, pivots, co-founder departures)
- Shutdown, acquisition, or current milestone

**For HN discussions, embed:**
```
<media-hn url="https://news.ycombinator.com/item?id=XXXXX" title="Title" points="" comments=""></media-hn>
```

**Checklist:**
- [ ] Minimum 8 entries
- [ ] Every entry has a date (at least year, prefer month+year)
- [ ] Every entry has a citation
- [ ] Entries are substantive sentences, not vague milestones ("Launched v2" → "Launched v2 with real-time collaboration, replacing the batch-upload workflow that had caused 40% user churn")
- [ ] Timeline tells a coherent story when read sequentially

---

## Section 4: What They Built (## What They Built)

**Length:** 4-6 paragraphs

**What to cover:**
1. **System architecture:** What was the technical system? Not "an AI platform" but "a pipeline that ingested X, processed it through Y, and output Z." Name specific technologies, algorithms, data sources.
2. **User workflow:** Walk through what a customer/user actually experienced. Step 1, step 2, step 3. What did the UI look like? What was the input and output?
3. **Key technical decisions:** What architectural choices defined the product? What were the trade-offs? (e.g., "chose to build on Ethereum rather than a private chain, which provided decentralization but limited throughput to 15 TPS")
4. **Flagship achievement:** The single most impressive demo, metric, or proof point. The thing they showed investors or customers to prove it worked.
5. **Novelty assessment:** What was genuinely new vs. incremental improvement? Be honest. Most startups combine existing ideas in a new way rather than inventing from scratch — that's fine, but name it.
6. **Scale and performance:** Any known metrics about the system's scale — data volume, user count, throughput, accuracy rates.

**Checklist:**
- [ ] A technical reader could roughly reconstruct the system from this description
- [ ] Trade-offs are named, not just the benefits
- [ ] At least one specific technical metric (accuracy, throughput, dataset size, etc.)
- [ ] The difference between this and existing solutions is concrete

---

## Section 5: Market Position (## Market Position)

**Length:** 2-3 paragraphs

**What to cover:**
- **Market size:** TAM/SAM/SOM with cited sources and dates. If using market research firm numbers, note "(exact figures should be independently verified)."
- **Competitors at the time:** Name 3-5 direct competitors that existed when the company was active. Describe each in one sentence: what they did and how they differed.
- **Positioning:** How did the company differentiate? Price, technology, distribution, niche?
- **Market dynamics:** What macro forces helped or hurt? (Regulatory changes, platform shifts, funding environment, buyer behavior changes)

**Checklist:**
- [ ] Market size has a cited source with a date
- [ ] Competitors are real companies, not hypothetical categories
- [ ] Positioning is described in terms of trade-offs, not just advantages

---

## Section 6: Business Model (## Business Model)

**Length:** 2-3 paragraphs

**What to cover:**
- **Revenue model:** Be specific. Not "SaaS" but "$X/month per seat with a free tier up to Y users." If pricing isn't public, describe the model structure.
- **Unit economics:** CAC, LTV, gross margins, payback period — whatever is publicly available or can be reasonably estimated. If nothing is public, say so.
- **Evolution:** How did the business model change? Most startups pivot pricing or model at least once. Document the before and after.
- **Fundamental challenge:** What was the core economic tension? (e.g., "marketplace chicken-and-egg problem," "long sales cycles vs. startup runway," "high CAC in a low-LTV market")

**Checklist:**
- [ ] Specific pricing or revenue model described
- [ ] At least one economic tension or challenge identified
- [ ] Evolution of the model documented if applicable

---

## Section 7: Traction (## Traction)

**Length:** 2-3 paragraphs

**What to cover:**
- **Hard metrics:** Revenue, ARR, MRR, GMV, MAU, DAU, growth rate, number of customers. Cite every number.
- **Funding:** Every round: date, amount, type (seed/A/B), lead investor, other notable investors, valuation if known. Format: "Raised a $X Series A led by [Investor] at a $Y valuation in [Month Year]."
- **Key wins:** Notable customers, partnerships, contracts, awards, press mentions that signal traction.
- **Trajectory:** Was growth accelerating, linear, decelerating, or plateaued? What was the trend in the last known period?

**Checklist:**
- [ ] Every number has a citation
- [ ] Funding history is complete (all known rounds)
- [ ] Growth trajectory is characterized (not just a snapshot)

---

## Section 8: Post-Mortem / Current Status

**Use `## Post-Mortem` for dead/acquired companies. Use `## Current Status` for active ones.**

### For dead companies (3-4 paragraphs):
1. **Root cause:** The PRIMARY reason for failure. Be specific and structural — not "ran out of money" but the underlying cause. Was it market timing? Product-market fit? Unit economics? Team dynamics? Competition?
2. **Contributing factors:** 2-3 secondary issues that compounded the primary cause. These are the things that might have been survivable alone but were fatal in combination.
3. **Counterfactual:** What could realistically have been done differently? Not "they should have been smarter" but specific, actionable alternatives: "Targeting enterprise customers instead of SMBs would have provided the contract sizes needed to sustain the 18-month sales cycle."
4. **Founders afterward:** Where did they go? What are they doing now? This often reveals lessons they learned. Check LinkedIn, subsequent YC batches, Crunchbase.

### For active companies (2-3 paragraphs):
1. **Current trajectory:** Latest revenue/growth numbers, recent funding, team size.
2. **Strategic moves:** Recent product launches, market expansions, partnerships, pivots.
3. **Outlook:** Key risks and opportunities. Be specific — name the risk, name the opportunity.

**Checklist:**
- [ ] Root cause is structural, not surface-level
- [ ] Counterfactual is specific and actionable
- [ ] Founder trajectories are documented with sources

---

## Section 9: Key Lessons (## Key Lessons)

**Length:** 5-8 bullet points

**Format:**
```
- **Lesson title in bold.** 2-3 sentence explanation with specific references to this company's story. Not generic advice.
```

**Required lesson categories (at least one from each):**
- Market timing or market dynamics
- Team composition or execution
- Business model or unit economics
- Product or technology decisions
- Fundraising or capital strategy

**Anti-patterns (do NOT write these):**
- "Product-market fit is important" — too generic
- "They should have listened to customers" — too vague
- "Timing is everything" — too cliché

**Good examples:**
- "**Software-speed teams need software-speed validation cycles.** 20n's pure-software team could iterate on pathway predictions in hours, but proving them required weeks of CRO wet lab work. The feedback loop mismatch meant they burned runway waiting for external validation that they couldn't control or accelerate."

**Checklist:**
- [ ] Every lesson references a specific fact from this company's story
- [ ] No lesson could apply equally to any random startup
- [ ] At least 5 lessons covering different categories

---

## Section 10: Sources (## Sources)

**Format:**
```
1. [Article Title](URL) — Publication/Author, Date
2. [Article Title](URL) — Publication/Author, Date
```

**Requirements:**
- Minimum 8 sources
- Prefer primary sources: company blog posts, founder interviews/podcasts, SEC filings, patent filings, direct HN comments by founders
- Secondary sources: TechCrunch, press coverage, Crunchbase, PitchBook
- Tertiary (use sparingly): Wikipedia, generic industry reports
- Every source must have a working URL
- Sources should be ordered by first citation appearance in the text
