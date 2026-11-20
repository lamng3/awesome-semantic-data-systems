<!--
  The blocks between BEGIN and END markers are generated from data/.
  Edit data/ and run `make`; edits inside the markers are overwritten.
-->

<div align="center">

# Awesome Semantic Data Systems

**A curated reading list on semantic query processing, vector search, knowledge graphs and ontologies, agent memory, and attacks on these&nbsp;systems.**

[![Check](https://github.com/lamng3/awesome-semantic-data-systems/actions/workflows/check.yml/badge.svg)](https://github.com/lamng3/awesome-semantic-data-systems/actions/workflows/check.yml)
[![Links](https://github.com/lamng3/awesome-semantic-data-systems/actions/workflows/links.yml/badge.svg)](https://github.com/lamng3/awesome-semantic-data-systems/actions/workflows/links.yml)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0%201.0-lightgrey.svg)](LICENSE)

</div>

## Contents

<!-- BEGIN CONTENTS -->
- [Semantic Query Processing](#semantic-query-processing)
- [Vector Search](#vector-search)
  - [Graph-Based Indexes](#vector-graph)
  - [Quantization and Partitioning](#vector-quantization)
  - [Hardware-Aware Search](#vector-hardware)
  - [Vector Databases and Filtered Search](#vector-systems)
- [Knowledge Graphs and Ontologies](#knowledge-graphs-and-ontologies)
- [Agent Memory](#agent-memory)
  - [Memory Systems](#memory-systems)
  - [Sleep and Dreaming](#memory-sleep)
- [Attacks and Robustness](#attacks-and-robustness)
  - [RAG and Retrieval Poisoning](#attacks-rag)
  - [Knowledge Graph and Graph Attacks](#attacks-graph)
  - [Data Quality and Perturbation](#attacks-quality)
  - [Search and Graph Algorithms](#attacks-algorithms)
<!-- END CONTENTS -->

<!-- BEGIN LIST -->
## Semantic Query Processing

Engines that run models as query operators, and the techniques that make such queries&nbsp;efficient.

- **arXiv&nbsp;2026** · [NousDB - A Fast Query Engine for Semantic Analytics](https://arxiv.org/abs/2610.28551)&nbsp;·&nbsp;Tsapelas&nbsp;et&nbsp;al.

## Vector Search

Approximate nearest neighbor search, from index design down to the hardware it runs&nbsp;on.

### <a id="vector-graph"></a>Graph-Based Indexes

Proximity graphs: construction, routing, disk-resident and streaming indexes, and&nbsp;theory.

- **KDD&nbsp;2026** · [PiPNN: Ultra-Scalable Graph-Based Nearest Neighbor Indexing](https://doi.org/10.1145/3770855.3817891)&nbsp;·&nbsp;Rubel&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2602.21247)
- **PODS&nbsp;2025** · [Proximity Graphs for Similarity Search: Fast Construction, Lower Bounds, and Euclidean Separation](https://doi.org/10.1145/3767716)&nbsp;·&nbsp;Lu&nbsp;and&nbsp;Tao&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2509.07732)
- **NeurIPS&nbsp;2023** · [Worst-case Performance of Popular Approximate Nearest Neighbor Search Implementations: Guarantees and Limitations](https://papers.nips.cc/paper_files/paper/2023/hash/d0ac28b79816b51124fcc804b2496a36-Abstract-Conference.html)&nbsp;·&nbsp;Indyk&nbsp;and&nbsp;Xu&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2310.19126)
- **TPAMI&nbsp;2020** · [Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs](https://doi.org/10.1109/tpami.2018.2889473)&nbsp;·&nbsp;Malkov&nbsp;and&nbsp;Yashunin&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1603.09320)
- **NeurIPS&nbsp;2019** · [DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node](https://papers.nips.cc/paper_files/paper/2019/hash/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Abstract.html)&nbsp;·&nbsp;Subramanya&nbsp;et&nbsp;al.
- **VLDB&nbsp;2019** · [Fast Approximate Nearest Neighbor Search With The Navigating Spreading-out Graph](https://doi.org/10.14778/3303753.3303754)&nbsp;·&nbsp;Fu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1707.00143)

### <a id="vector-quantization"></a>Quantization and Partitioning

Compressed codes, inverted files, and learned&nbsp;partitions.

- **SIGMOD&nbsp;2024** · [RaBitQ: Quantizing High-Dimensional Vectors with a Theoretical Error Bound for Approximate Nearest Neighbor Search](https://doi.org/10.1145/3654970)&nbsp;·&nbsp;Gao&nbsp;and&nbsp;Long&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2405.12497)
- **NeurIPS&nbsp;2023** · [SOAR: Improved Indexing for Approximate Nearest Neighbor Search](https://papers.nips.cc/paper_files/paper/2023/hash/0973524e02a712af33325d0688ae6f49-Abstract-Conference.html)&nbsp;·&nbsp;Sun&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2404.00774)
- **ICML&nbsp;2020** · [Accelerating Large-Scale Inference with Anisotropic Vector Quantization](https://proceedings.mlr.press/v119/guo20h.html)&nbsp;·&nbsp;Guo&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1908.10396)
- **TPAMI&nbsp;2011** · [Product Quantization for Nearest Neighbor Search](https://doi.org/10.1109/tpami.2010.57)&nbsp;·&nbsp;Jégou&nbsp;et&nbsp;al.

### <a id="vector-hardware"></a>Hardware-Aware Search

GPUs, CPU caches and SIMD, and kernel&nbsp;fusion.

- **VLDB&nbsp;2026** · [GPU-Native Approximate Nearest Neighbor Search with IVF-RaBitQ: Fast Index Build and Search](https://doi.org/10.14778/3836663.3836701)&nbsp;·&nbsp;Shi&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2602.23999)
- **SIGIR&nbsp;2026** · [SilverTorch: A Unified Model-based System to Democratize Large-Scale Recommendation on GPUs](https://doi.org/10.1145/3805712.3809755)&nbsp;·&nbsp;Xue&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2511.14881)
- **ICDE&nbsp;2024** · [CAGRA: Highly Parallel Graph Construction and Approximate Nearest Neighbor Search for GPUs](https://doi.org/10.1109/icde60146.2024.00323)&nbsp;·&nbsp;Ootomo&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2308.15136)
- **IEEE&nbsp;TBD&nbsp;2021** · [Billion-Scale Similarity Search with GPUs](https://doi.org/10.1109/tbdata.2019.2921572)&nbsp;·&nbsp;Johnson&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1702.08734)
- **VLDB&nbsp;2015** · [Cache Locality is not Enough: High-Performance Nearest Neighbor Search with Product Quantization Fast Scan](https://doi.org/10.14778/2856318.2856324)&nbsp;·&nbsp;André&nbsp;et&nbsp;al.
- **MICRO&nbsp;2012** · [Kernel Weaver: Automatically Fusing Database Primitives for Efficient GPU Computation](https://doi.org/10.1109/micro.2012.19)&nbsp;·&nbsp;Wu&nbsp;et&nbsp;al.

### <a id="vector-systems"></a>Vector Databases and Filtered Search

Vector data management systems, queries with structured predicates, and&nbsp;benchmarks.

- **SIGMOD&nbsp;2024** · [ACORN: Performant and Predicate-Agnostic Search Over Vector Embeddings and Structured Data](https://doi.org/10.1145/3654923)&nbsp;·&nbsp;Patel&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2403.04871)
- **WWW&nbsp;2023** · [Filtered-DiskANN: Graph Algorithms for Approximate Nearest Neighbor Search with Filters](https://doi.org/10.1145/3543507.3583552)&nbsp;·&nbsp;Gollapudi&nbsp;et&nbsp;al.
- **SIGMOD&nbsp;2021** · [Milvus: A Purpose-Built Vector Data Management System](https://doi.org/10.1145/3448016.3457550)&nbsp;·&nbsp;Wang&nbsp;et&nbsp;al.

## Knowledge Graphs and Ontologies

Storing, querying, aligning, versioning, and evolving ontologies and knowledge&nbsp;graphs.

- **arXiv&nbsp;2026** · [EvoOntology: A Self-Evolving Ontology Layer for Data Agents](https://arxiv.org/abs/2609.15779)&nbsp;·&nbsp;Chong&nbsp;et&nbsp;al.&nbsp;·&nbsp;[Code](https://github.com/ruc-datalab/EvoOntology)
- **TGDK&nbsp;2026** · [OM4OV: Leveraging Ontology Matching for Ontology Versioning](https://doi.org/10.4230/TGDK.4.2.6)&nbsp;·&nbsp;Qiang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2409.20302)
- **GitHub&nbsp;2026** · [OntoDB: A Database Management System for Ontologies](https://github.com/lamng3/OntoDB)&nbsp;·&nbsp;Nguyen
- **arXiv&nbsp;2026** · [Toward Effective and Reliable LLM Agents via Dynamic Ontology](https://arxiv.org/abs/2608.22974)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.
- **ISWC&nbsp;2025** · [KROMA: Ontology Matching with Knowledge Retrieval and Large Language Models](https://doi.org/10.1007/978-3-032-09527-5_34)&nbsp;·&nbsp;Nguyen&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2507.14032)&nbsp;·&nbsp;[Code](https://github.com/lamng3/kroma)
- **CIKM&nbsp;2025** · [OntoLDiff: A Highly Efficient System for Tracking Logical Difference in Large-Scale Ontologies](https://doi.org/10.1145/3746252.3761464)&nbsp;·&nbsp;Zhao&nbsp;and&nbsp;Schmidt

## Agent Memory

How agents store, organize, and recall what they learn, and how to tell whether memory&nbsp;helps.

### <a id="memory-systems"></a>Memory Systems

Memory architectures for agents and benchmarks for long-term&nbsp;memory.

- **Databricks&nbsp;Blog&nbsp;2026** · [MemCurrent: Designing Persistent Memory for Production Agents](https://www.databricks.com/blog/memcurrent-designing-persistent-memory-production-agents)&nbsp;·&nbsp;Databricks&nbsp;AI&nbsp;Research
- **NeurIPS&nbsp;2025** · [A-Mem: Agentic Memory for LLM Agents](https://doi.org/10.52202/085713-0593)&nbsp;·&nbsp;Xu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2502.12110)
- **ICLR&nbsp;2025** · [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://openreview.net/forum?id=pZiyCaVuti)&nbsp;·&nbsp;Wu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2410.10813)
- **arXiv&nbsp;2025** · [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956)&nbsp;·&nbsp;Rasmussen&nbsp;et&nbsp;al.
- **UIST&nbsp;2023** · [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763)&nbsp;·&nbsp;Park&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2304.03442)
- **arXiv&nbsp;2023** · [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)&nbsp;·&nbsp;Packer&nbsp;et&nbsp;al.

### <a id="memory-sleep"></a>Sleep and Dreaming

Offline consolidation: replaying, distilling, and rewriting memories between&nbsp;sessions.

- **NeurIPS&nbsp;2026** · [Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents](https://openreview.net/forum?id=SR1n2zkaBO)&nbsp;·&nbsp;Ye&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2605.20616)
- **arXiv&nbsp;2026** · [Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories](https://arxiv.org/abs/2606.03979)&nbsp;·&nbsp;Behrouz&nbsp;et&nbsp;al.
- **arXiv&nbsp;2025** · [Sleep-time Compute: Beyond Inference Scaling at Test-time](https://arxiv.org/abs/2504.13171)&nbsp;·&nbsp;Lin&nbsp;et&nbsp;al.
- **PLDI&nbsp;2021** · [DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning](https://doi.org/10.1145/3453483.3454080)&nbsp;·&nbsp;Ellis&nbsp;et&nbsp;al.
- **Science&nbsp;1995** · [The “Wake-Sleep” Algorithm for Unsupervised Neural Networks](https://doi.org/10.1126/science.7761831)&nbsp;·&nbsp;Hinton&nbsp;et&nbsp;al.

## Attacks and Robustness

Poisoning and adversarial attacks on semantic data systems, and the algorithms behind&nbsp;them.

### <a id="attacks-rag"></a>RAG and Retrieval Poisoning

Corrupting the corpus, retriever, or ranker that a retrieval-augmented model depends&nbsp;on.

- **IEEE&nbsp;S&P&nbsp;2026** · [GraphRAG under Fire](https://doi.org/10.1109/sp63933.2026.00070)&nbsp;·&nbsp;Liang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2501.14050)
- **USENIX&nbsp;Security&nbsp;2025** · [Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents](https://www.usenix.org/conference/usenixsecurity25/presentation/shafran)&nbsp;·&nbsp;Shafran&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2406.05870)
- **USENIX&nbsp;Security&nbsp;2025** · [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag)&nbsp;·&nbsp;Zou&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2402.07867)
- **NeurIPS&nbsp;2024** · [AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://papers.nips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html)&nbsp;·&nbsp;Chen&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2407.12784)
- **EMNLP&nbsp;2023** · [Poisoning Retrieval Corpora by Injecting Adversarial Passages](https://doi.org/10.18653/v1/2023.emnlp-main.849)&nbsp;·&nbsp;Zhong&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2310.19156)

### <a id="attacks-graph"></a>Knowledge Graph and Graph Attacks

Perturbing triples and edges to mislead embeddings, alignment, and graph neural&nbsp;networks.

- **EMNLP&nbsp;2021** · [Adversarial Attack against Cross-lingual Knowledge Graph Alignment](https://doi.org/10.18653/v1/2021.emnlp-main.432)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.
- **ACL&nbsp;2021** · [Poisoning Knowledge Graph Embeddings via Relation Inference Patterns](https://doi.org/10.18653/v1/2021.acl-long.147)&nbsp;·&nbsp;Bhardwaj&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2111.06345)
- **ICLR&nbsp;2019** · [Adversarial Attacks on Graph Neural Networks via Meta Learning](https://openreview.net/forum?id=Bylnx209YX)&nbsp;·&nbsp;Zügner&nbsp;and&nbsp;Günnemann&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1902.08412)
- **IJCAI&nbsp;2019** · [Data Poisoning Attack against Knowledge Graph Embedding](https://doi.org/10.24963/ijcai.2019/674)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1904.12052)
- **NAACL&nbsp;2019** · [Investigating Robustness and Interpretability of Link Prediction via Adversarial Modifications](https://doi.org/10.18653/v1/n19-1337)&nbsp;·&nbsp;Pezeshkpour&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1905.00563)
- **KDD&nbsp;2018** · [Adversarial Attacks on Neural Networks for Graph Data](https://doi.org/10.1145/3219819.3220078)&nbsp;·&nbsp;Zügner&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1805.07984)

### <a id="attacks-quality"></a>Data Quality and Perturbation

Noisy, perturbed, or low-quality data and metadata, and how well systems hold&nbsp;up.

- **arXiv&nbsp;2026** · [An Agentic Approach to Metadata Reasoning](https://arxiv.org/abs/2604.20144)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.
- **ICLR&nbsp;2023** · [Dr.Spider: A Diagnostic Evaluation Benchmark towards Text-to-SQL Robustness](https://openreview.net/forum?id=Wc5bmZZU9cy)&nbsp;·&nbsp;Chang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2301.08881)
- **ICML&nbsp;2023** · [Large Language Models Can Be Easily Distracted by Irrelevant Context](https://proceedings.mlr.press/v202/shi23a.html)&nbsp;·&nbsp;Shi&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2302.00093)
- **ACL&nbsp;2022** · [Towards Robustness of Text-to-SQL Models Against Natural and Realistic Adversarial Table Perturbation](https://doi.org/10.18653/v1/2022.acl-long.142)&nbsp;·&nbsp;Pi&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2212.09994)
- **SIGMOD&nbsp;2019** · [Raha: A Configuration-Free Error Detection System](https://doi.org/10.1145/3299869.3324956)&nbsp;·&nbsp;Mahdavi&nbsp;et&nbsp;al.
- **VLDB&nbsp;2017** · [HoloClean: Holistic Data Repairs with Probabilistic Inference](https://doi.org/10.14778/3137628.3137631)&nbsp;·&nbsp;Rekatsinas&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1702.00820)

### <a id="attacks-algorithms"></a>Search and Graph Algorithms

Beam search, Monte Carlo tree search and UCT, network flows, and dynamic&nbsp;trees.

- **ICML&nbsp;2024** · [Fast Adversarial Attacks on Language Models In One GPU Minute](https://proceedings.mlr.press/v235/sadasivan24a.html)&nbsp;·&nbsp;Sadasivan&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2402.15570)
- **NeurIPS&nbsp;2024** · [Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](https://papers.nips.cc/paper_files/paper/2024/hash/70702e8cbb4890b4a467b984ae59828a-Abstract-Conference.html)&nbsp;·&nbsp;Mehrotra&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2312.02119)
- **arXiv&nbsp;2023** · [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043)&nbsp;·&nbsp;Zou&nbsp;et&nbsp;al.
- **FOCS&nbsp;2022** · [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://doi.org/10.1109/focs54457.2022.00064)&nbsp;·&nbsp;Chen&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2203.00671)
- **EMNLP&nbsp;2020** · [If Beam Search Is the Answer, What Was the Question?](https://doi.org/10.18653/v1/2020.emnlp-main.170)&nbsp;·&nbsp;Meister&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2010.02650)
- **ALENEX&nbsp;2019** · [Batch-Parallel Euler Tour Trees](https://doi.org/10.1137/1.9781611975499.8)&nbsp;·&nbsp;Tseng&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1810.10738)
- **ACL&nbsp;2018** · [HotFlip: White-Box Adversarial Examples for Text Classification](https://doi.org/10.18653/v1/p18-2006)&nbsp;·&nbsp;Ebrahimi&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1712.06751)
- **IEEE&nbsp;TCIAIG&nbsp;2012** · [A Survey of Monte Carlo Tree Search Methods](https://doi.org/10.1109/tciaig.2012.2186810)&nbsp;·&nbsp;Browne&nbsp;et&nbsp;al.
- **ECML&nbsp;2006** · [Bandit Based Monte-Carlo Planning](https://doi.org/10.1007/11871842_29)&nbsp;·&nbsp;Kocsis&nbsp;and&nbsp;Szepesvári
- **Machine&nbsp;Learning&nbsp;2002** · [Finite-time Analysis of the Multiarmed Bandit Problem](https://doi.org/10.1023/a:1013689704352)&nbsp;·&nbsp;Auer&nbsp;et&nbsp;al.
- **JACM&nbsp;2001** · [Poly-Logarithmic Deterministic Fully-Dynamic Algorithms for Connectivity, Minimum Spanning Tree, 2-Edge, and Biconnectivity](https://doi.org/10.1145/502090.502095)&nbsp;·&nbsp;Holm&nbsp;et&nbsp;al.
- **JACM&nbsp;1999** · [Randomized Fully Dynamic Graph Algorithms with Polylogarithmic Time per Operation](https://doi.org/10.1145/320211.320215)&nbsp;·&nbsp;Henzinger&nbsp;and&nbsp;King
- **JACM&nbsp;1988** · [A New Approach to the Maximum-Flow Problem](https://doi.org/10.1145/48014.61051)&nbsp;·&nbsp;Goldberg&nbsp;and&nbsp;Tarjan
- **JCSS&nbsp;1983** · [A Data Structure for Dynamic Trees](https://doi.org/10.1016/0022-0000%2883%2990006-5)&nbsp;·&nbsp;Sleator&nbsp;and&nbsp;Tarjan
<!-- END LIST -->

## Long List

This list is kept short on purpose: top venues and strong industry papers, algorithms first. Other papers we track are in the [long list](LONGLIST.md), under the same&nbsp;sections.

## Citing

BibTeX for every paper here and in the long list is in [references.bib](references.bib), grouped by&nbsp;section.

## Contributing

Suggestions are welcome as issues. Scope and entry format are in&nbsp;[CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released into the public domain under [CC0&nbsp;1.0](LICENSE).
