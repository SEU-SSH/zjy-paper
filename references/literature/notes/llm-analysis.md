# LLM辅助测试、分析、规范与agent检索参考库

核验日期：2026-11-12。共28条新增文献，已与当前39条refs.bib去重；不重复既有Related Work 14篇及CoT、RAG、LangGraph。这里只建立候选文献库，不表示28篇均应进入正文。

## 证据层级与使用规则

本轮以正式出版社/Crossref记录、会议论文集、作者arXiv页面及作者机构页面核对元数据，并阅读一手摘要。统一标为metadata+abstract；不声称完成全文细读、独立验证方法正确性或复现实验。需要在正文使用机制细节、比较“不能做到什么”或实验数字时，应继续读对应方法和实验段落。source_urls记录实际读取并用于支持条目的URL；Google仅作发现入口，不作为事实证据。

原始下载与浏览器提取位于树外 `~/defuzz-project/feiyang-writing/reference-library-2026-11-12-evidence/llm-analysis/`。该目录包含检索候选及被排除的无关页面；只有collections/llm-analysis.json中的28条属于已收录项。远端Crossref/DBLP曾返回429，arXiv请求曾超时，因此通过本机浏览器下载小型元数据并上传。OpenReview校验页不被作为已读取论文证据。

## 优先阅读建议

- 生成与反馈路线优先：TitanFuzz、FuzzGPT、PromptFuzz、CodaMosa、CoverUp。ChatAFL用于跨领域知识驱动输入生成；ChatFuzz和LLAMAFUZZ补充灰盒变异。
- 规范与可信边界优先：nl2spec、AutoSpec、Lemur、Clover。重点区分候选要求、形式模型中的验证和自然语言意图正确性。
- 分析器近邻优先：IRIS、LLift、InferROI、GPTScan；Artemis补充2025特定缺陷模型的LLM辅助静态分析。
- 方法背景按实际需要选：BM25与DPR支持检索路线；ReAct、Reflexion、SWE-agent、AutoGen支持编排背景；Self-Refine有助于对照模型自反馈与外部程序反馈。Toolformer仅作可选背景。

## 已处理的版本与名称差异

- FuzzGPT：arXiv题名为“Large Language Models are Edge-Case Fuzzers: Testing Deep Learning Libraries via FuzzGPT”；正式ICSE2024题名为“Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries”。采用正式元数据。
- PromptFuzz的正确论文题名为“Prompt Fuzzing for Fuzz Driver Generation”，CCS2024，DOI 10.1145/3658644.3670396。另有2026题名含PromptFuzz的提示注入测试论文，不是同一工作。
- CoverUp正式FSE2025题名为“CoverUp: Effective High Coverage Test Generation for Python”；不能沿用旧预印本题名却填写新DOI。第一作者姓氏依正式Crossref拆分为Altmayer Pizzorno。
- SymPrompt是方法名，正式论文为“Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM”，PACMSE/FSE2024。
- Clover正式载体为AI Verification（2024），DOI 10.1007/978-3-031-65112-0_7；不写成FSE。
- Reflexion：NeurIPS正式作者列表不含arXiv页面出现的Edward Berman；采用会议列表。Toolformer正式NeurIPS版本包含Eric Hambro，arXiv初版列表少此作者；采用会议列表。
- AutoGen：COLM2024官方录用列表题名末尾为Multi-Agent Conversations，arXiv为Multi-Agent Conversation；28条库采用已读的官方录用列表题名，并保留两种一手来源。OpenReview正文因校验未读，若最后以其版本排版应再对齐题名。
- ChatFuzz的作者预印本为“Augmenting Greybox Fuzzing with Generative AI”，arXiv:2306.06782；本轮不替它虚构会议。LLAMAFUZZ是另一篇，已核实AST2026正式DOI。

## 既有条目边界

