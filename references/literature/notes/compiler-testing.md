# 编译器测试、验证、oracle与实验基础文献

核验日期：2026-11-12。范围：23篇新增论文。仅作为独立参考文献库，不改正文、不自动把这些条目加入主稿refs.bib，也未运行测试或缺陷复现。

## 使用顺序

优先考虑补充Alive、Athena、Hermes、CLsmith、SPE，以免把传统编译器测试缩成单纯随机生成和输出checksum。CompCert和Translation Validation用于严格界定语义保持与验证对象。Daikon、QuickCheck和metamorphic综述可帮助区分推断性质、执行性质与证明性质三个不同动作。

实验设计优先参考Evaluating Fuzz Testing、FuzzBench和Magma。Magma的reached/triggered/detected区分尤其适合防止把到达编译pass等同于发现防御错误；这些引用只提供方法论，不能替代本项目自己的实验ground truth。

C-Reduce正式论文补充现有creduce项目网页；两者不是重复出版条目，正文引用时应按需要选择。Z3已在现有refs.bib，本集合不重复。已有14篇Related Work均未重复收录。

## 本轮核验的边界

每条的read_depth明示实际深度：有些只有出版社摘要，有些读到论文Introduction或相关方法讨论。没有全篇逐句审计、复现实验，也没有重新核实各论文报告的漏洞数字；潜在用途刻意不依赖这些数字。source_urls只列实际成功读取的一手来源；跨ACM会议论文与SIGPLAN重印提取摘要时，以正式会议DOI组织一条记录。

多数作者姓名按出版社/正式论文完整署名保留，未省略作者。Pnueli/Siegel/Singerman在原论文及Springer仅署A./M./E.，T. H. Tse等也保留公开署名，未臆造首字母展开。

## 已处理的元数据异常

- Translation Validation正式年份是1998；Springer网页First Online为2006，不能用于改写论文年份。
- Magma正式完整论文为PACM on Measurement and Analysis of Computing Systems 4(3),2020，DOI 10.1145/3428334。搜索首先返回2021年81–82页的会议摘要/重印，未将它当完整论文。
- Pardis的出版社文本元数据遗漏了作为图片排版的工具名，已从正式PDF首页确认并补全题名。
- Perses、QuickCheck和metamorphic综述存在title/subtitle拆分；已保留完整题名。
- Manes等fuzzing综述正式卷期年份为2021；预印本2018、early-access 2019和早期投稿CSUR的说明不替代最终IEEE TSE信息。
- ACM会议与SIGPLAN Notices重印有不同DOI；没有重复计数。
- Google Research的FuzzBench作者页面可显示比正式论文更长的个人姓名；条目采用正式论文作者署名形式保持一致。

## 不应从这些文献推出的结论

- 不能说形式化编译器验证一概不涉及安全。CompCert摘要明确讨论在语义保持前提下传递源程序已证明的安全性质；DeFuzz的差别需要落到规格是否覆盖某项防御义务及实际验证范围。
- 不能说所有EMI只修改死代码，Hermes扩展到活代码；也不能把EMI限定输入集的等价提升为全输入等价。
- 不能说程序化checker、动态likely invariant或随机性质测试天然消除语义错误。验证的性质、执行的判据和目标安全意图需要独立对齐。
- SPE的穷举有固定骨架/变量集合边界；syntax-aware reduction的语法有效不等于无UB；最小化不能证明interestingness test正确。
- 覆盖率、原始crash数、确认bug数、到达/触发/检测是不同观测量。外部benchmark经验不能直接证明本项目的效果。

## 待核线索：不进入BibTeX集合

