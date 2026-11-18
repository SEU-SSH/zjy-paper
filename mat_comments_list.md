# 大佬两轮批注完整档案与当前稿件对照（自包含版）

> **文档用途**：完整、逐字收录大佬（Mat）对论文草稿的两轮全部批注（位置、视觉标记、被批注英文原文、批注英文原话），并精确映射至当前工作区 `main.tex` / `main.pdf` 的具体行号与落实状态。新开会话无需再读取任何批注 PDF。
>
> **🔒 当前锁定边界声明（2026-11-14 更新，同步 [`outline_status.md`](./outline_status.md) 与 [`AGENTS.md`](./AGENTS.md)）**：
> - **`Title` + `Abstract` + `Section I Introduction` + `Section II Motivation`（`main.tex` `L1–L182`）已结合大佬两轮意见全部修改定稿并锁定（`[ready]`）**，对应前 21 条批注（`[R1-1]`–`[R1-11]`、`[R2-1]`–`[R2-10]`）在该范围内均已处理完毕，未经用户显式要求禁止再改动 `L1–L182`。
> - **`Section III Design`（`L183–L353`）与 `Section IV Implementation`（`L354–L360`）及图 2（`figures/method-overview.pdf`）已完成大刀阔斧重构（待作者审阅确认后锁定 `[ready]`）**：全面落实大佬邮件整体总评 `[R2-0]` 与页内批注 `[R2-11]`–`[R2-15]`、`[R1-3]`、`[R2-5]`、`[R2-6]`。
> - **后续待改范围聚焦于 `L362` 起（`[不 ready]`）**：即 `Section V Evaluation`（`L362–L557`）及待补齐的 `Section VI+` 收尾章节。

## 版本演进关系

1. **V1 — 第一轮批注稿**：`defuzz_abstract_intro-mat.pdf`（共 2 页，仅含 Title + Abstract + Section I Introduction），含 **11 处**绿色批注（`[R1-1]`–`[R1-11]`）。
2. **V2 — 第二轮批注稿**：`defuzz-before-impl-mat.pdf`（共 7 页，含根据 V1 修订后的 Title + Abstract + Section I，以及首次送审的 Section II Motivation、Section III Design、Section IV Implementation；仓库内无批注同源底稿为 `defenzz-before-impl.pdf`），含 **1 封整体邮件总评（`[R2-0]`）** 与 **15 处**页内绿色批注（`[R2-1]`–`[R2-15]`，分布在 Page 1–6；**V2 的 Abstract 与 Page 7 无新批注**）。
3. **当前稿件（`main.tex` / `main.pdf`）**：共 **562 行**、**11 页**，系统名统一为 `DeFenzz`（`DEFENZZ_HIT` / `DEFENZZ_LOG`），漏洞统计同步为 `111 / 30 / 11`：
   - **已完成锁定区（`L1–L182`，`[ready]`）**：Title（`L103`）、Abstract（`L113–L117`）、Section I Introduction（`L119–L141`，含 `cb97d07` 对 Challenge 2 `Check IR` 准确性论证与 `GCC 16.2.0 / LLVM 23.1.2` 版本号的更新）以及 Section II Motivation（`L143–L182`，已完成 `[R2-8]`–`[R2-10]` 全部修订）均已根据大佬两轮意见修改定稿；
   - **已完成大改待审区（`L183–L360`，暂标 `[不 ready]` 待作者确认）**：Section III Design（`L183–L353`）与 Section IV Implementation（`L354–L360`）已依据大佬整体邮件 `[R2-0]`、`[R2-11]`–`[R2-15]` 及 `plain-paper-writing` 规范彻底重构——Section III 全面转向阐述每一步设计的必要性（`WHY`）与相比替代方案的优势，并将工程实现细节（`HOW`）完整下沉至 Section IV；`figures/method-overview.pdf` 图内术语已同步更新对齐；
   - **后续评估章节（`L362–L557`，`[不 ready]`）**：Section V Evaluation（末尾 `L559–L562` 接参考文献与文档结束，待补齐消融 `TBD` 及 Section VI+ 收尾章节）。

---

## 零、大佬第二轮整体邮件意见（Overall Email Feedback — Design 与 Implementation 重构总纲）

### [R2-0] 第二轮审稿随信整体意见（全文逐字收录）

```text
Thanks for sharing the draft. I made comments throughout the paper. One
concern is that the design is very abstract and fuzzy, making it
extremely hard to follow. The design essentially explains _HOW_ you do
it, not _WHY_ you do it.

For a good paper, I like reading the reason why a solution is necessary,
why each step makes sense, and how it is better than any of the
alternatives. This is missing in the current version.

You could almost rename the design section into implementation and write
a new design section to cover these design decisions ;)

Looking at the technique. my thought was to push for automatically
generated fuzz drivers that form hypotheses testing different mitigation
abstractions that result in triggerable failure conditions, allowing you
to distinguish a mitigation catching exploitation and silent errors --
inverting the flags where non-crashes signal errors.

Let me know when you have an updated draft/what I should look for. Also
happy to expand/discuss if you have questions.
```

### 核心拆解与当前 `main.tex`（`L183–L360`）落实映射

1. **从讲 `_HOW_` 彻底转向讲 `_WHY_` 与替代方案对比（`why a solution is necessary, why each step makes sense, and how it is better than any of the alternatives`）**：
   - **Overview（`L187`）**：删除 V2 机械的 `First/Second/Third/Finally` 流水账复述，改为从编译后防御测试颠覆传统模糊测试假设切入，用因果链推导出为何必须依次引入外部安全不变量、编译器分支映射、形式化原语检查器与定向种子合成四个耦合阶段。
   - **Section III-A（`L191, L208, L210`）**：先论证为何差分测试（良性输入不触发防御）、从编译器自身代码/产物反推规范（把已有 bug 当作规范）与纯人工编写形式化规范（跨数十种防御与多 ISA 无法扩展）均不可行；再论证为何直接裸问 LLM（捏造标志）或喂完整源码（混入带 bug 实现）不可行，必须锚定声明式权威契约源；最后论证为何手册遗漏边缘情形而直接搜原始补丁仅命中原函数，必须做去机制化的跨防御根因迁移。同时将具体示例 `Listing 2: INV-FORT-014`（覆盖全部 4 个目标架构 `x86_64, aarch64, riscv64, loongarch64`）前置到开篇第 1 段之后，彻底消除 Page 4 `[ ? ]`。
   - **Section III-B（`L230, L232, L250`）**：先论证为何黑盒随机生成（极少进入防御逻辑）、全编译器灰盒覆盖（数百万常规优化分支淹没防御分支）与纯关键词检索（前端标志跨越中端 pass / target hook / 后端 `.md` 内部异名）均失效；再论证为何必须结合静态导航工具按 `pass -> function -> branch` 逐层收敛，并在编译器内部而非目标二进制中注入轻量探针以保证目标代码生成与栈布局零扰动。
   - **Section III-C（`L254, L256, L286, L296, L317`）**：正面对比四种预言机构建替代方案（纯手工逐架构编写不可扩展、在线 LLM 裁判慢且易产生底层 ISA 幻觉、让 LLM 从零写原始解析器易误读汇编语法或目标 ABI 规则、单一声明式公式无法表达跨多调用点或多指令的迭代检查），引出 $\mathcal{T}_i + \Omega + \text{高层循环/条件逻辑}$ 的解耦设计；剥离零散旁支举例与破折号插入语，仅保留贯穿全文的 `_FORTIFY_SOURCE`（`INV-FORT-014`）静态检查器与栈金丝雀越界动态检查器一静一动两个示例；补充四态裁决（`ERROR / NA / PASS / FAIL`）与离线双门控验证（`Gate 1: Well-Formedness` 与 `Gate 2: Differential Anchoring`）。
   - **Section III-D（`L346, L348, L350, L352`）**：对比随机生成器与无约束自由 Agent 的漂移问题，点明为何必须采用有界 $B$ 轮确定性编排；剖析种子合成的**优化两难**（不加屏障会被早期常量折叠/死代码消除抹掉测试缓冲区 vs. 全局滥加 `volatile` 会直接关闭触发静默漏洞的中端优化）；论证为何分支轨迹与检查器裁决缺一不可；论证为何传统保退出码约简会删掉防御触发逻辑，必须绑定 `m + FAIL` 约简并做同源放大。
