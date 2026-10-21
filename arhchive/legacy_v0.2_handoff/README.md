# QSF / Physical Grammar — Complete Research Handoff (2026-09-08)

This archive is the **current complete handoff** for the QSF → Physical Grammar research line after the Entity/Feature reset and the electrodynamics/continuum-mechanics stress tests.

## Read order

1. `00_MASTER_HANDOFF.md` — current thesis, architecture, decisions, and shortest reconstruction path.
2. `01_CORE_SEMANTICS_ENTITY_FEATURE.md` — Scope, Entity, Feature, Quantity, Feature Kind.
3. `02_FORMAL_MODEL_TYPED_LAMBDA_AND_CONSTRAINTS.md` — lambda/dependent-slot interpretation and constructor grammar.
4. `03_DEFINITION_SYSTEM_AND_VOCABULARY.md` — how derived Feature Kinds are actually defined.
5. `04_SPATIAL_AND_TEMPORAL_GRAMMAR.md` — Site, Surface, Distance, Extent, Time, Change, Rate.
6. `05_QUANTITY_COMPOSITION_NORMALIZATION_AND_COMPARISON.md` — density/fraction/concentration/specific/molar families.
7. `06_FIELDS_TENSORS_AND_HIGHER_ORDER_GENERATION.md` — Field, Stress, tensor-order generation, Response Maps.
8. `07_BALANCE_TRANSPORT_AND_CONSERVATION.md` — Crossing, flux, continuity, momentum/energy balance.
9. `08_ELECTRODYNAMICS_STRESS_TEST.md` — Maxwell integral/differential forms and constitutive split.
10. `09_CONTINUUM_MECHANICS_STRESS_TEST.md` — configurations, strain, material derivative, Cauchy momentum.
11. `10_CONSTITUTIVE_RELATIONS_AND_RESPONSE_MAPS.md` — Hooke/Fourier/Fick/Ohm/Newtonian-fluid pattern.
12. `11_MOMENTS_POTENTIALS_AND_DERIVATIVE_FAMILIES.md` — moment and potential overload families.
13. `12_PROJECTION_INFORMATION_LOSS_AND_NOMENCLATURE.md` — full semantics → kind skeleton → component signature → dimension.
14. `13_VALIDATION_PROTOCOL_AND_BENCHMARKS.md` — blind corpus test and G0–G4 reducibility scale.
15. `14_RELATED_MATH_AND_STANDARDS.md` — existing mathematics/ontologies to borrow instead of reinventing.
16. `15_DSL_AND_IMPLEMENTATION_SKETCH.md` — executable notation / checker sketch.
17. `16_DECISIONS_DISCARDS_AND_OPEN_QUESTIONS.md` — frozen decisions, demoted ideas, unresolved points.
18. `17_RESUME_PROTOCOL.md` — exact instructions for continuing the research in a new session.
19. `18_WORKED_VOCABULARY_REFERENCE.md` — compact dictionary of worked Feature Kinds.
20. `19_CHANGELOG_FROM_2026-09-07.md` — what changed after the previous grammar checkpoint.
21. `20_FUTURE_STRESS_TESTS.md` — quantum–classical correspondence and other next domains.

## Archive / provenance

`archive/2026-09-07_checkpoint/` contains the prior checkpoint **unchanged**. The exact prior ZIP is also preserved as `archive/QSF_GRAMMAR_CHECKPOINT_2026-09-07_FINAL.zip`.

Old documents contain terminology that has since been superseded. They are preserved for research provenance, not as the current specification.

## Current shortest thesis

> **Scientific feature semantics contains reusable Entity-binding and compositional structure between full physical interpretation and ordinary dimensional analysis.**

The central empirical question is:

> **How much scientific feature semantics can be reconstructed from Entity grounding and a small generic constructor grammar before domain-specific physical knowledge is required?**

## Status

This is a **research specification / handoff**, not a finalized standard. Formal choices such as exact dependent-type semantics, the status of Site, Time, Count dimension, Angle dimension, and the core/extension boundary remain testable hypotheses.
