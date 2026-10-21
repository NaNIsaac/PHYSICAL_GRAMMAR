# 16. Decisions, Discards, Open Questions

## A. Current strong decisions

1. **Entity grounding is mandatory for Physical Features.**
2. Feature is broader than Quantity.
3. Quantity is a quantitatively structured Feature.
4. Feature Kind definitions include Entity binding patterns and constraints.
5. Roles are not automatically ontology classes.
6. Entity selection does not imply spatial partition.
7. Primitive/derived status may be resolution-relative.
8. Definition, physical law, constitutive relation, and representation must be distinct.
9. Dimension is a projection, not full semantic identity.
10. Prefer existing mathematics for hard geometry/time/tensor issues.
11. Freeze grammar before blind validation.

## B. Demoted / discarded directions

### Broad `Object` as central formal term

Too ambiguous between physical body and focus quantity. Use `Entity` and `Feature`.

### Huge universal ontology

Not the active goal.

### Domain as universal physical primitive

Too overloaded. Use Stage/Background/Site roles/structures where appropriate.

### A1Component/A2Component subclasses

Use repeated typed slots plus cross-slot constraints instead.

### `Surface = Boundary`

Too narrow. Arbitrary measurement surfaces exist; thin/surface Entities may have 2D occupancy.

### `Flux = Flow / Area` as universal definition

Only a special/simple case. Local flux density, orientation, crossing, moving surfaces, and integration matter.

### `Change = subtraction`

Too narrow. General Change is comparison of temporal occurrences; Delta is additive specialization.

### `Stress = Force / Area`

Dimensionally useful but semantically incomplete. Traction-map / momentum-transport structure is richer.

### `D = εE`, `σ=C:ε`, etc. as definitions

These are constitutive/model relations under assumptions.

## C. Open questions

### 1. Formal status of Site

Distinct sort vs Feature-like first-class term vs geometry extension object.

### 2. Exact Scope semantics

How much context should be explicit in terms vs inherited from the surrounding analysis?

### 3. Background Entity

Useful analytical anchor, but should not be confused with an ontological universal whole.

### 4. Time

Potential approaches:

- Temporal Stage + Sites;
- clock/synchronization-induced coordinates;
- external spacetime formalism.

Do not freeze until relativity/quantum tests.

### 5. State

Potential generalization above Position/Orientation, but avoid making an unstructured catch-all primitive.

### 6. Count and Angle dimensions

Optional richer generators `C` and `Θ` are attractive projections but need literature/standard compatibility review.

### 7. Crossing

Strong transport constructor candidate; determine whether it belongs in core physical grammar or transport extension.

### 8. Field

Likely a higher-order/site-indexed constructor. Need compatibility with distributions and generalized fields.

### 9. Tensor-order rules

Promising generation rules, but differential-form representations and dual-space conventions must be handled carefully.

### 10. Moment family

Determine whether distribution moments and `MomentAbout` should share one abstract parent or remain sibling constructors.

### 11. Potential family

Likely intentionally split due lexical overload.

### 12. Thermodynamics

Need serious benchmark of extensive/intensive, conjugate pairs, natural variables, Legendre transforms, heat capacity, entropy.

### 13. Quantum/classical correspondence

Next major stress test; see `20_FUTURE_STRESS_TESTS.md`.

### 14. Interrupted user term

Immediately before requesting this handoff, the user started: "양자 고전 대응원리나, ㄴ히터워" and the second term was interrupted/unclear. **Do not guess what it meant.** Resolve in the next session if relevant.