- Barr等《The Oracle Problem in Software Testing: A Survey》，IEEE TSE 2015，DOI 10.1109/TSE.2014.2372785：出版社题名和元数据已检索，尚未读到匹配的一手摘要/正文，因此只保留待核线索。不对其具体方法分类作已核验声明。
- McKeeman《Differential Testing for Software》、Orange、额外JIT-Picking条目：未达到本轮一手内容核验门槛，不凭记忆补元数据。
- 《Finding Missed Optimizations Through the Lens of Dead Code Elimination》及《Coverage Is Not Strongly Correlated with Test Suite Effectiveness》：已检索到出版社元数据，尚未完成一手摘要/方法阅读，不列入本批。

## 获取过程与证据目录

证据保存在工作树外 `~/defuzz-project/feiyang-writing/reference-library-2026-11-12-evidence/compiler-testing/`。包括出版社原始JSON、官方/作者HTML、少量PDF和提取文本。远端遇到超时/访问失败后，按授权使用本机下载小文件再上传；Delta Debugging、Perses、FuzzBench的最终有效证据均已按真实题名核对。

部分搜索和候选URL返回了错误论文或错误会议详情页，均未入集合：例如候选arXiv:1302.1660实际是凝聚态物理论文，与oracle survey无关；会议页面仅HTTP成功不代表目标论文匹配。本轮已显式按题名、作者及DOI交叉核验，不能把证据目录内所有下载文件都当成通过核验的参考文献。

## 条目索引

