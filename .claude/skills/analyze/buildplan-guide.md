# Build Plan Guide

Write as `# Build Plan: <Company Name> <Current Year>`. This is a plan to rebuild the company TODAY with current technology and market conditions. It should read like a technical co-founder's internal strategy doc — opinionated, specific, and actionable. Not a business school case study. Not a generic lean canvas.

The build plan must directly address the failure mode or core challenge identified in the research report. If the original company died because of long sales cycles, the build plan must explain how THIS version shortens them. If it died because of high CAC, this plan must show a lower-cost acquisition channel.

---

## Section 1: Overview (## Overview)

**Length:** 3 paragraphs, no sub-headers

**Paragraph 1 — The pitch:**
- First sentence: what this rebuild is, in one line (e.g., "By 2026, 20n is a cloud-native AI platform that turns target molecules into validated biosynthetic pathways in weeks, not years.")
- Then: what it specifically does, who it's for (specific customer profile, not "businesses"), and approximate price point
- End with the key differentiator in one clause

**Paragraph 2 — What changed:**
- The single most important technology, market, or regulatory shift that makes this viable now
- Be specific: name the technology, date the change, explain the mechanism
- BAD: "AI has improved significantly since 2015"
- GOOD: "AlphaFold2 (July 2021) solved protein structure prediction, making enzymatic pathway design computationally tractable at near-zero marginal cost"
- Connect the shift directly to the original company's failure mode

**Paragraph 3 — GTM in 3 sentences:**
- How you land the first customer
- How you prove the product works
- How you expand from there

**Checklist:**
- [ ] A reader can pitch this company after reading just this section
- [ ] The "what changed" is dated and specific
- [ ] Price point is mentioned (exact or range)
- [ ] Target customer is specific enough to find on LinkedIn

---

## Section 2: Why Now? (## Why Now?)

**Length:** 2-4 paragraphs

**Structure:**
1. **Opening paragraph:** The SINGLE most important change since the original company existed. Not a list of changes — the one that matters most. Name it, date it, explain the mechanical impact on the business (not just "this is better now" but HOW it changes the economics, speed, or feasibility).

2. **Additional shifts (3-4), each as a bold sub-heading:**

```
**Shift name in bold.** 2-3 sentences explaining what changed, when, and why it matters for THIS specific product. Include dates and names.
```

**Required shift categories (at least one from each):**
- **Technology shift:** New tools, platforms, APIs, open-source projects that didn't exist before. Name them: "Emerald Cloud Lab launched in 2020, providing programmatic API access to robotic wet labs."
- **Market shift:** Regulatory changes, buyer behavior shifts, market size growth, new procurement mandates. Cite the regulation or trend.
- **Infrastructure shift:** Cost reductions (10x drops in compute, storage, synthesis, etc.), new distribution channels, ecosystem maturation. Use specific numbers.

**Optional but valuable:**
- Distribution channel that now exists (app stores, marketplaces, API ecosystems)
- Talent availability (skills that were rare are now common)
- Social/cultural shift (acceptance of a behavior, regulatory normalization)

**Checklist:**
- [ ] Every shift has a date
- [ ] Every shift has a specific name (technology, regulation, company)
- [ ] At least one shift directly addresses why the original company failed
- [ ] No shift is "AI is better now" without specifics

---

## Section 3: Current Market Analysis (## Current Market Analysis)

**Length:** 1-2 paragraphs

**Structure:**

**Market size:** TAM with source, date, and growth rate. If using market research firms (Grand View Research, Mordor Intelligence, etc.), add: "(exact figures should be independently verified before use in investor materials)." Include both the broad market and the addressable sub-segment.

**Market validation:** Name 1-3 real companies that have raised significant funding or achieved scale in adjacent/overlapping space. This proves the market exists and investors are interested. Include: company name, what they do, funding/valuation, and what they DON'T do that creates the gap.

**Checklist:**
- [ ] Market size has a source and date
- [ ] At least one comparable company named with funding data
- [ ] The gap between comparable companies and this rebuild is explicit

---

