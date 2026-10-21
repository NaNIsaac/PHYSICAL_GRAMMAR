# 01. Core Semantics — Scope, Entity, Feature, Quantity

## 1. Scope

`Scope` is the current analytical context: which referents are independently named, what background/reference is chosen, and at what descriptive resolution distinctions are preserved.

A minimal schematic form is:

\[
\Gamma=(\mathcal E,B,R,\ldots)
\]

where `E` is the selected Entity set, `B` an optional Background Entity, and `R` a resolution/granularity choice.

Scope is meta-level. Do not attach it redundantly to every Feature unless a benchmark needs explicit context dependence.

## 2. Entity

> **Entity = independently addressable co-reference anchor under the current Scope.**

Entity is intentionally lightweight.

It does not imply:

- spatial disjointness;
- material-body status;
- exhaustive partition of reality;
- ontological fundamentality.

Examples include a person, a hand, a crystal, a beam, a material constituent selected as a sub-Entity, a laboratory frame, or a named coordinate/background frame `S`.

Part/whole and overlap should be represented by relations rather than by forcing exclusive classes.

## 3. Feature

> **A Physical Feature is an Entity-grounded first-class characteristic or relation carrying scientifically relevant distinction.**

Grounding condition:

\[
refs(F)\neq\varnothing.
\]

`refs(F)` may contain one or more Entities and may change under Scope refinement.

Examples:

- `Mass(A)` — one Entity;
- `Difference(Height(A),Height(B))` — two Entities;
- `Mean(Temperature,{A_i})` — collective referent;
- `Position(A;S)` — subject + reference/stage Entity;
- `Stress(B;x)` — body Entity + local Site/context.

Feature values need not be numerical.

## 4. Feature Value

Keep separate:

\[
Feature \neq FeatureValue \neq Representation.
\]

Examples:

- `Mass(A)` → quantity value → `2 kg` representation;
- `Material(A)` → categorical/structural value → `H2O` representation;
- `Phase(A)` → value `solid`;
- `Orientation(A;S)` → rotation-like value represented by matrix/quaternion/Euler angles.

Representation changes do not automatically create new Features.

## 5. Feature Kind

A Feature Kind is a schema for generating/comparing Features.

Working semantic record:

```text
FeatureKind:
    entity_slots
    value_space
    roles
    constraints
    capabilities
    optional definition
```

Examples:

```text
Mass(e : Entity) : Quantity
Position(e : Entity, s : Entity[Stage-role]) : Quantity/GeometricFeature
Material(e : Entity) : Feature
Count(x : CountedKind, e : Entity) : Quantity
```

## 6. Quantity

> **A Physical Quantity is a Physical Feature whose values have scientifically meaningful quantitative structure supporting comparison and measurement.**

Thus:

\[
Quantity\subset Feature.
\]

Do not define Quantity as "anything represented by a number".

A quantity kind may support only some operations. Capabilities are structure-dependent:

- order;
- additive difference;
- ratio comparison;
- discreteness;
- vector/tensor operations;
- metric comparison;
- differential structure.

## 7. Non-quantitative Features

Important examples:

- Material/Substance;
- Phase;
- Species/constituent identity;
- Shape;
- Structure;
- configuration labels;
- categorical state.

This is why Feature is the main semantic category and Quantity a structured subfamily.

## 8. Feature vs Feature Kind expression

`Mass` and `Volume` are kinds/schemata.

`Mass/Volume` without Entity binding is not yet a concrete Physical Feature. It is an **ungrounded Kind Expression / kind skeleton**.

\[
\boxed{
\text{Grounded Feature} \to \text{Ungrounded Kind Expression} \to \text{Dimension}
}
\]

The first projection is already a major semantic loss.

## 9. Relation can be a Feature

Do not require a separate ontological `Relation` class for every relation-like scientific fact.

If the scientifically analyzed target is relational, treat the result as a multi-Entity Feature when useful.

Examples:

\[
Distance(A,B),\quad Difference(Q(A),Q(B)),\quad Relative(Q(A),Q(B)).
\]

The relation/constructor distinction is grammatical and need not become an ontology explosion.

## 10. Resolution-relative grounding

A coarse Feature may expand into finer relational Features.

\[
Height(Person)
\leftrightarrow
Distance(CrownSite(Person),SoleSite(Person)).
\]

A Site may itself be promoted to an Entity in a finer Scope.

Therefore:

\[
\boxed{refs(F)\text{ and primitive/derived status are Scope-relative.}}
\]
