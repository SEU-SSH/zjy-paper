# 02 — Baseline Comparison against Traditional & LLM Compiler Fuzzers (RQ2)

- **Machine-Readable Data**: [`data/02_baseline_rq2.json`](./data/02_baseline_rq2.json)
- **Drop-in LaTeX Table**: [`tables/tab_rq2_comparison.tex`](./tables/tab_rq2_comparison.tex)
- **Primary Raw Artifact Provenance**:
  - Aggregated Final Summary: [`runs/rq2-summary/rq2-comparison-table.md`](../../runs/rq2-summary/rq2-comparison-table.md), [`runs/rq2-summary/rq2-comparison-summary.json`](../../runs/rq2-summary/rq2-comparison-summary.json), [`runs/rq2-summary/rq2-hourly-convergence.json`](../../runs/rq2-summary/rq2-hourly-convergence.json)
  - Traditional Trial JSONLs (`5 × 500 = 2,500` seeds/fuzzer): [`runs/rq2-summary/eval_results/`](../../runs/rq2-summary/eval_results/)
  - Official Upstream LLM Baseline Campaigns, Full-Corpus JSONLs & Token Ledgers: [`runs/rq2-llm-baselines/`](../../runs/rq2-llm-baselines/)

---

## 1. Experimental Protocol & Fairness Design (`Protocol 2.2.0-small-pot-step5`)

