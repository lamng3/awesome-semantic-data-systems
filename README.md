<!--
  The blocks between BEGIN and END markers are generated from data/*.toml.
  Edit the data files and run `make`; edits inside the markers are overwritten.
-->

<div align="center">

# Awesome Semantic DB

**A curated reading list on semantic data systems and memory for&nbsp;AI&nbsp;agents.**

[![Check](https://github.com/lamng3/awesome-semantic-db/actions/workflows/check.yml/badge.svg)](https://github.com/lamng3/awesome-semantic-db/actions/workflows/check.yml)
[![Links](https://github.com/lamng3/awesome-semantic-db/actions/workflows/links.yml/badge.svg)](https://github.com/lamng3/awesome-semantic-db/actions/workflows/links.yml)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0%201.0-lightgrey.svg)](LICENSE)

</div>

## Contents

<!-- BEGIN CONTENTS -->
- [Semantic Data Systems](#semantic-data-systems)
  - [Semantic Operators and Query Engines](#sds-engines)
  - [Knowledge Graph and Ontology Databases](#sds-knowledge-graphs)
- [Agent Memory](#agent-memory)
  - [Memory Architectures and Systems](#mem-systems)
<!-- END CONTENTS -->

<!-- BEGIN RECENT -->
<!-- END RECENT -->

<!-- BEGIN LIST -->
## Semantic Data Systems

Data systems where meaning is first class, in the query operators or in the data&nbsp;model.

### <a id="sds-engines"></a>Semantic Operators and Query Engines

Semantic operators, their algebra, and the engines that run them inside declarative&nbsp;queries.

- **[NousDB - A Fast Query Engine for Semantic Analytics](https://arxiv.org/abs/2610.28551)**&nbsp;(Tsapelas&nbsp;et&nbsp;al., arXiv&nbsp;2026)
  <details><summary>Semantic operators with algebraic rewrite rules and a token-based cost model for batching LLM&nbsp;calls.</summary><blockquote>A semantic analytics engine on Apache DataFusion. Extends relational algebra with three semantic operators whose algebraic properties enable query rewriting, and batches tuples under context-window limits using a token-based cost model built on equi-depth token&nbsp;histograms.<br><br><i>Authors:</i> Christos Tsapelas, Georgia Koutrika, Yannis&nbsp;Ioannidis</blockquote></details>

### <a id="sds-knowledge-graphs"></a>Knowledge Graph and Ontology Databases

Storage and query engines for RDF, OWL ontologies, and property&nbsp;graphs.

- **[OntoDB: A Database Management System for Ontologies](https://github.com/lamng3/OntoDB)**&nbsp;(Nguyen, GitHub&nbsp;2026)
  <details><summary>An RDF/SPARQL database with B+ tree indexes, ARIES recovery, and ontology-aware semantic&nbsp;search.</summary><blockquote>An RDF and SPARQL database with B+ tree triple indexes, a cost-based optimizer, strict two-phase locking, and ARIES recovery. Supports semantic search through interval labeling of class hierarchies and vector indexes, and answers RDFS subclass entailment without materializing&nbsp;triples.<br><br><i>Authors:</i> Lam&nbsp;Nguyen</blockquote></details>

## Agent Memory

How agents store, organize, and recall what they learn, and how to tell whether memory&nbsp;helps.

### <a id="mem-systems"></a>Memory Architectures and Systems

End-to-end memory designs and production systems that agents read from and write&nbsp;to.

- **[MemCurrent: Designing Persistent Memory for Production Agents](https://www.databricks.com/blog/memcurrent-designing-persistent-memory-production-agents)**&nbsp;(Databricks&nbsp;AI&nbsp;Research, Databricks&nbsp;Blog&nbsp;2026)
  <details><summary>Episodic and derived memory for production agents, kept fresh by an offline consolidation&nbsp;pipeline.</summary><blockquote>Combines episodic memory (raw session traces) with derived memory (a structured knowledge base of distilled learnings), accessed through plugins, agent tools, and an offline consolidation pipeline. Powers Agent Bricks Memory and&nbsp;Genie.</blockquote></details>
<!-- END LIST -->

## Contributing

Suggestions are welcome as issues. Scope and entry format are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released into the public domain under [CC0&nbsp;1.0](LICENSE).