## Section 4: Competition Map (## Competition map and gaps:)

**Length:** Bullet list + 2 paragraphs

**Competitor bullets (4-6 real companies):**
```
- **Company Name (context/year):** What they do, their model, and their weakness. 2-3 sentences. The weakness should be specific — not "they're too expensive" but "their Foundry model requires minimum $2M engagements, pricing out companies under $500M revenue."
```

**After bullets — "The gap:" paragraph:**
- Identify the specific market position that no current competitor occupies
- Frame it in terms of the customer: "No current competitor offers [specific capability] at [price point] for [customer segment]"
- This gap must be the exact position the rebuild occupies

**After gap — "Demand signals:" paragraph:**
- Evidence that buyers want this. Not that the market exists, but that specific buyers are actively looking for this solution.
- Examples: comparable product adoption in adjacent markets, RFPs, industry surveys, community discussions, job postings signaling unmet needs

**Checklist:**
- [ ] All competitors are real companies that exist today
- [ ] Each competitor has a named weakness, not just a description
- [ ] The gap is specific enough to be falsifiable
- [ ] Demand signals are evidence-based, not assumed

---

## Section 5: Recommended MVP (## Recommended MVP)

**Core features (3-4), each as:**
```
### Core Feature N: <Descriptive Name>
```

**Each feature paragraph (4-8 sentences) must cover:**
1. What it does — specific user-facing functionality
2. How it differs from the original company's approach — what's new or different
3. Why it's technically feasible now — what technology/infrastructure enables it
4. What it builds on — name existing tools, APIs, open-source projects, services

**After features:**

```
## What we will NOT build:
```
- 3-4 bullet points of deliberate scope exclusions
- Each with a 1-sentence rationale explaining WHY not (not just "out of scope" but the strategic reason)
- These should be things people would naturally ask about — preempt the question

```
## Success metrics with concrete thresholds:
```
- 4-5 metrics with specific numbers and timeframes
- Format: "Metric: ≥X within Y months of launch (baseline: Z, rationale for threshold: ...)"
- Include at least: one product metric, one revenue metric, one retention metric
- Thresholds should be justified — not arbitrary round numbers

**Checklist:**
- [ ] Each feature references specific technology that enables it
- [ ] Features directly counter the original company's failure points
- [ ] Exclusions explain strategic reasoning, not just scope limits
- [ ] Success metrics have baselines and rationale for thresholds
- [ ] A developer could start building from these feature descriptions

---

## Section 6: Go-to-Market Strategy (## Go-to-Market Strategy)

**Length:** 3-4 paragraphs, each with a bold label

**Paragraph 1 — "Target customer segment:"**
- Specific company profile: industry, revenue range, headcount range, geography
- Specific buyer: job title of the person who signs the check
- Specific trigger: what event or pain point causes them to start looking for a solution
- NOT: "SMBs" or "enterprise companies" — describe them precisely enough to build a prospect list

**Paragraph 2 — "Primary distribution channel:"**
- How you reach the target buyer. Name specific platforms, events, communities, partnerships, marketplaces.
- Secondary channel as well.
- For each channel: why it works for THIS customer segment (not generically "content marketing works")

**Paragraph 3 — "Pricing strategy:"**
- Specific prices, not ranges. $X/month, $Y/project, $Z/seat.
- Justify against: competitor pricing (from section 4), unit economics, and customer willingness to pay
- Describe the pricing model structure: free tier? Usage-based? Seat-based? Hybrid?
- If it departs from the original company's pricing, explain why

**Paragraph 4 — "Differentiation vs. <year> competitors:"**
- 2-3 sentences for each competitor named in section 4
- Format: "Against [Competitor], the rebuild wins on [dimension] — [specific reason]."
- Dimensions: price, speed, accessibility, depth, integration, simplicity

**Checklist:**
- [ ] Target customer is specific enough to search for on LinkedIn
- [ ] Pricing is exact dollar amounts with justification
- [ ] Each competitor from section 4 has a differentiation statement
- [ ] Distribution channels are specific to the customer segment