2. **Design 与 Implementation 彻底分离（`rename the design section into implementation and write a new design section`）**：
   - 将原 Section III 中的全部工程实现细节——包括源码单函数切片与 `.md` / 手册切分规则、BM25 下划线子词切分 + `sqlite-vec` 稠密向量检索 + Reciprocal Rank Fusion 融合排序、`clangd` / CodeQL / Tree-sitter MCP 工具栈、AST 重写器哈希生成 `fortify#b4e1` 及 `DEFENZZ_LOG` 环境变量零开销门控、Go gRPC 服务与 rootless Podman + 四架构 QEMU 容器沙箱、Go AST/类型检查（Gate 1）与自动差分构建（Gate 2）、C-Reduce 包装器及内容寻址重放账本——全部干净迁移至 **Section IV Implementation（`L354–L360`）**，并在 `Listing 5` 中剥离 `package` / 语言样板噪声。
3. **自动生成测试假设的 Fuzz Drivers 与“反转崩溃标志”洞察（`automatically generated fuzz drivers that form hypotheses testing different mitigation abstractions... inverting the flags where non-crashes signal errors`）**：
   - 在 **Section III-A（`L191`）** 与 **Section III-D（`L348`）** 明确将每条不变量建模为可测试的防御假设（`precond / rule / signal`），并将 Generator Agent 合成的种子明确定位为针对特定防御假设的 **targeted fuzz drivers**（包含受控越界输入以触发缓解边界）；
   - 在 **Section III-C 首段（`L254`）与动态示例（`L296`）** 专门阐明**反转运行时失败信号（inverting the failure signal）**：传统模糊测试把崩溃当 bug、把正常退出当正确；而测试运行时防御恰好相反——跨越受保护边界时，完好的缓解机制必须主动中止执行（`PASS`），**越界后不崩溃正常返回（non-crash）才暴露静默防御漏洞（`FAIL`）**；同时简明补足硬件辅助指令休眠与编译产物静态可见性为何仍需静态检查器配合。

---

## 全部批注速查索引（1 封整体邮件总评 + 26 处页内批注）

| 编号 | 批注所在章节与段落 | 大佬批注原话核心摘录 | 当前 `main.tex` 状态与行号 |
| :--- | :--- | :--- | :--- |
| **R2-0** | 第二轮审稿随信整体总评 | `The design essentially explains _HOW_ you do it, not _WHY_ you do it... better than any of the alternatives... fuzz drivers that form hypotheses... inverting the flags where non-crashes signal errors` | `✅ 已完成大改待审`（Sec III `L183–L353` 重写 `WHY` 与替代方案对比 + 反转崩溃语义；Sec IV `L354–L360` 承接全部 `HOW`） |
| **R1-1** | Abstract 第 1 段第 1 句 | `form a last line of protection against the exploitation of software flaws such as ..` | `✅ 已完成锁定`（`L114`） |
| **R1-2** | Abstract 第 1 段第 3 句（`CVE-2023-4039`） | `fairly old` | `✅ 已完成锁定`（`L114, L123` 保留经典 CVE；`L125, L153` 搭配潜伏 14 年新修复漏洞） |
| **R1-3** | Abstract 第 2 段第 2 句（`CoT and RAG`） | `expand CoT / RAG (this is not an AI conf)` | `✅ Abstract 已锁定 & Sec III 已展开`（`L116` 已展开；正文首次出现处 `L208, L210` 已完整展开，Overview `L187` 已移除缩写） |
| **R1-4** | Abstract 第 2 段第 4 句前 | `define violations first` | `✅ 已完成锁定`（`L116, L127` 均已补入 defense violation 定义） |
| **R1-5** | Sec I Intro 第 1 段第 1 句（`software`） | `in what software?` | `✅ 已完成锁定`（`L121, L147` 均已明确为 `C and C++ systems software`） |
| **R1-6** | Sec I Intro 第 1 段末三句 | `compiler does not distinguish between security checks and regular code, so there is no explicit barrier... best bet is to check... after the compilation` | `✅ 已完成锁定`（`L121, L125, L127` 已完整体现无显式屏障及编译后检查推论） |
| **R1-7** | Sec I Intro 第 3 段第 4 句末（oracle gap） | `the lack of mitigation would only be detected if the program executes outside of the language semantics...` | `✅ 已完成锁定`（`L123` Intro 与 `L177` Sec II-C 均已明确写出） |
| **R1-8** | Sec I Intro 第 3 段末句 & 第 4 段首句 | `the LLM spin is weird. this is not a good explanation why LLMs can't stop these attacks` | `✅ 已完成锁定`（`L125, L127` 已移除突兀 LLM 表述并重构问题引入） |
| **R1-9** | Sec I Intro 第 4 段第 2 句（`DEFUZZ`） | `DeFenceFuzz?` | `✅ 已完成锁定`（`L103, L116, L127` 全篇定名 `DeFenzz` / `Defense Fuzzer`） |
| **R1-10** | Sec I Intro 第 4 段第 3 句（`security invariants`） | `defining those is a contribution` | `✅ 已完成锁定`（`L129, L137` Challenge 1 与 Contribution 1 均突出定义贡献） |
| **R1-11** | Sec I Intro 第 5 段（Challenge 2 后半段） | `the LLM angle is not clear` | `✅ 已完成锁定`（`L127` 先交代引入 LLM 动因，`L129` 明确 LLM 组合 `Check IR` 原语与 $\mathcal{T}_i$） |
| **R2-1** | Sec I Intro 第 1 段中部（跨 ISA 下沉处） | `key challenge: mitigations assume language properties are violated (undefined behavior) while optimizations assume the properties hold...` | `✅ 已完成锁定`（`L121` 已插入语言层 UB 与缓解假设冲突） |
| **R2-2** | Sec I Intro 第 1 段后部（无显式屏障处） | `this side is a good technical description on why barriers are not implemented. but I would like to highlight the language level aspect as well...` | `✅ 已完成锁定`（`L121` 紧邻无显式屏障前补充语言层 UB 冲突） |
| **R2-3** | Sec I Intro 第 2 段首句（`goes wrong`） | `unclear what going wrong means` | `✅ 已完成锁定`（`L123` 已具象化为中端优化放宽/移除检查与后端违反 ISA 规则） |
| **R2-4** | Sec I Intro 第 4 段中部（`Because LLM-assisted...`） | `unclear that LLMs were used. Do you want to keep this more genreal? Customization is fine but a choice` | `✅ 已完成锁定`（`L127` 已前置说明人工不可行、离线引入 LLM 提取与转换并锁定定稿） |
| **R2-5** | Sec I Intro 第 5 段 Challenge 2（`verify` / `formalizing`） | `fully safe? proven? validated?` | `✅ Intro 已锁定 & Sec III-C 已对齐待审`（`L129` 已锁定；`L256, L317` 已对齐 `Check IR` + $\mathcal{T}_i$ + 离线双门控验证且零 `verify/proven` 越界词） |
| **R2-6** | Sec I Intro 第 5 段 Challenge 2（`with zero LLM involvement in bug`） | `not sure "zero LLM involvement" is a good distinction` | `✅ Intro 已锁定 & Sec III-C 已改待审`（`L129` 已锁定；`L317` 已改为 `directly tests each compiled seed without LLM judgment`；Sec V `L380` 留待评估章处理） |
| **R2-7** | Sec I Intro 第 6 段 & Contribution 4 底部 | `what versions of GCC / LLVM ? Would it make sense to build a benchmark of old versions to test ground truth / well known old bugs?` | `✅ Intro 已锁定 / ⏳ Sec V & VI 待对齐`（`L133, L140` 已补齐 `GCC 16.2.0 and LLVM 23.1.2`；历史漏洞讨论留待后文对齐） |
| **R2-8** | Sec II-A 第 1 段首句（`security threats`） | `unknown or unpatched vulnerabilities` | `✅ 已完成锁定`（`L121, L147` 均已改为 `against the exploitation of unknown or unpatched vulnerabilities`） |
| **R2-9** | Sec II-A 第 2 段末句（`quietly`） | `silently` | `✅ 已完成锁定`（`L123, L149` 均已改为 `silently weakened or broken`；Abstract `L114` 按注册锁定保持原样） |
| **R2-10** | Sec II-C 第 1 段（Oracle Gap 段） | `say explicitly that during benign executions, the mitigation is never triggered` | `✅ 已完成锁定`（`L177` 已显式补入 `During benign executions, the mitigation is never triggered...`） |
| **R2-11** | Sec III Overview 段（Page 4 左栏顶部） | `this paragraph does not add much`（并圈出 `CoT` 与 `RAG`） | `✅ 已完成大改待审`（`L185–L187` 删去流水账复述与未展开缩写，改为 7 句因果动机推导；图 2 标签同步更新） |
| **R2-12** | Sec III-A 标题、第 1–2 段 & 右栏 `[ ? ]` | `this is very abstract and opaque. it's not clear what data you extract and how it looks like` / `creating a set of targets (fuzz drivers)...` | `✅ 已完成大改待审`（`L191–L206` 开篇即前置展示 `Listing 2: INV-FORT-014` 三字段结构，并在 `L191, L348` 呼应可测试假设与 targeted fuzz drivers） |
| **R2-13** | Sec III-A 第 3 段（Hybrid RAG 检索细节）& 全局设计 | `across the design you're using very complex and convoluted language to explain simple concepts. simplify and go for the gist, then dive deeper in the implementation section...` | `✅ 已完成大改待审`（全节遵循 15–25 词平实句法，切片、BM25/RRF、MCP/AST 哈希、gRPC/Podman/C-Reduce 全部下沉至 Sec IV `L354–L360`） |
| **R2-14** | Sec III 跨栏总评（Page 5 顶部） | `the big issue: you describe what you do, not why you do each step... from reading this section, I know what the approach does but not why` | `✅ 已完成大改待审`（`L183–L353` 每一小节均先论证问题本质与替代方案失效原因，再导出 `DeFenzz` 设计决策） |
| **R2-15** | Sec III-D 第 2 段（Generator Agent 多语句合成段） | `this part makes sense, create hypotheses that test mitigations and mitigation constraints. then use fuzzing to validate it` | `✅ 已完成强化待审`（`L348` 完整保留多语句耦合构造与选择性防折叠精髓，进一步点明 targeted fuzz drivers 测试防御假设与优化两难） |

