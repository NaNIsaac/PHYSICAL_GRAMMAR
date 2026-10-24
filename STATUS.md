# Physical Grammar — Current Status

## Repository audit (2026-10-23)

[Audit](research/AUDIT_2026-10-23.md): lineage, frozen/provisional index, case index and
open problems, gathered from the existing files. All eight pgcheck scripts reran on
Python 3.14.5 and 3.10: 159 checks passed and both matched-comparison ledgers were
reproduced. `tests/test_pgcheck.py` now pins those numbers. No result, grade or kernel
text changed.

## Latest continuation — M001/M003 model fixtures (2026-09-10)

[Matched model fixtures 02](research/MATCHED_MODELS_02.md) adds six finite queries
over actual spring and ideal-gas derivative records. `matched_models.py` executed
successfully with all integrity/model assertions passing: both representations
return two unsafe and four safe decisions. Role erasure loses drive identity even
when reciprocal values agree; condition erasure loses compressibility information.
Full records and condition-record reordering provide safe finite controls.

Shared exhaustive mathematics supplies these decisions; no PG advantage or
continuous-domain safety claim follows. This uses a different classifier from
pilot 01, so decision rates are not directly comparable. Human annotation costs,
independent encodings/review and the full typed/context comparison remain open.
An explicit case-ledger oracle, independent of Property/PG objects, now agrees on
all six decisions; it is an implementation cross-check over the same supplied
values, not independent physical validation. The harness also rejects three
malformed records (arity, unit, and held-fixed-variable violations). All seven inherited executable
scripts plus `matched_models.py` reran successfully on 2026-09-10; their
assertions passed. This is additive fixture validation, not grammar grading.
Kernel v0.4 and historical BB1 totals remain unchanged.
The compact machine-readable ledger is `research/MATCHED_MODELS_02_RESULTS.json`.

## Latest checkpoint — matched-information pilot (2026-09-10)

[Pilot 01](research/MATCHED_BASELINE_01.md) is executed on ten finite abstract
development diagnostics. Generic expression tree and PG adapter tie: eight correct
decisions, two unknown, zero false-safe/false-unsafe. Shared mathematics supplies
the collision findings; no PG advantage is demonstrated. These are duplicated
scalar patterns inspired by M4, not full physical encodings or independent cases.
The full typed/context baseline comparison and measured annotation costs remain
open. Next: actual M4 model encodings with matched operator/context declarations,
then independent review. Kernel v0.4 and historical BB1 totals stay unchanged.

## Kernel
v0.4 — still frozen. Blind Benchmark I reported no G4 failure; the evidence audit
has not independently reproduced that result. No kernel revision is justified yet.

## Research package
v0.5 — post-freeze research/meta layer.

## Current phase
M4 — Adversarial Counterexample Campaign. Five batches have **20/20 provisional
analyses**, with explicit witnesses or insufficiency questions and source checks.
This completes first-pass analysis, not independent validation or all predictions.
M3/BB1 is historically
reported complete (60/60); individual original evidence remains unavailable.

## Blind Benchmark I result (provisional, pending audit)
- G0 Grammar-derived: 0
- G1 Generic mathematics required: 7
- G2 Domain semantic seed required: 49
- G3 Model/law dependent: 4
- G4 Grammar failure: 0

The inherited claim is that 60 frozen cases were handled without emergency
primitives. The repository currently lacks the individual records needed to
reproduce that claim. G1/G2 boundaries and case provenance need independent audit
before publication-level claims.

## Main evidence clusters
1. Quantity identity needs grounding **and construction genealogy**.
2. Ordered/role-conditioned grounding matters, but `Role` is not yet justified as a primitive.
3. Held-fixed derivative conditions are semantic content, but `Condition` is not yet justified as a primitive.
4. Grounding Closure generalizes across spatial, species, state, and scatterer binding.
5. Coarse dimension/unit/value do not identify a Property.
6. Representation and Projection behave differently; projections can explicitly lose distinctions.
7. Reference/convention dependence recurs but remains heterogeneous.
8. Physical Expression must remain broader than named scalar Property.

