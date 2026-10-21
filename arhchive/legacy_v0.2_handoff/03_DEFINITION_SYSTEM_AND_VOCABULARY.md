# 03. Definition System and Vocabulary

## 1. Standard Feature Kind definition template

```text
Feature Kind: K

Entity slots:
    ...

Roles:
    ...

Definition:
    ...

Constraints:
    ...

Value structure:
    ...

Capabilities:
    ...

Dimension/signature:
    ...   # if quantitative

Derived from:
    ...

Conventional names:
    ...
```

## 2. Primitive-like vs derived

`Primitive` is not absolute. A kind may be atomic at one resolution and derived at another.

Use terms:

- **seed Feature Kind**: accepted without internal expansion in the current grammar layer;
- **Derived Feature Kind**: explicitly generated from other Feature Kinds/constructors;
- **Named/Established Kind**: conventional scientific lexeme mapped to a semantic expression.

Avoid metaphysical claims about ultimate primitives.

## 3. Seed candidates

Current domain seed candidates include:

- Mass;
- Charge;
- Count;
- Amount of substance;
- Material/Species/Phase;
- Energy (often treated as domain seed rather than reduced through model equations);
- State/Position/Occupancy/Geometry as needed;
- Field-specific seeds such as E/B/D/H or stress if a domain definition is imported externally.

Seed status is benchmark-driven.

## 4. Named derived kinds

Examples:

\[
MassDensity := \lambda e.Mass(e)/Volume(e)
\]

\[
SpecificEnergy := \lambda e.Energy(e)/Mass(e)
\]

\[
MassFraction :=
\lambda p,w.Mass(p)/Mass(w)
\quad where\ PartOf(p,w)
\]

\[
Velocity := Rate(Position)
\]

\[
Speed := Magnitude(Velocity).
\]

## 5. Well-formed expression vs established kind

A mathematically and dimensionally valid expression need not correspond to an established scientific kind.

\[
Height(A)\times Mass(B)
\]

may be a valid derived quantity expression but lacks a conventional named kind.

Therefore:

\[
\boxed{
\text{well-formed expression}
\not\Rightarrow
\text{established Feature Kind}
}
\]

## 6. Definition vs determination formula

Do not treat every formula used to calculate a quantity as its semantic definition.

Examples to keep model/law dependent:

- `F = ma`;
- `p = mv` in Newtonian mechanics;
- `K = 1/2 mv^2`;
- `σ = C:ε`.

The grammar must mark whether an equality is:

- definitional;
- physical law;
- constitutive relation;
- model/approximation;
- representation/conversion.

## 7. Conventional lexicalization

A scientific term may lexicalize a complex expression:

```text
Volumic(Mass) -> mass density
PartWholeRatio(Mass) -> mass fraction
Rate(Position) -> velocity
Magnitude(Velocity) -> speed
MomentAbout(Force) -> torque
```

Scientific naming should be treated as a realization/lexicalization layer over the semantic grammar.
