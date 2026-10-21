# M4 batch 1 — 2026-09-09

Scope: four of the twenty frozen M4-01 targets. Source passages checked and
explicit encodings/witnesses reviewed by the same analyst. These are provisional
assessments, not independent replication, final corpus grades or a blind benchmark.
The sixteen remaining targets are unassessed. Kernel v0.4 remains unchanged.

| Case | Provisional G/E | Specific projection and query | Evidence |
|---|---|---|---|
| [M007](M007_MEMORY_RESPONSE.md) | G3/E1 | Current input -> current response in declared relaxation model | Equal current inputs; different convolution outputs. Analytic witness and numerical integration agree. |
| [M010](M010_AHARONOV_BOHM.md) | G3/E2 | Accessible local fields -> loop phase | Zero local fields for both backgrounds; half-flux-quantum difference gives distinct U(1) phases. Full-turn control gives the same phase. |
| [M015](M015_COARSE_DENSITY.md) | G2/E1 | Adjacent-cell averages -> fine mean square | Equal coarse profiles; mean squares 5 versus 4. Total mass has an explicit safe factorization. |
| [M020](M020_ONE_PARTICLE_MARGINAL.md) | G1/E1 | Ensemble marginals -> pair coincidence | Equal marginals; coincidence probabilities 1 versus 0. Product lift adds independence rather than recovering the joint state. |

G grades apply to the exact target relation and declared seeds in each record.
They do not form an intrinsic ranking of the physical concept's complexity. In
particular, M020 receives the physically interpreted joint distribution as input;
M015 needs the regional-mass/density interpretation; M010's physical phase coupling
is a law rather than just the definition of a line-integral functional.

## Findings from this batch

1. **A projection needs a specified domain and retained output.** The same phrase
   “coarse description” can mean a genuinely many-to-one reduction, an exact
   injective smoothing transform, or a numerically unstable inverse problem.
   Only the first automatically supplies exact indistinguishability classes with
   distinct members. M015's claim uses a specified cell-average map.
2. **A statistical label does not identify the reduction.** An empirical measure
   of a microstate and an ensemble marginal are different objects. M020's witness
   applies to the ensemble marginal; it does not prove loss for every object called
   a one-particle distribution.
3. **Global observables test contract scope.** M010 requires loop, gauge-domain and
   boundary information. Equality of local fields on an excluded-flux domain is
   insufficient for its loop-phase query.
4. **Availability is weaker than semantic correctness.** B018's wrong-bearer mass
   becomes dependency-closed when that bearer is put in context, but remains the
   wrong definition. Neither closure nor matching dimensions validates the whole
   physical expression. This is a ceiling of the spike, not a newly found G4.

These are clarifications supported by constructed examples, not novelty claims.
No repeated G4 or E3 was established. E2 in M010 records real mathematical/domain
scaffolding and needs further independent assessment; it is not being called a
natural success merely because arbitrary annotation is allowed.

## Executable evidence

From the project root, with Python 3.10+:

```text
python experiments/pgcheck/pgcheck.py
python experiments/pgcheck/m4_checks.py
```

Results: **33 existing checks + 18 new checks = 51 passed**. The new script uses
exact rational witnesses for M010/M015/M020, validates the probability domain,
includes negative controls, and encodes B018's derivative-plus-mass normalization.
Finite search returns **unknown**, never safe, when no collision is found. It
does not decide general factorization, validate quantum coupling or infer G/E grades.

## BB1 repair checkpoint

[B018 retrospective reconstruction](../../benchmark/analyses/B018_RETROSPECTIVE.md)
verifies cp=Cp/m against IUPAC and preserves the fixed-pressure/fixed-composition
derivative. The old ledger and totals are untouched. The documentary mismatch is
confirmed; whether the original analysis itself used the wrong target is unknown.

## Next bounded batch

- M008: compare hysteretic preparations with explicit state/history encoding.
- M009: specify admissible gauge transformations and equivalence, complementary to M010.
- M016: effective-mass tensor with momentum and approximation regime.
- M019: permutation quotient with an explicit label-sensitive query.
- Continue BB1 retrospective G1/G2 seed accounting; do not report reconstructed
  parses as recovered original evidence. Independent review remains outstanding.