已有CoT、RAG、LangGraph等条目由主线程整理，本集合不重收。原refs.bib的AgentFuzz、SpecAuditor等条目在初读时缺完整定位信息；本集合未确认其现有字段准确性，交由主线程核验，不据此判断文献虚构，也不改动正文或refs.bib。

## 逐条记录

### deng2023titanfuzz

**Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models**（2023；Proceedings of the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis；core）

作者：Yinlin Deng；Chunqiu Steven Xia；Haoran Peng；Chenyuan Yang；Lingming Zhang。

潜在支持点：LLM同时承担程序生成与补全式变异，利用训练语料中语言/API约束知识提高输入有效性；适合相关工作中生成侧背景。

不可外推：评估对象主要是深度学习库；不能外推到编译器防御完整性，也不能把生成有效性当成oracle正确性。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1145%2F3597926.3598067)；[2](https://arxiv.org/abs/2212.14834)。

### deng2024fuzzgpt

**Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries**（2024；Proceedings of the IEEE/ACM 46th International Conference on Software Engineering；core）

作者：Yinlin Deng；Chunqiu Steven Xia；Chenyuan Yang；Shizhuo Dylan Zhang；Shujing Yang；Lingming Zhang。

潜在支持点：利用历史触发缺陷程序的稀有成分，通过in-context learning或fine-tuning生成非常规输入；可支持缺陷历史作为生成知识源。

不可外推：历史bug模式启发输入不等于从历史补丁准确恢复防御规范；本文收录正式ICSE题名，预印本题名不同。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1145%2F3597503.3623343)；[2](https://arxiv.org/abs/2304.02014)。

### meng2024chatafl

**Large Language Model guided Protocol Fuzzing**（2024；Proceedings 2024 Network and Distributed System Security Symposium；core）

作者：Ruijie Meng；Martin Mirchev；Marcel Böhme；Abhik Roychoudhury。

潜在支持点：利用LLM中的协议知识生成消息语法并引导消息序列探索，说明自然语言领域知识能够辅助结构化测试。

不可外推：评估对象是网络协议实现；状态覆盖不证明编译产物防御性质。不能把论文结果外推到任意协议或任意模型。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.14722%2Fndss.2024.24556)；[2](https://www.ndss-symposium.org/ndss-paper/large-language-model-guided-protocol-fuzzing/)。

### lyu2024promptfuzz

**Prompt Fuzzing for Fuzz Driver Generation**（2024；Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security；core）

作者：Yunlong Lyu；Yuxuan Xie；Peng Chen；Hao Chen。

潜在支持点：覆盖反馈驱动prompt变异与fuzz driver生成，并结合程序验证和调度；可用于输入/驱动合成及反馈循环近邻。

不可外推：它生成库测试驱动，不生成DeFuzz防御oracle；不要与另一篇同名PromptFuzz提示注入测试论文混淆。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1145%2F3658644.3670396)；[2](https://arxiv.org/abs/2312.17677)。

### hu2023chatfuzz

**Augmenting Greybox Fuzzing with Generative AI**（2023；arXiv preprint arXiv:2306.06782；supporting）

作者：Jie Hu；Qian Zhang；Heng Yin。

潜在支持点：从灰盒fuzzer的seed pool选取种子，提示生成模型产生更符合格式的变体；适合说明LLM辅助变异的早期工作。

不可外推：本轮核实的是2023作者预印本，未核实正式出版版本；原文明确在复杂非平凡语法目标上未普遍优于AFL++。

阅读深度：已核对作者arXiv元数据并阅读摘要；未核实正式出版版本，未逐节精读或复现实验。

一手来源：[1](https://arxiv.org/abs/2306.06782)。

### zhang2026llamafuzz

**LLAMAFUZZ: Large Language Model Enhanced Greybox Fuzzing**（2026；Proceedings of the 7th ACM/IEEE International Conference on Automation of Software Test；supporting）

作者：Hongxiang Zhang；Yuyang Rong；Yifeng He；Hao Chen。

潜在支持点：通过配对变异种子微调LLM并接入灰盒fuzzing，补充结构化输入变异路线；正式AST2026版本已核。

不可外推：通用程序的结构化数据变异，不是编译器防御oracle；摘要中的覆盖/bug结果只适用于其基准、配置和统计口径。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1145%2F3793654.3793756)；[2](https://arxiv.org/abs/2406.07714)。

### lemieux2023codamosa

**CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models**（2023；2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)；core）

作者：Caroline Lemieux；Jeevana Priya Inala；Shuvendu K. Lahiri；Siddhartha Sen。

潜在支持点：搜索式测试覆盖进入平台期时，调用LLM产生欠覆盖函数的示例，再由搜索继续探索；可支持按反馈选择模型介入时机。

不可外推：覆盖提高并不证明安全性质；这里的LLM辅助单元测试生成不能直接当成编译器防御对照实验结果。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1109%2FICSE48619.2023.00085)；[2](https://www.microsoft.com/en-us/research/publication/codamosa-escaping-coverage-plateaus-in-test-generation-with-pre-trained-large-language-models/)。

### ryan2024symprompt

**Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM**（2024；Proceedings of the ACM on Software Engineering；supporting）

作者：Gabriel Ryan；Siddhartha Jain；Mingyue Shang；Shiqi Wang；Xiaofei Ma；Murali Krishna Ramanathan；Baishakhi Ray。

潜在支持点：把生成过程拆成与执行路径对齐的多阶段prompt，并提供类型及依赖上下文；可支持源码条件与输入生成的连接。

不可外推：路径引导用于Python回归测试，不能声称它不利用源码，也不能把路径覆盖等同于语义正确性证明。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1145%2F3643769)；[2](https://arxiv.org/abs/2402.00097)。

### altmayerpizzorno2025coverup

**CoverUp: Effective High Coverage Test Generation for Python**（2025；Proceedings of the ACM on Software Engineering；core）

作者：Juan Altmayer Pizzorno；Emery D. Berger。

潜在支持点：迭代结合覆盖分析、代码上下文和执行反馈生成高覆盖Python回归测试；是2025年反馈驱动测试生成近邻。

不可外推：正式题名已改为Effective High Coverage Test Generation for Python；覆盖结果不能证明oracle或程序语义完整。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1145%2F3729398)；[2](https://arxiv.org/abs/2403.16218)。

### chen2024chatunitest

**ChatUniTest: A Framework for LLM-Based Test Generation**（2024；Companion Proceedings of the 32nd ACM International Conference on the Foundations of Software Engineering；supporting）

作者：Yinghao Chen；Zehao Hu；Chen Zhi；Junxiao Han；Shuiguang Deng；Jianwei Yin。

潜在支持点：自适应focal context及generation-validation-repair流程，可作为上下文压缩、生成后检查与修复的工程近邻。

不可外推：收录的是FSE2024 Companion工具论文；通过编译/测试检查不代表生成断言准确表达用户意图。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1145%2F3663529.3663801)；[2](https://arxiv.org/abs/2305.04764)。

### cosler2023nl2spec

**nl2spec: Interactively Translating Unstructured Natural Language to Temporal Logics with Large Language Models**（2023；Computer Aided Verification；core）

作者：Matthias Cosler；Christopher Hahn；Daniel Mendoza；Frederik Schmitt；Caroline Trippel。

潜在支持点：将自然语言要求转成时序逻辑，并把子公式映射回原文供人交互修正；非常适合说明规范提取的歧义和可追溯性。

不可外推：明确包含用户增删改子翻译；不能写成全自动正确恢复规范，更不能据此声称DeFuzz结构化要求就是形式化证明。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1007%2F978-3-031-37703-7_18)；[2](https://arxiv.org/abs/2303.04864)。

### sun2024clover

**Clover: Closed-Loop Verifiable Code Generation**（2024；AI Verification；core）

作者：Chuyue Sun；Ying Sheng；Oded Padon；Clark Barrett。

潜在支持点：检查代码、docstring与形式化标注的一致性，结合LLM和验证工具；可用于讨论生成规范与代码之间的交叉检查。

不可外推：摘要评估为教材级Dafny程序；基准上的零误接收不是普遍零误报保证，也不是编译器防御语义正确性证据。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1007%2F978-3-031-65112-0_7)；[2](https://arxiv.org/abs/2310.17807)。

### wen2024autospec

**Enchanting Program Specification Synthesis by Large Language Models Using Static Analysis and Program Verification**（2024；Computer Aided Verification；core）

作者：Cheng Wen；Jialun Cao；Jie Su；Zhiwu Xu；Shengchao Qin；Mengda He；Haokun Li；Shing-Chi Cheung；Cong Tian。

潜在支持点：静态分析和验证器驱动LLM生成候选规范，分解程序并逐轮验证候选；适合说明生成器与外部判据分工。

不可外推：候选规范在给定形式模型中验证，不自动等于自然语言防御意图正确；不要把AutoSpec当作仅生成loop invariant的系统。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1007%2F978-3-031-65630-9_16)；[2](https://arxiv.org/abs/2404.00762)。

### wu2024lemur

**Lemur: Integrating Large Language Models in Automated Program Verification**（2024；The Twelfth International Conference on Learning Representations；core）

作者：Haoze Wu；Clark Barrett；Nina Narodytska。

潜在支持点：将LLM提出候选证明信息与自动推理器组合，并给出规则及soundness论证；适合对照程序化验证和LLM启发式的边界。

不可外推：论文证明的可靠性依赖其验证演算与自动推理器前提；不能移植成DeFuzz确定执行checker的语义正确性保证。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://arxiv.org/abs/2310.04870)；[2](https://theory.stanford.edu/~barrett/pubs/WCB24-abstract.html)。

### li2025iris

**IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities**（2025；The Thirteenth International Conference on Learning Representations；core）

作者：Ziyang Li；Saikat Dutta；Mayur Naik。

潜在支持点：结合LLM推断污点规范、上下文分析与全仓库静态推理；直接相关于模型提供知识、分析器承担系统检查的路线。

不可外推：面向Java安全缺陷检测；LLM参与规范与上下文判别，不能概括成完全没有模型介入的裁决链或任意源码检查器合成。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://arxiv.org/abs/2405.17238)；[2](https://proceedings.iclr.cc/paper_files/paper/2025/hash/582d4e27fa24168f3af1f4582655034b-Abstract-Conference.html)。

### li2024llift

**Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach**（2024；Proceedings of the ACM on Programming Languages；core）

作者：Haonan Li；Yu Hao；Yizhuo Zhai；Zhiyun Qian。

潜在支持点：将静态分析与LLM结合，通过post-constraint guidance改进Linux内核use-before-initialization分析；可说明语义辅助路径筛选。

不可外推：针对特定缺陷模型和内核变量约定；不是通用checker生成，也不是形式化soundness保证。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1145%2F3649828)。

