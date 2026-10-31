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
import html
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAXONOMY = ROOT / "data" / "taxonomy.toml"
PAPERS = ROOT / "data" / "papers.toml"
README = ROOT / "README.md"

REQUIRED = {"title", "venue", "year", "section", "url", "tldr", "added"}
OPTIONAL = {"authors", "org", "cite", "code", "docs", "project", "summary"}
EXTRA_LINKS = [("code", "Code"), ("docs", "Docs"), ("project", "Project")]
# Long enough for one clause, short enough to stay on one line in GitHub's README column.
MAX_TLDR = 100
MAX_DESCRIPTION = 100
MAX_SUMMARY = 400
RECENT_COUNT = 10
ARXIV_ABS = re.compile(r"^https://arxiv\.org/abs/\d{4}\.\d{4,5}$")
SECTION_ID = re.compile(r"^(sds|mem)-[a-z0-9-]+$")
SURNAME_PARTICLES = {"da", "das", "de", "del", "della", "der", "di", "dos", "du", "la", "le", "ten", "ter", "van", "von"}
NAME_SUFFIXES = {"jr", "jr.", "sr", "sr.", "ii", "iii", "iv"}
# Headings written by hand in README.md; generated anchors must not collide with them.
STATIC_HEADINGS = {"Awesome Semantic DB", "Contents", "Recently Added", "Contributing", "License"}


def slug(text: str) -> str:
    text = re.sub(r"[^\w\- ]", "", text.lower())
    return text.replace(" ", "-")


def md_escape(text: str) -> str:
    return re.sub(r"([\\`*_\[\]<>])", r"\\\1", text)


def nbsp(text: str) -> str:
    return text.replace(" ", "&nbsp;")


def no_widow(text: str) -> str:
    """Join the last two words so a wrapped line never ends with a single word."""
    head, _, last = text.rpartition(" ")
    return f"{head}&nbsp;{last}" if head else text


def load() -> tuple[list[dict], list[dict], list[str]]:
    errors: list[str] = []
    pillars = tomllib.loads(TAXONOMY.read_text())["pillar"]
    entries = tomllib.loads(PAPERS.read_text()).get("entry", [])

    anchors = {slug(h) for h in STATIC_HEADINGS}
    section_ids: set[str] = set()
    for pillar in pillars:
        if slug(pillar["title"]) in anchors:
            errors.append(f"taxonomy: pillar {pillar['title']!r} collides with another heading")
        anchors.add(slug(pillar["title"]))
    for item in [*pillars, *(s for p in pillars for s in p["section"])]:
        if len(item["description"]) > MAX_DESCRIPTION:
            errors.append(f"taxonomy: description of {item['title']!r} is {len(item['description'])} characters, limit {MAX_DESCRIPTION}")
    for pillar in pillars:
        for section in pillar["section"]:
            sid = section["id"]
            if not SECTION_ID.match(sid):
                errors.append(f"taxonomy: section id {sid!r} must look like sds-name or mem-name")
            if sid in section_ids or sid in anchors:
                errors.append(f"taxonomy: section id {sid!r} is not unique")
            section_ids.add(sid)

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
        if "authors" in e and (not e["authors"] or not all(isinstance(a, str) and a.strip() for a in e["authors"])):
            errors.append(f"{where}: authors must be a non-empty list of names")
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
        if len(e["tldr"]) > MAX_TLDR:
            errors.append(f"{where}: tldr is {len(e['tldr'])} characters, limit {MAX_TLDR}")
        if len(e.get("summary", "")) > MAX_SUMMARY:
            errors.append(f"{where}: summary is {len(e['summary'])} characters, limit {MAX_SUMMARY}")
        for key in ("tldr", "summary", "cite"):
            if "\n" in e.get(key, ""):
                errors.append(f"{where}: {key} must be a single line")
        if e["title"].endswith("."):
            errors.append(f"{where}: title ends with a period")
        for seen, key, label in [(seen_urls, e["url"], "url"), (seen_titles, e["title"].casefold(), "title")]:
            if key in seen:
                errors.append(f"{where}: same {label} as {seen[key]!r}")
            seen[key] = name
    return pillars, entries, errors


