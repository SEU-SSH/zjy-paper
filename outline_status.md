# DeFenzz - IEEE S&P 论文撰写与精校进度追踪 (Paper Writing Status)

> **状态定义说明**：
> 本文档严格执行**二值状态**规范——全篇仅存在 **`[ready]`** 与 **`[不 ready]`** 两种状态，坚决杜绝模糊中间态。
> - **`[ready]`**：已结合导师与大佬（Mat）两轮批注精校定稿并锁定，具备最高权威性，未经用户显式要求严禁修改。
> - **`[不 ready]`**：未定稿 / 待结合大佬二审意见修改 / 待对齐实证数据或补齐收尾章节。
>
> **当前状态汇总（对照 `main.tex` 与 [`mat_comments_list.md`](./mat_comments_list.md)）**：
> - **`[ready]`（`main.tex` `L1–L190`，Motivation 及之前全部章节已按大佬两轮意见修改定稿并锁定，已同步全篇 `\autoref` 与 `Motivation Example` 标题）**：
>   1. **Title & Abstract（标题与摘要，`L111–L125`）**
>   2. **Section 1 Introduction（第一章 引言，`L127–L149`）**
>   3. **Section 2 Background and Motivation（第二章 背景与动机，`L151–L190`）**
> - **`[不 ready]`（`main.tex` `L191` 起所有后续章节）**：
>   - Section 3 Design（`L191–L387`）、Section 4 Implementation（`L388–L394`）、Section 5 Evaluation（`L396–L618`）、Section 6 Discussion（`L620–L629`）、Section 7 Related Work（`L631–L658`）与 Section 8 Conclusion（`L660–L662`）均已完成全文扩充、故事线融合与 `conference,compsoc` 正文 **12.5 页**（`12.57p`，全文含参考文献 14 页）精确排版，均待作者审阅确认后升级为 `[ready]`。

---

## 逐章节精校状态列表

### 0. Title & Abstract (`main.tex` `L103–L117`)
- [ready] **Title & Abstract**（已结合大佬第一轮批注 `[R1-1]`–`[R1-4]`、`[R1-9]` 及最新漏洞统计 `111 / 30 / 11` 定稿锁定；二审无新批注）

### 1. Introduction (`main.tex` `L119–L141`)
- [ready] **Section 1 Introduction（全章锁定）**（已完整落实大佬两轮批注 `[R1-4]`–`[R1-11]` 与 `[R2-1]`–`[R2-7]`；2026-11-18 按第三轮 `[R3-1]`–`[R3-9]` 压缩半页、引用 LangSec correctness-security gap、Fig. 1 改黄/橙配色，详见 `mat_comments_list.md` 第三节）
  - [ready] 1.1 Scope, Cross-ISA Lowering & UB vs. Mitigation Conflict (`L121`, `[R1-5]`, `[R1-6]`, `[R2-1]`, `[R2-2]`, `[R2-8]`)
  - [ready] 1.2 Silent Defense Failures & Running Example CVE-2023-4039 (`L123`, `[R1-2]`, `[R1-7]`, `[R2-3]`, `[R2-9]`)
  - [ready] 1.3 Post-Compilation Verification & Two Barriers in Prior Work (`L125`, `[R1-2]`, `[R1-6]`, `[R1-8]`)
  - [ready] 1.4 Central Question, Core Insight & LLM Role (`L127`, `[R1-4]`, `[R1-8]`, `[R1-9]`, `[R1-10]`, `[R2-4]`)
  - [ready] 1.5 Three Challenges & `Check IR` Accuracy Grounding (`L129`, `[R1-10]`, `[R1-11]`, `[R2-5]`, `[R2-6]`)
  - [ready] 1.6 Evaluation Summary & Four Contributions with Compiler Versions (`L131–L141`, `[R1-10]`, `[R2-7]`)

### 2. Background and Motivation (`main.tex` `L143–L182`)
- [ready] **Section 2 Background and Motivation（全章锁定）**（已完整落实大佬两轮批注 `[R2-8]`–`[R2-10]` 并对齐 `AGENTS.md` 规范）
  - [ready] 2.1 Compiler-Instrumented Defenses (`L145–L149`，明确保护 `C and C++ systems software` 抵御 `unknown or unpatched vulnerabilities`，统一 `silently weakened or broken`，回应 `[R2-8]`、`[R2-9]`)
  - [ready] 2.2 Motivation Example (`L159–L181`，标题与正文统一改为 `Motivation Example`，GCC `_FORTIFY_SOURCE` 潜伏 14 年静默放宽漏洞匿名化解析与代码块排版)
  - [ready] 2.3 Limitations of Existing Approaches (`L175–L181`，显式点明良性执行期间缓解机制从不触发 `[R2-10]`，并对齐静态检查/动态执行确定性 Oracle 表述)