| Key | 论文 | 年份 | 优先级 | 深度 |
| --- | --- | --- | --- | --- |
| `pnueli1998translationvalidation` | [Translation Validation](https://doi.org/10.1007/bfb0054170) | 1998 | core | metadata+method |
| `claessen2000quickcheck` | [QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs](https://doi.org/10.1145/351240.351266) | 2000 | supporting | metadata+abstract |
| `zeller2002deltadebugging` | [Simplifying and Isolating Failure-Inducing Input](https://doi.org/10.1109/32.988498) | 2002 | core | metadata+method |
| `ernst2007daikon` | [The Daikon system for dynamic detection of likely invariants](https://doi.org/10.1016/j.scico.2007.01.015) | 2007 | core | metadata+method |
| `leroy2009compcert` | [Formal verification of a realistic compiler](https://doi.org/10.1145/1538788.1538814) | 2009 | core | metadata+abstract |
| `holler2012langfuzz` | [Fuzzing with Code Fragments](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/holler) | 2012 | supporting | metadata+abstract |
| `regehr2012creduce` | [Test-Case Reduction for C Compiler Bugs](https://doi.org/10.1145/2254064.2254104) | 2012 | core | metadata+abstract |
| `le2015athena` | [Finding Deep Compiler Bugs via Guided Stochastic Program Mutation](https://doi.org/10.1145/2814270.2814319) | 2015 | core | metadata+abstract |
| `lidbury2015clsmith` | [Many-Core Compiler Fuzzing](https://doi.org/10.1145/2737924.2737986) | 2015 | core | metadata+abstract |
| `lopes2015alive` | [Provably Correct Peephole Optimizations with Alive](https://doi.org/10.1145/2737924.2737965) | 2015 | core | metadata+abstract |
| `menendez2016alivefp` | [Alive-FP: Automated Verification of Floating Point Based Peephole Optimizations in LLVM](https://doi.org/10.1007/978-3-662-53413-7_16) | 2016 | supporting | metadata+method |
| `sun2016hermes` | [Finding Compiler Bugs via Live Code Mutation](https://doi.org/10.1145/2983990.2984038) | 2016 | core | metadata+abstract |
| `donaldson2017glfuzz` | [Automated Testing of Graphics Shader Compilers](https://doi.org/10.1145/3133917) | 2017 | supporting | metadata+abstract |
| `zhang2017spe` | [Skeletal Program Enumeration for Rigorous Compiler Testing](https://doi.org/10.1145/3062341.3062379) | 2017 | core | metadata+abstract |
| `chen2018metamorphicsurvey` | [Metamorphic Testing: A Review of Challenges and Opportunities](https://doi.org/10.1145/3143561) | 2018 | core | metadata+abstract |
| `klees2018fuzzeval` | [Evaluating Fuzz Testing](https://doi.org/10.1145/3243734.3243804) | 2018 | core | metadata+method |
| `sun2018perses` | [Perses: Syntax-Guided Program Reduction](https://doi.org/10.1145/3180155.3180236) | 2018 | supporting | metadata+method |
| `gharachorlu2019pardis` | [Pardis: Priority Aware Test Case Reduction](https://doi.org/10.1007/978-3-030-16722-6_24) | 2019 | optional | metadata+method |
| `hazimeh2020magma` | [Magma: A Ground-Truth Fuzzing Benchmark](https://doi.org/10.1145/3428334) | 2020 | core | metadata+method |
| `park2020die` | [Fuzzing JavaScript Engines with Aspect-preserving Mutation](https://doi.org/10.1109/sp40000.2020.00067) | 2020 | supporting | metadata+method |
| `manes2021fuzzingsurvey` | [The Art, Science, and Engineering of Fuzzing: A Survey](https://doi.org/10.1109/tse.2019.2946563) | 2021 | supporting | metadata+abstract |
| `metzman2021fuzzbench` | [FuzzBench: An Open Fuzzer Benchmarking Platform and Service](https://doi.org/10.1145/3468264.3473932) | 2021 | core | metadata+abstract |
| `gross2023fuzzilli` | [FUZZILLI: Fuzzing for JavaScript JIT Compiler Vulnerabilities](https://doi.org/10.14722/ndss.2023.24290) | 2023 | supporting | metadata+abstract |

## 每条的可用论点与限制

### pnueli1998translationvalidation

已读Springer摘要、正式PDF首页及Introduction；正式出版年1998，网页First Online 2006不是论文年份。作者忠实保留原发表署名。

可用于：支持逐次验证编译结果、共同语义框架和refinement的历史来源；与证明整个编译器的路线区分。

边界：本文实例为SIGNAL到C，不能据此声称任意编译器后端或安全机制已有端到端保证；未将作者首字母臆造展开。

一手来源：[1](https://api.crossref.org/works/10.1007/BFb0054170)；[2](https://link.springer.com/chapter/10.1007/BFb0054170)；[3](https://link.springer.com/content/pdf/10.1007/BFb0054170.pdf)。

### claessen2000quickcheck

已读出版社SIGPLAN重印的完整摘要，并核对ICFP正式论文DOI、作者、题名与副题。

可用于：支持将性质写为可执行函数并在随机输入上测试，以及自定义生成器与性质判据相分离的经典先例。

边界：测试给定性质不证明性质符合需求，也不构成程序普遍正确性证明；不能将可执行predicate本身称为形式化证明。

一手来源：[1](https://api.crossref.org/works/10.1145/351240.351266)；[2](https://api.crossref.org/works/10.1145/357766.351266)。

### zeller2002deltadebugging

已读作者正式论文PDF首页、摘要与Introduction，核对作者全名及dd/ddmin区别；出版社元数据用于正式页码和DOI。

可用于：支持保持失败条件的测试缩减和通过/失败输入之间差异隔离；用于解释最小案例产出与后续确认的分工。

边界：ddmin的局部最小性不等于全局最小；缩减保留的是给定测试判据，不证明该判据语义正确。

一手来源：[1](https://api.crossref.org/works/10.1109/32.988498)；[2](https://www.st.cs.uni-saarland.de/papers/tse2002/tse2002.pdf)。

### ernst2007daikon

已读作者正式PDF首页、摘要、Introduction与示例前半部分；核对全部作者、正式期刊年份及DOI。

可用于：支持从执行观测推断likely invariants，与从文档/历史推断规格形成可比较路线；提醒观测成立和规范性正确应分开。

边界：likely invariant由已观察轨迹支持，不是普遍语义定理或安全意图证明；不能把动态统计推断与形式化验证混称。

一手来源：[1](https://api.crossref.org/works/10.1016/j.scico.2007.01.015)；[2](https://homes.cs.washington.edu/~mernst/pubs/daikon-tool-scp2007.pdf)。

### leroy2009compcert

已读出版社登记的完整摘要，核对作者、正式年份、卷期、页码与DOI。

可用于：支持区分编译器验证、具体翻译验证和测试；CompCert以Coq证明Clight到PowerPC的语义保持。

边界：限于该论文所覆盖的语言、目标和证明边界。摘要明确提到源程序已证明安全性质向目标代码传递，不能写成形式化编译器验证完全不涉及安全。

一手来源：[1](https://api.crossref.org/works?query.title=Formal%20verification%20of%20a%20realistic%20compiler&rows=2)。

### holler2012langfuzz

已读USENIX官方页完整摘要、作者列表及官方BibTeX，核对出版年和页码。

可用于：支持语法生成与既有代码片段重用结合的输入生成路线，补足LLM前的语言测试生成背景。

边界：语言引擎测试生成方法不等于编译器防御契约检查；语法有效和片段重用也不自动保证完整程序无语义错误。

一手来源：[1](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/holler)。

### regehr2012creduce

已读出版社SIGPLAN重印完整摘要，与PLDI正式记录核对；此条是正式论文，区别既有refs.bib的C-Reduce项目网页。

可用于：支持编译器测试缩减需要语言相关变换，普通文本delta debugging可能保留过大或依赖UB的案例。

边界：C-Reduce依赖interestingness test，不能把缩减完成解释成自动证明程序无UB或缺陷已确认；本条不是对既有creduce网页条目的自动替换。

一手来源：[1](https://api.crossref.org/works?query.title=Test-case%20reduction%20for%20C%20compiler%20bugs&rows=2)。

### le2015athena

已读出版社SIGPLAN重印摘要；与正式OOPSLA会议记录匹配题名、完整作者列表、年份和页码。

可用于：支持EMI由Orion删死代码扩展至Athena插入/删除未执行代码，并用控制流多样性目标引导随机搜索的演进。

边界：等价仅针对给定输入；不是全输入语义等价，也不直接证明安全防御契约。没有复现实验或重新核验所报bug数量。

一手来源：[1](https://api.crossref.org/works?query.title=Finding%20Deep%20Compiler%20Bugs%20via%20Guided%20Stochastic%20Program%20Mutation&rows=2)。

### lidbury2015clsmith

已读出版社SIGPLAN重印摘要，并核对同论文的PLDI正式记录。

可用于：支持随机差分与EMI向OpenCL多核环境扩展，生成确定性、可通信kernel，以及增加动态死代码的注入机制。

边界：涉及多设备配置并不等于具有跨ISA语义或安全契约可比性；不能直接当DeFuzz四ISA实验的统一baseline。

一手来源：[1](https://api.crossref.org/works?query.title=Many-core%20compiler%20fuzzing&rows=3)。

### lopes2015alive

已读同一论文SIGPLAN重印记录的完整摘要，并以会议记录核对正式DOI、作者和页码。

可用于：支持以DSL表达LLVM局部优化、自动证明或产生反例，以及从已验证规则生成实现的前例。

边界：Alive主要针对所支持的局部优化及其语义模型，不等于验证所有后端防御；不能把整数原版的范围套用为任意浮点优化。

一手来源：[1](https://api.crossref.org/works?query.title=Provably%20correct%20peephole%20optimizations%20with%20Alive&rows=2)。

### menendez2016alivefp

已读Springer原文摘要及Introduction，核对正式作者、出版年、题名、页码和DOI。

可用于：支持浮点优化验证需要明确NaN、有符号零、无穷及fast-math等语义前提，形式化checker的范围受模型约束。

边界：只覆盖论文声明的一类不会造成精度损失的浮点/fast-math优化，不可外推所有浮点近似优化都已得到验证。

一手来源：[1](https://api.crossref.org/works?query.title=Alive-FP%20Automated%20Verification%20of%20Floating%20Point%20Based%20Peephole%20Optimizations&rows=2)；[2](https://link.springer.com/chapter/10.1007/978-3-662-53413-7_16)。

### sun2016hermes

已读出版社SIGPLAN重印完整摘要，核对正式会议记录；确认工具名Hermes及live/dead两类区域的变异。

可用于：支持EMI不应被一概描述为只能改死代码；Hermes扩展到活代码区域，是Related Work潜在的重要遗漏。

边界：针对输入集保持等价仍是前提；活代码变异并不自动产生针对编译器防御的专门oracle。

一手来源：[1](https://api.crossref.org/works?query.title=Finding%20compiler%20bugs%20via%20live%20code%20mutation%20Hermes&rows=3)。

### donaldson2017glfuzz

已读出版社完整摘要，确认GLFuzz、语义等价shader变换、图像差异与自动缩减的描述；核对全部作者和DOI。

可用于：支持当图形结果不完全指定时，metamorphic testing仍可为shader编译器构造实用oracle；说明编译器测试并非只比较整数checksum。

边界：图像等价/渲染差异的判据依赖该领域设定，不可直接外推为所有安全防御契约oracle；不复用其漏洞或效果数字。

一手来源：[1](https://api.crossref.org/works?query.title=Metamorphic%20Testing%20of%20Graphics%20Shader%20Compilers&rows=2)。

### zhang2017spe

已读作者arXiv v4完整摘要及作者publication页面，正式年份与DOI使用PLDI记录。

可用于：支持在固定语法骨架和变量集合下系统枚举非alpha等价变量使用模式；补足随机生成之外的枚举路线。

边界：穷举保证受固定骨架与变量集合限定，不能称为穷举所有程序或证明编译器正确。

一手来源：[1](https://api.crossref.org/works/10.1145/3062341.3062379)；[2](https://arxiv.org/abs/1610.03148)；[3](https://people.inf.ethz.ch/suz/publications/)。

### chen2018metamorphicsurvey

已读出版社登记的完整摘要，核对title与subtitle、全部作者、正式卷期与年份。

可用于：支持metamorphic relation是多输入及期望输出之间的必要性质，兼具测试生成与结果判定角色；可解释关系型oracle。

边界：关系需符合目标规格，满足关系不代表实现全面正确；本文是综述，不能作为DeFuzz checker正确性的证明。T. H. Tse保留公开发表署名。

一手来源：[1](https://api.crossref.org/works/10.1145/3143561)。

### klees2018fuzzeval

已读作者arXiv论文摘要和Introduction（含重复运行、统计检验、基准/种子/预算敏感性及ground truth讨论），正式出版元数据与CCS匹配。

可用于：支持重复实验、合理baseline、代表性基准、固定资源、统计检验和以真实bug而非原始crash计数评价。

边界：不应从该文机械推出某个统一运行次数或时长适合所有DeFuzz实验；其对既有论文的结论属于当年的样本范围。

一手来源：[1](https://api.crossref.org/works/10.1145/3243734.3243804)；[2](https://arxiv.org/pdf/1808.09700)。

### sun2018perses

已读作者官方仓库所附ICSE正式PDF摘要和Introduction，以及README；论文全题名由PDF补全出版社只保留Perses的短title。

可用于：支持用输入语法避免大量语法无效的缩减候选，以及通用reducer与性质判据之间的接口。

边界：语法有效不等于语义有效或不含UB；性质保持依赖外部测试脚本，不能据此证明oracle正确。

一手来源：[1](https://api.crossref.org/works/10.1145/3180155.3180236)；[2](https://raw.githubusercontent.com/perses-project/perses/master/doc/publication/2018_perses_icse.pdf)；[3](https://raw.githubusercontent.com/perses-project/perses/master/README.md)。

### gharachorlu2019pardis

已读Springer全文摘要和Introduction以及正式PDF首页；PDF确认工具名Pardis，修正出版社文本元数据遗漏的图片标题。

可用于：支持结构化缩减中的优先级反转会影响效率，作为reduction成本与实现设计的补充背景。

边界：相对Perses的效率数字依赖论文同组基准与设置；不可宣称对所有语言/缺陷普遍更快。

一手来源：[1](https://api.crossref.org/works?query.title=Pardis%20Priority%20Aware%20Test%20Case%20Reduction&rows=2)；[2](https://link.springer.com/chapter/10.1007/978-3-030-16722-6_24)；[3](https://link.springer.com/content/pdf/10.1007/978-3-030-16722-6_24.pdf)。

### hazimeh2020magma

已读完整论文的作者arXiv摘要、Introduction与指标问题讨论，并核对2020完整期刊论文DOI；排除2021两页会议摘要版本。

可用于：支持区分bug reached、triggered、detected；说明crash去重和覆盖率不足以替代真实bug ground truth。

边界：Magma自身是特定应用及历史bug基准，不可直接当作DeFuzz防御缺陷的ground truth；也不支持覆盖率与任何任务效果完全无关的极端说法。

一手来源：[1](https://api.crossref.org/works/10.1145/3428334)；[2](https://arxiv.org/pdf/2009.01120)。

### park2020die

已读作者托管正式论文首页摘要与Introduction，核对出版社正式年份、题名、作者、页码。

可用于：支持随机变异保留类型和结构等有利于触发深层JIT行为的特征，说明输入多样性与保留触发条件之间的权衡。

边界：aspect-preserving指概率性保留特征，不是严格保语义或形式化证明；JavaScript引擎结果不能直接视为LLVM/GCC防御检查效果。

一手来源：[1](https://api.crossref.org/works?query.title=Fuzzing%20JavaScript%20Engines%20with%20Aspect-preserving%20Mutation&rows=3)；[2](https://taesoo.kim/pubs/2020/park:die.pdf)。

### manes2021fuzzingsurvey

已读作者arXiv v4完整摘要并核对IEEE正式卷期页码；正式发表年2021，区别预印本2018及early-access DOI中的2019。

可用于：支持fuzzing的一般模型及各阶段设计分类，用于Background组织输入生成、执行、反馈与结果判定。

边界：这是综述及分类参考，不能为DeFuzz具体性能或首创性直接背书；本文arXiv曾标注投ACM CSUR但正式载体是IEEE TSE。

一手来源：[1](https://api.crossref.org/works?query.title=Fuzzing%20Art%20Science%20and%20Engineering&rows=2)；[2](https://arxiv.org/abs/1812.00140)。

### metzman2021fuzzbench

已读Google Research官方论文摘要及官方仓库README，并核对正式会议作者、年份、页码与DOI。

可用于：支持可重现的大规模fuzzer比较平台、统一集成接口和统计报告的实验组织思路。

边界：使用FuzzBench不自动保证DeFuzz编译器/防御任务公平；样本README的24小时20次配置只是示例，不能据此宣称是统一必需标准。

一手来源：[1](https://api.crossref.org/works/10.1145/3468264.3473932)；[2](https://research.google/pubs/fuzzbench-an-open-fuzzer-benchmarking-platform-and-service/)；[3](https://raw.githubusercontent.com/google/fuzzbench/master/README.md)。

### gross2023fuzzilli

已读NDSS官方论文页完整摘要及作者列表，并核对出版社DOI记录。

可用于：支持专门设计中间表示以生成能触发JIT语义的输入；用于讨论到达编译阶段需要结构化输入。

边界：不能将其JIT漏洞目标等同编译器静态防御契约验证；官方摘要的首创/覆盖声明仅属该论文自身范围，不据此排除所有先前方法。

一手来源：[1](https://api.crossref.org/works?query.title=JIT-Picking%20Differential%20Fuzzing%20of%20JavaScript%20Engines&rows=2)；[2](https://www.ndss-symposium.org/ndss-paper/fuzzilli-fuzzing-for-javascript-jit-compiler-vulnerabilities/)。
