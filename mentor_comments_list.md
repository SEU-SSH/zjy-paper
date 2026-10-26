# DeFuzz 论文修改意见清单

> **来源文档**：[DeFuzz 论文 - 飞书文档](https://dxqswftp8yb.feishu.cn/wiki/YB1Jwb2pKiMXTvk8LEYcPESOnxb?from=from_copylink)  
> **内容概要**：针对 Abstract 与 Introduction 的 19 条具体批注与修改要求。

---

## 1. Abstract（摘要）

- **位置**：Abstract 第 1 段
  - **原文**：`against memory errors and control-flow hijackin`
  - **修改要求**：描述防御目标太局限了，用 `such as` 举例（拓宽范围）。

- **位置**：Abstract 第 1 段末尾
  - **原文**：`Such failures expose a fundamental oracle gap: conventional crash and differential testing only check whether a program produces`
  - **修改要求**：换个写法，先说已有的工具检测不到问题，再引出 oracle gap。

- **位置**：Abstract 第 2 段
  - **原文**：`mapped logic `
  - **修改要求**：转换为 Oracle 的主体不是 mapped logic，其实是不变量（invariants）。

---

## 2. Introduction - 痛点案例与现有工作障碍

- **位置**：Introduction 第 2 段末尾
  - **原文**：`We examine the root cause and stack layout mechanics of this bug in Section II.`
  - **修改要求**：不要推迟到 Section II，直接在这里把 CVE-2023-4039 的根因和栈破坏机制写清楚。

- **位置**：Introduction 第 3 段
  - **原文**：`—` (破折号)
  - **修改要求**：少用破折号。

- **位置**：Introduction 第 3 段
  - **原文**：`barrier`
  - **修改要求**：说明是相关工作的 barrier（明确主体是现有测试工作面临的障碍）。

- **位置**：Introduction 第 3 段
  - **原文**：`The second barrier is reaching deep defense decision branches.`
  - **修改要求**：
    1. 突出难以知道哪些是防御 branch（reach branch 本身很简单）。
    2. 实际上 reach 了还没用，还得满足特定的条件。
    3. 这个条件不能泛泛而谈数据流、控制流。

- **位置**：Introduction 第 3 段
  - **原文**：`specific code patterns`
  - **修改要求**：太废话了，专一点（具体指出需要什么代码特征/约束）。

- **位置**：Introduction 第 3 段
  - **原文**：`such as pairing a __strcat_chk call on an op`
  - **修改要求**：容易引起误解。直接说这是某一个 bug，不要说 such as（避免让读者误以为是普遍模式）。

- **位置**：Introduction 第 3 段
  - **原文**：`static analyzers `
  - **修改要求**：从人力角度去说（指出人工静态分析和规则编写的高昂人力成本）。

---

## 3. Introduction - 核心方法与设计理念

- **位置**：Introduction 第 4 段
  - **原文**：`By converting`
  - **修改要求**：
    1. 交代为什么 converting 是正确的（实际上是 AI 转换的）。
    2. 说明如何保证正确性（可以结合形式化方法、人工+抽样核验）。

- **位置**：Introduction 第 4 段
  - **原文**：`overcomes`
  - **修改要求**：删掉自夸词，没有 overcome。

- **位置**：Introduction 第 5 段 (Challenge 1)
  - **原文**：`Because compilers themselves have bugs, we cannot trust their current outputs as the ground truth`
  - **修改要求**：没有回到根本上。核心其实是想说“编译器有 bug，所以我们不能信任它作为 ground truth”。

- **位置**：Introduction 第 5 段 (Challenge 1)
  - **原文**：`Instead, DeFuzz extracts invariants from compiler source code, ISA specifications, and historical bug fixes using a hybrid CoT a`
  - **修改要求**：缺少 insight idea，太流水（不能只列技术流程，要有核心洞见）。

- **位置**：Introduction 第 5 段 (Challenge 2)
  - **原文**：`without false positives`
  - **修改要求**：表述有点 low，不太本质，表述为“足够准确即可”。

- **位置**：Introduction 第 5 段 (Challenge 2)
  - **原文**：`by turning each invariant into ISA-specific static and dynamic checkers`
  - **修改要求**：需要解释为什么 checker 一定对（论证其可靠性依据）。

---

## 4. Introduction - 评估成果与论文贡献

- **位置**：Introduction 倒数第 2 段 (Results)
  - **原文**：`These results `
  - **修改要求**：还有哪些好？还有哪些核心的东西（丰富实验结果维度的亮点，不仅报 Bug 数量）。

- **位置**：Introduction 贡献段起始
  - **原文**：`In summary, this paper makes the following contributions:`
  - **修改要求**：能不能 question（尝试采用核心问题/设问的方式引出贡献）。

- **位置**：Introduction Contribution 2 标题
  - **原文**：`Multi-ISA Programmatic Oracles`
  - **修改要求**：缺个动词，增加 translation。
