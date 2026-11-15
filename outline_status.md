# DeFenzz - IEEE S&P 论文撰写与精校进度追踪 (Paper Writing Status)

> **状态定义说明**：
> 本文档严格执行**二值状态**规范——全篇仅存在 **`[ready]`** 与 **`[不 ready]`** 两种状态，坚决杜绝模糊中间态。
> - **`[ready]`**：已结合导师与大佬（Mat）两轮批注精校定稿并锁定，具备最高权威性，未经用户显式要求严禁修改。
> - **`[不 ready]`**：未定稿 / 待结合大佬二审意见修改 / 待对齐实证数据或补齐收尾章节。
>
> **当前状态汇总（对照 `main.tex` 与 [`mat_comments_list.md`](./mat_comments_list.md)）**：
> - **`[ready]`（`main.tex` `L1–L182`，Motivation 及之前全部章节已按大佬两轮意见修改定稿并锁定）**：
>   1. **Title & Abstract（标题与摘要，`L103–L117`）**
>   2. **Section 1 Introduction（第一章 引言，`L119–L141`）**
>   3. **Section 2 Motivation（第二章 动机与背景，`L143–L182`）**
> - **`[不 ready]`（`main.tex` `L183` 起所有后续章节）**：
>   - Section 3 Design（`L183–L353`）与 Section 4 Implementation（`L354–L360`）已完成大刀阔斧重构初稿与图 2 对齐，Section 5 Evaluation（`L362–L594`）已完成全章大改、原始运行日志交叉核验与 4 幅矢量图 + 5 张三线表重绘，均待作者审阅确认后方可升级为 `[ready]`；待补齐的 Discussion / Related Work / Conclusion 处于 `不 ready` 状态。

---

## 逐章节精校状态列表

### 0. Title & Abstract (`main.tex` `L103–L117`)
- [ready] **Title & Abstract**（已结合大佬第一轮批注 `[R1-1]`–`[R1-4]`、`[R1-9]` 及最新漏洞统计 `111 / 30 / 11` 定稿锁定；二审无新批注）

### 1. Introduction (`main.tex` `L119–L141`)
- [ready] **Section 1 Introduction（全章锁定）**（已完整落实大佬两轮批注 `[R1-4]`–`[R1-11]` 与 `[R2-1]`–`[R2-7]`）
  - [ready] 1.1 Scope, Cross-ISA Lowering & UB vs. Mitigation Conflict (`L121`, `[R1-5]`, `[R1-6]`, `[R2-1]`, `[R2-2]`, `[R2-8]`)
  - [ready] 1.2 Silent Defense Failures & Running Example CVE-2023-4039 (`L123`, `[R1-2]`, `[R1-7]`, `[R2-3]`, `[R2-9]`)
  - [ready] 1.3 Post-Compilation Verification & Two Barriers in Prior Work (`L125`, `[R1-2]`, `[R1-6]`, `[R1-8]`)
  - [ready] 1.4 Central Question, Core Insight & LLM Role (`L127`, `[R1-4]`, `[R1-8]`, `[R1-9]`, `[R1-10]`, `[R2-4]`)
  - [ready] 1.5 Three Challenges & `Check IR` Accuracy Grounding (`L129`, `[R1-10]`, `[R1-11]`, `[R2-5]`, `[R2-6]`)
  - [ready] 1.6 Evaluation Summary & Four Contributions with Compiler Versions (`L131–L141`, `[R1-10]`, `[R2-7]`)

### 2. Motivation (`main.tex` `L143–L182`)
- [ready] **Section 2 Motivation（全章锁定）**（已完整落实大佬两轮批注 `[R2-8]`–`[R2-10]` 并对齐 `AGENTS.md` 规范）
  - [ready] 2.1 Compiler-Instrumented Defenses (`L145–L149`，明确保护 `C and C++ systems software` 抵御 `unknown or unpatched vulnerabilities`，统一 `silently weakened or broken`，回应 `[R2-8]`、`[R2-9]`)
  - [ready] 2.2 Motivating Example (`L151–L173`，GCC `_FORTIFY_SOURCE` 潜伏 14 年静默放宽漏洞匿名化解析与代码块排版)
  - [ready] 2.3 Limitations of Existing Approaches (`L175–L181`，显式点明良性执行期间缓解机制从不触发 `[R2-10]`，并对齐静态检查/动态执行确定性 Oracle 表述)

