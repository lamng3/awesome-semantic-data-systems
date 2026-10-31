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
  - [Ontologies and Semantic Layers for Agents](#sds-semantic-layers)
  - [Knowledge Graph and Ontology Databases](#sds-knowledge-graphs)
  - [Ontology Matching, Versioning, and Evolution](#sds-ontology-evolution)
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
  <details><summary>Semantic operators with algebraic rewrite rules and a token-based cost model for batching LLM&nbsp;calls.</summary><blockquote>A semantic analytics engine on Apache DataFusion. Extends relational algebra with three semantic operators whose algebraic properties enable query rewriting, and batches tuples under context-window limits using a token-based cost model built on equi-depth token&nbsp;histograms.<br><br><i>Authors:</i> Christos Tsapelas, Georgia Koutrika, Yannis&nbsp;Ioannidis<br><br><i>BibTeX:</i> <a href="references.bib"><code>tsapelas2026nousdb</code></a></blockquote></details>

### <a id="sds-semantic-layers"></a>Ontologies and Semantic Layers for Agents

Ontologies and semantic layers that give agents a typed, queryable view of their&nbsp;data.

- **[EvoOntology: A Self-Evolving Ontology Layer for Data Agents](https://arxiv.org/abs/2609.15779)**&nbsp;(Chong&nbsp;et&nbsp;al., arXiv&nbsp;2026)&nbsp;·&nbsp;[Code](https://github.com/ruc-datalab/EvoOntology)
  <details><summary>An ontology layer, served over MCP, that data agents query at runtime and that refines&nbsp;itself.</summary><blockquote>Wraps an ontology of heterogeneous data (tables, files, databases) as an MCP server with schema, content, and tool layers. A builder agent constructs it, and a self-evolution loop applies attribution-guided typed edits, keeping each only if a paired evaluation shows it&nbsp;helps.<br><br><i>Authors:</i> Meiduo Chong, Shaolei Zhang, Ju Fan, Xiaoyong&nbsp;Du<br><br><i>BibTeX:</i> <a href="references.bib"><code>chong2026evoontology</code></a></blockquote></details>
- **[Toward Effective and Reliable LLM Agents via Dynamic Ontology](https://arxiv.org/abs/2608.22974)**&nbsp;(Zhang&nbsp;et&nbsp;al., arXiv&nbsp;2026)
  <details><summary>OaK builds a task-specific ontology with typed reasoning functions and uses it as an agent&#x27;s&nbsp;kernel.</summary><blockquote>OaK (ontology as a kernel) constructs a task-oriented schema and knowledge graph from task data, generates typed functions for retrieval and multi-step graph reasoning, and refines both with judge feedback before freezing the kernel for&nbsp;inference.<br><br><i>Authors:</i> Xiaohui Zhang, Zequn Sun, Chengyuan Yang, Yuanning Cui, Lingbing Guo, Wei&nbsp;Hu<br><br><i>BibTeX:</i> <a href="references.bib"><code>zhang2026effective</code></a></blockquote></details>

### <a id="sds-knowledge-graphs"></a>Knowledge Graph and Ontology Databases

Storage and query engines for RDF, OWL ontologies, and property&nbsp;graphs.

- **[OntoDB: A Database Management System for Ontologies](https://github.com/lamng3/OntoDB)**&nbsp;(Nguyen, GitHub&nbsp;2026)
  <details><summary>An RDF/SPARQL database with B+ tree indexes, ARIES recovery, and ontology-aware semantic&nbsp;search.</summary><blockquote>An RDF and SPARQL database with B+ tree triple indexes, a cost-based optimizer, strict two-phase locking, and ARIES recovery. Supports semantic search through interval labeling of class hierarchies and vector indexes, and answers RDFS subclass entailment without materializing&nbsp;triples.<br><br><i>Authors:</i> Lam&nbsp;Nguyen<br><br><i>BibTeX:</i> <a href="references.bib"><code>nguyen2026ontodb</code></a></blockquote></details>

### <a id="sds-ontology-evolution"></a>Ontology Matching, Versioning, and Evolution

Aligning ontologies, tracking how they change, and checking each change for&nbsp;errors.

- **[OM4OV: Leveraging Ontology Matching for Ontology Versioning](https://doi.org/10.4230/TGDK.4.2.6)**&nbsp;(Qiang&nbsp;et&nbsp;al., TGDK&nbsp;2026)&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2409.20302)
  <details><summary>Separates ontology versioning from matching and reuses matching systems to detect what&nbsp;changed.</summary><blockquote>Analyzes where ontology versioning differs from ontology matching and defines an OM4OV pipeline in the LLM-based Agent-OM system. A cross-reference mechanism reuses earlier alignments to cut candidates and better detect updated&nbsp;entities.<br><br><i>Authors:</i> Zhangcheng Qiang, Kerry Taylor, Weiqing&nbsp;Wang<br><br><i>BibTeX:</i> <a href="references.bib"><code>qiang2026om4ov</code></a></blockquote></details>
- **[KROMA: Ontology Matching with Knowledge Retrieval and Large Language Models](https://doi.org/10.1007/978-3-032-09527-5_34)**&nbsp;(Nguyen&nbsp;et&nbsp;al., ISWC&nbsp;2025)&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2507.14032)&nbsp;·&nbsp;[Code](https://github.com/lamng3/kroma)
  <details><summary>Ontology matching that retrieves each concept&#x27;s context, asks an LLM, and refines as it&nbsp;goes.</summary><blockquote>For each candidate pair, KROMA retrieves local context from the ontologies, their graphs, and external knowledge bases, asks a language model whether the concepts match, and updates equivalence classes online as matches are accepted. Pairs it cannot settle go to an&nbsp;expert.<br><br><i>Authors:</i> Lam Nguyen, Erika Barcelos, Roger French, Yinghui&nbsp;Wu<br><br><i>BibTeX:</i> <a href="references.bib"><code>nguyen2025kroma</code></a></blockquote></details>
- **[OntoLDiff: A Highly Efficient System for Tracking Logical Difference in Large-Scale Ontologies](https://doi.org/10.1145/3746252.3761464)**&nbsp;(Zhao&nbsp;and&nbsp;Schmidt, CIKM&nbsp;2025)
  <details><summary>Shows what a change to an ontology gained or lost logically, via uniform&nbsp;interpolation.</summary><blockquote>The logical difference between two versions is the set of axioms entailed by one but not the other. OntoLDiff computes a finite representation of it for ELH ontologies, so curators can see the semantic effect of each change in industrial-scale&nbsp;ontologies.<br><br><i>Authors:</i> Yizheng Zhao, Renate A.&nbsp;Schmidt<br><br><i>BibTeX:</i> <a href="references.bib"><code>zhao2025ontoldiff</code></a></blockquote></details>

## Agent Memory

How agents store, organize, and recall what they learn, and how to tell whether memory&nbsp;helps.

### <a id="mem-systems"></a>Memory Architectures and Systems

End-to-end memory designs and production systems that agents read from and write&nbsp;to.

- **[MemCurrent: Designing Persistent Memory for Production Agents](https://www.databricks.com/blog/memcurrent-designing-persistent-memory-production-agents)**&nbsp;(Databricks&nbsp;AI&nbsp;Research, Databricks&nbsp;Blog&nbsp;2026)
  <details><summary>Episodic and derived memory for production agents, kept fresh by an offline consolidation&nbsp;pipeline.</summary><blockquote>Combines episodic memory (raw session traces) with derived memory (a structured knowledge base of distilled learnings), accessed through plugins, agent tools, and an offline consolidation pipeline. Powers Agent Bricks Memory and&nbsp;Genie.<br><br><i>BibTeX:</i> <a href="references.bib"><code>databricks2026memcurrent</code></a></blockquote></details>
<!-- END LIST -->

## Citing

BibTeX for every entry is in [references.bib](references.bib).

## Contributing

Suggestions are welcome as issues. Scope and entry format are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released into the public domain under [CC0&nbsp;1.0](LICENSE).
