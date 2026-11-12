# 建议的阅读路线

先按要写的论点选读，不需要顺序通读整个候选库。以下是阅读安排，不是已核实的比较结论；标记 `metadata+abstract` 或 `metadata-only` 的条目用于正文前仍需读方法章节。

## 近期最相关

| 写作问题 | 建议先读 | 接下来需要核对 |
| --- | --- | --- |
| 为何语言语义保持仍可能不足以满足安全预期 | [Silent Bugs Matter: A Study of Compiler-Introduced Security Bugs](catalog.md#silentbugs2023)；[Towards Optimization-Safe Systems: Analyzing the Impact of Undefined Behavior](catalog.md#wang2013stack)；[What You Get is What You C: Controlling Side Effects in Mainstream C Compilers](catalog.md#simon2018whatyouc)；[Dead Store Elimination (Still) Considered Harmful](catalog.md#yang2017deadstore) | 区分语言UB、程序员安全意图、规范承诺与编译器实现缺陷，避免将它们混为一类bug。 |
| sanitizer测试与其他编译器防御测试如何区分 | [UBFuzz: Finding Bugs in Sanitizer Implementations](catalog.md#li2024ubfuzz)；[Random Testing for C and C++ Compilers with YARPGen](catalog.md#livinskii2020yarpgen)；[Fuzzing Loop Optimizations in Compilers for C++ and Data-Parallel Languages](catalog.md#livinskii2023loops) | oracle的具体输入与判据、优化引起的不报告，以及工具/版本适用范围。 |
| 生成规格和生成checker有哪些近邻 | [SpecAuditor: Generating Audit Specifications for LLM-Driven Bug Detection](catalog.md#lin2026specauditor)；[KNighter: Transforming Static Analysis with LLM-Synthesized Checkers](catalog.md#yang2025knighter)；[PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation](catalog.md#liu2025propertygpt)；[IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](catalog.md#li2025iris)；[nl2spec: Interactively Translating Unstructured Natural Language to Temporal Logics with Large Language Models](catalog.md#cosler2023nl2spec) | SpecAuditor本轮只核文献身份，优先取得全文；其余核对生成对象、外部验证器和语义保证边界。 |
| 优化/源码反馈如何进入生成过程 | [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](catalog.md#yang2024whitefox)；[The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators](catalog.md#ou2024metamut)；[Fuzz4All: Universal Fuzzing with Large Language Models](catalog.md#xia2024fuzz4all)；[Bulbasaur: Branch-Guided Online Mutator Generation for Greybox Fuzzing](catalog.md#wang2026bulbasaur) | 输入生成、变异算子和判定器分别由什么信息驱动，避免过大的首创性表述。 |
| 已有形式验证能保证什么 | [Formal verification of a realistic compiler](catalog.md#leroy2009compcert)；[Alive2: Bounded Translation Validation for LLVM](catalog.md#lopes2021alive2)；[Verifying Constant-Time Implementations](catalog.md#almeida2016ctverif)；[Spectector: Principled Detection of Speculative Information Flows](catalog.md#guarnieri2020spectector) | 语言、目标、循环界限、泄漏模型与安全性质，不把范围差别写成对方没有安全保证。 |
| 实验怎样形成可解释的证据 | [Evaluating Fuzz Testing](catalog.md#klees2018fuzzeval)；[FuzzBench: An Open Fuzzer Benchmarking Platform and Service](catalog.md#metzman2021fuzzbench)；[Magma: A Ground-Truth Fuzzing Benchmark](catalog.md#hazimeh2020magma)；[Metamorphic Testing: A Review of Challenges and Opportunities](catalog.md#chen2018metamorphicsurvey) | 基准适配、重复实验和统计口径；这些背景文献不能代替师兄确认的实验分工与结果。 |
| 如何缩减复现材料并保持判据 | [Test-Case Reduction for C Compiler Bugs](catalog.md#regehr2012creduce)；[Perses: Syntax-Guided Program Reduction](catalog.md#sun2018perses)；[Pardis: Priority Aware Test Case Reduction](catalog.md#gharachorlu2019pardis)；[Simplifying and Isolating Failure-Inducing Input](catalog.md#zeller2002deltadebugging) | interestingness predicate和局部最小性；缩减器本身不负责证明oracle正确。 |

## 机制规范随用随查

涉及开关、属性或机器级义务时，优先从 [官方文档专题](notes/official-docs.md) 进入对应小节。GCC本批固定15.2，Clang/LLVM/glibc有滚动页面，Arm ABI固定2025Q1；RISC-V psABI当前为2.0-rc0预发布，RISC-V CFI规范使用main分支。论文方法与实验应固定自己的版本，不能用这些收集时版本代替实验版本。

涉及寄存器约定时使用对应ISA的ABI；涉及安全擦除时区分目标存储与其他副本；涉及sanitizer时核对report/recover/trap模式。x86-64 psABI只核维护仓库入口，具体规范段落仍待阅读。

## 合适的补读记录

每次决定引用一篇候选论文，在写作笔记中记录：要支持的句子、原文页码/小节、实际研究对象、oracle/验证器、假设与限制、所用正式版本。若只拿到摘要，应保留摘要层面的介绍，不自行补写算法或评价数字。

返回 [总目录](catalog.md) 或 [README](README.md)。