### 3. Design of DeFenzz (`main.tex` `L183–L353`)
- [不 ready] **3.0 Section 3 Overview & Architecture**（`L183–L187`：已按 `[R2-0]`、`[R2-11]` 重写为 7 句因果动机推导、移除未展开缩写并重绘对齐 `figures/method-overview.pdf`，待作者审阅确认）
- [不 ready] **3.1 Security Invariant Generation (Section 3.A)**（`L189–L226`：已按 `[R2-0]`、`[R1-3]`、`[R2-12]`–`[R2-14]` 对比替代方案、前置 `Listing 2: INV-FORT-014` 四架构结构、首次展开 `CoT`/`RAG` 并剥离切片与检索工程细节，待作者审阅确认）
- [不 ready] **3.2 Compiler Source Mapping (Section 3.B)**（`L228–L250`：已按 `[R2-0]`、`[R2-13]`、`[R2-14]` 论证黑盒/全覆盖/关键词检索失效原因与编译器内探针零二进制扰动优势，待作者审阅确认）
- [不 ready] **3.3 Programmatic Oracle Construction (Section 3.C)**（`L252–L317`：已按 `[R2-0]`、`[R2-5]`、`[R2-6]`、`[R2-13]`、`[R2-14]` 补入反转运行时崩溃语义、对比四种预言机方案、剥离 Go 语言样板并补齐离线 Gate 1 / Gate 2 双门控验证，待作者审阅确认）
- [不 ready] **3.4 Agentic Directed Fuzzing (Section 3.D)**（`L319–L352`：已按 `[R2-0]`、`[R2-13]`–`[R2-15]` 点明 targeted fuzz drivers 测试防御假设与选择性防折叠优化两难，强化联合诊断与绑定 `m + FAIL` 约简放大，待作者审阅确认）

### 4. Implementation (`main.tex` `L354–L360`)
- [不 ready] **Section 4 Implementation**（`L354–L360`：已配合 `[R2-0]`、`[R2-13]` 完整承接从 Section 3 下沉的单函数/`.md`/手册切片、BM25 下划线子词 + `sqlite-vec` 稠密向量 RRF、`clangd`/CodeQL/Tree-sitter MCP 工具与 `fortify#b4e1` 探针重写、Go gRPC/Podman/QEMU 四架构执行、Gate 1/2 实现及 C-Reduce 工程细节，待作者审阅确认）

### 5. Evaluation (`main.tex` `L362–L594`)
- [不 ready] **5.1 Experimental Setup**（`L372–L385`：已对齐 GCC 16.2.0 / 17.0 trunk、LLVM 23.1.2、四类 64 位目标架构及跨架构补充目标、`F1`–`F6` 六大防御族、`deepseek-flash` + 16-vCPU Neoverse-N2 30 GiB 环境、5 个基线与 5 个消融变体，待作者审阅确认）
- [不 ready] **5.2 RQ1: Silent Defense Bug Discovery and Oracle Funnel**（`L410–L486`：已对齐 `Table II` 111 新漏洞 / 30 确认 / 11 修复 / +5 标签与 20 非漏洞排除明细、重绘 `Fig. 3` 根因阶段与非 x86 严重度分布、核准 `Table III` 921 $\to$ 2,922 $\to$ 9,061 $\to$ 915 (906S/9D) 离线漏斗，并精选 GCC PR 128271 与 LLVM #237864 双案例，待作者审阅确认）
- [不 ready] **5.3 RQ2: Comparison with Existing Compiler Fuzzers**（`L487–L522`：已新增 `Table IV` 与 `Fig. 4` 对比 YARPGen / UBfuzz / MetaMut / FeatureFuzz / Fuzz4All，分离 *Native* vs. *+Our Oracle* 预言机鸿沟与 9,061 探针分支覆盖鸿沟，论证 $1 \subset 3 \subset 8 \subset 14 \subset 18 \subset 111$ 严格超集与 93 个独占漏洞，待作者审阅确认）
- [不 ready] **5.4 RQ3: Ablation Study**（`L523–L584`：已重绘双面板独立坐标轴 `Fig. 5` 与双作用域 `Table V`，覆盖全量 921 不变量 Check IR / RAG 消融与 41 不变量受控切片在线消融，严格剥离失真表述并对齐真实 Go Check IR 架构，待作者审阅确认）
- [不 ready] **5.5 RQ4: Agent Telemetry, Cost, and Overhead**（`L585–L594`：已重绘概念级标签 `Fig. 6` 99,236 次工具调用分布并核准 `Table VI` 59,671 次调用、1,610.01M Token、92.4% KV 缓存命中率、$<2.0\%$ 编译开销与 $0.0\%$ 目标二进制开销，待作者审阅确认）

### 6. Discussion, Related Work, and Conclusion (`main.tex` `L594` 后待补齐)
- [不 ready] 6.1 Discussion and Limitations（含人工核验边界、Token 成本及历史漏洞基准讨论 `[R2-7]`）
- [不 ready] 6.2 Related Work
- [不 ready] 6.3 Conclusion
