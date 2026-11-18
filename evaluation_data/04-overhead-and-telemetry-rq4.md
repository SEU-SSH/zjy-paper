# 04 — System Telemetry, Token Cost & Toolchain Overhead (RQ4)

- **Machine-Readable Data**: [`data/04_overhead_rq4.json`](./data/04_overhead_rq4.json)
- **Drop-in LaTeX Table**: [`tables/tab_rq4_overhead.tex`](./tables/tab_rq4_overhead.tex)
- **Primary Raw Artifact Provenance**:
  - Frontier Usage Summaries: [`runs/gcc16-multi-isa-frontier/`](/Users/bytedance/projects/research/defenzz/main/runs/gcc16-multi-isa-frontier/), [`runs/llvm23-multi-isa-frontier/`](/Users/bytedance/projects/research/defenzz/main/runs/llvm23-multi-isa-frontier/)
  - Session Tool-Call Telemetry & Figure: `/Users/bytedance/projects/research/defenzz-paper/figures/src/generate_eval_figures.py` (lines 297–367), `/Users/bytedance/projects/research/defenzz-paper/figures/eval-tool-calls.pdf`
  - Clean Hardware Compiler Build Benchmark: `/Users/bytedance/projects/research/defenzz-paper/compiler-benchmark-20261101/report.md`

---

## 1. End-to-End LLM Call, Token & Wall-Clock Accounting (`GCC 16.2` + `LLVM 23.1`)

All LLM stages run with 8 concurrent workers on `deepseek-chat` with prefix KV-caching enabled across shared compiler source slices and system schemas:

| Pipeline Stage | Execution Scope | LLM Calls | Cached Input (`M` tok) | Uncached Input (`M` tok) | Output (`M` tok) | Total (`M` tok) | KV-Cache Hit Rate | Wall-Clock (`h`) |
| :--- | :---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Step 1: Invariant Extraction** | Offline (1-Time) | 1,160 | 18.20 | 9.45 | 3.15 | **30.80** | 65.8% | **1.70** |
| **Step 2: MCP Source Mapping** | Offline (1-Time) | 35,976 | 556.82 | 49.64 | 17.10 | **623.56** | 91.8% | **29.50** |
| **Step 3: Check IR Synthesis** | Offline (1-Time) | 1,120 | 46.41 | 5.23 | 3.17 | **54.81** | 89.9% | **3.32** |
| *Offline Subtotal (Reusable per Release)* | *Offline* | *38,256* | *621.43* | *64.32* | *23.42* | ***709.17*** | *90.6%* | ***34.52*** |
| **Step 4: Directed Fuzzing (4 ISAs)** | Online Campaign | 21,415 | 824.12 | 57.05 | 19.67 | **900.84** | 93.5% | **10.16** |
| **Grand Total (`GCC 16` + `LLVM 23`)** | **End-to-End** | **59,671** | **1,445.55** | **121.37** | **43.09** | **1,610.01** | **92.4%** | **44.68** |

### Key Cost & Efficiency Highlights for §5.5 Prose:
1. **High KV-Cache Efficiency (`92.4%` Overall)**: Because `DeFenzz` pins immutable compiler pass slices and `Check IR` primitive schemas in the prompt prefix while appending compact delta blackboard telemetry, **`1,445.55M` out of `1,566.92M` prompt tokens (`92.4%`) hit the provider's prefix KV-cache** (billed at ~$0.1\times$ uncached input rate).
2. **Offline Amortization**: Steps 1–3 (`34.52h`, `709.17M` tokens) execute **once per major compiler release** to produce the reusable `915`-checker oracle suite and `9,061`-probe instrumented compilers.
3. **Per-Bug Online Efficiency**: Across the `10.16h` online Step-4 campaign (`21,415` calls, `900.84M` tokens), discovering **`111` silent defense bugs** amortizes to **`5.49` minutes (`5.5 min`)**, **`192.9` LLM calls**, and **`8.12M` tokens (`0.18M` output tokens)** per bug.

---

## 2. Agent Tool-Invocation Telemetry (`99,236` Tool Calls Across `6,798` Sessions)

Matches `/Users/bytedance/projects/research/defenzz-paper/figures/eval-tool-calls.pdf` 100%:

