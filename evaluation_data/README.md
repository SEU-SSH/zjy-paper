# DeFenzz Authoritative Evaluation Data & Writing Handbook

> **Single Source of Truth for Paper Writing Agents (`IEEE S&P` Submission)**
> - **Last Verified**: `2026-11-17`
> - **Engineering Repo Path**: `/Users/bytedance/projects/research/defenzz/main/docs/evaluation/`
> - **Mirrored Paper Repo Path**: `/Users/bytedance/projects/research/defenzz-paper/evaluation_data/`
> - **Status**: **100% Complete, Cross-Verified, Zero `TBD`s**

---

## 1. Directory Map (Start Here)

| File | Scope | Machine-Readable JSON | Drop-in LaTeX Table(s) |
| :--- | :--- | :--- | :--- |
| **[`01-main-experiment-rq1.md`](./01-main-experiment-rq1.md)** | **Main Experiment (RQ1)** + **Offline Invariant & Check-IR Funnel** + **Case Studies** (`111` silent defense bugs, `30` confirmed, `11` fixed; `921` invariants $\to$ `915` checkers) | [`data/01_main_rq1.json`](./data/01_main_rq1.json) | [`tables/tab_rq1_bugs.tex`](./tables/tab_rq1_bugs.tex)<br>[`tables/tab_offline_funnel.tex`](./tables/tab_offline_funnel.tex) |
| **[`02-baseline-comparison-rq2.md`](./02-baseline-comparison-rq2.md)** | **Baseline Comparison (RQ2)** (`YARPGen`, `UBfuzz`, `MetaMut` at `1c × 12h × 5`; official upstream `Fuzz4All`, `FeatureFuzz` at `@21,415 calls`; Per-Mechanism Small-Pot + Step-5 Audit Parity) | [`data/02_baseline_rq2.json`](./data/02_baseline_rq2.json) | [`tables/tab_rq2_comparison.tex`](./tables/tab_rq2_comparison.tex) |
| **[`03-ablation-study-rq3.md`](./03-ablation-study-rq3.md)** | **Component Ablation Study (RQ3)** (`w/o Formal Check IR`, `w/o Hybrid RAG` on full 921-invariant 4-ISA campaign; `w/o Source Mapping`, `w/o Programmatic Oracle`, `Bare Agent` on controlled 41-invariant GCC-16 AArch64 lane) | [`data/03_ablation_rq3.json`](./data/03_ablation_rq3.json) | [`tables/tab_rq3_ablation.tex`](./tables/tab_rq3_ablation.tex) |
| **[`04-overhead-and-telemetry-rq4.md`](./04-overhead-and-telemetry-rq4.md)** | **System Telemetry, Token Cost & Toolchain Overhead (RQ4)** (`59,671` LLM calls, `1,610.01M` tokens, `92.4%` KV-cache hit, `44.68h` total, `5.5 min`/bug, `99,236` tool calls, clean compiler build times, `0%` target runtime overhead) | [`data/04_overhead_rq4.json`](./data/04_overhead_rq4.json) | [`tables/tab_rq4_overhead.tex`](./tables/tab_rq4_overhead.tex) |

---

## 2. Canonical Headline Numbers Cheat-Sheet (Use Identically Across Abstract, Intro, §4 & §5)

