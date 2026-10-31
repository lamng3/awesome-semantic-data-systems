<!--
  The blocks between BEGIN and END markers are generated from data/*.toml.
  Edit the data files and run `make`; edits inside the markers are overwritten.
-->

<div align="center">

# Awesome Semantic DB

**A curated reading list on semantic data systems and memory for AI agents.**

[![Check](https://github.com/lamng3/awesome-semantic-db/actions/workflows/check.yml/badge.svg)](https://github.com/lamng3/awesome-semantic-db/actions/workflows/check.yml)
[![Links](https://github.com/lamng3/awesome-semantic-db/actions/workflows/links.yml/badge.svg)](https://github.com/lamng3/awesome-semantic-db/actions/workflows/links.yml)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0%201.0-lightgrey.svg)](LICENSE)

</div>

Language models are becoming database operators, and agents need somewhere to keep what they learn. This list follows both threads: query engines that run models inside query plans, databases built around meaning (ontologies, knowledge graphs, embeddings), and memory systems that let agents carry knowledge across sessions.
## Contents

<!-- BEGIN CONTENTS -->
3 entries across 3 sections.

- [Semantic Data Systems](#semantic-data-systems) (2)
  - [Semantic Query Engines and Operators](#semantic-query-engines-and-operators) (1)
  - [Ontology and Knowledge Graph Databases](#ontology-and-knowledge-graph-databases) (1)
- [Agent Memory](#agent-memory) (1)
  - [Memory Architectures and Systems](#memory-architectures-and-systems) (1)
<!-- END CONTENTS -->

<!-- BEGIN RECENT -->
<!-- END RECENT -->

<!-- BEGIN LIST -->
## Semantic Data Systems

Database systems where semantics are first class, either because models run as query operators or because the data model itself encodes meaning.

### Semantic Query Engines and Operators

Systems that run LLM-powered operators (filter, join, extract, aggregate) inside declarative queries over structured and unstructured data.

- **[NousDB - A Fast Query Engine for Semantic Analytics](https://arxiv.org/abs/2610.28551)**<br>
  <sub>Christos Tsapelas, Georgia Koutrika, Yannis Ioannidis · <i>arXiv 2026</i></sub>
  <details><summary>Semantic operators with algebraic rewrite rules and a token-based cost model for batching LLM calls.</summary><blockquote>A semantic analytics engine on Apache DataFusion. Extends relational algebra with three semantic operators whose algebraic properties enable query rewriting, and batches tuples under context-window limits using a token-based cost model built on equi-depth token histograms.</blockquote></details>

### Ontology and Knowledge Graph Databases

Storage and query engines for RDF, OWL ontologies, and knowledge graphs, including reasoning and semantic search over them.

- **[OntoDB: A Database Management System for Ontologies](https://github.com/lamng3/OntoDB)**<br>
  <sub>Lam Nguyen · <i>GitHub 2026</i> · <a href="https://lamng3.com/ontodb/">Docs</a></sub>
  <details><summary>An RDF/SPARQL database with B+ tree indexes, ARIES recovery, and ontology-aware semantic search.</summary><blockquote>An RDF and SPARQL database with B+ tree triple indexes, a cost-based optimizer, strict two-phase locking, and ARIES recovery. Supports semantic search through interval labeling of class hierarchies and vector indexes, and answers RDFS subclass entailment without materializing triples.</blockquote></details>

<div align="right"><a href="#awesome-semantic-db">Back to top</a></div>

## Agent Memory

How agents store, consolidate, and retrieve what they learn across sessions, and how to measure whether memory helps.

### Memory Architectures and Systems

Designs and production systems for persistent agent memory.

- **[MemCurrent: Designing Persistent Memory for Production Agents](https://www.databricks.com/blog/memcurrent-designing-persistent-memory-production-agents)**<br>
  <sub>Databricks AI Research · <i>Databricks Blog 2026</i></sub>
  <details><summary>Episodic and derived memory for production agents, kept fresh by an offline consolidation pipeline.</summary><blockquote>Combines episodic memory (raw session traces) with derived memory (a structured knowledge base of distilled learnings), accessed through plugins, agent tools, and an offline consolidation pipeline. Powers Agent Bricks Memory and Genie.</blockquote></details>

<div align="right"><a href="#awesome-semantic-db">Back to top</a></div>
<!-- END LIST -->

## Contributing

This list is curated by its maintainer. Suggestions are welcome as issues. See [CONTRIBUTING.md](CONTRIBUTING.md) for the scope and the entry format.

## License

To the extent possible under law, the maintainer has waived all copyright and related rights to this list under [CC0 1.0](LICENSE).
