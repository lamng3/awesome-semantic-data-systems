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
<table>
<tr>
<th width="50%"><a href="#semantic-data-systems">Semantic Data Systems</a> (2)</th>
<th width="50%"><a href="#agent-memory">Agent Memory</a> (1)</th>
</tr>
<tr>
<td valign="top"><a href="#sds-engines">Semantic Operators and Query Engines</a> (1)<br><a href="#sds-knowledge-graphs">Knowledge Graph and Ontology Databases</a> (1)</td>
<td valign="top"><a href="#mem-systems">Memory Architectures and Systems</a> (1)</td>
</tr>
</table>
<!-- END CONTENTS -->

<!-- BEGIN RECENT -->
<!-- END RECENT -->

<!-- BEGIN LIST -->
## Semantic Data Systems

Data systems where meaning is first class: models run as query operators, or the data model itself encodes semantics.

### <a id="sds-engines"></a>Semantic Operators and Query Engines

Semantic operators, their algebra, and the engines that run them inside declarative queries over structured and unstructured data.

- **[NousDB - A Fast Query Engine for Semantic Analytics](https://arxiv.org/abs/2610.28551)** (Tsapelas et al., arXiv 2026)
  <details><summary>Semantic operators with algebraic rewrite rules and a token-based cost model for batching LLM calls.</summary><blockquote>A semantic analytics engine on Apache DataFusion. Extends relational algebra with three semantic operators whose algebraic properties enable query rewriting, and batches tuples under context-window limits using a token-based cost model built on equi-depth token histograms.<br><br><i>Authors:</i> Christos Tsapelas, Georgia Koutrika, Yannis Ioannidis</blockquote></details>

### <a id="sds-knowledge-graphs"></a>Knowledge Graph and Ontology Databases

Storage and query engines for RDF, OWL ontologies, and property graphs, including reasoning and semantic search over them.

- **[OntoDB: A Database Management System for Ontologies](https://github.com/lamng3/OntoDB)** (Nguyen, GitHub 2026) · [Docs](https://lamng3.com/ontodb/)
  <details><summary>An RDF/SPARQL database with B+ tree indexes, ARIES recovery, and ontology-aware semantic search.</summary><blockquote>An RDF and SPARQL database with B+ tree triple indexes, a cost-based optimizer, strict two-phase locking, and ARIES recovery. Supports semantic search through interval labeling of class hierarchies and vector indexes, and answers RDFS subclass entailment without materializing triples.<br><br><i>Authors:</i> Lam Nguyen</blockquote></details>

<div align="right"><a href="#awesome-semantic-db">Back to top</a></div>

## Agent Memory

How agents store, organize, and recall what they learn across sessions, and how to tell whether memory helps.

### <a id="mem-systems"></a>Memory Architectures and Systems

End-to-end memory designs and production systems that agents read from and write to.

- **[MemCurrent: Designing Persistent Memory for Production Agents](https://www.databricks.com/blog/memcurrent-designing-persistent-memory-production-agents)** (Databricks AI Research, Databricks Blog 2026)
  <details><summary>Episodic and derived memory for production agents, kept fresh by an offline consolidation pipeline.</summary><blockquote>Combines episodic memory (raw session traces) with derived memory (a structured knowledge base of distilled learnings), accessed through plugins, agent tools, and an offline consolidation pipeline. Powers Agent Bricks Memory and Genie.</blockquote></details>

<div align="right"><a href="#awesome-semantic-db">Back to top</a></div>
<!-- END LIST -->

## Contributing

This list is curated by its maintainer. Suggestions are welcome as issues. See [CONTRIBUTING.md](CONTRIBUTING.md) for the scope and the entry format.

## License

To the extent possible under law, the maintainer has waived all copyright and related rights to this list under [CC0 1.0](LICENSE).