---

## 一、第一轮批注详单（V1：`defuzz_abstract_intro-mat.pdf`，共 11 处）

### [R1-1] Abstract — 第 1 段第 1 句（Page 1 左栏第 2–3 行）
- **视觉标记**：绿色横线划除 `protect software against security threats,`，并在该行正上方写入绿色替换文本。
- **V1 被批注原文**：
  > Compiler-instrumented defenses (e.g., stack canaries, Control-Flow Integrity (CFI), and `_FORTIFY_SOURCE`) ~~protect software against security threats,~~ such as memory corruption, control-flow hijacking, and data leakage.
- **大佬批注原文**：
  > `form a last line of protection against the exploitation of software flaws such as ..`
- **V2 与当前 `main.tex`（`L114`）对应状态**：V2 已按原话修改，Round 2 无新批注；当前 `main.tex`（`L114`）保持一致：
  > `Compiler-instrumented defenses (e.g., stack canaries, Control-Flow Integrity (CFI), and \texttt{\_FORTIFY\_SOURCE}) form a last line of protection against the exploitation of software flaws, such as memory corruption, control-flow hijacking, and data leakage.`

### [R1-2] Abstract — 第 1 段第 3 句（Page 1 左栏第 7 行左侧空白）
- **视觉标记**：在 `example, in CVE-2023-4039,` 左侧页边距写绿色短评（无划线）。
- **V1 被批注原文**：
  > For example, in **CVE-2023-4039**, dynamic stack allocation allowed an overflow to bypass the GCC stack canary on AArch64.
- **大佬批注原文**：
  > `fairly old`
- **V2 与当前 `main.tex`（`L114, L123, L125, L153`）对应状态**：Abstract（`L114`）与 Intro 第 2 段（`L123`）保留经典的 `CVE-2023-4039`，同时在 Intro 第 3 段（`L125`）和 Section II-B（`L153`）搭配 2026 年新修复的潜伏 14 年漏洞 `GCC PR 125079`。Round 2 大佬未再对此处留评。

### [R1-3] Abstract — 第 2 段第 2 句（Page 1 左栏第 19–20 行左侧空白）
- **视觉标记**：在 `specifications, and historical bug fixes using a hybrid CoT and` / `RAG pipeline.` 左侧页边距写绿色批注。
- **V1 被批注原文**：
  > DEFUZZ first extracts security invariants from compiler source code, Instruction Set Architecture (ISA) specifications, and historical bug fixes using a hybrid CoT and RAG pipeline.
- **大佬批注原文**：
  > `expand CoT / RAG (this is not an AI conf)`
- **V2 与当前 `main.tex`（`L116, L208, L210`）对应状态**：✅ **Abstract 已锁定 & Sec III 正文首次出现处已展开**
  - V2 与当前 `main.tex`（`L116`）在 Abstract 中已展开为 `using a hybrid Chain-of-Thought (CoT) and Retrieval-Augmented Generation (RAG) pipeline.`。
  - 当前重构后的 Section III Overview（`L185, L187`）已彻底移除未展开的 `CoT` 与 `RAG` 缩写；正文首次出现处位于 Section III-A，均已完整展开：`Chain-of-Thought (CoT) prompting`（`L208`）与 `Retrieval-Augmented Generation (RAG)`（`L210`），其后方可使用缩写（如 Implementation `L356` 与 Evaluation `L381+`）。

### [R1-4] Abstract — 第 2 段第 3–4 句之间（Page 1 左栏第 23 行左侧空白）
- **视觉标记**：左侧页边距写绿色批注，并画一条绿色弧线精准指向 `and controlled.` 与 `To detect violations reliably,` 之间的空隙。
- **V1 被批注原文**：
  > It then maps these invariants to compiler passes and decision branches, locating where defenses are implemented and controlled. **[↖插入点]** To detect violations reliably, DEFUZZ formalizes these invariants in a predicate IR and lowers them into programmatic bug oracles, implementing them as static and dynamic checkers across target ISAs.
- **大佬批注原文**：
  > `define violations first`
- **V2 与当前 `main.tex`（`L116, L127`）对应状态**：
  - V2 与当前 `main.tex`（`L116`）均在该插入点补入定义句：`Here, a defense violation occurs when a compiled program fails to preserve the required protection rule.`（Round 2 无新批注）。
  - 当前 `main.tex` 在 Intro 第 4 段（`L127`）首次引出 `security invariants` 时也同步补入：`where any compiled binary breaking a required rule constitutes a defense violation.`

### [R1-5] Section I Introduction — 第 1 段第 1 句（Page 1 左栏下部第 2 行）
- **视觉标记**：绿色下划线标出 `harden software` 中的 `software`，并拉一条绿色竖线向上指到 `I. INTRODUCTION` 标题右侧的绿色提问。
- **V1 被批注原文**：
  > Compilers deploy a wide range of compiler-instrumented defenses to harden <u>software</u> against security threats, such as memory corruption, control-flow hijacking, and sensitive data leakage.
- **大佬批注原文**：
  > `in what software?`
- **V2 与当前 `main.tex`（`L121`）对应状态**：V2 改为 `harden C and C++ systems software against security threats...`；当前 `main.tex`（`L121`）结合 `[R2-8]` 定稿为：
  > `Compilers deploy a wide range of compiler-instrumented defenses to harden C and C++ systems software against the exploitation of unknown or unpatched vulnerabilities, such as memory corruption, control-flow hijacking, and sensitive data leakage.`