### ji2025artemis

**Artemis: Toward Accurate Detection of Server-Side Request Forgeries through LLM-Assisted Inter-procedural Path-Sensitive Taint Analysis**（2025；Proceedings of the ACM on Programming Languages；supporting）

作者：Yuchen Ji；Ting Dai；Zhichao Zhou；Yutian Tang；Jingzhu He。

潜在支持点：LLM辅助的过程间、路径敏感污点分析，是从规范/上下文知识进入静态分析的2025近邻。

不可外推：对象为PHP中的SSRF，已有分析器核心及特定规则；本轮只读摘要，LLM具体介入点应在正文引用前再精读方法。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1145%2F3720488)；[2](https://arxiv.org/abs/2502.21026)。

### wang2025inferroi

**Boosting Static Resource Leak Detection via LLM-based Resource-Oriented Intention Inference**（2025；2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)；core）

作者：Chong Wang；Jianan Liu；Xin Peng；Yang Liu；Yiling Lou。

潜在支持点：LLM推断资源获取、释放和可达性验证意图，再结合两阶段静态分析检查泄漏；与“规范/意图生成+程序检查”相关。

不可外推：意图推断不是完整资源语义证明；原论文作者验证与开发者确认数量不同，不能混写成全部获开发者确认。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1109%2FICSE55347.2025.00131)；[2](https://arxiv.org/abs/2311.04448)。

### sun2024gptscan

**GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis**（2024；Proceedings of the IEEE/ACM 46th International Conference on Software Engineering；core）

作者：Yuqiang Sun；Daoyuan Wu；Yue Xue；Han Liu；Haijun Wang；Zhengzi Xu；Xiaofei Xie；Yang Liu。

潜在支持点：以LLM识别逻辑缺陷候选及关键变量/语句，再执行静态确认；可支持模型建议与程序分析证据相结合。

不可外推：静态确认降低误报并不消除误报；智能合约业务逻辑和编译器防御要求不同，不能直接外推精度数字。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works?query.title=GPTScan%20Detecting%20Logic%20Vulnerabilities&rows=3)；[2](https://arxiv.org/abs/2308.03314)。

### yao2023react

**ReAct: Synergizing Reasoning and Acting in Language Models**（2023；The Eleventh International Conference on Learning Representations；supporting）

作者：Shunyu Yao；Jeffrey Zhao；Dian Yu；Nan Du；Izhak Shafran；Karthik Narasimhan；Yuan Cao。

潜在支持点：交替推理、动作与环境观察的agent设计先例；可为DeFuzz迭代读取源码、执行工具、根据反馈调整生成的组织方式提供背景。

不可外推：ReAct是通用agent范式，不是编译器测试专用算法；它不提供工具输出或最终判定正确性的保证。

阅读深度：已核对作者arXiv的ICLR camera-ready说明并阅读摘要、作者项目页的prompting说明；未复现实验。

一手来源：[1](https://arxiv.org/abs/2210.03629)；[2](https://react-lm.github.io/)。

### shinn2023reflexion

**Reflexion: language agents with verbal reinforcement learning**（2023；Advances in Neural Information Processing Systems；supporting）

作者：Noah Shinn；Federico Cassano；Ashwin Gopinath；Karthik Narasimhan；Shunyu Yao。

潜在支持点：将任务反馈转换为语言反思并保存到episodic memory，用于下一次尝试；可讨论跨轮反馈积累。

不可外推：语言反思不是独立验证器，也不等于更新模型参数的强化学习；正式会议作者名单与arXiv元数据不同，采用会议名单。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html)。

### yang2024sweagent

**SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering**（2024；Advances in Neural Information Processing Systems；supporting）

作者：John Yang；Carlos E. Jimenez；Alexander Wettig；Kilian Lieret；Shunyu Yao；Karthik Narasimhan；Ofir Press。

潜在支持点：agent-computer interface对仓库导航、文件编辑和测试执行的作用，可支撑工具接口与agent能力分离的设计理由。

不可外推：软件修复基准成功率不能作为编译器缺陷发现能力或防御验证正确性的依据。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html)。