| Metric | Canonical Value | Exact Breakdown & Provenance |
| :--- | :--- | :--- |
| **Evaluated Compilers** | **GCC `16.2.0`** (+ `17.0` trunk repro) & **LLVM/Clang `23.1.2`** | Frozen commits: GCC `78d4ac73dd39`, LLVM `85ac56026243` |
| **Target Architectures (4 ISAs)** | **`x86-64`, `AArch64`, `RISC-V64`, `LoongArch64`** | Cross-compiled + verified under QEMU `9.2.0` user-mode (`rv64gc+zicfilp+zicfiss`, `max`, `la464`) |
| **Defense Families (`F1`–`F6`)** | **6 families (`28+` concrete mechanisms)** | `F1` CFI, `F2` Stack, `F3` Sanitizers, `F4` Scrubbing, `F5` Speculation, `F6` Bounds/Fortify |
| **Offline Invariant Funnel** | **`580` slices $\to$ `921` invariants (`904` CoT + `17` RAG)** | GCC `475` (`463 + 12`), LLVM `446` (`441 + 5`) |
| **Mapped Compiler Paths & Probes** | **`2,922` paths (`747` files) $\to$ `9,061` active 4-ISA probes** | GCC `1,669` paths / `4,537` probes; LLVM `1,253` paths / `4,524` probes |
| **Validated Check-IR Oracles** | **`915` checkers (`99.3%` yield; `82.3%` 1st-attempt)** | GCC `473` (`470` active 4-ISA + `3` NA), LLVM `442` (`433` active 4-ISA + `9` NA) $\Rightarrow$ **`903` active 4-ISA batch checkers** |
| **Previously Unknown Silent Bugs** | **`111` bugs (`58` GCC + `53` LLVM)** | From `131` ledger entries (`docs/bugs/metadata.json`) after excluding `20` non-bugs (`3` FP, `8` suspended review, `7` disputed UB/spec, `2` independently fixed) |
| **Upstream Maintainer Status** | **`30` officially confirmed (`18` GCC, `12` LLVM), `11` fixed (`9` GCC, `2` LLVM)** | `11` fixed + `1` partial-fixed + `18` open `CONFIRMED`/`NEW` = `30` (`+5` more carry maintainer `wrong-code`/`miscompilation` tags; `76` awaiting review) |
| **Cross-ISA Bug Impact** | **`35 / 111` (`31.5%`) affect ONLY non-x86 ISAs** | `47` Cross-ISA (`3+`/generic), `35` Non-x86 Only, `22` `x86-64` Only, `7` Dual-ISA |
| **RQ2 Baseline Comparison Headline** | **`DeFenzz`: `111` bugs (`79.6%` probe cov, `833 / 903 = 92.2%` active checkers, `83 / 111 = 74.8%` exclusive vs. all 5 baselines; `28` baseline union, `0` missed)** | vs. `FeatureFuzz` `23` (`12G/11L`, `79.7%` probes, `187` chk, `0` native), `Fuzz4All` `18` (`8G/10L`, `75.8%` probes, `173` chk, `0` native), `MetaMut` `8` union / `6.4±0.9` (`0` native), `UBfuzz` `3` union / `2.2±0.5`, `YARPGen` `1` union / `1.0±0.0` |
| **RQ3 Formal Check IR Ablation** | **`+29` unique bugs (`111` vs `82`), `2.1×` non-x86 hits (`136` vs `64`), `-51` raw FPs (`0` vs `51`), `11.6×` fewer Step-3 tokens (`54.81M` vs `638.44M`)** | Full 921-invariant / 4-ISA comparison against unconstrained raw Go checker synthesis |
| **RQ4 Cost & Amortization** | **`59,671` calls, `1,610.01M` tokens (`92.4%` cached), `44.68h` total** | `34.52h` one-time offline + `10.16h` online Step 4 (`21,415` calls, `900.84M` tokens) $\Rightarrow$ **`5.5 min` & `8.12M` online tokens per bug**; **`0%` target binary runtime overhead** |

---

## 3. Eight Strict Anti-Pitfall Rules for the Writing Agent

1. **NEVER cite `126` or `131` or `175` as the discovered bug count**:
   - An older draft in `outline_status.md` mentioned `126 Bugs`, and the raw ledger `docs/bugs/metadata.json` has `131` active tracking entries. The canonical, audited, deduplicated count of previously unknown silent defense bugs is strictly **`111` (`58` GCC + `53` LLVM)** (`+20` ICEs observed separately in RQ2 seed evaluation, not counted in the `111` silent defense bugs).
