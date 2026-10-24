# Post-v0.5 Research Continuation — 2026-10-25

**Status:** working research synthesis; **not** a v0.4 kernel revision.  
**Purpose:** merge the post-v0.5 project state into the repository without rewriting the provenance of the frozen kernel, BB1, M4, or pgcheck results.

## 1. Compatibility rule

This document deliberately separates two things:

1. **Historical specification state** — the v0.4 kernel and the v0.5 research package remain exactly what the existing repository says they were.
2. **Current research state** — later discussion has produced a broader architecture, new tests, and a renewed nomenclature/identity program. These are recorded here as Working/Candidate unless separately promoted by a future decision record.

Therefore:

- do not reinterpret old BB1/M4 grades as if they tested the architecture below;
- do not silently edit the v0.4 grammar to make later ideas appear older than they are;
- do not treat a useful analysis vocabulary as a new AST primitive without a separate decision;
- use this file as the current continuation point when asking what the project is investigating now.

## 2. Current positive thesis

The project is now best understood as an attempt to make the **implicit semantic context of physical expressions explicit and structurally manipulable**.

Ordinary notation is optimized for calculation and communication within an already shared context. It often leaves the reader to infer, from definitions and convention:

- what entity a quantity or feature is about;
- what region, component, reference, condition, or process is involved;
- how a derived concept was constructed;
- which distinctions are preserved, bound, aggregated, transformed, or discarded.

Physical Grammar investigates whether enough of that context can be represented structurally that physical concepts can be **searched, compared, checked, and partly inferred by their structure**, rather than only by names, symbols, units, or surface formulas.

This keeps the earlier grounding/genealogy thesis but broadens the research question beyond one monolithic grammar.

## 3. Physical Feature re-opened as the semantic umbrella

The v0.4 kernel deliberately preferred `Property` and retired `Quantity ⊂ Feature` as a core axiom. That historical decision remains intact.

Post-v0.5 work has nevertheless reopened **Physical Feature** as a useful *semantic umbrella* above quantitative and non-quantitative cases. This is currently a research-layer hypothesis, not a retroactive kernel edit.

### Working definitions

- **Physical Feature** — a semantic attribute, relation, state-characteristic, or other physically meaningful feature attributable to an entity, state, process, region, or relation.
- **Feature Concept** — the general kind/schema independent of a particular bearer or value.
- **Feature Instance** — a feature concept grounded to a particular bearer/context.
- **Feature Value** — a value associated with a feature instance; it need not be a real scalar.
- **Quantity** — a Physical Feature whose value space supports scientifically meaningful quantitative structure such as comparison, order, algebra, measurement, or transformation.
- **Qualitative Feature** — a feature whose relevant value space may be nominal or categorical in the current use.
- **Representation** — a way of encoding or expressing a feature/value, not the feature identity itself.

Examples that motivate the broader umbrella include:

- `Mass[A]` — quantitative;
- `ElectricField[A, Site]` — vector-valued quantitative;
- phase — cyclic-valued;
- impedance — complex-valued;
- crystal phase label — categorical;
- color category — nominal/categorical in one representation, while color can also admit quantitative representations.

A strict disjoint taxonomy such as `Physical Feature = Quantity ⊔ Qualitative Feature` is **not** adopted. The same physical subject may admit multiple representations and value structures.

## 4. From one universal grammar to a federation of small calculi

A major post-v0.5 shift is architectural.

The current hypothesis is that Physical Grammar should not force every semantic responsibility into one AST. It may be better modeled as a **federation of narrow formalisms/services exchanging typed contracts**.

| Label | Working responsibility | Typical questions |
|---|---|---|
| **R — Referential / Grounding** | entity reference, slots, binding, partial grounding, referential genealogy | “about what?”, “which entity is bound?” |
| **T — Physical Type** | admissible value/feature structure, scalar/vector/tensor/cyclic/categorical, dimension where relevant | “is this operation meaningful for these operands?” |
| **C — Construction** | composition, normalization, derivative, integration, aggregation, coordinate change | “how was this concept built?” |
| **A — Abstraction / Scope** | projection, information loss, tracked distinction, equivalence, tolerance | “what can be forgotten safely for this task?” |
| **G — Geometry / Localization** | region, boundary, site, orientation, normal, measure, gradient prerequisites | “what geometric objects/operations must exist?” |
| **D — Process Structure** | process identity, participation, change, transfer, rate, balance, sequence | “rate of what process?”, “what is transferred?” |
| **K — Restriction Context** | held-fixed variables, explicit restrictions, regime/context constraints | “under what restriction is this defined?” |
| **S-ID — Semantic Identity** | convergence/certification of concept identity from typed structure plus domain semantics | “what makes this the physical concept it is?” |
| **Q? — Assertion / Law status** | definition, identity, constraint, constitutive relation, evolution law, conservation law, empirical/model relation | “what kind of statement is this equation?” |
| **M — Realization / Measurement** | sensor, calibration, inference, uncertainty, simulation, reported result | “how was the feature/value obtained?” |
| **X — Expression / Nomenclature** | names, symbols, aliases, language, descriptors, terminology provenance | “how is the concept expressed?” |