### wu2024autogen

**AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversations**（2024；First Conference on Language Modeling；supporting）

作者：Qingyun Wu；Gagan Bansal；Jieyu Zhang；Yiran Wu；Beibin Li；Erkang Zhu；Li Jiang；Xiaoyun Zhang；Shaokun Zhang；Jiale Liu；Ahmed Hassan Awadallah；Ryen W White；Doug Burger；Chi Wang。

潜在支持点：可编程多agent对话以及模型、工具、人类输入的组合框架；仅在解释编排背景时引用。

不可外推：框架通用性不是DeFuzz采用特定多agent配置有效的实验证据；不能把多agent编排称为本项目独有。

阅读深度：已核对COLM2024官方录用名单及完整作者列表，并阅读作者arXiv摘要；官方录用列表题名为Conversations，预印本为Conversation。OpenReview遇到浏览器校验，未读取其正文。

一手来源：[1](https://arxiv.org/abs/2308.08155)；[2](https://colmweb.org/2024/AcceptedPapers.html)。

### schick2023toolformer

**Toolformer: Language Models Can Teach Themselves to Use Tools**（2023；Advances in Neural Information Processing Systems；optional）

作者：Timo Schick；Jane Dwivedi-Yu；Roberto Dessi；Roberta Raileanu；Maria Lomeli；Eric Hambro；Luke Zettlemoyer；Nicola Cancedda；Thomas Scialom。

潜在支持点：通过自监督训练学习何时、怎样调用API的工具使用先例，可为背景中的工具增强语言模型提供出处。

不可外推：Toolformer包含模型训练，不能拿来直接证明纯prompt驱动工具循环的效果；正式版多一位作者Eric Hambro。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://papers.nips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html)。

### madaan2023selfrefine

**Self-Refine: Iterative Refinement with Self-Feedback**（2023；Advances in Neural Information Processing Systems；supporting）

作者：Aman Madaan；Niket Tandon；Prakhar Gupta；Skyler Hallinan；Luyu Gao；Sarah Wiegreffe；Uri Alon；Nouha Dziri；Shrimai Prabhumoye；Yiming Yang；Shashank Gupta；Bodhisattwa Prasad Majumder；Katherine Hermann；Sean Welleck；Amir Yazdanbakhsh；Peter Clark。

潜在支持点：同一模型生成、反馈和修订的迭代模式；可作为与外部编译/执行反馈不同的自我修订路线。

不可外推：模型自反馈不是独立oracle；不应由其平均任务增益推出编译器测试中的可靠性。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html)。

