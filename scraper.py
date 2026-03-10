"""
YC Startup Scraper
==================
Scrapes data from two sources:
1. YC Directory (ycombinator.com/companies) via Algolia API
2. Startups.RIP (dead/acquired YC startups) via web scraping

Outputs JSON files in data/ directory.
"""

import html as html_lib
import httpx
import json
import time
import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin

RAW_DIR = Path("raw")
RAW_DIR.mkdir(exist_ok=True)

# ─── YC Directory (Algolia) ─────────────────────────────────────────────────

ALGOLIA_APP_ID = "45BWZJ1SGC"
ALGOLIA_API_KEY = (
    "NzllNTY5MzJiZGM2OTY2ZTQwMDEzOTNhYWZiZGRjODlhYzVkNjBmOGRjNzJiMWM4ZTU0ZDlhYTZjOTJiMjlhMW"
    "FuYWx5dGljc1RhZ3M9eWNkYyZyZXN0cmljdEluZGljZXM9WUNDb21wYW55X3Byb2R1Y3Rpb24lMkNZQ0NvbXBh"
    "bnlfQnlfTGF1bmNoX0RhdGVfcHJvZHVjdGlvbiZ0YWdGaWx0ZXJzPSU1QiUyMnljZGNfcHVibGljJTIyJTVE"
)
ALGOLIA_INDEX = "YCCompany_production"
ALGOLIA_URL = f"https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/*/queries"