### [R1-6] Section I Introduction — 第 1 段末尾（Page 1 左栏底部最后 3 行至右栏顶部）
- **视觉标记**：绿色竖线括住左栏最后 3 行（`into machine instructions across diverse target ISAs... stack frame`），绿色弯箭头向下指向底边距的 6 行长批注。
- **V1 被批注原文**：
  > Defense code must interact with complex optimization passes and translate abstract protection rules **[左栏竖线起]** into machine instructions across diverse target ISAs. This translation relies on strict assumptions about object bounds, instruction semantics, register conventions, and stack frame **[左栏竖线止，接右栏顶]** layouts. When the implementation of a defense mechanism fails to match these ISA or optimization assumptions, its security protection breaks from within.
- **大佬批注原文**：
  > `I would also say that the compiler does not distinguish between security checks and regular code, so there is no explicit barrier. The mitigation passes try to retrofit these barriers as good as they can but it's not modelled explicitly. But it would be too expensive to model them (both in lost optimization and cost of rewriting the compiler). So the best bet is to check for correctness of placed mitigations after the compilation, alas your solution`
- **V2 与当前 `main.tex`（`L121, L125, L127`）对应状态**：
  - V2 在第 1 段末尾补入了关于安全检查无显式屏障、全流水线建模代价过高的 3 句话，大佬在 Round 2 `[R2-2]` 中评价其为 `good technical description`，同时在 `[R2-1, R2-2]` 要求补充语言层 UB 假设冲突。
  - 当前 `main.tex` 除了保留第 1 段末尾解释（`L121`），还在第 3 段开头（`L125`）补齐了大佬批注最后一句的推论：`Because modeling explicit barriers across the compiler pipeline is impractical, our best bet is to check the correctness of placed mitigations after compilation.`，并在第 4 段首句设问（`L127`）中呼应 `how can we systematically verify placed mitigations after compilation...`。

### [R1-7] Section I Introduction — 第 3 段第 4 句末（Page 1 右栏中部 `oracle gap` 处）
- **视觉标记**：在 `...crash and differential oracles remain blind when a defense is weakened or broken.` 句末 `broken.` 右侧标绿色短横，拉一条长绿色弧线沿右页边距一直引向右下角的 3 行批注。
- **V1 被批注原文**：
  > The first barrier of existing fuzzers is the **oracle gap**. Widely used compiler fuzzers (e.g., Csmith [2] and YARPGen [3]) check for compiler crashes or output mismatches across optimization levels. Because a binary with a broken defense still produces correct outputs on benign inputs, crash and differential oracles remain blind when a defense is weakened or broken. **[↗绿色引线起点]**
- **大佬批注原文**：
  > `the lack of mitigation would only be detected if the program executes outside of the language semantics, that's why the violations are not detected during regular executions`
- **V2 与当前 `main.tex`（`L123`）对应状态**：V2 将该解释合入 **Intro 第 2 段第 2 句**，当前 `main.tex`（`L123`）原样保留：
  > `Because the lack of a mitigation is only detected when the program executes outside standard language semantics, regular executions on benign inputs run normally, allowing standard functional tests to pass completely while leaving the software exposed to attack.`
  *(注：Section II-C 同类位置的进一步批注见 `[R2-10]`。)*

### [R1-8] Section I Introduction — 第 3 段末句与第 4 段首句（Page 2 左栏顶部第 1–4 行）
- **视觉标记**：绿色括号 `[ ... >` 框住 Page 2 左栏第 1 行 `suffer from severe hallucinations and false bug reports.`，并向上引线至页眉批注。
- **V1 被批注原文**：
  > *(接 Page 1 右栏底)* Meanwhile, building static analyzers demands heavy manual effort from experts to craft custom rules for each defense mechanism and target ISA, while unconstrained LLM agents **[Page 2 框选：]** `suffer from severe hallucinations and false bug reports.`
  > These barriers raise a central question: how can we systematically detect silent defense failures when neither the buggy compiler nor direct LLM judgment provides a reliable oracle?
- **大佬批注原文**：
  > `the LLM spin is weird. this is not a good explanation why LLMs can't stop these attacks`
- **V2 与当前 `main.tex`（`L125, L127`）对应状态**：
  - V2 删除了第 3 段末尾的 `, while unconstrained LLM agents suffer from severe hallucinations and false bug reports`，但遗留了第 4 段首句中的 `nor direct LLM judgment`，引发了 Round 2 的 `[R2-4]`。
  - 当前 `main.tex`（`L125, L127`）已同步将第 4 段首句改为：`These barriers raise a central question: how can we systematically verify placed mitigations after compilation when the buggy compiler itself cannot serve as a reliable oracle?`

### [R1-9] Section I Introduction — 第 4 段第 2 句（Page 2 左栏上部第 5 行）
- **视觉标记**：从 `we present DEFUZZ,` 中的 `DEFUZZ` 向右上拉绿色斜线至左栏与 Fig. 1 之间的空白处。
- **V1 被批注原文**：
  > To answer this question, we present **DEFUZZ**, an invariant-directed agentic framework for testing compiler-instrumented defenses.
- **大佬批注原文**：
  > `DeFenceFuzz?`
- **V2 与当前 `main.tex`（`L103, L116, L127`）对应状态**：V2 补充了全称提示 `DEFUZZ (Defense Fuzzer)`；当前 `main.tex` 全篇定名为 `\textsc{DeFenzz}`（首次出现写为 `\textbf{\textsc{DeFenzz}} (\textbf{Defen}se Fu\textbf{zz}er)`）。

### [R1-10] Section I Introduction — 第 4 段第 3 句（Page 2 左栏中上部第 9–10 行）
- **视觉标记**：绿色折角括号框出跨行的 `security invari-` / `ants.`，左侧页边距写绿色批注。
- **V1 被批注原文**：
  > Our core insight is that although defense implementations vary across backends, their intended security guarantees follow target-independent **[框选：]** *security invariants.*
- **大佬批注原文**：
  > `defining those is a contribution`
- **V2 与当前 `main.tex`（`L129, L137`）对应状态**：V2 与当前 `main.tex` 均在 Challenge 1（`L129`：`defining and establishing reliable security invariants... define machine-checkable security contracts`）及 Contribution 1（`L137`：`**Security Invariant Definition and Extraction:** We define target-independent security invariants...`）明确将其列为贡献点。Round 2 无新批注。

### [R1-11] Section I Introduction — 第 5 段 Challenge 2 后半段（Page 2 左栏中下部）
- **视觉标记**：左侧页边距画绿色竖线，括住 `and dynamic checkers. Dual static-dynamic cross-checking` 至 `adjudication.` 共 6 行。
- **V1 被批注原文**：
  > The second challenge is checking these invariants with high accuracy across diverse ISAs, where distinct registers and stack layouts cause direct LLM judgment to hallucinate. DEFUZZ addresses this by formalizing each invariant in a predicate IR parameterized by target ISA specifications, lowering it into ISA-specific static **[竖线起]** and dynamic checkers. Dual static-dynamic cross-checking and differential baseline builds further verify each target, ensuring reliable verdicts with **zero LLM involvement in bug adjudication.** **[竖线止]**
- **大佬批注原文**：
  > `the LLM angle is not clear`
- **V2 与当前 `main.tex`（`L127, L129`）对应状态**：✅ **已完成锁定**
  - `L127` 第 4–6 句已先交代人工提取不现实、因此离线引入 LLM 提取并转换不变量；
  - `L129` Challenge 2（提交 `cb97d07`）已明确交代 LLM 的边界与分工：直接让 LLM 做预言机会产生底层 ISA 幻觉且速度过慢，直接让 LLM 从零写检查器仍会出错；因此 `DeFenzz` 在 `Check IR` 中形式化底层二进制与运行时查询原语并配对目标 ISA 规范，由 LLM 编写高层检查逻辑组合成静态或动态检查器，模糊测试时由确定性检查器直接测试每个编译后的种子。

---

## 二、第二轮批注详单（V2：`defuzz-before-impl-mat.pdf`，共 15 处）

> **说明**：V2 的 Title 与 Abstract 没有任何新批注；Page 7（Section III-D 后两段、Section IV 全文、References）没有任何批注。全部 15 处批注分布在 Page 1–6。

