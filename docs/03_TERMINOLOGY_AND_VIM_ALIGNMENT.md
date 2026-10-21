# Terminology and VIM Alignment — v0.4

## 1. Principle

Prefer established terminology unless Physical Grammar introduces a genuinely new formal role. New names should mark new IR machinery, not merely restate existing scientific concepts.

v0.4 retains the v0.3 VIM/metrology alignment and adds only the minimum vocabulary required to distinguish representation, projection, and qualified equivalence.

## 2. Recommended vocabulary

| Term | Status | Physical Grammar use |
|---|---|---|
| Scope | PG core | Analytical context determining relevant distinctions, tracked referents, and resolution. |
| Entity | PG core | Unit of reference distinguished for independent treatment in a Scope. |
| EntityMap | PG core | Typed map from Entity tuple to Entity; constructs/selects referents and preserves genealogy. |
| Property | Established + formalized | Physical characterization represented with Entity slots and compositional semantic structure. |
| Open Property | PG modifier | Property expression with unfilled Entity slots. |
| Grounded Property | PG modifier | Property with explicit Entity grounding. |
| Ground / Grounding | PG core verb | Apply Entity/Entities to Property Entity slots. |
| Quantity | VIM | Preserve VIM meaning; do not use as synonym for `3 kg`. |
| Quantity Value | VIM | Value of a quantity, commonly represented by number and reference/unit. |
| Numerical Quantity Value | VIM | Numerical component relative to a chosen reference/unit. |
| Measurand | VIM | Quantity intended to be measured. |
| Quantify / Q | PG bridge | Expose/lower an admissible Property as a VIM-compatible Quantity. |
| Represent | PG/general math | Choose an admissible representation/encoding/coordinate form. |
| Projection | PG core formal role in v0.4 | Explicit information-reducing map used to form a coarser view. |
| Projection-induced equivalence | PG core relation | `A ~_π B iff π(A)=π(B)`. |
| Task-relative exact equivalence | Provisional | Exact substitutability for a declared task/observable set. |
| Approximate substitutability | Provisional | `A ≈_{T,ε} B`; not generally an equivalence relation. |
| Physical Expression | PG core | Typed composition of Properties, EntityMaps, parameters/constants, mathematics, relations, representations, and projections. |
| Feature | Legacy | v0.2 umbrella term; remains deprecated candidate. |
| Feature Kind | Legacy/provisional | Avoid as a grand ontology; use ordinary Property family/type/classification metadata if needed. |
| Distinction | Organizing language only | Explains the architecture; not a v0.4 AST node/type. |

## 3. Entity rather than Object

Physical Grammar uses **Entity** because its formal criterion is referential rather than merely “has properties”.

> **Entity = a unit of reference distinguished for independent treatment within a given Scope.**

Intuition: something the analysis can stably name and refer back to as one.

This supports material bodies but also regions, boundaries, sites, processes, states, interactions, modes, frames, and constructed systems when Scope requires them.

The claim is not “VIM forgot objects.” The claim remains:

> **Physical Grammar makes the referential side explicit, typed, compositional, and statically traceable.**

## 4. General versus grounded Property

Use the mathematical distinction directly:

`Mass` — open/general Property.

`Mass[A]` — grounded Property.

`Force[A,B]` — relational grounded Property.

There is no need to reintroduce a heavy `FeatureKind → FeatureInstance` ontology merely to express this.

## 5. Property versus Quantity

Do not define Quantity as simply “a Property with a number and unit.”

Working relation:

`Property --Quantify--> Quantity`

when the Property admits the relevant VIM-compatible quantity structure.

This remains an interface/view relation rather than a frozen metaphysical subclass claim.

## 6. Property versus Property value

Do not introduce a universal `PropertyValue` core object in v0.4. It risks conflating:

- the Property being characterized;
- a VIM Quantity;
- a Quantity Value;
- a coordinate representation;
- a categorical/nominal result;
- an observation or measurement result.

Use domain-appropriate downstream terms until a genuine common abstraction is demonstrated.

## 7. Representation versus Projection

This distinction is now frozen.

### Representation

Changes the form in which a semantic object is encoded/expressed. It may be information-preserving over a declared domain.

Examples: orientation as a rotation matrix or quaternion.

### Projection

Intentionally maps a richer representation to a coarser one and may identify source objects that were previously distinguishable.

Examples: full grounded semantics to physical dimension; tensor to a selected component; optional angle-aware dimension to conventional dimension with `Θ→1`.

Do not classify every `Represent` operation as a projection.

## 8. Equality and equivalence vocabulary

Avoid one unqualified `same` semantic relation.

At minimum distinguish:

- mathematical equality;
- identity/reference identity where relevant;
- structural equivalence/isomorphism;
- projection-induced equivalence `~_π`;
- provisional exact task-relative equivalence `~_T`;
- provisional approximate substitutability `≈_{T,ε}`.

Surface mathematics may still use conventional notation. The IR should preserve the semantic relation type when it matters.

## 9. Measurement discipline inherited from metrology

Physical Grammar continues to adopt the following discipline:

1. A scientific target must be sufficiently specified before a numerical result is meaningful.
2. Quantity and quantity value are distinct.
3. Measurement procedure/result should not be identified with the Property or Quantity itself.
4. Uncertainty can arise from incomplete specification of the measurand, not only instrument error.
5. Multiple procedures/models may target the same sufficiently specified quantity.

## 10. Positioning statement

Recommended paper wording:

> **Physical Grammar does not replace metrological vocabulary. It adopts its discipline of explicit specification and extends that discipline upstream into a typed, compositional representation of the entities and properties to which physical expressions refer, while making information-reducing projections and their induced equivalences explicit.**