def _get_yc_batches(client, headers):
    """Get all batch names from Algolia facets."""
    payload = {
        "requests": [
            {
                "indexName": ALGOLIA_INDEX,
                "params": "hitsPerPage=0&facets=[\"batch\"]",
            }
        ]
    }
    resp = client.post(ALGOLIA_URL, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()["results"][0]["facets"]["batch"]


def scrape_yc_directory():
    """Scrape all YC companies from Algolia API, paginating by batch."""
    print("=" * 60)
    print("Scraping YC Directory (Algolia API)")
    print("=" * 60)

    client = httpx.Client(timeout=30)
    headers = {
        "x-algolia-application-id": ALGOLIA_APP_ID,
        "x-algolia-api-key": ALGOLIA_API_KEY,
        "Content-Type": "application/json",
    }

    batches = _get_yc_batches(client, headers)
    print(f"  Found {len(batches)} batches, {sum(batches.values())} total companies")

    all_companies = []
    for batch_name, expected_count in sorted(batches.items()):
        payload = {
            "requests": [
                {
                    "indexName": ALGOLIA_INDEX,
                    "params": f'hitsPerPage=1000&facetFilters=[["batch:{batch_name}"]]',
                }
            ]
        }
        resp = client.post(ALGOLIA_URL, headers=headers, json=payload)
        resp.raise_for_status()
        hits = resp.json()["results"][0]["hits"]
        all_companies.extend(hits)
        print(f"  {batch_name}: {len(hits)}/{expected_count} (total: {len(all_companies)})")
        time.sleep(0.2)

    client.close()

    # Save cleaned data — drop only Algolia search decoration
    DROP_KEYS = {"_highlightResult", "tags_highlighted"}
    cleaned = []
    for c in all_companies:
        record = {k: v for k, v in c.items() if k not in DROP_KEYS}
        record["url"] = f"https://www.ycombinator.com/companies/{c.get('slug')}"
        cleaned.append(record)

    out_path = RAW_DIR / "yc_directory.json"
    with open(out_path, "w") as f:
        json.dump(cleaned, f, indent=2)
    print(f"Saved cleaned data to {out_path}")

    return all_companies


def scrape_yc_detail_pages(slugs: list[str] | None = None):
    """Scrape detail pages from ycombinator.com/companies/<slug>.

    Extracts founders, social links, news, launches, and full descriptions
    from the data-page JSON blob embedded in each page.
    """
    print("\n" + "=" * 60)
    print("Scraping YC Detail Pages")
    print("=" * 60)

    # If no slugs provided, load from the directory data
    if slugs is None:
        with open(RAW_DIR / "yc_directory.json") as f:
            companies = json.load(f)
        slugs = [c["slug"] for c in companies if c.get("slug")]

    print(f"  {len(slugs)} companies to scrape")

    # Resume support: skip already-scraped slugs
    out_path = RAW_DIR / "yc_details.json"
    existing = {}
    if out_path.exists():
        with open(out_path) as f:
            existing_list = json.load(f)
        existing = {d["slug"]: d for d in existing_list}
        print(f"  Resuming: {len(existing)} already scraped")

    client = httpx.Client(timeout=30, follow_redirects=True)
    results = list(existing.values())
    scraped_slugs = set(existing.keys())

    for i, slug in enumerate(slugs):
        if slug in scraped_slugs:
            continue

        try:
            url = f"https://www.ycombinator.com/companies/{slug}"
            resp = client.get(url)
            resp.raise_for_status()

            match = re.search(r'data-page="([^"]{500,})"', resp.text)
            if not match:
                results.append({"slug": slug, "error": "no data-page found"})
                continue

            page_data = json.loads(html_lib.unescape(match.group(1)))
            company = page_data.get("props", {}).get("company", {})
            news_items = page_data.get("props", {}).get("newsItems", [])
            launches = page_data.get("props", {}).get("launches", [])

            # Clean founders (remove large avatar URLs to save space)
            founders = []
            for f in company.get("founders", []):
                founders.append({
                    "full_name": f.get("full_name"),
                    "title": f.get("title"),
                    "founder_bio": f.get("founder_bio"),
                    "is_active": f.get("is_active"),
                    "twitter_url": f.get("twitter_url"),
                    "linkedin_url": f.get("linkedin_url"),
                })

            # Clean news items
            news = []
            for n in news_items:
                news.append({
                    "title": n.get("title"),
                    "url": n.get("url"),
                    "date": n.get("date"),
                    "source": n.get("source"),
                })

            partner = company.get("primary_group_partner") or {}

            detail = {
                "slug": slug,
                "name": company.get("name"),
                "batch": company.get("batch"),
                "batch_name": company.get("batch_name"),
                "status": company.get("ycdc_status"),
                "one_liner": company.get("one_liner"),
                "long_description": company.get("long_description"),
                "website": company.get("website"),
                "tags": company.get("tags", []),
                "team_size": company.get("team_size"),
                "year_founded": company.get("year_founded"),
                "location": company.get("location"),
                "city": company.get("city"),
                "country": company.get("country"),
                "twitter_url": company.get("twitter_url"),
                "fb_url": company.get("fb_url"),
                "linkedin_url": company.get("linkedin_url"),
                "github_url": company.get("github_url"),
                "cb_url": company.get("cb_url"),
                "primary_partner": partner.get("full_name"),
                "founders": founders,
                "news": news,
                "launches": launches,
                "app_answers": company.get("app_answers", []),
            }

            results.append(detail)

        except Exception as e:
            results.append({"slug": slug, "error": str(e)})

        if (i + 1) % 50 == 0:
            print(f"  [{i + 1}/{len(slugs)}] scraped {slug}")
            # Checkpoint save
            with open(out_path, "w") as f:
                json.dump(results, f, indent=2, default=str)

        time.sleep(0.3)

    client.close()

    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved {len(results)} company details to {out_path}")

    return results


# ─── Startups.RIP ───────────────────────────────────────────────────────────

STARTUPS_RIP_BASE = "https://startups.rip"


def scrape_startups_rip_listing():
    """Scrape the main listing page to get all company slugs."""
    print("\n" + "=" * 60)
    print("Scraping Startups.RIP - Listing")
    print("=" * 60)

    client = httpx.Client(timeout=30, follow_redirects=True)
    resp = client.get(STARTUPS_RIP_BASE)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    links = soup.select('a[href*="/company/"]')

    companies = []
    seen = set()
    for link in links:
        href = link.get("href", "")
        slug = href.split("/company/")[-1].strip("/")
        if not slug or slug in seen:
            continue
        seen.add(slug)

        text = link.get_text(separator="\n", strip=True)
        companies.append({
            "slug": slug,
            "url": f"{STARTUPS_RIP_BASE}/company/{slug}",
            "card_text": text,
        })

    client.close()
    print(f"  Found {len(companies)} companies in listing")
    return companies


def _decode_rsc_chunks(html: str) -> list[str]:
    """Decode Next.js RSC flight payloads from HTML.

    RSC data is embedded as: self.__next_f.push([1,"<JS-escaped payload>"])
    Since JS string escaping is JSON-compatible, we json.loads the entire
    [1,"..."] array to properly decode all escaping in one shot.
    """
    raw_pushes = re.findall(
        r'self\.__next_f\.push\((\[1,".*?"\])\)', html, re.DOTALL
    )
    decoded = []
    for raw in raw_pushes:
        try:
            arr = json.loads(raw)
            decoded.append(arr[1])
        except (json.JSONDecodeError, IndexError):
            pass
    return decoded


def _extract_company_json(decoded_chunks: list[str]) -> dict | None:
    """Extract initialCompany JSON from decoded RSC chunks."""
    for chunk in decoded_chunks:
        if '"initialCompany":{' not in chunk:
            continue
        idx = chunk.find('"initialCompany":{')
        start = chunk.index("{", idx)
        depth = 0
        i = start
        while i < len(chunk):
            if chunk[i] == "\\" and i + 1 < len(chunk):
                i += 2
                continue
            if chunk[i] == "{":
                depth += 1
            elif chunk[i] == "}":
                depth -= 1
            if depth == 0:
                try:
                    return json.loads(chunk[start:i + 1])
                except json.JSONDecodeError:
                    return None
            i += 1
    return None


def _build_rsc_text_map(decoded_chunks: list[str], company_data: dict | None = None) -> dict[str, str]:
    """Build a map of RSC ref keys to their text content.

    RSC flight format uses T-header chunks like "2a:Td5c," to declare a text
    node with key "2a" and hex-length d5c.  The actual text follows in the
    next chunk.  The very first text chunk (before any T-header) is keyed by
    the first $ref found in the company's report sections.
    """
    text_map = {}
    pending_key = None

    # Determine the overview key from the company data — it's the first $ref
    # in the report sections (varies per request, e.g. $28, $29, $2a)
    overview_key = None
    if company_data:
        for tab in ("report", "buildPlan"):
            sections = company_data.get(tab, {})
            if isinstance(sections, dict):
                sections = sections.get("sections", [])
            for sec in sections:
                ref = sec.get("content", "")
                if isinstance(ref, str) and ref.startswith("$"):
                    overview_key = ref[1:]
                    break
            if overview_key:
                break

    # Find the first T-header index
    first_t_idx = None
    for i, chunk in enumerate(decoded_chunks):
        if re.match(r'^[0-9a-f]+:T[0-9a-f]+,', chunk):
            first_t_idx = i
            break

    # The Overview chunk is the last bare prose chunk before the first T-header.
    if first_t_idx is not None and overview_key is not None:
        for i in range(first_t_idx - 1, -1, -1):
            chunk = decoded_chunks[i]
            if (len(chunk) > 100
                and not re.match(r'^(\d+:|\[|I\[|[0-9a-f]+:)', chunk)
                and "className" not in chunk[:200]
                and "react." not in chunk[:200]):
                text_map[overview_key] = chunk
                break

    # Pass 2: process T-header chunks and their following text
    # When a T-header has inline content, the next bare chunk maps to key+1
    # (the next sequential hex key). When it has no inline content, the next
    # bare chunk maps to the same key.
    for chunk in decoded_chunks:
        m = re.match(r'^([0-9a-f]+):T([0-9a-f]+),(.*)', chunk, re.DOTALL)
        if m:
            key = m.group(1)
            inline_content = m.group(3)
            if inline_content.strip():
                text_map[key] = inline_content
                # Next bare chunk maps to key+1
                next_key = format(int(key, 16) + 1, 'x')
                pending_key = next_key
            else:
                pending_key = key
            continue

        if pending_key is not None:
            text_map[pending_key] = chunk
            pending_key = None
            continue

    return text_map


def _extract_rsc_data(html: str) -> dict:
    """Extract initialCompany JSON and text content from RSC flight payloads."""
    decoded_chunks = _decode_rsc_chunks(html)

    company_data = _extract_company_json(decoded_chunks)
    text_map = _build_rsc_text_map(decoded_chunks, company_data)

    # Also keep the old text_chunks for full_text fallback
    text_chunks = {}

    for unescaped in decoded_chunks:

        # Collect text content from RSC flight data
        # Pattern 1: "key:Thexlen,content" - T-prefixed text nodes
        hex_match = re.match(r'([0-9a-f]+):T([0-9a-f]+),(.*)', unescaped, re.DOTALL)
        if hex_match:
            key = hex_match.group(1)
            content = hex_match.group(3)
            if content.strip():
                text_chunks[key] = content
            continue

        # Pattern 2: Pure prose/markdown chunks (no RSC prefix)
        # These are continuations of T-chunks or standalone text
        stripped = unescaped.strip()
        if len(stripped) > 100:
            # Skip framework/component chunks
            is_framework = bool(re.match(
                r'^(\d+:|\[|{"|\$|I\[|imate|["$]|[a-f0-9]+:\[|\))',
                stripped
            )) or 'className' in stripped[:300] or '"content"' in stripped[:100]
            if not is_framework:
                text_chunks[f'prose_{len(text_chunks)}'] = stripped

    return {
        'company': company_data or {},
        'content_chunks': text_chunks,
        'text_map': text_map,
    }


def _resolve_section_content(sections, text_map):
    """Resolve $XX references in report sections to actual text content."""
    resolved = []
    for section in sections:
        heading = section.get("heading", "")
        content_ref = section.get("content", "")
        content_text = ""

        if isinstance(content_ref, str) and content_ref.startswith("$"):
            ref_key = content_ref[1:]  # $29 -> "29", $2a -> "2a"
            content_text = text_map.get(ref_key, "")
        elif isinstance(content_ref, str) and len(content_ref) > 50:
            # Some sections have inline content instead of a ref
            content_text = content_ref

        resolved.append({"heading": heading, "content": content_text})
    return resolved


def scrape_startups_rip_detail(slug: str, client: httpx.Client) -> dict:
    """Scrape a single company detail page from startups.rip."""
    url = f"{STARTUPS_RIP_BASE}/company/{slug}"
    resp = client.get(url)
    resp.raise_for_status()

    rsc = _extract_rsc_data(resp.text)
    company = rsc['company']
    content_chunks = rsc['content_chunks']
    text_map = rsc['text_map']

    # Extract structured sections for each tab
    report_raw = company.get("report", {})
    build_plan_raw = company.get("buildPlan", {})
    specs_preview_val = company.get("specsPreview", {})
    specs_preview_raw = specs_preview_val if isinstance(specs_preview_val, dict) else {}
    specs_toc_raw = company.get("specsToc", [])

    report_sections = _resolve_section_content(
        report_raw.get("sections", []), text_map
    )
    build_plan_sections = _resolve_section_content(
        build_plan_raw.get("sections", []), text_map
    )
    specs_preview_sections = _resolve_section_content(
        specs_preview_raw.get("sections", []), text_map
    )

    # Extract founders
    founders_raw = company.get("founders", [])
    founders = []
    for f in founders_raw:
        founders.append({
            "name": f.get("name", ""),
            "title": f.get("title", ""),
            "linkedin": f.get("linkedin", ""),
            "twitter": f.get("twitter", ""),
            "avatar_url": f.get("avatarUrl", ""),
        })

    # Combine all text content into full_text as fallback
    full_text = "\n\n".join(content_chunks.values())

    data = {
        "slug": slug,
        "url": url,
        "name": company.get("name", ""),
        "batch": company.get("batch", ""),
        "status": company.get("status", ""),
        "one_liner": company.get("oneLiner", ""),
        "description": company.get("description", ""),
        "category": company.get("category", ""),
        "categories": company.get("categories", []),
        "website": company.get("website", ""),
        "yc_url": company.get("ycUrl", ""),
        "team_size": company.get("teamSize"),
        "founded_year": company.get("foundedYear"),
        "logo_url": company.get("logoUrl", ""),
        "analysis_status": company.get("analysisStatus", ""),
        "specs_unlocked": company.get("specsUnlocked", False),
        "citation_labels": company.get("citation_labels", []),
        "founders": founders,
        "report": {
            "title": report_raw.get("title", ""),
            "word_count": report_raw.get("metadata", {}).get("word_count"),
            "sections": report_sections,
        },
        "build_plan": {
            "title": build_plan_raw.get("title", ""),
            "word_count": build_plan_raw.get("metadata", {}).get("word_count"),
            "sections": build_plan_sections,
        },
        "specs_preview": {
            "title": specs_preview_raw.get("title", ""),
            "sections": specs_preview_sections,
        },
        "specs_toc": specs_toc_raw,
        "full_text": full_text,
    }

    return data


def scrape_startups_rip():
    """Scrape all companies from startups.rip including detail pages."""
    listing = scrape_startups_rip_listing()

    print(f"\nScraping {len(listing)} detail pages...")
    client = httpx.Client(timeout=30, follow_redirects=True)

    all_details = []
    for i, company in enumerate(listing):
        slug = company["slug"]
        try:
            detail = scrape_startups_rip_detail(slug, client)
            detail["card_text"] = company["card_text"]
            all_details.append(detail)
            if (i + 1) % 20 == 0:
                print(f"  [{i + 1}/{len(listing)}] scraped {slug}")
        except Exception as e:
            print(f"  ERROR scraping {slug}: {e}")
            all_details.append({"slug": slug, "error": str(e)})
        time.sleep(0.5)  # Be polite

    client.close()

    out_path = RAW_DIR / "startups_rip.json"
    with open(out_path, "w") as f:
        json.dump(all_details, f, indent=2, default=str)
    print(f"\nSaved {len(all_details)} companies to {out_path}")

    return all_details


# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="YC Startup Scraper")
    parser.add_argument("--source", choices=["yc", "yc-details", "rip", "all"], default="all",
                        help="Which source to scrape")
    args = parser.parse_args()

    if args.source in ("yc", "all"):
        scrape_yc_directory()

    if args.source in ("yc-details", "all"):
        scrape_yc_detail_pages()

    if args.source in ("rip", "all"):
        scrape_startups_rip()

    print("\nDone!")