### liu2024lostmiddle

**Lost in the Middle: How Language Models Use Long Contexts**（2024；Transactions of the Association for Computational Linguistics；supporting）

作者：Nelson F. Liu；Kevin Lin；John Hewitt；Ashwin Paranjape；Michele Bevilacqua；Fabio Petroni；Percy Liang。

潜在支持点：相关信息在长上下文中位置不同会影响模型表现；可解释为什么检索和上下文组织值得做消融。

不可外推：实验主要是问答和键值检索；不能宣称它已经证明某种源码切片或BM25优于embedding。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works?query.title=Lost%20in%20the%20Middle%20How%20Language%20Models%20Use%20Long%20Contexts&rows=3)；[2](https://arxiv.org/abs/2307.03172)。

### robertson2009bm25

**The Probabilistic Relevance Framework: BM25 and Beyond**（2009；Foundations and Trends in Information Retrieval；core）

作者：Stephen Robertson；Hugo Zaragoza。

潜在支持点：BM25/BM25F概率相关性框架的权威系统阐述，可支撑方法部分词法检索公式和参数来源。

不可外推：这是检索方法基础，不是针对编译器源码的优越性证据；不能把经典BM25和项目定制融合排序的效果混为一谈。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://api.crossref.org/works/10.1561%2F1500000019)。

### karpukhin2020dpr

**Dense Passage Retrieval for Open-Domain Question Answering**（2020；Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)；supporting）

作者：Vladimir Karpukhin；Barlas Oguz；Sewon Min；Patrick Lewis；Ledell Wu；Sergey Edunov；Danqi Chen；Wen-tau Yih。

潜在支持点：双编码器dense passage retrieval的代表工作；可在方法或检索消融背景中说明密集检索路线。

不可外推：在开放域问答上优于BM25不代表编译器标识符、pass名或代码上下文也更好。

阅读深度：已核对正式元数据及一手摘要；未逐节精读、未复现实验。

一手来源：[1](https://aclanthology.org/2020.emnlp-main.550/)。
