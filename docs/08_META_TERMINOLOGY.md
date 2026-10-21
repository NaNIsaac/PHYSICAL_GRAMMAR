# Physical Grammar — Meta-Terminology

**Status:** v0.5 working convention. This file governs how the project talks about itself; it does not add AST nodes.

## 1. Two independent axes

Every project term may be annotated by `(Layer, Status)`.

### Layer

| Layer | Question | Examples |
|---|---|---|
| Physical | What physical meaning/referent is represented? | Entity, Property, Reference, Condition |
| Grammar | How is that meaning composed/tracked/lowered? | grounding, genealogy, binding, projection |
| Analysis | How do we inspect quantities and names? | semantic parse, minimal pair, naming yield |
| Framework | How do we design/evaluate PG itself? | benchmark, G0–G4, [G]/[M]/[D] |

These are bookkeeping layers, **not an AST hierarchy**. Some terms legitimately straddle layers.

### Status

- **Canonical** — adopted in the current specification.
- **Working** — used in analysis but not frozen.
- **Candidate** — under consideration.
- **Deferred** — potentially useful, deliberately not formalized now.
- **Rejected** — deliberately excluded from the current design.

`Working != Canonical`.

## 2. Physical terms

### Entity — Physical / Canonical
A referent distinguished for independent treatment within Scope. It need not be a material object.

### Property — Physical / Canonical
A typed physical characterization with explicit Entity grounding and semantic structure.

### EntityMap — Physical / Canonical
Constructs/selects an Entity from Entity inputs while preserving genealogy, e.g. `OccupiedRegion[A]`.

### Reference — Physical / Working
A physical or semantic comparison reference that can participate in quantity identity, e.g. vertical direction or vacuum level. Do not confuse with prerequisite structure.

### Condition — Physical / Working
A held-fixed or constrained physical condition, e.g. `(∂V/∂p)_T`. Conditions may distinguish quantities with the same variables and dimensions.

## 3. Grammar terms

### Grounding — Grammar / Canonical
The semantic dependency answering **“about what referent(s) is this expression?”**. It is not generic dependency and not data provenance.

### Grounding genealogy — Grammar / Canonical
The compositional path by which grounding is preserved, e.g. `A -> OccupiedRegion[A] -> Volume[OccupiedRegion[A]]`.

### Grounding Continuity / Grounding Closure — Grammar / Canonical
Grounding must remain traceable and every Entity dependency must be focal/free, EntityMap-derived, bound, explicitly eliminated, or Scope-supplied.

### Distinction — Grammar / Canonical organizing principle
A difference that may matter to downstream semantics and may be preserved or discarded. **Distinction is not an AST node.**

### Scope — Grammar / Canonical
Determines which distinctions/referents are relevant and tracked and at what resolution. **Scope chooses relevance; it does not manufacture truth.**

### Binding / Elimination — Grammar / Canonical
Binding makes a free variable/dependency internal to a construction; elimination means a distinction is no longer independently available downstream. They often coincide but are not assumed identical.

### Representation — Physical/Grammar / Canonical
A way of expressing a physical meaning. Coordinate, quaternion, matrix, phase-angle, etc. may be representations. Representation change need not lose information.

### Projection — Grammar / Canonical
A semantic map that intentionally discards distinctions. `A ~_π B iff π(A)=π(B)`.

### Projection safety — Grammar / Canonical
For downstream task/map `P`, projection `π` is safe when `P = P̄ ∘ π`. **Loss is allowed; dependence on lost distinctions is not.**

### Generic semantic dependency — Grammar / Candidate
Benchmarking shows grounding is not all semantic dependence: roles, references, conditions, indices/resolution and operator domains may matter. Do not yet unify them into one new AST calculus.

## 4. Analysis terms

### Semantic parse — Analysis / Working
A diagnostic decomposition of a quantity/property into the semantic questions relevant to it.

### Prerequisite — Analysis / Working
Diagnostic question: **what structure must be presupposed for this Property/construction to be meaningful?** Examples: metric structure for distance, cyclic structure for phase, differential structure for gradient. This is not currently a grammar object.

### Role — Analysis/Physical / Working
Semantic function of an argument/referent, e.g. Source/Target. Role-sensitive grounding is empirically required, but `Role(...)` is not currently a new core node.

### Construction / construction family — Analysis / Working
How an expression is built, and a recurring family of such constructions: normalization/density, response derivative, aggregation, projection, reference difference, etc. Recurrence does not automatically justify a grammar primitive.

### Minimal pair — Analysis / Working
Two quantities that share most visible structure but differ in a crucial semantic distinction, e.g. isothermal vs isentropic compressibility.

### Naming yield — Analysis / Working
Qualitative ability of the semantic parse to explain or productively generate conventional naming: `none / explanatory / productive`. Not a formal metric.

### Lexicalization / naming transparency — Analysis / Working
Whether and how semantic distinctions are encoded in conventional names. `spectral`, `isothermal`, `angular` are relatively transparent modifiers; `work function` and `activity` are more opaque lexicalizations.

### Rich Physical Dimension (RPD) — Grammar/Analysis / Working
A task-/Scope-relative dimensional view `[·]_R` that preserves selected distinctions useful for dimensional comparison. It is **not** a universal replacement for SI and does not carry full grounding genealogy.

## 5. Framework terms

### Grammar primitive
A structure supplied by PG itself rather than by domain knowledge.

### [G] / [M] / [D]
Responsibility annotations: `[G]` grammar structure, `[M]` generic mathematics, `[D]` domain semantic seed. These annotations are framework bookkeeping, not physical semantics.

### Reducibility G0–G4
- G0 grammar-derived
- G1 generic mathematics required
- G2 domain semantic seed required
- G3 model/law/regime dependent
- G4 genuine grammar failure

The grade measures outside knowledge required, not conceptual difficulty.

### Calibration set / blind benchmark / grammar pressure / grammar failure
Calibration deliberately selects phenomena to exercise the grammar. Blind benchmark freezes an external corpus first. Grammar pressure is evidence that the current design may need revision. A domain seed is not by itself a grammar failure.

## 6. Design verbs

`Introduce` propose; `Adopt` accept into framework; `Refine` sharpen; `Generalize` widen; `Specialize` narrow; `Split` separate; `Merge` combine; `Promote` move an analysis notion into grammar; `Defer` postpone formalization; `Reject` exclude; `Freeze` hold fixed during evaluation.

## 7. Meta-rules

> **A useful description is not automatically a grammatical primitive.**

> **Failure to predict a conventional name is not automatically a grammar failure.**

Avoid premature nodes such as `Distinction(...)`, `BackgroundStructure(...)`, `CharacteristicScale(...)`, `ResponseCoefficient(...)`, or a universal `Role(...)` merely because the corresponding analysis vocabulary is useful.
