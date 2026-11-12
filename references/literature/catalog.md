# 候选文献目录

核验日期：2026-11-12。此目录是选读与引用索引，不是全部文献的全文评审或系统综述。用途仅表示可进一步考察的引用位置；比较论点必须核对条目的阅读深度和限制。

共 136 项，102 篇论文、34 项官方文档/软件；114 个引用键不在当前 refs.bib 中。

返回 [README](README.md) · [优先阅读路线](reading-map.md) · [完整 BibTeX](library.bib) · [新增 BibTeX](additional.bib)

## 既有 Related Work 与方法基础

23 项。专题说明：[notes/existing-and-methods.md](notes/existing-and-methods.md)。

| Key | 年份 | 候选条目 | 优先级 | 核验深度 | 与现有 refs 的关系 |
| --- | --- | --- | --- | --- | --- |
| `livinskii2020yarpgen` | 2020 | [Random Testing for C and C++ Compilers with YARPGen](#livinskii2020yarpgen) | core | metadata+method | 已有 key，核对后替换 |
| `livinskii2023loops` | 2023 | [Fuzzing Loop Optimizations in Compilers for C++ and Data-Parallel Languages](#livinskii2023loops) | core | metadata+method | 已有 key，核对后替换 |
| `xia2024fuzz4all` | 2024 | [Fuzz4All: Universal Fuzzing with Large Language Models](#xia2024fuzz4all) | core | metadata+method | 已有 key，核对后替换 |
| `ou2024metamut` | 2024 | [The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators](#ou2024metamut) | core | metadata+method | 已有 key，核对后替换 |
| `li2024ubfuzz` | 2024 | [UBFuzz: Finding Bugs in Sanitizer Implementations](#li2024ubfuzz) | core | metadata+method | 已有 key，核对后替换 |
| `yang2011csmith` | 2011 | [Finding and Understanding Bugs in C Compilers](#yang2011csmith) | core | metadata+method | 已有 key，核对后替换 |
| `le2014emi` | 2014 | [Compiler Validation via Equivalence Modulo Inputs](#le2014emi) | core | metadata+method | 已有 key，核对后替换 |
| `bohme2017aflgo` | 2017 | [Directed Greybox Fuzzing](#bohme2017aflgo) | core | metadata+method | 已有 key，核对后替换 |
| `lopes2021alive2` | 2021 | [Alive2: Bounded Translation Validation for LLVM](#lopes2021alive2) | core | metadata+method | 已有 key，核对后替换 |
| `liu2025propertygpt` | 2025 | [PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation](#liu2025propertygpt) | core | metadata+method | 已有 key，核对后替换 |
| `wang2013stack` | 2013 | [Towards Optimization-Safe Systems: Analyzing the Impact of Undefined Behavior](#wang2013stack) | core | metadata+method | 已有 key，核对后替换 |
| `wang2026bulbasaur` | 2026 | [Bulbasaur: Branch-Guided Online Mutator Generation for Greybox Fuzzing](#wang2026bulbasaur) | core | metadata+method | 已有 key，核对后替换 |
| `yang2024whitefox` | 2024 | [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](#yang2024whitefox) | core | metadata+method | 已有 key，核对后替换 |
| `yang2025knighter` | 2025 | [KNighter: Transforming Static Analysis with LLM-Synthesized Checkers](#yang2025knighter) | core | metadata+method | 已有 key，核对后替换 |
| `silentbugs2023` | 2023 | [Silent Bugs Matter: A Study of Compiler-Introduced Security Bugs](#silentbugs2023) | core | metadata+abstract | 已有 key，核对后替换 |
| `liu2025agentfuzz` | 2025 | [Make Agent Defeat Agent: Automatic Detection of Taint-Style Vulnerabilities in LLM-based Agents](#liu2025agentfuzz) | optional | metadata+abstract | 已有 key，核对后替换 |
| `lin2026specauditor` | 2026 | [SpecAuditor: Generating Audit Specifications for LLM-Driven Bug Detection](#lin2026specauditor) | core | metadata-only | 已有 key，核对后替换 |
| `su2026cill` | 2026 | [CIll: CTI-Guided Invariant Generation via LLMs for Model Checking](#su2026cill) | supporting | metadata+abstract | 已有 key，核对后替换 |
| `wei2022chain` | 2022 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](#wei2022chain) | supporting | metadata+abstract | 已有 key，核对后替换 |
| `lewis2020retrieval` | 2020 | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](#lewis2020retrieval) | supporting | metadata+abstract | 已有 key，核对后替换 |
| `lattner2004llvm` | 2004 | [LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation](#lattner2004llvm) | supporting | metadata+abstract | 新增 key |
| `demoura2008z3` | 2008 | [Z3: An Efficient SMT Solver](#demoura2008z3) | supporting | metadata-only | 已有 key，核对后替换 |
| `langgraph` | 滚动/未定 | [LangGraph](#langgraph) | optional | official-doc | 已有 key，核对后替换 |

## 编译器测试、验证、评测与缩减

23 项。专题说明：[notes/compiler-testing.md](notes/compiler-testing.md)。

| Key | 年份 | 候选条目 | 优先级 | 核验深度 | 与现有 refs 的关系 |
| --- | --- | --- | --- | --- | --- |
| `pnueli1998translationvalidation` | 1998 | [Translation Validation](#pnueli1998translationvalidation) | core | metadata+method | 新增 key |
| `claessen2000quickcheck` | 2000 | [QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs](#claessen2000quickcheck) | supporting | metadata+abstract | 新增 key |
| `zeller2002deltadebugging` | 2002 | [Simplifying and Isolating Failure-Inducing Input](#zeller2002deltadebugging) | core | metadata+method | 新增 key |
| `ernst2007daikon` | 2007 | [The Daikon system for dynamic detection of likely invariants](#ernst2007daikon) | core | metadata+method | 新增 key |
| `leroy2009compcert` | 2009 | [Formal verification of a realistic compiler](#leroy2009compcert) | core | metadata+abstract | 新增 key |
| `holler2012langfuzz` | 2012 | [Fuzzing with Code Fragments](#holler2012langfuzz) | supporting | metadata+abstract | 新增 key |
| `regehr2012creduce` | 2012 | [Test-Case Reduction for C Compiler Bugs](#regehr2012creduce) | core | metadata+abstract | 新增 key |
| `le2015athena` | 2015 | [Finding Deep Compiler Bugs via Guided Stochastic Program Mutation](#le2015athena) | core | metadata+abstract | 新增 key |
| `lidbury2015clsmith` | 2015 | [Many-Core Compiler Fuzzing](#lidbury2015clsmith) | core | metadata+abstract | 新增 key |
| `lopes2015alive` | 2015 | [Provably Correct Peephole Optimizations with Alive](#lopes2015alive) | core | metadata+abstract | 新增 key |
| `menendez2016alivefp` | 2016 | [Alive-FP: Automated Verification of Floating Point Based Peephole Optimizations in LLVM](#menendez2016alivefp) | supporting | metadata+method | 新增 key |
| `sun2016hermes` | 2016 | [Finding Compiler Bugs via Live Code Mutation](#sun2016hermes) | core | metadata+abstract | 新增 key |
| `donaldson2017glfuzz` | 2017 | [Automated Testing of Graphics Shader Compilers](#donaldson2017glfuzz) | supporting | metadata+abstract | 新增 key |
| `zhang2017spe` | 2017 | [Skeletal Program Enumeration for Rigorous Compiler Testing](#zhang2017spe) | core | metadata+abstract | 新增 key |
| `chen2018metamorphicsurvey` | 2018 | [Metamorphic Testing: A Review of Challenges and Opportunities](#chen2018metamorphicsurvey) | core | metadata+abstract | 新增 key |
| `klees2018fuzzeval` | 2018 | [Evaluating Fuzz Testing](#klees2018fuzzeval) | core | metadata+method | 新增 key |
| `sun2018perses` | 2018 | [Perses: Syntax-Guided Program Reduction](#sun2018perses) | supporting | metadata+method | 新增 key |
| `gharachorlu2019pardis` | 2019 | [Pardis: Priority Aware Test Case Reduction](#gharachorlu2019pardis) | optional | metadata+method | 新增 key |
| `hazimeh2020magma` | 2020 | [Magma: A Ground-Truth Fuzzing Benchmark](#hazimeh2020magma) | core | metadata+method | 新增 key |
| `park2020die` | 2020 | [Fuzzing JavaScript Engines with Aspect-preserving Mutation](#park2020die) | supporting | metadata+method | 新增 key |
| `manes2021fuzzingsurvey` | 2021 | [The Art, Science, and Engineering of Fuzzing: A Survey](#manes2021fuzzingsurvey) | supporting | metadata+abstract | 新增 key |
| `metzman2021fuzzbench` | 2021 | [FuzzBench: An Open Fuzzer Benchmarking Platform and Service](#metzman2021fuzzbench) | core | metadata+abstract | 新增 key |
| `gross2023fuzzilli` | 2023 | [FUZZILLI: Fuzzing for JavaScript JIT Compiler Vulnerabilities](#gross2023fuzzilli) | supporting | metadata+abstract | 新增 key |

## 编译器防御与安全语义

29 项。专题说明：[notes/defenses.md](notes/defenses.md)。

| Key | 年份 | 候选条目 | 优先级 | 核验深度 | 与现有 refs 的关系 |
| --- | --- | --- | --- | --- | --- |
| `abadi2009cfi` | 2009 | [Control-flow integrity principles, implementations, and applications](#abadi2009cfi) | core | metadata+abstract | 新增 key |
| `burow2017cfisurvey` | 2017 | [Control-Flow Integrity: Precision, Security, and Performance](#burow2017cfisurvey) | core | metadata+abstract | 新增 key |
| `cowan1998stackguard` | 1998 | [StackGuard: Automatic Adaptive Detection and Prevention of Buffer-Overflow Attacks](#cowan1998stackguard) | core | metadata+abstract | 新增 key |
| `kuznetsov2014cpi` | 2014 | [Code-Pointer Integrity](#kuznetsov2014cpi) | core | metadata+abstract | 新增 key |
| `tice2014forwardcfi` | 2014 | [Enforcing Forward-Edge Control-Flow Integrity in GCC & LLVM](#tice2014forwardcfi) | core | metadata+abstract | 新增 key |
| `burow2019shadowstacks` | 2019 | [SoK: Shining Light on Shadow Stacks](#burow2019shadowstacks) | core | metadata+abstract | 新增 key |
| `mashtizadeh2015ccfi` | 2015 | [CCFI: Cryptographically Enforced Control Flow Integrity](#mashtizadeh2015ccfi) | supporting | metadata+abstract | 新增 key |
| `zhang2016vtrust` | 2016 | [VTrust: Regaining Trust on Virtual Calls](#zhang2016vtrust) | supporting | metadata+abstract | 新增 key |
| `burow2018cfixx` | 2018 | [CFIXX: Object Type Integrity for C++](#burow2018cfixx) | supporting | metadata+abstract | 新增 key |
| `serebryany2012asan` | 2012 | [AddressSanitizer: A Fast Address Sanity Checker](#serebryany2012asan) | core | metadata+abstract | 新增 key |
| `stepanov2015msan` | 2015 | [MemorySanitizer: Fast Detector of Uninitialized Memory Use in C++](#stepanov2015msan) | core | metadata+method | 新增 key |
| `nagarakatte2009softbound` | 2009 | [SoftBound: Highly Compatible and Complete Spatial Memory Safety for C](#nagarakatte2009softbound) | core | metadata+abstract | 新增 key |
| `nagarakatte2010cets` | 2010 | [CETS: compiler enforced temporal safety for C](#nagarakatte2010cets) | core | metadata+abstract | 新增 key |
| `akritidis2009baggy` | 2009 | [Baggy Bounds Checking: An Efficient and Backwards-Compatible Defense against Out-of-Bounds Errors](#akritidis2009baggy) | supporting | metadata+method | 新增 key |
| `berger2006diehard` | 2006 | [DieHard: probabilistic memory safety for unsafe languages](#berger2006diehard) | optional | metadata+abstract | 新增 key |
| `duck2018effectivesan` | 2018 | [EffectiveSan: type and memory error detection using dynamically typed C/C++](#duck2018effectivesan) | supporting | metadata+abstract | 新增 key |
| `haller2016typesan` | 2016 | [TypeSan: Practical Type Confusion Detection](#haller2016typesan) | supporting | metadata+abstract | 新增 key |
| `jeon2017hextype` | 2017 | [HexType: Efficient Detection of Type Confusion Errors for C++](#jeon2017hextype) | supporting | metadata+abstract | 新增 key |
| `serebryany2018memorytagging` | 2018 | [Memory Tagging and how it improves C/C++ memory safety](#serebryany2018memorytagging) | supporting | metadata+abstract | 新增 key |
| `jeon2020fuzzan` | 2020 | [FuZZan: Efficient Sanitizer Metadata Design for Fuzzing](#jeon2020fuzzan) | core | metadata+abstract | 新增 key |
| `marini2025qmsan` | 2025 | [QMSan: Efficiently Detecting Uninitialized Memory Errors During Fuzzing](#marini2025qmsan) | supporting | metadata+abstract | 新增 key |
| `szekeres2013eternalwar` | 2013 | [SoK: Eternal War in Memory](#szekeres2013eternalwar) | core | metadata+abstract | 新增 key |
| `yang2017deadstore` | 2017 | [Dead Store Elimination (Still) Considered Harmful](#yang2017deadstore) | core | metadata+abstract | 新增 key |
| `simon2018whatyouc` | 2018 | [What You Get is What You C: Controlling Side Effects in Mainstream C Compilers](#simon2018whatyouc) | core | metadata+abstract | 新增 key |
| `almeida2016ctverif` | 2016 | [Verifying Constant-Time Implementations](#almeida2016ctverif) | core | metadata+abstract | 新增 key |
| `blazy2019constanttime` | 2019 | [Verifying constant-time implementations by abstract interpretation](#blazy2019constanttime) | supporting | metadata+abstract | 新增 key |
| `oleksenko2020specfuzz` | 2020 | [SpecFuzz: Bringing Spectre-type vulnerabilities to the surface](#oleksenko2020specfuzz) | core | metadata+abstract | 新增 key |
| `guarnieri2020spectector` | 2020 | [Spectector: Principled Detection of Speculative Information Flows](#guarnieri2020spectector) | core | metadata+abstract | 新增 key |
| `vassena2021blade` | 2021 | [Automatically Eliminating Speculative Leaks from Cryptographic Code with Blade](#vassena2021blade) | core | metadata+abstract | 新增 key |

## LLM 测试、分析、规范及方法近邻

28 项。专题说明：[notes/llm-analysis.md](notes/llm-analysis.md)。

| Key | 年份 | 候选条目 | 优先级 | 核验深度 | 与现有 refs 的关系 |
| --- | --- | --- | --- | --- | --- |
| `deng2023titanfuzz` | 2023 | [Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models](#deng2023titanfuzz) | core | metadata+abstract | 新增 key |
| `deng2024fuzzgpt` | 2024 | [Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries](#deng2024fuzzgpt) | core | metadata+abstract | 新增 key |
| `meng2024chatafl` | 2024 | [Large Language Model guided Protocol Fuzzing](#meng2024chatafl) | core | metadata+abstract | 新增 key |
| `lyu2024promptfuzz` | 2024 | [Prompt Fuzzing for Fuzz Driver Generation](#lyu2024promptfuzz) | core | metadata+abstract | 新增 key |
| `hu2023chatfuzz` | 2023 | [Augmenting Greybox Fuzzing with Generative AI](#hu2023chatfuzz) | supporting | metadata+abstract | 新增 key |
| `zhang2026llamafuzz` | 2026 | [LLAMAFUZZ: Large Language Model Enhanced Greybox Fuzzing](#zhang2026llamafuzz) | supporting | metadata+abstract | 新增 key |
| `lemieux2023codamosa` | 2023 | [CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models](#lemieux2023codamosa) | core | metadata+abstract | 新增 key |
| `ryan2024symprompt` | 2024 | [Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM](#ryan2024symprompt) | supporting | metadata+abstract | 新增 key |
| `altmayerpizzorno2025coverup` | 2025 | [CoverUp: Effective High Coverage Test Generation for Python](#altmayerpizzorno2025coverup) | core | metadata+abstract | 新增 key |
| `chen2024chatunitest` | 2024 | [ChatUniTest: A Framework for LLM-Based Test Generation](#chen2024chatunitest) | supporting | metadata+abstract | 新增 key |
| `cosler2023nl2spec` | 2023 | [nl2spec: Interactively Translating Unstructured Natural Language to Temporal Logics with Large Language Models](#cosler2023nl2spec) | core | metadata+abstract | 新增 key |
| `sun2024clover` | 2024 | [Clover: Closed-Loop Verifiable Code Generation](#sun2024clover) | core | metadata+abstract | 新增 key |
| `wen2024autospec` | 2024 | [Enchanting Program Specification Synthesis by Large Language Models Using Static Analysis and Program Verification](#wen2024autospec) | core | metadata+abstract | 新增 key |
| `wu2024lemur` | 2024 | [Lemur: Integrating Large Language Models in Automated Program Verification](#wu2024lemur) | core | metadata+abstract | 新增 key |
| `li2025iris` | 2025 | [IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](#li2025iris) | core | metadata+abstract | 新增 key |
| `li2024llift` | 2024 | [Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach](#li2024llift) | core | metadata+abstract | 新增 key |
| `ji2025artemis` | 2025 | [Artemis: Toward Accurate Detection of Server-Side Request Forgeries through LLM-Assisted Inter-procedural Path-Sensitive Taint Analysis](#ji2025artemis) | supporting | metadata+abstract | 新增 key |
| `wang2025inferroi` | 2025 | [Boosting Static Resource Leak Detection via LLM-based Resource-Oriented Intention Inference](#wang2025inferroi) | core | metadata+abstract | 新增 key |
| `sun2024gptscan` | 2024 | [GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis](#sun2024gptscan) | core | metadata+abstract | 新增 key |
| `yao2023react` | 2023 | [ReAct: Synergizing Reasoning and Acting in Language Models](#yao2023react) | supporting | metadata+abstract | 新增 key |
| `shinn2023reflexion` | 2023 | [Reflexion: language agents with verbal reinforcement learning](#shinn2023reflexion) | supporting | metadata+abstract | 新增 key |
| `yang2024sweagent` | 2024 | [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](#yang2024sweagent) | supporting | metadata+abstract | 新增 key |
| `wu2024autogen` | 2024 | [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversations](#wu2024autogen) | supporting | metadata+abstract | 新增 key |
| `schick2023toolformer` | 2023 | [Toolformer: Language Models Can Teach Themselves to Use Tools](#schick2023toolformer) | optional | metadata+abstract | 新增 key |
| `madaan2023selfrefine` | 2023 | [Self-Refine: Iterative Refinement with Self-Feedback](#madaan2023selfrefine) | supporting | metadata+abstract | 新增 key |
| `liu2024lostmiddle` | 2024 | [Lost in the Middle: How Language Models Use Long Contexts](#liu2024lostmiddle) | supporting | metadata+abstract | 新增 key |
| `robertson2009bm25` | 2009 | [The Probabilistic Relevance Framework: BM25 and Beyond](#robertson2009bm25) | core | metadata+abstract | 新增 key |
| `karpukhin2020dpr` | 2020 | [Dense Passage Retrieval for Open-Domain Question Answering](#karpukhin2020dpr) | supporting | metadata+abstract | 新增 key |

## 编译器、运行库和 ISA/ABI 官方文档

33 项。专题说明：[notes/official-docs.md](notes/official-docs.md)。

| Key | 年份 | 候选条目 | 优先级 | 核验深度 | 与现有 refs 的关系 |
| --- | --- | --- | --- | --- | --- |
| `gcc15instrumentation` | 2025 | [GCC 15.2: Instrumentation Options](#gcc15instrumentation) | core | official-doc | 新增 key |
| `gcc15commonfunctionattrs` | 2025 | [GCC 15.2: Common Function Attributes](#gcc15commonfunctionattrs) | supporting | official-doc | 新增 key |
| `gcc15commonvariableattrs` | 2025 | [GCC 15.2: Common Variable Attributes](#gcc15commonvariableattrs) | supporting | official-doc | 新增 key |
| `gcc15codegen` | 2025 | [GCC 15.2: Code Generation Options](#gcc15codegen) | supporting | official-doc | 新增 key |
| `gcc15staticanalysis` | 2025 | [GCC 15.2: Static Analyzer Options](#gcc15staticanalysis) | supporting | official-doc | 新增 key |
| `gcc15optimize` | 2025 | [GCC 15.2: Optimize Options](#gcc15optimize) | supporting | official-doc | 新增 key |
| `clangcfi` | 滚动/未定 | [Clang: Control Flow Integrity](#clangcfi) | core | official-doc | 新增 key |
| `clangcfidesign` | 滚动/未定 | [Clang: Control Flow Integrity Design Documentation](#clangcfidesign) | supporting | official-doc | 新增 key |
| `clangsafestack` | 滚动/未定 | [Clang: SafeStack](#clangsafestack) | supporting | official-doc | 新增 key |
| `clangshadowcallstack` | 滚动/未定 | [Clang: ShadowCallStack](#clangshadowcallstack) | supporting | official-doc | 新增 key |
| `clangasan` | 滚动/未定 | [Clang: AddressSanitizer](#clangasan) | supporting | official-doc | 新增 key |
| `clangmsan` | 滚动/未定 | [Clang: MemorySanitizer](#clangmsan) | supporting | official-doc | 新增 key |
| `clangubsan` | 滚动/未定 | [Clang: UndefinedBehaviorSanitizer](#clangubsan) | supporting | official-doc | 新增 key |
| `clanghwasan` | 滚动/未定 | [Clang: Hardware-assisted AddressSanitizer Design](#clanghwasan) | supporting | official-doc | 新增 key |
| `clangslh` | 滚动/未定 | [LLVM: Speculative Load Hardening](#clangslh) | supporting | official-doc | 新增 key |
| `clangattrs` | 滚动/未定 | [Clang: Attribute Reference](#clangattrs) | supporting | official-doc | 新增 key |
| `llvmreflang` | 滚动/未定 | [LLVM Language Reference Manual](#llvmreflang) | core | official-doc | 新增 key |
| `llvmub` | 滚动/未定 | [LLVM IR Undefined Behavior Manual](#llvmub) | core | official-doc | 新增 key |
| `llvmcodegen` | 滚动/未定 | [The LLVM Target-Independent Code Generator](#llvmcodegen) | supporting | official-doc | 新增 key |
| `llvmtestguide` | 滚动/未定 | [LLVM Testing Infrastructure Guide](#llvmtestguide) | supporting | official-doc | 新增 key |
| `glibcfortify` | 滚动/未定 | [The GNU C Library: Source Fortification](#glibcfortify) | core | official-doc | 新增 key |
| `glibcerase` | 滚动/未定 | [The GNU C Library: Erasing Sensitive Data](#glibcerase) | core | official-doc | 新增 key |
| `arm_aapcs64` | 2025 | [Procedure Call Standard for the Arm 64-bit Architecture (AAPCS64), 2025Q1](#arm_aapcs64) | core | official-doc | 新增 key |
| `arm_sysvabi64` | 2025 | [System V ABI for the Arm 64-bit Architecture, 2025Q1](#arm_sysvabi64) | supporting | official-doc | 新增 key |
| `riscvpsabi` | 滚动/未定 | [RISC-V ABIs Specification, version 2.0-rc0](#riscvpsabi) | supporting | official-doc | 新增 key |
| `loongarchabi` | 滚动/未定 | [LoongArch ELF ABI Specification, version 2.01](#loongarchabi) | supporting | official-doc | 新增 key |
| `loongarchisa` | 滚动/未定 | [LoongArch Reference Manual, Volume 1: Basic Architecture, version 1.10](#loongarchisa) | supporting | official-doc | 新增 key |
| `riscvcfi_raw` | 滚动/未定 | [RISC-V Unprivileged ISA Manual: Control-Flow Integrity](#riscvcfi_raw) | supporting | official-doc | 新增 key |
| `x86psabi` | 滚动/未定 | [System V Application Binary Interface: AMD64 Architecture Processor Supplement](#x86psabi) | supporting | official-doc | 新增 key |
| `clangcsacheckers` | 滚动/未定 | [Clang Static Analyzer: Checker Developer Manual](#clangcsacheckers) | supporting | official-doc | 新增 key |
| `gcctypeattrs` | 2025 | [GCC 15.2: Common Type Attributes](#gcctypeattrs) | supporting | official-doc | 新增 key |
| `gccobjectsize` | 2025 | [GCC 15.2: Object Size Checking](#gccobjectsize) | core | official-doc | 新增 key |
| `gccstrictflex` | 2025 | [GCC 15.2: C Dialect Options](#gccstrictflex) | supporting | official-doc | 新增 key |

## 条目详情：既有 Related Work 与方法基础

<a id="livinskii2020yarpgen"></a>

### Random Testing for C and C++ Compilers with YARPGen

`livinskii2020yarpgen` · 2020 · Proceedings of the ACM on Programming Languages · core

作者/机构：Vsevolod Livinskii; Dmitry Babokin; John Regehr

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §2.1，p2；§3，pp3–4。未通读全文逐句审核或复现实验。

**候选用途**：随机程序生成与差分测试基线；生成策略如何触发优化。

**使用限制**：不能推广为所有版本仅使用差分 oracle；不能声称覆盖所有防御语义。

来源：[raw.githubusercontent.com 1](https://raw.githubusercontent.com/intel/yarpgen/main/papers/yarpgen-ooplsa-2020.pdf) · [doi.org 2](https://doi.org/10.1145/3428264)

标签：compiler-testing, baseline

<a id="livinskii2023loops"></a>

### Fuzzing Loop Optimizations in Compilers for C++ and Data-Parallel Languages

`livinskii2023loops` · 2023 · Proceedings of the ACM on Programming Languages · core

作者/机构：Vsevolod Livinskii; Dmitry Babokin; John Regehr

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §3.1，p4。未通读全文逐句审核或复现实验。

**候选用途**：循环优化测试、预计算结果与差分两类判定。

**使用限制**：适用范围和语言/版本需按论文区分，不能把 v1 的判定描述套到 v2。

来源：[raw.githubusercontent.com 1](https://raw.githubusercontent.com/intel/yarpgen/main/papers/yarpgen-pldi-2023.pdf) · [doi.org 2](https://doi.org/10.1145/3591295)

标签：compiler-testing, baseline

<a id="xia2024fuzz4all"></a>

### Fuzz4All: Universal Fuzzing with Large Language Models

`xia2024fuzz4all` · 2024 · Proceedings of the IEEE/ACM 46th International Conference on Software Engineering · core

作者/机构：Chunqiu Steven Xia; Matteo Paltenghi; Jia Le Tian; Michael Pradel; Lingming Zhang

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §3.1–3.2.3，pp4–6。未通读全文逐句审核或复现实验。

**候选用途**：文档 autoprompting、LLM 输入生成与变异以及用户可配置 oracle。

**使用限制**：不能写成完全不能使用自定义 oracle，或由 universal 推断覆盖任何安全属性。

来源：[arxiv.org 1](https://arxiv.org/abs/2308.04748) · [doi.org 2](https://doi.org/10.1145/3597503.3639121)

标签：LLM-fuzzing, baseline

<a id="ou2024metamut"></a>

### The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators

`ou2024metamut` · 2024 · Proceedings of the 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 4 · core

作者/机构：Xianfei Ou; Cong Li; Yanyan Jiang; Chang Xu

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §2–3.4，pp2–6。未通读全文逐句审核或复现实验。

**候选用途**：用 LLM 合成可复用、semantic-aware 的编译器变异算子。

**使用限制**：验证/修复步骤不等于每个算子都保持语义或经过充分形式化证明。

来源：[connglli.github.io 1](https://connglli.github.io/pdfs/metamut_asplos24.pdf) · [doi.org 2](https://doi.org/10.1145/3622781.3674171)

标签：compiler-testing, LLM-fuzzing, baseline

<a id="li2024ubfuzz"></a>

### UBFuzz: Finding Bugs in Sanitizer Implementations

`li2024ubfuzz` · 2024 · Proceedings of the 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 1 · core

作者/机构：Shaohua Li; Zhendong Su

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §3.3，pp7–8；§4.1，p8。未通读全文逐句审核或复现实验。

**候选用途**：主动引入 UB 测试 sanitizer，并用 crash-site mapping 区分优化效应与漏报。

**使用限制**：不能称其没有 oracle；测试 sanitizer 的范围不能自动外推到全部编译器防御。

来源：[arxiv.org 1](https://arxiv.org/pdf/2401.04538) · [doi.org 2](https://doi.org/10.1145/3617232.3624874)

标签：sanitizer-testing, baseline

<a id="yang2011csmith"></a>

### Finding and Understanding Bugs in C Compilers

`yang2011csmith` · 2011 · Proceedings of the 32nd ACM SIGPLAN Conference on Programming Language Design and Implementation · core

作者/机构：Xuejun Yang; Yang Chen; Eric Eide; John Regehr

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §2.1–2.2，p2。未通读全文逐句审核或复现实验。

**候选用途**：避免 UB 的随机 C 程序生成和差分执行。

**使用限制**：程序生成约束及执行差异判定不等同于防御机制的安全语义契约。

来源：[users.cs.utah.edu 1](https://users.cs.utah.edu/~regehr/papers/pldi11-preprint.pdf) · [doi.org 2](https://doi.org/10.1145/1993498.1993532)

标签：compiler-testing, baseline

<a id="le2014emi"></a>

### Compiler Validation via Equivalence Modulo Inputs

`le2014emi` · 2014 · Proceedings of the 35th ACM SIGPLAN Conference on Programming Language Design and Implementation · core

作者/机构：Vu Le; Mehrdad Afshari; Zhendong Su

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §3.1–3.2，pp4–5。未通读全文逐句审核或复现实验。

**候选用途**：在指定输入集上构造等价程序变体进行编译器验证。

**使用限制**：输入集约束很关键，不能描述成全输入上的形式化等价证明。

来源：[web.cs.ucdavis.edu 1](https://web.cs.ucdavis.edu/~su/publications/emi.pdf) · [doi.org 2](https://doi.org/10.1145/2594291.2594334)

标签：compiler-testing, metamorphic-testing

<a id="bohme2017aflgo"></a>

### Directed Greybox Fuzzing

`bohme2017aflgo` · 2017 · Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security · core

作者/机构：Marcel Böhme; Van-Thuan Pham; Manh-Dung Nguyen; Abhik Roychoudhury

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §3.2–3.3，pp5–6。未通读全文逐句审核或复现实验。

**候选用途**：面向给定位置的距离反馈和定向灰盒搜索。

**使用限制**：距离反馈不是漏洞或防御正确性的 oracle，也不代表跨目标普遍胜出。

来源：[mboehme.github.io 1](https://mboehme.github.io/paper/CCS17.pdf) · [doi.org 2](https://doi.org/10.1145/3133956.3134020)

标签：fuzzing, directed-fuzzing

<a id="lopes2021alive2"></a>

### Alive2: Bounded Translation Validation for LLVM

`lopes2021alive2` · 2021 · Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation · core

作者/机构：Nuno P. Lopes; Juneyoung Lee; Chung-Kil Hur; Zhengyang Liu; John Regehr

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 abstract p1；§7–8，p9。未通读全文逐句审核或复现实验。

**候选用途**：LLVM IR refinement 与有界翻译验证。

**使用限制**：不能声称对所有循环/后端/硬件或防御性质给出无条件保证。

来源：[web.ist.utl.pt 1](https://web.ist.utl.pt/nuno.lopes/pubs/alive2-pldi21.pdf) · [doi.org 2](https://doi.org/10.1145/3453483.3454030)

标签：compiler-validation, formal-methods

<a id="liu2025propertygpt"></a>

### PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation

`liu2025propertygpt` · 2025 · Proceedings of the 2025 Network and Distributed System Security Symposium · core

作者/机构：Ye Liu; Yue Xue; Daoyuan Wu; Yuqiang Sun; Yi Li; Miaolei Shi; Yang Liu

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §V–VI，pp5–7；§VIII-F p13。未通读全文逐句审核或复现实验。

**候选用途**：检索辅助属性生成，以及 prover 检查合约是否满足给定属性。

**使用限制**：证明给定属性不证明生成属性完整表达用户或规范意图。

来源：[arxiv.org 1](https://arxiv.org/pdf/2405.02580) · [doi.org 2](https://doi.org/10.14722/ndss.2025.241357)

标签：LLM-specification, formal-methods

<a id="wang2013stack"></a>

### Towards Optimization-Safe Systems: Analyzing the Impact of Undefined Behavior

`wang2013stack` · 2013 · Proceedings of the Twenty-Fourth ACM Symposium on Operating Systems Principles · core

作者/机构：Xi Wang; Nickolai Zeldovich; M. Frans Kaashoek; Armando Solar-Lezama

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §3.1–3.2，p5。未通读全文逐句审核或复现实验。

**候选用途**：应用依赖 UB 而出现 optimization-unstable code 的问题与分析。

**使用限制**：不能把全部此类现象归为编译器违反语言语义的实现 bug。

来源：[pdos.csail.mit.edu 1](https://pdos.csail.mit.edu/papers/stack:sosp13.pdf) · [doi.org 2](https://doi.org/10.1145/2517349.2522728)

标签：undefined-behavior, motivation

<a id="wang2026bulbasaur"></a>

### Bulbasaur: Branch-Guided Online Mutator Generation for Greybox Fuzzing

`wang2026bulbasaur` · 2026 · 35th USENIX Security Symposium (USENIX Security 26) · core

作者/机构：Yiyi Wang; Dongsong Yu; Ruiqi Dong; Yiyang Chen; Xiaogang Zhu; Chao Zhang

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §3.1–3.3，pp5–7。未通读全文逐句审核或复现实验。

**候选用途**：利用分支源码上下文和运行反馈在线生成分支专用 mutators。

**使用限制**：对象为一般软件灰盒测试；不能改述成专门的编译器或防御测试工具。

来源：[www.usenix.org 1](https://www.usenix.org/system/files/usenixsecurity26-wang-yiyi.pdf) · [www.usenix.org 2](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-yiyi)

标签：LLM-fuzzing, feedback

<a id="yang2024whitefox"></a>

### WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models

`yang2024whitefox` · 2024 · Proceedings of the ACM on Programming Languages · core

作者/机构：Chenyuan Yang; Yinlin Deng; Runyu Lu; Jiayi Yao; Jiawei Liu; Reyhaneh Jabbarvand; Lingming Zhang

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §3.1 p7；§3.3 p10；§3.4 pp12–13；§7.2 p22。未通读全文逐句审核或复现实验。

**候选用途**：从源码提炼优化触发要求，分离分析与生成，并利用优化触发反馈。

**使用限制**：不能称只测 DL 编译器；源码引导或分析/生成角色分工并非本项目独有。

来源：[arxiv.org 1](https://arxiv.org/pdf/2310.15991) · [doi.org 2](https://doi.org/10.1145/3689736)

标签：compiler-testing, LLM-fuzzing

<a id="yang2025knighter"></a>

### KNighter: Transforming Static Analysis with LLM-Synthesized Checkers

`yang2025knighter` · 2025 · Proceedings of the ACM SIGOPS 31st Symposium on Operating Systems Principles · core

作者/机构：Chenyuan Yang; Zijie Zhao; Zichen Xie; Haoyu Li; Lingming Zhang

**核验深度**：`metadata+method`。沿用 2026-11-11/12 的原文核验；选择性阅读 §3.1 p5；§3.1.4–3.2 p6；§5.4.1 p11。未通读全文逐句审核或复现实验。

**候选用途**：从补丁合成 CSA checker，并进行修复前后验证及 triage/refinement。

**使用限制**：可编译或通过单组修复前后对照，不构成检查器的一般语义正确性证明。

来源：[arxiv.org 1](https://arxiv.org/pdf/2503.09002) · [doi.org 2](https://doi.org/10.1145/3731569.3764827)

标签：LLM-analysis, checker-generation

<a id="silentbugs2023"></a>

### Silent Bugs Matter: A Study of Compiler-Introduced Security Bugs

`silentbugs2023` · 2023 · 32nd USENIX Security Symposium (USENIX Security 23) · core

作者/机构：Jianhao Xu; Kangjie Lu; Zhengjie Du; Zhu Ding; Linke Li; Qiushi Wu; Mathias Payer; Bing Mao

**核验深度**：`metadata+abstract`。已核对一手出版/作者页面的元数据并阅读摘要；未通读全文或复现实验。

**候选用途**：作为 compiler-introduced security bugs 与编译器/用户安全预期差距的动机文献。

**使用限制**：此类安全问题不全是违反语言语义的编译器实现 bug；具体分类与数量须再核对正文。

来源：[www.usenix.org 1](https://www.usenix.org/conference/usenixsecurity23/presentation/xu-jianhao)

标签：compiler-security, motivation

<a id="liu2025agentfuzz"></a>

### Make Agent Defeat Agent: Automatic Detection of Taint-Style Vulnerabilities in LLM-based Agents

`liu2025agentfuzz` · 2025 · 34th USENIX Security Symposium (USENIX Security 25) · optional

作者/机构：Fengyu Liu; Yuan Zhang; Jiaqi Luo; Jiarun Dai; Tian Chen; Letian Yuan; Zhengmin Yu; Youkun Shi; Ke Li; Chengyuan Zhou; Hao Chen; Min Yang

**核验深度**：`metadata+abstract`。已核对一手出版/作者页面的元数据并阅读摘要；未通读全文或复现实验。

**候选用途**：LLM-agent 应用测试中结合语义及距离反馈的邻近工作，可用于反馈设计背景。

**使用限制**：测试对象是 LLM-agent 应用；不应列为编译器防御测试的直接同类基线。

来源：[www.usenix.org 1](https://www.usenix.org/conference/usenixsecurity25/presentation/liu-fengyu)

标签：LLM-agents, testing

<a id="lin2026specauditor"></a>

### SpecAuditor: Generating Audit Specifications for LLM-Driven Bug Detection

`lin2026specauditor` · 2026 · 2026 IEEE Symposium on Security and Privacy (SP) · core

作者/机构：Miaoqian Lin; Hao Chen

**核验深度**：`metadata-only`。仅确认题名、署名和出版记录；尚未取得或阅读可靠原文摘要/方法。

**候选用途**：优先补读：题名与本项目的审计规格生成/LLM bug detection 讨论相关。

**使用限制**：仅依据官方录用列表确认身份；未读摘要/方法，不能描述具体算法、实验表现或优劣。

来源：[sp2026.ieee-security.org 1](https://sp2026.ieee-security.org/accepted-papers.html#collapse-212)

标签：LLM-specification, to-read

<a id="su2026cill"></a>

### CIll: CTI-Guided Invariant Generation via LLMs for Model Checking

`su2026cill` · 2026 · arXiv preprint · supporting

作者/机构：Yuheng Su; Tianjun Bu; Qiusong Yang; Yiwei Ci; Enyuan Tian

**核验深度**：`metadata+abstract`。已核对一手出版/作者页面的元数据并阅读摘要；未通读全文或复现实验。

**候选用途**：CTI 引导不变量生成、模型检查与归纳性检查的邻近工作。

**使用限制**：预印本；形式化模型中的检查不能证明生成的编译器防御规则自动正确。

来源：[arxiv.org 1](https://arxiv.org/abs/2602.23389)

标签：LLM-specification, invariant-generation, preprint

<a id="wei2022chain"></a>

### Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

`wei2022chain` · 2022 · Advances in Neural Information Processing Systems · supporting

作者/机构：Jason Wei; Xuezhi Wang; Dale Schuurmans; Maarten Bosma; Brian Ichter; Fei Xia; Ed Chi; Quoc V Le; Denny Zhou

**核验深度**：`metadata+abstract`。已核对一手出版/作者页面的元数据并阅读摘要；未通读全文或复现实验。

**候选用途**：LLM 推理提示方法背景。

**使用限制**：推理基准上的改善不构成程序/检查器正确性保证。

来源：[papers.nips.cc 1](https://papers.nips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html)

标签：LLM-foundation

<a id="lewis2020retrieval"></a>

### Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

`lewis2020retrieval` · 2020 · Advances in Neural Information Processing Systems · supporting

作者/机构：Patrick Lewis; Ethan Perez; Aleksandra Piktus; Fabio Petroni; Vladimir Karpukhin; Naman Goyal; Heinrich Küttler; Mike Lewis; Wen-tau Yih; Tim Rocktäschel; Sebastian Riedel; Douwe Kiela

**核验深度**：`metadata+abstract`。已核对一手出版/作者页面的元数据并阅读摘要；未通读全文或复现实验。

**候选用途**：检索与生成结合的方法背景。

**使用限制**：检索增强不能保证检索内容版本正确、生成结果符合规范或没有幻觉。

来源：[papers.nips.cc 1](https://papers.nips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)

标签：LLM-foundation

<a id="lattner2004llvm"></a>

### LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation

`lattner2004llvm` · 2004 · Proceedings of the 2004 International Symposium on Code Generation and Optimization (CGO) · supporting

作者/机构：Chris Lattner; Vikram Adve

**核验深度**：`metadata+abstract`。已核对一手出版/作者页面的元数据并阅读摘要；未通读全文或复现实验。

**候选用途**：LLVM 框架、SSA 表示及跨阶段分析/变换的背景引用。

**使用限制**：2004 年框架论文不能用于证明当前版本的防御支持或后端实现正确性。

来源：[llvm.org 1](https://llvm.org/pubs/2004-01-30-CGO-LLVM.html)

标签：compiler-infrastructure

<a id="demoura2008z3"></a>

### Z3: An Efficient SMT Solver

`demoura2008z3` · 2008 · Tools and Algorithms for the Construction and Analysis of Systems (TACAS) · supporting

作者/机构：Leonardo de Moura; Nikolaj Bjørner

**核验深度**：`metadata-only`。仅确认题名、署名和出版记录；尚未取得或阅读可靠原文摘要/方法。

**候选用途**：SMT solver 背景候选；正式引述能力或实验时需补读原文/对应版本文档。

**使用限制**：本轮只读取出版方登记的 Crossref 元数据，没有取得摘要/全文，不据此推导工具能力。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1007%2F978-3-540-78800-3_24)

标签：SMT, formal-methods

<a id="langgraph"></a>

### LangGraph

`langgraph` · 发表年未核定/滚动文档 · Official software repository · optional

作者/机构：LangChain

**核验深度**：`official-doc`。已读取官方项目入口和说明；未核验本项目的依赖版本。

**候选用途**：Agent 编排软件的候选背景引用；仅在论文实现确实使用时引用对应版本。

**使用限制**：不是学术算法论文；本轮未核对 DeFuzz 的依赖文件或固定版本，不凭此声称实际使用。

来源：[github.com 1](https://github.com/langchain-ai/langgraph)

标签：software, agent-orchestration

## 条目详情：编译器测试、验证、评测与缩减

<a id="pnueli1998translationvalidation"></a>

### Translation Validation

`pnueli1998translationvalidation` · 1998 · TACAS 1998 · core

作者/机构：A. Pnueli; M. Siegel; E. Singerman

**核验深度**：`metadata+method`。已读Springer摘要、正式PDF首页及Introduction；正式出版年1998，网页First Online 2006不是论文年份。作者忠实保留原发表署名。

**候选用途**：支持逐次验证编译结果、共同语义框架和refinement的历史来源；与证明整个编译器的路线区分。

**使用限制**：本文实例为SIGNAL到C，不能据此声称任意编译器后端或安全机制已有端到端保证；未将作者首字母臆造展开。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1007/BFb0054170) · [link.springer.com 2](https://link.springer.com/chapter/10.1007/BFb0054170) · [link.springer.com 3](https://link.springer.com/content/pdf/10.1007/BFb0054170.pdf)

标签：translation-validation, refinement, background

<a id="claessen2000quickcheck"></a>

### QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs

`claessen2000quickcheck` · 2000 · ICFP 2000 · supporting

作者/机构：Koen Claessen; John Hughes

**核验深度**：`metadata+abstract`。已读出版社SIGPLAN重印的完整摘要，并核对ICFP正式论文DOI、作者、题名与副题。

**候选用途**：支持将性质写为可执行函数并在随机输入上测试，以及自定义生成器与性质判据相分离的经典先例。

**使用限制**：测试给定性质不证明性质符合需求，也不构成程序普遍正确性证明；不能将可执行predicate本身称为形式化证明。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/351240.351266) · [api.crossref.org 2](https://api.crossref.org/works/10.1145/357766.351266)

标签：property-based-testing, random-testing, oracle

<a id="zeller2002deltadebugging"></a>

### Simplifying and Isolating Failure-Inducing Input

`zeller2002deltadebugging` · 2002 · IEEE Transactions on Software Engineering 28(2), 2002 · core

作者/机构：Andreas Zeller; Ralf Hildebrandt

**核验深度**：`metadata+method`。已读作者正式论文PDF首页、摘要与Introduction，核对作者全名及dd/ddmin区别；出版社元数据用于正式页码和DOI。

**候选用途**：支持保持失败条件的测试缩减和通过/失败输入之间差异隔离；用于解释最小案例产出与后续确认的分工。

**使用限制**：ddmin的局部最小性不等于全局最小；缩减保留的是给定测试判据，不证明该判据语义正确。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1109/32.988498) · [www.st.cs.uni-saarland.de 2](https://www.st.cs.uni-saarland.de/papers/tse2002/tse2002.pdf)

标签：test-reduction, delta-debugging, oracle

<a id="ernst2007daikon"></a>

### The Daikon system for dynamic detection of likely invariants

`ernst2007daikon` · 2007 · Science of Computer Programming 69, 2007 · core

作者/机构：Michael D. Ernst; Jeff H. Perkins; Philip J. Guo; Stephen McCamant; Carlos Pacheco; Matthew S. Tschantz; Chen Xiao

**核验深度**：`metadata+method`。已读作者正式PDF首页、摘要、Introduction与示例前半部分；核对全部作者、正式期刊年份及DOI。

**候选用途**：支持从执行观测推断likely invariants，与从文档/历史推断规格形成可比较路线；提醒观测成立和规范性正确应分开。

**使用限制**：likely invariant由已观察轨迹支持，不是普遍语义定理或安全意图证明；不能把动态统计推断与形式化验证混称。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1016/j.scico.2007.01.015) · [homes.cs.washington.edu 2](https://homes.cs.washington.edu/~mernst/pubs/daikon-tool-scp2007.pdf)

标签：invariant-inference, specification-mining, dynamic-analysis, oracle

<a id="leroy2009compcert"></a>

### Formal verification of a realistic compiler

`leroy2009compcert` · 2009 · Communications of the ACM 52(7), 2009 · core

作者/机构：Xavier Leroy

**核验深度**：`metadata+abstract`。已读出版社登记的完整摘要，核对作者、正式年份、卷期、页码与DOI。

**候选用途**：支持区分编译器验证、具体翻译验证和测试；CompCert以Coq证明Clight到PowerPC的语义保持。

**使用限制**：限于该论文所覆盖的语言、目标和证明边界。摘要明确提到源程序已证明安全性质向目标代码传递，不能写成形式化编译器验证完全不涉及安全。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Formal%20verification%20of%20a%20realistic%20compiler&rows=2)

标签：compiler-verification, semantic-preservation, background

<a id="holler2012langfuzz"></a>

### Fuzzing with Code Fragments

`holler2012langfuzz` · 2012 · USENIX Security 2012 · supporting

作者/机构：Christian Holler; Kim Herzig; Andreas Zeller

**核验深度**：`metadata+abstract`。已读USENIX官方页完整摘要、作者列表及官方BibTeX，核对出版年和页码。

**候选用途**：支持语法生成与既有代码片段重用结合的输入生成路线，补足LLM前的语言测试生成背景。

**使用限制**：语言引擎测试生成方法不等于编译器防御契约检查；语法有效和片段重用也不自动保证完整程序无语义错误。

来源：[www.usenix.org 1](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/holler)

标签：generation, grammar, javascript, fuzzing

<a id="regehr2012creduce"></a>

### Test-Case Reduction for C Compiler Bugs

`regehr2012creduce` · 2012 · PLDI 2012 · core

作者/机构：John Regehr; Yang Chen; Pascal Cuoq; Eric Eide; Chucky Ellison; Xuejun Yang

**核验深度**：`metadata+abstract`。已读出版社SIGPLAN重印完整摘要，与PLDI正式记录核对；此条是正式论文，区别既有refs.bib的C-Reduce项目网页。

**候选用途**：支持编译器测试缩减需要语言相关变换，普通文本delta debugging可能保留过大或依赖UB的案例。

**使用限制**：C-Reduce依赖interestingness test，不能把缩减完成解释成自动证明程序无UB或缺陷已确认；本条不是对既有creduce网页条目的自动替换。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Test-case%20reduction%20for%20C%20compiler%20bugs&rows=2)

标签：test-reduction, compiler-testing, undefined-behavior

<a id="le2015athena"></a>

### Finding Deep Compiler Bugs via Guided Stochastic Program Mutation

`le2015athena` · 2015 · OOPSLA 2015 · core

作者/机构：Vu Le; Chengnian Sun; Zhendong Su

**核验深度**：`metadata+abstract`。已读出版社SIGPLAN重印摘要；与正式OOPSLA会议记录匹配题名、完整作者列表、年份和页码。

**候选用途**：支持EMI由Orion删死代码扩展至Athena插入/删除未执行代码，并用控制流多样性目标引导随机搜索的演进。

**使用限制**：等价仅针对给定输入；不是全输入语义等价，也不直接证明安全防御契约。没有复现实验或重新核验所报bug数量。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Finding%20Deep%20Compiler%20Bugs%20via%20Guided%20Stochastic%20Program%20Mutation&rows=2)

标签：compiler-testing, emi, metamorphic-testing, mutation

<a id="lidbury2015clsmith"></a>

### Many-Core Compiler Fuzzing

`lidbury2015clsmith` · 2015 · PLDI 2015 · core

作者/机构：Christopher Lidbury; Andrei Lascu; Nathan Chong; Alastair F. Donaldson

**核验深度**：`metadata+abstract`。已读出版社SIGPLAN重印摘要，并核对同论文的PLDI正式记录。

**候选用途**：支持随机差分与EMI向OpenCL多核环境扩展，生成确定性、可通信kernel，以及增加动态死代码的注入机制。

**使用限制**：涉及多设备配置并不等于具有跨ISA语义或安全契约可比性；不能直接当DeFuzz四ISA实验的统一baseline。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Many-core%20compiler%20fuzzing&rows=3)

标签：compiler-testing, opencl, many-core, differential-testing, emi

<a id="lopes2015alive"></a>

### Provably Correct Peephole Optimizations with Alive

`lopes2015alive` · 2015 · PLDI 2015 · core

作者/机构：Nuno P. Lopes; David Menendez; Santosh Nagarakatte; John Regehr

**核验深度**：`metadata+abstract`。已读同一论文SIGPLAN重印记录的完整摘要，并以会议记录核对正式DOI、作者和页码。

**候选用途**：支持以DSL表达LLVM局部优化、自动证明或产生反例，以及从已验证规则生成实现的前例。

**使用限制**：Alive主要针对所支持的局部优化及其语义模型，不等于验证所有后端防御；不能把整数原版的范围套用为任意浮点优化。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Provably%20correct%20peephole%20optimizations%20with%20Alive&rows=2)

标签：translation-validation, llvm, peephole, oracle

<a id="menendez2016alivefp"></a>

### Alive-FP: Automated Verification of Floating Point Based Peephole Optimizations in LLVM

`menendez2016alivefp` · 2016 · SAS 2016 · supporting

作者/机构：David Menendez; Santosh Nagarakatte; Aarti Gupta

**核验深度**：`metadata+method`。已读Springer原文摘要及Introduction，核对正式作者、出版年、题名、页码和DOI。

**候选用途**：支持浮点优化验证需要明确NaN、有符号零、无穷及fast-math等语义前提，形式化checker的范围受模型约束。

**使用限制**：只覆盖论文声明的一类不会造成精度损失的浮点/fast-math优化，不可外推所有浮点近似优化都已得到验证。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Alive-FP%20Automated%20Verification%20of%20Floating%20Point%20Based%20Peephole%20Optimizations&rows=2) · [link.springer.com 2](https://link.springer.com/chapter/10.1007/978-3-662-53413-7_16)

标签：translation-validation, llvm, floating-point, semantic-model

<a id="sun2016hermes"></a>

### Finding Compiler Bugs via Live Code Mutation

`sun2016hermes` · 2016 · OOPSLA 2016 · core

作者/机构：Chengnian Sun; Vu Le; Zhendong Su

**核验深度**：`metadata+abstract`。已读出版社SIGPLAN重印完整摘要，核对正式会议记录；确认工具名Hermes及live/dead两类区域的变异。

**候选用途**：支持EMI不应被一概描述为只能改死代码；Hermes扩展到活代码区域，是Related Work潜在的重要遗漏。

**使用限制**：针对输入集保持等价仍是前提；活代码变异并不自动产生针对编译器防御的专门oracle。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Finding%20compiler%20bugs%20via%20live%20code%20mutation%20Hermes&rows=3)

标签：compiler-testing, emi, metamorphic-testing, live-code-mutation

<a id="donaldson2017glfuzz"></a>

### Automated Testing of Graphics Shader Compilers

`donaldson2017glfuzz` · 2017 · PACMPL 1(OOPSLA), 2017 · supporting

作者/机构：Alastair F. Donaldson; Hugues Evrard; Andrei Lascu; Paul Thomson

**核验深度**：`metadata+abstract`。已读出版社完整摘要，确认GLFuzz、语义等价shader变换、图像差异与自动缩减的描述；核对全部作者和DOI。

**候选用途**：支持当图形结果不完全指定时，metamorphic testing仍可为shader编译器构造实用oracle；说明编译器测试并非只比较整数checksum。

**使用限制**：图像等价/渲染差异的判据依赖该领域设定，不可直接外推为所有安全防御契约oracle；不复用其漏洞或效果数字。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Metamorphic%20Testing%20of%20Graphics%20Shader%20Compilers&rows=2)

标签：compiler-testing, graphics, metamorphic-testing, oracle

<a id="zhang2017spe"></a>

### Skeletal Program Enumeration for Rigorous Compiler Testing

`zhang2017spe` · 2017 · PLDI 2017 · core

作者/机构：Qirun Zhang; Chengnian Sun; Zhendong Su

**核验深度**：`metadata+abstract`。已读作者arXiv v4完整摘要及作者publication页面，正式年份与DOI使用PLDI记录。

**候选用途**：支持在固定语法骨架和变量集合下系统枚举非alpha等价变量使用模式；补足随机生成之外的枚举路线。

**使用限制**：穷举保证受固定骨架与变量集合限定，不能称为穷举所有程序或证明编译器正确。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/3062341.3062379) · [arxiv.org 2](https://arxiv.org/abs/1610.03148) · [people.inf.ethz.ch 3](https://people.inf.ethz.ch/suz/publications/)

标签：compiler-testing, enumeration, generation, coverage

<a id="chen2018metamorphicsurvey"></a>

### Metamorphic Testing: A Review of Challenges and Opportunities

`chen2018metamorphicsurvey` · 2018 · ACM Computing Surveys 51(1), 2018 · core

作者/机构：Tsong Yueh Chen; Fei-Ching Kuo; Huai Liu; Pak-Lok Poon; Dave Towey; T. H. Tse; Zhi Quan Zhou

**核验深度**：`metadata+abstract`。已读出版社登记的完整摘要，核对title与subtitle、全部作者、正式卷期与年份。

**候选用途**：支持metamorphic relation是多输入及期望输出之间的必要性质，兼具测试生成与结果判定角色；可解释关系型oracle。

**使用限制**：关系需符合目标规格，满足关系不代表实现全面正确；本文是综述，不能作为DeFuzz checker正确性的证明。T. H. Tse保留公开发表署名。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/3143561)

标签：metamorphic-testing, oracle, survey

<a id="klees2018fuzzeval"></a>

### Evaluating Fuzz Testing

`klees2018fuzzeval` · 2018 · ACM CCS 2018 · core

作者/机构：George Klees; Andrew Ruef; Benji Cooper; Shiyi Wei; Michael Hicks

**核验深度**：`metadata+method`。已读作者arXiv论文摘要和Introduction（含重复运行、统计检验、基准/种子/预算敏感性及ground truth讨论），正式出版元数据与CCS匹配。

**候选用途**：支持重复实验、合理baseline、代表性基准、固定资源、统计检验和以真实bug而非原始crash计数评价。

**使用限制**：不应从该文机械推出某个统一运行次数或时长适合所有DeFuzz实验；其对既有论文的结论属于当年的样本范围。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/3243734.3243804) · [arxiv.org 2](https://arxiv.org/pdf/1808.09700)

标签：fuzzing-evaluation, statistics, benchmark, metrics

<a id="sun2018perses"></a>

### Perses: Syntax-Guided Program Reduction

`sun2018perses` · 2018 · ICSE 2018 · supporting

作者/机构：Chengnian Sun; Yuanbo Li; Qirun Zhang; Tianxiao Gu; Zhendong Su

**核验深度**：`metadata+method`。已读作者官方仓库所附ICSE正式PDF摘要和Introduction，以及README；论文全题名由PDF补全出版社只保留Perses的短title。

**候选用途**：支持用输入语法避免大量语法无效的缩减候选，以及通用reducer与性质判据之间的接口。

**使用限制**：语法有效不等于语义有效或不含UB；性质保持依赖外部测试脚本，不能据此证明oracle正确。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/3180155.3180236) · [raw.githubusercontent.com 2](https://raw.githubusercontent.com/perses-project/perses/master/doc/publication/2018_perses_icse.pdf) · [raw.githubusercontent.com 3](https://raw.githubusercontent.com/perses-project/perses/master/README.md)

标签：test-reduction, syntax-guided, language-agnostic

<a id="gharachorlu2019pardis"></a>

### Pardis: Priority Aware Test Case Reduction

`gharachorlu2019pardis` · 2019 · FASE 2019 · optional

作者/机构：Golnaz Gharachorlu; Nick Sumner

**核验深度**：`metadata+method`。已读Springer全文摘要和Introduction以及正式PDF首页；PDF确认工具名Pardis，修正出版社文本元数据遗漏的图片标题。

**候选用途**：支持结构化缩减中的优先级反转会影响效率，作为reduction成本与实现设计的补充背景。

**使用限制**：相对Perses的效率数字依赖论文同组基准与设置；不可宣称对所有语言/缺陷普遍更快。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Pardis%20Priority%20Aware%20Test%20Case%20Reduction&rows=2) · [link.springer.com 2](https://link.springer.com/chapter/10.1007/978-3-030-16722-6_24) · [link.springer.com 3](https://link.springer.com/content/pdf/10.1007/978-3-030-16722-6_24.pdf)

标签：test-reduction, priority, efficiency

<a id="hazimeh2020magma"></a>

### Magma: A Ground-Truth Fuzzing Benchmark

`hazimeh2020magma` · 2020 · PACM on Measurement and Analysis of Computing Systems 4(3), 2020 · core

作者/机构：Ahmad Hazimeh; Adrian Herrera; Mathias Payer

**核验深度**：`metadata+method`。已读完整论文的作者arXiv摘要、Introduction与指标问题讨论，并核对2020完整期刊论文DOI；排除2021两页会议摘要版本。

**候选用途**：支持区分bug reached、triggered、detected；说明crash去重和覆盖率不足以替代真实bug ground truth。

**使用限制**：Magma自身是特定应用及历史bug基准，不可直接当作DeFuzz防御缺陷的ground truth；也不支持覆盖率与任何任务效果完全无关的极端说法。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/3428334) · [arxiv.org 2](https://arxiv.org/pdf/2009.01120)

标签：fuzzing-evaluation, ground-truth, benchmark, metrics

<a id="park2020die"></a>

### Fuzzing JavaScript Engines with Aspect-preserving Mutation

`park2020die` · 2020 · IEEE Symposium on Security and Privacy 2020 · supporting

作者/机构：Soyeon Park; Wen Xu; Insu Yun; Daehee Jang; Taesoo Kim

**核验深度**：`metadata+method`。已读作者托管正式论文首页摘要与Introduction，核对出版社正式年份、题名、作者、页码。

**候选用途**：支持随机变异保留类型和结构等有利于触发深层JIT行为的特征，说明输入多样性与保留触发条件之间的权衡。

**使用限制**：aspect-preserving指概率性保留特征，不是严格保语义或形式化证明；JavaScript引擎结果不能直接视为LLVM/GCC防御检查效果。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Fuzzing%20JavaScript%20Engines%20with%20Aspect-preserving%20Mutation&rows=3) · [taesoo.kim 2](https://taesoo.kim/pubs/2020/park:die.pdf)

标签：jit, javascript, mutation, generation

<a id="manes2021fuzzingsurvey"></a>

### The Art, Science, and Engineering of Fuzzing: A Survey

`manes2021fuzzingsurvey` · 2021 · IEEE Transactions on Software Engineering 47(11), 2021 · supporting

作者/机构：Valentin J.M. Manes; HyungSeok Han; Choongwoo Han; Sang Kil Cha; Manuel Egele; Edward J. Schwartz; Maverick Woo

**核验深度**：`metadata+abstract`。已读作者arXiv v4完整摘要并核对IEEE正式卷期页码；正式发表年2021，区别预印本2018及early-access DOI中的2019。

**候选用途**：支持fuzzing的一般模型及各阶段设计分类，用于Background组织输入生成、执行、反馈与结果判定。

**使用限制**：这是综述及分类参考，不能为DeFuzz具体性能或首创性直接背书；本文arXiv曾标注投ACM CSUR但正式载体是IEEE TSE。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Fuzzing%20Art%20Science%20and%20Engineering&rows=2) · [arxiv.org 2](https://arxiv.org/abs/1812.00140)

标签：fuzzing, survey, taxonomy, background

<a id="metzman2021fuzzbench"></a>

### FuzzBench: An Open Fuzzer Benchmarking Platform and Service

`metzman2021fuzzbench` · 2021 · ESEC/FSE 2021 Industry Track · core

作者/机构：Jonathan Metzman; László Szekeres; Laurent Simon; Read Sprabery; Abhishek Arya

**核验深度**：`metadata+abstract`。已读Google Research官方论文摘要及官方仓库README，并核对正式会议作者、年份、页码与DOI。

**候选用途**：支持可重现的大规模fuzzer比较平台、统一集成接口和统计报告的实验组织思路。

**使用限制**：使用FuzzBench不自动保证DeFuzz编译器/防御任务公平；样本README的24小时20次配置只是示例，不能据此宣称是统一必需标准。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/3468264.3473932) · [research.google 2](https://research.google/pubs/fuzzbench-an-open-fuzzer-benchmarking-platform-and-service/) · [raw.githubusercontent.com 3](https://raw.githubusercontent.com/google/fuzzbench/master/README.md)

标签：fuzzing-evaluation, benchmark, reproducibility, infrastructure

<a id="gross2023fuzzilli"></a>

### FUZZILLI: Fuzzing for JavaScript JIT Compiler Vulnerabilities

`gross2023fuzzilli` · 2023 · NDSS 2023 · supporting

作者/机构：Samuel Groß; Simon Koch; Lukas Bernhard; Thorsten Holz; Martin Johns

**核验深度**：`metadata+abstract`。已读NDSS官方论文页完整摘要及作者列表，并核对出版社DOI记录。

**候选用途**：支持专门设计中间表示以生成能触发JIT语义的输入；用于讨论到达编译阶段需要结构化输入。

**使用限制**：不能将其JIT漏洞目标等同编译器静态防御契约验证；官方摘要的首创/覆盖声明仅属该论文自身范围，不据此排除所有先前方法。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=JIT-Picking%20Differential%20Fuzzing%20of%20JavaScript%20Engines&rows=2) · [www.ndss-symposium.org 2](https://www.ndss-symposium.org/ndss-paper/fuzzilli-fuzzing-for-javascript-jit-compiler-vulnerabilities/)

标签：jit, javascript, intermediate-representation, generation

## 条目详情：编译器防御与安全语义

<a id="abadi2009cfi"></a>

### Control-flow integrity principles, implementations, and applications

`abadi2009cfi` · 2009 · ACM Transactions on Information and System Security · core

作者/机构：Martín Abadi; Mihai Budiu; Úlfar Erlingsson; Jay Ligatti

**核验深度**：`metadata+abstract`。核对出版方登记的 Crossref 题名、作者、年份、venue、DOI，并阅读同一记录的完整摘要；未通读全文或复现实验。

**候选用途**：用于定义 CFI 的基本策略、控制流约束及其与影子调用栈的联系。

**使用限制**：此条为 2009 年扩展期刊版，不能写成 CFI 首次提出于 2009 年；安全保证依赖论文策略与威胁模型，不代表所有实际 CFI 实现都阻止全部控制流攻击。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/1609956.1609960)

标签：CFI, foundation

<a id="burow2017cfisurvey"></a>

### Control-Flow Integrity: Precision, Security, and Performance

`burow2017cfisurvey` · 2017 · ACM Computing Surveys · core

作者/机构：Nathan Burow; Scott A. Carr; Joseph Nash; Per Larsen; Michael Franz; Stefan Brunthaler; Mathias Payer

**核验深度**：`metadata+abstract`。核对 Crossref 出版元数据及完整摘要，并阅读作者公开稿的署名、摘要与引言；作者稿保留占位 DOI/卷期，最终元数据以出版登记为依据；未通读全文或复现实验。

**候选用途**：用于组织 CFI 精度、安全性、性能和前向/后向边比较维度。

**使用限制**：该综述反映当时系统；不能据此概括所有 2026 年编译器实现，论文性能数字也不能直接充当 DeFuzz baseline。 2017 为首次在线发表年；Crossref 另列 2018 印刷日期，二者不是两项独立研究。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/3054924) · [hexhive.epfl.ch 2](https://hexhive.epfl.ch/publications/files/17CSUR.pdf)

标签：CFI, survey

<a id="cowan1998stackguard"></a>

### StackGuard: Automatic Adaptive Detection and Prevention of Buffer-Overflow Attacks

`cowan1998stackguard` · 1998 · 7th USENIX Security Symposium · core

作者/机构：Crispin Cowan; Calton Pu; Dave Maier; Heather Hinton; Jonathan Walpole; Peat Bakke; Steve Beattie; Aaron Grier; Perry Wagle; Qian Zhang

**核验深度**：`metadata+abstract`。阅读 USENIX 原始 PDF 的正文题名、作者、摘要与引言；作者顺序取正文署名而非归档封面；未通读全文或复现实验。

**候选用途**：用于交代编译器插入栈保护的历史及 canary 机制的背景。

**使用限制**：历史原型不等同于当前 GCC/LLVM stack protector；不能表述为检测一切栈越界或内存破坏。

来源：[www.usenix.org 1](https://www.usenix.org/legacy/publications/library/proceedings/sec98/full_papers/cowan/cowan.pdf)

标签：stack-protector, canary, foundation

<a id="kuznetsov2014cpi"></a>

### Code-Pointer Integrity

`kuznetsov2014cpi` · 2014 · 11th USENIX Symposium on Operating Systems Design and Implementation (OSDI 14) · core

作者/机构：Volodymyr Kuznetsov; Laszlo Szekeres; Mathias Payer; George Candea; R. Sekar; Dawn Song

**核验深度**：`metadata+abstract`。阅读 USENIX 官方页面的完整摘要与官方 BibTeX；未通读全文或复现实验。

**候选用途**：用于介绍代码指针保护、CPI/CPS 及安全栈分离相关设计背景。

**使用限制**：需区分论文的 CPI、较弱 CPS 与具体 SafeStack 实现；不能把整篇 CPI 的保证直接赋给当前 LLVM SafeStack。

来源：[www.usenix.org 1](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/kuznetsov)

标签：CPI, CPS, SafeStack, pointer-integrity

<a id="tice2014forwardcfi"></a>

### Enforcing Forward-Edge Control-Flow Integrity in GCC & LLVM

`tice2014forwardcfi` · 2014 · 23rd USENIX Security Symposium (USENIX Security 14) · core

作者/机构：Caroline Tice; Tom Roeder; Peter Collingbourne; Stephen Checkoway; Úlfar Erlingsson; Luis Lozano; Geoff Pike

**核验深度**：`metadata+abstract`。阅读 USENIX 官方页面的完整摘要与官方 BibTeX；未通读全文或复现实验。

**候选用途**：用于说明生产编译器中的前向边 CFI 及增量编译、动态库等兼容性约束。

**使用限制**：研究对象是当时实现和前向边策略，不证明当前所有 CFI 模式、所有 ISA 或后向边保护均正确。

来源：[www.usenix.org 1](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/tice)

标签：CFI, compiler-hardening, LLVM, GCC

<a id="burow2019shadowstacks"></a>

### SoK: Shining Light on Shadow Stacks

`burow2019shadowstacks` · 2019 · 2019 IEEE Symposium on Security and Privacy (SP) · core

作者/机构：Nathan Burow; Xinping Zhang; Mathias Payer

**核验深度**：`metadata+abstract`。核对 Crossref 出版元数据，并阅读作者公开 PDF 的题名、署名、摘要与引言；未通读全文或复现实验。

**候选用途**：用于讨论后向边保护、影子栈的安全性、性能及兼容性权衡。

**使用限制**：是 IEEE S&P 2019 论文，不是 USENIX；研究结论不能替代当前 Intel CET、Arm GCS 或各编译器实现的文档与测试。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1109/sp.2019.00076) · [hexhive.epfl.ch 2](https://hexhive.epfl.ch/publications/files/19Oakland.pdf)

标签：shadow-stack, backward-edge, survey

<a id="mashtizadeh2015ccfi"></a>

### CCFI: Cryptographically Enforced Control Flow Integrity

`mashtizadeh2015ccfi` · 2015 · Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security · supporting

作者/机构：Ali José Mashtizadeh; Andrea Bittau; Dan Boneh; David Mazières

**核验深度**：`metadata+abstract`。核对 Crossref 元数据并阅读作者公开 PDF 的署名、摘要与引言；未通读全文或复现实验。

**候选用途**：用于补充基于消息认证码的代码指针完整性机制和编译器支持的历史背景。

**使用限制**：论文采用 AES-NI 的 Clang/LLVM 原型；不能等同于 Arm PAC，也不沿用摘要中历史性的“all known attacks”作为今天的无条件结论。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/2810103.2813676) · [www.scs.stanford.edu 2](https://www.scs.stanford.edu/~dm/home/papers/mashtizadeh:ccfi.pdf)

标签：CFI, pointer-integrity, cryptographic

<a id="zhang2016vtrust"></a>

### VTrust: Regaining Trust on Virtual Calls

`zhang2016vtrust` · 2016 · Proceedings 2016 Network and Distributed System Security Symposium · supporting

作者/机构：Chao Zhang; Scott A. Carr; Tongxin Li; Yu Ding; Chengyu Song; Mathias Payer; Dawn Song

**核验深度**：`metadata+abstract`。核对 Crossref 元数据并阅读作者公开 PDF 的署名、摘要与引言；未通读全文或复现实验。

**候选用途**：用于补充针对 C++ 虚调用的类型约束和虚表指针保护设计。

**使用限制**：安全描述须保留虚表只读、论文威胁模型和实现条件；不是一般内存安全保证，也不是所有间接控制转移的全面保护。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.14722/ndss.2016.23164) · [hexhive.epfl.ch 2](https://hexhive.epfl.ch/publications/files/16NDSS.pdf)

标签：CFI, C++, virtual-dispatch

<a id="burow2018cfixx"></a>

### CFIXX: Object Type Integrity for C++

`burow2018cfixx` · 2018 · Proceedings 2018 Network and Distributed System Security Symposium · supporting

作者/机构：Nathan Burow; Derrick McKee; Scott A. Carr; Mathias Payer

**核验深度**：`metadata+abstract`。核对 NDSS DOI 的 Crossref 元数据，并阅读作者公开 PDF 的署名、摘要与引言；记录题名版本差异；未通读全文或复现实验。

**候选用途**：用于说明动态对象类型完整性与静态合法目标集合之间的区别，以及 OTI 对 CFI 的补充。

**使用限制**：Crossref/NDSS DOI 登记题名为 Object Type Integrity for C++，作者 PDF 题名另有 Virtual Dispatch；两者 DOI 相同。本条采用登记题名。论文 OTI 的范围不能扩大为所有 C++ 类型安全。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.14722/ndss.2018.23279) · [hexhive.epfl.ch 2](https://hexhive.epfl.ch/publications/files/18NDSS.pdf)

标签：CFI, OTI, C++

<a id="serebryany2012asan"></a>

### AddressSanitizer: A Fast Address Sanity Checker

`serebryany2012asan` · 2012 · 2012 USENIX Annual Technical Conference (USENIX ATC 12) · core

作者/机构：Konstantin Serebryany; Derek Bruening; Alexander Potapenko; Dmitriy Vyukov

**核验深度**：`metadata+abstract`。阅读 USENIX 官方页面的完整摘要与官方 BibTeX；未通读全文或复现实验。

**候选用途**：用于介绍地址 sanitizer 的编译器插桩、分配器与内存错误检测背景。

**使用限制**：ASan 的内存错误检测不等于证明 sanitizer 自身插桩正确，也不能用未报告错误证明程序完全内存安全。

来源：[www.usenix.org 1](https://www.usenix.org/conference/atc12/technical-sessions/presentation/serebryany)

标签：sanitizer, ASan, memory-safety

<a id="stepanov2015msan"></a>

### MemorySanitizer: Fast Detector of Uninitialized Memory Use in C++

`stepanov2015msan` · 2015 · 2015 IEEE/ACM International Symposium on Code Generation and Optimization (CGO) · core

作者/机构：Evgeniy Stepanov; Konstantin Serebryany

**核验深度**：`metadata+method`。核对 Crossref 出版元数据；阅读 Google sanitizers 官方项目 MemorySanitizer 文档的引言、检测条件、库插桩要求与论文链接；原论文 PDF 未成功取得。

**候选用途**：用于区分未初始化值使用检测与地址越界检测，并记录全栈插桩的实际约束。

**使用限制**：原论文 Google PDF 在本次远端环境下载失败；方法说明来自官方项目文档而非对原论文全文/摘要的阅读，当前文档也不能视为 2015 实现逐项快照。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1109/cgo.2015.7054186) · [raw.githubusercontent.com 2](https://raw.githubusercontent.com/wiki/google/sanitizers/MemorySanitizer.md)

标签：sanitizer, MSan, uninitialized-memory

<a id="nagarakatte2009softbound"></a>

### SoftBound: Highly Compatible and Complete Spatial Memory Safety for C

`nagarakatte2009softbound` · 2009 · Proceedings of the 30th ACM SIGPLAN Conference on Programming Language Design and Implementation · core

作者/机构：Santosh Nagarakatte; Jianzhou Zhao; Milo M. K. Martin; Steve Zdancewic

**核验深度**：`metadata+abstract`。核对会议论文的 Crossref 元数据，并阅读同文 SIGPLAN Notices 版的完整摘要；库内采用会议版 DOI，未将两版作为不同研究计数；未通读全文或复现实验。

**候选用途**：用于介绍通过分离的每指针 base/bound 元数据实施空间内存安全。

**使用限制**：完整检查与仅写检查模式的保证不同；不能把空间安全描述成时间安全，也不应把论文形式化模型直接扩大到任意现代 C/C++ 构建。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/1542476.1542504) · [api.crossref.org 2](https://api.crossref.org/works/10.1145/1543135.1542504)

标签：spatial-safety, bounds, compiler-instrumentation

<a id="nagarakatte2010cets"></a>

### CETS: compiler enforced temporal safety for C

`nagarakatte2010cets` · 2010 · Proceedings of the 2010 international symposium on Memory management · core

作者/机构：Santosh Nagarakatte; Jianzhou Zhao; Milo M. K. Martin; Steve Zdancewic

**核验深度**：`metadata+abstract`。核对会议论文的 Crossref 元数据，并阅读同文 SIGPLAN Notices 版的完整摘要；库内采用会议版 DOI，未将两版作为不同研究计数；未通读全文或复现实验。

**候选用途**：用于介绍对象标识符和指针元数据支持的时间内存安全，与空间安全形成对照。

**使用限制**：摘要中的形式化时间安全保证以不存在空间安全违规为条件；不能省略该前提或将单独 CETS 表述为完整内存安全。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/1806651.1806657) · [api.crossref.org 2](https://api.crossref.org/works/10.1145/1837855.1806657)

标签：temporal-safety, compiler-instrumentation

<a id="akritidis2009baggy"></a>

### Baggy Bounds Checking: An Efficient and Backwards-Compatible Defense against Out-of-Bounds Errors

`akritidis2009baggy` · 2009 · 18th USENIX Security Symposium · supporting

作者/机构：Periklis Akritidis; Manuel Costa; Miguel Castro; Steven Hand

**核验深度**：`metadata+method`。阅读 USENIX 原始 PDF 的署名、摘要、引言及设计开头关于分配边界的定义；未通读全文或复现实验。

**候选用途**：用于说明边界检查中安全粒度、元数据布局与兼容性的设计权衡。

**使用限制**：Baggy 检查的是分配边界，可能允许对象与分配块之间的 padding 访问；不能称为精确的子对象边界检查。

来源：[www.usenix.org 1](https://www.usenix.org/legacy/event/sec09/tech/full_papers/akritidis.pdf)

标签：spatial-safety, bounds

<a id="berger2006diehard"></a>

### DieHard: probabilistic memory safety for unsafe languages

`berger2006diehard` · 2006 · Proceedings of the 27th ACM SIGPLAN Conference on Programming Language Design and Implementation · optional

作者/机构：Emery D. Berger; Benjamin G. Zorn

**核验深度**：`metadata+abstract`。核对会议论文的 Crossref 元数据，并阅读同文 SIGPLAN Notices 版的完整摘要；库内采用会议版 DOI，未将两版作为不同研究计数；未通读全文或复现实验。

**候选用途**：用于补充随机化、冗余与概率性内存安全容错的另一类设计。

**使用限制**：其概率保证与确定性的边界检查不同；不能将容错成功或多副本输出一致写成无漏洞证明。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/1133981.1134000) · [api.crossref.org 2](https://api.crossref.org/works/10.1145/1133255.1134000)

标签：probabilistic-safety, memory-safety

<a id="duck2018effectivesan"></a>

### EffectiveSan: type and memory error detection using dynamically typed C/C++

`duck2018effectivesan` · 2018 · Proceedings of the 39th ACM SIGPLAN Conference on Programming Language Design and Implementation · supporting

作者/机构：Gregory J. Duck; Roland H. C. Yap

**核验深度**：`metadata+abstract`。核对会议论文的 Crossref 元数据，并阅读同文 SIGPLAN Notices 版的完整摘要；库内采用会议版 DOI，未将两版作为不同研究计数；未通读全文或复现实验。

**候选用途**：用于补充动态类型检查、类型元数据和子对象边界检测等 sanitizer 设计维度。

**使用限制**：该方法的覆盖范围、兼容性和开销需按论文实验对象与模式陈述；不能泛称所有 sanitizer 都能检测相同类型/子对象错误。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/3192366.3192388) · [api.crossref.org 2](https://api.crossref.org/works/10.1145/3296979.3192388)

标签：sanitizer, type-safety, subobject-bounds

<a id="haller2016typesan"></a>

### TypeSan: Practical Type Confusion Detection

`haller2016typesan` · 2016 · Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security · supporting

作者/机构：Istvan Haller; Yuseok Jeon; Hui Peng; Mathias Payer; Cristiano Giuffrida; Herbert Bos; Erik van der Kouwe

**核验深度**：`metadata+abstract`。核对 ACM/Crossref 元数据并阅读作者公开 PDF 的题名、署名、摘要与引言；作者顺序采用出版记录与正文共同支持的顺序；未通读全文或复现实验。

**候选用途**：用于说明 C++ 错误类型转换检测与每对象运行时类型元数据。

**使用限制**：TypeSan 针对类型混淆检测，不是所有内存错误的统一检测器；摘要中的覆盖和开销比较限于当时被比较的工具与基准。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/2976749.2978405) · [hexhive.epfl.ch 2](https://hexhive.epfl.ch/publications/files/16CCS2.pdf)

标签：sanitizer, type-confusion, C++

<a id="jeon2017hextype"></a>

### HexType: Efficient Detection of Type Confusion Errors for C++

`jeon2017hextype` · 2017 · Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security · supporting

作者/机构：Yuseok Jeon; Priyam Biswas; Scott Carr; Byoungyoung Lee; Mathias Payer

**核验深度**：`metadata+abstract`。核对 ACM/Crossref 元数据，并阅读作者公开 PDF 的署名、摘要与引言；未通读全文或复现实验。

**候选用途**：用于补充显式运行时类型检查、对象分配模式覆盖及 sanitizer 优化。

**使用限制**：是 C++ 类型混淆检测研究；对 Firefox/SPEC 的改善不能外推为任何编译器防御或任意工作负载的优势。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/3133956.3134062) · [hexhive.epfl.ch 2](https://hexhive.epfl.ch/publications/files/17CCS.pdf)

标签：sanitizer, type-confusion, C++

<a id="serebryany2018memorytagging"></a>

### Memory Tagging and how it improves C/C++ memory safety

`serebryany2018memorytagging` · 2018 · arXiv preprint arXiv:1802.09517 · supporting

作者/机构：Kostya Serebryany; Evgenii Stepanov; Aleksey Shlyapnikov; Vlad Tsyrklevich; Dmitry Vyukov

**核验深度**：`metadata+abstract`。阅读 arXiv 官方题名、作者、年份与摘要；未通读全文或复现实验。

**候选用途**：用于介绍内存标记机制及硬件/编译器协作的背景。

**使用限制**：这是预印本；摘要讨论 SPARC 硬件与 AArch64 方案，不能据此宣称已评价当前 Arm MTE 全部实现或获得确定性的完整内存安全。

来源：[arxiv.org 1](https://arxiv.org/abs/1802.09517)

标签：memory-tagging, hardware-assisted, memory-safety

<a id="jeon2020fuzzan"></a>

### FuZZan: Efficient Sanitizer Metadata Design for Fuzzing

`jeon2020fuzzan` · 2020 · 2020 USENIX Annual Technical Conference (USENIX ATC 20) · core

作者/机构：Yuseok Jeon; WookHyun Han; Nathan Burow; Mathias Payer

**核验深度**：`metadata+abstract`。阅读 USENIX 官方页面的完整摘要与官方 BibTeX；未通读全文或复现实验。

**候选用途**：用于区分提高 fuzzing 中 sanitizer 运行效率的工作与检测编译器防御实现错误的工作。

**使用限制**：文中设计应用于 ASan，性能与检出结论有基准范围；不能把吞吐量提升改写为所有 sanitizer 的检测能力提升。

来源：[www.usenix.org 1](https://www.usenix.org/conference/atc20/presentation/jeon)

标签：sanitizer, fuzzing, metadata

<a id="marini2025qmsan"></a>

### QMSan: Efficiently Detecting Uninitialized Memory Errors During Fuzzing

`marini2025qmsan` · 2025 · Proceedings 2025 Network and Distributed System Security Symposium · supporting

作者/机构：Matteo Marini; Daniele Cono D’Elia; Mathias Payer; Leonardo Querzoni

**核验深度**：`metadata+abstract`。核对 NDSS DOI 的 Crossref 元数据，并阅读作者公开 PDF 的署名、摘要与引言；未通读全文或复现实验。

**候选用途**：用于补充近期未初始化内存检测、二进制翻译和 fuzzing 场景下插桩兼容性问题。

**使用限制**：论文实验中未出现误报/漏报不等于一般性零误报/零漏报证明；该研究检测被测程序错误，不直接验证编译器安全防御的正确性。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.14722/ndss.2025.241133) · [hexhive.epfl.ch 2](https://hexhive.epfl.ch/publications/files/25NDSS3.pdf)

标签：sanitizer, fuzzing, uninitialized-memory

<a id="szekeres2013eternalwar"></a>

### SoK: Eternal War in Memory

`szekeres2013eternalwar` · 2013 · 2013 IEEE Symposium on Security and Privacy · core

作者/机构：László Szekeres; Mathias Payer; Tao Wei; Dawn Song

**核验深度**：`metadata+abstract`。核对 IEEE/Crossref 出版元数据，并阅读作者公开 PDF 的署名、摘要与引言；未通读全文或复现实验。

**候选用途**：用于组织空间/时间内存安全、代码指针保护等策略的关系和部署权衡。

**使用限制**：综述中的当前系统、已部署防御与攻击情况对应 2013 年；不能将历史判断照搬为 2026 年事实。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1109/sp.2013.13) · [hexhive.epfl.ch 2](https://hexhive.epfl.ch/publications/files/13Oakland.pdf)

标签：memory-safety, survey, foundation

<a id="yang2017deadstore"></a>

### Dead Store Elimination (Still) Considered Harmful

`yang2017deadstore` · 2017 · 26th USENIX Security Symposium (USENIX Security 17) · core

作者/机构：Zhaomo Yang; Brian Johannesmeyer; Anders Trier Olesen; Sorin Lerner; Kirill Levchenko

**核验深度**：`metadata+abstract`。阅读 USENIX 官方页面的完整摘要与官方 BibTeX；未通读全文或复现实验。

**候选用途**：直接支持编译器优化可能破坏程序员预期的敏感数据擦除，以及擦除技术和编译器支持的讨论。

**使用限制**：应限定为安全擦除场景和具体技术；不能扩展为编译器通常破坏所有安全检查，或将擦除语义混同于标准功能输出。

来源：[www.usenix.org 1](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/yang)

标签：secure-erasure, optimization, security-semantics

<a id="simon2018whatyouc"></a>

### What You Get is What You C: Controlling Side Effects in Mainstream C Compilers

`simon2018whatyouc` · 2018 · 2018 IEEE European Symposium on Security and Privacy (EuroS&P) · core

作者/机构：Laurent Simon; David Chisnall; Ross Anderson

**核验深度**：`metadata+abstract`。核对 IEEE/Crossref 元数据，并阅读作者公开 PDF 的署名、摘要与引言；未通读全文或复现实验。

**候选用途**：用于论证常数时间和秘密擦除等隐含安全属性需要显式编译器支持，而普通 C 可观察行为不足以表达全部安全意图。

**使用限制**：论文实现和论证有具体属性、架构与工具链范围；不能据此声称所有常数时间代码都会被优化破坏或所有副作用都可由该方案保障。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1109/eurosp.2018.00009) · [www.cl.cam.ac.uk 2](https://www.cl.cam.ac.uk/archive/rja14/Papers/whatyouc.pdf)

标签：secure-erasure, constant-time, optimization, security-semantics

<a id="almeida2016ctverif"></a>

### Verifying Constant-Time Implementations

`almeida2016ctverif` · 2016 · 25th USENIX Security Symposium (USENIX Security 16) · core

作者/机构：José Bacelar Almeida; Manuel Barbosa; Gilles Barthe; François Dupressoir; Michael Emmi

**核验深度**：`metadata+abstract`。阅读 USENIX 官方页面的完整摘要与官方 BibTeX；未通读全文或复现实验。

**候选用途**：用于说明常数时间是关系型安全属性，以及可在优化后的 LLVM 实现上开展专门验证。

**使用限制**：需保留泄漏模型、公开输入/输出和验证假设；不能把 LLVM 层验证直接写成所有微架构侧信道安全。

来源：[www.usenix.org 1](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/almeida)

标签：constant-time, verification, LLVM, security-semantics

<a id="blazy2019constanttime"></a>

### Verifying constant-time implementations by abstract interpretation

`blazy2019constanttime` · 2019 · Journal of Computer Security · supporting

作者/机构：Sandrine Blazy; David Pichardie; Alix Trieu

**核验深度**：`metadata+abstract`。核对出版方登记的 Crossref 题名、作者、年份、venue、DOI，并阅读同一记录的完整摘要；未通读全文或复现实验。 Crossref 明确区分 2018 在线发表和 2019 卷期，条目采用卷期年。

**候选用途**：用于补充基于抽象解释的 C 源程序常数时间验证及其与 CompCert/Verasco 的联系。

**使用限制**：源语言分析和核心语言语义论证不自动推出所有后端、ISA 或微架构上的完整侧信道安全。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.3233/jcs-181136)

标签：constant-time, abstract-interpretation, verification

<a id="oleksenko2020specfuzz"></a>

### SpecFuzz: Bringing Spectre-type vulnerabilities to the surface

`oleksenko2020specfuzz` · 2020 · 29th USENIX Security Symposium (USENIX Security 20) · core

作者/机构：Oleksii Oleksenko; Bohdan Trach; Mark Silberstein; Christof Fetzer

**核验深度**：`metadata+abstract`。阅读 USENIX 官方页面的完整摘要与官方 BibTeX；未通读全文或复现实验。

**候选用途**：用于介绍通过软件暴露推测执行路径、结合检查器和 fuzzing 检测特定推测执行风险的思路。

**使用限制**：其检测范围受推测模型、执行覆盖和检查器约束；不应表述为涵盖所有瞬态执行漏洞或对编译器防御正确性的通用证明。

来源：[www.usenix.org 1](https://www.usenix.org/conference/usenixsecurity20/presentation/oleksenko)

标签：speculation, fuzzing, Spectre

<a id="guarnieri2020spectector"></a>

### Spectector: Principled Detection of Speculative Information Flows

`guarnieri2020spectector` · 2020 · 2020 IEEE Symposium on Security and Privacy (SP) · core

作者/机构：Marco Guarnieri; Boris Köpf; José Francisco Morales; Jan Reineke; Andrés Sánchez

**核验深度**：`metadata+abstract`。核对 IEEE/Crossref 元数据，阅读作者项目网站方法说明，以及作者公开论文 PDF 的署名、摘要与引言；未通读全文或复现实验。

**候选用途**：用于补充基于符号执行与 SMT 的推测信息流分析，以及检查编译器插入推测执行缓解措施的相关工作。

**使用限制**：结论相对论文的执行/泄漏模型、程序范围和分析限制成立；不能概括为任意真实处理器上无侧信道。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1109/sp40000.2020.00011) · [spectector.github.io 2](https://spectector.github.io/) · [spectector.github.io 3](https://spectector.github.io/papers/spectector.pdf)

标签：speculation, verification, compiler-hardening

<a id="vassena2021blade"></a>

### Automatically Eliminating Speculative Leaks from Cryptographic Code with Blade

`vassena2021blade` · 2021 · Proceedings of the ACM on Programming Languages · core

作者/机构：Marco Vassena; Craig Disselkoen; Klaus von Gleissenthall; Sunjay Cauligi; Rami Gökhan Kıcı; Ranjit Jhala; Dean Tullsen; Deian Stefan

**核验深度**：`metadata+abstract`。核对出版方登记的 Crossref 题名、作者、年份、venue、DOI，并阅读同一记录的完整摘要；未通读全文或复现实验。

**候选用途**：用于补充通过类型系统约束推测信息流并自动插入保护的编译器防御研究。

**使用限制**：论文原型基于 Cranelift/WebAssembly，保证相对形式化模型成立；不能表述成已保护所有原生 C/C++ 编译器或所有瞬态执行机制。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145/3434330)

标签：speculation, type-system, compiler-hardening

## 条目详情：LLM 测试、分析、规范及方法近邻

<a id="deng2023titanfuzz"></a>

### Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models

`deng2023titanfuzz` · 2023 · Proceedings of the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis · core

作者/机构：Yinlin Deng; Chunqiu Steven Xia; Haoran Peng; Chenyuan Yang; Lingming Zhang

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：LLM同时承担程序生成与补全式变异，利用训练语料中语言/API约束知识提高输入有效性；适合相关工作中生成侧背景。

**使用限制**：评估对象主要是深度学习库；不能外推到编译器防御完整性，也不能把生成有效性当成oracle正确性。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145%2F3597926.3598067) · [arxiv.org 2](https://arxiv.org/abs/2212.14834)

标签：LLM-fuzzing, DL-libraries, generation-mutation

<a id="deng2024fuzzgpt"></a>

### Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries

`deng2024fuzzgpt` · 2024 · Proceedings of the IEEE/ACM 46th International Conference on Software Engineering · core

作者/机构：Yinlin Deng; Chunqiu Steven Xia; Chenyuan Yang; Shizhuo Dylan Zhang; Shujing Yang; Lingming Zhang

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：利用历史触发缺陷程序的稀有成分，通过in-context learning或fine-tuning生成非常规输入；可支持缺陷历史作为生成知识源。

**使用限制**：历史bug模式启发输入不等于从历史补丁准确恢复防御规范；本文收录正式ICSE题名，预印本题名不同。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145%2F3597503.3623343) · [arxiv.org 2](https://arxiv.org/abs/2304.02014)

标签：LLM-fuzzing, historical-bugs, edge-cases

<a id="meng2024chatafl"></a>

### Large Language Model guided Protocol Fuzzing

`meng2024chatafl` · 2024 · Proceedings 2024 Network and Distributed System Security Symposium · core

作者/机构：Ruijie Meng; Martin Mirchev; Marcel Böhme; Abhik Roychoudhury

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：利用LLM中的协议知识生成消息语法并引导消息序列探索，说明自然语言领域知识能够辅助结构化测试。

**使用限制**：评估对象是网络协议实现；状态覆盖不证明编译产物防御性质。不能把论文结果外推到任意协议或任意模型。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.14722%2Fndss.2024.24556) · [www.ndss-symposium.org 2](https://www.ndss-symposium.org/ndss-paper/large-language-model-guided-protocol-fuzzing/)

标签：LLM-fuzzing, protocol, structured-input

<a id="lyu2024promptfuzz"></a>

### Prompt Fuzzing for Fuzz Driver Generation

`lyu2024promptfuzz` · 2024 · Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security · core

作者/机构：Yunlong Lyu; Yuxuan Xie; Peng Chen; Hao Chen

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：覆盖反馈驱动prompt变异与fuzz driver生成，并结合程序验证和调度；可用于输入/驱动合成及反馈循环近邻。

**使用限制**：它生成库测试驱动，不生成DeFuzz防御oracle；不要与另一篇同名PromptFuzz提示注入测试论文混淆。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145%2F3658644.3670396) · [arxiv.org 2](https://arxiv.org/abs/2312.17677)

标签：LLM-fuzzing, harness-generation, coverage-feedback

<a id="hu2023chatfuzz"></a>

### Augmenting Greybox Fuzzing with Generative AI

`hu2023chatfuzz` · 2023 · arXiv preprint arXiv:2306.06782 · supporting

作者/机构：Jie Hu; Qian Zhang; Heng Yin

**核验深度**：`metadata+abstract`。已核对作者arXiv元数据并阅读摘要；未核实正式出版版本，未逐节精读或复现实验。

**候选用途**：从灰盒fuzzer的seed pool选取种子，提示生成模型产生更符合格式的变体；适合说明LLM辅助变异的早期工作。

**使用限制**：本轮核实的是2023作者预印本，未核实正式出版版本；原文明确在复杂非平凡语法目标上未普遍优于AFL++。

来源：[arxiv.org 1](https://arxiv.org/abs/2306.06782)

标签：LLM-fuzzing, greybox, structured-input

<a id="zhang2026llamafuzz"></a>

### LLAMAFUZZ: Large Language Model Enhanced Greybox Fuzzing

`zhang2026llamafuzz` · 2026 · Proceedings of the 7th ACM/IEEE International Conference on Automation of Software Test · supporting

作者/机构：Hongxiang Zhang; Yuyang Rong; Yifeng He; Hao Chen

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：通过配对变异种子微调LLM并接入灰盒fuzzing，补充结构化输入变异路线；正式AST2026版本已核。

**使用限制**：通用程序的结构化数据变异，不是编译器防御oracle；摘要中的覆盖/bug结果只适用于其基准、配置和统计口径。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145%2F3793654.3793756) · [arxiv.org 2](https://arxiv.org/abs/2406.07714)

标签：LLM-fuzzing, greybox, fine-tuning, 2026

<a id="lemieux2023codamosa"></a>

### CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models

`lemieux2023codamosa` · 2023 · 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE) · core

作者/机构：Caroline Lemieux; Jeevana Priya Inala; Shuvendu K. Lahiri; Siddhartha Sen

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：搜索式测试覆盖进入平台期时，调用LLM产生欠覆盖函数的示例，再由搜索继续探索；可支持按反馈选择模型介入时机。

**使用限制**：覆盖提高并不证明安全性质；这里的LLM辅助单元测试生成不能直接当成编译器防御对照实验结果。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1109%2FICSE48619.2023.00085) · [www.microsoft.com 2](https://www.microsoft.com/en-us/research/publication/codamosa-escaping-coverage-plateaus-in-test-generation-with-pre-trained-large-language-models/)

标签：LLM-test-generation, coverage-feedback, hybrid-search

<a id="ryan2024symprompt"></a>

### Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM

`ryan2024symprompt` · 2024 · Proceedings of the ACM on Software Engineering · supporting

作者/机构：Gabriel Ryan; Siddhartha Jain; Mingyue Shang; Shiqi Wang; Xiaofei Ma; Murali Krishna Ramanathan; Baishakhi Ray

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：把生成过程拆成与执行路径对齐的多阶段prompt，并提供类型及依赖上下文；可支持源码条件与输入生成的连接。

**使用限制**：路径引导用于Python回归测试，不能声称它不利用源码，也不能把路径覆盖等同于语义正确性证明。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145%2F3643769) · [arxiv.org 2](https://arxiv.org/abs/2402.00097)

标签：LLM-test-generation, source-context, path-guidance

<a id="altmayerpizzorno2025coverup"></a>

### CoverUp: Effective High Coverage Test Generation for Python

`altmayerpizzorno2025coverup` · 2025 · Proceedings of the ACM on Software Engineering · core

作者/机构：Juan Altmayer Pizzorno; Emery D. Berger

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：迭代结合覆盖分析、代码上下文和执行反馈生成高覆盖Python回归测试；是2025年反馈驱动测试生成近邻。

**使用限制**：正式题名已改为Effective High Coverage Test Generation for Python；覆盖结果不能证明oracle或程序语义完整。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145%2F3729398) · [arxiv.org 2](https://arxiv.org/abs/2403.16218)

标签：LLM-test-generation, coverage-feedback, 2025

<a id="chen2024chatunitest"></a>

### ChatUniTest: A Framework for LLM-Based Test Generation

`chen2024chatunitest` · 2024 · Companion Proceedings of the 32nd ACM International Conference on the Foundations of Software Engineering · supporting

作者/机构：Yinghao Chen; Zehao Hu; Chen Zhi; Junxiao Han; Shuiguang Deng; Jianwei Yin

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：自适应focal context及generation-validation-repair流程，可作为上下文压缩、生成后检查与修复的工程近邻。

**使用限制**：收录的是FSE2024 Companion工具论文；通过编译/测试检查不代表生成断言准确表达用户意图。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145%2F3663529.3663801) · [arxiv.org 2](https://arxiv.org/abs/2305.04764)

标签：LLM-test-generation, context-selection, validation-repair

<a id="cosler2023nl2spec"></a>

### nl2spec: Interactively Translating Unstructured Natural Language to Temporal Logics with Large Language Models

`cosler2023nl2spec` · 2023 · Computer Aided Verification · core

作者/机构：Matthias Cosler; Christopher Hahn; Daniel Mendoza; Frederik Schmitt; Caroline Trippel

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：将自然语言要求转成时序逻辑，并把子公式映射回原文供人交互修正；非常适合说明规范提取的歧义和可追溯性。

**使用限制**：明确包含用户增删改子翻译；不能写成全自动正确恢复规范，更不能据此声称DeFuzz结构化要求就是形式化证明。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1007%2F978-3-031-37703-7_18) · [arxiv.org 2](https://arxiv.org/abs/2303.04864)

标签：specification-inference, natural-language, human-in-loop

<a id="sun2024clover"></a>

### Clover: Closed-Loop Verifiable Code Generation

`sun2024clover` · 2024 · AI Verification · core

作者/机构：Chuyue Sun; Ying Sheng; Oded Padon; Clark Barrett

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：检查代码、docstring与形式化标注的一致性，结合LLM和验证工具；可用于讨论生成规范与代码之间的交叉检查。

**使用限制**：摘要评估为教材级Dafny程序；基准上的零误接收不是普遍零误报保证，也不是编译器防御语义正确性证据。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1007%2F978-3-031-65112-0_7) · [arxiv.org 2](https://arxiv.org/abs/2310.17807)

标签：formal-verification, code-generation, specification-consistency

<a id="wen2024autospec"></a>

### Enchanting Program Specification Synthesis by Large Language Models Using Static Analysis and Program Verification

`wen2024autospec` · 2024 · Computer Aided Verification · core

作者/机构：Cheng Wen; Jialun Cao; Jie Su; Zhiwu Xu; Shengchao Qin; Mengda He; Haokun Li; Shing-Chi Cheung; Cong Tian

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：静态分析和验证器驱动LLM生成候选规范，分解程序并逐轮验证候选；适合说明生成器与外部判据分工。

**使用限制**：候选规范在给定形式模型中验证，不自动等于自然语言防御意图正确；不要把AutoSpec当作仅生成loop invariant的系统。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1007%2F978-3-031-65630-9_16) · [arxiv.org 2](https://arxiv.org/abs/2404.00762)

标签：specification-inference, formal-verification, static-analysis

<a id="wu2024lemur"></a>

### Lemur: Integrating Large Language Models in Automated Program Verification

`wu2024lemur` · 2024 · The Twelfth International Conference on Learning Representations · core

作者/机构：Haoze Wu; Clark Barrett; Nina Narodytska

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：将LLM提出候选证明信息与自动推理器组合，并给出规则及soundness论证；适合对照程序化验证和LLM启发式的边界。

**使用限制**：论文证明的可靠性依赖其验证演算与自动推理器前提；不能移植成DeFuzz确定执行checker的语义正确性保证。

来源：[arxiv.org 1](https://arxiv.org/abs/2310.04870) · [theory.stanford.edu 2](https://theory.stanford.edu/~barrett/pubs/WCB24-abstract.html)

标签：formal-verification, neuro-symbolic, soundness

<a id="li2025iris"></a>

### IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities

`li2025iris` · 2025 · The Thirteenth International Conference on Learning Representations · core

作者/机构：Ziyang Li; Saikat Dutta; Mayur Naik

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：结合LLM推断污点规范、上下文分析与全仓库静态推理；直接相关于模型提供知识、分析器承担系统检查的路线。

**使用限制**：面向Java安全缺陷检测；LLM参与规范与上下文判别，不能概括成完全没有模型介入的裁决链或任意源码检查器合成。

来源：[arxiv.org 1](https://arxiv.org/abs/2405.17238) · [proceedings.iclr.cc 2](https://proceedings.iclr.cc/paper_files/paper/2025/hash/582d4e27fa24168f3af1f4582655034b-Abstract-Conference.html)

标签：LLM-static-analysis, taint-specifications, CodeQL, 2025

<a id="li2024llift"></a>

### Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach

`li2024llift` · 2024 · Proceedings of the ACM on Programming Languages · core

作者/机构：Haonan Li; Yu Hao; Yizhuo Zhai; Zhiyun Qian

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：将静态分析与LLM结合，通过post-constraint guidance改进Linux内核use-before-initialization分析；可说明语义辅助路径筛选。

**使用限制**：针对特定缺陷模型和内核变量约定；不是通用checker生成，也不是形式化soundness保证。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145%2F3649828)

标签：LLM-static-analysis, kernel, post-constraints

<a id="ji2025artemis"></a>

### Artemis: Toward Accurate Detection of Server-Side Request Forgeries through LLM-Assisted Inter-procedural Path-Sensitive Taint Analysis

`ji2025artemis` · 2025 · Proceedings of the ACM on Programming Languages · supporting

作者/机构：Yuchen Ji; Ting Dai; Zhichao Zhou; Yutian Tang; Jingzhu He

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：LLM辅助的过程间、路径敏感污点分析，是从规范/上下文知识进入静态分析的2025近邻。

**使用限制**：对象为PHP中的SSRF，已有分析器核心及特定规则；本轮只读摘要，LLM具体介入点应在正文引用前再精读方法。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1145%2F3720488) · [arxiv.org 2](https://arxiv.org/abs/2502.21026)

标签：LLM-static-analysis, taint-analysis, 2025

<a id="wang2025inferroi"></a>

### Boosting Static Resource Leak Detection via LLM-based Resource-Oriented Intention Inference

`wang2025inferroi` · 2025 · 2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE) · core

作者/机构：Chong Wang; Jianan Liu; Xin Peng; Yang Liu; Yiling Lou

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：LLM推断资源获取、释放和可达性验证意图，再结合两阶段静态分析检查泄漏；与“规范/意图生成+程序检查”相关。

**使用限制**：意图推断不是完整资源语义证明；原论文作者验证与开发者确认数量不同，不能混写成全部获开发者确认。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1109%2FICSE55347.2025.00131) · [arxiv.org 2](https://arxiv.org/abs/2311.04448)

标签：LLM-static-analysis, resource-intention, 2025

<a id="sun2024gptscan"></a>

### GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis

`sun2024gptscan` · 2024 · Proceedings of the IEEE/ACM 46th International Conference on Software Engineering · core

作者/机构：Yuqiang Sun; Daoyuan Wu; Yue Xue; Han Liu; Haijun Wang; Zhengzi Xu; Xiaofei Xie; Yang Liu

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：以LLM识别逻辑缺陷候选及关键变量/语句，再执行静态确认；可支持模型建议与程序分析证据相结合。

**使用限制**：静态确认降低误报并不消除误报；智能合约业务逻辑和编译器防御要求不同，不能直接外推精度数字。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=GPTScan%20Detecting%20Logic%20Vulnerabilities&rows=3) · [arxiv.org 2](https://arxiv.org/abs/2308.03314)

标签：LLM-static-analysis, static-confirmation, smart-contracts

<a id="yao2023react"></a>

### ReAct: Synergizing Reasoning and Acting in Language Models

`yao2023react` · 2023 · The Eleventh International Conference on Learning Representations · supporting

作者/机构：Shunyu Yao; Jeffrey Zhao; Dian Yu; Nan Du; Izhak Shafran; Karthik Narasimhan; Yuan Cao

**核验深度**：`metadata+abstract`。已核对作者arXiv的ICLR camera-ready说明并阅读摘要、作者项目页的prompting说明；未复现实验。

**候选用途**：交替推理、动作与环境观察的agent设计先例；可为DeFuzz迭代读取源码、执行工具、根据反馈调整生成的组织方式提供背景。

**使用限制**：ReAct是通用agent范式，不是编译器测试专用算法；它不提供工具输出或最终判定正确性的保证。

来源：[arxiv.org 1](https://arxiv.org/abs/2210.03629) · [react-lm.github.io 2](https://react-lm.github.io/)

标签：agents, tool-use, reasoning-action

<a id="shinn2023reflexion"></a>

### Reflexion: language agents with verbal reinforcement learning

`shinn2023reflexion` · 2023 · Advances in Neural Information Processing Systems · supporting

作者/机构：Noah Shinn; Federico Cassano; Ashwin Gopinath; Karthik Narasimhan; Shunyu Yao

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：将任务反馈转换为语言反思并保存到episodic memory，用于下一次尝试；可讨论跨轮反馈积累。

**使用限制**：语言反思不是独立验证器，也不等于更新模型参数的强化学习；正式会议作者名单与arXiv元数据不同，采用会议名单。

来源：[papers.nips.cc 1](https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html)

标签：agents, memory, verbal-feedback

<a id="yang2024sweagent"></a>

### SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

`yang2024sweagent` · 2024 · Advances in Neural Information Processing Systems · supporting

作者/机构：John Yang; Carlos E. Jimenez; Alexander Wettig; Kilian Lieret; Shunyu Yao; Karthik Narasimhan; Ofir Press

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：agent-computer interface对仓库导航、文件编辑和测试执行的作用，可支撑工具接口与agent能力分离的设计理由。

**使用限制**：软件修复基准成功率不能作为编译器缺陷发现能力或防御验证正确性的依据。

来源：[proceedings.neurips.cc 1](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html)

标签：agents, tool-interface, repository-navigation

<a id="wu2024autogen"></a>

### AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversations

`wu2024autogen` · 2024 · First Conference on Language Modeling · supporting

作者/机构：Qingyun Wu; Gagan Bansal; Jieyu Zhang; Yiran Wu; Beibin Li; Erkang Zhu; Li Jiang; Xiaoyun Zhang; Shaokun Zhang; Jiale Liu; Ahmed Hassan Awadallah; Ryen W White; Doug Burger; Chi Wang

**核验深度**：`metadata+abstract`。已核对COLM2024官方录用名单及完整作者列表，并阅读作者arXiv摘要；官方录用列表题名为Conversations，预印本为Conversation。OpenReview遇到浏览器校验，未读取其正文。

**候选用途**：可编程多agent对话以及模型、工具、人类输入的组合框架；仅在解释编排背景时引用。

**使用限制**：框架通用性不是DeFuzz采用特定多agent配置有效的实验证据；不能把多agent编排称为本项目独有。

来源：[arxiv.org 1](https://arxiv.org/abs/2308.08155) · [colmweb.org 2](https://colmweb.org/2024/AcceptedPapers.html)

标签：agents, multi-agent, orchestration

<a id="schick2023toolformer"></a>

### Toolformer: Language Models Can Teach Themselves to Use Tools

`schick2023toolformer` · 2023 · Advances in Neural Information Processing Systems · optional

作者/机构：Timo Schick; Jane Dwivedi-Yu; Roberto Dessi; Roberta Raileanu; Maria Lomeli; Eric Hambro; Luke Zettlemoyer; Nicola Cancedda; Thomas Scialom

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：通过自监督训练学习何时、怎样调用API的工具使用先例，可为背景中的工具增强语言模型提供出处。

**使用限制**：Toolformer包含模型训练，不能拿来直接证明纯prompt驱动工具循环的效果；正式版多一位作者Eric Hambro。

来源：[papers.nips.cc 1](https://papers.nips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html)

标签：agents, tool-use, self-supervised-learning

<a id="madaan2023selfrefine"></a>

### Self-Refine: Iterative Refinement with Self-Feedback

`madaan2023selfrefine` · 2023 · Advances in Neural Information Processing Systems · supporting

作者/机构：Aman Madaan; Niket Tandon; Prakhar Gupta; Skyler Hallinan; Luyu Gao; Sarah Wiegreffe; Uri Alon; Nouha Dziri; Shrimai Prabhumoye; Yiming Yang; Shashank Gupta; Bodhisattwa Prasad Majumder; Katherine Hermann; Sean Welleck; Amir Yazdanbakhsh; Peter Clark

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：同一模型生成、反馈和修订的迭代模式；可作为与外部编译/执行反馈不同的自我修订路线。

**使用限制**：模型自反馈不是独立oracle；不应由其平均任务增益推出编译器测试中的可靠性。

来源：[proceedings.neurips.cc 1](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html)

标签：agents, iterative-refinement, self-feedback

<a id="liu2024lostmiddle"></a>

### Lost in the Middle: How Language Models Use Long Contexts

`liu2024lostmiddle` · 2024 · Transactions of the Association for Computational Linguistics · supporting

作者/机构：Nelson F. Liu; Kevin Lin; John Hewitt; Ashwin Paranjape; Michele Bevilacqua; Fabio Petroni; Percy Liang

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：相关信息在长上下文中位置不同会影响模型表现；可解释为什么检索和上下文组织值得做消融。

**使用限制**：实验主要是问答和键值检索；不能宣称它已经证明某种源码切片或BM25优于embedding。

来源：[api.crossref.org 1](https://api.crossref.org/works?query.title=Lost%20in%20the%20Middle%20How%20Language%20Models%20Use%20Long%20Contexts&rows=3) · [arxiv.org 2](https://arxiv.org/abs/2307.03172)

标签：retrieval, long-context, context-selection

<a id="robertson2009bm25"></a>

### The Probabilistic Relevance Framework: BM25 and Beyond

`robertson2009bm25` · 2009 · Foundations and Trends in Information Retrieval · core

作者/机构：Stephen Robertson; Hugo Zaragoza

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：BM25/BM25F概率相关性框架的权威系统阐述，可支撑方法部分词法检索公式和参数来源。

**使用限制**：这是检索方法基础，不是针对编译器源码的优越性证据；不能把经典BM25和项目定制融合排序的效果混为一谈。

来源：[api.crossref.org 1](https://api.crossref.org/works/10.1561%2F1500000019)

标签：retrieval, BM25, probabilistic-ranking

<a id="karpukhin2020dpr"></a>

### Dense Passage Retrieval for Open-Domain Question Answering

`karpukhin2020dpr` · 2020 · Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP) · supporting

作者/机构：Vladimir Karpukhin; Barlas Oguz; Sewon Min; Patrick Lewis; Ledell Wu; Sergey Edunov; Danqi Chen; Wen-tau Yih

**核验深度**：`metadata+abstract`。已核对正式元数据及一手摘要；未逐节精读、未复现实验。

**候选用途**：双编码器dense passage retrieval的代表工作；可在方法或检索消融背景中说明密集检索路线。

**使用限制**：在开放域问答上优于BM25不代表编译器标识符、pass名或代码上下文也更好。

来源：[aclanthology.org 1](https://aclanthology.org/2020.emnlp-main.550/)

标签：retrieval, dense-retrieval, dual-encoder

## 条目详情：编译器、运行库和 ISA/ABI 官方文档

<a id="gcc15instrumentation"></a>

### GCC 15.2: Instrumentation Options

`gcc15instrumentation` · 2025 · Official documentation · core

作者/机构：GCC Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：栈保护、stack-clash、CFI、sanitizer、hardened 选项及平台限制。

**使用限制**：选项文档描述预期行为，不能证明具体编译器构建的实现正确。

来源：[gcc.gnu.org 1](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Instrumentation-Options.html)

标签：official-documentation, compiler-defense-flags

<a id="gcc15commonfunctionattrs"></a>

### GCC 15.2: Common Function Attributes

`gcc15commonfunctionattrs` · 2025 · Official documentation · supporting

作者/机构：GCC Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：zero_call_used_regs、access 等函数属性的规范与启用条件。

**使用限制**：strub 的主要规范在 Common Type Attributes，不能把属性存在等同于任意调用点已被正确加固。

来源：[gcc.gnu.org 1](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Common-Function-Attributes.html)

标签：official-documentation, strub-zero-call-used-regs-access

<a id="gcc15commonvariableattrs"></a>

### GCC 15.2: Common Variable Attributes

`gcc15commonvariableattrs` · 2025 · Official documentation · supporting

作者/机构：GCC Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：counted_by 和 nonstring 属性及对象边界相关语义。

**使用限制**：属性支持和语义依赖语言及编译器版本，不代表自动保证所有动态边界安全。

来源：[gcc.gnu.org 1](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Common-Variable-Attributes.html)

标签：official-documentation, counted-by-nonstring

<a id="gcc15codegen"></a>

### GCC 15.2: Code Generation Options

`gcc15codegen` · 2025 · Official documentation · supporting

作者/机构：GCC Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：栈复用、代码生成与 noplt 等编译选项背景。

**使用限制**：ABI、链接器和平台条件需要同时核对；性能选项并非一律是安全防御。

来源：[gcc.gnu.org 1](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Code-Gen-Options.html)

标签：official-documentation, abi-stack-reuse-noplt

<a id="gcc15staticanalysis"></a>

### GCC 15.2: Static Analyzer Options

`gcc15staticanalysis` · 2025 · Official documentation · supporting

作者/机构：GCC Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：-fanalyzer 的用途、检查器选项和诊断边界。

**使用限制**：静态诊断与运行时插桩属于不同验证对象，不应混为所有后端均生效的防御。

来源：[gcc.gnu.org 1](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Static-Analyzer-Options.html)

标签：official-documentation, static-analysis

<a id="gcc15optimize"></a>

### GCC 15.2: Optimize Options

`gcc15optimize` · 2025 · Official documentation · supporting

作者/机构：GCC Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：自动变量初始化、寄存器清零以及优化选项的预期语义。

**使用限制**：需同时考虑优化等级、目标支持和显式选项；此页面不是实验支持矩阵。

来源：[gcc.gnu.org 1](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Optimize-Options.html)

标签：official-documentation, optimization-init-scrubbing

<a id="clangcfi"></a>

### Clang: Control Flow Integrity

`clangcfi` · 发表年未核定/滚动文档 · Official documentation · core

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：Clang CFI 方案、启用条件及使用限制。

**使用限制**：不同 CFI 方案、LTO 和可见性条件不同，不能概括为同一检查契约。

来源：[clang.llvm.org 1](https://clang.llvm.org/docs/ControlFlowIntegrity.html)

标签：official-documentation, cfi

<a id="clangcfidesign"></a>

### Clang: Control Flow Integrity Design Documentation

`clangcfidesign` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：类型测试与控制流完整性实现设计背景。

**使用限制**：设计文档不证明当前版本或所有 ISA 上的实现正确。

来源：[clang.llvm.org 1](https://clang.llvm.org/docs/ControlFlowIntegrityDesign.html)

标签：official-documentation, cfi-design

<a id="clangsafestack"></a>

### Clang: SafeStack

`clangsafestack` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：safe/unsafe stack 划分、使用条件和已说明的限制。

**使用限制**：SafeStack 不等于通用越界检测，也不能等同于硬件 shadow stack。

来源：[clang.llvm.org 1](https://clang.llvm.org/docs/SafeStack.html)

标签：official-documentation, safestack

<a id="clangshadowcallstack"></a>

### Clang: ShadowCallStack

`clangshadowcallstack` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：返回地址保护与架构专用寄存器、运行时支持前提。

**使用限制**：页面是滚动版本；平台支持需对齐实验编译器，不能仅由文档清单推出可用性。

来源：[clang.llvm.org 1](https://clang.llvm.org/docs/ShadowCallStack.html)

标签：official-documentation, shadow-stack

<a id="clangasan"></a>

### Clang: AddressSanitizer

`clangasan` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：ASan 检测对象、构建和运行要求、局限。

**使用限制**：检测器本身的正确性与覆盖范围仍需独立验证，不代表不存在漏报。

来源：[clang.llvm.org 1](https://clang.llvm.org/docs/AddressSanitizer.html)

标签：official-documentation, asan

<a id="clangmsan"></a>

### Clang: MemorySanitizer

`clangmsan` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：未初始化内存使用检测与完整插桩等运行前提。

**使用限制**：MSan 与 ASan 的问题模型不同，不能交换其缺陷覆盖范围。

来源：[clang.llvm.org 1](https://clang.llvm.org/docs/MemorySanitizer.html)

标签：official-documentation, msan

<a id="clangubsan"></a>

### Clang: UndefinedBehaviorSanitizer

`clangubsan` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：UBSan 检查集合、recover/trap 等报告行为。

**使用限制**：报告模式可配置；不能把所有 sanitizer 的成功诊断都概括成必然进程崩溃。

来源：[clang.llvm.org 1](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)

标签：official-documentation, ubsan

<a id="clanghwasan"></a>

### Clang: Hardware-assisted AddressSanitizer Design

`clanghwasan` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：指针/内存标记及 AArch64 TBI 支持下的检测设计。

**使用限制**：HWASan 与硬件 MTE 不是同一机制，也不提供一般无遗漏保证。

来源：[clang.llvm.org 1](https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html)

标签：official-documentation, hwasan

<a id="clangslh"></a>

### LLVM: Speculative Load Hardening

`clangslh` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：SLH 的威胁范围、谓词依赖与实现思路。

**使用限制**：只适用于文档明确的推测执行问题模型，不是所有微架构侧信道的统一防御。

来源：[llvm.org 1](https://llvm.org/docs/SpeculativeLoadHardening.html)

标签：official-documentation, speculative-load-hardening

<a id="clangattrs"></a>

### Clang: Attribute Reference

`clangattrs` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：musttail、counted_by 及其他检查适用条件所需的属性规范。

**使用限制**：必须引用具体属性小节；整个属性目录不能作为某一目标后端正确实现的证据。

来源：[clang.llvm.org 1](https://clang.llvm.org/docs/AttributeReference.html)

标签：official-documentation, attributes-counted-by-musttail

<a id="llvmreflang"></a>

### LLVM Language Reference Manual

`llvmreflang` · 发表年未核定/滚动文档 · Official documentation · core

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：IR 语义、属性、内存操作与正确性约束的规范基础。

**使用限制**：滚动开发版需与实验 LLVM commit 对齐；不能自动覆盖机器码层防御义务。

来源：[llvm.org 1](https://llvm.org/docs/LangRef.html)

标签：official-documentation, ir-semantics-poison-ub

<a id="llvmub"></a>

### LLVM IR Undefined Behavior Manual

`llvmub` · 发表年未核定/滚动文档 · Official documentation · core

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：undef、poison、freeze 与 refinement 比较的语义背景。

**使用限制**：LLVM IR 的 UB 语义不能直接等同于 C/C++ 源语言规则。

来源：[llvm.org 1](https://llvm.org/docs/UndefinedBehavior.html)

标签：official-documentation, ub-refinement

<a id="llvmcodegen"></a>

### The LLVM Target-Independent Code Generator

`llvmcodegen` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：middle-end/backend lowering、指令选择与机器级变换背景。

**使用限制**：架构说明不证明某个 pass 或保护机制在全部目标上的行为。

来源：[llvm.org 1](https://llvm.org/docs/CodeGenerator.html)

标签：official-documentation, backend-lowering

<a id="llvmtestguide"></a>

### LLVM Testing Infrastructure Guide

`llvmtestguide` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：回归测试、lit/FileCheck 等实现验证背景。

**使用限制**：通过既有回归测试不等于对全部安全契约的语义证明。

来源：[llvm.org 1](https://llvm.org/docs/TestingGuide.html)

标签：official-documentation, testing-regression

<a id="glibcfortify"></a>

### The GNU C Library: Source Fortification

`glibcfortify` · 发表年未核定/滚动文档 · Official documentation · core

作者/机构：GNU C Library Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：_FORTIFY_SOURCE、对象大小内建函数及加固调用的库/编译器契约。

**使用限制**：glibc 版本、编译器能力和优化条件共同决定行为，不能由符号存在推出边界计算正确。

来源：[sourceware.org 1](https://sourceware.org/glibc/manual/latest/html_node/Source-Fortification.html)

标签：official-documentation, fortify

<a id="glibcerase"></a>

### The GNU C Library: Erasing Sensitive Data

`glibcerase` · 发表年未核定/滚动文档 · Official documentation · core

作者/机构：GNU C Library Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：普通擦除可能被优化删除，与 explicit_bzero/memset_explicit 承诺的区别。

**使用限制**：擦除目标内存的保证不自动覆盖寄存器副本和所有中间数据。

来源：[sourceware.org 1](https://sourceware.org/glibc/manual/latest/html_node/Erasing-Sensitive-Data.html)

标签：official-documentation, secure-erasure

<a id="arm_aapcs64"></a>

### Procedure Call Standard for the Arm 64-bit Architecture (AAPCS64), 2025Q1

`arm_aapcs64` · 2025 · Official documentation · core

作者/机构：Arm

**核验深度**：`official-doc`。已读取 2025Q1 规范源码的寄存器/特性约定小节。

**候选用途**：AArch64 参数、返回值、callee-saved 与平台寄存器约定。

**使用限制**：特别注意 x18 的平台保留规则；ABI 义务与 caller-saved 寄存器清零义务不同。

来源：[raw.githubusercontent.com 1](https://raw.githubusercontent.com/ARM-software/abi-aa/2025Q1/aapcs64/aapcs64.rst)

标签：official-documentation, arm_aapcs64

<a id="arm_sysvabi64"></a>

### System V ABI for the Arm 64-bit Architecture, 2025Q1

`arm_sysvabi64` · 2025 · Official documentation · supporting

作者/机构：Arm

**核验深度**：`official-doc`。已读取 2025Q1 规范源码的寄存器/特性约定小节。

**候选用途**：BTI、PAC、GCS 相关 ELF 特性与链接/调用约定。

**使用限制**：规范支持不表示任意硬件、内核或 QEMU 已实现该特性。

来源：[raw.githubusercontent.com 1](https://raw.githubusercontent.com/ARM-software/abi-aa/2025Q1/sysvabi64/sysvabi64.rst)

标签：official-documentation, arm_sysvabi64

<a id="riscvpsabi"></a>

### RISC-V ABIs Specification, version 2.0-rc0

`riscvpsabi` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：RISC-V International

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：RISC-V 寄存器约定、调用约定和 ELF ABI。

**使用限制**：本次页面标示 2026-11-04 pre-release 2.0-rc0；不能当作已冻结正式版本，实验前必须固定版本。

来源：[riscv-non-isa.github.io 1](https://riscv-non-isa.github.io/riscv-elf-psabi-doc/)

标签：official-documentation, riscv-abi

<a id="loongarchabi"></a>

### LoongArch ELF ABI Specification, version 2.01

`loongarchabi` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：Loongson Technology Corporation Limited

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：LoongArch 寄存器、参数/返回值及 ELF ABI。

**使用限制**：ABI 文档不能证明某个 compiler defense 已被 LoongArch 后端实现。

来源：[loongson.github.io 1](https://loongson.github.io/LoongArch-Documentation/LoongArch-ELF-ABI-EN.html)

标签：official-documentation, loongarch-abi

<a id="loongarchisa"></a>

### LoongArch Reference Manual, Volume 1: Basic Architecture, version 1.10

`loongarchisa` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：Loongson Technology Corporation Limited

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：LoongArch 指令语义及机器级观察的规范入口。

**使用限制**：按具体指令小节和版本引用，不从 ISA 规范推断工具链与运行环境支持。

来源：[loongson.github.io 1](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html)

标签：official-documentation, loongarch-isa

<a id="riscvcfi_raw"></a>

### RISC-V Unprivileged ISA Manual: Control-Flow Integrity

`riscvcfi_raw` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：RISC-V International

**核验深度**：`official-doc`。已读取官方规范源码的前向/后向边 CFI 及扩展定义。

**候选用途**：Zicfilp 前向边与 Zicfiss 后向边防御的官方规范源码。

**使用限制**：读取的是 main 分支规范源码；正式引用前应固定 release/commit，并核验硬件及编译器支持。

来源：[raw.githubusercontent.com 1](https://raw.githubusercontent.com/riscv/riscv-isa-manual/main/src/unpriv/cfi.adoc)

标签：official-documentation, riscvcfi_raw

<a id="x86psabi"></a>

### System V Application Binary Interface: AMD64 Architecture Processor Supplement

`x86psabi` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：x86-64 psABI Maintainers

**核验深度**：`official-doc`。已读取维护仓库的项目标识和规范入口，尚未逐节读取规范 PDF。

**候选用途**：x86-64 psABI 维护仓库与规范入口。

**使用限制**：本次只核维护仓库和规范入口；具体寄存器或 red-zone 论断需进一步查阅相应版本 PDF。

来源：[gitlab.com 1](https://gitlab.com/x86-psABIs/x86-64-ABI)

标签：official-documentation, x86psabi

<a id="clangcsacheckers"></a>

### Clang Static Analyzer: Checker Developer Manual

`clangcsacheckers` · 发表年未核定/滚动文档 · Official documentation · supporting

作者/机构：LLVM Project

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：CSA checker 接口与扩展分析器背景，可配合 KNighter。

**使用限制**：这里只支持开发接口背景，不证明合成 checker 的可靠性。

来源：[clang-analyzer.llvm.org 1](https://clang-analyzer.llvm.org/checker_dev_manual.html)

标签：official-documentation, checker-synthesis

<a id="gcctypeattrs"></a>

### GCC 15.2: Common Type Attributes

`gcctypeattrs` · 2025 · Official documentation · supporting

作者/机构：GCC Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：strub 类型属性、模式、调用约束与栈擦除规范。

**使用限制**：须与 instrumentation options 联合读；不能把未启用或不适用的擦除视为遗漏。

来源：[gcc.gnu.org 1](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Common-Type-Attributes.html)

标签：official-documentation, gcctypeattrs

<a id="gccobjectsize"></a>

### GCC 15.2: Object Size Checking

`gccobjectsize` · 2025 · Official documentation · core

作者/机构：GCC Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：__builtin_object_size、动态对象大小和加固调用的判定基础。

**使用限制**：对象大小语义及未知值处理依赖 type 参数；常量差异本身不能证明错误。

来源：[gcc.gnu.org 1](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Object-Size-Checking.html)

标签：official-documentation, gccobjectsize

<a id="gccstrictflex"></a>

### GCC 15.2: C Dialect Options

`gccstrictflex` · 2025 · Official documentation · supporting

作者/机构：GCC Developers

**核验深度**：`official-doc`。已读取官方页面及与用途对应的小节；未核对实现或执行实验。

**候选用途**：-fstrict-flex-arrays 等 C 方言选项与柔性数组的适用规则。

**使用限制**：语言选项的行为不等同于独立运行时 bounds checker。

来源：[gcc.gnu.org 1](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/C-Dialect-Options.html)

标签：official-documentation, gccstrictflex