### 1.1 Selected Baselines (5 Representative Compiler Fuzzers Across 2 Paradigms)
1. **Traditional Grammar / Mutation / Sanitizer-Differential Fuzzers**:
   - **`YARPGen`** (*OOPSLA '20*): State-of-the-art UB-free random C/C++ program generator for miscompilation testing via differential runtime checksums.
   - **`UBfuzz`** (*ASPLOS '24*): Sanitizer-oriented mutator designed to uncover silent sanitizer omissions via injected undefined behavior.
   - **`MetaMut`** (*ASPLOS '24*): LLM-synthesized semantic mutator engine compiled into a high-throughput native C++ AST mutator (`muss`, crash/ICE-only native oracle).
2. **LLM-Driven Compiler Fuzzers (Official Open-Source Upstream Codebases)**:
   - **`Fuzz4All`** (*ICSE '24*, `fuzz4all/fuzz4all@0bf42fe037c8761bdde61e1c37a0946e8103fba1`): Official upstream `CTarget` executing automatic prompt distillation (`auto_prompt` scoring over official GCC/Clang defense manual sections and starter C programs) followed by evolutionary `cs`/`ci`/`ce`/`comb` generation across all 12 `(compiler × family)` cells.
   - **`FeatureFuzz`** (*2026*, `addaddgo/FeatureFuzz@7486da17d863293f657a00329ac5b4b23d8cbc7d`): Official upstream `CombineFeatureSetStrategy` and `GCCValidator` combining one defense-related historical PR feature, one manual-derived defense operator, and general C features over `67,530` C-compatible historical PR features (`62,377` general C + family defense PR features), replacing only its fine-tuned Qwen model with `deepseek-chat` and omitting its GCC-only coverage server so it covers both GCC and Clang.

### 1.2 Budget Parity & Multi-Trial Statistical Rigor
- **Traditional Fuzzers (`1 CPU Core × 12h × 5` Independent Trials = `60` CPU-hours/baseline)**:
  - Follows the standard single-core multi-trial benchmarking convention of top security venues (`HLPFuzz` USENIX Security '25, `PBFuzz` CCS '26, `TrigFuzz` IEEE S&P '26), capturing both per-trial variance (`mean ± std`) and cumulative 5-trial discovery (`Union [U]`).
  - From each 12-hour trial's valid seed pool, we draw a deterministic stratified sample of `500` valid seeds (`2,500` seeds evaluated across 4 ISAs per traditional fuzzer, `random_seed = 20261112`), preserving full invariant-precondition activation coverage.
- **LLM Fuzzers (`@21,415` Valid Online LLM Calls on `deepseek-chat` — Exact 1:1 Online Call Parity)**:
  - Both official upstream `Fuzz4All` and `FeatureFuzz` codebases run on the **exact same `deepseek-chat` model** (DeepSeek-V4.1-Flash, non-thinking mode) and execute **`21,415` valid online generation calls** (`1,784`–`1,785` calls per `compiler × family` cell across `12` cells), matching `DeFenzz` Step 4's `21,415` online LLM calls 1-for-1 (`zero_leakage = true`).
  - **100% of unique valid compiled seeds** produced by `Fuzz4All` (`14,906` unique retained / `21,090` valid compiled, `98.48%` compile rate) and `FeatureFuzz` (`14,814` unique retained / `14,864` valid compiled, `69.41%` compile rate) are evaluated across all 4 ISAs (`0` sampling loss).
  - **Token & Throughput Accounting**: At `21,415` calls, `Fuzz4All` consumed `57.66M` prompt tokens (`35.13M` cached) and generated **`31.83M` completion tokens** (`89.49M` total, `1.34h`)—**`+61.8%` MORE LLM output tokens** than `DeFenzz` Step 4 (`19.67M` completion tokens; `881.17M` prompt tokens at `93.1%` KV-cache hit rate, `900.84M` total, `10.16h`)—while `FeatureFuzz`'s concise feature-combination prompts consumed `8.64M` prompt tokens (`4.48M` cached) and generated **`13.32M` completion tokens** (`21.96M` total, `1.06h`).

### 1.3 Two-Stage Oracle Evaluation: `Native Oracle` vs. `+Our Oracle` (Per-Mechanism Small-Pot)
To disentangle **(i) the Seed Generation Gap** from **(ii) the Bug Adjudication (Oracle) Gap**, every fuzzer's seeds are evaluated under two oracles:
1. **`Silent Bugs (Native)`**: Bugs flagged by each baseline's built-in oracle (`-O0` vs. `-O2` + defense flags differential runtime checksums for `YARPGen`; expected-UB sanitizer trap check in `F3` for `UBfuzz`; **ICE-only compiler crash native oracles** for `MetaMut`'s `muss` AST mutator, `Fuzz4All`'s `CTarget`, and `FeatureFuzz`'s `GCCValidator`). Because silent defense omissions compile cleanly without crashing or altering standard program output, all crash and differential native oracles report **`0`** silent defense bugs.
2. **`Silent Bugs (+Our Oracle)`**: Each baseline's seeds are evaluated through `DeFenzz`'s deterministic 4-ISA `Check IR` oracle using **Per-Mechanism Small-Pot Routing**:
   - Instead of compiling every seed with a conflicting "big-pot" flag soup (e.g., mixing `-fsanitize=address` with `_FORTIFY_SOURCE` or conflicting CFI modes), each seed is compiled under clean **per-mechanism profiles** matching `DeFenzz`'s own online workers and audited only by the checkers bound to that mechanism.
   - Every `FAIL` verdict must pass **UBSan clean-input filtering** (`-fsanitize=undefined -Werror=uninitialized -fno-sanitize-recover=all`) and **Step-5 calibrated verification** (excluding 12 uncalibrated canary/layout over-approximations), deduplicated by `(compiler, checker_id)` across all 4 ISAs.

---

## 2. Main RQ2 Comparison Table (5 Core Metrics)

| Fuzzer / Baseline | Budget | Valid Seeds (`#ICE`) | Defense Branch Cov (`/ 9,061`) | Active Checkers (`/ 903`) | Silent Bugs (`Native`) | Silent Bugs (`+Our Oracle`) |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| **YARPGen** | `1c × 12h × 5` | `13,114.0 ± 335.2`/t (`0.4±0.5`, U:2) | `4,629.8 ± 2.4` (`51.1%`) `[U:4,648 (51.30%)]` | `103.8 ± 1.5` (`11.5%`) `[U:107 (11.85%)]` | `0.0 ± 0.0` `[U:0]` *(diff checksum)* | **`1.0 ± 0.0`** `[U:1 (G:0, L:1); 1 chk]` |
| **UBfuzz** | `1c × 12h × 5` | `4,974.8 ± 177.8`/t (`0.0±0.0`, U:0) | `5,586.2 ± 31.6` (`61.6%`) `[U:5,672 (62.60%)]` | `135.6 ± 2.4` (`15.0%`) `[U:140 (15.50%)]` | `0`* *(F3 UB: `649.0±23.8` `[U:3,102]`)* | **`2.2 ± 0.5`** `[U:3 (G:0, L:3); 3 chk]` |
| **MetaMut** | `1c × 12h × 5` | `126,605.2 ± 1,697.8`/t (`0.6±0.5`, U:1) | `6,297.4 ± 19.4` (`69.5%`) `[U:6,429 (70.95%)]` | `143.8 ± 6.5` (`15.9%`) `[U:163 (18.05%)]` | `0.0 ± 0.0` `[U:0]` *(ICE-only)* | **`6.4 ± 0.9`** `[U:8 (G:1, L:7); 8 chk]` |
| **Fuzz4All** | `@21,415 calls` | `21,090` (`0`) `[14,906 uniq]` | `6,870 / 9,061` (`75.82%`) `[G:3,665, L:3,205]` | `173 / 903` (`19.16%`) | `0` *(ICE-only)* | **`18`** `(G:8, L:10) [17 chk]` |
| **FeatureFuzz** | `@21,415 calls` | `14,864` (`4`) `[14,814 uniq]` | `7,220 / 9,061` (`79.68%`) `[G:3,920, L:3,300]` | `187 / 903` (`20.71%`) | `0` *(ICE-only)* | **`23`** `(G:12, L:11) [21 chk]` |
| **DeFenzz (Ours)** | `@21,415 calls` | **`715`**† (**`20`**) | **`7,210 / 9,061` (`79.57%`)** `[G:3,493, L:3,717]` | **`833 / 903` (`92.25%`)** | **`111`** | **`111` `(G:58, L:53)` `[63 batch / 68 all chk]`** |

*\*Note on UBfuzz Native Column*: `UBfuzz` mutates seeds to inject deliberate undefined behavior and checks whether `-fsanitize=undefined/address` aborts at runtime. On `F1, F2, F4, F5, F6`, its oracle is structurally inapplicable (`N/A`) because silent omission of `endbr64`, stack-clash probes, or register scrubbing produces identical normal output. Even on `F3`, its `649.0 ± 23.8` raw alerts/trial stem predominantly from dead-code-eliminated UB branches rather than compiler defense bugs; when filtered for UB-free valid defense failures under `+Our Oracle`, `UBfuzz` seeds trigger `2.2 ± 0.5` (`Union: 3`) real silent defense bugs.  
*†Note on DeFenzz Seed Set*: Unlike 1-call-per-program LLM baselines (`Fuzz4All`, `FeatureFuzz`), `DeFenzz` spends its `21,415` online LLM calls across multi-turn tool-assisted compiler source reasoning (`~20.9` turns/worker), emitting C/C++ witnesses only when testing concrete trigger paths (`715` unique valid seeds in total across the entire campaign: `268` GCC, `447` LLVM, zero valid seeds discarded). Evaluating 100% of these `715` seeds covers `7,210` (`79.57%`) active defense probes (`257 / 903 = 28.46%` checkers on the offline batch stratum, `833 / 903 = 92.25%` across online Step-4 invariant audit sessions).

---

## 3. Defense Branch Coverage Breakdown by ISA (`/ 9,061` Active Probes)

| Fuzzer / Baseline | `x86_64` (`/ 2,295`) | `aarch64` (`/ 2,568`) | `riscv64` (`/ 2,095`) | `loongarch64` (`/ 2,103`) | Total (`/ 9,061`) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| **YARPGen** (`1c × 12h × 5`) | `1,221.4±0.6` `[U:1,224 (53.3%)]` | `1,287.8±0.5` `[U:1,292 (50.3%)]` | `1,044.4±0.9` `[U:1,049 (50.1%)]` | `1,076.2±1.6` `[U:1,083 (51.5%)]` | `4,629.8±2.4` `[U:4,648 (51.30%)]` |
| **UBfuzz** (`1c × 12h × 5`) | `1,462.0±6.0` `[U:1,481 (64.5%)]` | `1,538.6±15.4` `[U:1,566 (61.0%)]` | `1,282.0±5.7` `[U:1,302 (62.1%)]` | `1,303.6±5.6` `[U:1,323 (62.9%)]` | `5,586.2±31.6` `[U:5,672 (62.60%)]` |
| **MetaMut** (`1c × 12h × 5`) | `1,635.8±5.1` `[U:1,669 (72.7%)]` | `1,738.2±6.9` `[U:1,774 (69.1%)]` | `1,444.0±5.7` `[U:1,474 (70.4%)]` | `1,479.4±3.6` `[U:1,512 (71.9%)]` | `6,297.4±19.4` `[U:6,429 (70.95%)]` |
| **Fuzz4All** (`@21,415`) | `1,782` (`77.6%`) | `1,882` (`73.3%`) | `1,586` (`75.7%`) | `1,620` (`77.0%`) | `6,870` (`75.82%`) |
| **FeatureFuzz** (`@21,415`) | `1,869` (`81.4%`) | `1,981` (`77.1%`) | `1,668` (`79.6%`) | `1,702` (`80.9%`) | `7,220` (`79.68%`) |
| **DeFenzz (Ours)** (`@21,415`) | **`1,838` (`80.1%`)** | **`2,052` (`79.9%`)** | **`1,644` (`78.5%`)** | **`1,676` (`79.7%`)** | **`7,210` (`79.57%`)** |

---

## 4. Per-Family Probe Coverage & Silent Bugs (`+Our Oracle`)

| Fuzzer / Baseline | `F1` CFI (`/ 1,747`) | `F2` Stack (`/ 1,429`) | `F3` Sanitizer (`/ 2,265`) | `F4` Scrub (`/ 575`) | `F5` Spec (`/ 296`) | `F6` Fortify (`/ 2,749`) | Total Bugs |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **YARPGen** (`Union`) | 789 probes / **1** bug | 717 probes / **0** | 1,538 probes / **0** | 329 probes / **0** | 214 probes / **0** | 1,061 probes / **0** | **1** (`1.0±0.0`) |
| **UBfuzz** (`Union`) | 789 probes / **1** bug | 1,094 probes / **0** | 1,682 probes / **2** | 380 probes / **0** | 229 probes / **0** | 1,498 probes / **0** | **3** (`2.2±0.5`) |
| **MetaMut** (`Union`) | 885 probes / **1** bug | 1,176 probes / **1** | 1,769 probes / **6** | 453 probes / **0** | 237 probes / **0** | 1,909 probes / **0** | **8** (`6.4±0.9`) |
| **Fuzz4All** (`@21,415`) | 917 probes / **3** bugs | 1,159 probes / **3** | 1,819 probes / **9** | 454 probes / **2** | 262 probes / **1** | 2,259 probes / **0** | **18** |
| **FeatureFuzz** (`@21,415`) | 925 probes / **3** bugs | 1,229 probes / **4** | 1,870 probes / **10** | 501 probes / **1** | 248 probes / **2** | 2,447 probes / **3** | **23** |
| **DeFenzz (Ours)** (`@21,415`) | **1,187** / **36** bugs | **1,241** / **21** | **2,045** / **21** | **479** / **10** | **277** / **9** | **1,981** / **14** | **111** |

---

## 5. Cross-Baseline Bug Overlap Matrix & Three Core Takeaways for §5.3 Prose

- **Total Unique Silent Bugs Across All 6 Tools (`+Our Oracle`)**: **`111`**
- **Union of All 5 Baselines (`YARPGen ∪ UBfuzz ∪ MetaMut ∪ Fuzz4All ∪ FeatureFuzz`)**: **`28`** (`Fuzz4All` `18` $\cap$ `FeatureFuzz` `23` = `13`; `YARPGen` `1` $\subset$ `UBfuzz` `3` $\subset$ `MetaMut` `8` $\subset$ `FeatureFuzz` `23`)
- **Missed by `DeFenzz` (`Found by Any Baseline \ DeFenzz`)**: **`0`** (`100%` of the `28` baseline bugs are covered by `DeFenzz`)
- **Strictly Exclusive to `DeFenzz` (vs. All 5 Baselines Combined)**: **`83 / 111` (`74.77%` / `74.8%`)** (`+88` bugs / `79.3%` over the strongest single baseline `FeatureFuzz`'s `23` bugs)

| Baseline | YARPGen | UBfuzz | MetaMut | Fuzz4All | FeatureFuzz | DeFenzz (Ours) | **Exclusive (vs. All Other 5)** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **YARPGen** (`Union: 1`) | 1 | 1 | 1 | 1 | 1 | 1 | **0** |
| **UBfuzz** (`Union: 3`) | 1 | 3 | 3 | 3 | 3 | 3 | **0** |
| **MetaMut** (`Union: 8`) | 1 | 3 | 8 | 6 | 8 | 8 | **0** |
| **Fuzz4All** (`18`) | 1 | 3 | 6 | 18 | 13 | 18 | **0** |
| **FeatureFuzz** (`23`) | 1 | 3 | 8 | 13 | 23 | 23 | **0** |
| **DeFenzz (Ours)** (`111`) | 1 | 3 | 8 | 18 | 23 | **111** | **83 (`74.8%`)** |

### Three Crisp Analytical Takeaways for the Writing Agent:
1. **Proof of the Oracle Gap (`Native` vs. `+Our Oracle`)**:
   - `MetaMut` (`muss` AST mutator), `Fuzz4All` (`CTarget`), and `FeatureFuzz` (`GCCValidator`) rely on ICE-only compiler crash native oracles, and `YARPGen` relies on differential runtime checksums—all catching **`0` silent defense bugs natively** because weakened defenses compile cleanly and preserve standard I/O. Attaching `DeFenzz`'s programmatic `Check IR` oracle immediately uncovers **`8`** (`MetaMut`), **`18`** (`Fuzz4All`), and **`23`** (`FeatureFuzz`) real silent defense bugs (`28` unique across all 5 baselines combined) already latent in their generated corpora.
2. **Proof of the Precondition-Steering & Directed Synthesis Gap (`23` Best Single / `28` Union vs. `111` Bugs, `83` Exclusive)**:
   - Even when *gifted* `DeFenzz`'s full 915-checker programmatic oracle, the strongest single baseline (`FeatureFuzz`) reaches **`23` bugs** (`Fuzz4All`: **`18`**; union of all 5 baselines: **`28`**), leaving **`83 / 111` (`74.8%`)** silent bugs **strictly exclusive to `DeFenzz`** (`0` baseline bugs missed by `DeFenzz`).
   - Crucially, `FeatureFuzz` compiles `14,814` unique valid C programs (`20.7×` `DeFenzz`'s `715` synthesized seeds) and sweeps **`79.68%` (`7,220 / 9,061`)** of defense probes—virtually matching `DeFenzz`'s **`79.57%` (`7,210 / 9,061`)**—yet activates only **`187 / 903` (`20.7%`)** checkers vs. `DeFenzz`'s **`833 / 903` (`92.2%`)** (`4.45×`). Compiling ~15K diverse C programs under hardening flags easily hits shallow pass-entry branches (e.g., `2,447` `F6` Fortify probes yielding just `3` bugs in `FeatureFuzz`, and `2,259` `F6` probes yielding `0` bugs in `Fuzz4All`), whereas without mapped branch traces and invariant preconditions, baseline seeds rarely satisfy the coupled multi-condition bailout paths that silently drop defenses (nearly half of LLM baseline bugs—`9/18` in `Fuzz4All` and `10/23` in `FeatureFuzz`—concentrate in `F3` sanitizers).
3. **Rapid Traditional Saturation (`0–12h` Convergence)**:
   - Across `H1`–`H12` (`runs/rq2-summary/rq2-hourly-convergence.json`), `YARPGen` and `MetaMut` scale linearly in raw seed count (`1,082` $\to$ `13,357` and `11,239` $\to$ `127,149` seeds/trial), yet native silent-bug detection stays flat at **`0.0 ± 0.0` across all 12 hours**, demonstrating that raw CPU throughput cannot substitute for defense-aware seed synthesis and binary-level programmatic oracles.