def surname(name: str) -> str:
    tokens = name.split()
    while len(tokens) > 1 and tokens[-1].lower() in NAME_SUFFIXES:
        tokens.pop()
    start = len(tokens) - 1
    while start > 0 and tokens[start - 1].lower() in SURNAME_PARTICLES:
        start -= 1
    return " ".join(tokens[start:])


def cite(e: dict) -> str:
    """Author part of an inline citation: Smith, Smith and Lee, or Smith et al."""
    if "cite" in e:
        return e["cite"]
    if "org" in e:
        return e["org"]
    names = [surname(a) for a in e["authors"]]
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return f"{names[0]} et al."


def render_entry(e: dict) -> str:
    # The citation may break only after its comma, and never leaves the title's last word behind.
    links = "".join(f"&nbsp;·&nbsp;[{label}]({e[key]})" for key, label in EXTRA_LINKS if key in e)
    citation = f"({nbsp(md_escape(cite(e)))}, {nbsp(md_escape(e['venue']))}&nbsp;{e['year']})"
    head = f"- **[{md_escape(e['title'])}]({e['url']})**&nbsp;{citation}{links}"

    details = []
    if "summary" in e:
        details.append(no_widow(html.escape(e["summary"])))
    if "authors" in e:
        details.append(f"<i>Authors:</i> {no_widow(html.escape(', '.join(e['authors'])))}")
    tldr = no_widow(html.escape(e["tldr"]))
    if not details:
        return f"{head}<br>\n  {tldr}"
    body = "<br><br>".join(details)
    return f"{head}\n  <details><summary>{tldr}</summary><blockquote>{body}</blockquote></details>"


def newest_first(entries: list[dict]) -> list[dict]:
    return sorted(entries, key=lambda e: (-e["year"], -e["added"].toordinal(), e["title"].casefold()))


def group(pillars: list[dict], entries: list[dict]) -> list[tuple[dict, list[tuple[dict, list[dict]]]]]:
    """Pillars with their non-empty sections, each section's entries newest first."""
    out = []
    for pillar in pillars:
        sections = []
        for section in pillar["section"]:
            members = [e for e in entries if e["section"] == section["id"]]
            if members:
                sections.append((section, newest_first(members)))
        out.append((pillar, sections))
    return out


def render_contents(grouped, total: int) -> str:
    lines = []
    if total >= RECENT_COUNT:
        lines.append(f"- [Recently Added](#{slug('Recently Added')})")
    for pillar, sections in grouped:
        if not sections:
            continue
        lines.append(f"- [{pillar['title']}](#{slug(pillar['title'])})")
        lines += [f"  - [{s['title']}](#{s['id']})" for s, _ in sections]
    return "\n".join(lines)


def render_recent(entries: list[dict]) -> str:
    if len(entries) < RECENT_COUNT:
        return ""
    recent = sorted(entries, key=lambda e: (-e["added"].toordinal(), e["title"].casefold()))[:RECENT_COUNT]
    lines = ["## Recently Added", ""]
    lines += [f"- {e['added'].isoformat()} · [{md_escape(e['title'])}]({e['url']})" for e in recent]
    return "\n".join(lines)


def render_list(grouped) -> str:
    blocks = []
    for pillar, sections in grouped:
        if not sections:
            continue
        lines = [f"## {pillar['title']}", "", no_widow(pillar["description"])]
        for section, members in sections:
            lines += ["", f'### <a id="{section["id"]}"></a>{section["title"]}', "", no_widow(section["description"]), ""]
            lines += [render_entry(e) for e in members]
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
    pillars, entries, errors = load()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    grouped = group(pillars, entries)
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
