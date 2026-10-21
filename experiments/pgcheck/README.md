# pgcheck — Disposable Executable-Formalism Spike

Latest experiment: `python experiments/pgcheck/matched_baseline.py` runs ten finite
matched-information development diagnostics. PG and generic expression trees each
make eight correct decisions and abstain twice. These rows are separate from the
159 existing self-checks. See [the pilot report](../../research/MATCHED_BASELINE_01.md)
for shared-algorithm attribution, abstract-model scope and unmeasured costs.

Purpose: test which Physical Grammar claims can be made mechanically checkable. This is **not** a production implementation and must not drive ontology design.

Suggested first objects:
- `Entity`
- `Property`
- `EntityMap`
- `Integral` / `Sum`
- `Derivative(fixed=[...])`
- minimal relation types (`Definition`, `Law`, `Constraint`, `ConstitutiveRelation`)

Suggested checks:
1. free/derived/bound/eliminated/context Entity dependencies;
2. unresolved Entity dependency detection;
3. distinction loss across projection-like operations;
4. simple construction genealogy comparison.

Start by manually encoding ~10–15 benchmark cases. Record every point where the implementation feels forced. Do not immediately add a grammar feature to make the code prettier.

A useful prototype can remain ~300–500 lines and disposable.

## Implemented checkpoint — 2026-09-09

Run `python experiments/pgcheck/pgcheck.py` from the project root (Python 3.10+).
The script uses only the standard library and exits nonzero when a self-check fails.
It prints JSON with check names, 12 retrospective BB1 dependency sketches, and the
M007 memory-response counterexample calculation. No output files are written.

Implemented: ordered Entity/EntityMap genealogy, root-dependency closure, local
Integral/Sum binding, declared derivative conditions, relation labels, and a
single-contract safe/unsafe/unknown classifier. See `FRICTION.md` for limitations.

These sketches are not reconstructed historical BB1 records or new benchmark grades.
They include manually supplied domain terms and schematic operators. The prototype
does not check dimensions, mathematical value types, physical truth, arbitrary
dependency elimination, alpha-equivalence or general projection factorization.

Run `python experiments/pgcheck/m4_checks.py` for 18 additional checks covering
three exact rational M4 witnesses and a B018 retrospective dependency sketch.
These two scripts pass 51 checks. `m4_checks.collision` searches for
finite witnesses of insufficiency; no collision yields unknown, never a safe claim.
See `research/m4/BATCH_01_RESULTS.md` from the project root for scientific scope.

Run `python experiments/pgcheck/m4_batch2_checks.py` for 25 further checks covering
M008 axial hysteresis, M009 gauge representatives, M016 curvature mass and M019
permutation invariance. All three scripts pass **76 checks** as of 2026-09-10.
See `research/m4/BATCH_02_RESULTS.md` for source passages, models and limitations.
The batch 2 checks use exact rational examples and reuse the finite collision
search; they do not add a parser, validate constitutive physics or infer grades.

If Python is absent from PATH in the current Windows Codex environment, the
existing runtime used for this checkpoint can be invoked in PowerShell:

```powershell
& "$env:USERPROFILE/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe" experiments/pgcheck/m4_batch2_checks.py
```

That path is environment-specific; any standard Python 3.10+ installation suffices.

Run `python experiments/pgcheck/m4_batch3_checks.py` for 26 additional checks on
M003 constrained compressibility, M004 reacting equilibrium, M005 nonlocal response
and M006 covariance. Four scripts now pass **102 checks** (33 + 18 + 25 + 26).
The batch 3 script reuses probability validation, collision search, matrix inversion
and dependency machinery. It adds no general constraint solver. The reacting-model
finite differences are local numerical controls; other witnesses use exact rational
arithmetic. See `research/m4/BATCH_03_RESULTS.md`, including its Korean explanation.

Run `python experiments/pgcheck/m4_batch4_checks.py` for 24 additional exact checks
on M001 role reversal, M002 restitution, M013 observer energy and M014 field
decomposition. All five scripts pass **126 checks** (33 + 18 + 25 + 26 + 24).
The witnesses reuse existing helpers and add no dependencies or core grammar code.
See `research/m4/BATCH_04_RESULTS.md` for assumptions, sources and grading limits.

Run `python experiments/pgcheck/m4_batch5_checks.py` for 33 further checks on
M011 polygon winding, M012 Berry phase, M017 calibration and M018 procedure
semantics/Vickers arithmetic. Six scripts pass **159 checks** as of 2026-09-10.
Polygon interpolation is explicit; this does not recover arbitrary continuous
winding from samples. No real-material hardness conversion is implemented.
See `research/m4/BATCH_05_RESULTS.md` for sources and unresolved boundaries.
# Matched physical model continuation

Run `python experiments/pgcheck/matched_models.py` from the repository root for
six finite M001/M003 queries using ordered spring-response derivatives and
held-fixed ideal-gas derivatives. See [the comparison report](../../research/MATCHED_MODELS_02.md)
for shared model declarations, attribution and limits. The new script passed its
integrity and analytic model assertions on 2026-09-10; it does not alter pgcheck.
