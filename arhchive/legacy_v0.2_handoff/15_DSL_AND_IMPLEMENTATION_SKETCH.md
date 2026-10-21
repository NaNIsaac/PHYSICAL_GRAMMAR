# 15. DSL and Implementation Sketch

The DSL should make semantic categories visibly different.

## 1. Minimal declarations

```text
entity A
entity B
entity S

seed Mass(e: Entity) : Quantity[Scalar, M]
seed Charge(e: Entity) : Quantity[Scalar, Q]
seed Occupancy(e: Entity, s: Entity) : Feature[Region]
```

## 2. Definitions

```text
define Volume :=
    λe, s. Measure3(Occupancy(e, s))

define MassDensity :=
    λe, s. Mass(e) / Volume(e, s)

define MassConcentration :=
    λpart, whole, s.
        Mass(part) / Volume(whole, s)
    where PartOf(part, whole)
```

## 3. Laws

```text
law Balance[Q] :=
    Rate(Content(Q, region))
      = -NetOutflow(Flux(Q), Boundary(region))
        + Production(Q, region)
```

## 4. Constitutive relations

```text
constitutive Ohm(material M):
    J = Conductivity(M) · E

constitutive LinearElasticity(material M):
    Stress = Stiffness(M) : Strain
```

## 5. Views / representations

```text
view SI:
    AngleDimension -> 1
    CountDimension -> 1
```

A richer internal view may retain those distinctions before projection.

## 6. Checker attributes

Potential synthesized fields:

```text
refs
feature_kind
quantity_kind
dimension
value_structure
tensor_order
component_tree
component_signature
```

Validation predicates:

```text
same_entity
part_of
same_kind
compatible_for_difference
same_or_mapped_stage
surface_embedded_in_stage
supports_metric
supports_derivative
supports_contraction
```

## 7. AST node families

```text
EntityRef
FeatureApplication
LambdaBinding
ConstructorApplication
Constraint
Definition
Law
ConstitutiveRelation
Projection/View
Lexicalization
Representation
```

## 8. Prototype priority

Do **not** build a large parser first.

Recommended order:

1. freeze annotation schema;
2. manually encode benchmark terms as Python/dataclass or JSON objects;
3. implement referent/dimension/value-structure propagation;
4. implement constraint checker;
5. implement projection and lexicalization;
6. only then design pleasant DSL syntax.

## 9. Core safety rule

The checker must never turn a law into a definition simply because the equation type-checks.