### 2.1 Section I: Introduction（Page 1–2，共 7 处）

#### [R2-1] Intro 第 1 段中部（Page 1 左栏下部第 8–16 行）
- **视觉标记**：左栏左侧页边距画长绿色弧线，从 `However, implementing these defenses accurately inside pro-` 一直括到左栏底行 `ventions, and stack frame layouts. When the implemen-`，引向左下角 4 行批注。
- **V2 被批注原文**：
  > **[弧线起]** However, implementing these defenses accurately inside production compilers like GCC and LLVM is difficult. Defense code must interact with complex optimization passes and translate abstract protection rules into machine instructions across diverse target ISAs. This translation relies on strict assumptions about object bounds, instruction semantics, register conventions, and stack frame layouts. When the implemen- **[左栏底，接右栏顶]** tation of a defense mechanism fails to match these ISA or optimization assumptions, its security protection breaks from within.
- **大佬批注原文**：
  > `key challenge: mitigations assume language properties are violated (undefined behavior) while optimizations assume the properties hold and optimize accordingly. This results in compilers inadvertendly breaking underlying assumptions of security mechanisms`
- **当前 `main.tex`（`L121`，`main.pdf` Page 1 左栏底至右栏顶）对应文本**：
  完整保留上述 V2 跨 ISA 下沉原句，并在 `breaks from within.` 后紧接着插入语言层 UB 假设冲突句：
  > `...its security protection breaks from within. At the language level, compiler optimizations assume programs are safe and free of undefined behavior (UB), whereas mitigations assume these properties are violated at runtime. Crucially, the compiler does not distinguish...`

#### [R2-2] Intro 第 1 段后半部（Page 1 右栏顶部第 3–12 行）
- **视觉标记**：右栏左上角画绿色斜线指向 `Crucially, the compiler does not distinguish...`，上方配 5 行绿色批注。
- **V2 被批注原文**：
  > **[↙斜线指向]** Crucially, the compiler does not distinguish between security checks and regular code, so there is no explicit barrier protecting them. Mitigation passes try to retrofit these checks into the intermediate representation, but modeling them as explicit barriers across the entire compiler pipeline would be too expensive in lost optimizations and rewriting costs. Consequently, subsequent optimization passes can unwittingly weaken or eliminate placed mitigations.
- **大佬批注原文**：
  > `this side is a good technical description on why barriers are not implemented. but I would like to highlight the language level aspect as well: compilers assume the program is safe and optimize accordingly. mitigations don't`
- **当前 `main.tex`（`L121`，`main.pdf` Page 1 右栏上部）对应文本**：
  原封不动保留上述 3 句屏障技术解释，并在 `Crucially...` 之前补入 `[R2-1]` 所示的语言层假设冲突句。

#### [R2-3] Intro 第 2 段第 1 句（Page 1 右栏中上部第 13 行）
- **视觉标记**：绿色下划线标出 `goes wrong`，右上角引出单行绿色批注。
- **V2 被批注原文**：
  > When a defense implementation <u>goes wrong</u>, it often causes **silent defense failures**: the compiler produces a working binary without any warnings or crashes, yet the security protection is quietly weakened or broken.
- **大佬批注原文**：
  > `unclear what going wrong means`
- **当前 `main.tex`（`L123`，`main.pdf` Page 1 右栏中部）对应文本**：
  将 `When a defense implementation goes wrong` 具体化为中端优化与后端下沉两类错误动作（并同步 `[R2-9]` 将 `quietly` 改为 `silently`）：
  > `When an optimization relaxes or removes a check or backend lowering violates an ISA rule, it often causes \textbf{silent defense failures}: the compiler produces a working binary without any warnings or crashes, yet the security protection is silently weakened or broken.`

#### [R2-4] Intro 第 4 段中部（Page 2 左栏上部第 12–16 行）
- **视觉标记**：绿色折角括号框住 `⌜Because LLM-assisted translation can introduce errors⌟`，左侧页边距写 6 行绿色批注。
- **V2 被批注完整上下文（第 4 段第 1–5 句）**：
  > These barriers raise a central question: how can we systematically detect silent defense failures when neither the buggy compiler nor direct LLM judgment provides a reliable oracle? To answer this question, we present **DEFUZZ (Defense Fuzzer)**, an invariant-directed agentic framework for testing compiler-instrumented defenses. Our core insight is that although defense implementations vary across backends, their intended security guarantees follow target-independent *security invariants*. DEFUZZ translates these invariants into programmatic bug oracles implemented as ISA-specific static and dynamic checkers, closing the oracle gap. **[⌜]** Because LLM-assisted translation can introduce errors **[⌟]**, DEFUZZ formalizes each invariant in a predicate IR with explicit applicability and safety semantics, deterministically lowering validated specifications into executable checkers.
- **大佬批注原文**：
  > `unclear that LLMs were used. Do you want to keep this more genreal? Customization is fine but a choice`
- **当前 `main.tex`（`L127`，`main.pdf` Page 2 左栏上部）对应文本**：✅ **已完成锁定**
  1. 第 1 句已移除 `nor direct LLM judgment`；
  2. 第 4–6 句先明确交代人工跨数十种防御、庞大编译器代码库与复杂 ISA 手册提取规则不现实，因此离线使用 LLM 提取并转换不变量；
  3. 第 7–9 句保留作者审定的高层总结，整段已定稿锁定。

#### [R2-5] Intro 第 5 段 Challenge 2（Page 2 左栏下部第 16–20 行）
- **视觉标记**：在 `builds further verify each target, ensuring reliable verdicts` 左侧页边距写 3 行绿色疑问。
- **V2 被批注原文**：
  > DEFUZZ addresses this by formalizing each invariant in a predicate IR parameterized by target ISA specifications, lowering it into ISA-specific static and dynamic checkers. Dual static-dynamic cross-checking and differential baseline builds further verify each target, ensuring reliable verdicts with **zero LLM involvement in bug adjudication**.
- **大佬批注原文**：
  > `fully safe?`
  > `proven?`
  > `validated?`
- **当前 `main.tex`（`L129` 已锁定 / `L252–L317` Sec III-C 已重构待审）对应文本**：✅ **Intro 已锁定 & Sec III-C 已完整对齐**
  - Intro Challenge 2（`L129`，提交 `cb97d07`）已彻底移除 `predicate IR`、`Dual static-dynamic cross-checking` 与 `verify`，重写为在 `Check IR` 中形式化二进制与运行时查询原语并结合目标 ISA 规范，由 LLM 编写高层逻辑组合成静态或动态检查器并直接测试每个编译后的种子（遵循 `AGENTS.md` 技术事实红线）；
  - Abstract `L116` 与 Intro `L127, L133, L138` 的现有措辞经作者审定保留锁定；
  - Section III-C（`L256, L281–L317`）已与 Intro 及 Section V-C（`921 -> 915`）完全对齐：严格采用静态或动态二选一模式（$\mu \in \{\mathsf{Static}, \mathsf{Dynamic}\}$），补齐离线双门控验证（`Gate 1: Well-Formedness` 与 `Gate 2: Differential Anchoring`），并清零 `verify/verified/proven` 等过度形式化声称。

#### [R2-6] Intro 第 5 段 Challenge 2 末句（Page 2 左栏下部第 21 行）
- **视觉标记**：绿色下划线标出 `with zero LLM involvement in bug`（接 `adjudication.`），紧接在 `[R2-5]` 下方的左页边距写 5 行绿色批注。
- **V2 被批注原文**：
  > Dual static-dynamic cross-checking and differential baseline builds further verify each target, ensuring reliable verdicts <u>**with zero LLM involvement in bug**</u> **adjudication**.
- **大佬批注原文**：
  > `not sure "zero LLM involvement" is a good distinction`
- **当前 `main.tex`（`L129` 已锁定 / `L317` Sec III-C 已改待审 / `L381` Sec V 待处理）对应文本**：✅ **Intro 已锁定 & Sec III-C 已改待审**
  - Intro Challenge 2 被批注句（`L129`）已改为正面对比表述：`During fuzzing, these deterministic checkers directly test each compiled seed, rather than relying on an LLM to judge whether silent defense bugs occur.`；
  - Section III-C（`L317`）已移除原 `zero LLM involvement in bug adjudication` 口号，改为具体机制表述：`during online fuzzing, each validated checker directly tests each compiled seed without LLM judgment.`；
  - Abstract `L116` 与 Contribution 2 `L138` 按作者审定保留锁定；Section V（`L381`）中的同短语留待后续修改评估章节时一并审定。

