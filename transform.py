"""
Transform raw JSON scraper output into a directory-based markdown structure.

Usage:
    uv run python3 transform.py
    uv run python3 transform.py --raw-dir raw --out-dir data
"""

import json
import re
import shutil
from pathlib import Path

RAW_DIR = Path("raw")
OUT_DIR = Path("data")

YC_BASE = "https://www.ycombinator.com"

# Map full batch names (from Algolia) to short codes (from detail pages)
SEASON_MAP = {"Summer": "S", "Winter": "W", "Fall": "F", "Spring": "Sp"}


def _batch_to_short(batch_name: str) -> str:
    """Convert 'Summer 2005' → 'S05', 'Fall 2024' → 'F24', etc."""
    if not batch_name:
        return ""
    m = re.match(r"(Summer|Winter|Fall|Spring)\s+(\d{4})", batch_name)
    if not m:
        return batch_name  # Already short or unknown format
    season, year = m.group(1), m.group(2)
    return f"{SEASON_MAP[season]}{year[2:]}"


def _yaml_scalar(value) -> str:
    """Format a value for YAML frontmatter."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    s = str(value)
    if any(c in s for c in ":#{}[]|>&*!?,\n\"'") or s.startswith(("-", " ")):
        return json.dumps(s)
    return s


def _yaml_list(items: list) -> str:
    """Format a list for YAML frontmatter."""
    if not items:
        return "[]"
    lines = []
    for item in items:
        lines.append(f"  - {_yaml_scalar(item)}")
    return "\n" + "\n".join(lines)


def load_raw_data() -> dict[str, dict]:
    """Load all raw JSONs and merge by slug into a unified dict."""
    companies: dict[str, dict] = {}

    # YC Directory (Algolia)
    dir_path = RAW_DIR / "yc_directory.json"
    if dir_path.exists():
        for entry in json.load(open(dir_path)):
            slug = entry.get("slug", "")
            if not slug:
                continue
            companies.setdefault(slug, {})
            companies[slug]["directory"] = entry

    # YC Detail Pages
    det_path = RAW_DIR / "yc_details.json"
    if det_path.exists():
        for entry in json.load(open(det_path)):
            slug = entry.get("slug", "")
            if not slug:
                continue
            companies.setdefault(slug, {})
            companies[slug]["details"] = entry

    # Startups.RIP
    rip_path = RAW_DIR / "startups_rip.json"
    if rip_path.exists():
        for entry in json.load(open(rip_path)):
            slug = entry.get("slug", "")
            if not slug or "error" in entry:
                continue
            companies.setdefault(slug, {})
            companies[slug]["rip"] = entry

    return companies


def _resolve_batch(sources: dict) -> str:
    """Get short batch code from available sources."""
    # Prefer detail page (already short code)
    det = sources.get("details", {})
    if det.get("batch"):
        return det["batch"]
    # Fall back to directory (full name → convert)
    dir_entry = sources.get("directory", {})
    if dir_entry.get("batch"):
        return _batch_to_short(dir_entry["batch"])
    # Fall back to rip
    rip = sources.get("rip", {})
    if rip.get("batch"):
        return _batch_to_short(rip["batch"])
    return ""


def write_company_md(slug: str, sources: dict, company_dir: Path):
    """Write company.md with merged core info."""
    d = sources.get("directory", {})
    det = sources.get("details", {})
    rip = sources.get("rip", {})

    batch = _resolve_batch(sources)
    name = det.get("name") or d.get("name") or rip.get("name") or slug
    status = det.get("status") or d.get("status") or rip.get("status") or ""
    one_liner = det.get("one_liner") or d.get("one_liner") or rip.get("one_liner") or ""
    website = det.get("website") or d.get("website") or rip.get("website") or ""
    description = det.get("long_description") or d.get("long_description") or rip.get("description") or ""

    lines = ["---"]
    lines.append(f"name: {_yaml_scalar(name)}")
    lines.append(f"slug: {_yaml_scalar(slug)}")
    lines.append(f"batch: {_yaml_scalar(batch)}")
    lines.append(f"status: {_yaml_scalar(status)}")
    if one_liner:
        lines.append(f"one_liner: {_yaml_scalar(one_liner)}")
    if website:
        lines.append(f"website: {_yaml_scalar(website)}")

    # Numeric fields
    team_size = det.get("team_size") or d.get("team_size") or rip.get("team_size")
    if team_size is not None:
        lines.append(f"team_size: {team_size}")
    year_founded = det.get("year_founded") or d.get("year_founded") or rip.get("founded_year")
    if year_founded is not None:
        lines.append(f"year_founded: {year_founded}")

    # Location
    location = det.get("location") or d.get("all_locations") or ""
    if location:
        lines.append(f"location: {_yaml_scalar(location)}")
    if det.get("city"):
        lines.append(f"city: {_yaml_scalar(det['city'])}")
    if det.get("country"):
        lines.append(f"country: {_yaml_scalar(det['country'])}")

    # Social links
    for key in ("twitter_url", "fb_url", "linkedin_url", "github_url", "cb_url"):
        val = det.get(key) or ""
        if val:
            lines.append(f"{key}: {_yaml_scalar(val)}")

    # Tags and categories
    tags = det.get("tags") or d.get("tags") or []
    if tags:
        lines.append(f"tags:{_yaml_list(tags)}")
    industries = d.get("industries") or []
    if industries:
        lines.append(f"industries:{_yaml_list(industries)}")
    regions = d.get("regions") or []
    if regions:
        lines.append(f"regions:{_yaml_list(regions)}")

    # YC-specific
    if d.get("top_company"):
        lines.append("top_company: true")
    if d.get("isHiring"):
        lines.append("is_hiring: true")
    if d.get("nonprofit"):
        lines.append("nonprofit: true")
    if det.get("primary_partner"):
        lines.append(f"yc_partner: {_yaml_scalar(det['primary_partner'])}")

    # Rip-specific
    if rip:
        lines.append("has_postmortem: true")
    if rip.get("category"):
        lines.append(f"rip_category: {_yaml_scalar(rip['category'])}")

    lines.append("---")
    lines.append("")
    lines.append(f"# {name}")
    lines.append("")
    if one_liner:
        lines.append(f"> {one_liner}")
        lines.append("")
    if description:
        lines.append(description.strip())
        lines.append("")

    company_dir.mkdir(parents=True, exist_ok=True)
    (company_dir / "company.md").write_text("\n".join(lines))


def write_founders_md(slug: str, sources: dict, company_dir: Path):
    """Write founders.md from detail page and/or rip data."""
    det = sources.get("details", {})
    rip = sources.get("rip", {})

    founders = det.get("founders", [])
    rip_founders = rip.get("founders", [])

    if not founders and not rip_founders:
        return

    lines = [f"# Founders", ""]

    for f in founders:
        name = f.get("full_name") or f.get("name") or "Unknown"
        title = f.get("title") or ""
        lines.append(f"## {name}")
        if title:
            lines.append(f"**{title}**")
        lines.append("")
        bio = f.get("founder_bio") or ""
        if bio and bio.strip() != "-":
            lines.append(bio.strip())
            lines.append("")
        # Links
        links = []
        if f.get("linkedin_url") or f.get("linkedin"):
            links.append(f"[LinkedIn]({f.get('linkedin_url') or f.get('linkedin')})")
        if f.get("twitter_url") or f.get("twitter"):
            links.append(f"[Twitter]({f.get('twitter_url') or f.get('twitter')})")
        if links:
            lines.append(" | ".join(links))
            lines.append("")

    # Add rip founders if they have data not already covered
    if rip_founders and not founders:
        for f in rip_founders:
            name = f.get("name") or "Unknown"
            title = f.get("title") or ""
            lines.append(f"## {name}")
            if title:
                lines.append(f"**{title}**")
            lines.append("")
            links = []
            if f.get("linkedin"):
                links.append(f"[LinkedIn]({f['linkedin']})")
            if f.get("twitter"):
                links.append(f"[Twitter]({f['twitter']})")
            if links:
                lines.append(" | ".join(links))
                lines.append("")

    company_dir.mkdir(parents=True, exist_ok=True)
    (company_dir / "founders.md").write_text("\n".join(lines))


def write_news_md(slug: str, sources: dict, company_dir: Path):
    """Write news.md from detail page."""
    news = sources.get("details", {}).get("news", [])
    if not news:
        return

    lines = ["# News", ""]
    for item in news:
        title = item.get("title") or "Untitled"
        url = item.get("url") or ""
        date = item.get("date") or ""
        source = item.get("source") or ""
        link = f"[{title}]({url})" if url else title
        meta = f" — {source}" if source else ""
        if date:
            meta = f" ({date}){meta}"
        lines.append(f"- {link}{meta}")

    lines.append("")
    company_dir.mkdir(parents=True, exist_ok=True)
    (company_dir / "news.md").write_text("\n".join(lines))


def _fix_relative_urls(text: str, base: str) -> str:
    """Resolve relative URLs (e.g. /media/...) to absolute URLs."""
    return re.sub(
        r'(\]\(|src=["\'])(/[^)\s"\']+)',
        lambda m: m.group(1) + base + m.group(2),
        text,
    )


def write_launches_md(slug: str, sources: dict, company_dir: Path):
    """Write launches.md from detail page."""
    launches = sources.get("details", {}).get("launches", [])
    if not launches:
        return

    lines = ["# Launches", ""]
    for launch in launches:
        title = launch.get("title") or "Untitled"
        lines.append(f"## {title}")
        lines.append("")
        body = launch.get("body") or ""
        if body:
            lines.append(_fix_relative_urls(body.strip(), YC_BASE))
            lines.append("")

    company_dir.mkdir(parents=True, exist_ok=True)
    (company_dir / "launches.md").write_text("\n".join(lines))


def _write_sections_md(title: str, sections: list[dict]) -> str:
    """Convert a list of {heading, content} sections to markdown."""
    lines = [f"# {title}", ""]
    for sec in sections:
        heading = sec.get("heading") or ""
        content = sec.get("content") or ""
        if heading:
            lines.append(f"## {heading}")
            lines.append("")
        if content:
            lines.append(content.strip())
            lines.append("")
    return "\n".join(lines)


def write_postmortem_files(slug: str, sources: dict, company_dir: Path):
    """Write postmortem.md, buildplan.md, techspecs.md from startups.rip."""
    rip = sources.get("rip")
    if not rip:
        return

    company_dir.mkdir(parents=True, exist_ok=True)

    # Post-mortem report
    report = rip.get("report", {})
    if report.get("sections"):
        title = report.get("title") or "Post-Mortem Report"
        md = _write_sections_md(title, report["sections"])
        (company_dir / "postmortem.md").write_text(md)

    # Build plan
    build_plan = rip.get("build_plan", {})
    if build_plan.get("sections"):
        title = build_plan.get("title") or "Build Plan"
        md = _write_sections_md(title, build_plan["sections"])
        (company_dir / "buildplan.md").write_text(md)

    # Tech specs (preview + TOC)
    specs_preview = rip.get("specs_preview", {})
    specs_toc = rip.get("specs_toc", [])
    if specs_preview.get("sections") or specs_toc:
        lines = ["# Technical Specs", ""]
        if specs_toc:
            lines.append("## Table of Contents")
            lines.append("")
            for item in specs_toc:
                if isinstance(item, dict):
                    lines.append(f"- {item.get('title', '')}")
                elif isinstance(item, str):
                    lines.append(f"- {item}")
            lines.append("")
        if specs_preview.get("sections"):
            lines.append("## Preview")
            lines.append("")
            for sec in specs_preview["sections"]:
                heading = sec.get("heading") or ""
                content = sec.get("content") or ""
                if heading:
                    lines.append(f"### {heading}")
                    lines.append("")
                if content:
                    lines.append(content.strip())
                    lines.append("")
        (company_dir / "techspecs.md").write_text("\n".join(lines))


def build_index(companies: dict[str, dict]) -> list[dict]:
    """Build lightweight index for quick lookups."""
    index = []
    for slug, sources in sorted(companies.items()):
        d = sources.get("directory", {})
        det = sources.get("details", {})
        rip = sources.get("rip")
        batch = _resolve_batch(sources)

        index.append({
            "slug": slug,
            "name": det.get("name") or d.get("name") or (rip or {}).get("name") or slug,
            "batch": batch,
            "status": det.get("status") or d.get("status") or (rip or {}).get("status") or "",
            "has_postmortem": rip is not None,
        })
    return index


def transform_all():
    """Transform raw JSON data into directory-based markdown structure."""
    print("Loading raw data...")
    companies = load_raw_data()
    print(f"  {len(companies)} unique companies")

    # Count sources
    n_dir = sum(1 for s in companies.values() if "directory" in s)
    n_det = sum(1 for s in companies.values() if "details" in s)
    n_rip = sum(1 for s in companies.values() if "rip" in s)
    print(f"  Sources: {n_dir} directory, {n_det} details, {n_rip} rip")

    # Clean output directory (but preserve .gitkeep if any)
    if OUT_DIR.exists():
        for child in OUT_DIR.iterdir():
            if child.name.startswith("."):
                continue
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()

    print("Transforming...")
    for i, (slug, sources) in enumerate(sorted(companies.items())):
        batch = _resolve_batch(sources)
        batch_dir = batch if batch else "_no_batch"
        company_dir = OUT_DIR / batch_dir / slug

        write_company_md(slug, sources, company_dir)
        write_founders_md(slug, sources, company_dir)
        write_news_md(slug, sources, company_dir)
        write_launches_md(slug, sources, company_dir)
        write_postmortem_files(slug, sources, company_dir)

        if (i + 1) % 500 == 0:
            print(f"  [{i + 1}/{len(companies)}]")

    # Build and write index
    index = build_index(companies)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_DIR / "index.json", "w") as f:
        json.dump(index, f, indent=2)

    # Stats
    md_count = sum(1 for _ in OUT_DIR.rglob("*.md"))
    dir_count = sum(1 for p in OUT_DIR.rglob("*") if p.is_dir() and p.parent != OUT_DIR)
    print(f"\nDone! {md_count} markdown files across {dir_count} companies")
    print(f"Index: {OUT_DIR / 'index.json'} ({len(index)} entries)")


if __name__ == "__main__":
    transform_all()
