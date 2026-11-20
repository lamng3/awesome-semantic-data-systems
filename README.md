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

- **ECIR&nbsp;2026** · [Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”](https://doi.org/10.1007/978-3-032-21324-2_3)&nbsp;·&nbsp;Munyampirwa&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2412.01940)
- **KDD&nbsp;2026** · [PiPNN: Ultra-Scalable Graph-Based Nearest Neighbor Indexing](https://doi.org/10.1145/3770855.3817891)&nbsp;·&nbsp;Rubel&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2602.21247)
- **SIGMOD&nbsp;2026** · [Through the Lens of Hubness: A Revisit on Graph-Based Approximate Nearest Neighbor Search](https://doi.org/10.1145/3802120)&nbsp;·&nbsp;Xu&nbsp;et&nbsp;al.
- **SIGMOD&nbsp;2025** · [Graph-Based Vector Search: An Experimental Evaluation of the State-of-the-Art](https://doi.org/10.1145/3709693)&nbsp;·&nbsp;Azizi&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2502.05575)
- **PODS&nbsp;2025** · [Proximity Graphs for Similarity Search: Fast Construction, Lower Bounds, and Euclidean Separation](https://doi.org/10.1145/3767716)&nbsp;·&nbsp;Lu&nbsp;and&nbsp;Tao&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2509.07732)
- **VLDB&nbsp;2025** · [Revisiting the Index Construction of Proximity Graph-Based Approximate Nearest Neighbor Search](https://doi.org/10.14778/3725688.3725709)&nbsp;·&nbsp;Yang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2410.01231)
- **NeurIPS&nbsp;2024** · [Navigable Graphs for High-Dimensional Nearest Neighbor Search: Constructions and Limits](https://papers.nips.cc/paper_files/paper/2024/hash/6dc63b4063c978cf195bc15178e8152a-Abstract-Conference.html)&nbsp;·&nbsp;Diwan&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2405.18680)
- **PPoPP&nbsp;2024** · [ParlayANN: Scalable and Deterministic Parallel Graph-Based Approximate Nearest Neighbor Search Algorithms](https://doi.org/10.1145/3627535.3638475)&nbsp;·&nbsp;Manohar&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2305.04359)
- **ICML&nbsp;2024** · [Probabilistic Routing for Graph-Based Approximate Nearest Neighbor Search](https://proceedings.mlr.press/v235/lu24l.html)&nbsp;·&nbsp;Lu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2402.11354)
- **VLDB&nbsp;2024** · [RoarGraph: A Projected Bipartite Graph for Efficient Cross-Modal Approximate Nearest Neighbor Search](https://doi.org/10.14778/3681954.3681959)&nbsp;·&nbsp;Chen&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2408.08933)
- **SIGMOD&nbsp;2024** · [Starling: An I/O-Efficient Disk-Resident Graph Index Framework for High-Dimensional Vector Similarity Search on Data Segment](https://doi.org/10.1145/3639269)&nbsp;·&nbsp;Wang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2401.02116)
- **VLDB&nbsp;2024** · [Steiner-Hardness: A Query Hardness Measure for Graph-Based ANN Indexes](https://doi.org/10.14778/3704965.3704974)&nbsp;·&nbsp;Wang&nbsp;et&nbsp;al.
- **VLDB&nbsp;2023** · [ELPIS: Graph-Based Similarity Search for Scalable Data Science](https://doi.org/10.14778/3583140.3583166)&nbsp;·&nbsp;Azizi&nbsp;et&nbsp;al.
- **NeurIPS&nbsp;2023** · [Worst-case Performance of Popular Approximate Nearest Neighbor Search Implementations: Guarantees and Limitations](https://papers.nips.cc/paper_files/paper/2023/hash/d0ac28b79816b51124fcc804b2496a36-Abstract-Conference.html)&nbsp;·&nbsp;Indyk&nbsp;and&nbsp;Xu&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2310.19126)
- **VLDB&nbsp;2021** · [A Comprehensive Survey and Experimental Comparison of Graph-Based Approximate Nearest Neighbor Search](https://doi.org/10.14778/3476249.3476255)&nbsp;·&nbsp;Wang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2101.12631)
- **arXiv&nbsp;2021** · [FreshDiskANN: A Fast and Accurate Graph-Based ANN Index for Streaming Similarity Search](https://arxiv.org/abs/2105.09613)&nbsp;·&nbsp;Singh&nbsp;et&nbsp;al.
- **TPAMI&nbsp;2020** · [Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs](https://doi.org/10.1109/tpami.2018.2889473)&nbsp;·&nbsp;Malkov&nbsp;and&nbsp;Yashunin&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1603.09320)
- **ICML&nbsp;2020** · [Graph-based Nearest Neighbor Search: From Practice to Theory](https://proceedings.mlr.press/v119/prokhorenkova20a.html)&nbsp;·&nbsp;Prokhorenkova&nbsp;and&nbsp;Shekhovtsov&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1907.00845)
- **NeurIPS&nbsp;2019** · [DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node](https://papers.nips.cc/paper_files/paper/2019/hash/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Abstract.html)&nbsp;·&nbsp;Subramanya&nbsp;et&nbsp;al.
- **VLDB&nbsp;2019** · [Fast Approximate Nearest Neighbor Search With The Navigating Spreading-out Graph](https://doi.org/10.14778/3303753.3303754)&nbsp;·&nbsp;Fu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1707.00143)
- **WWW&nbsp;2011** · [Efficient K-Nearest Neighbor Graph Construction for Generic Similarity Measures](https://doi.org/10.1145/1963405.1963487)&nbsp;·&nbsp;Dong&nbsp;et&nbsp;al.

### <a id="vector-quantization"></a>Quantization and Partitioning

Compressed codes, inverted files, and learned&nbsp;partitions.

- **VLDB&nbsp;2026** · [Quantization Meets Projection: A Happy Marriage for Approximate k-Nearest Neighbor Search](https://doi.org/10.14778/3797919.3797931)&nbsp;·&nbsp;Yang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2411.06158)
- **SIGMOD&nbsp;2025** · [Practical and Asymptotically Optimal Quantization of High-Dimensional Vectors in Euclidean Space for Approximate Nearest Neighbor Search](https://doi.org/10.1145/3725413)&nbsp;·&nbsp;Gao&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2409.09913)
- **SIGMOD&nbsp;2025** · [SymphonyQG: Towards Symphonious Integration of Quantization and Graph for Approximate Nearest Neighbor Search](https://doi.org/10.1145/3709730)&nbsp;·&nbsp;Gou&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2411.12229)
- **SIGMOD&nbsp;2024** · [RaBitQ: Quantizing High-Dimensional Vectors with a Theoretical Error Bound for Approximate Nearest Neighbor Search](https://doi.org/10.1145/3654970)&nbsp;·&nbsp;Gao&nbsp;and&nbsp;Long&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2405.12497)
- **SIGMOD&nbsp;2023** · [High-Dimensional Approximate Nearest Neighbor Search: with Reliable and Efficient Distance Comparison Operations](https://doi.org/10.1145/3589282)&nbsp;·&nbsp;Gao&nbsp;and&nbsp;Long&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2303.09855)
- **VLDB&nbsp;2023** · [Similarity Search in the Blink of an Eye with Compressed Indices](https://doi.org/10.14778/3611479.3611537)&nbsp;·&nbsp;Aguerrebere&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2304.04759)
- **NeurIPS&nbsp;2023** · [SOAR: Improved Indexing for Approximate Nearest Neighbor Search](https://papers.nips.cc/paper_files/paper/2023/hash/0973524e02a712af33325d0688ae6f49-Abstract-Conference.html)&nbsp;·&nbsp;Sun&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2404.00774)
- **SOSP&nbsp;2023** · [SPFresh: Incremental In-Place Update for Billion-Scale Vector Search](https://doi.org/10.1145/3600006.3613166)&nbsp;·&nbsp;Xu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2410.14452)
- **NeurIPS&nbsp;2021** · [SPANN: Highly-efficient Billion-scale Approximate Nearest Neighbor Search](https://papers.nips.cc/paper_files/paper/2021/hash/299dc35e747eb77177d9cea10a802da2-Abstract.html)&nbsp;·&nbsp;Chen&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2111.08566)
- **ICML&nbsp;2020** · [Accelerating Large-Scale Inference with Anisotropic Vector Quantization](https://proceedings.mlr.press/v119/guo20h.html)&nbsp;·&nbsp;Guo&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1908.10396)
- **ICLR&nbsp;2020** · [Learning Space Partitions for Nearest Neighbor Search](https://openreview.net/forum?id=rkenmREFDr)&nbsp;·&nbsp;Dong&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1901.08544)
- **TPAMI&nbsp;2011** · [Product Quantization for Nearest Neighbor Search](https://doi.org/10.1109/tpami.2010.57)&nbsp;·&nbsp;Jégou&nbsp;et&nbsp;al.

### <a id="vector-hardware"></a>Hardware-Aware Search

GPUs, CPU caches and SIMD, and kernel&nbsp;fusion.

- **ICDE&nbsp;2026** · [GLIDE: GPU-Accelerated ANN Graph Index Construction via Data Locality](https://doi.org/10.1109/icde65706.2026.00250)&nbsp;·&nbsp;Ruan&nbsp;et&nbsp;al.
- **VLDB&nbsp;2026** · [GPU-Native Approximate Nearest Neighbor Search with IVF-RaBitQ: Fast Index Build and Search](https://doi.org/10.14778/3836663.3836701)&nbsp;·&nbsp;Shi&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2602.23999)
- **KDD&nbsp;2026** · [Hitcher: Efficient GPU-based Vector Search via Cluster-Centric Kernel and Hitch-Ride Ordering](https://doi.org/10.1145/3770854.3780212)&nbsp;·&nbsp;Zhou&nbsp;et&nbsp;al.
- **SIGIR&nbsp;2026** · [SilverTorch: A Unified Model-based System to Democratize Large-Scale Recommendation on GPUs](https://doi.org/10.1145/3805712.3809755)&nbsp;·&nbsp;Xue&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2511.14881)
- **SIGMOD&nbsp;2025** · [Accelerating Graph Indexing for ANNS on Modern CPUs](https://doi.org/10.1145/3725260)&nbsp;·&nbsp;Wang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2502.18113)
- **IEEE&nbsp;TBD&nbsp;2025** · [BANG: Billion-Scale Approximate Nearest Neighbour Search Using a Single GPU](https://doi.org/10.1109/tbdata.2025.3581085)&nbsp;·&nbsp;Venkatasubba&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2401.11324)
- **SIGMOD&nbsp;2025** · [Scalable Graph Indexing using GPUs for Approximate Nearest Neighbor Search](https://doi.org/10.1145/3769825)&nbsp;·&nbsp;Li&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2508.08744)
- **FAST&nbsp;2025** · [Towards High-throughput and Low-latency Billion-scale Vector Search via CPU/GPU Collaborative Filtering and Re-ranking](https://www.usenix.org/conference/fast25/presentation/tian-bing)&nbsp;·&nbsp;Tian&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2409.16576)
- **VLDB&nbsp;2025** · [VSAG: An Optimized Search Framework for Graph-based Approximate Nearest Neighbor Search](https://doi.org/10.14778/3750601.3750624)&nbsp;·&nbsp;Zhong&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2503.17911)
- **ICDE&nbsp;2024** · [CAGRA: Highly Parallel Graph Construction and Approximate Nearest Neighbor Search for GPUs](https://doi.org/10.1109/icde60146.2024.00323)&nbsp;·&nbsp;Ootomo&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2308.15136)
- **ASPLOS&nbsp;2024** · [Juno: Optimizing High-Dimensional Approximate Nearest Neighbour Search with Sparsity-Aware Algorithm and Ray-Tracing Core Mapping](https://doi.org/10.1145/3620665.3640360)&nbsp;·&nbsp;Liu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2312.01712)
- **IEEE&nbsp;TBD&nbsp;2023** · [GGNN: Graph-Based GPU Nearest Neighbor Search](https://doi.org/10.1109/tbdata.2022.3161156)&nbsp;·&nbsp;Groh&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1912.01059)
- **PPoPP&nbsp;2023** · [iQAN: Fast and Accurate Vector Search with Efficient Intra-Query Parallelism on Multi-Core Architectures](https://doi.org/10.1145/3572848.3577527)&nbsp;·&nbsp;Peng&nbsp;et&nbsp;al.
- **SC&nbsp;2023** · [Parallel Top-K Algorithms on GPU: A Comprehensive Study and New Methods](https://doi.org/10.1145/3581784.3607062)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.
- **NeurIPS&nbsp;2022** · [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://papers.nips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html)&nbsp;·&nbsp;Dao&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2205.14135)
- **ICDE&nbsp;2022** · [GPU-accelerated Proximity Graph Approximate Nearest Neighbor Search and Construction](https://doi.org/10.1109/icde53745.2022.00046)&nbsp;·&nbsp;Yu&nbsp;et&nbsp;al.
- **NeurIPS&nbsp;2022** · [Graph Reordering for Cache-Efficient Near Neighbor Search](https://papers.nips.cc/paper_files/paper/2022/hash/fb44a668c2d4bc984e9d6ca261262cbb-Abstract-Conference.html)&nbsp;·&nbsp;Coleman&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2104.03221)
- **IEEE&nbsp;TBD&nbsp;2021** · [Billion-Scale Similarity Search with GPUs](https://doi.org/10.1109/tbdata.2019.2921572)&nbsp;·&nbsp;Johnson&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1702.08734)
- **TPAMI&nbsp;2021** · [Quicker ADC: Unlocking the Hidden Potential of Product Quantization with SIMD](https://doi.org/10.1109/tpami.2019.2952606)&nbsp;·&nbsp;André&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1812.09162)
- **ICDE&nbsp;2020** · [SONG: Approximate Nearest Neighbor Search on GPU](https://doi.org/10.1109/icde48307.2020.00094)&nbsp;·&nbsp;Zhao&nbsp;et&nbsp;al.
- **VLDB&nbsp;2015** · [Cache Locality is not Enough: High-Performance Nearest Neighbor Search with Product Quantization Fast Scan](https://doi.org/10.14778/2856318.2856324)&nbsp;·&nbsp;André&nbsp;et&nbsp;al.
- **MICRO&nbsp;2012** · [Kernel Weaver: Automatically Fusing Database Primitives for Efficient GPU Computation](https://doi.org/10.1109/micro.2012.19)&nbsp;·&nbsp;Wu&nbsp;et&nbsp;al.

### <a id="vector-systems"></a>Vector Databases and Filtered Search

Vector data management systems, queries with structured predicates, and&nbsp;benchmarks.

- **ICDE&nbsp;2026** · [Text2VectorSQL: Towards a Unified Interface for Vector Search and SQL Queries](https://doi.org/10.1109/icde65706.2026.00109)&nbsp;·&nbsp;Wang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2506.23071)
- **IEEE&nbsp;TBD&nbsp;2026** · [The Faiss Library](https://doi.org/10.1109/tbdata.2025.3618474)&nbsp;·&nbsp;Douze&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2401.08281)
- **VLDB&nbsp;2025** · [Filtered Vector Search: State-of-the-Art and Research Opportunities](https://doi.org/10.14778/3750601.3750700)&nbsp;·&nbsp;Chronis&nbsp;et&nbsp;al.
- **SIGMOD&nbsp;2024** · [ACORN: Performant and Predicate-Agnostic Search Over Vector Embeddings and Structured Data](https://doi.org/10.1145/3654923)&nbsp;·&nbsp;Patel&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2403.04871)
- **SIGMOD&nbsp;2024** · [Navigating Labels and Vectors: A Unified Approach to Filtered Approximate Nearest Neighbor Search](https://doi.org/10.1145/3698822)&nbsp;·&nbsp;Cai&nbsp;et&nbsp;al.
- **SIGMOD&nbsp;2024** · [SeRF: Segment Graph for Range-Filtering Approximate Nearest Neighbor Search](https://doi.org/10.1145/3639324)&nbsp;·&nbsp;Zuo&nbsp;et&nbsp;al.
- **VLDBJ&nbsp;2024** · [Survey of Vector Database Management Systems](https://doi.org/10.1007/s00778-024-00864-x)&nbsp;·&nbsp;Pan&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2310.14021)
- **arXiv&nbsp;2023** · [CAPS: A Practical Partition Index for Filtered Similarity Search](https://arxiv.org/abs/2308.15014)&nbsp;·&nbsp;Gupta&nbsp;et&nbsp;al.
- **WWW&nbsp;2023** · [Filtered-DiskANN: Graph Algorithms for Approximate Nearest Neighbor Search with Filters](https://doi.org/10.1145/3543507.3583552)&nbsp;·&nbsp;Gollapudi&nbsp;et&nbsp;al.
- **SIGMOD&nbsp;2023** · [High-Throughput Vector Similarity Search in Knowledge Graphs](https://doi.org/10.1145/3589777)&nbsp;·&nbsp;Mohoney&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2304.01926)
- **OSDI&nbsp;2023** · [VBASE: Unifying Online Vector Similarity Search and Relational Queries via Relaxed Monotonicity](https://www.usenix.org/conference/osdi23/presentation/zhang-qianxi)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.
- **SIGMOD&nbsp;2021** · [Milvus: A Purpose-Built Vector Data Management System](https://doi.org/10.1145/3448016.3457550)&nbsp;·&nbsp;Wang&nbsp;et&nbsp;al.
- **NeurIPS&nbsp;Competitions&nbsp;2021** · [Results of the NeurIPS'21 Challenge on Billion-Scale Approximate Nearest Neighbor Search](https://proceedings.mlr.press/v176/simhadri22a.html)&nbsp;·&nbsp;Simhadri&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2205.03763)
- **VLDB&nbsp;2020** · [AnalyticDB-V: A Hybrid Analytical Engine Towards Query Fusion for Structured and Unstructured Data](https://doi.org/10.14778/3415478.3415541)&nbsp;·&nbsp;Wei&nbsp;et&nbsp;al.
- **Information&nbsp;Systems&nbsp;2020** · [ANN-Benchmarks: A Benchmarking Tool for Approximate Nearest Neighbor Algorithms](https://doi.org/10.1016/j.is.2019.02.006)&nbsp;·&nbsp;Aumüller&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1807.05614)

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
- **ECAI&nbsp;2025** · [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://doi.org/10.3233/faia251160)&nbsp;·&nbsp;Chhikara&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2504.19413)
- **arXiv&nbsp;2025** · [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956)&nbsp;·&nbsp;Rasmussen&nbsp;et&nbsp;al.
- **UIST&nbsp;2023** · [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763)&nbsp;·&nbsp;Park&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2304.03442)
- **arXiv&nbsp;2023** · [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)&nbsp;·&nbsp;Packer&nbsp;et&nbsp;al.

### <a id="memory-sleep"></a>Sleep and Dreaming

Offline consolidation: replaying, distilling, and rewriting memories between&nbsp;sessions.

- **NeurIPS&nbsp;2026** · [Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents](https://openreview.net/forum?id=SR1n2zkaBO)&nbsp;·&nbsp;Ye&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2605.20616)
- **arXiv&nbsp;2026** · [Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories](https://arxiv.org/abs/2606.03979)&nbsp;·&nbsp;Behrouz&nbsp;et&nbsp;al.
- **arXiv&nbsp;2025** · [Sleep-time Compute: Beyond Inference Scaling at Test-time](https://arxiv.org/abs/2504.13171)&nbsp;·&nbsp;Lin&nbsp;et&nbsp;al.
- **Nature&nbsp;Communications&nbsp;2022** · [Sleep-Like Unsupervised Replay Reduces Catastrophic Forgetting in Artificial Neural Networks](https://doi.org/10.1038/s41467-022-34938-7)&nbsp;·&nbsp;Tadros&nbsp;et&nbsp;al.
- **PLDI&nbsp;2021** · [DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning](https://doi.org/10.1145/3453483.3454080)&nbsp;·&nbsp;Ellis&nbsp;et&nbsp;al.
- **NeurIPS&nbsp;2017** · [Continual Learning with Deep Generative Replay](https://papers.nips.cc/paper_files/paper/2017/hash/0efbe98067c6c73dba1250d2beaa81f9-Abstract.html)&nbsp;·&nbsp;Shin&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1705.08690)
- **Science&nbsp;1995** · [The “Wake-Sleep” Algorithm for Unsupervised Neural Networks](https://doi.org/10.1126/science.7761831)&nbsp;·&nbsp;Hinton&nbsp;et&nbsp;al.

## Attacks and Robustness

Poisoning and adversarial attacks on semantic data systems, and the algorithms behind&nbsp;them.

### <a id="attacks-rag"></a>RAG and Retrieval Poisoning

Corrupting the corpus, retriever, or ranker that a retrieval-augmented model depends&nbsp;on.

- **SaTML&nbsp;2026** · [Certifiably Robust RAG against Retrieval Corruption](https://doi.org/10.1109/satml68715.2026.00029)&nbsp;·&nbsp;Xiang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2405.15556)
- **IEEE&nbsp;S&P&nbsp;2026** · [GraphRAG under Fire](https://doi.org/10.1109/sp63933.2026.00070)&nbsp;·&nbsp;Liang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2501.14050)
- **WWW&nbsp;2026** · [KEPo: Knowledge Evolution Poison on Graph-based Retrieval-Augmented Generation](https://doi.org/10.1145/3774904.3792547)&nbsp;·&nbsp;Chen&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2603.11501)
- **SACMAT&nbsp;2026** · [Practical Poisoning Attacks against Retrieval-Augmented Generation](https://doi.org/10.1145/3750555.3811900)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2504.03957)
- **arXiv&nbsp;2025** · [A Few Words Can Distort Graphs: Knowledge Poisoning Attacks on Graph-based Retrieval-Augmented Generation of Large Language Models](https://arxiv.org/abs/2508.04276)&nbsp;·&nbsp;Wen&nbsp;et&nbsp;al.
- **arXiv&nbsp;2025** · [Benchmarking Poisoning Attacks against Retrieval-Augmented Generation](https://arxiv.org/abs/2505.18543)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.
- **ACL&nbsp;Findings&nbsp;2025** · [Corpus Poisoning via Approximate Greedy Gradient Descent](https://doi.org/10.18653/v1/2025.findings-acl.222)&nbsp;·&nbsp;Su&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2406.05087)
- **USENIX&nbsp;Security&nbsp;2025** · [Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents](https://www.usenix.org/conference/usenixsecurity25/presentation/shafran)&nbsp;·&nbsp;Shafran&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2406.05870)
- **USENIX&nbsp;Security&nbsp;2025** · [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag)&nbsp;·&nbsp;Zou&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2402.07867)
- **WWW&nbsp;2025** · [Traceback of Poisoning Attacks to Retrieval-Augmented Generation](https://doi.org/10.1145/3696410.3714756)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2504.21668)
- **arXiv&nbsp;2025** · [TrustRAG: Enhancing Robustness and Trustworthiness in Retrieval-Augmented Generation](https://arxiv.org/abs/2501.00879)&nbsp;·&nbsp;Zhou&nbsp;et&nbsp;al.
- **NeurIPS&nbsp;2024** · [AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://papers.nips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html)&nbsp;·&nbsp;Chen&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2407.12784)
- **arXiv&nbsp;2024** · [BadRAG: Identifying Vulnerabilities in Retrieval Augmented Generation of Large Language Models](https://arxiv.org/abs/2406.00083)&nbsp;·&nbsp;Xue&nbsp;et&nbsp;al.
- **arXiv&nbsp;2024** · [Black-Box Opinion Manipulation Attacks to Retrieval-Augmented Generation of Large Language Models](https://arxiv.org/abs/2407.13757)&nbsp;·&nbsp;Chen&nbsp;et&nbsp;al.
- **arXiv&nbsp;2024** · [Phantom: General Backdoor Attacks on Retrieval Augmented Language Generation](https://arxiv.org/abs/2405.20485)&nbsp;·&nbsp;Chaudhari&nbsp;et&nbsp;al.
- **IEEE&nbsp;S&P&nbsp;2024** · [Poisoning Web-Scale Training Datasets is Practical](https://doi.org/10.1109/sp54263.2024.00179)&nbsp;·&nbsp;Carlini&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2302.10149)
- **arXiv&nbsp;2024** · [TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models](https://arxiv.org/abs/2405.13401)&nbsp;·&nbsp;Cheng&nbsp;et&nbsp;al.
- **EMNLP&nbsp;Findings&nbsp;2024** · [Typos that Broke the RAG's Back: Genetic Attack on RAG Pipeline by Simulating Documents in the Wild via Low-level Perturbations](https://doi.org/10.18653/v1/2024.findings-emnlp.161)&nbsp;·&nbsp;Cho&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2404.13948)
- **AISec&nbsp;2023** · [Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://doi.org/10.1145/3605764.3623985)&nbsp;·&nbsp;Greshake&nbsp;et&nbsp;al.
- **EMNLP&nbsp;2023** · [Poisoning Retrieval Corpora by Injecting Adversarial Passages](https://doi.org/10.18653/v1/2023.emnlp-main.849)&nbsp;·&nbsp;Zhong&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2310.19156)
- **TOIS&nbsp;2023** · [PRADA: Practical Black-box Adversarial Attacks against Neural Ranking Models](https://doi.org/10.1145/3576923)&nbsp;·&nbsp;Wu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2204.01321)
- **SIGIR&nbsp;2023** · [Topic-oriented Adversarial Attacks against Black-box Neural Ranking Models](https://doi.org/10.1145/3539618.3591777)&nbsp;·&nbsp;Liu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2304.14867)

### <a id="attacks-graph"></a>Knowledge Graph and Graph Attacks

Perturbing triples and edges to mislead embeddings, alignment, and graph neural&nbsp;networks.

- **SIGIR&nbsp;2024** · [Untargeted Adversarial Attack on Knowledge Graph Embeddings](https://doi.org/10.1145/3626772.3657702)&nbsp;·&nbsp;Zhao&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2405.10970)
- **WWW&nbsp;2023** · [MaSS: Model-agnostic, Semantic and Stealthy Data Poisoning Attack on Knowledge Graph Embedding](https://doi.org/10.1145/3543507.3583203)&nbsp;·&nbsp;You&nbsp;et&nbsp;al.
- **TKDE&nbsp;2022** · [Adversarial Attack and Defense on Graph Data: A Survey](https://doi.org/10.1109/tkde.2022.3201243)&nbsp;·&nbsp;Sun&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1812.10528)
- **NeurIPS&nbsp;2022** · [Are Defenses for Graph Neural Networks Robust?](https://papers.nips.cc/paper_files/paper/2022/hash/3ac904a31f9141444009777abef2ed8e-Abstract-Conference.html)&nbsp;·&nbsp;Mujkanovic&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2301.13694)
- **EMNLP&nbsp;2021** · [Adversarial Attack against Cross-lingual Knowledge Graph Alignment](https://doi.org/10.18653/v1/2021.emnlp-main.432)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.
- **EMNLP&nbsp;2021** · [Adversarial Attacks on Knowledge Graph Embeddings via Instance Attribution Methods](https://doi.org/10.18653/v1/2021.emnlp-main.648)&nbsp;·&nbsp;Bhardwaj&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2111.03120)
- **ACL&nbsp;2021** · [Poisoning Knowledge Graph Embeddings via Relation Inference Patterns](https://doi.org/10.18653/v1/2021.acl-long.147)&nbsp;·&nbsp;Bhardwaj&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2111.06345)
- **NeurIPS&nbsp;2021** · [Robustness of Graph Neural Networks at Scale](https://papers.nips.cc/paper_files/paper/2021/hash/3ea2db50e62ceefceaf70a9d9a56a6f4-Abstract.html)&nbsp;·&nbsp;Geisler&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2110.14038)
- **KDD&nbsp;2020** · [Graph Structure Learning for Robust Graph Neural Networks](https://doi.org/10.1145/3394486.3403049)&nbsp;·&nbsp;Jin&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2005.10203)
- **ICLR&nbsp;2019** · [Adversarial Attacks on Graph Neural Networks via Meta Learning](https://openreview.net/forum?id=Bylnx209YX)&nbsp;·&nbsp;Zügner&nbsp;and&nbsp;Günnemann&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1902.08412)
- **ICML&nbsp;2019** · [Adversarial Attacks on Node Embeddings via Graph Poisoning](https://proceedings.mlr.press/v97/bojchevski19a.html)&nbsp;·&nbsp;Bojchevski&nbsp;and&nbsp;Günnemann&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1809.01093)
- **IJCAI&nbsp;2019** · [Data Poisoning Attack against Knowledge Graph Embedding](https://doi.org/10.24963/ijcai.2019/674)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1904.12052)
- **NAACL&nbsp;2019** · [Investigating Robustness and Interpretability of Link Prediction via Adversarial Modifications](https://doi.org/10.18653/v1/n19-1337)&nbsp;·&nbsp;Pezeshkpour&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1905.00563)
- **IJCAI&nbsp;2019** · [Topology Attack and Defense for Graph Neural Networks: An Optimization Perspective](https://doi.org/10.24963/ijcai.2019/550)&nbsp;·&nbsp;Xu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1906.04214)
- **ICML&nbsp;2018** · [Adversarial Attack on Graph Structured Data](https://proceedings.mlr.press/v80/dai18b.html)&nbsp;·&nbsp;Dai&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1806.02371)
- **KDD&nbsp;2018** · [Adversarial Attacks on Neural Networks for Graph Data](https://doi.org/10.1145/3219819.3220078)&nbsp;·&nbsp;Zügner&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1805.07984)

### <a id="attacks-quality"></a>Data Quality and Perturbation

Noisy, perturbed, or low-quality data and metadata, and how well systems hold&nbsp;up.

- **arXiv&nbsp;2026** · [An Agentic Approach to Metadata Reasoning](https://arxiv.org/abs/2604.20144)&nbsp;·&nbsp;Zhang&nbsp;et&nbsp;al.
- **ICDE&nbsp;Workshops&nbsp;2026** · [Less Is More? When Dataset Context Hurts LLM-Generated Dataset Descriptions](https://doi.org/10.1109/icdew71238.2026.00022)&nbsp;·&nbsp;Gan&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2606.02334)
- **AAAI&nbsp;2024** · [Benchmarking Large Language Models in Retrieval-Augmented Generation](https://doi.org/10.1609/aaai.v38i16.29728)&nbsp;·&nbsp;Chen&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2309.01431)
- **ICLR&nbsp;2024** · [Making Retrieval-Augmented Language Models Robust to Irrelevant Context](https://openreview.net/forum?id=ZS4m74kZpH)&nbsp;·&nbsp;Yoran&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2310.01558)
- **SIGIR&nbsp;2024** · [The Power of Noise: Redefining Retrieval for RAG Systems](https://doi.org/10.1145/3626772.3657834)&nbsp;·&nbsp;Cuconasu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2401.14887)
- **TKDE&nbsp;2023** · [Data Lakes: A Survey of Functions and Systems](https://doi.org/10.1109/tkde.2023.3270101)&nbsp;·&nbsp;Hai&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2106.09592)
- **ICLR&nbsp;2023** · [Dr.Spider: A Diagnostic Evaluation Benchmark towards Text-to-SQL Robustness](https://openreview.net/forum?id=Wc5bmZZU9cy)&nbsp;·&nbsp;Chang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2301.08881)
- **ICML&nbsp;2023** · [Large Language Models Can Be Easily Distracted by Irrelevant Context](https://proceedings.mlr.press/v202/shi23a.html)&nbsp;·&nbsp;Shi&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2302.00093)
- **ACL&nbsp;2023** · [RobuT: A Systematic Study of Table QA Robustness Against Human-Annotated Adversarial Perturbations](https://doi.org/10.18653/v1/2023.acl-long.334)&nbsp;·&nbsp;Zhao&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2306.14321)
- **ACL&nbsp;2022** · [Towards Robustness of Text-to-SQL Models Against Natural and Realistic Adversarial Table Perturbation](https://doi.org/10.18653/v1/2022.acl-long.142)&nbsp;·&nbsp;Pi&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2212.09994)
- **ICDE&nbsp;2021** · [CleanML: A Study for Evaluating the Impact of Data Cleaning on ML Classification Tasks](https://doi.org/10.1109/icde51399.2021.00009)&nbsp;·&nbsp;Li&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1904.09483)
- **EMNLP&nbsp;2021** · [Dealing with Typos for BERT-based Passage Retrieval and Ranking](https://doi.org/10.18653/v1/2021.emnlp-main.225)&nbsp;·&nbsp;Zhuang&nbsp;and&nbsp;Zuccon&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2108.12139)
- **ACL&nbsp;2021** · [Towards Robustness of Text-to-SQL Models against Synonym Substitution](https://doi.org/10.18653/v1/2021.acl-long.195)&nbsp;·&nbsp;Gan&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2106.01065)
- **SIGMOD&nbsp;2019** · [Raha: A Configuration-Free Error Detection System](https://doi.org/10.1145/3299869.3324956)&nbsp;·&nbsp;Mahdavi&nbsp;et&nbsp;al.
- **VLDB&nbsp;2018** · [Automating Large-Scale Data Quality Verification](https://doi.org/10.14778/3229863.3229867)&nbsp;·&nbsp;Schelter&nbsp;et&nbsp;al.
- **VLDB&nbsp;2017** · [HoloClean: Holistic Data Repairs with Probabilistic Inference](https://doi.org/10.14778/3137628.3137631)&nbsp;·&nbsp;Rekatsinas&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1702.00820)
- **Semantic&nbsp;Web&nbsp;2017** · [Knowledge Graph Refinement: A Survey of Approaches and Evaluation Methods](https://doi.org/10.3233/sw-160218)&nbsp;·&nbsp;Paulheim
- **SIGMOD&nbsp;2016** · [Data Cleaning: Overview and Emerging Challenges](https://doi.org/10.1145/2882903.2912574)&nbsp;·&nbsp;Chu&nbsp;et&nbsp;al.
- **Semantic&nbsp;Web&nbsp;2016** · [Quality Assessment for Linked Data: A Survey](https://doi.org/10.3233/sw-150175)&nbsp;·&nbsp;Zaveri&nbsp;et&nbsp;al.
- **IJSWIS&nbsp;2014** · [Improving the Quality of Linked Data Using Statistical Distributions](https://doi.org/10.4018/ijswis.2014040104)&nbsp;·&nbsp;Paulheim&nbsp;and&nbsp;Bizer
- **WWW&nbsp;2014** · [Test-driven Evaluation of Linked Data Quality](https://doi.org/10.1145/2566486.2568002)&nbsp;·&nbsp;Kontokostas&nbsp;et&nbsp;al.

### <a id="attacks-algorithms"></a>Search and Graph Algorithms

Beam search, Monte Carlo tree search and UCT, network flows, and dynamic&nbsp;trees.

- **SaTML&nbsp;2025** · [Jailbreaking Black Box Large Language Models in Twenty Queries](https://doi.org/10.1109/satml64287.2025.00010)&nbsp;·&nbsp;Chao&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2310.08419)
- **COLING&nbsp;2025** · [Monte Carlo Tree Search Based Prompt Autogeneration for Jailbreak Attacks against LLMs](https://aclanthology.org/2025.coling-main.71/)&nbsp;·&nbsp;Wu&nbsp;et&nbsp;al.
- **ICLR&nbsp;2024** · [AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models](https://openreview.net/forum?id=7Jwpw4qKkb)&nbsp;·&nbsp;Liu&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2310.04451)
- **ICML&nbsp;2024** · [Fast Adversarial Attacks on Language Models In One GPU Minute](https://proceedings.mlr.press/v235/sadasivan24a.html)&nbsp;·&nbsp;Sadasivan&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2402.15570)
- **NeurIPS&nbsp;2024** · [Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](https://papers.nips.cc/paper_files/paper/2024/hash/70702e8cbb4890b4a467b984ae59828a-Abstract-Conference.html)&nbsp;·&nbsp;Mehrotra&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2312.02119)
- **arXiv&nbsp;2023** · [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043)&nbsp;·&nbsp;Zou&nbsp;et&nbsp;al.
- **FOCS&nbsp;2022** · [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://doi.org/10.1109/focs54457.2022.00064)&nbsp;·&nbsp;Chen&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2203.00671)
- **EMNLP&nbsp;2020** · [If Beam Search Is the Answer, What Was the Question?](https://doi.org/10.18653/v1/2020.emnlp-main.170)&nbsp;·&nbsp;Meister&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/2010.02650)
- **AAAI&nbsp;2020** · [Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment](https://doi.org/10.1609/aaai.v34i05.6311)&nbsp;·&nbsp;Jin&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1907.11932)
- **ACL&nbsp;2020** · [Word-level Textual Adversarial Attacking as Combinatorial Optimization](https://doi.org/10.18653/v1/2020.acl-main.540)&nbsp;·&nbsp;Zang&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1910.12196)
- **ALENEX&nbsp;2019** · [Batch-Parallel Euler Tour Trees](https://doi.org/10.1137/1.9781611975499.8)&nbsp;·&nbsp;Tseng&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1810.10738)
- **SPAA&nbsp;2019** · [Parallel Batch-Dynamic Graph Connectivity](https://doi.org/10.1145/3323165.3323196)&nbsp;·&nbsp;Acar&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1903.08794)
- **EMNLP&nbsp;2019** · [Universal Adversarial Triggers for Attacking and Analyzing NLP](https://doi.org/10.18653/v1/d19-1221)&nbsp;·&nbsp;Wallace&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1908.07125)
- **EMNLP&nbsp;2018** · [Generating Natural Language Adversarial Examples](https://doi.org/10.18653/v1/d18-1316)&nbsp;·&nbsp;Alzantot&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1804.07998)
- **ACL&nbsp;2018** · [HotFlip: White-Box Adversarial Examples for Text Classification](https://doi.org/10.18653/v1/p18-2006)&nbsp;·&nbsp;Ebrahimi&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/1712.06751)
- **Nature&nbsp;2016** · [Mastering the Game of Go with Deep Neural Networks and Tree Search](https://doi.org/10.1038/nature16961)&nbsp;·&nbsp;Silver&nbsp;et&nbsp;al.
- **IEEE&nbsp;TCIAIG&nbsp;2012** · [A Survey of Monte Carlo Tree Search Methods](https://doi.org/10.1109/tciaig.2012.2186810)&nbsp;·&nbsp;Browne&nbsp;et&nbsp;al.
- **JEA&nbsp;2009** · [Dynamic Trees in Practice](https://doi.org/10.1145/1498698.1594231)&nbsp;·&nbsp;Tarjan&nbsp;and&nbsp;Werneck
- **ECML&nbsp;2006** · [Bandit Based Monte-Carlo Planning](https://doi.org/10.1007/11871842_29)&nbsp;·&nbsp;Kocsis&nbsp;and&nbsp;Szepesvári
- **Computers&nbsp;and&nbsp;Games&nbsp;2006** · [Efficient Selectivity and Backup Operators in Monte-Carlo Tree Search](https://doi.org/10.1007/978-3-540-75538-8_7)&nbsp;·&nbsp;Coulom
- **TALG&nbsp;2005** · [Maintaining Information in Fully Dynamic Trees with Top Trees](https://doi.org/10.1145/1103963.1103966)&nbsp;·&nbsp;Alstrup&nbsp;et&nbsp;al.&nbsp;·&nbsp;[arXiv](https://arxiv.org/abs/cs/0310065)
- **TPAMI&nbsp;2004** · [An Experimental Comparison of Min-Cut/Max-Flow Algorithms for Energy Minimization in Vision](https://doi.org/10.1109/tpami.2004.60)&nbsp;·&nbsp;Boykov&nbsp;and&nbsp;Kolmogorov
- **Machine&nbsp;Learning&nbsp;2002** · [Finite-time Analysis of the Multiarmed Bandit Problem](https://doi.org/10.1023/a:1013689704352)&nbsp;·&nbsp;Auer&nbsp;et&nbsp;al.
- **JACM&nbsp;2001** · [Poly-Logarithmic Deterministic Fully-Dynamic Algorithms for Connectivity, Minimum Spanning Tree, 2-Edge, and Biconnectivity](https://doi.org/10.1145/502090.502095)&nbsp;·&nbsp;Holm&nbsp;et&nbsp;al.
- **JACM&nbsp;1999** · [Randomized Fully Dynamic Graph Algorithms with Polylogarithmic Time per Operation](https://doi.org/10.1145/320211.320215)&nbsp;·&nbsp;Henzinger&nbsp;and&nbsp;King
- **JACM&nbsp;1988** · [A New Approach to the Maximum-Flow Problem](https://doi.org/10.1145/48014.61051)&nbsp;·&nbsp;Goldberg&nbsp;and&nbsp;Tarjan
- **JCSS&nbsp;1983** · [A Data Structure for Dynamic Trees](https://doi.org/10.1016/0022-0000%2883%2990006-5)&nbsp;·&nbsp;Sleator&nbsp;and&nbsp;Tarjan
<!-- END LIST -->

## Citing

BibTeX for every entry is in [references.bib](references.bib), grouped by&nbsp;section.

## Contributing

Suggestions are welcome as issues. Scope and entry format are in&nbsp;[CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released into the public domain under [CC0&nbsp;1.0](LICENSE).