#### [R2-7] Intro 第 6 段评估摘要与 Contribution 4 末尾（Page 2 右栏底部）
- **视觉标记**：在右栏最后一个贡献点下方空白处写 2 行绿色批注。
- **V2 被批注原文**：
  > *(第 6 段首句)* We evaluated DEFUZZ on GCC and LLVM across x86-64, AArch64, and RISC-V, spanning diverse defenses such as stack canaries, CFI, shadow stacks, register scrubbing, and `_FORTIFY_SOURCE`. ... Overall, **DEFUZZ discovered 126 previously unknown silent failures in compiler-instrumented defenses, of which 34 have already been confirmed upstream, including 11 fixed** (Figure 1)...
  > *(Contribution 4)* **New Silent Defense Bug Discovery:** We evaluate DEFUZZ on GCC and LLVM across multiple ISAs and discover 126 previously unknown silent failures in compiler-instrumented defenses, with 34 confirmed upstream, including 11 fixed.
- **大佬批注原文**：
  > `what versions of GCC / LLVM ?`
  > `Would it make sense to build a benchmark of old versions to test ground truth / well known old bugs?`
- **当前 `main.tex`（`L133, L140` 已锁定 / 后文待对齐）对应文本**：✅ **Intro 已完成锁定 / ⏳ Sec V & Discussion 待补充**
  - Intro 第 6 段（`L133`）与 Contribution 4（`L140`）已在 `cb97d07` 中补齐具体编译器版本 `GCC~16.2.0 and LLVM~23.1.2` 及 `915 validated security invariants`、`111 / 30 / 11` 最新统计并锁定；
  - 针对第二问“用旧版本已知历史漏洞构建 ground-truth 基准”，可在后续撰写 Section V / Discussion 时补充回应。

---

### 2.2 Section II: Motivation（Page 3，共 3 处 — 已全部完成并锁定）

#### [R2-8] Section II-A 第 1 段第 1 句（Page 3 左栏顶部第 2 行）
- **视觉标记**：绿色横线划除 `security threats`，并在其正上方写绿色替换词。
- **V2 被批注原文**：
  > Compilers deploy automated defenses to protect software against ~~security threats~~.
- **大佬批注原文**：
  > `unknown or unpatched vulnerabilities`
- **当前 `main.tex`（`L121, L147`）对应文本**：✅ **已完成锁定**
  - Section I Intro 第 1 段（`L121`）与 Section II-A 第 1 段首句（`L147`）均已统一修改为：
    `Compilers deploy automated defenses to protect C and C++ systems software against the exploitation of unknown or unpatched vulnerabilities.`（同时呼应 `[R1-5]`）。

#### [R2-9] Section II-A 第 2 段末句（Page 3 左栏中上部第 15 行）
- **视觉标记**：绿色横线划除 `quietly`，并在其正下方写绿色替换词。
- **V2 被批注原文（第 2 段全文）**：
  > Preserving security guarantees across this multi-stage pipeline is error-prone. A middle-end optimization can rewrite a defense check under flawed size assumptions, or a backend pass can misplace a stack guard slot. When such bugs occur, the compiler neither crashes nor emits warnings. Instead, it produces a working binary whose security protection is ~~quietly~~ weakened or broken.
- **大佬批注原文**：
  > `silently`
- **当前 `main.tex`（`L123, L149`）对应文本**：✅ **已完成锁定**
  - Section I Intro 第 2 段（`L123`）与 Section II-A 第 2 段末句（`L149`）均已改为 `silently weakened or broken`（Abstract `L114` 按 HotCRP 注册锁定保持不变）。

#### [R2-10] Section II-C 第 1 段（Page 3 右栏中上部 Oracle Gap 段）
- **视觉标记**：右栏右侧页边距画长绿色弧线括住 Section II-C 第 1 段全段，向上引至 `C. Limitations of Existing Approaches` 标题右上方的 3 行绿色批注。
- **V2 被批注原文（Section II-C 第 1 段全文）**：
  > **[弧线起]** Existing compiler testing tools fail to detect this vulnerability due to two fundamental barriers in prior work. The first barrier of existing fuzzers is the **oracle gap**. Widely used compiler fuzzers such as Csmith [2], YARPGen [3], and EMI [4] only check whether the compiler crashes or whether compiled binaries produce consistent outputs on benign inputs. In Listing 1, GCC compiles the code cleanly, and any benign string `src` produces the exact same return value across all optimization levels. Because crash and differential testing do not check whether the binary enforces the reduced bound ($64 - k$), they remain blind when the defense is weakened. **[弧线止]**
- **大佬批注原文**：
  > `say explicitly that during benign executions, the mitigation is never triggered`
- **当前 `main.tex`（`L177, L181`）对应文本**：✅ **已完成锁定**
  - Section II-C 第 1 段（`L177`）已显式补入正常执行不触发缓解机制的因果链：
    `In Listing~\ref{lst:motivating-fortify}, GCC compiles the code cleanly. During benign executions, the mitigation is never triggered because the program stays within bounds. Thus, any benign string \texttt{src} produces the exact same return value across all optimization levels.`
  - 同节第 3 段末句（`L181`）亦已对齐 `AGENTS.md` 静态/动态二选一确定性 Oracle 表述（`inspect or execute the compiled binary using deterministic oracles`）。

---

### 2.3 Section III: Design（Page 4–6，共 5 处）

#### [R2-11] Section III Overview 段（Page 3 右栏底至 Page 4 左栏顶）
- **视觉标记**：Page 4 左栏顶部用大号绿色方括号 `[` 括住 Overview 段落在第 4 页的全部行（共 16 行），括号正上方写 `this paragraph does not add much`，同时在第 2–3 行用**两个绿色圆圈**分别圈出 `CoT` 和 `RAG`。
- **V2 被批注原文（Overview 全段）**：
  > *(Page 3 右栏底)* In this section, we present the design of DEFUZZ, an invariant-guided framework for discovering silent failures in compiler-instrumented defenses. Figure 2 illustrates its overall workflow, which consists of four core steps: security invariant generation, compiler source mapping, programmatic oracle construction, and agentic directed fuzzing. First, we extract **[Page 4 左栏方括号起]** security invariants from compiler source code, official documentation, and historical bug reports using a hybrid **(绿圈：`CoT`)** and **(绿圈：`RAG`)** pipeline. Second, we map these invariants to the relevant compiler passes and decision branches, identifying where defenses are implemented and which conditions govern their execution. Third, we combine Check IR primitives with target ISA specifications to synthesize executable static and dynamic Go checkers across architectures, verifying whether compiled programs preserve intended defenses without model hallucination. Finally, our agentic directed fuzzing coordinates a generator agent and a feedback agent to iteratively synthesize and mutate test programs under branch-trace and checker feedback. We discuss each step in detail in the following subsections. **[方括号止]**
- **大佬批注原文**：
  > `this paragraph does not add much`（外加圈出 `CoT`、`RAG`）
- **当前 `main.tex`（`L185–L187`，`main.pdf` Page 4）对应状态**：✅ **已完成大改待审**
  - Overview（`L187`）已彻底重写为 7 句精炼因果推导：删除机械的 `First/Second/Third/Finally` 步骤复述与未展开的 `CoT`/`RAG` 缩写，从良性输入不触发防御、静默失效不引起崩溃切入，逐句回答为什么需要外部安全不变量、分支映射与编译期探针、形式化原语检查器以及定向 fuzz driver 种子合成；
  - `figures/method-overview.pdf`（`L185`）已通过 `figures/src/generate_overview.py` 重绘，图内标签与正文术语完全统一（`Security Invariant Generation` / `Precondition · Rule · Signal`、`Mapped Branches & Compile-Time Probes`、`Check IR + Two-Gate Validation`、`Targeted Seed Synthesis`、`Seeds` / `Mutated Seeds`）。