2. **NEVER cite `8c × 24h`, `8c × 8h`, or `@24,000 calls` for RQ2**:
   - Those were pre-execution draft plans (now archived in `docs/_archive_pre_final/`).
   - The final executed RQ2 protocol is strictly:
     - **Traditional fuzzers (`YARPGen`, `UBfuzz`, `MetaMut`)**: **`1 CPU core × 12h × 5` independent trials** (`500` stratified seeds/trial = `2,500` seeds/baseline; report both `mean ± std` and `5-trial Union [U]`).
     - **LLM fuzzers (`Fuzz4All`, `FeatureFuzz`)**: **`@21,415` valid online `deepseek-chat` calls** running their official open-source upstream codebases (`fuzz4all/fuzz4all@0bf42fe037c8761bdde61e1c37a0946e8103fba1` and `addaddgo/FeatureFuzz@7486da17d863293f657a00329ac5b4b23d8cbc7d`; exact 1:1 online call parity with `DeFenzz` Step 4's `21,415` calls; `100%` of unique valid seeds evaluated: `14,906` for `Fuzz4All` and `14,814` for `FeatureFuzz`).
3. **Unify the Six Defense Families (`F1`–`F6`) between RQ1 Table 1 and RQ2**:
   - Ensure RQ1 Table 1 (`tab:bug-summary`) and RQ2 use the identical canonical `F1`–`F6` taxonomy (`473/442 = 915` checkers; `F1: 36, F2: 21, F3: 21, F4: 10, F5: 9, F6: 14` = `111`).
4. **Distinguish `915` Total Validated Checkers vs. `903` Active 4-ISA Batch Checkers**:
   - Step 3 produces **`915` validated checkers (`473` GCC + `442` LLVM)**.
   - In the 4-ISA Linux ELF RQ2 batch harness, `12` checkers (`3` GCC + `9` LLVM, e.g., Windows SEH/PE or non-4-ISA targets) uniformly evaluate to `NA` and are excluded from the RQ2 activation denominator, leaving **`903` active 4-ISA checkers (`470` GCC + `433` LLVM)**.
5. **Report `833 / 903` (`92.2%`) as `DeFenzz`'s Canonical Active Checkers in RQ2**:
   - Across `@21,415` online Step-4 calls, `DeFenzz` activated **`833 / 903` (`92.2%`)** active 4-ISA checkers (vs. at most `187 / 903 = 20.7%` for any baseline) and triggered **`63` batch checkers** (`68` checkers across the full campaign including multi-TU LTO/driver harnesses) to uncover all **`111` bugs** (`83 / 111 = 74.8%` exclusive across all 5 baselines; `28` baseline union, `0` missed). Always report **`833` (`92.2%`)** in RQ2 Table (`tab:rq2-comparison`) and prose (`DeFenzz` spends its `21,415` calls across multi-turn agent loops, synthesizing `715` unique valid seeds in total—zero valid seeds discarded—which cover `7,210 / 9,061 = 79.6%` probes).
6. **Keep the Two RQ3 Ablation Scopes Strictly Separated (Just as `figures/eval-ablation.pdf` Already Does)**:
   - `Full DeFenzz`, `w/o Formal Check IR`, and `w/o Hybrid RAG` are evaluated across the **full 921-invariant, 4-ISA campaign**.
   - `w/o Source Mapping`, `w/o Programmatic Oracle` (`llm-judge`), and `Bare Agent` are evaluated on the **controlled 41-invariant `GCC 16.2.0` `AArch64` end-to-end audit lane (`demo-workset`)**. Never claim those three online ablations were run across all 921 invariants × 4 ISAs.
7. **Respect Locked `[ready]` Sections in `defenzz-paper/main.tex`**:
   - Per `/Users/bytedance/projects/research/defenzz-paper/outline_status.md`, **Abstract**, **Section 2 Motivation**, **Section 3.0 Overview**, and **Section 3.1 Security Invariant Generation** are marked `[ready]`. Do not alter them unless explicitly instructed by the user.
8. **Never Read From Archived Directories**:
   - Ignore `docs/_archive_pre_final/`, `runs/rq2-summary-preview/`, and outdated `PENDING` notes in `runs/paper-evaluation-summary/rq4_cost_overhead.md`.