## Current decision
Do **not** create v0.6 yet. Keep the v0.4 kernel frozen while actively searching for counterexamples.

## M4 plan
Attack the weak boundaries: role collision, complex conditions, nonlocality, history dependence, gauge/quotient identity, topology, observer/frame dependence, emergence/coarse-graining, operational definitions, and Scope-induced identity collapse.

Add an orthogonal naturalness score E0–E4 so “technically expressible only by an escape hatch” is not mistaken for success.

## User-side experiment
The disposable `pgcheck` prototype is implemented, including 12 initial BB1
sketches, a separate B018 reconstruction and M4 witnesses. Record friction rather
than repairing the grammar immediately; it is not a production or complete checker.

## Operating rule
`Question → Evidence → Analysis → Finding → Decision → Theory revision`

Interesting idea ≠ grammar change.

## 2026-09-09 execution checkpoint

- BB1 evidence/consistency audit recorded in
  `benchmark/analyses/BB1_AUDIT_2026-09-09.md`. Individual case parses/citations are
  absent; B018 has a specific-heat-capacity versus heat-capacity target mismatch.
  Reported totals remain provisional and unchanged; independent regrading is open.
- M4-01 selection frozen: 20 adversarial targets in `research/m4/CORPUS_M4_01.md`.
  This is an informed adversarial corpus, not a new blind test. Source completion
  and full scoring remain open.
- First worked candidate: `research/m4/M007_MEMORY_RESPONSE.md`. An explicit pair
  proves current input insufficient for current response in a chosen memory model.
  Candidate G3/E1 is not finalized; this is not a kernel counterexample.
- `experiments/pgcheck/pgcheck.py` now runs with standard-library Python: 12 BB1
  dependency sketches plus targeted checks and the M007 numeric witness. All 33
  checks passed. Implementation ceilings are recorded in `FRICTION.md`.
- Next: verify M007's complete source and encoding; analyze M010/M015/M020;
  reconstruct B018 and G1/G2 boundary records without rewriting historical results.

### Continuation: first M4 batch complete

- M007 source checked in the author's working PDF mirror; local encoding reviewed.
- M010, M015 and M020 analyzed with explicit domains, original comparison pairs,
  knowledge accounts and provisional grades. See
  [M4 batch 1](research/m4/BATCH_01_RESULTS.md).
- Current provisional grades: M007 G3/E1, M010 G3/E2, M015 G2/E1, M020 G1/E1.
  These are single-analyst assessments. The remaining 16 targets are unassessed.
- B018 reconstructed from IUPAC as cp=Cp/m, with fixed-pressure/fixed-composition
  semantics. Original result ledger/totals preserved; historical encoding unknown.
- Validation: `pgcheck.py` 33 checks and `m4_checks.py` 18 checks passed, **51 total**.
- Main refinement in analysis: distinguish actual information loss from injective
  smoothing, and ensemble marginals from exact empirical microstate measures.
- Next bounded batch: M008/M009/M016/M019; BB1 G1/G2 retrospective accounting.
  Independent review and final M4 grading remain open. No new primitive added.

### 2026-09-10 continuation: second M4 batch

- [M4 batch 2](research/m4/BATCH_02_RESULTS.md) records M008/M009/M016/M019,
  each with checked source passages, a 13-field parse, explicit domains,
  constructed comparisons, knowledge accounts and provisional assessment.
- Provisional grades: M008 G3/E1, M009 G2/E1, M016 G2/E1, M019 G1/E1.
  M019's G1 applies to the classical permutation quotient with supplied physical
  input; its quantum boundary check does not derive exchange statistics.
- Main distinction: representative information lost in gauge/permutation
  quotients differs from predictive state information lost in hysteresis.
  Local band curvature also does not determine finite-neighborhood dispersion.