### 3. Design of DeFenzz (`main.tex` `L183–L379`)
- [不 ready] **3.0 Section 3 Overview & Architecture**（`L183–L187`：已重写为 7 句因果动机推导并重绘对齐 `figures/method-overview.pdf`，待作者审阅确认）
- [不 ready] **3.1 Security Invariant Generation (Section 3.A)**（`L189–L226`：已对比替代方案、前置 `Figure 4: INV-FORT-014` 四架构结构、首次展开 `CoT`/`RAG` 并清零细碎举例，待作者审阅确认）
- [不 ready] **3.2 Compiler Source Mapping (Section 3.B)**（`L228–L250`：已论证黑盒/全覆盖/关键词检索失效原因与编译器内探针零二进制扰动优势，待作者审阅确认）
- [不 ready] **3.3 Programmatic Oracle Construction (Section 3.C)**（`L252–L343`：已补齐 `Check IR` 静态/动态查询原语设计段落与 `Table 2` 原语表，并在设计层阐明离线检查器结构与参考构建验证的必要性，待作者审阅确认）
- [不 ready] **3.4 Agentic Directed Fuzzing (Section 3.D)**（`L345–L378`：已点明 targeted fuzz drivers 测试防御假设与选择性防折叠优化两难，强化联合诊断与绑定 `m + FAIL` 约简放大，待作者审阅确认）

### 4. Implementation (`main.tex` `L380–L386`)
- [不 ready] **Section 4 Implementation**（`L380–L386`：已补充核心框架 40.2K 行代码量明细（27.0K Python / 12.5K Go / 0.7K TypeScript），并完整承接单函数/`.md`/手册切片、BM25+`sqlite-vec` 稠密向量 RRF、MCP 工具与 `fortify#b4e1` 探针重写、Go gRPC/Podman/QEMU 四架构执行、离线 Gate 1/2 校验及 C-Reduce 工程细节，待作者审阅确认）

### 5. Evaluation (`main.tex` `L388–L610`)
- [不 ready] **5.1 Experimental Setup**（`L398–L402`：交代 GCC 16.2.0 / LLVM 23.1.2、9700X+32G 硬件、DeepSeek-V4.1-Flash `1017`、5 个对比基线的公平输入对齐、逐机制独立编译与 UBSan 洁净过滤，以及统一用 `DeFenzz` checker 套件判定，待作者审阅确认）
- [不 ready] **5.2 Real-World Silent Defense Bugs (RQ1)**（`L465–L545`：`Table 3` 111 新漏洞 / 30 确认 / 11 修复、`Table 4` 离线三阶段统计、`Figure 9` 编译器阶段与 ISA 分布详解、131 候选剔除 20 非漏洞口径，以及 GCC LoongArch64 canary 残留 + GCC x86-64 非预期 `endbr64` + LLVM AArch64 SafeStack/SVE 槽位溢出三案例（全脱敏），待作者审阅确认）
- [不 ready] **5.3 Comparison with Existing Fuzzers (RQ2)**（`L541–L547`：配合 `Table 5` 与 `Figure 13`，详述五基线并集 28 个 vs. `DeFenzz` 111 个（83 个独占、0 漏报）、浅层探针覆盖（79.7% vs. 79.6%）与深层检查器激活（20.7% vs. 92.2%）的反差及 `F1`–`F6` 分布机制，待作者审阅确认）
- [不 ready] **5.4 Ablation Study (RQ3)**（`L549–L578`：配合 `Table 6` 展开离线 `w/o Check IR` 与在线 41 不变量切片各消融变体的具体失效机制，待作者审阅确认）
- [不 ready] **5.5 Practicality, Cost, and Overhead (RQ4)**（`L580–L610`：配合 `Figure 14` Agent 工具调用分布（99,236 次 vs. `w/o Check IR` 18,495 次）与 `Table 7` Token/构建/运行时开销统计，聚焦一次性离线摊销、目标二进制 0.0% 开销与每漏洞 5.5 分钟在线成本，待作者审阅确认）

### 6. Discussion, Related Work, and Conclusion (`main.tex` `L620–L662`)
- [不 ready] **Section 6 Discussion**（`L641–L651`：三段——Cross-Defense RAG Transfer 已改为仅陈述自身实证结果（`17` 条跨防御不变量 = `12` GCC + `5` LLVM，暴露 `2` 个手册未提及的未知静默漏洞）；Generalizing to Other Compilers and Architectures 跨编译器与新架构泛化；Limitations 聚焦文档/注释误差与单次用户态观测边界，待作者审阅确认）
- [不 ready] **Section 7 Related Work**（`L631–L658`：已按导师意见融合全篇主线重写三段——分别紧扣「编译后 Oracle Gap 与单一防御检测局限」「防御分支定位与耦合前提条件引导」「外部安全契约与多架构确定性二进制/运行时检查器」，篇幅精准保持不变，待作者审阅确认）
- [不 ready] **Section 8 Conclusion**（`L660–L662`：单段 6 句闭环收束全篇问题、机制与 111/30/11 实证成果，待作者审阅确认）
