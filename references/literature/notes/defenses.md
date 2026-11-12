# 防御机制与安全语义文献收集

核验日期：2026-11-12。范围是 DeFuzz 后续写作可能引用的基础与相关研究，不是要求把所有条目都加入当前 Related Work。共收集 29 项；其中 1 项是明确标记的 arXiv 预印本，其余是已发表会议/期刊论文。

## 阅读与使用边界

本次完成题名、作者、年份、venue、DOI（存在时）及摘要或官方方法说明的核验。没有通读全部全文、重跑工具或检验论文实验结论。每条 JSON 分别记录实际阅读深度、潜在用途和不能外推的边界。Crossref 是出版方登记元数据来源；作者 PDF 或 USENIX 官方页面用于交叉核对。仅据摘要判断出的用途是候选引用位置，不是已经完成论证的比较结论。

`core` 表示与编译器防御、sanitizer、程序安全语义或相关验证方法直接相关；`supporting` 表示适合背景/扩展对比；`optional` 表示可能帮助区分另一类机制。这里的优先级不是论文质量或方法优劣排名。

按主题：CFI、栈与代码指针保护 9 项；sanitizer 与内存安全 13 项；安全擦除与常数时间 4 项；推测执行防御/分析 3 项。当前 Clang/GCC 各开关语义、支持 ISA 和版本行为仍应另引官方实现文档，不能只由历史论文推出。

## 元数据与证据注意事项

- CFI 基础条目选用 Abadi 等 2009 年扩展期刊版，避免在未取得 2005 原文摘要的情况下声称读过原始会议版本。CFI 首次提出年份不能据此改为 2009。
- SoftBound、CETS、EffectiveSan、DieHard 保留会议版 DOI，摘要来自同文 SIGPLAN Notices 版的出版登记记录。两版均列入证据来源，不作为两项独立研究计数。
- USENIX 某些旧官方 BibTeX 的 URL 为失效的 `http://web/...`。库内改为本次实际读取的公开官方 URL。StackGuard、Baggy 未强填未核验的页码。
- StackGuard 归档封面与正文署名排序不同，封面还出现 `Crispan`；条目采用正文 `Crispin Cowan` 和正文作者顺序。
- CPI 作者顺序采用 USENIX 官方条目。作者课题组索引页的顺序不作为覆盖依据。
- `SoK: Shining Light on Shadow Stacks` 是 IEEE S&P 2019，作者为 `Xinping Zhang`；作者组网页出现的 `Xingping` 不采用。
- CFIXX 的 NDSS DOI 登记题名为 `CFIXX: Object Type Integrity for C++`，作者 PDF 标题带 `Virtual Dispatch`。两者 DOI 相同；库内采用 DOI 登记题名并保留差异说明。
- TypeSan 采用 ACM/Crossref 与论文正文共同支持的作者顺序；作者组索引另有名称/排序差异。HexType 正文和出版记录署名为 `Scott Carr`，本条保留此署名。
- MemorySanitizer 的 Crossref 标题存在双重 HTML 转义，已还原 `C++`。原论文 Google PDF 在此次远端网络中下载失败，因此其方法依据明确标记为官方项目文档，不能宣称已读原论文摘要/全文。
- memory tagging 条目保留 arXiv 预印本身份；它不能代替当前 Arm MTE 实现说明。
- Blade 采用 POPL/PACMPL 正文 DOI `10.1145/3434330`，不把复现包登记项误当论文；此前查询命中的无关 arXiv 项没有进入文献库。

- 期刊日期有两种口径：CFI survey 采用作者组与出版登记支持的首次在线年份 2017（Crossref 另列 2018 印刷日期）；Blazy 等常数时间论文采用卷期年 2019（2018 首次在线）。两条均在 JSON 保留 online/print 日期，防止误认成不同论文。CFI survey 作者稿仍有占位 DOI/卷期，未用于覆盖最终出版元数据。

## 候选使用表

