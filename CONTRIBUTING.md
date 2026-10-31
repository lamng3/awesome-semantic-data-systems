# Contributing

This is a curated list, hand-picked rather than exhaustive. The maintainer chooses what goes in, and suggestions are welcome as issues. Each entry appears in one section, newest first, and every entry is presented the same way: no badges, rankings, or highlights.

## Scope

The list has two pillars. An entry belongs here if its main contribution falls under one of them:

- **Semantic Data Systems.** Data systems where meaning is first class: engines and operators that call models, the optimization of such queries, knowledge graph and ontology databases, and vector or hybrid search treated as a database problem.
- **Agent Memory.** How agents store, organize, recall, and forget knowledge across sessions, and how memory is evaluated.

General LLM papers, prompt-engineering techniques, and RAG applications that make no systems or memory contribution are out of scope.

## Structure

Both pillars follow the same order: surveys, then systems, then techniques, then benchmarks. Semantic Data Systems has two extra sections for ontologies, which are a focus of this list. Sections are defined in [`data/taxonomy.toml`](data/taxonomy.toml).

| Semantic Data Systems | Agent Memory |
| --- | --- |
| `sds-surveys` Surveys and Vision | `mem-surveys` Surveys and Vision |
| `sds-engines` Semantic Operators and Query Engines | `mem-systems` Memory Architectures and Systems |
| `sds-optimization` Query Optimization and Execution | `mem-representation` Representation and Retrieval |
| `sds-semantic-layers` Ontologies and Semantic Layers for Agents | `mem-management` Consolidation, Updating, and Forgetting |
| `sds-knowledge-graphs` Knowledge Graph and Ontology Databases | `mem-experiential` Experiential and Procedural Memory |
| `sds-ontology-evolution` Ontology Matching, Versioning, and Evolution | `mem-benchmarks` Benchmarks and Evaluation |
| `sds-vector-search` Vector and Hybrid Search | |
| `sds-benchmarks` Benchmarks | |

### Placement rules

Each entry goes in exactly one section, chosen by its main contribution:

1. **Pillar first.** Memory systems built on a database belong to Agent Memory. Data systems designed for agent workloads belong to Semantic Data Systems.
2. **Surveys and benchmarks win.** A survey goes in Surveys and Vision, and a benchmark goes in Benchmarks, even if it also proposes a system or a baseline.
3. **Systems over techniques.** A paper that presents a complete engine or memory system goes in the systems section, even if it also introduces an optimization or a retrieval method. It goes in a technique section only when that technique is the main contribution and the system is a vehicle for it.
4. **When torn, pick the section a reader would look in first** and keep the TL;DR specific enough that it is still findable.

### Changing the structure

- An empty section stays hidden until it gets an entry, so planned sections cost nothing.
- Section ids are the README link anchors. Never change an id once it has entries. Titles can be renamed freely.
- Add a section only when an existing one doesn't fit and the new one will collect several entries. Split a section once it passes about 15 entries and has a natural seam.

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
section = "sds-engines"                      # an id from data/taxonomy.toml
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
| `section` | yes | One section id. See the placement rules. |
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
