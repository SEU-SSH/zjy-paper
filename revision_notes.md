# 论文修订意见整理

## 2026-09-08：截图意见落实（标题、摘要与前两章）

本轮以截图最后一组意见为准，将挑战改为“不变量提炼、checker 与种子的协同构造、跨 ISA 语义适配”。下文“近期提交落实情况”保留为历史记录，不代表本轮修订后的状态。

| 意见 | 本轮处理 |
| --- | --- |
| 使用 `compiler-instrumented defenses`，重构标题 | 标题改为 `DeFuzz: Invariant-Guided Agentic Testing of Compiler-Instrumented Defenses`；摘要、前两章及 defense-role 图统一术语，正文定义 `compiler defenses` 为简称。 |
| 减少摘要中的枚举和原因解释 | 仅保留 stack canaries 与 CFI 两个例子；删除 `on a particular backend`，直接描述 CVE-2023-4039 导致的保护绕过；摘要由约 366 词缩至约 223 词。 |
| 体现 invariants 从哪里来 | 首次使用时给出定义；第二章新增来源说明，区分编译器源码与文档、ISA/ABI 规范、历史漏洞及补丁，并说明当前实现行为不能直接当作规范。 |
| 将生成 checker 与生成种子合为一个挑战 | 第二项挑战围绕同一个不变量的可观测违例与触发条件组织，贡献列表与其对应。 |
| 体现编译器防御实现与 ISA 假设是否匹配 | 第三项挑战明确指令语义、寄存器约定和栈布局；checker 需要解释这些语义，ISA 元数据路由只是适用性控制。 |
| 说明为何引入 Agent | 动机改为利用源码上下文生成有特定语义结构的种子，并根据 coverage/checker 反馈迭代；不再把 free agent 的不可复现性当成领域固有挑战。 |
| 参考近期 invariant 研究 | 引用已核验的 PropertyGPT（NDSS 2025）与 CIll（2026 年 arXiv 预印本），借鉴“候选生成与独立检查分离”，不将本文的 security invariants 等同于归纳循环不变量。 |
| 保留必要技术细节与图 | 保留 VLA/alloca、动态栈调整和关键图；defense-matrix 与 stack-layout 各保留第二章的一份，消除重复图及标签。 |

### 随文核实

- PR-96191 实际是 AArch64 `stack_protect_test` 后 canary 值残留于寄存器，不是 CVE-2023-4039 的栈布局同源漏洞。已修正文献标题和第二章描述，并用该案例说明如何从 machine-description 要求提炼不变量。
- CVE-2023-4039 的地址关系改为明确的“动态缓冲区 < 保存的返回地址 < canary”；违例是覆盖返回地址而不改变 guard，不是 canary 比较没有执行。
- Threat Model 明确防御已启用且所需运行环境成立；不把超出机制威胁模型的任意写入当作防御缺陷。GCC 16.1 限定为不变量提炼语料，避免与 GCC/LLVM 测试范围冲突。
- 不再把确定性证据等同于形式化 soundness 或零误报保证。漏洞数及上游确认数保留占位符，未补造实验结果。