| Key | 文献 | 年份 | 优先级 | 可能用途 |
|---|---|---:|---|---|
| `abadi2009cfi` | Control-flow integrity principles, implementations, and applications | 2009 | core | 用于定义 CFI 的基本策略、控制流约束及其与影子调用栈的联系。 |
| `burow2017cfisurvey` | Control-Flow Integrity: Precision, Security, and Performance | 2017 | core | 用于组织 CFI 精度、安全性、性能和前向/后向边比较维度。 |
| `cowan1998stackguard` | StackGuard: Automatic Adaptive Detection and Prevention of Buffer-Overflow Attacks | 1998 | core | 用于交代编译器插入栈保护的历史及 canary 机制的背景。 |
| `kuznetsov2014cpi` | Code-Pointer Integrity | 2014 | core | 用于介绍代码指针保护、CPI/CPS 及安全栈分离相关设计背景。 |
| `tice2014forwardcfi` | Enforcing Forward-Edge Control-Flow Integrity in GCC & LLVM | 2014 | core | 用于说明生产编译器中的前向边 CFI 及增量编译、动态库等兼容性约束。 |
| `burow2019shadowstacks` | SoK: Shining Light on Shadow Stacks | 2019 | core | 用于讨论后向边保护、影子栈的安全性、性能及兼容性权衡。 |
| `mashtizadeh2015ccfi` | CCFI: Cryptographically Enforced Control Flow Integrity | 2015 | supporting | 用于补充基于消息认证码的代码指针完整性机制和编译器支持的历史背景。 |
| `zhang2016vtrust` | VTrust: Regaining Trust on Virtual Calls | 2016 | supporting | 用于补充针对 C++ 虚调用的类型约束和虚表指针保护设计。 |
| `burow2018cfixx` | CFIXX: Object Type Integrity for C++ | 2018 | supporting | 用于说明动态对象类型完整性与静态合法目标集合之间的区别，以及 OTI 对 CFI 的补充。 |
| `serebryany2012asan` | AddressSanitizer: A Fast Address Sanity Checker | 2012 | core | 用于介绍地址 sanitizer 的编译器插桩、分配器与内存错误检测背景。 |
| `stepanov2015msan` | MemorySanitizer: Fast Detector of Uninitialized Memory Use in C++ | 2015 | core | 用于区分未初始化值使用检测与地址越界检测，并记录全栈插桩的实际约束。 |
| `nagarakatte2009softbound` | SoftBound: Highly Compatible and Complete Spatial Memory Safety for C | 2009 | core | 用于介绍通过分离的每指针 base/bound 元数据实施空间内存安全。 |
| `nagarakatte2010cets` | CETS: compiler enforced temporal safety for C | 2010 | core | 用于介绍对象标识符和指针元数据支持的时间内存安全，与空间安全形成对照。 |
| `akritidis2009baggy` | Baggy Bounds Checking: An Efficient and Backwards-Compatible Defense against Out-of-Bounds Errors | 2009 | supporting | 用于说明边界检查中安全粒度、元数据布局与兼容性的设计权衡。 |
| `berger2006diehard` | DieHard: probabilistic memory safety for unsafe languages | 2006 | optional | 用于补充随机化、冗余与概率性内存安全容错的另一类设计。 |
| `duck2018effectivesan` | EffectiveSan: type and memory error detection using dynamically typed C/C++ | 2018 | supporting | 用于补充动态类型检查、类型元数据和子对象边界检测等 sanitizer 设计维度。 |
| `haller2016typesan` | TypeSan: Practical Type Confusion Detection | 2016 | supporting | 用于说明 C++ 错误类型转换检测与每对象运行时类型元数据。 |
| `jeon2017hextype` | HexType: Efficient Detection of Type Confusion Errors for C++ | 2017 | supporting | 用于补充显式运行时类型检查、对象分配模式覆盖及 sanitizer 优化。 |
| `serebryany2018memorytagging` | Memory Tagging and how it improves C/C++ memory safety | 2018 | supporting | 用于介绍内存标记机制及硬件/编译器协作的背景。 |
| `jeon2020fuzzan` | FuZZan: Efficient Sanitizer Metadata Design for Fuzzing | 2020 | core | 用于区分提高 fuzzing 中 sanitizer 运行效率的工作与检测编译器防御实现错误的工作。 |
| `marini2025qmsan` | QMSan: Efficiently Detecting Uninitialized Memory Errors During Fuzzing | 2025 | supporting | 用于补充近期未初始化内存检测、二进制翻译和 fuzzing 场景下插桩兼容性问题。 |
| `szekeres2013eternalwar` | SoK: Eternal War in Memory | 2013 | core | 用于组织空间/时间内存安全、代码指针保护等策略的关系和部署权衡。 |
| `yang2017deadstore` | Dead Store Elimination (Still) Considered Harmful | 2017 | core | 直接支持编译器优化可能破坏程序员预期的敏感数据擦除，以及擦除技术和编译器支持的讨论。 |
| `simon2018whatyouc` | What You Get is What You C: Controlling Side Effects in Mainstream C Compilers | 2018 | core | 用于论证常数时间和秘密擦除等隐含安全属性需要显式编译器支持，而普通 C 可观察行为不足以表达全部安全意图。 |
| `almeida2016ctverif` | Verifying Constant-Time Implementations | 2016 | core | 用于说明常数时间是关系型安全属性，以及可在优化后的 LLVM 实现上开展专门验证。 |
| `blazy2019constanttime` | Verifying constant-time implementations by abstract interpretation | 2019 | supporting | 用于补充基于抽象解释的 C 源程序常数时间验证及其与 CompCert/Verasco 的联系。 |
| `oleksenko2020specfuzz` | SpecFuzz: Bringing Spectre-type vulnerabilities to the surface | 2020 | core | 用于介绍通过软件暴露推测执行路径、结合检查器和 fuzzing 检测特定推测执行风险的思路。 |
| `guarnieri2020spectector` | Spectector: Principled Detection of Speculative Information Flows | 2020 | core | 用于补充基于符号执行与 SMT 的推测信息流分析，以及检查编译器插入推测执行缓解措施的相关工作。 |
| `vassena2021blade` | Automatically Eliminating Speculative Leaks from Cryptographic Code with Blade | 2021 | core | 用于补充通过类型系统约束推测信息流并自动插入保护的编译器防御研究。 |

## 暂未纳入的候选

ProPolice、Low-Fat Pointers、KCoFI、STT、TypeArmor 等仍可按实际写作需要继续补核；本批未因搜索命中就直接生成已核验条目。KCoFI 历史论文与现代 Clang KCFI 不能仅凭近似缩写混同。暂未纳入也不构成这些方向不存在工作的结论。

## 与 DeFuzz 比较时需保留的边界

防御论文介绍的是特定策略或实现；sanitizer/fuzzing 论文通常检测被测程序错误；验证论文证明的性质相对其执行、泄漏或语言模型成立。与 DeFuzz 比较时应明确被测对象、oracle、输入生成、执行覆盖及威胁模型，不能简单把“保护程序”“检测程序漏洞”“检测防御实现错误”合并为同一问题。保留各条目的限制，避免把论文当时的“all known attacks”“无误报”等描述扩大为今天的无条件事实。
