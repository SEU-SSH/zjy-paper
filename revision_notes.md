  1→# 论文修订意见整理
  2→
  3→## 标题与核心术语
  4→- 调研并统一 compiler defense 的通用命名，避免使用文献中不常见的表述。
  5→- 修改标题中的 `cross-mechanism invariants`，因为最终不变量仍与具体机制绑定。
  6→- 全文统一使用 `security invariants`，不要与 `safety invariants` 混用。
  7→- 核心术语首次出现时定义，后文保持一致，避免概念漂移。
  8→
  9→## Abstract (摘要)
 10→- 将篇幅压缩约一半，删除重复内容和次要实现细节。
 11→- 按“问题、挑战、方案、结果、意义”重写，避免按执行流程介绍系统。
 12→- 删除将 ISA 写成唯一失效根因的表述，因为实际问题还包括实现错误和机制交互。
 13→- 补充实验结果的意义，不能只报告漏洞数量。
 14→
 15→## Introduction (引言) 与 Research Gap
 16→- 按 `Scope -> Problem -> Research Gap -> Insight -> Approach -> Results -> Contributions` 重组，使主线更清晰。
 17→- 补充现有方法的不足，并明确 oracle、多 ISA 和搜索空间带来的挑战。
 18→- 新增由 Agent 解决的独立挑战，否则标题中的 Agent 缺少必要动机。
 19→- 修正“所有防御都分析 AST”的错误表述，因为部分防御工作在 IR 等层级。
 20→- 明确不覆盖编译优化选项与防御机制的交互，避免扩大论文声明范围。
 21→
 22→## Background 与 Threat Model
 23→- 定义 compiler defense，介绍防御实现模型和相关历史漏洞。
 24→- 新增 Threat Model，保持与被研究防御机制自身的威胁模型一致。
 25→- 明确 Scope，将研究范围限定为 compiler defense 的静默失效。
 26→
 27→## Contributions (贡献提炼)
 28→- 按挑战组织贡献，避免按执行步骤拆分或重复计数。
 29→- 不将 `LLM-driven fuzzing` 作为主体贡献，因为 fuzzing 只是实现手段。
 30→- 突出 Agentic Framework、Oracle/Invariant、跨 ISA Checker 和漏洞发现结果。
 31→- 将 `silent failures` 明确为 compiler defense failures，避免范围含糊。
 32→
 33→## 图示设计 (Figures)
 34→- 减少纯流程图，因为其对核心问题的解释力有限。
 35→- 保留能够解释问题本质、关键设计或结果分布的图。
 36→- 将 defense-matrix 放在 Background 或结果章节，使其服务于问题空间或结果分析。
 37→
 38→## 近期提交落实情况
 39→
 40→以下状态以当前 `main` 的 `e7835fb` 为准，而非某次历史提交时的状态。`e7835fb` 保留了三项挑战的结构，但回调了摘要和引言的部分表述，因此少数此前标记为“已完成”的事项已回退。
 41→
 42→相关提交：
 43→
 44→- `073ab93`：完成标题、摘要、引言、研究缺口、威胁模型和贡献表述的第一轮重构。
 45→- `e9cb83e`：恢复 `oracle-flow`、`blackboard`、`checker-routing` 等关键图，并补回必要技术细节。
 46→- `9d3ba48`、`8545aef`：将 Oracle Gap、Search Space 和 free-running agent 问题显式组织为三项挑战。
 47→- `973fdf3`：将摘要和引言中的方案与三项挑战逐一对应。
 48→- `e7835fb`：回调摘要和引言的措辞以恢复可读性，同时保留三项挑战；也重新引入了部分术语和范围问题。
 49→- `14f607b`、`447691b`、`9087a20`：重新编译或更新 `main.pdf`。
 50→
 51→### 标题与核心术语
 52→
 53→| 审阅意见 | 状态 | 处理方式 |
 54→| --- | --- | --- |
 55→| 统一 compiler defense 的通用命名 | 部分完成 | Background 定义了 `compiler security defense`，但标题使用 `compiler defenses`，摘要和引言使用 `compiler-inserted defenses`，Conclusion 使用 `compiler-inserted security defenses`。需要选定一个规范名称并全局替换。 |
 56→| 修改标题中的 `cross-mechanism invariants` | 已完成 | 标题改为 `Cross-Mechanism Invariant Transfer`，强调跨机制迁移历史根因和不变量知识，不再声称不变量本身跨机制通用。 |
 57→| 统一使用 `security invariants` | 已完成 | 正文与摘要已统一使用 `security invariants`。 |
 58→| 首次出现时定义核心术语并保持一致 | 部分完成 | Background 定义了 `compiler security defense`，Section IV 定义了 `security invariant`；但 Abstract 和 Introduction 在正式定义前已使用相关概念，且 compiler defense 命名仍有漂移。 |
 59→
 60→### Abstract
 61→
 62→| 审阅意见 | 状态 | 处理方式 |
 63→| --- | --- | --- |
 64→| 将篇幅压缩约一半 | 未完成 | `073ab93` 曾将摘要压缩至约 220 词；当前版本回调后约 367 词，而修订前约 398 词，仅缩短约 8%。需在不损失三项挑战主线的前提下再次压缩。 |
 65→| 按“问题、挑战、方案、结果、意义”重写 | 已完成 | 当前三段依次说明静默失效问题、三项挑战，以及逐项对应的方案与结果，不再按系统执行流程展开。 |
 66→| 不将 ISA 写成唯一失效根因 | 已完成 | 摘要明确将防御代码本身的正确性与 ISA 假设并列为影响因素；引言也说明 defense emission 可因实现逻辑错误及 backend lowering 而失效。 |
 67→| 补充实验结果的意义 | 部分完成 | 摘要说明了可复现性、可消融性和确定性证据的系统意义，但实验发现仍是 `\tbd{N}` / `\tbd{M}`，且未再明确解释漏洞结果揭示的防御脆弱性。 |
 68→
 69→### Introduction 与 Research Gap
 70→
 71→| 审阅意见 | 状态 | 处理方式 |
 72→| --- | --- | --- |
 73→| 按 Scope 到 Contributions 重组 | 部分完成 | 引言已包含范围、Silent Failure、三项挑战、Approach 和 Contributions；但现有方法的不足主要放在 Background，Research Gap 和 Insight 未形成清晰独立段落，Results 仍无独立段落。 |
 74→| 补充现有方法不足及 oracle、多 ISA、搜索空间挑战 | 已完成 | 说明传统 fuzzing 缺少有效 oracle、静态分析难以覆盖异构 backend，以及机制乘 ISA 矩阵带来的搜索空间。 |
 75→| 新增由 Agent 解决的独立挑战 | 已完成 | 增加 free-running agent 的幻觉、不可复现等问题，并在 Introduction 中通过 "First... Second... Third..." 的句式将其与 Oracle Gap、Search Space 明确并列为三大挑战。 |
 76→| 修正“所有防御都分析 AST” | 部分完成 | Background 已说明防御通常在 GIMPLE 或 LLVM IR 引入，并经历 backend lowering；但 Introduction 仍写成“the compiler analyzes the AST”，与前者矛盾。 |
 77→| 排除优化选项与防御机制的交互 | 未完成 | `073ab93` 曾明确仅研究 standard defense emissions；当前引言和 Threat Model 已无该排除项，需要恢复这一范围说明。 |
 78→
 79→### Background 与 Threat Model
 80→
 81→| 审阅意见 | 状态 | 处理方式 |
 82→| --- | --- | --- |
 83→| 定义 compiler defense 并介绍实现模型和历史漏洞 | 已完成 | 新增 compiler security defense 定义、IR 到 backend lowering 的实现模型，以及 CVE-2023-4039 和 PR-96191 案例。 |
 84→| 新增 Threat Model | 已完成 | 给出攻击者能力、研究范围和排除项，并明确与被研究防御机制自身的假设一致。 |
 85→| 将 Scope 限定为 compiler defense 的静默失效 | 部分完成 | `In-Scope` 已限定为编译器自动插入机制的失效，紧随其后的 Silent Failure 案例定义了“无编译诊断且功能行为正常”；但 Threat Model 本身没有将该双重静默条件写入范围定义。 |
 86→
 87→### Contributions
 88→
 89→| 审阅意见 | 状态 | 处理方式 |
 90→| --- | --- | --- |
 91→| 按挑战组织贡献 | 已完成 | 重组为 deterministic oracle、invariant transfer、agentic framework 和 empirical discovery 四项。 |
 92→| 不将 `LLM-driven fuzzing` 作为主体贡献 | 已完成 | LLM 仅作为 agentic framework 中的生成和反馈手段，不再单列为主体贡献。 |
 93→| 突出 Agentic Framework、Oracle/Invariant、跨 ISA Checker 和结果 | 部分完成 | Oracle/Invariant、显式编排 Agentic Framework 和 ISA-bound checker routing 已进入贡献列表；漏洞数量、CVE 和补丁仍为 `DEFERRED` 占位，经验发现尚不能作为已证实结果强调。 |
 94→| 将 `silent failures` 明确为 compiler defense failures | 部分完成 | Contributions 已改为 `silent compiler defense failures`；Abstract 和 Conclusion 仍存在泛化的 `silent failures` 或 `silent-failure defects`。 |
 95→
 96→### 图示设计
 97→
 98→| 审阅意见 | 状态 | 处理方式 |
 99→| --- | --- | --- |
100→| 减少解释力有限的纯流程图 | 部分完成 | `073ab93` 曾删除部分图，`e9cb83e` 恢复了支撑 Oracle、blackboard 和 checker routing 的关键图。当前仍同时保留 `architecture`、`main-loop` 和算法流程，需结合版面与叙事再判断是否删减。 |
101→| 保留解释问题、设计或结果的关键图 | 已完成 | `e9cb83e` 恢复 `oracle-flow`、`blackboard` 和 `checker-routing`。 |
102→| 将 defense-matrix 放入 Background 或结果章节 | 部分完成 | `defense-matrix` 已在 Background 中解释 mechanism $\times$ ISA 问题空间，但仍在 Introduction 重复插入；两处使用同一 `fig:defense-matrix` 标签。应保留 Background 版本并删除引言中的重复图。 |