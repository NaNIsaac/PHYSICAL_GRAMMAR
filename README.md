# Physical Grammar v0.5 Handoff — Source-Deletion-Ready Consolidation

**Date:** 2026-09-08  
**Status:** v0.4 grammar kernel retained; v0.5 adds post-freeze analysis/meta documentation.  
**Lineage:** physical-quantity naming / QSF → Physical Grammar → semantic parse → quantity semantics → naming/rendering.

## 2026-10-25 research continuation

The historical v0.4 kernel and v0.5/M4 evidence remain unchanged. Later project work has moved toward a **federation of small semantic calculi** rather than silently expanding the frozen kernel.

For the current research state, read:

- [research/CONTINUATION_2026-10-25.md](research/CONTINUATION_2026-10-25.md) — current thesis, Physical Feature working umbrella, R/T/C/A/G/D/K/M/X architecture, renaming tests, process/restriction candidates, and practical examples.
- [research/NOMENCLATURE_REGISTRY_2026-10-25.md](research/NOMENCLATURE_REGISTRY_2026-10-25.md) — downstream naming, semantic identity, proposal/registry/lifecycle/provenance design.
- [research/POST_V05_STRUCTURAL_TRIALS_2026-10-25.md](research/POST_V05_STRUCTURAL_TRIALS_2026-10-25.md) — conversation-derived structural/interface/condition/process trial summaries that still require repository-native reproduction.

**Compatibility rule:** these files are Working/Candidate continuation documents. They do not retroactively change the v0.4 specification or re-grade BB1/M4.

## What this package is

This is the self-contained restart package for the Physical Grammar / 물리량 명명학 project. It intentionally preserves the **v0.4 core grammar** rather than silently promoting ideas discovered during calibration. The new v0.5 documents capture the post-v0.4 discussions needed to delete the source chats/intermediate notes without losing the project state.

## Read in this order

1. `00_OVERVIEW.md` — thesis and project boundary.
2. `01_GRAMMAR_SPEC.md` — canonical v0.4 kernel.
3. `02_PROJECTION_AND_EQUIVALENCE.md` — explicit information loss, qualified sameness, factorization safety.
4. `03_TERMINOLOGY_AND_VIM_ALIGNMENT.md` — metrology boundary.
5. `04_WORKED_EXAMPLES.md` — canonical examples.
6. `05_DECISIONS_AND_OPEN_QUESTIONS.md` — freeze/provisional/do-not-add decisions.
7. `07_BLIND_BENCHMARK_PROTOCOL.md` — benchmark gate.
8. `08_META_TERMINOLOGY.md` — Physical/Grammar/Analysis/Framework layers and status vocabulary.
9. `09_SEMANTIC_PARSE_AND_CALIBRATION.md` — semantic parse sheet, 20 calibration quantities, R1–R4 findings, naming patterns.
10. `10_RICH_PHYSICAL_DIMENSION_AND_PERIODICITY.md` — RPD, angle/phase, Count, 2π doctrine.
11. `11_RESEARCH_POSITIONING_AND_LITERATURE.md` — neighboring fields, references, novelty ledger.
12. `12_HANDOFF_AND_NEXT_STEPS.md` — compressed restart state and next gate.
13. `06_CHANGELOG_V0_3_TO_V0_4.md` and `legacy_v0.2_handoff/` — historical recovery only.

## Current project thesis

> **Physical Grammar is a typed compositional semantic IR / semantic dependency calculus for physical expressions. It represents Properties through explicit Entity grounding, preserves grounding genealogy through composition, and makes scientifically relevant distinction loss explicit and task-checkable.**

Downstream project structure:

`PG core -> physics semantic patterns -> physical quantity semantics -> naming/rendering`

## Frozen principles

- Make scientific distinctions explicit.
- Construct distinctions explicitly; erase them explicitly.
- Loss is allowed; dependence on lost distinctions is not.
- Distinction is an organizing principle, not an AST node.
- Scope chooses relevance; it does not manufacture truth.
- Representation is not Projection.
- No universal unqualified `Same`.
- `A ~_π B iff π(A)=π(B)` for projection-induced exact indistinguishability.
- Projection is safe for downstream `P` when `P = P̄ ∘ π`.
- Exact `~` and tolerance-relative `≈` must not be conflated.
- VIM Quantity / Quantity Value / measurement terminology is retained rather than reinvented.

## Important post-v0.4 findings — not automatically grammar changes

- **R1:** role and grounding genealogy can matter.
- **R2:** held-fixed/constrained conditions can be part of quantity identity.
- **R3:** grounding is not all semantic dependence; indices/resolution/reference/operator domain can matter.
- **R4:** some Properties/constructions presuppose prerequisite structures that are not focal groundings.

The response to R1–R4 is **benchmark first, ontology later**.

## Next action

Freeze the kernel and run a genuinely blind multi-domain benchmark using the semantic parse sheet. Repeated G4 failures, not descriptive convenience, are the trigger for grammar revision.

---

## 2026-09-08 Post-BB1 checkpoint
Blind Benchmark I is complete (60/60; provisional G0=0, G1=7, G2=49, G3=4, G4=0). The v0.4 kernel remains frozen. Current work is M4 adversarial counterexample design plus a small executable-formalism spike (`experiments/pgcheck/`). Start with `STATUS.md` and `HANDOFF_2026-09-08_POST_BB1.md`.

## 2026-09-09 execution checkpoint

Start with [STATUS.md](STATUS.md) for the latest evidence audit, frozen M4 selection,
first memory-response analysis, and runnable `pgcheck`. The historical post-BB1
handoff is at [arhchive/HANDOFF_2026-09-08_POST_BB1.md](arhchive/HANDOFF_2026-09-08_POST_BB1.md).
BB1's reported completion is not independently reproducible from the current
aggregate-only records; see the new audit before treating its totals as validated.