核验来源：[CVE 原始报告](https://rtx.meta.security/mitigation/2023/09/12/CVE-2023-4039.html)、[GCC PR-96191](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=96191)、[PropertyGPT 官方页面](https://www.ndss-symposium.org/ndss-paper/propertygpt-llm-driven-formal-verification-of-smart-contracts-through-retrieval-augmented-property-generation/)、[CIll 预印本](https://arxiv.org/abs/2602.23389)。

### 后续范围

- 第三章及之后正文未改；后续需同步术语和挑战主线，并核实关于 soundness、复现保证和现有方法不足的绝对化表述。
- `refs.bib` 原有 SpecAuditor 条目本轮未找到可核验的原始来源；保留其现状，待修改 Related Work 时确认，不用于前两章论证。
- 实验数据、确认状态及图中结果标记仍需与实验记录核对；本轮未改变这些数据。

## 标题与核心术语
- 调研并统一 compiler defense 的通用命名，避免使用文献中不常见的表述。
- 修改标题中的 `cross-mechanism invariants`，因为最终不变量仍与具体机制绑定。
- 全文统一使用 `security invariants`，不要与 `safety invariants` 混用。
- 核心术语首次出现时定义，后文保持一致，避免概念漂移。

## Abstract (摘要)
- 将篇幅压缩约一半，删除重复内容和次要实现细节。
- 按“问题、挑战、方案、结果、意义”重写，避免按执行流程介绍系统。
- 删除将 ISA 写成唯一失效根因的表述，因为实际问题还包括实现错误和机制交互。
- 补充实验结果的意义，不能只报告漏洞数量。

## Introduction (引言) 与 Research Gap
- 按 `Scope -> Problem -> Research Gap -> Insight -> Approach -> Results -> Contributions` 重组，使主线更清晰。
- 补充现有方法的不足，并明确 oracle、多 ISA 和搜索空间带来的挑战。
- 新增由 Agent 解决的独立挑战，否则标题中的 Agent 缺少必要动机。
- 修正“所有防御都分析 AST”的错误表述，因为部分防御工作在 IR 等层级。
- 明确不覆盖编译优化选项与防御机制的交互，避免扩大论文声明范围。

## Background 与 Threat Model
- 定义 compiler defense，介绍防御实现模型和相关历史漏洞。
- 新增 Threat Model，保持与被研究防御机制自身的威胁模型一致。
- 明确 Scope，将研究范围限定为 compiler defense 的静默失效。

## Contributions (贡献提炼)
- 按挑战组织贡献，避免按执行步骤拆分或重复计数。
- 不将 `LLM-driven fuzzing` 作为主体贡献，因为 fuzzing 只是实现手段。
- 突出 Agentic Framework、Oracle/Invariant、跨 ISA Checker 和漏洞发现结果。
- 将 `silent failures` 明确为 compiler defense failures，避免范围含糊。

## 图示设计 (Figures)
- 减少纯流程图，因为其对核心问题的解释力有限。
- 保留能够解释问题本质、关键设计或结果分布的图。
- 将 defense-matrix 放在 Background 或结果章节，使其服务于问题空间或结果分析。

## 近期提交落实情况

相关提交：

- `073ab93`：落实标题、摘要、引言、研究缺口、威胁模型和贡献表述等主要修改。
- `e9cb83e`：精修摘要，恢复关键图示及必要技术细节。
- `14f607b`、`447691b`：仅重新编译或更新 `main.pdf`。

### 标题与核心术语

| 审阅意见 | 状态 | 处理方式 |
| --- | --- | --- |
| 统一 compiler defense 的通用命名 | 部分完成 | `073ab93` 引入并定义 `compiler security defense`；但当前仍混用 `compiler defenses`、`compiler security defenses` 和 `compiler-inserted security defenses`。 |
| 修改标题中的 `cross-mechanism invariants` | 已完成 | 标题改为 `Cross-Mechanism Invariant Transfer`，强调跨机制迁移历史根因和不变量知识，不再声称不变量本身跨机制通用。 |
| 统一使用 `security invariants` | 已完成 | 摘要中的 `safety invariants` 已改为 `security invariants`，正文无 `safety invariant` 残留。 |
| 首次出现时定义核心术语并保持一致 | 部分完成 | Background 定义了 compiler security defense，Section IV 定义了 security invariant；但术语在 Abstract 和 Introduction 中先于正式定义出现，compiler defense 命名仍有漂移。 |

### Abstract

| 审阅意见 | 状态 | 处理方式 |
| --- | --- | --- |
| 将篇幅压缩约一半 | 部分完成 | `073ab93` 将摘要从 387 词压缩至 220 词，`e9cb83e` 为恢复逻辑和必要信息扩展至 259 词，最终缩短约 33%。 |
| 按“问题、挑战、方案、结果、意义”重写 | 已完成 | 第一段说明问题、oracle gap 和搜索空间，第二段说明方案、结果与意义，不再按系统执行流程展开。 |
| 不将 ISA 写成唯一失效根因 | 已完成 | 摘要改为 `complex backend lowering and other root causes`；引言补充 ISA 差异、设计与实现不匹配、栈布局假设错误等原因。 |
| 补充实验结果的意义 | 基本完成 | 增加“揭示 compiler defense 的脆弱性”和“证明 grounded agent fuzzing 可系统化保护 backend”的结论；漏洞数和 CVE 数仍为占位符。 |

### Introduction 与 Research Gap

| 审阅意见 | 状态 | 处理方式 |
| --- | --- | --- |
| 按 Scope 到 Contributions 重组 | 基本完成 | 当前依次介绍研究范围、Silent Defense Failures、Research Gap、Insight、Approach 和 Contributions；Results 尚未形成独立段落。 |
| 补充现有方法不足及 oracle、多 ISA、搜索空间挑战 | 已完成 | 说明传统 fuzzing 缺少有效 oracle、静态分析难以覆盖异构 backend，以及机制乘 ISA 矩阵带来的搜索空间。 |
| 新增由 Agent 解决的独立挑战 | 已完成 | 增加 free-running agent 的幻觉、不可复现等问题，并在 Introduction 中通过 "First... Second... Third..." 的句式将其与 Oracle Gap、Search Space 明确并列为三大挑战。 |
| 修正“所有防御都分析 AST” | 已完成 | 改为分析不同中间表示，并列举 AST、GIMPLE 和 LLVM IR。 |
| 排除优化选项与防御机制的交互 | 已完成 | 明确当前只研究 standard defense emissions，不覆盖 defense 与 compilation optimization flags 的交互。 |

### Background 与 Threat Model

| 审阅意见 | 状态 | 处理方式 |
| --- | --- | --- |
| 定义 compiler defense 并介绍实现模型和历史漏洞 | 已完成 | 新增 compiler security defense 定义、IR 到 backend lowering 的实现模型，以及 CVE-2023-4039 和 PR-96191 案例。 |
| 新增 Threat Model | 已完成 | 给出攻击者能力、研究范围和排除项，并明确与被研究防御机制自身的假设一致。 |
| 将 Scope 限定为 compiler defense 的静默失效 | 部分完成 | 全文主线已限定为 silent defense failures；但 Threat Model 的 `In-Scope` 仅写防御未按预期工作，未再次明确其必须静默通过编译和功能测试。 |

### Contributions

| 审阅意见 | 状态 | 处理方式 |
| --- | --- | --- |
| 按挑战组织贡献 | 已完成 | 重组为 deterministic oracle、invariant transfer、agentic framework 和 empirical discovery 四项。 |
| 不将 `LLM-driven fuzzing` 作为主体贡献 | 已完成 | LLM 仅作为 agentic framework 中的生成和反馈手段，不再单列为主体贡献。 |
| 突出 Agentic Framework、Oracle/Invariant、跨 ISA Checker 和结果 | 已完成 | 四项内容均已进入贡献列表，其中跨 ISA 能力表述为 ISA-bound checker routing。 |
| 将 `silent failures` 明确为 compiler defense failures | 部分完成 | Contributions 已改为 `silent compiler defense failures`；Abstract 和 Conclusion 仍存在泛化的 `silent failures` 或 `silent-failure defects`。 |

### 图示设计

| 审阅意见 | 状态 | 处理方式 |
| --- | --- | --- |
| 减少解释力有限的纯流程图 | 部分完成 | `073ab93` 删除了部分图，但同时误删了帮助理解关键设计的图。 |
| 保留解释问题、设计或结果的关键图 | 已完成 | `e9cb83e` 恢复 `oracle-flow`、`blackboard` 和 `checker-routing`。 |
| 将 defense-matrix 放入 Background 或结果章节 | 已完成 | `defense-matrix` 已移至 Background，用于解释 defense mechanism 乘 ISA 的问题空间。 |
