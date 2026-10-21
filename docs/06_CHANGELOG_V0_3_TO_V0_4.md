# Changelog — v0.3 Candidate to v0.4 Candidate

## 1. Version intent

v0.4 is an integration release, not an ontology expansion.

`v0.4 = v0.3 Entity/Property kernel + v0.2 Projection/Equivalence restoration + minimal formal bridge`.

## 2. Preserved unchanged in spirit from v0.3

- Physical Grammar remains a typed compositional physical-semantic IR.
- Scope remains the analytical context for relevant distinctions, tracked referents, and resolution.
- Entity remains the first-class referential unit.
- Square brackets remain Entity application; Property + Entity application is grounding.
- EntityMap remains `E^n → E` and carries referential genealogy.
- Grounding Continuity and Grounding Closure remain core.
- Entity-dependency checking remains a static-semantic pillar beside type/value and dimension checks.
- Feature → Property migration remains in force as a strong candidate.
- Feature Kind remains demoted.
- `Quantity ⊂ Feature` remains retired as a core statement.
- `Quantify` remains a VIM-compatible Property → Quantity bridge/view.
- Quantity, Quantity Value, and measurement result remain distinct.
- Site identity remains distinct from coordinate representation.
- Definition, law, constitutive relation, and representation remain semantically distinct.

## 3. Restored from v0.2 projection work

The following v0.2 principles are restored to the canonical body:

- richer semantics can be lowered through multiple information-reducing views;
- each projection induces an equivalence relation on its source;
- semantic constructor tree, component signature, physical dimension, symbolic skeleton, lexical form, etc. are distinct views;
- these views need not lie on one universal total order;
- do not use one unqualified `same` judgment;
- optional rich count/angle dimensions may be projected to conventional dimensionless views;
- nomenclature is a lexicalization/view, not ontology itself;
- explicit-first, compress-later remains the preferred low-context policy.

## 4. New formal bridge in v0.4

### Projection-induced equivalence

`A ~_π B  iff  π(A)=π(B)`.

### Factorization safety criterion

For `π:X→Y` and `P:X→Z`, the reduced representation is sufficient for `P` when

`P=P̄∘π`

for some `P̄:Y→Z`.

This is interpreted as independence from distinctions erased by `π`.

### Exact versus approximate relations

- exact task-relative equivalence: provisional `~_T`;
- approximate substitutability: provisional `≈_{T,ε}`;
- tolerance relations are not assumed transitive.

### Projection validity checking

Added as a provisional static-semantics target with no completeness promise.

## 5. Clarified representation architecture

v0.4 freezes:

> **Representation ≠ Projection.**

A lossless coordinate/encoding change and an information-losing reduction are distinct semantic operations.

The architecture now distinguishes:

- a general representation graph, possibly reversible/cyclic;
- an information/refinement DAG for directed lossy lowerings.

## 6. New design principles

Project principle:

> **Make scientific distinctions explicit.**

Design principle:

> **Construct distinctions explicitly; erase them explicitly.**

Safety principle:

> **Loss is allowed; dependence on lost distinctions is not.**

Provocative slogan, explicitly non-axiomatic:

> **Same is not a property. It is a projection.**

## 7. Explicitly rejected/delayed in v0.4

v0.4 does not add:

- a `Distinction` AST object/type;
- a universal `Same` operator;
- exhaustive `Lost(π)` analysis;
- a detailed Scope tuple;
- universal semantic distance;
- complete automatic factorization checking.

## 8. Benchmark consequence

The next step after documentation freeze is not additional philosophy. It is blind validation:

`grammar freeze → hidden multi-domain benchmark → failure taxonomy → minimal revision`.

Projection validity and recoverability are added to the benchmark record alongside Entity signature, construction tree, genealogy, quantity/representation status, dimension, and reducibility grade.
