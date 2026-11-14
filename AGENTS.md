# DeFenzz Paper — Agent Writing & Technical Ground-Truth Rules

## 1. Writing Skill & Locked Sections
- Always load and follow the **`plain-paper-writing`** skill when drafting or revising manuscript prose (plain vocabulary, 15–25 words per sentence, strict design-vs-implementation separation outside `Section IV Implementation`, and sentence-split `diff` + word-level track-changes on delivery).
- Check [`outline_status.md`](./outline_status.md) before editing `main.tex`: never modify sections marked `[ready]` unless explicitly instructed by the user.
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
