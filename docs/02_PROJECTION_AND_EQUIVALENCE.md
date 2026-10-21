# Projection, Equivalence, and Information Loss

## 1. Status

This chapter restores the strongest surviving principles from the v0.2 projection work and integrates them with the v0.3 Entity/Property kernel.

Projection is now a core semantic mechanism in v0.4. The surrounding contract/checker machinery remains partly provisional.

## 2. Central example: density

Rich grounded density:

`MassDensity[A] := Mass[A] / Volume[OccupiedRegion[A]]`

A projection may forget explicit Entity binding and genealogy, yielding a skeleton such as:

`Mass / Volume`.

A further dimensional projection yields:

`M L^-3`.

At each lowering, more expressions may become indistinguishable.

This is not an error by itself. It is a controlled reduction in represented distinctions.

## 3. Projection-induced equivalence

For a projection

`π : X → Y`,

define

`A ~_π B  iff  π(A)=π(B)`.

This relation groups source objects into the fibers/equivalence classes induced by the chosen projection.

The target representation therefore answers a precise question:

> Which source distinctions has this representation chosen not to express?

## 4. No universal projection ladder

Useful reductions/views include, depending on the object:

- grounded semantics → ungrounded Property/construction view;
- semantic constructor tree → component signature;
- rich quantity semantics → physical dimension;
- rich value structure → selected scalar/vector/tensor component;
- full symbolic object → algebraic skeleton;
- semantic object → conventional lexical form;
- physical semantic object → numerical/unit representation;
- physical semantic object → task-specific summary.

These maps need not form one total order.

Physical Grammar therefore distinguishes:

1. a **general representation graph**, which may include reversible maps and cycles; and
2. an **information/refinement DAG**, which orients explicitly information-reducing views from richer to coarser representations.

## 5. Component tree versus component signature

A semantic constructor tree preserves order and nesting:

```text
Rate(Density(Q))
Density(Rate(Q))
```

A component signature may intentionally commutativize this into a coarse multiset/signature, losing tree order.

Physical dimension forgets different and often further semantic distinctions.

Therefore semantic signature and physical dimension are separate projections of richer semantics; neither should be assumed to determine the other.

## 6. Qualified sameness

Physical Grammar does not treat “same” as one scalar judgment.

Potential criteria include:

- same mathematical value;
- same object identity;
- structurally isomorphic;
- same grounded Property semantics;
- same Entity-binding/genealogy graph;
- same construction tree;
- same component signature;
- same physical dimension;
- same tensor/value structure;
- same symbolic skeleton;
- same conventional name;
- same projection image;
- substitutable for a declared task.

The grammar should preserve the criterion rather than silently collapsing them into one token.

### Provocative slogan

> **Same is not a property. It is a projection.**

This is intentionally provocative, not a literal universal axiom. The formal statement is narrower:

> **A projection induces a notion of indistinguishability.**

And the broader design principle is:

> **Sameness is relative to a declared criterion of distinction.**

## 7. Factorization as a safety criterion

Suppose

`π : X → Y`

and a downstream observable/question is

`P : X → Z`.

If there exists

`P̄ : Y → Z`

such that

`P = P̄ ∘ π`,

then `P` can be answered using only the projected representation `Y`.

Equivalently, if `π(A)=π(B)`, then every such factorizing `P` must satisfy

`P(A)=P(B)`.

Interpretation:

> `P` is insensitive to the distinctions erased by `π`.

This produces the central safety principle:

> **Loss is allowed; dependence on lost distinctions is not.**

## 8. Principle versus algorithm

The factorization criterion is a semantic rule. It is **not** a claim that an implementation can decide every case.

v0.4 explicitly distinguishes:

`Projection Validity Principle ≠ Complete Projection Validity Algorithm`.

A practical static checker may use declared dependencies and projection contracts to prove some cases and return:

- `safe` — sufficient information is guaranteed;
- `unsafe` — a required distinction is known to have been removed;
- `unknown` — the checker cannot establish either result.

This conservative three-valued outcome is compatible with real static-analysis practice.

