# Physical Grammar — Post-BB1 Handoff

## One-sentence state
The v0.4 kernel survived a 60-case frozen blind benchmark without a G4 failure; the project is now switching from broad validation to adversarial falsification while keeping the kernel frozen.

## Read first
1. `STATUS.md`
2. `01_GRAMMAR_SPEC.md`
3. `02_PROJECTION_AND_EQUIVALENCE.md`
4. `07_BLIND_BENCHMARK_PROTOCOL.md`
5. `benchmark/results/BLIND_BENCHMARK_I_RESULTS.md`
6. `benchmark/analyses/OBSERVATION_LEDGER_BB1.md`
7. `research/decisions/RD_001_POST_BB1_KERNEL_FREEZE.md`
8. `research/m4/ADVERSARIAL_CAMPAIGN.md`

## Non-negotiable conceptual guardrails
- Distinction is an organizing principle, not an AST node.
- Scope changes representation/tracking resolution, not physical truth.
- Preserve justified distinctions; do not invent unjustified ones.
- Loss is allowed; dependence on lost distinctions is not.
- Representation ≠ Projection.
- Same formula/dimension/unit/value does not imply same physical Property.
- There is no universal unqualified Same relation.
- Useful analysis concepts do not automatically become grammar primitives.

## Frozen core reminder
Primitive semantic categories remain Scope, Entity, Property, EntityMap, and Physical Expression, with typed semantic relations. Grounding Closure classifies dependencies as focal/free, derived, bound, explicitly eliminated, or context-supplied; anything else is unresolved.

## BB1 correction worth preserving
B005 coefficient of restitution is **G2**, not G3. Its semantic definition requires a domain seed and exposes role-sensitive before/after grounding; it is not inherently a model/law-dependent G3 case.

## Current strongest candidate result
A useful working hypothesis is:

`Quantity identity ≈ referential genealogy + construction genealogy + preserved distinctions`

This remains a candidate finding until adversarial review.

## Next work
1. Audit borderline G1/G2 grades independently.
2. Freeze the M4 adversarial corpus before parsing it.
3. Score each adversarial case on both G0–G4 and E0–E4.
4. In parallel, build a small `pgcheck` spike and record encoding friction.
5. Only after recurring adversarial failures: write Findings → Research Decision → consider kernel revision.