#### [R2-12] Section III-A 开篇与切片提取段（Page 4 左栏中部至右栏顶部空白）
- **视觉标记**（三处联动标记）：
  1. 绿色短斜线指向小节标题 `A. Security Invariant Generation`，其右侧紧邻 5 行绿色批注；
  2. 大号绿色左弧线 `(` 从左栏第 1 段后部（`whenever a bug silently weakens... Instead, DEFUZZ extracts...`）一直括到左栏底部的第 2 段末尾；
  3. 在右栏顶部第 2 段结束语（`...subtract that same length from the remaining size bound.`）正下方的空白区域，画了一个占半栏高的巨型绿色方括号问号 **`[ ? ]`**。（原因：V2 把具体不变量示例 `Listing 3: INV-FORT-014` 放在了第 5 页左栏中部，第 4 页整页未展示提取出的数据结构长什么样。）
- **V2 被批注原文（Section III-A 第 1–2 段全文）**：
  > **A. Security Invariant Generation** **[↙斜线指向标题]**
  > To detect silent defense failures, DEFUZZ extracts security invariants that specify the protection rules each compiler defense must enforce. Because the compiler itself may contain bugs, neither its implementation logic nor its compiled outputs can serve as the ground truth. Treating current compiler behavior as the reference would cause circular self-validation **[左弧线起]** whenever a bug silently weakens or breaks a defense. Instead, DEFUZZ extracts security invariants from three sources: official compiler documentation and ISA/ABI manuals, developer comments and assertions in compiler source code, and confirmed historical bug reports.
  > Feeding whole compiler files or manuals to an LLM exceeds context limits and causes hallucinations. To keep each prompt focused, DEFUZZ splits compiler source code and official documentation into small, self-contained slices. For compiler source code, each slice contains a single C/C++ function with its leading header comment, or a single machine-description pattern (`define_insn` or `define_expand`). For official documentation, each slice captures a self-contained manual section defining defense requirements, such as a command-line option entry in GCC's user manual, a target-hook specification in GCC's internals manual, or a feature design section in Clang documentation. Every slice records its source path, line boundaries, defense mechanism, and target ISA. Because these slices are completely independent, DEFUZZ analyzes them in parallel using CoT prompting [5] to extract the triggering **[接右栏顶]** precondition, the protection rule, and the observable violation signal. In the fortified string bug, reviewing the slice for `get_string_length()` and its header comment leads the model to infer a clear rule: when advancing a destination pointer by a prefix length, the pass must subtract that same length from the remaining size bound. **[下方紧接巨型绿色 `[ ? ]`]**
- **大佬批注原文**：
  > `this is very abstract and opaque. it's not clear what data you extract and how it looks like`
  > `creating a set of targets (fuzz drivers) for each mitigation to trigger its execution may be more meaningful? will you add that?`
  > *(及右栏巨型 `[ ? ]`)*
- **当前 `main.tex`（`L189–L226, L348`）对应状态**：✅ **已完成大改待审**
  - Section III-A 首段（`L191`）在对比完差分测试、编译器自举规范与人工编写规范的不足后，**立即前置展示 `Listing 2: INV-FORT-014`（`L193–L206`，渲染于 `main.pdf` Page 4 右栏顶部，恰好填补原 `[ ? ]` 位置）**，直观呈现 `precond`、`rule`、`signal` 三字段结构及全部 4 个目标架构（`x86_64, aarch64, riscv64, loongarch64`）；
  - 全部源码/`.md`/手册切片粒度细节已移出 Section III-A，下沉至 Section IV Implementation（`L356`）；
  - 在 `L191` 点明每条不变量构成可测试的防御假设（`testable hypothesis`），并在 Section III-D（`L348`）明确说明 Generator Agent 基于该假设合成 **targeted fuzz drivers** 以触发防御执行与边界违例（同时回应 `[R2-0]` 邮件总评）。

#### [R2-13] Section III-A 第 3 段 Hybrid RAG 与全局设计语言（Page 4 右栏下半部）
- **视觉标记**：两条长绿色交叉弧线在 Section III-A 第 3 段正文中央画出一个贯穿全段的大叉/环圈，引向页面右下角的 3 行全局批注。
- **V2 被批注原文（Section III-A 第 3 段全文）**：
  > Different defenses and backends often perform similar low-level operations, such as updating size bounds, laying out stack frames, or clearing registers before return. As a result, new silent failures often share the same root causes as historical bugs. To find such bugs across defenses and architectures, DEFUZZ uses a hybrid RAG pipeline [6], [7] to transfer historical bug patterns. Searching directly with a raw bug patch only matches the original buggy function. **[绿色大交叉线覆盖区域起]** Instead, DEFUZZ strips defense-specific function and flag names from each historical bug report, distilling a general query with three parts: a root-cause summary, defense-agnostic action keywords, and original defense terms to exclude, as shown in Listing 2 for GCC PR 96191 [8]. Using this query, DEFUZZ searches the sliced source and documentation corpus by combining BM25 keyword search with dense vector retrieval via Reciprocal Rank Fusion. BM25 matches underscore-split identifier tokens that share naming conventions across passes, such as `ix86_zero_call_used_regs`. Dense vector retrieval finds slices that implement the same operation with different data structures, such as the register bitmap in ARM's `cmse_nonsecure_entry_clear_before_return`. After filtering out slices that contain the excluded terms, DEFUZZ selects the top-$k$ candidate slices. **[交叉线止]** For each candidate slice, the model pairs the code with the historical root cause and uses CoT reasoning to derive a new invariant for that target defense.
- **大佬批注原文**：
  > `across the design you're using very complex and convoluted language to explain simple concepts. simplify and go for the gist, then dive deeper in the implementation section to add the details. but break apart details from overall design`
- **当前 `main.tex`（`L183–L360`）对应状态**：✅ **已完成大改待审**
  - Section III-A 第 3 段（`L210`）与 `Listing 3`（`L212–L226`）已彻底剥离 `BM25`、下划线子词、`dense vector`、`Reciprocal Rank Fusion` 等检索实现细节，直指设计核心：不同防御共享底层操作导致同类 bug 跨防御复发，而原始补丁只匹配原防御名，因此剥离机制专有标识符构造通用失效查询，把 `GCC PR 96191` 栈金丝雀寄存器泄露迁移为 x86 与 ARM 的寄存器清理不变量；
  - 整个 Section III（`L183–L353`）与 Section IV（`L354–L360`）严格执行 `plain-paper-writing` 规范：全节每句控制在 7–25 词，零空洞修饰词，所有工程实现细节全部归入 Section IV Implementation。

#### [R2-14] Section III 全局跨栏总评（Page 5 顶部页眉）
- **视觉标记**：在 Page 5 顶端双栏上方居中偏左写 3 行绿色总评（`the` 上方有一绿色起笔点），统摄整个 Section III 各步设计。
- **V2 对应上下文范围（Page 4–7 Section III 全节）**：
  V2 的 Section III 依次包含：
  - `III-A Security Invariant Generation`（切片 CoT 提取 + Hybrid RAG 迁移 + `Listing 2` RAG 查询 + `Listing 3` `INV-FORT-014` 目录记录）；
  - `III-B Compiler Source Mapping`（符号索引 / 调用图 / AST 三工具按 `pass → function → branch` 映射 + `Listing 4` `DEFUZZ_HIT` 编译期探针日志）；
  - `III-C Programmatic Oracle Construction`（目标规范表 $\mathcal{T}_i$ `Table I` + `Check IR` 原语库 $\Omega$ + 四态裁决公式 `ERROR/NA/PASS/FAIL` + `Listing 5` 静态 Go 检查器 + PR 96191 动态检查器说明）；
  - `III-D Agentic Directed Fuzzing`（`Algorithm 1` 固定预算 $B$ 轮编排器与共享黑板 + Generator 多语句防折叠种子合成 + Feedback 分支轨迹与裁决联合诊断 + C-Reduce 绑定检查器约简与横向变异放大）。
  V2 各小节主要按工作流顺序陈述了每一步“做了什么”，较少展开“为什么更简单的替代方案不可行、为什么每一步设计不可或缺”。