## 9. Projection contracts

The recommended provisional direction is guarantee-centered.

For a projection `π`, record positive preserved invariants/observables:

`Preserves(π,I)`.

Example:

```text
DimensionProjection

guarantees:
    physical dimension

known_losses:
    Entity grounding
    construction history
    selected semantic roles
```

The `known_losses` list is non-exhaustive. v0.4 does not attempt to construct a complete information-loss set.

## 10. Exact task-relative sameness

If a task `T` declares a set of relevant observables `O_T`, define provisionally:

`A ~_T B  iff  ∀P∈O_T, P(A)=P(B)`.

For a fixed `O_T`, this is an equivalence relation under ordinary equality in the outputs.

Operational reading:

> Within task `T`, `A` and `B` are exactly substitutable for all declared observables.

This supports the slogan:

> **Same means substitutable.**

But only as an operational criterion for a declared task, not as the universal definition of identity or all equivalence relations.

The status of `Task`/`O_T` as a core grammar object remains provisional.

## 11. Approximate substitutability

Real scientific work often tolerates bounded deviations. Use separate notation:

`A ≈_{T,ε} B`.

A typical criterion is:

`d(P(A),P(B)) ≤ ε_P`

for the observables required by task `T`.

This relation is generally **not transitive**. Therefore it must not be called an equivalence relation without additional structure/conditions.

Consequently:

- `~` is reserved for exact equivalence-like relations;
- `≈` denotes tolerance-relative approximate substitutability.

## 12. Angle and count views

The v0.2 handoff proposed optional richer internal generators:

`[Count]=C`,

`[Angle]=Θ`.

These remain optional hypotheses/views, not v0.4 core requirements.

A conventional projection may send:

`C → 1`,

`Θ → 1`.

This can collapse distinctions retained by a richer view.

Examples discussed in the project include:

- number density `C L^-3 → L^-3`;
- frequency-like count/cycle distinctions collapsing to `T^-1`;
- angular velocity `Θ T^-1 → T^-1`;
- torque and energy becoming dimensionally indistinguishable once the angular generator is projected away.

The doctrine is not “SI is wrong.” It is:

> **A coarser representation should not be asked to recover a distinction that its own projection erased.**

Memorable version:

> **Make angle dimensionless if you want. Just do not ask dimensional analysis to remember the distinction you erased.**

## 13. Distinction maximalism is rejected

Physical Grammar does not demand that every scientifically conceivable distinction remain explicit forever.

A Scope/task may deliberately choose a coarser representation when the discarded difference is irrelevant to the permitted questions.

Therefore:

`maximum distinction ≠ maximum correctness`.

The target is **controlled distinction**: introduce and preserve distinctions that matter; discard others explicitly and with known consequences.

## 14. Nomenclature as another view

Scientific names can lexicalize rich semantic structures, but lexical identity is not semantic identity.

Examples inherited from the v0.2 work include:

```text
Volumic(Mass) -> mass density
Specific(Energy) -> specific energy
PartWholeRatio(Mass) -> mass fraction
Rate(Position) -> velocity
Magnitude(Velocity) -> speed
MomentAbout(Force) -> torque
```

Surface morphology is not ontology. Terms such as `potential`, `flow`, `effective`, `specific`, and `intensity` may be lexically overloaded.

Preferred workflow:

1. construct an explicit semantic form;
2. validate grounding/dependencies and typed constraints;
3. choose an admissible projection/representation for the current Scope/task;
4. lexicalize into conventional terminology when useful.

> **First learn to say everything; then learn what can safely be omitted.**

## 15. Scientific-data application — non-core

The same formal pattern can later apply to data reduction:

`RawData → Corrected → ROI → Profile → PeakParameters`.

Each reduction may be modeled as a projection or transformation with explicit guarantees. A future question is answerable from a reduced archive only when it factors through the retained representation.

This suggests an application principle:

> **Preserve the distinctions required by future questions.**

Because future tasks are uncertain, long-term archival practice may rationally preserve richer/raw data and provenance. This is an application of the projection framework, not part of the v0.4 core grammar.
