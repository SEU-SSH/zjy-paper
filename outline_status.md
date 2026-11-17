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
>   3. **Section 2 Background and Motivation（第二章 背景与动机，`L143–L182`）**
> - **`[不 ready]`（`main.tex` `L183` 起所有后续章节）**：
>   - Section 3 Design（`L183–L351`）、Section 4 Implementation（`L352–L358`）、Section 5 Evaluation（`L360–L531`）、Section 6 Discussion（`L532–L545`）、Section 7 Related Work（`L546–L576`）与 Section 8 Conclusion（`L578–L580`）均已完成全文初稿与 `conference,compsoc` 12 页排版，均待作者审阅确认后升级为 `[ready]`。

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

### 2. Background and Motivation (`main.tex` `L143–L182`)
- [ready] **Section 2 Background and Motivation（全章锁定）**（已完整落实大佬两轮批注 `[R2-8]`–`[R2-10]` 并对齐 `AGENTS.md` 规范）
  - [ready] 2.1 Compiler-Instrumented Defenses (`L145–L149`，明确保护 `C and C++ systems software` 抵御 `unknown or unpatched vulnerabilities`，统一 `silently weakened or broken`，回应 `[R2-8]`、`[R2-9]`)
  - [ready] 2.2 Motivating Example (`L151–L173`，GCC `_FORTIFY_SOURCE` 潜伏 14 年静默放宽漏洞匿名化解析与代码块排版)
  - [ready] 2.3 Limitations of Existing Approaches (`L175–L181`，显式点明良性执行期间缓解机制从不触发 `[R2-10]`，并对齐静态检查/动态执行确定性 Oracle 表述)

### 3. Design of DeFenzz (`main.tex` `L183–L351`)
- [不 ready] **3.0 Section 3 Overview & Architecture**（`L183–L187`：已重写为 7 句因果动机推导并重绘对齐 `figures/method-overview.pdf`，待作者审阅确认）
- [不 ready] **3.1 Security Invariant Generation (Section 3.A)**（`L189–L226`：已对比替代方案、前置 `Listing 2: INV-FORT-014` 四架构结构、首次展开 `CoT`/`RAG` 并清零细碎举例，待作者审阅确认）
- [不 ready] **3.2 Compiler Source Mapping (Section 3.B)**（`L228–L250`：已论证黑盒/全覆盖/关键词检索失效原因与编译器内探针零二进制扰动优势，待作者审阅确认）
- [不 ready] **3.3 Programmatic Oracle Construction (Section 3.C)**（`L252–L315`：已理顺动态/静态检查器因果衔接、清零破折号与旁支举例，离线双门控下沉至 Section 4，待作者审阅确认）
- [不 ready] **3.4 Agentic Directed Fuzzing (Section 3.D)**（`L317–L350`：已点明 targeted fuzz drivers 测试防御假设与选择性防折叠优化两难，强化联合诊断与绑定 `m + FAIL` 约简放大，待作者审阅确认）

### 4. Implementation (`main.tex` `L352–L358`)
- [不 ready] **Section 4 Implementation**（`L352–L358`：已补充核心框架 40.2K 行代码量明细（27.0K Python / 12.5K Go / 0.7K TypeScript），并完整承接单函数/`.md`/手册切片、BM25+`sqlite-vec` 稠密向量 RRF、MCP 工具与 `fortify#b4e1` 探针重写、Go gRPC/Podman/QEMU 四架构执行、离线 Gate 1/2 校验及 C-Reduce 工程细节，待作者审阅确认）

### 5. Evaluation (`main.tex` `L360–L526`)
- [不 ready] **5.1 Experimental Setup**（`L370–L374`：交代 GCC 16.2.0 / LLVM 23.1.2、9700X+32G 硬件、DeepSeek-V4.1-Flash `1017`、5 个对比基线的公平输入对齐，以及统一用 `DeFenzz` checker 套件判定，待作者审阅确认）
- [不 ready] **5.2 Real-World Silent Defense Bugs (RQ1)**（`L400–L453`：`Table II` 111 新漏洞 / 30 确认 / 11 修复、`Fig. 3` 编译器与 ISA 分布（去主观严重度与非必要 `&`）、全章节双盲脱敏，以及 LoongArch64 canary 残留动态 checker + x86-64 非预期 `endbr64` 静态 checker 双案例，待作者审阅确认）
- [不 ready] **5.3 Comparison with Existing Fuzzers (RQ2)**（`L471–L475`：配合 `Table III` 与 `Fig. 4`，去掉原生 oracle 对比列与 Native 标签，聚焦同一预言机下基线止步 18 个漏洞而 `DeFenzz` 独占 93 个的原因，待作者审阅确认）
- [不 ready] **5.4 Ablation Study (RQ3)**（`L477–L504`：去掉 RAG 消融行，保留 `Table IV` 讲清离线 Check IR 与在线源映射/确定性检查器/受控编排的贡献，待作者审阅确认）
- [不 ready] **5.5 Practicality, Cost, and Overhead (RQ4)**（`L506–L532`：保留单栏 `Table V`，聚焦离线一次性复用、目标二进制 0.0% 开销与每漏洞 5.5 分钟在线成本，待作者审阅确认）

### 6. Discussion, Related Work, and Conclusion (`main.tex` `L532–L577`)
- [不 ready] **Section 6 Discussion**（`L532–L542`：三段——Cross-Defense RAG Transfer 跨防御历史经验迁移与发现、Generalizing to Other Compilers and Architectures 跨编译器与新架构泛化、Limitations 聚焦无法自动区分编译器漏洞与文档/注释笔误或滞后及未文档化假设与单次用户态观测边界，待作者审阅确认）
- [不 ready] **Section 7 Related Work**（`L543–L573`：编译器测试与防御验证、定向与 LLM 辅助 Fuzzing、规范提取与 Checker 生成三段对照，待作者审阅确认）
- [不 ready] **Section 8 Conclusion**（`L575–L577`：单段 6 句闭环收束全篇问题、机制与 111/30/11 实证成果，待作者审阅确认）