| Stage & Toolchain | Call-Graph MCP | Lexical `grep` | File Slice `read` | Spec/Code `write/edit` | Workspace / Exec | Total Tool Calls | Sessions | Avg Calls / Session |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Source Map (`GCC 16`)** | 9,529 (`18.0%`) | 17,322 (`32.7%`) | 12,292 (`23.2%`) | 0 (`0%`) | 13,810 (`26.1%`) | **52,953** | 3,677 | **14.4** |
| **Source Map (`LLVM 23`)** | 9 (`0.1%`) | 3,421 (`54.8%`) | 2,606 (`41.7%`) | 0 (`0%`) | 208 (`3.3%`) | **6,244** | 568 | **11.0** |
| **Check IR Synth (`GCC 16`)** | 0 (`0%`) | 101 (`12.5%`) | 90 (`11.1%`) | 607 (`75.1%`) | 10 (`1.2%`) | **808** | 558 | **1.4** |
| **Check IR Synth (`LLVM 23`)** | 0 (`0%`) | 155 (`17.8%`) | 91 (`10.4%`) | 609 (`69.8%`) | 17 (`1.9%`) | **872** | 562 | **1.6** |
| **Fuzz Audit (`GCC 16`)** | 1,498 (`6.3%`) | 10,757 (`45.0%`) | 10,261 (`42.9%`) | 0 (`0%`) | 1,408 (`5.9%`) | **23,924** | 860 | **27.8** |
| **Fuzz Audit (`LLVM 23`)** | 1,077 (`7.5%`) | 7,317 (`50.7%`) | 5,272 (`36.5%`) | 0 (`0%`) | 769 (`5.3%`) | **14,435** | 573 | **25.2** |
| **`Full DeFenzz` Total** | **12,113** | **39,073** | **30,612** | **1,216** | **16,222** | **99,236** | **6,798** | **14.6** |
| *Ablation: `w/o Check IR` (Step 3)* | *0 (`0%`)* | *4,606 (`24.9%`)* | *7,961 (`43.0%`)* | *4,447 (`24.0%`)* | *1,481 (`8.0%`)* | ***18,495*** | *1,229* | ***15.0*** |

- **Why `Check IR` Is So Compact**: In Step 3, `Check IR` sessions average only **`1.4–1.6` tool calls/session** (`1,680` total calls across GCC+LLVM), whereas raw Go checker authoring (`w/o Check IR`) explodes to **`15.0` calls/session (`18,495` calls, `11.0×` higher)** as the agent repeatedly reads Go helper files and edits broken disassembly parsers.

---

## 3. Toolchain Build-Time & Compile/Runtime Overhead Benchmark

Measured cleanly from scratch (`ccache` disabled, RAM-backed build dir, Ninja + LLD `-j16`) on a **16-vCPU ARM Neoverse-N2 server (`62 GiB` RAM, NVMe SSD, Linux `5.15`)** (`/Users/bytedance/projects/research/defenzz-paper/compiler-benchmark-20261101/report.md`):

| Toolchain & Configuration | Frozen Commit | Targets Built | Clean Build Wall-Clock | User CPU Time | Deterministic Probe Injection Pass | Per-Seed Compile Overhead | Emitted Binary Runtime Overhead |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **GCC `16.2.0`** (`c,c++`, `--disable-bootstrap`) | `78d4ac73dd39` | Cross-ISA (`x86_64`, `aarch64`, `riscv64`, `loongarch64`) | **`4m 37.1s`** (`277.08s`) | `21,796.7s` | `21m 27.6s` (`1,287.6s` across 4-ISA pass set) | **`< 2.0%`** | **`0.0%`** |
| **LLVM/Clang `23.1.2`** (`Release`, `4,562` Ninja actions) | `85ac56026243` | `X86;AArch64;RISCV;LoongArch` (unified multi-target binary) | **`25m 50.8s`** (`1,550.83s`) | `18,950.4s` | `27m 25.4s` (`1,645.4s` across 4-ISA pass set) | **`< 2.0%`** | **`0.0%`** |

- **Zero Target-Binary Runtime Overhead (`0.0%`)**: Crucially, `DEFENZZ_LOG` instruments *host compiler decision branches* (logging pass/branch trace IDs during compilation) and injects **zero instructions** into the generated target ELF binaries. Thus, target binaries execute in QEMU/hardware at native speed with zero perturbation to stack layouts, register allocation, or instruction offsets audited by `Check IR`.
