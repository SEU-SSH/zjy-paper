# DeFuzz - IEEE S&P 论文撰写与精校进度追踪 (Paper Writing Status)

> **状态定义说明**：
> 本文档严格执行**二值状态**规范——全篇仅存在 **`[ready]`** 与 **`[不 ready]`** 两种状态，坚决杜绝模糊中间态。
> - **`[ready]`**：已精校定稿，具备最高权威性，作为后续撰写与全篇对齐的基准参考。
> - **`[不 ready]`**：未精校 / 未定稿 / 待修改 / 草稿 / 待补充数据状态。
>
> **当前状态汇总**：
> - **`[ready]` (仅以下 2 处)**：
>   1. **Abstract（摘要）**
>   2. **Section 3 Overview（第三章 系统概览）**
> - **`[不 ready]`**：其余所有章节与子章节均处于 `不 ready` 状态。

---

## 逐章节精校状态列表

### 0. Abstract
- [ready] **Abstract** (已精校锁定，确立核心问题、Oracle Gap、四步工作流与零 LLM 裁决基准)

### 1. Introduction
- [不 ready] 1.1 Scope & Context
- [不 ready] 1.2 The Core Problem (Silent Defense Failures & CVE-2023-4039)
- [不 ready] 1.3 Research Gap & Fundamental Bottlenecks
- [不 ready] 1.4 Key Insights & Our Approach
- [不 ready] 1.5 Summary of Results
- [不 ready] 1.6 Contributions (Four Disjoint Contributions)

### 2. Motivation
- [ready] **Section 2 Motivation** (已精校锁定：2.1 编译器防御跨阶段机制、2.2 单一案例 GCC PR 125079 逻辑透析与代码块高亮排版、2.3 现有方法局限与破局要求；符合 plain writing 规范与导师意见)

### 3. Design of DeFuzz (System Overview & Methodology)
- [ready] **3.0 Section 3 Overview & Architecture** (第三章概览正文与系统架构总图，已精校锁定，明确四步核心流程)
- [不 ready] 3.1 Security Invariant Generation
  - [不 ready] 3.1.1 Formal Invariant Contract
  - [不 ready] 3.1.2 Candidate Extraction via Segmented CoT
  - [不 ready] 3.1.3 Cross-Mechanism Transfer via Hybrid RAG
  - [不 ready] 3.1.4 Grounding Gates and Catalog Maintenance
- [不 ready] 3.2 Compiler Source Mapping
  - [不 ready] 3.2.1 MCP-Guided Codebase Navigation
  - [不 ready] 3.2.2 Three-Level Decision Hierarchy (Pass / Function / Branches)
  - [不 ready] 3.2.3 Compile-Time Branch Probing (`GCC_INST`)
- [不 ready] 3.3 Programmatic Oracle Construction
  - [不 ready] 3.3.1 Oracle Contract and Four-State Verdict Matrix
  - [不 ready] 3.3.2 Dual Static and Dynamic Checkers (Canary Register Leak & `_FORTIFY_SOURCE` Bounds)
  - [不 ready] 3.3.3 Target-Specific Specialization Across ISAs
  - [不 ready] 3.3.4 Differential Configuration Profiling
- [不 ready] 3.4 Agentic Directed Fuzzing
  - [不 ready] 3.4.1 Deterministic Orchestration Pipeline & Versioned Blackboard
  - [不 ready] 3.4.2 Checker-Aware Seed Synthesis and DCE Evasion
  - [不 ready] 3.4.3 Adaptive Telemetry Feedback and Checker Evolution
  - [不 ready] 3.4.4 Automated Bug Minimization and Lateral Amplification

### 4. Implementation
- [不 ready] 4.1 Go Core & Deterministic Evaluation Service
- [不 ready] 4.2 Python Agent Orchestrator & MCP/gRPC Integration
- [不 ready] 4.3 Artifact Bundle & Deterministic Replay Pipeline

### 5. Evaluation
- [不 ready] 5.1 Experimental Setup & Evaluation Matrix
- [不 ready] 5.2 RQ1: Silent Defense Vulnerability Discovery (Real Bugs & CVEs)
- [不 ready] 5.3 RQ2: Invariant Extraction & Transfer Quality
- [不 ready] 5.4 RQ3: Ablation Study (Explicit Orchestration vs. Free-Running Agent)
- [不 ready] 5.5 RQ4: Multi-ISA Checker Cross-Validation & Generalization
- [不 ready] 5.6 RQ5: Anti-DCE Probe Efficiency & Telemetry Feedback Impact

### 6. Discussion and Limitations
- [不 ready] 6.1 Manual Effort & Human-in-the-Loop Boundaries
- [不 ready] 6.2 Token Costs & Computational Budget
- [不 ready] 6.3 False Positive and Oracle Divergence Analysis

### 7. Related Work
- [不 ready] 7.1 Compiler Bug Finding and the Oracle Gap
- [不 ready] 7.2 Silent and Security Bugs in Compilers
- [不 ready] 7.3 LLM and RAG-based Property Generation
- [不 ready] 7.4 LLM-Agent Fuzzing: Hallucination vs. Determinism

### 8. Conclusion
- [不 ready] 8.1 Summary of Findings and Contributions
