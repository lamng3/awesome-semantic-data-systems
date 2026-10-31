# Contributing

This is a curated list, hand-picked rather than exhaustive. The maintainer chooses what goes in, and suggestions are welcome as issues. Each entry appears in one pillar, newest first, and every entry is presented the same way: no badges, rankings, or highlights.

## Scope

An entry belongs here if its main contribution falls under one of three pillars:

- **Semantic Query Processing.** Engines and operators that call models inside declarative queries, the optimization of such queries, and vector or hybrid search treated as a query-processing problem.
- **Knowledge Graphs and Ontologies.** Storing and querying ontologies and knowledge graphs, matching them, versioning and evolving them, checking changes for errors, and ontologies built for agents to use.
- **Agent Memory.** How agents store, organize, recall, and forget what they learn across sessions, and how memory is evaluated.

Out of scope: general LLM papers, prompt engineering, ontology or knowledge graph applications with no contribution to how the knowledge is managed, and RAG pipelines that make no systems or memory contribution.

## Structure

The pillars are defined in [`data/taxonomy.toml`](data/taxonomy.toml). Each is one flat list, newest first, until it is large enough to need sections.

### Placement rules

Each entry goes in exactly one pillar, chosen by its main contribution:

1. **Memory is about the agent's own experience.** A store of what an agent learned across sessions is Agent Memory, even when it is built on a database or a knowledge graph.
2. **Ontologies and knowledge graphs are about curated domain knowledge.** An ontology or knowledge graph that an agent reads, including one the agent builds or refines, is Knowledge Graphs and Ontologies.
3. **Query processing is about running queries.** An engine, operator, or optimizer is Semantic Query Processing, even when its queries run over a knowledge graph, unless the contribution is specific to ontologies.
4. **When torn, pick the pillar a reader would look in first,** and keep the TL;DR specific enough that the entry is still findable.

### Splitting a pillar

- Split a pillar once it passes about 15 entries, into 2 to 4 sections along a seam the entries already show. The likely seams are noted in `data/taxonomy.toml`.
- Never create a section ahead of the entries that fill it, and never for a single paper.
- Once a pillar is split, every entry in it needs a `section`. Section ids become README anchors, so never change one once it has entries.

## Adding an entry

1. Add an `[[entry]]` to [`data/papers.toml`](data/papers.toml).
2. Run `make`. It validates the data and regenerates `README.md` and `references.bib`.
3. Commit all three files. CI fails if either generated file does not match the data.

`make` needs [uv](https://docs.astral.sh/uv/). Without it, run `python3 scripts/build.py` with Python 3.11 or newer.

```toml
[[entry]]
title = "Exact Title as Published"
authors = ["First Author", "Second Author"]   # or: org = "Databricks AI Research"
venue = "VLDB"                               # arXiv, SIGMOD, CIDR, Databricks Blog, GitHub, ...
year = 2026
pillar = "query"                            # query, knowledge, or memory
url = "https://arxiv.org/abs/2610.28551"
code = "https://github.com/..."              # optional
docs = "https://..."                         # optional
project = "https://..."                      # optional
tldr = "One line, shown in the list."
summary = "One or two sentences, shown when the TL;DR is expanded."   # optional
added = 2026-10-31
```

## Fields

| Field | Required | Notes |
| --- | --- | --- |
| `title` | yes | Exact title, no trailing period. |
| `authors` or `org` | one of them | Full author list, each name written given name first. The list shows a citation (Smith; Smith and Lee; Smith et al.), and the expanded view shows every name. Use `org` for team-authored posts. |
| `cite` | no | Overrides the citation when the family name is not the last word, for example `cite = "Zhang Wei"`. |
| `venue` | yes | The venue where it was published. When a preprint is accepted, change `arXiv` to the conference and keep the same `url`. |
| `year` | yes | Year of the version being linked. |
| `pillar` | yes | `query`, `knowledge`, or `memory`. See the placement rules. |
| `section` | only in a split pillar | One of the pillar's section ids. |
| `url` | yes | Canonical page. For arXiv, use the versionless abstract page, `https://arxiv.org/abs/NNNN.NNNNN`, not a PDF. |
| `arxiv` | no | The arXiv abstract page of a paper whose `url` is the published version, so readers have a free copy. |
| `code`, `docs`, `project` | no | Extra links. Omit them rather than leaving them empty. || `tldr` | yes | At most 100 characters, so it stays on one line. Name the core idea, not the paper's claims, so it jogs your memory when skimming. |
| `summary` | no | At most 400 characters, hidden until the TL;DR is clicked. Say what it does and what is new, in neutral terms. Leave out headline numbers that only make sense in context. |
| `added` | yes | The date the entry was added. Drives "Recently Added". |
| `bibtex` | no | The official BibTeX, pasted as a `"""` multi-line string, for example from DBLP or the publisher. Used verbatim in `references.bib`. Prefer it for published papers. |
| `bibkey` | no | Overrides the generated key (`surname` + `year` + first title word, such as `tsapelas2026nousdb`). Only needed when two entries would get the same key. |

## BibTeX

`make` also writes [`references.bib`](references.bib) with one entry per item, in README order. Without a `bibtex` field, arXiv papers become `@misc` entries with `eprint`, and everything else becomes `@misc` with `howpublished` set to the venue. Keys never change once published, so set `bibkey` rather than renaming when titles change.

## Checks

- `make check` validates the data and confirms that `README.md` is up to date. CI runs it on every push and pull request.
- A weekly workflow checks every link in the README.
