# Contributing

This is a curated list. The maintainer chooses what goes in, and suggestions are welcome as issues.

## Scope

An entry belongs here if its main contribution is one of:

- **Semantic data systems.** Query engines and operators that call models, the optimization of such queries, ontology and knowledge graph databases, and vector or hybrid search as a database problem.
- **Agent memory.** How agents store, consolidate, retrieve, and forget knowledge across sessions, and how memory is evaluated.

General LLM papers, prompt-engineering techniques, and RAG applications that make no systems or memory contribution are out of scope.

## Adding an entry

1. Add an `[[entry]]` to [`data/papers.toml`](data/papers.toml).
2. Run `make`. It validates the data and regenerates `README.md`.
3. Commit both files. CI fails if `README.md` does not match the data.

`make` needs [uv](https://docs.astral.sh/uv/). Without it, run `python3 scripts/build.py` with Python 3.11 or newer.

```toml
[[entry]]
title = "Exact Title as Published"
authors = ["First Author", "Second Author"]   # or: org = "Databricks AI Research"
venue = "VLDB"                               # arXiv, SIGMOD, CIDR, Databricks Blog, GitHub, ...
year = 2026
section = "semantic-query-engines"           # an id from data/taxonomy.toml
url = "https://arxiv.org/abs/2610.28551"
code = "https://github.com/..."              # optional
docs = "https://..."                         # optional
project = "https://..."                      # optional
summary = "One or two sentences on what it contributes."
added = 2026-10-31
```

## Fields

| Field | Required | Notes |
| --- | --- | --- |
| `title` | yes | Exact title, no trailing period. |
| `authors` or `org` | one of them | Full author list. The README shows up to three names, then "et al.". Use `org` for team-authored posts. |
| `venue` | yes | The venue where it was published. When a preprint is accepted, change `arXiv` to the conference and keep the same `url`. |
| `year` | yes | Year of the version being linked. |
| `section` | yes | Exactly one section. Pick the one that matches its main contribution. |
| `url` | yes | Canonical page. For arXiv, use the versionless abstract page, `https://arxiv.org/abs/NNNN.NNNNN`, not a PDF. |
| `code`, `docs`, `project` | no | Extra links. Omit them rather than leaving them empty. |
| `summary` | yes | At most 400 characters. Say what it does and what is new, in neutral terms. Leave out headline numbers that only make sense in context. |
| `added` | yes | The date the entry was added. Drives "Recently Added". |

## Sections

Sections are defined in [`data/taxonomy.toml`](data/taxonomy.toml). An empty section stays hidden until it gets an entry. Before adding a section, check that an existing one doesn't already fit, and expect it to collect at least a few entries. Changing a section's title changes its link anchor, so rename sections sparingly.

## Checks

- `make check` validates the data and confirms that `README.md` is up to date. CI runs it on every push and pull request.
- A weekly workflow checks every link in the README.