- Validation: existing 33 + 18 checks rerun successfully; 25 new checks in
  `experiments/pgcheck/m4_batch2_checks.py` passed; **76 total**. These verify
  constructed mathematics/model examples, not physical truth or grammar grades.
- Twelve M4 targets remain unassessed. Next bounded batch: M003/M004/M005/M006.
  BB1 retrospective G1/G2 accounting and independent review remain open.
  Historical totals and the v0.4 kernel are unchanged.

### 2026-09-10 continuation: third M4 batch

- [M4 batch 3](research/m4/BATCH_03_RESULTS.md) adds M003/M004/M005/M006,
  with a Korean plain-language explanation, checked source passages, semantic
  parses, explicit witnesses, knowledge accounts and provisional grades.
- Grades: M003 G2/E1 (definitions; ideal-gas witness uses model input),
  M004 G3/E2, M005 G3/E1, M006 G1/E1 (given joint probability inputs).
- M004 is the main new pressure: a reacting equilibrium branch needs explicit
  constraints, local regularity and composition, beyond a fixed-variable list.
  E2/E3 naturalness and independent review remain open; no G4 established.
- M005 distinguishes source-index binding from information loss: the full
  response vector in the invertible spring model retains the complete force vector.
- Validation: 26 new batch 3 checks passed; **102 total** across four scripts.
  These validate constructed examples and limited dependency sketches, not the
  physical model truth, arbitrary constraint support or G/E grades.
- Eight M4 targets remain unassessed. Next batch: M001/M002/M013/M014, followed
  by M011/M012/M017/M018. BB1 retrospective accounting remains open.
  Kernel v0.4 and historical BB1 totals are unchanged.

### 2026-09-10 continuation: fourth M4 batch

- [M4 batch 4](research/m4/BATCH_04_RESULTS.md) adds M001/M002/M013/M014,
  with checked source passages, Korean explanations, 13-field parses and exact
  constructed witnesses. Provisional grades: M001 G3/E1; the other three G2/E1.
- Reciprocity in the chosen spring model and restitution under consistent
  relabeling preserve values without erasing experiment/body/stage semantics.
- Observer change differs from a common coordinate transformation. Complete
  electromagnetic decomposition is invertible; electric-only retention can lose
  information required by another observer.
- Validation: all five scripts passed, **126 checks** (33 + 18 + 25 + 26 + 24).
  These check declared examples and limited syntax/dependencies, not tensor typing,
  physical truth, general grammar sufficiency or provisional G/E grades.
- Next bounded batch: M011/M012/M017/M018, the four remaining frozen targets.
  BB1 retrospective accounting and independent review remain open. No new primitive
  or kernel revision; historical BB1 totals remain unchanged.

### 2026-09-10 continuation: fifth M4 batch and research assessment

- [M4 batch 5](research/m4/BATCH_05_RESULTS.md) adds M011/M012/M017/M018.
  Provisional grades: M011 G1/E1, M012 G2/E2, M017 G3/E1, M018 G2/E2
  for procedure semantics. Quantitative hardness conversion remains unknown.
- Winding requires a nonzero continuous trace; Berry holonomy requires the loop
  and consistent gauge/endpoint data. Berry phase is not generally homotopy invariant.
- Calibration distinguishes the instrument indication from the sample measurand
  and inferred result. Procedure encoding does not supply empirical hardness conversion.
- Validation: all six scripts passed **159 checks** (33 + 18 + 25 + 26 + 24 + 33).
  Tests cover constructed witnesses and limited records, not real calibration,
  general gauge patching, hardness conversion or independent grammar grading.
- M4-01 first-pass analysis is complete, **20/20**, with no G4 established.
  Independent review, especially E2/E3, and BB1 reconstruction remain open.
- [Research assessment](research/ASSESSMENT_2026-09-10.md) records strengths,
  novelty limits and a proposed matched-information baseline comparison.
  That comparison has not been run; it is the next recommended bounded work.
  Kernel v0.4 and historical BB1 totals remain unchanged.
