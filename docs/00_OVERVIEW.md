# Physical Grammar v0.4 Candidate — Overview

**Status:** integration draft, 2026-09-08  
**Primary aim:** a typed, compositional physical-semantic Intermediate Representation (IR).

## 1. Core thesis

Ordinary physical notation is excellent for calculation but often suppresses what a property is grounded in, which dependencies are carried through composition, and which distinctions have been deliberately discarded by a chosen representation.

Physical Grammar therefore works in two complementary directions.

### Semantic construction

`Scope → Entity → Property/Grounding → Composition/Genealogy → Rich Physical Semantics`

This direction introduces and preserves scientifically relevant referential and semantic structure.

### Controlled reduction

`Rich Physical Semantics → Projection / refinement views → coarser representations`

This direction deliberately removes distinctions while recording what the chosen view still guarantees.

> **Physical Grammar is a typed compositional semantic IR that represents physical Properties through explicit Entity grounding and preserves their semantic dependencies through composition.**

The higher-level design principle is:

> **Physical Grammar makes scientific distinctions explicit—how they are introduced, preserved, composed, represented, and selectively discarded.**

`Distinction` is organizing language for the architecture, not a new primitive semantic category.

## 2. Scope and relevance

A **Scope** determines which referents are independently tracked, which distinctions are relevant, and at what resolution the analysis is performed.

> **Scope chooses relevance; it does not manufacture truth.**

Changing Scope may change which representation is sufficient or useful. It does not make arbitrary physical claims true.

This gives the overall architecture:

`Scope → Semantic Construction → Controlled Reduction`

## 3. Entity-grounded kernel

Physical Grammar retains the v0.3 kernel.

> **Entity: a unit of reference distinguished for independent treatment within a given Scope.**

Entityhood is referential, not necessarily material. A body, region, boundary, site, process, state, interaction, mode, frame, or constructed system may be an Entity when the analysis requires stable reference to it.

A **Property** is represented as a typed physical characterization with Entity slots and semantic structure sufficient for grounding and composition.

Examples:

`Mass[A]`

`Distance[A,B]`

`Temperature[System,Site,Time]`

`Force[Source,Target]`

An **EntityMap** constructs or selects an Entity from Entities and preserves referential genealogy:

`A → OccupiedRegion[A] → Volume[OccupiedRegion[A]]`.

Thus:

`MassDensity[A] := Mass[A] / Volume[OccupiedRegion[A]]`

retains more semantics than the ungrounded skeleton `Mass/Volume`, which in turn retains more than the physical dimension `M L^-3`.

## 4. Projection is a core concept, not a minor constructor

v0.4 restores projection as a first-class part of the architecture.

A projection

`π : X → Y`

may intentionally make distinct objects indistinguishable in the target representation.

The induced equivalence is:

`A ~_π B  iff  π(A) = π(B)`.

This does **not** mean every form of sameness is a projection. Mathematical equality, identity, structural equivalence, projection-induced indistinguishability, and task-relative substitutability remain distinct semantic relations.

Projection/refinement relations are modeled as a **Directed Acyclic Graph (DAG)** or partial-order-like structure where appropriate, not as one universal lowering ladder. General representation morphisms may form a graph with reversible paths; the DAG applies to the information-order/refinement view.

## 5. Representation is not projection

`Represent` covers changes of representation that may preserve the relevant semantics.

Examples:

`Represent[Orientation[A,R], RotationMatrix]`

`Represent[Orientation[A,R], Quaternion]`

These can be alternative encodings/coordinate representations of the same orientation structure, subject to their mathematical domains and conventions.

By contrast:

`RichSemantics → Dimension`

is information-losing: Entity grounding, construction history, role information, and other distinctions may disappear.

Therefore:

> **Representation ≠ Projection.**

Some representation changes are lossless; some are lossy projections. The IR must type them differently.

## 6. Projection validity and factorization

Let

`π : X → Y`

be a projection and

`P : X → Z`

be a question, observable, prediction, or downstream operation.

The projection is sufficient for `P` when there exists

`P̄ : Y → Z`

such that

`P = P̄ ∘ π`.

Interpretation:

> `P` does not depend on distinctions erased by `π`.

This yields the safety principle:

> **Loss is allowed; dependence on lost distinctions is not.**

This is a semantic validity principle, not a promise that a checker can decide all factorization questions automatically. A future checker may conservatively return `safe`, `unsafe`, or `unknown`.

## 7. Qualified sameness

Physical Grammar rejects one unqualified `same` judgment.

Ask instead whether two objects have:

- mathematical equality;
- structural equivalence/isomorphism;
- the same grounded semantics;
- the same Entity-binding graph;
- the same constructor structure;
- the same component signature;
- the same physical dimension;
- the same symbolic skeleton;
- the same conventional name;
- projection-induced indistinguishability;
- task-relative substitutability.

The exact projection-induced relation is:

`A ~_π B  iff  π(A) = π(B)`.

A provisional exact task-relative relation may be defined by a declared observable set `O_T`:

`A ~_T B  iff  for every P in O_T, P(A)=P(B)`.

Approximate substitutability must use separate notation, for example:

`A ≈_{T,ε} B`,

because tolerance-relative closeness is generally not transitive and therefore need not be an equivalence relation.

## 8. Angle as doctrine example

A richer internal view may provisionally retain an angle generator `Θ`. A conventional projection can send

`Θ → 1`.

Under that projection, distinctions visible to an angle-aware dimensional system may disappear; torque and energy can then share the same dimensional signature.

Physical Grammar does not conclude that the conventional projection is wrong. It concludes only that the chosen dimension view no longer remembers that distinction.

> **Make angle dimensionless if you want. Just do not ask dimensional analysis to recover the distinction you erased.**

Likewise, if a declared Scope/task does not require a distinction between two otherwise distinct families, a coarser representation may intentionally identify them. Maximum distinction is not the goal; controlled distinction is.

## 9. VIM boundary

Physical Grammar does not replace VIM/metrology. It keeps the v0.3 division of labor:

`Scope → Entity → Property grounding/composition → Quantify/Represent → Quantity or other representation`

VIM terminology for Quantity, Quantity Value, Numerical Quantity Value, measurand, and measurement result is retained where applicable.

`Quantify` is a bridge/view from admissible Property semantics to a VIM-compatible Quantity structure, not shorthand for “return a number × unit”.

## 10. Research question

The empirical question remains grounded and testable:

> **How much physical-property semantics can be reconstructed from explicit Entity grounding, a small generic constructor grammar, and controlled projections before domain-specific knowledge is required?**

v0.4 adds a second validation dimension to the v0.3 question:

> **Which distinctions are preserved or collapsed by each admissible projection, and are downstream questions valid on that reduced representation?**

## 11. Non-goals

Physical Grammar does not aim to:

- replace SI/VIM metrology;
- replace dimensional analysis;
- replace established mathematics;
- provide a universal ontology of reality;
- maximize semantic detail at all costs;
- force every representation into one hierarchy;
- define one universal notion of sameness;
- guarantee complete static proof of projection validity.
