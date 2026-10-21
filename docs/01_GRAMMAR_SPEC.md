# Physical Grammar v0.4 Candidate — Compact Grammar Specification

## 1. Primitive semantic categories

### 1.1 Scope

A **Scope** determines which distinctions are relevant, which referents are independently tracked, and at what resolution the analysis is performed.

> **Scope changes representation, not physical truth.**

Equivalent boundary statement:

> **Scope chooses relevance; it does not manufacture truth.**

No universal internal tuple representation of Scope is frozen in v0.4.

### 1.2 Entity

An **Entity** is a unit of reference distinguished for independent treatment within a given Scope.

Entity is referential, not necessarily material. Entities may overlap, nest, be constructed, or be reified from relations/patterns when the Scope needs stable reference to them.

Examples: particle, person, hand, crystal, region, boundary, site, process, state, interaction, mode, reference frame.

### 1.3 Property

Within Physical Grammar, a **Property** is represented as a typed physical characterization with Entity slots and semantic structure sufficient for grounding and composition.

Examples:

`Mass[A]`

`Distance[A,B]`

`Temperature[System,Site,Time]`

`Force[Source,Target]`

The formalism does not require Property to be unary ownership.

### 1.4 EntityMap

An **EntityMap** constructs or selects an Entity from one or more Entities:

`M : E1 × ... × En → E'`

Examples:

`ArmOf[Person] → Arm`

`Boundary[Region] → BoundaryEntity`

`System[A,B] → SystemEntity`

`Interaction[A,B] → InteractionEntity`

`OccupiedRegion[A] → Region`

EntityMaps make referential genealogy explicit.

### 1.5 Physical Expression

A **Physical Expression** is a typed expression built from grounded/open Properties, EntityMaps, constants, parameters, coordinates, mathematical constructors, semantic relations, and admissible representation/projection nodes.

Not every expression is itself a named Property.

### 1.6 Distinction is not a primitive node

`Distinction` is an organizing concept used to explain what Scope, grounding, composition, representation, and projection do. v0.4 does **not** add a `Distinction` AST object or type.

## 2. Application and grounding

### Rule G1 — Entity application

`X[E1,...,En]`

means application of Entities to Entity slots.

### Rule G2 — Property grounding

If `P` is a Property, `P[E1,...,En]` is grounding.

### Rule G3 — Partial grounding

A multi-Entity Property may be partially grounded:

`Force[A]`

which denotes a Property family awaiting the remaining Entity slot(s).

This is mathematically analogous to currying/partial application but receives a physical interpretation as sequential grounding.

### Rule G4 — Entity mapping

If `M` is an EntityMap, `M[E1,...,En]` returns an Entity rather than a Property.

Return type, not bracket shape, distinguishes grounding from Entity construction.

## 3. Entity dependency discipline

### 3.1 Grounding Continuity

In a preferred definition or law, grounding dependencies introduced on the left should remain traceable through the right-hand expression, unless explicitly bound, eliminated, or supplied by context.

Example:

`MassDensity[A] := Mass[A] / Volume[OccupiedRegion[A]]`

`A` remains traceable through the EntityMap chain.

### 3.2 Grounding Closure

Every Entity dependency in a well-formed expression must be one of:

1. focal/free grounding;
2. derived grounding through an EntityMap;
3. bound grounding under integration, summation, or quantification;
4. explicitly eliminated grounding through normalization, invariance, marginalization, or another typed reduction;
5. context grounding fixed by Scope/header.

Otherwise the expression contains an **Unresolved Entity Dependency**.

Example error:

`K[A] = 1/2 Mass[B] Speed[A]^2`

unless `B` is explicitly related to `A` or supplied by context.

This preserves the v0.3 static discipline:

`value/type checking + dimension checking + Entity-dependency checking`.

## 4. Composition rules

### 4.1 EntityMap composition

`A → M[A] → N[M[A]]`

preserves Entity genealogy.

### 4.2 Mathematical constructors

Mathematical operators act on suitable Property/quantity representations and carry typing rules.

Examples:

- multiplication combines compatible value structures and reconciles Entity dependencies;
- derivative generally preserves focal grounding while changing differential/value structure;
- gradient introduces/uses Site dependence while preserving bearer genealogy;
- integral/sum may bind and eliminate local Entity dependencies;
- normalization may intentionally eliminate selected dependencies;
- projection may intentionally discard semantic distinctions under an explicit contract.

### 4.3 Definition, law, constraint, constitutive relation

These are distinct semantic relations in the IR.

- `Definition(A,B)` establishes semantic construction/definition.
- `Equality(A,B)` asserts mathematical equality in the applicable mathematical context.
- `Law(...)` records a physical law/model relation.
- `Constraint(...)` records admissibility or held-fixed/restriction semantics.
- `ConstitutiveRelation(...)` records model-dependent response structure.

Surface syntax may continue to use conventional `=` where physics does. The parser/IR should classify the semantic node from context/annotation rather than inventing a new visible symbol for every relation.

## 5. Property granularity and reification

Entity granularity and Property definition granularity are dual design choices.

Fine representation:

`A := ArmOf[Person]`

`Position[A]`

Coarse representation:

`ArmPosition[Person] := Position[ArmOf[Person]]`

These are alternative factorizations of a semantic graph.

A relation, pattern, absence, decomposition component, or process may be reified as an Entity when repeated independent reference makes that factorization useful. Reification is Scope-relative, not a universal ontological claim.

## 6. Spatial and temporal semantics

### 6.1 Site before coordinate

Prefer distinguishing a Site Entity from its coordinate representation:

`SiteOf[Target] → Site`

`Coordinate[Site,ReferenceFrame] → vector representation`

Coordinate change should not change Site identity.

### 6.2 Relative position

Position is naturally treated as a reference-conditioned relation:

`RelativePosition[A,R]`

Binding the reference frame yields a familiar position family.

`Distance[A,B] := Norm(RelativePosition[A,B])`

Velocity and acceleration are derivatives of reference-conditioned position.

### 6.3 State/configuration

Reference and current configurations in continuum mechanics can be represented as Stages/configurations associated with the same material Entity. Material derivatives preserve material identity while changing configuration/time representation.

## 7. Fields, tensors, and local projections

Field and tensor are orthogonal notions.

A field is a Site-indexed family:

`Temperature[System,Site]`

A tensor describes value structure:

`Stress[Body,Site]` may have second-order tensor structure.

Example value projection chain:

`StressTensor[x] → Traction[x,n] → NormalStress[x,n]`

with conventional mathematics such as `t(n)=σ n` and `p_n = -n·σ n` where the chosen sign convention applies.

Such local projections do not imply that every representation relation lies on one global ladder.

## 8. Balance and transport

Generic balance schema:

`Rate(Content_Q[Region]) = -Outflow_Q[Boundary[Region]] + Production_Q[Region]`

Local and integral forms should preserve Region/Boundary genealogy under Gauss/Stokes transformations.

Current density is a local charge-flux-density Property; integrating it over a surface produces current through that surface. Similar grammar may apply to mass, heat, momentum, etc., while constitutive relations remain domain-specific.

## 9. Quantity interface and VIM alignment

Physical Grammar preserves VIM terminology where practical.

Do not identify:

`Quantity = Quantity Value = Numerical Quantity Value`.

A grounded Property may admit a VIM-compatible Quantity view.

`Quantify(P) → Quantity`

`Q(P)` is the short surface notation for this operation.

`Quantify` is not defined as “return a number with a unit”. It exposes/lowers a Property into a quantity structure when such a structure is admissible.

The actual quantity value and measurement result belong to later layers.

A non-quantifiable Property may instead support nominal, structural, geometric, categorical, distributional, or other representations.

## 10. Representation and projection

### 10.1 Representation

`Represent[X,R]`

selects an admissible representation/encoding/coordinate form of `X`.

Examples:

`Represent[Orientation[A], Quaternion]`

`Represent[Orientation[A], RotationMatrix]`

Some representations are information-preserving over a declared domain.

### 10.2 Projection

A **Projection** is a typed information-reducing map when used in the v0.4 semantic sense:

`π : X → Y`.

Projection is not merely “another notation”. It declares that some distinctions present in `X` are not represented in `Y`.

### 10.3 Representation ≠ Projection

A reversible or lossless coordinate/encoding change should not be classified as an information-losing projection merely because the surface form changes.