This is **not** a strict pipeline. For example geometry may supply objects to referential and construction layers; restriction may constrain a construction; process structure may contribute to semantic identity; measurement should target an already identified feature.

## 5. Structural invariance / renaming program

A useful diagnostic introduced after v0.5 is to remove physical vocabulary and ask what remains.

Example:

`MassDensity[A] := Mass[A] / Volume[OccupiedRegion[A]]`

Rename the domain vocabulary:

`P3[A] := P1[A] / P2[R1[A]]`

Even after renaming, some structure remains visible:

- `A` is a referent;
- `R1[A]` constructs/selects another referent;
- `P1` and `P2` are applied to referents;
- the resulting expressions are combined.

The current test ladder is:

- **R0 — lexical renaming:** erase conventional physical names.
- **R1 — domain erasure with signatures retained:** keep types/signatures but remove domain labels.
- **R2 — type weakening:** replace rich quantity/value types by a generic Feature-like type.
- **R3 — grounding restoration:** reattach physical identities/roles/conditions and observe what judgments return.

The intended lesson is not “physics can be made substance-free.” Rather:

> **Before adding more physical meaning to the grammar, test what structure survives when that meaning is removed.**

The working design principle is therefore **substance-minimal grammar with explicitly grounded physics**, not substance-free physics.

## 5.1 Formal inspirations and architecture lessons

The later conversations compared PG with several field-independent formalisms, not to import them wholesale but to isolate reusable design lessons.

- **Institution-style abstraction:** define stable interfaces rather than one universal domain language.
- **Typed lambda calculus / type theory:** separate application, binding, composition, and well-formedness from full physical interpretation.
- **Operads / PROPs and compositional systems:** model typed input/output composition while supplying concrete semantics separately.
- **Process algebra:** allow behavioral/process structure to form its own reusable calculus.
- **Abstract interpretation:** treat abstraction, information loss, and downstream soundness as explicit questions.

The resulting hypothesis is a **federation of narrow calculi**, not a single all-purpose ontology.

The conversations also used three diagnostic tests:

- **Renaming Test** — erase vocabulary progressively and ask what structure survives.
- **Realization Test** — separate a target feature from measurement/inference/simulation routes.
- **Minimal-Operations Test** — attempt reduction to a small operation basis before adding primitives.

A later conversation temporarily called semantic-dependence strata `G0–G3`; this conflicts with the repository's established G0–G4 reducibility grades. The continuation therefore uses:

- **SD0** structural;
- **SD1** physically typed;
- **SD2** semantically grounded;
- **SD3** realization dependent.

See [PROJECT_CONVERSATION_SYNTHESIS_2026-10-25.md](PROJECT_CONVERSATION_SYNTHESIS_2026-10-25.md) for the full conversation-derived record.

## 6. Candidate minimal operations

Post-v0.5 work has explored a small reusable operation basis:

- `APPLY`
- `BIND`
- `COMPOSE`
- `COMBINE`
- `AGGREGATE`
- `PROJECT`
- `ASSERT`

Possible reductions under investigation:

- partial grounding ≈ `APPLY + BIND`;
- normalization ≈ typed `COMBINE(/)` plus semantic classification;
- integration/summation ≈ `AGGREGATE + BIND`.

`CONDITION`, `REPRESENT`, and `REIFY` remain unresolved as primitive operations versus interfaces/services.

## 7. Practical semantic examples

### 7.1 Density, concentration, and fraction

Surface formulas can share the same arithmetic skeleton while differing in bearer/reference structure.

`MassDensity[A] := Mass[A] / Volume[OccupiedRegion[A]]`

`NumberDensity[X in A] := Count[X in A] / Volume[OccupiedRegion[A]]`

