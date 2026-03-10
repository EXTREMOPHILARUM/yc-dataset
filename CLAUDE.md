# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

YC startup dataset: scrapes company data from two sources, merges into agent-friendly markdown files organized by batch.

- **YC Directory** (ycombinator.com/companies) — ~5,758 companies via Algolia Search API
- **Startups.RIP** — 173 curated dead/acquired YC startup post-mortems via Next.js RSC scraping

## Commands

```bash
# Scrape to raw/
uv run python3 scraper.py --source yc          # YC directory (Algolia)
uv run python3 scraper.py --source yc-details   # YC detail pages (slow, ~5k pages, has resume support)
uv run python3 scraper.py --source rip           # startups.rip listing + detail pages
uv run python3 scraper.py --source all           # All of the above

# Transform raw/ → data/
uv run python3 transform.py                      # Merge + convert to markdown
```

## Pipeline: Scrape → Transform → Commit

1. **Scrapers** (`scraper.py`) output raw JSON to `raw/` (git-ignored)
2. **Transformer** (`transform.py`) merges all sources by slug and writes markdown to `data/`
3. Data is committed to git as individual markdown files (meaningful diffs, agent-readable)

## Data Structure

```
raw/                          # .gitignored staging area
  yc_directory.json
  yc_details.json
  startups_rip.json

data/
  index.json                  # Lightweight lookup: {slug, name, batch, status, has_postmortem}
  S05/
    reddit/
      company.md              # YAML frontmatter + description
      founders.md             # Founder profiles with links
      news.md                 # News articles (if any)
      launches.md             # YC launches (if any)
      postmortem.md           # Post-mortem report (startups.rip only)
      buildplan.md            # Build plan (startups.rip only)
      techspecs.md            # Specs preview + TOC (startups.rip only)
```

Batch codes: S05 = Summer 2005, W07 = Winter 2007, F24 = Fall 2024, Sp25 = Spring 2025.

## Scraping Techniques

**YC Directory**: Algolia API (app ID `45BWZJ1SGC`). Paginates by batch facet filter to bypass 1000-hit limit.

**YC Detail Pages**: JSON blob in `data-page` HTML attribute. Decoded via `html.unescape` + `json.loads`. Checkpoints every 50 companies.

**Startups.RIP**: Next.js RSC site. Content is in `self.__next_f.push([1,"..."])` flight payloads, not the DOM. `json.loads` on the raw array decodes JS string escaping generically. RSC pipeline: `_decode_rsc_chunks` → `_extract_company_json` → `_build_rsc_text_map` → `_resolve_section_content`.

## Custom Skills

### `/analyze <company> [sections]`

Generates research report, build plan, and technical specs for any company in the dataset. Structured as a skill directory at `.claude/skills/analyze/`:

- `SKILL.md` — Main command with frontmatter (`allowed-tools`, `argument-hint`), auto-loaded index search via `!`backtick`` injection, phased execution plan
- `report-guide.md` — Section-by-section requirements for the 10-section research report (citations, tone, checklists)
- `buildplan-guide.md` — Section-by-section requirements for the 6-section build plan
- `techspecs-guide.md` — Section-by-section requirements for the 12-section technical spec
- `quality-checklist.md` — Cross-document validation checklist
- `examples/` — Real 20n analysis files from startups.rip as gold-standard examples

Results are saved to the company's data directory and tracked in `raw/analyses.json`.
