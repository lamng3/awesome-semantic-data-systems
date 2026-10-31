<!--
  Maintainer notes. This comment does not render on GitHub.

  Entry template (newest first within each section):

  - **[Title](link)**
    <br>Authors or organization · Venue/Source Year · [📄 Paper](...) · [💻 Code](...) · [📖 Docs](...)
    <br><sub>One or two sentences on what it is and why it is on the list.</sub>

  Use only the links that exist. Source labels: arXiv, conference (SIGMOD, VLDB, CIDR, ...),
  Blog (organization), or System for code-first projects.
  Add a new subsection only when it has at least one entry, and add it to the Contents list.
-->

<div align="center">

# Awesome Semantic DB

**A curated reading list on semantic data systems and memory for AI agents.**

[![License: CC0-1.0](https://img.shields.io/badge/license-CC0%201.0-lightgrey.svg)](LICENSE)

[🔎 Semantic Data Systems](#-semantic-data-systems) · [🧠 Agent Memory](#-agent-memory) · [🔖 Legend](#-legend)

</div>

LLMs are turning into database operators, and agents need a place to keep what they learn. This list follows both threads: query engines that run models inside query plans, databases built around meaning (ontologies, knowledge graphs, embeddings), and memory systems that let agents carry knowledge across sessions.

## Contents

- [🔎 Semantic Data Systems](#-semantic-data-systems)
  - [Semantic Query Engines and Operators](#semantic-query-engines-and-operators)
  - [Ontology and Knowledge Graph Databases](#ontology-and-knowledge-graph-databases)
- [🧠 Agent Memory](#-agent-memory)
  - [Memory Systems](#memory-systems)
- [🔖 Legend](#-legend)

---

## 🔎 Semantic Data Systems

Database systems where semantics are first class, either because models run as query operators or because the data model itself encodes meaning.

### Semantic Query Engines and Operators

LLM-powered operators (filter, join, extract, aggregate) inside declarative queries, with the algebra, cost models, and optimizers to run them efficiently.

- **[NousDB - A Fast Query Engine for Semantic Analytics](https://arxiv.org/abs/2610.28551)**
  <br>Christos Tsapelas, Georgia Koutrika, Yannis Ioannidis · arXiv 2026 · [📄 Paper](https://arxiv.org/pdf/2610.28551v1)
  <br><sub>A semantic analytics engine on Apache DataFusion. Extends relational algebra with three semantic operators whose algebraic properties enable query rewriting, and uses a token-based cost model with equi-depth token histograms to batch tuples within context-window limits. Reports up to 86× speedups.</sub>

### Ontology and Knowledge Graph Databases

Storage and query engines for RDF, OWL ontologies, and knowledge graphs, including reasoning and semantic search over them.

- **[OntoDB: A Database Management System for Ontologies](https://github.com/lamng3/OntoDB)**
  <br>Lam Nguyen · System 2026 · [💻 Code](https://github.com/lamng3/OntoDB) · [📖 Docs](https://lamng3.com/ontodb/)
  <br><sub>An RDF/SPARQL database with B+ tree triple indexes, a cost-based optimizer, strict two-phase locking, and ARIES recovery. Supports semantic search through interval labeling of class hierarchies and exact, IVF, and HNSW vector indexes, plus RDFS subclass entailment without materializing triples.</sub>

<div align="right"><a href="#awesome-semantic-db">⬆ back to top</a></div>

---

## 🧠 Agent Memory

How agents store, consolidate, and retrieve what they learn across sessions, and how to measure whether memory helps.

### Memory Systems

Architectures and production systems for persistent agent memory.

- **[MemCurrent: Designing Persistent Memory for Production Agents](https://www.databricks.com/blog/memcurrent-designing-persistent-memory-production-agents)**
  <br>Databricks AI Research · Blog (Databricks) 2026 · [📝 Blog](https://www.databricks.com/blog/memcurrent-designing-persistent-memory-production-agents)
  <br><sub>Combines episodic memory (raw session traces) with derived memory (a structured knowledge base of distilled learnings), accessed through plugins, agent tools, and an offline "dreaming" consolidation pipeline. Powers Agent Bricks Memory and Genie, and triples pass rate over no memory on an internal enterprise benchmark with 31% fewer tokens.</sub>

<div align="right"><a href="#awesome-semantic-db">⬆ back to top</a></div>

---

## 🔖 Legend

| Link | Meaning |
| --- | --- |
| 📄 Paper | Paper or preprint |
| 📝 Blog | Blog post or technical report |
| 💻 Code | Source code |
| 📖 Docs | Documentation or manual |

Entries are listed newest first within each section.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the maintainer has waived all copyright and related rights to this list. See [LICENSE](LICENSE).