- **大佬批注原文**：
  > `the big issue: you describe what you do, not why you do each step. a great paper builds up these steps and highlights how each individual step is necessary and why the approach is the best choice. from reading this section, I know what the approach does but not why`
- **当前 `main.tex`（`L183–L353`）对应状态**：✅ **已完成大改待审**
  - Section III 全节四个子节（`III-A` `L189–L226`、`III-B` `L228–L250`、`III-C` `L252–L317`、`III-D` `L319–L352`）均按大佬邮件 `[R2-0]` 与本条总评彻底重写为 **`问题挑战 -> 更简单替代方案为何失效 -> DeFenzz 设计决策为何最优`** 的自然段落流（无生硬小标题堆砌）。

#### [R2-15] Section III-D Generator Agent 多语句合成段（Page 6 右栏底部）
- **视觉标记**：绿色竖向方括号 `[` 括住 Page 6 右栏最下方一整段（Section III-D 第 2 段全段），引向右下角 2 行绿色正面批注。
- **V2 被批注原文（Section III-D 第 2 段全文）**：
  > **[竖括号起]** In each round, the Generator Agent writes a C or C++ test program $p$ to reach the mapped branches $m$ and satisfy the precondition $G_{\text{app}}(p, \mathcal{T}_i)$. Triggering a silent defense bug often requires multiple statements to work together on the same buffer. In `INV-FORT-014`, triggering the faulty rewrite requires a fixed-size buffer, an unknown prefix length at compile time, a fortified string append, and a trailing length query on that buffer. Guided by $m$ and the invariant record, the Generator Agent writes small programs that satisfy all of these conditions at once, while hiding selected values across non-inlined helper calls, runtime inputs, and memory barriers so that early optimizations do not fold away the test logic. **[竖括号止]**
- **大佬批注原文**：
  > `this part makes sense, create hypotheses that test mitigations and mitigation constraints. then use fuzzing to validate it`
- **当前 `main.tex`（`L348`）对应状态**：✅ **已完成强化待审**
  - `L348` 完整保留了获大佬肯定的多语句耦合构造（`INV-FORT-014` 定长缓冲区 + 未知前缀长度 + 强化拼接 + `strlen` 查询）与函数边界不透明屏障逻辑，并结合大佬邮件 `[R2-0]` 进一步点明：生成的种子作为测试特定缓解假设的 **targeted fuzz drivers**，通过选择性边界隐藏解决“无屏障被常量折叠抹除 vs. 全局加 `volatile` 抑制触发漏洞的中端优化”这一核心矛盾，且为动态检查器提供受控越界输入以区分缓解中止（`PASS`）与静默穿透（`FAIL`）。

---

## 三、当前 `main.tex` / `main.pdf` 锁定进度与后续待办核查

供后续审阅与继续修改 `main.tex` `Section V` 及之后章节时直接定位：

1. **章节锁定与重改进度分界线**：
   - **已完成并硬锁定的范围（`L1–L182`，`[ready]`）**：Title（`L103`）、Abstract（`L113–L117`）、Section I Introduction（`L119–L141`）与 Section II Motivation（`L143–L182`）已全部结合大佬两轮批注修订定稿并标记为 `[ready]`（同步记录于 [`outline_status.md`](./outline_status.md) 与 [`AGENTS.md`](./AGENTS.md)）。未经用户明确指示，禁止修改 `L1–L182`。
   - **已完成 V3 大刀阔斧重构待作者审阅锁定的范围（`L183–L360` + `figures/method-overview.pdf`，暂保持 `[不 ready]` 待确认）**：
     - **Section III Design（`L183–L353`）**：全面落实大佬整体邮件 `[R2-0]` 与 `[R2-11]`–`[R2-15]`、`[R1-3]`、`[R2-5]`、`[R2-6]`，包括因果推导式 Overview、前置 `Listing 2: INV-FORT-014`（覆盖 4 个目标 ISA）、正文首次展开 `CoT`/`RAG`、反转运行时崩溃语义（`SIGABRT` = `PASS`，越界不崩溃/泄露金丝雀 = `FAIL`）、对比各阶段替代方案、剥离 Go 语言样板与底层工程细节、补齐离线 Gate 1 / Gate 2 双门控验证（与 Section V-C `921 -> 915` 严格一致）；
     - **Section IV Implementation（`L354–L360`）**：完整承接从 Section III 剥离的工程实现细节（单函数/`.md`/手册切片、BM25 下划线子词 + `sqlite-vec` 稠密向量 RRF、`clangd`/CodeQL/Tree-sitter MCP 工具栈与 `fortify#b4e1` 探针重写、Go gRPC 服务与 rootless Podman + 四架构 QEMU 容器执行、Gate 1/Gate 2 实现、C-Reduce 包装器与内容寻址重放账本）；
     - **图 2（`figures/method-overview.pdf`）**：已同步重绘并与正文术语完全对齐。
2. **下一阶段待办（Section V Evaluation `L362–L557` 及 Section VI+ 收尾章节）**：
   - **Section V 措辞与占位符核查**：审定 `L381` 处 `zero LLM involvement in bug adjudication` 表述（`[R2-6]`），并依据 [`evaluation_data/`](./evaluation_data/README.md) 填入已完成数据，替换尚存的 `\tbd{N}` / `TBD`（`L406–L407, L415, L498, L509–L512, L547`）；
   - **Section VI+ 收尾章节补齐**：在 `L557` 后补齐 Discussion（回应 `[R2-7]` 用旧版本已知历史漏洞构建 ground-truth 基准的讨论、人工核验边界与 Token 成本）、Related Work 与 Conclusion。

---

## 三、第三轮批注（V3：`defenzz1117-mat.pdf`，2026-11-17，共 15 处）及落实状态（2026-11-18）

| 编号 | 位置 | 批注原话 | 落实 |
| :--- | :--- | :--- | :--- |
| R3-1 | Intro 第 1 段首句 | `systems software` → `code` | ✅ `harden C and C++ code` |
| R3-2 | Intro 第 1 段 | `these defenses insert` → `mitigations` | ✅ |
| R3-3 | Intro 第 1 段 | `Defense code must interact` → `Defense passes` | ✅ |
| R3-4 | Intro 第 2 段 | `violates an ISA rule` → `dependencies` | ✅ `violates ISA dependencies` |
| R3-5 | Intro 第 2 段 CVE 处 | cite the "correctness compiler gap" from LangSec (best paper) | ✅ 新增 `dsilva2015correctness`（D'Silva, Payer, Song, LangSec 2015），第三人称引用 |
| R3-6 | Fig. 1 | green is not a good color; use yellow and orange for reported/confirmed | ✅ Reported 黄、Confirmed 橙，Historical 改深灰边框 |
| R3-7 | Intro 第 4 段（central question）左栏 | this column is quite fluffy and could be shortened | ✅ 208 → ~110 词，删除 predicate IR 旧表述 |
| R3-8 | Intro 第 5 段（三挑战） | cut by 1/2 | ✅ 282 → ~150 词 |
| R3-9 | Intro 末尾 | intro is too long, cut by 1/2 page | ✅ Intro 1.81 → 1.31 页（-0.50 页） |
| R3-10 | Fig. 2 | too small to read; simplify text, make remaining text larger | ✅ 按作者决定保留原图（logo 与文字不变），仅在正文中由 `0.90\textwidth` 放大到 `\textwidth` |
| R3-11 | Listing 3 | 勾画换行处 | ✅ Listing 1/2/3/6 全部消除自动折行 |
| R3-12 | §3.2 首句 | LLMism, rephrase | ✅ 去掉 "X, not Y" 句式 |
| R3-13 | §3.2 | `drown out` → hide? suppress? | ✅ `hide` |
| R3-14 | §3.3 | `exact opposite logic` → behavior? | ✅ `Runtime defenses expect the opposite behavior.` |
| R3-15 | §3.4 | would it make sense to show an example of the loop? | ✅ 新增 Listing 6：INV-FORT-014 三轮示例 + 解读段 |