`AmountConcentration[X in S] := Amount[X in S] / Volume[S]`

`MassFraction[X in M] := Mass[X in M] / Mass[M]`

The point is not to mandate these surface spellings. The point is that a semantic representation can preserve distinctions such as:

- bearer versus component;
- component versus whole;
- spatial normalization versus whole-quantity ratio;
- the genealogy of the denominator;
- the construction family shared across differently named quantities.

This suggests searches such as “quantities normalized by a spatial measure” or “component/whole ratios” without relying only on lexical labels.

### 7.2 Partial grounding

`Distance[A, □]`

represents a relation with one referential slot bound and another still open. It should not be confused with a missing measured value.

### 7.3 Held-fixed response quantities

`κ_T` and `κ_S` motivate separating the response construction from restrictions such as `HOLD(T)` and `HOLD(S)`.

The current direction is a thin **Restriction Context**, not a giant universal `Condition` primitive.

### 7.4 Resolution-dependent quantities

Wavelength-resolved and frequency-resolved radiance motivate decomposition of “resolution” into:

- the resolved variable identity;
- free/bound variable status;
- the measure/density with respect to that variable;
- the dependency of the resulting feature.

An invertible transformation between `L_λ` and `L_ν` does not by itself establish semantic identity.

### 7.5 Same dimension, different process semantics

Frequency and radionuclide activity can both have dimension `T^-1`, while differing by process identity:

- `RATE[oscillation]`
- `RATE[radioactive decay]`

Likewise absorbed dose and kerma can share unit and coarse construction while differing in energy-transfer genealogy.

### 7.6 Measurement realization

`Temperature[A]` may be realized through thermocouple voltage, resistance calibration, or optical inference.

The target feature identity and the realization genealogy should therefore remain separable.

## 8. Process Structure candidate

Process semantics showed enough recurring identity-bearing structure to warrant an independent candidate subformalism.

Working skeleton:

- `PROCESS`
- `PARTICIPATE`
- `CHANGE`
- `TRANSFER`
- `RATE`
- `BALANCE`
- `SEQUENCE`

This does **not** mean process-bearing concepts are themselves laws. For example:

- radionuclide activity is not the radioactive decay law;
- heat flux is not Fourier's constitutive law.

This reinforces the need for a separate future **Assertion / Law-Status** audit.

## 9. Restriction Context candidate

Post-v0.5 trials suggest that several notions previously grouped as “conditions” should not be conflated.

Examples:

- `HOLD(T)` — held-fixed variation constraint;
- `BIND(T=T0)` — binding to a value;
- `FREE(λ)` — resolved/free variable status;
- `REFERENCE(standard_state)` — reference selection;
- boundary/equilibrium/small-perturbation/gauge/cutoff conditions — may require other providers.

The current view is therefore a **thin cross-cutting restriction service**, not a self-contained universal condition calculus.

## 10. Semantic identity as a convergence problem

The current semantic-domain analysis suggests that “grounded physical semantics” is heterogeneous.

Possible identity-bearing inputs include:

- concept identity seed;
- physical referent kind;
- participant/context roles;
- reference/baseline;
- restrictions;
- resolved-variable identity;
- physical construction class;
- process/transfer semantics.

Other responsibilities may belong elsewhere:

- law/assertion status;
- model/regime context;
- measurement realization;
- terminology/authority;
- equivalence policy.

The working hypothesis is that semantic identity is better treated as a **certificate/convergence layer** that integrates evidence from multiple small formalisms, rather than as one enormous semantic node.

## 11. Current open questions

1. Is `Physical Feature` only an analysis-level semantic umbrella, or should a future kernel expose it explicitly?
2. What is the smallest stable interface among R/T/C/A/G/D/K/M/X?
3. Which constructions are true reusable grammar operations and which are typed mathematics?
4. Can Process Structure justify an independent calculus across unrelated domains?
5. Can Restriction Context remain thin without becoming an ontology dump?
6. How should assertion/law status be formalized?
7. How should semantic identity certificates be represented and compared?
8. Which structural searches provide measurable benefit over generic typed expression trees?
9. How should the nomenclature/identity registry connect to the semantic architecture without becoming the ontology itself?
10. Which of the post-v0.5 trials should be reconstructed as reproducible repository benchmarks?

## 12. Research rule retained

The earlier repository rule still applies:

`Question → Evidence → Analysis → Finding → Decision → Theory revision`

The architecture above is a **research map**, not evidence that every box deserves a primitive or a permanent module.