A representation operation may internally contain projections if the target representation is lossy; that loss must be explicit in its contract.

## 11. Projection and equivalence rules

### Rule P1 — Projection-induced indistinguishability

`A ~_π B  iff  π(A)=π(B)`.

This is the equivalence relation induced by the fibers/kernel of the map `π`.

### Rule P2 — No universal unqualified Same

Physical Grammar does not add a universal `Same(A,B)` operator.

Mathematical equality, structural equivalence, projection equivalence, task-relative equivalence, dimensional equality, lexical identity, and other criteria must remain distinguishable in the IR or surrounding annotation.

### Rule P3 — Projection/refinement graph

Information-reducing projection/refinement relations may be organized as a DAG/partial-order-like structure where appropriate.

General representation transformations are not required to form a DAG; reversible transforms may create cycles in the general representation graph.

### Rule P4 — Projection validity principle

For `π:X→Y` and downstream question/observable `P:X→Z`, `π` is sufficient for `P` when

`P = P̄ ∘ π`

for some `P̄:Y→Z`.

Interpretation: `P` does not depend on distinctions erased by `π`.

This is a semantic criterion, not a complete automatic-decision algorithm.

### Rule P5 — Exact versus approximate substitutability

A provisional exact task-relative equivalence may be written:

`A ~_T B`.

If a task `T` declares a fixed observable set `O_T`, one formalization is:

`A ~_T B  iff  ∀P∈O_T, P(A)=P(B)`.

Approximate substitutability must use distinct notation:

`A ≈_{T,ε} B`.

A tolerance relation need not be transitive; therefore it must not be casually called an equivalence relation.

The exact status of `Task` as a core grammar object is **provisional** in v0.4.

## 12. Projection contracts

Projection contract machinery is provisional.

Preferred direction:

`Preserves(π,I)`

records a positive guarantee that invariant/observable/property `I` remains available after projection.

Diagnostic metadata may include non-exhaustive known losses:

```text
DimensionProjection

guarantees:
    physical dimension

known_losses:
    Entity grounding
    semantic construction/history
    selected semantic roles
```

`known_losses` is explanatory and is not required to enumerate everything erased by `π`.

## 13. Static semantics

v0.4 retains three established checks and adds one provisional family.

### Established

- **Type check:** is the operation admissible for the typed operands/value structures?
- **Dimension check:** is quantitative dimensional structure consistent?
- **Entity dependency check:** are referential dependencies traceable, bound, derived, explicitly eliminated, or supplied by Scope?

### Provisional

- **Projection validity check:** does a downstream operation require a distinction that the chosen projection no longer guarantees?

A practical checker may conservatively return:

`safe | unsafe | unknown`.

A possible diagnostic style:

```text
ProjectionError:
    requested distinction: semantic construction
    unavailable after: DimensionProjection
```

`use-after-projection` is an implementation metaphor, not a new semantic primitive.

## 14. Surface syntax summary

- `P[A,B]` — Entity application; grounding when `P` is a Property.
- `M[A,B]` — EntityMap application when `M` returns Entity.
- `f(x,y)` — ordinary mathematical/value application.
- `P<α>` — provisional parameter specialization notation.
- `:=` — surface definition marker.
- `=` — conventional mathematical/physical equality notation; IR relation type must be classified contextually.
- `Q(P[A])` — Quantify: Property → VIM-compatible Quantity view, when admissible.
- `Represent[X,R]` — representation selection.
- `π(X)` or a named projection — typed information-reducing map.
- `~_π` — projection-induced equivalence.
- `~_T` — provisional exact task-relative equivalence.
- `≈_{T,ε}` — provisional approximate task-relative substitutability.

## 15. Non-goals

Physical Grammar does not aim to:

- replace SI/VIM metrology;
- replace dimensional analysis;
- replace tensor calculus, differential geometry, probability theory, or established mathematics;
- force every relation into a Property;
- turn every relation into an Entity;
- provide a universal ontology of reality;
- create a `Distinction` ontology;
- create one universal `Same` relation;
- compute an exhaustive `Lost(π)` set;
- define a universal semantic distance;
- guarantee complete automatic factorization checking;
- make every semantically valid expression numerically executable.
