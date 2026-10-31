# /// script
# requires-python = ">=3.11"
# ///
"""Validate data/*.toml and regenerate the marked blocks of README.md.

Usage:
    uv run scripts/build.py          # rewrite README.md
    uv run scripts/build.py --check  # exit 1 if README.md is stale or data is invalid
"""

from __future__ import annotations

import datetime as dt
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAXONOMY = ROOT / "data" / "taxonomy.toml"
PAPERS = ROOT / "data" / "papers.toml"
README = ROOT / "README.md"

REQUIRED = {"title", "venue", "year", "section", "url", "summary", "added"}
OPTIONAL = {"authors", "org", "code", "docs", "project"}
EXTRA_LINKS = [("code", "Code"), ("docs", "Docs"), ("project", "Project")]
MAX_AUTHORS = 3
MAX_SUMMARY = 400
RECENT_COUNT = 10
ARXIV_ABS = re.compile(r"^https://arxiv\.org/abs/\d{4}\.\d{4,5}$")
# Headings written by hand in README.md; generated headings must not collide with them.
STATIC_HEADINGS = {"Awesome Semantic DB", "Contents", "Recently Added", "Contributing", "License"}


def slug(text: str) -> str:
    text = re.sub(r"[^\w\- ]", "", text.lower())
    return text.replace(" ", "-")


def load() -> tuple[list[dict], list[dict], list[str]]:
    errors: list[str] = []
    parts = tomllib.loads(TAXONOMY.read_text())["part"]
    entries = tomllib.loads(PAPERS.read_text()).get("entry", [])

    section_ids: set[str] = set()
    slugs = {slug(h) for h in STATIC_HEADINGS}
    for part in parts:
        for heading in [part["title"]] + [s["title"] for s in part["section"]]:
            if slug(heading) in slugs:
                errors.append(f"taxonomy: heading {heading!r} collides with another heading")
            slugs.add(slug(heading))
        for section in part["section"]:
            if section["id"] in section_ids:
                errors.append(f"taxonomy: duplicate section id {section['id']!r}")
            section_ids.add(section["id"])

    seen_urls: dict[str, str] = {}
    seen_titles: dict[str, str] = {}
    this_year = dt.date.today().year
    for e in entries:
        name = e.get("title", "<untitled>")
        where = f"papers.toml: {name!r}"
        if missing := REQUIRED - e.keys():
            errors.append(f"{where}: missing {', '.join(sorted(missing))}")
            continue
        if unknown := e.keys() - REQUIRED - OPTIONAL:
            errors.append(f"{where}: unknown field {', '.join(sorted(unknown))}")
        if ("authors" in e) == ("org" in e):
            errors.append(f"{where}: set exactly one of authors or org")
        if e["section"] not in section_ids:
            errors.append(f"{where}: unknown section {e['section']!r}")
        if not isinstance(e["year"], int) or not 1950 <= e["year"] <= this_year + 1:
            errors.append(f"{where}: year must be an integer between 1950 and {this_year + 1}")
        if not isinstance(e["added"], dt.date):
            errors.append(f"{where}: added must be a date like 2026-10-31")
        if "arxiv.org" in e["url"] and not ARXIV_ABS.match(e["url"]):
            errors.append(f"{where}: arXiv links use the versionless abstract page, https://arxiv.org/abs/NNNN.NNNNN")
        for key in ["url"] + [k for k, _ in EXTRA_LINKS]:
            if key in e and not e[key].startswith("https://"):
                errors.append(f"{where}: {key} must start with https://")
        if len(e["summary"]) > MAX_SUMMARY:
            errors.append(f"{where}: summary is {len(e['summary'])} characters, limit {MAX_SUMMARY}")
        if e["title"].endswith("."):
            errors.append(f"{where}: title ends with a period")
        for seen, key, label in [(seen_urls, e["url"], "url"), (seen_titles, e["title"].casefold(), "title")]:
            if key in seen:
                errors.append(f"{where}: same {label} as {seen[key]!r}")
            seen[key] = name
    return parts, entries, errors


def byline(e: dict) -> str:
    if "org" in e:
        return e["org"]
    authors = e["authors"]
    if len(authors) > MAX_AUTHORS:
        return f"{authors[0]} et al."
    return ", ".join(authors)


def render_entry(e: dict) -> str:
    meta = [byline(e), f"*{e['venue']} {e['year']}*"]
    meta += [f"[{label}]({e[key]})" for key, label in EXTRA_LINKS if key in e]
    return (
        f"- **[{e['title']}]({e['url']})**<br>\n"
        f"  {' · '.join(meta)}<br>\n"
        f"  {e['summary']}"
    )


def newest_first(entries: list[dict]) -> list[dict]:
    return sorted(entries, key=lambda e: (-e["year"], -e["added"].toordinal(), e["title"].casefold()))


def group(parts: list[dict], entries: list[dict]) -> list[tuple[dict, list[tuple[dict, list[dict]]]]]:
    """Parts and sections that have entries, each section's entries newest first."""
    out = []
    for part in parts:
        sections = []
        for section in part["section"]:
            members = [e for e in entries if e["section"] == section["id"]]
            if members:
                sections.append((section, newest_first(members)))
        if sections:
            out.append((part, sections))
    return out


def render_contents(grouped, total: int) -> str:
    n_sections = sum(len(s) for _, s in grouped)
    lines = [f"{total} entries across {n_sections} sections.", ""]
    if total >= RECENT_COUNT:
        lines.append(f"- [Recently Added](#{slug('Recently Added')})")
    for part, sections in grouped:
        count = sum(len(m) for _, m in sections)
        lines.append(f"- [{part['title']}](#{slug(part['title'])}) ({count})")
        for section, members in sections:
            lines.append(f"  - [{section['title']}](#{slug(section['title'])}) ({len(members)})")
    return "\n".join(lines)


def render_recent(entries: list[dict]) -> str:
    if len(entries) < RECENT_COUNT:
        return ""
    recent = sorted(entries, key=lambda e: (-e["added"].toordinal(), e["title"].casefold()))[:RECENT_COUNT]
    lines = ["## Recently Added", ""]
    lines += [f"- {e['added'].isoformat()} · [{e['title']}]({e['url']})" for e in recent]
    return "\n".join(lines)


def render_list(grouped) -> str:
    blocks = []
    for part, sections in grouped:
        lines = [f"## {part['title']}", "", part["description"], ""]
        for section, members in sections:
            lines += [f"### {section['title']}", "", section["description"], ""]
            lines += [render_entry(e) for e in members]
            lines.append("")
        lines.append('<div align="right"><a href="#awesome-semantic-db">Back to top</a></div>')
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def fill(readme: str, name: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- BEGIN {name} -->\n).*?(<!-- END {name} -->)", re.S)
    if not pattern.search(readme):
        raise SystemExit(f"README.md: missing <!-- BEGIN {name} --> / <!-- END {name} --> markers")
    content = f"{body}\n" if body else ""
    return pattern.sub(lambda m: m.group(1) + content + m.group(2), readme)


def main() -> int:
    check = "--check" in sys.argv[1:]
    parts, entries, errors = load()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    grouped = group(parts, entries)
    current = README.read_text()
    updated = current
    updated = fill(updated, "CONTENTS", render_contents(grouped, len(entries)))
    updated = fill(updated, "RECENT", render_recent(entries))
    updated = fill(updated, "LIST", render_list(grouped))

    if check:
        if updated != current:
            print("README.md is out of date. Run `make` and commit the result.", file=sys.stderr)
            return 1
        return 0
    README.write_text(updated)
    print(f"README.md: {len(entries)} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
