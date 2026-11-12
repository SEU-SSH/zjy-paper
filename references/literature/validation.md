# 文献库检查记录

检查日期：2026-11-12。比较基准是 Related Work 提交 `a60e54e061686af36592fe3b5673ae6cb754d983`。

- 136 个 JSON 条目具备必需字段、来源链接、阅读深度、用途和限制；25 项 metadata+method、75 项 metadata+abstract、2 项 metadata-only、34 项 official-doc。
- 使用 bibtexparser 1.4.3 成功解析全部条目；逐项核对 JSON 与 BibTeX 的 key、类型、年份和 DOI 一致。BibTeX采用ASCII及标准TeX作者名转义，JSON/Markdown采用UTF-8。
- 按规范化引用键、题名和 DOI 检查无重复；114个新增键与基准 refs.bib 的引用键、题名和DOI没有冲突。原书目39项，其中22个key在完整候选库内保留。
- 检查 Markdown 本地文件链接和 catalog 显式锚点均能解析；中文无替代字符。来源网页的核验范围见各条目，不将“链接存在”等同于“全文已读”。
- 用 Tectonic 0.17.0 内的 BibTeX 0.99d 和论文同款 IEEEtran class / IEEEtran.bst 1.14，运行两个 `nocite{*}` 独立检查：完整库成功生成136个bibitem；原refs.bib加additional.bib成功生成153个bibitem。两个BibTeX日志均无错误或警告。
- 两个TeX检查均成功输出PDF；长URL换行存在underfull box提示，未产生引用缺失/重复键错误。该检查针对书目解析及加载，不是整篇投稿稿件的排版检查。
- 本分支相对基准仅新增 `references/literature/`；`main.tex`、`refs.bib`、`main.pdf` 未修改。原书目错误仅在候选库及纠错笔记中处理，供作者后续按key替换。

完整日志、生成脚本和SHA-256清单保留在 ssh004：`~/defuzz-project/feiyang-writing/pr-reference-library-2026-11-12-qa/`。原始来源快照在 `reference-library-2026-11-12-evidence/`，与Git提交分离。
