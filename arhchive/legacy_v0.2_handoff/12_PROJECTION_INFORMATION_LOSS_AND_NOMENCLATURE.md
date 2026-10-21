# 12. Projection, Information Loss, Nomenclature

## 1. Central projection example

Grounded density:

\[
\lambda e.\frac{Mass(e)}{Volume(e)}
\]

forget Entity binding:

\[
Mass/Volume
\]

forget kind/construction identity further:

\[
ML^{-3}.
\]

Each map creates a larger equivalence class.

## 2. Component tree and component signature

A semantic constructor tree preserves order/nesting:

```text
Rate(Density(Q))
Density(Rate(Q))
```

A component signature can intentionally commutativize this into a coarse multiset/signature such as `R D`, losing tree order.

Physical dimension forgets further distinctions.

## 3. Projection lattice

Useful projections include:

- full grounded interpretation → Feature/constructor tree;
- tree → component signature;
- grounded expression → ungrounded kind skeleton;
- rich quantity → physical dimension;
- rich quantity → tensor/value structure;
- rich object → symbolic/algebraic skeleton;
- semantic expression → conventional scientific name;
- Feature → numerical/unit representation.

There is no reason all must lie on one total order.

## 4. Equality is resolution-relative

Ask explicitly:

- same grounded semantics?
- same Entity-binding graph?
- same Feature Kind?
- same constructor tree?
- same component signature?
- same physical dimension?
- same symbolic skeleton?
- same conventional name?

Do not use one unqualified `same` judgment.

## 5. Richer count/angle views

Candidate optional rich dimensions:

\[
[Count]=\mathsf C,
\qquad
[Angle]=\Theta.
\]

Conventional projection may set `C -> 1` and `Θ -> 1`.

This allows semantic distinctions to be preserved longer without declaring SI practice wrong.

Examples:

- number density `C L^-3` → `L^-3`;
- frequency `C_cycle T^-1` → `T^-1`;
- angular velocity `Θ T^-1` → `T^-1`;
- torque can remain distinct from energy under some angle-aware conventions before SI projection.

These remain hypotheses/views to test, not core requirements.

## 6. Nomenclature as lexicalization

Many scientific terms are aliases for semantic expressions:

```text
Volumic(Mass) -> mass density
Specific(Energy) -> specific energy
PartWholeRatio(Mass) -> mass fraction
Rate(Position) -> velocity
Magnitude(Velocity) -> speed
MomentAbout(Force) -> torque
```

But surface morphology is not ontology. `potential`, `flow`, `intensity`, etc. are lexically overloaded.

## 7. Low-context explicit-first policy

Preferred design:

1. construct a rich explicit semantic form;
2. validate bindings/constraints;
3. compress/omit only what a grammar or convention can recover;
4. map to conventional names and notation.

> First learn to say everything; then learn what can safely be omitted.
