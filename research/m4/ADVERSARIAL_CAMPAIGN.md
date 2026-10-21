# M4 — Adversarial Counterexample Campaign

## Research question
What is the smallest physically legitimate case that the frozen v0.4 kernel cannot express naturally?

Unlike Blind Benchmark I, finding a failure is a success condition.

## Attack families
| ID | Attack | Target weakness |
|---|---|---|
| A1 | Role collision | value symmetry vs semantic role asymmetry |
| A2 | Condition identity | complex physical conditions beyond fixed-variable notation |
| A3 | Nonlocal properties | multi-point/source-response dependencies |
| A4 | History dependence | trajectories, memory kernels, hysteresis; Entity escape hatch |
| A5 | Gauge / quotient identity | representation equivalence vs physical identity |
| A6 | Topological quantities | global invariants and equivalence classes |
| A7 | Observer / frame dependence | observer-relative projections of deeper objects |
| A8 | Emergent / effective quantities | coarse-graining creates effective Entities/Properties |
| A9 | Operational quantities | operational definition vs ontological definition |
| A10 | Scope-induced identity collapse | Entities/distinctions disappear or emerge across Scope |

Priority: A4, A5, A8, A10 are highest-risk.

## Dual scoring
Keep G0–G4 for reducibility/required knowledge and add an orthogonal naturalness scale:

- **E0 Natural** — direct, idiomatic use of the grammar.
- **E1 Mild encoding** — small explicit structure with no conceptual distortion.
- **E2 Awkward encoding** — substantial scaffolding but semantics remain transparent.
- **E3 Escape-hatch encoding** — technically expressible mainly by reifying/annotating arbitrary things; threatens falsifiability.
- **E4 Genuine failure** — cannot be represented without changing the grammar.

A case may be `G2 / E3`: domain semantics are known, yet the grammar only survives unnaturally.

## Corpus rule
Freeze ~20–30 adversarial cases before detailed parsing. Use 2–3 minimal cases per attack family where possible. Do not repair the grammar during scoring.

## Special falsifiability test
Repeatedly ask whether `Entity` is acting as a principled referential category or a universal escape hatch. History, effective systems, measurement processes and equivalence classes are especially diagnostic.
