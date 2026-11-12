# DeFuzz 候选参考文献库

核验日期：2026-11-12。此库为后续论文写作收集候选来源，不要求把所有文献加入当前稿件。权威编辑源是本分支的 `collections/*.json`；本机同步文件只是阅读副本。

本批共 **136 项：102 篇论文、34 项官方文档或软件资料**。其中 22 项沿用当前稿件的引用键，114 项为新增键。数量按独立书目条目计算；同一系统的论文与使用手册可分别存在，不表示有同样多条独立研究路线。

## 阅读入口

- [优先阅读路线](reading-map.md)：按近期写作问题挑选先读条目。
- [完整目录](catalog.md)：可搜索题名、作者、引用键和标签；逐项查看一手来源、实际阅读深度、候选用途与不能外推的限制。
- [library.bib](library.bib)：全部候选条目的 BibTeX，包含已存在引用键的核实版本。
- [additional.bib](additional.bib)：相对 Related Work 基准提交 `a60e54e` 的新增引用键，便于按需选入正文。
- [检查记录](validation.md)：结构、重复键、链接和 IEEEtran 书目编译验证。
- [原书目问题](notes/existing-and-methods.md)：Silent Bugs Matter、AgentFuzz、SpecAuditor、CoT 的实质元数据纠错，以及其他补全事项。

## 覆盖范围

| 专题 | 条目数 | 说明 |
| --- | ---: | --- |
| [既有 Related Work 与方法基础](notes/existing-and-methods.md) | 23 | 14 篇已核对方法/oracle章节的文献，加上编译器安全、RAG/CoT、LLVM、Z3 和软件背景 |
| [编译器测试、验证、评测与缩减](notes/compiler-testing.md) | 23 | 编译器验证、变形测试、fuzzing评测、ground truth 与输入缩减 |
| [防御与安全语义](notes/defenses.md) | 29 | CFI、栈保护、sanitizer、内存安全、安全擦除、常数时间、推测执行 |
| [LLM 分析与近邻](notes/llm-analysis.md) | 28 | fuzzing/测试生成、规格/属性生成、静态分析、agent、检索 |
| [官方文档](notes/official-docs.md) | 33 | GCC/Clang/LLVM、glibc、四 ISA 的 ABI/规范入口 |

## 核验标记的含义

| 标记 | 数量 | 本轮实际完成的工作 |
| --- | ---: | --- |
| `metadata+method` | 25 | 核对文献身份并选择性阅读方法/oracle相关章节；个别项依据官方方法文档，细节见条目 |
| `metadata+abstract` | 75 | 核对一手出版或作者来源的元数据并阅读摘要；没有声称通读全文 |
| `metadata-only` | 2 | 仅确认文献身份；SpecAuditor 和 Z3 的具体方法论断需补读原文 |
| `official-doc` | 34 | 读取官方规范/文档或软件入口；x86-64 psABI目前仅核维护入口，见其阅读深度 |

`core`（71 项）、`supporting`（60 项）、`optional`（5 项）是对 DeFuzz 写作相关性的阅读优先级，不是论文质量或效果排名。每条的 `source_urls` 是实际读取的一手来源；Crossref条目使用出版方登记信息。DOI若未核到就留空，预印本不冒写正式会议。滚动文档保留访问日期而不猜发表年份。

元数据与摘要核验不能替代正文比较论点的证据。涉及算法细节、优劣、首创性、实验数字或保证范围时，应先读对应原文，并记录页码/小节。未复现实验；未对全部条目做系统综述意义上的穷尽检索。

## 合入正文时

1. 从目录挑选实际需要的条目，先核实所支撑的具体句子及所用版本。
2. 新引用可从 `additional.bib` 挑取。这个文件相对 `a60e54e` 检查无现有 key、DOI 或题名重复；后续主分支变化后应再次检查。
3. 旧引用的元数据修正需按相同 key 替换原条目。**不要把 `library.bib` 与原 `refs.bib` 同时加载，也不要将整份候选库直接追加到原书目**，否则会产生重复键。C-Reduce 正式 PLDI论文与现有软件网页条目是不同文献载体，按引用用途选择。
4. 运行论文自己的 BibTeX/LaTeX 检查。收集库本身不改变论文正文和当前引用选择。

## 分支关系

本分支 `feature/feiyang-reference-library-20261112` 基于 Related Work 分支 `feature/feiyang-related-work-20261112`，基准提交 `a60e54e061686af36592fe3b5673ae6cb754d983`。PR 初始 base 设为 Related Work 分支，因此差异只包含文献库。Related Work 合并后再改到 `main`；若此前用了 squash/rebase merge，应先把仅属于本库的提交 rebase 到最新 `main`，防止重复带入 Related Work。

## 可复核资料与待补项

原始页面/PDF快照保存在 ssh004 的 `~/defuzz-project/feiyang-writing/reference-library-2026-11-12-evidence/`，此前14篇的证据保存在同级 `references/` 和来源审计笔记中。仓库只收来源链接、元数据与笔记，不提交下载的PDF或网页。证据目录也包含失败/误命中线索；只有入库条目注明的来源经过采用核验。

各专题 notes 保留待核文献和来源冲突。Oracle survey、Intel SDM/CET、部分防御历史论文等未因搜索命中就冒充已读文献。官方文档不能代替实验使用版本、平台支持矩阵或实现正确性的独立证据。
