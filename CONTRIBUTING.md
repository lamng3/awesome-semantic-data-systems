# Contributing

This is a curated list, hand-picked rather than exhaustive. The maintainer chooses what goes in, and suggestions are welcome as issues. Each entry appears in one place, newest first, as one line: venue and year, title, authors, and links. There are no badges, rankings, or&nbsp;summaries.

## The bar

The README is a short list meant to be read in full, so each paper has to earn its place: published at a top venue (such as KDD, VLDB, SIGMOD, ICDE, TKDE, TKDD, CIKM, ICLR, ICML, NeurIPS, ACL, ISWC, ESWC, and the top security and theory venues), or a strong industry paper that may never be published. Algorithmic contributions come first. Everything else worth tracking, such as follow-ups, benchmarks, surveys, and preprints, goes to the [long list](LONGLIST.md), marked with `longlist = true` in its&nbsp;entry.

## Scope

An entry belongs here if its main contribution falls under one of five&nbsp;pillars:

- **Semantic Query Processing.** Engines and operators that call models inside declarative queries, and the optimization of such&nbsp;queries.
- **Vector Search.** Approximate nearest neighbor search: graph indexes, quantization and partitioning, search tuned to GPUs and CPUs (including kernel fusion), and vector databases with filtered or hybrid&nbsp;queries.
- **Knowledge Graphs and Ontologies.** Storing and querying ontologies and knowledge graphs, matching them, versioning and evolving them, checking changes for errors, and ontologies built for agents to&nbsp;use.
- **Agent Memory.** How agents store, organize, recall, and forget what they learn across sessions, including offline consolidation such as sleep and dreaming, and how memory is&nbsp;evaluated.
- **Attacks and Robustness.** Poisoning of retrieval corpora and knowledge graphs, adversarial perturbation of data and metadata, data quality, and the search and graph algorithms that attacks are built on (beam search, Monte Carlo tree search, network flows, dynamic&nbsp;trees).

Out of scope: general LLM papers, prompt engineering, and applications that make no contribution to how data or knowledge is stored, searched, remembered, or&nbsp;attacked.

## Structure

The pillars and their sections are defined in [`data/taxonomy.toml`](data/taxonomy.toml), and each pillar's entries live in `data/papers/<pillar>.toml`. A pillar is one flat list, newest first, until it is large enough to need&nbsp;sections.

### Placement rules

Each entry goes in exactly one place, chosen by its main&nbsp;contribution:

1. **Memory is about the agent's own experience.** A store of what an agent learned across sessions is Agent Memory, even when it is built on a database or a knowledge&nbsp;graph.
2. **Ontologies and knowledge graphs are about curated domain knowledge.** An ontology or knowledge graph that an agent reads, including one the agent builds or refines, is Knowledge Graphs and&nbsp;Ontologies.
3. **Vector search is about the index.** A vector index, its hardware, or a vector database is Vector Search; an engine that runs models inside queries is Semantic Query&nbsp;Processing.
4. **Attacks go with the attack.** A paper whose contribution is an attack, a defense, or robustness under perturbation is Attacks and Robustness, whatever system it&nbsp;targets.
5. **When torn, pick the place a reader would look in&nbsp;first.**

### Splitting a pillar

- Split a pillar once it passes about 15 entries, into 2 to 4 sections along a seam the entries already show. The likely seams are noted in&nbsp;`data/taxonomy.toml`.
- Never create a section ahead of the entries that fill it, and never for a single&nbsp;paper.
- Once a pillar is split, every entry in it needs a `section`. Section ids become README anchors, so never change one once it has&nbsp;entries.

## Adding an entry

1. Add an `[[entry]]` to the pillar's file in&nbsp;[`data/papers/`](data/papers).
2. Run `make`. It validates the data and regenerates `README.md`, `LONGLIST.md`, and&nbsp;`references.bib`.
3. Commit the data file with `README.md`, `LONGLIST.md`, and `references.bib`. CI fails if a generated file does not match the&nbsp;data.

`make` needs [uv](https://docs.astral.sh/uv/). Without it, run `python3 scripts/build.py` with Python 3.11 or&nbsp;newer.

```toml
[[entry]]
title = "Exact Title as Published"
authors = ["First Author", "Second Author"]   # or: org = "Databricks AI Research"
section = "vector-graph"                     # only in a split pillar
venue = "VLDB"                               # arXiv, SIGMOD, KDD, ICLR, ...
year = 2026
url = "https://doi.org/..."
arxiv = "https://arxiv.org/abs/NNNN.NNNNN"    # optional
code = "https://github.com/..."              # optional
added = 2026-11-20
longlist = true                              # optional: track it in LONGLIST.md, not the README
bibtex = '''
@inproceedings{author2026title,
  ...
}
'''
```

## Fields

| Field | Required | Notes |
| --- | --- | --- |
| `title` | yes | Exact title, no trailing period. |
| `authors` or `org` | one of them | Full author list, each name written given name first. The list shows Smith; Smith and Lee; or Smith et al. Use `org` for team-authored posts. |
| `cite` | no | Overrides the author text when the family name is not the last word, for example `cite = "Zhang Wei"`. |
| `section` | only in a split pillar | One of the pillar's section ids. |
| `venue` | yes | Short venue name: `VLDB` for PVLDB, `SIGMOD` for PACMMOD, `arXiv` for preprints. When a preprint is accepted, change the venue and year. |
| `year` | yes | Year of the version being linked. |
| `url` | yes | Canonical page: the DOI for published papers, otherwise the proceedings page, otherwise the arXiv abstract page (`https://arxiv.org/abs/NNNN.NNNNN`). |
| `arxiv` | no | The arXiv abstract page of a paper whose `url` is the published version. |
| `code`, `docs`, `project` | no | Extra links. Omit them rather than leaving them empty. |
| `added` | yes | The date the entry was added. |
| `longlist` | no | `true` puts the entry in [LONGLIST.md](LONGLIST.md) instead of the README. See the bar above. |
| `bibtex` | no | The BibTeX entry, pasted as a `'''` multi-line string and used verbatim. Prefer it for published papers. |
| `bibkey` | no | Overrides the generated key (`surname` + `year` + first title word, such as `tsapelas2026nousdb`) when two entries would collide. |

## BibTeX

`make` writes [`references.bib`](references.bib) with every entry from the README and the long list, in section order, with a comment header before each section. Without a `bibtex` field, arXiv papers become `@misc` entries with `eprint`, and everything else becomes `@misc` with `howpublished` set to the venue. Keys never change once published, so set `bibkey` rather than renaming when titles&nbsp;change.

## Checks

- `make check` validates the data and confirms that `README.md`, `LONGLIST.md`, and `references.bib` are up to date. CI runs it on every push and pull&nbsp;request.
- A weekly workflow checks every link in the README and the long&nbsp;list.
