# 既有 Related Work 与方法基础候选

核验日期：2026-11-12。共 23 项，其中 14 项沿用此前对原始论文方法/oracle章节的选择性核验，另外 9 项来自本轮一手出版/作者页面与官方软件仓库。文献收集不等于全文评审。

## 既有条目需要修正的元数据

本轮只在候选库提供纠正条目，未改论文的 `refs.bib`。

| 条目 | 发现的问题与核实结果 | 一手来源 |
| --- | --- | --- |
| Silent Bugs Matter | 现有作者误为 Giuseppe Antonio Di Luna 等；实际第一作者 Jianhao Xu，共 8 位作者，USENIX Security 2023，3655–3672。 | [官方出版页](https://www.usenix.org/conference/usenixsecurity23/presentation/xu-jianhao) |
| AgentFuzz | 现有题名不符；正式题名为 Make Agent Defeat Agent: Automatic Detection of Taint-Style Vulnerabilities in LLM-based Agents，补齐 12 位作者及页码。 | [官方出版页](https://www.usenix.org/conference/usenixsecurity25/presentation/liu-fengyu) |
| SpecAuditor | 现有副标题不符；官方录用题名为 Generating Audit Specifications for LLM-Driven Bug Detection。未拿到可靠摘要/全文，因此仅标 metadata-only。 | [官方录用列表](https://sp2026.ieee-security.org/accepted-papers.html#collapse-212) |
| Chain-of-Thought | 原条目漏署 Brian Ichter；官方共 9 位作者。 | [NeurIPS出版页](https://papers.nips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html) |
| RAG | 官方作者为 Heinrich Küttler；候选 BibTeX 保留变音符号。 | [NeurIPS出版页](https://papers.nips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) |

Z3 增补出版 DOI，但没有假称读到摘要。LangGraph 改用官方软件引用并记录访问日期，不将未核定的 2024 当成页面发表年。CIll 明确是 arXiv 预印本。

## 使用边界

- Silent Bugs Matter 适合支撑动机，但不能将所有 compiler-introduced security bugs 都归为编译器违反语言语义的实现缺陷。
- SpecAuditor 优先补读，当前只可确认文献身份；禁止从题名补写算法、效果或比较结论。
- AgentFuzz 的对象是 LLM-agent 应用，不是编译器防御测试。
- CoT/RAG 可支撑方法来源，不能支撑“生成属性/检查器保证正确”的结论。
- 14 篇 Related Work 的逐项原文位置及不能外推的边界保存在 JSON 和生成的 catalog 中。未运行论文复现，也未将任何结果数字迁入稿件。
