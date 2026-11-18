# DeFenzz Paper — Agent Writing & Technical Ground-Truth Rules

## 1. Writing Skill & Locked Sections
- Always load and follow the **`plain-paper-writing`** skill when drafting or revising manuscript prose (plain vocabulary, 15–25 words per sentence, strict design-vs-implementation separation outside `Section IV Implementation`, and sentence-split `diff` + word-level track-changes on delivery).
- Check [`outline_status.md`](./outline_status.md) and [`mat_comments_list.md`](./mat_comments_list.md) before editing `main.tex`: never modify sections marked `[ready]` unless explicitly instructed by the user.
- **Current Locked Boundary (`L1–L182` `[ready]`)**: **`Title`, `Abstract`, `Section I (Introduction)`, and `Section II (Motivation)` (`main.tex` `L1–L182`) have completed all revisions per Mat's Round 1 & Round 2 comments (`[R1-1]`–`[R1-11]`, `[R2-1]`–`[R2-10]`) and are strictly LOCKED.** Focus subsequent Mat-comment revisions (`[R2-11]`–`[R2-15]`) on `Section III (Design)` onward (`L183+`).
- Use [`evaluation_data/README.md`](./evaluation_data/README.md) as the single source of truth for experimental numbers.

## 2. Step 3 (`Check IR` & Programmatic Oracles) Ground-Truth Architecture
**CRITICAL — Never confuse our actual `Check IR` design (`main.tex` §III-C) with superseded early brainstorms (`step3_formal_design_option_a.md`):**

1. **`Check IR` is a library of formalized query primitives, NOT a rigid `predicate IR` formula mechanically lowered into a checker**:
   - `DeFenzz` formalizes low-level static (compiler dump / assembly / ELF inspection) and dynamic (sandbox execution) query primitives in **`Check IR`** ($\Omega$), paired with explicit **target ISA specifications** ($\mathcal{T}_i$: stack growth direction, registers, calling conventions, CFI landing-pad bytes, alignment).
   - Rather than encoding an entire invariant as a single rigid `predicate IR` expression and mechanically lowering it, **the LLM writes high-level checking logic (loops, conditionals, cross-site correlations) to combine `Check IR` primitives and target ISA specifications into an executable checker**.
   - *Do NOT cite `predicate IR`, `Z3 SMT solving`, or mechanical lowering from `step3_formal_design_option_a.md` (historical draft).*
2. **Static OR Dynamic per invariant (二选一), NEVER "dual static-dynamic cross-checking"**:
   - Each checker implements **either** a static check (for properties observable in compiled artifacts) **or** a dynamic check (for properties observable only at runtime), i.e., $\mu \in \{\mathsf{Static}, \mathsf{Dynamic}\}$. Never claim `dual static-dynamic cross-checking`.
3. **Direct deterministic testing on each compiled seed, NEVER differential testing to find bugs**:
   - During fuzzing, deterministic checkers directly test **each compiled seed** (`each compiled seed`) to detect invariant violations, rather than relying on differential baseline builds to find bugs or asking an LLM to judge whether silent defense bugs occur.
4. **Formalization wording boundary**:
   - Describing our formalized primitives / specifications is accurate and encouraged, but avoid overclaiming formal verification terms such as `verify`, `verified`, `proven`, or `fully safe` without theorem-prover proofs; use `check`, `test`, `detect`, or `validate`.

## 3. Anonymized Artifact Repository
- **Live Anonymous URL (included in `main.tex` §IV Implementation)**: `https://anonymous.4open.science/r/DeFenzz/README.md`
- **Local Staging Repository**: `/Users/bytedance/projects/research/defenzz-artifact` (orphan commit `2671de5`, `Anonymous Authors <anonymous@example.invalid>`).
- **Backing GitHub Repository**: `git@github.com:zjy-dev/defenzz-artifact.git` (**must remain Private** throughout double-blind review so code search cannot link identifiers to the author's GitHub handle; local gitignored `pipeline/.env` is not tracked or served on `anonymous.4open.science`).
- **CFP Freeze Rule**: Per IEEE S&P 2027 CFP, **do NOT push updates** to the artifact repository after the paper submission deadline passes.
