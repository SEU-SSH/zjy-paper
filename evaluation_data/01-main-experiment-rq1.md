# 01 — Main Experiment (RQ1) & Offline Oracle Construction Funnel

- **Machine-Readable Data**: [`data/01_main_rq1.json`](./data/01_main_rq1.json)
- **Drop-in LaTeX Tables**: [`tables/tab_rq1_bugs.tex`](./tables/tab_rq1_bugs.tex), [`tables/tab_offline_funnel.tex`](./tables/tab_offline_funnel.tex)
- **Primary Raw Artifact Provenance**:
  - Bug Ledger & Upstream Links: [`docs/bugs/metadata.json`](/Users/bytedance/projects/research/defenzz/main/docs/bugs/metadata.json), [`docs/bugs/README.md`](/Users/bytedance/projects/research/defenzz/main/docs/bugs/README.md)
  - 4-ISA Denominator & 111-Bug Family Manifest: [`runs/rq2-eval-config.json`](/Users/bytedance/projects/research/defenzz/main/runs/rq2-eval-config.json)
  - Frontier Stage Outputs: [`runs/gcc16-multi-isa-frontier/`](/Users/bytedance/projects/research/defenzz/main/runs/gcc16-multi-isa-frontier/), [`runs/llvm23-multi-isa-frontier/`](/Users/bytedance/projects/research/defenzz/main/runs/llvm23-multi-isa-frontier/)
  - Existing Paper Figure: `/Users/bytedance/projects/research/defenzz-paper/figures/eval-bug-char.pdf`

---

## 1. Ledger Reconciliation: Why Exactly `111` Silent Defense Bugs (`58` GCC + `53` LLVM)

`docs/bugs/metadata.json` tracks **`131` active candidate entries** (`75` GCC + `54` LLVM + `2` `compiler-rt`, where `compiler-rt` is grouped under the LLVM toolchain column in `docs/bugs/README.md` to give `75 + 56 = 131`).

