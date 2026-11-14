# DeFenzz Paper (`IEEE S&P` Submission)

This repository contains the manuscript, bibliography, figures, build assets, and verified evaluation data package for the **DeFenzz** paper. The review manuscript uses the IEEE conference format and keeps author information anonymous.

## Authoritative Evaluation Data for Writing Agents (`Start Here`)

All cleaned, reconciled, and machine-verified experimental results, JSON summaries, and ready-to-paste IEEE `booktabs` LaTeX tables are located in **[`evaluation_data/`](./evaluation_data/README.md)** (mirrored from `/Users/bytedance/projects/research/defenzz/main/docs/evaluation/`):

- **[`evaluation_data/README.md`](./evaluation_data/README.md)** — Master headline cheat-sheet & 8 anti-pitfall consistency rules
- **[`evaluation_data/01-main-experiment-rq1.md`](./evaluation_data/01-main-experiment-rq1.md)** — Main Experiment (RQ1: `111` silent bugs, `30` confirmed, `11` fixed; unified `F1`–`F6` taxonomy) + Offline Invariant/Check-IR Funnel (`921` invariants $\to$ `915` checkers)
- **[`evaluation_data/02-baseline-comparison-rq2.md`](./evaluation_data/02-baseline-comparison-rq2.md)** — Baseline Comparison (RQ2: `YARPGen`, `UBfuzz`, `MetaMut` at `1c × 12h × 5`; `FeatureFuzz`, `Fuzz4All` at `@21,415 calls`; Per-Mechanism Small-Pot evaluation)
- **[`evaluation_data/03-ablation-study-rq3.md`](./evaluation_data/03-ablation-study-rq3.md)** — Component Ablation Study (RQ3: Full 921-invariant campaign `w/o Check IR` & `w/o Hybrid RAG` + Controlled 41-invariant audit lane `w/o Source Mapping`, `w/o Programmatic Oracle`, `Bare Agent`)
- **[`evaluation_data/04-overhead-and-telemetry-rq4.md`](./evaluation_data/04-overhead-and-telemetry-rq4.md)** — Token Cost, KV-Cache (`92.4%`), Tool-Call Telemetry (`99,236` calls), & Clean Compiler Build Benchmark (`compiler-benchmark-20261101/`)
- **[`evaluation_data/tables/`](./evaluation_data/tables/)** — Drop-in `.tex` tables (`tab_rq1_bugs.tex`, `tab_offline_funnel.tex`, `tab_rq2_comparison.tex`, `tab_rq3_ablation.tex`, `tab_rq4_overhead.tex`)
- **[`evaluation_data/data/`](./evaluation_data/data/)** — Machine-verified JSON summaries (`01_main_rq1.json` .. `04_overhead_rq4.json`)

## Build

Install [Tectonic](https://tectonic-typesetting.github.io/) and run:

```sh
make
```

The generated review manuscript is `main.pdf`. Use `make verify` to rebuild it and display its PDF metadata.

## Critical Technical Ground-Truth Rules (Must Read Before Editing Prose)

See **[`AGENTS.md`](./AGENTS.md)** for full writing constraints. In particular, for Step 3 (`Check IR` & Programmatic Oracles):
- **`Check IR` Primitives + LLM Composition (NOT `Predicate IR` Lowering)**: `Check IR` ($\Omega$) formalizes low-level binary-inspection and runtime-execution query primitives alongside target ISA specifications ($\mathcal{T}_i$). **The LLM writes high-level check logic to combine these `Check IR` primitives and ISA parameters into a checker**—we do *not* encode an entire invariant into a single rigid `predicate IR` expression for mechanical lowering.
- **Static OR Dynamic (`二选一`)**: Each invariant checker is **either** static **or** dynamic ($\mu \in \{\mathsf{Static}, \mathsf{Dynamic}\}$); never claim "dual static-dynamic cross-checking".
- **No Differential Testing for Bug Finding**: Online fuzzing runs deterministic checkers directly on **each compiled seed**, rather than using differential baseline builds to find bugs or relying on an LLM to judge whether silent defense bugs occur.

## Repository Layout

- `AGENTS.md`: Mandatory technical ground-truth and writing rules for AI agents
- `main.tex`: LaTeX manuscript source (check `outline_status.md` for locked `[ready]` sections before editing!)
- `evaluation_data/`: Authoritative cleaned evaluation handbook, JSON data, and LaTeX tables
- `step3_formal_design_option_a.md`: Historical early-stage brainstorm (**superseded** by `main.tex` §III-C; do NOT copy `Predicate IR` or `Z3` claims from this file)
- `compiler-benchmark-20261101/`: Clean hardware build-time benchmark for GCC 16.2.0 and Clang 23.1
- `refs.bib`: BibTeX bibliography
- `figures/`: Publication PDFs, SVG previews, and Python/D2 sources (`figures/src/generate_eval_figures.py`)
- `outline_status.md`: Section-by-section `[ready]` / `[不 ready]` lock tracker