Following strict scientific bug-reporting hygiene, **`20` non-bug / unverified entries are excluded** from paper bug claims:
1. **`3` False Positives / Intentional Compiler Design** (`DF-G-021` RISC-V Zicfilp direct GOT call exemption, `DF-G-042` withdrawn analyzer callback cast, `DF-G-079` C typedef identifier shadowing `PR 128596`).
2. **`8` Suspended Pre-Filing Candidates (`needs-review`)** (`DF-G-061, 068, 071, 072, 074, 075, 077, 080` — e.g., invalid `-fgimple` SSA input, `naked` function mixing non-basic-asm C outside GCC's documented contract, or already covered by an existing upstream ticket `PR 128072`).
3. **`7` Disputed Language / UB Boundary Reports (`disputed`)** (`5` GCC + `2` LLVM/compiler-rt — e.g., C++ non-standard flexible array extensions in `PR 127311`, internal-only `__builtin_eh_return` in `PR 127322`).
4. **`2` Independently Patched Upstream Before Filing (`independently-fixed`)** (`1` GCC `DF-G-005` / `PR 109267`, `1` LLVM).

Subtracting `131 - 20 = 111` yields **`111` previously unknown, PoC-reproducible silent defense bugs**:
- **By Toolchain**: **`58` in GCC** (`16.2.0` & `17.0` trunk) and **`53` in LLVM/Clang** (`52` LLVM core + `1` `compiler-rt`, `23.1.2` & trunk).
- **By Upstream Maintainer Status** (as of `2026-11-11`):
  - **`30` Officially Confirmed by Maintainers (`18` GCC + `12` LLVM)**:
    - **`11` Fixed in Mainline**: `9` GCC + `2` LLVM;
    - **`1` Partially Fixed**: `1` GCC (`DF-G-001`, LoongArch `PR 125049` merged; MIPS64 `PR 125077` pending);
    - **`18` Confirmed Open (`NEW` / `ASSIGNED` / `confirmed` label)**: `8` GCC + `10` LLVM.
  - **`+5` Substantively Confirmed via Bug-Validity Tags** (`3` GCC `wrong-code` + `2` LLVM `miscompilation` tags applied by maintainers without toggling the status dropdown; i.e., `35` corroborated upstream in total).
  - **`76` Awaiting Maintainer Triage (`pending`)**: `37` GCC + `39` LLVM/compiler-rt (all filed with minimal C/C++ reproducers and assembly/runtime diffs).

---

## 2. Unified Six-Family Breakdown (`F1`–`F6`) — Recommended for Table 1

> **Alignment Note for Writing Agent**: Adopting this table (provided as [`tables/tab_rq1_bugs.tex`](./tables/tab_rq1_bugs.tex)) makes RQ1 Table 1 and RQ2's per-family evaluation 100% consistent across all six defense families (`F1`–`F6`), all `915` checkers (`473` GCC + `442` LLVM), all `9,061` active 4-ISA probes, and all `111` bugs (`58` GCC + `53` LLVM).

| ID | Defense Family | Checkers (GCC / LLVM / Total) | Active 4-ISA Checkers | Active 4-ISA Probes (GCC / LLVM / Total) | Silent Bugs (GCC / LLVM / **Total**) | Official Conf. (G / L / **Tot**) | Fixed (G / L / **Tot**) | Representative Upstream Bug IDs |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`F1`** | **Control-Flow Integrity** (IBT, SHSTK, BTI, PAC, GCS, Zicfilp/Zicfiss, KCFI, VTV) | 52 / 171 / **223** | 220 | 271 / 1,476 / **1,747** | 14 / 22 / **36** | 6 / 7 / **13** | 4 / 1 / **5** | GCC PR 125084, 128011, 128015, 128360, 128373; LLVM #208751 |
| **`F2`** | **Stack Protection** (SSP, SafeStack, ShadowCallStack, Stack-Clash) | 117 / 56 / **173** | 170 | 754 / 675 / **1,429** | 10 / 11 / **21** | 3 / 3 / **6** *(+2 subst)* | 2 / 1 / **3** | GCC PR 125049, 127318, 128036, 128271, 128273; LLVM #237864, #236674 |
| **`F3`** | **Memory Sanitizers** (ASan, HWASan, MTE, UBSan, MemTag-Stack) | 66 / 128 / **194** | 191 | 756 / 1,509 / **2,265** | 9 / 12 / **21** | 3 / 1 / **4** | 1 / 0 / **1** | GCC PR 128276, 128280, 128282, 128592; LLVM #237909 |
| **`F4`** | **State Scrubbing** (`zero-call-used-regs`, `strub`, `trivial-auto-var-init`, DSE volatile scrub) | 66 / 2 / **68** | 68 | 523 / 52 / **575** | 8 / 2 / **10** | 3 / 0 / **3** *(+2 subst)* | 0 / 0 / **0** | GCC PR 128287, 128363, 128575; LLVM #236795, #236796 |
| **`F5`** | **Speculation Hardening** (SLH, SLS, Retpoline, Indirect-Thunk, Harden-Compares) | 17 / 48 / **65** | 64 | 47 / 249 / **296** | 4 / 5 / **9** | 1 / 1 / **2** | 1 / 0 / **1** | GCC PR 128364, 128367, 128388; LLVM #240257 |
| **`F6`** | **Bounds & Fortification** (`_FORTIFY_SOURCE`, `counted_by`, `nonstring`, Analyzer Attrs) | 155 / 37 / **192** | 190 | 2,186 / 563 / **2,749** | 13 / 1 / **14** | 2 / 0 / **2** *(+1 subst)* | 1 / 0 / **1** | GCC PR 125079, 127333, 128274, 128591 |
| **Total** | **All Six Defense Families (`4` ISAs)** | **473 / 442 / 915** | **470 / 433 / 903** | **4,537 / 4,524 / 9,061** | **58 / 53 / 111** | **18 / 12 / 30** *(+5 subst)* | **9 / 2 / 11** | **100% PoC-Verified Silent Failures** |

*(Note: If keeping the legacy 6-row grouping currently in `main.tex` lines 468–475 where `Scrubbing & Speculation` are merged (`20`) and `Call, Link & Enclave` (`5`, e.g., SGX `PR 128015`, `PR 128283`, `noplt` `PR 128577`) is a separate row, see `legacy_main_tex_table1_crosswalk` in [`data/01_main_rq1.json`](./data/01_main_rq1.json)—both sum to the exact same `915` checkers, `58 + 53 = 111` bugs, `30` confirmed, and `11` fixed.)*

---

## 3. Multi-Dimensional Bug Characterization (Matches `figures/eval-bug-char.pdf` 100%)

### 3.1 By Compiler Pipeline Stage (`Sum = 111`)
| Pipeline Stage | Bug Count | Share | Key Technical Insight |
| :--- | :---: | :---: | :--- |
| **Backend / CodeGen** | **54** | **48.6%** | Epilogue expansion, prolog stack-clash probing, target machine-instruction lowering, register allocation spills |
| **Middle-End / GIMPLE / IR** | **25** | **22.5%** | Early constant folding (`fold_const_call`), DSE deleting `volatile` scrubs, inliner dropping sanitizer/protection attrs |
| **Frontend / Attributes** | **12** | **10.8%** | Mutual-exclusion silent attribute drops (`cf_check` + `nocf_check`, `no_sanitize_*` merge), `transparent_union` qualifier loss |
| **Driver / Option Handling** | **10** | **9.0%** | Negative flag bitmask clearing bugs (`-fno-sanitize=kernel-hwaddress` wiping user HWASan; `-fcf-protection=none` leaving `__CET__=8`) |
| **LTO / IPA** | **7** | **6.3%** | LTO bytecode streaming stripping HWASan/MTE scope markers (`PR 128276`) or dropping `-fzero-call-used-regs` (`PR 128287`) |
| **Runtime (`libgcc` / `compiler-rt`)** | **3** | **2.7%** | Missing `.note.GNU-stack` markers (`LLVM #220866`) and runtime guard initialization mismatches |

### 3.2 By Security Impact Severity (`Sum = 111`)
- **High (`50`, `45.0%`)**: Complete silent omission or runtime bypass of an enabled exploit mitigation (e.g., missing `endbr64`/`bti`/`lpad` landing pad, unprobed stack-clash page skip, stripped HWASan/ASan memory checks, dead-store-eliminated `volatile` secret wipe, dead-code-eliminated CET shadow-stack verification).
- **Medium (`39`, `35.1%`)**: Partial weakening, secret/canary register leakage across return boundaries, or ABI/unwind corruption under active hardening (`PR 125049`, `PR 128273`).
- **Low (`22`, `19.8%`)**: Silent diagnostic suppression on security annotations (`-Wstringop-overread`, `-fanalyzer`) or defense-flag corner-case ICEs.

### 3.3 By Target ISA Exclusivity (`Sum = 111`)
- **Cross-ISA (`3+` ISAs or ISA-independent middle-end/LTO)**: **`47` (`42.3%`)**
- **Non-x86 Only (`AArch64`, `RISC-V64`, or `LoongArch64` exclusively — invisible to x86-only fuzzers)**: **`35` (`31.5%`)**
- **`x86-64` Only**: **`22` (`19.8%`)**
- **Dual-ISA (`x86-64` + 1 Non-x86 ISA)**: **`7` (`6.3%`)**
- **Per-ISA Total Affected Bugs (including generic/multi-ISA bugs, do not sum across columns)**:
  - Within the `111` bugs: `x86-64` **`81`** (`56` explicit + `25` generic), `AArch64` **`78`** (`53` + `25`), `RISC-V64` **`61`** (`36` + `25`), `LoongArch64` **`46`** (`21` + `25`).

---

## 4. Offline Invariant Extraction, Source Mapping & Check-IR Oracle Funnel

| Funnel Stage | GCC `16.2.0` | LLVM `23.1.2` | Combined Total | Notes |
| :--- | :---: | :---: | :---: | :--- |
| **1. Documentation & Source Slices** | 312 | 268 | **580** | Official manuals, ISA specs, option tables, pass headers |
| **2a. Accepted Invariants (Segmented CoT)** | 463 | 441 | **904** | Passed all 3 Grounding Gates |
| **2b. Accepted Invariants (Hybrid RAG Transfer)** | +12 | +5 | **+17** | Net non-duplicate cross-mechanism transfers (e.g., x86 IBT $\to$ RV64 Zicfilp) |
| **2. Total Accepted Security Invariants ($\Phi$)** | **475** | **446** | **921** | Zero hallucinated flags |
| **3. Mapped Compiler Decision Paths** | 1,669 | 1,253 | **2,922** | Across **747** distinct files (`412` GCC + `335` LLVM) |
| **4. Active 4-ISA Compile-Time Branch Probes** | 4,537 | 4,524 | **9,061** | `x86_64`: 2,295 \| `aarch64`: 2,568 \| `riscv64`: 2,095 \| `loongarch64`: 2,103 |
| **5a. Check-IR 1st-Attempt Validation Rate** | 83.4% (`396/475`) | 81.2% (`362/446`) | **82.3%** (`758/921`) | Passed Gate A (Type/ISA), Gate B (Z3 SMT), Gate C (Differential Build) on try 1 |
| **5b. Final Validated Checkers ($\le 5$ Repairs)** | **473** (`99.6%`) | **442** (`99.1%`) | **915** (`99.3%`) | `6` invariants (`2` GCC, `4` LLVM) excluded due to unsupported kernel-only environments |
| **5c. Active 4-ISA Linux ELF Batch Checkers** | **470** | **433** | **903** | Excludes `12` (`3` GCC, `9` LLVM) non-4-ISA / Windows-SEH `NA` checkers |

---

## 5. High-Impact Case Studies Ready for Manuscript Prose

1. **Motivation Anchor (`DF-G-002` / `GCC PR 125079`, Fixed — already locked in §2)**: `gimple-fold.cc` rewrites `strcat_chk(dst, src, bos)` into `memcpy_chk(dst + len, src, slen + 1, bos)` without subtracting `len` from `bos`, leaving an $O(\text{len})$ heap/stack fortification overflow window despite `-D_FORTIFY_SOURCE=2 -O2`.
2. **Case Study 1 — Optimizer Deleting Hardware Shadow-Stack Verification (`DF-G-025` / `GCC PR 128271`, Fixed)**: Under `-fcf-protection=return -mshstk -O2`, GCC's x86 RTL templates for CET shadow-stack intrinsics (`rdsspd`/`rdsspq`, `incsspd`/`incsspq`) omitted `CC_REG` clobber and volatile memory side-effect annotations, allowing RTL CSE/DCE to merge or delete shadow-stack pointer checks while compilation exited `0`. Caught by static Check-IR `CountInsn` / side-effect checker.
3. **Case Study 2 — Cross-ISA SafeStack + SVE Spill Escape (`DF-L-023` / `LLVM #237864`, Confirmed)**: On `AArch64` with `-fsanitize=safe-stack -march=armv8.2-a+sve -O2`, `SafeStack` moved fixed address-taken arrays to the unsafe stack (`__safestack_unsafe_stack_ptr`), but `AArch64FrameLowering` spilled scalable SVE predicate/vector registers onto the **safe stack** adjacent to the return-address link register (`x30`) without bounds isolation. Caught exclusively on `AArch64` by Check-IR frame-offset directional relation.
4. **Case Study 3 — Non-x86 RISC-V Zicfilp Hot-Patch Landing-Pad Inversion (`DF-G-023` / `GCC PR 128011`, Confirmed)** & **LoongArch Stack-Clash Unprobed Residual (`DF-G-015` / `GCC PR 128036`, Confirmed)**: On `RISC-V64` with `-fcf-protection=branch -march=rv64gc_zicfilp` + `-fpatchable-function-entry=2`, GCC emitted `nop` padding *before* `lpad`, causing indirect calls `jalr` to fault or bypass landing-pad label matching at function entry (`offset 0`). On `LoongArch64`, `-fstack-clash-protection` failed to probe final residual frame allocations, permitting guard-page skip.
