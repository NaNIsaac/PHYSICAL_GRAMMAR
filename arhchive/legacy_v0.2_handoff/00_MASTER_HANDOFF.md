# 00. Master Handoff — Current State (2026-09-08)

## 0. Strategic reset

The project has moved from a broad QSF ontology program toward a narrower, testable **Physical Grammar / Physical Feature Grammar** program.

QSF remains useful as:

- the predecessor architecture;
- a source of projection/information-loss principles;
- an archive of terminology experiments;
- a domain-general shell if one is needed later.

The active research target is now:

\[
\boxed{\text{Entity-grounded Physical Feature Grammar}}
\]

Do **not** expand QSF into a universal ontology unless benchmark failure forces it.

## 1. Current research thesis

A physical or chemical expression has scientifically useful semantic structure that is richer than physical dimension but more compositional than full prose interpretation.

The current hierarchy is approximately:

\[
\boxed{
\text{Grounded Physical Semantics}
\to
\text{Feature/Kind Structure}
\to
\text{Component Tree}
\to
\text{Component Signature}
\to
\text{Physical Dimension}
}
\]

Other projections such as symbolic skeleton, conventional terminology, unit/value representation, and tensor/value structure form a **projection lattice**, not necessarily one linear ladder.

## 2. Most important semantic commitment

\[
\boxed{\textbf{No Entity grounding, no Physical Feature.}}
\]

`Mass`, `Volume`, `Position` by themselves are Feature Kinds/schemata. Actual Physical Features are things like:

\[
Mass(A),\quad Volume(A),\quad Position(A;S).
\]

An ungrounded expression such as

\[
Mass/Volume
\]

contains a quantity-kind skeleton and dimension information, but lacks enough referential structure to distinguish e.g. density from concentration.

## 3. Entity

An **Entity** is a referential unit independently identified within the current analytical Scope so that multiple Features can be co-referenced to it.

Entity boundaries follow analytical interest, not necessarily spatial partition.

Consequences:

- a person and that person's hand can both be Entities;
- Entities may overlap or nest;
- coordinate/background frames such as `S`, `S'` may be Entities in this framework;
- Entity is not synonymous with material body;
- Entity selection is Scope-relative.

## 4. Feature

A **Physical Feature** is an Entity-grounded first-class characteristic or relation carrying scientifically relevant distinction.

Feature is broader than Quantity.

Examples:

- quantitative: mass, position, count, temperature;
- categorical: material, phase, species;
- structural: shape, crystal structure;
- relational: distance, difference, relative quantity;
- collective: mean of a collection;
- field-valued/local: stress at a Site, temperature field.

A Feature can depend on multiple Entities:

\[
refs(F)\neq\varnothing.
\]

The referent set is Scope/resolution-relative.

## 5. Quantity

\[
\boxed{Quantity\subset Feature}
\]

A Physical Quantity is a Physical Feature whose Value Space has scientifically meaningful quantitative structure supporting comparison and measurement.

`numerical representation ≠ quantity`.

Sample ID `37` is numerical but not a physical quantity merely because it is a number.

## 6. Feature Kind

A Feature Kind is not just a label. It is a definition schema containing some combination of:

\[
\boxed{
\text{Entity slots}
+
\text{Value Space}
+
\text{Allowed operations/capabilities}
+
\text{Roles}
+
\text{Constraints}
}
\]

Primitive-like example:

\[
Mass: Entity\to Quantity.
\]

Derived example:

\[
\boxed{
MassDensity := \lambda e.\frac{Mass(e)}{Volume(e)}
}
\]

The repeated bound variable `e` is itself the same-Entity condition.

Concentration uses a different binding pattern:

\[
\boxed{
MassConcentration :=
\lambda c,w.\frac{Mass(c)}{Volume(w)}
\quad \text{where }PartOf(c,w)
}
\]

Deleting Entity bindings collapses both to `Mass/Volume`, then to `ML^{-3}`.

## 7. Derived Feature Kinds are constrained lambda-like definitions

Working interpretation:

\[
K := \lambda e_1\ldots e_n.\;\mathcal E
\quad\text{where }P(e_1,\ldots,e_n).
\]

This is not a claim that lambda calculus is novel. Lambda/dependent-function notation is a compact vehicle for the grammar.

The mathematically relevant analogy is closer to:

- dependent types / dependent sorts;
- generalized algebraic theories;
- partial/essentially algebraic operations;
- typed multicategory/operadic constructor composition;
- refinement predicates for cross-slot constraints.

## 8. Entity resolution changes definitional form

This is one of the strongest current ideas.

At coarse resolution:

\[
Height(Person)
\]

may be treated atomically.

At finer Site resolution:

\[
Height(Person)
\equiv
Distance(CrownSite(Person),SoleSite(Person)).
\]

At still finer Entity selection, endpoints may be promoted into distinct Entities.

Thus:

\[
\boxed{
\text{Entity granularity}
\leftrightarrow
\text{definition granularity}
}
\]

and primitive/derived status may be resolution-relative.

There need not be one absolute primitive vocabulary.

## 9. Site / Stage / Background

- **Background Entity**: Scope-level reference/background anchor.
- **Stage**: a role played by an Entity or mathematical space in a particular construction.
- **Site**: a designated location/part of a Stage; current formal status remains open (Feature-like first-class term vs distinct sort).
- **Spot**: point-like Site.
- **SurfaceSite**: surface-like Site.
- **RegionSite**: region-like Site.

`Spot ≠ coordinate`. Coordinates are representations of Sites.

`Stage` is repeatable: subject Stage and transit Stage can be distinct and connected by a map instead of equality.

## 10. Geometry and size

Use existing geometry/topology rather than reinventing it.

Working chain:

\[
Entity
\to Occupancy(E;S)
\to Boundary/Site
\to Surface
\to Area/Volume.
\]

General area/volume are measures, not universally products of extents.

\[
Area(\Sigma):=Measure_2(\Sigma),
\qquad
Volume(E):=Measure_3(Occupancy(E)).
\]

Extent is a constrained internal distance:

\[
Extent(E,u)
:=
Distance(Extreme^-_u(E),Extreme^+_u(E)).
\]

Height/width/thickness are lexicalized/specialized Extent notions.

## 11. Time / change / rate

Do not over-formalize Time internally yet. Reuse relativity, spacetime geometry, clock/synchronization theory as needed.

Current useful distinctions:

- time structure ≠ clock reading;
- timestamp ≠ duration;
- a Feature has temporal occurrences `F@t`;
- History is a family of occurrences;
- Change compares occurrences of the same grounded Feature;
- Delta is an additive specialization of Change;
- Rate is a partial constructor requiring local comparison/differential structure.

\[
Change(F;t_1,t_2)
:=Compare_K(F@t_2,F@t_1).
\]

\[
Rate(F)\sim dF/dt
\]

only where the required structure exists.

Material derivative is not treated as a magical primitive: the key distinction is which identity is held fixed (spatial Site vs material Entity), with exact chain-rule geometry delegated to continuum mechanics/differential geometry.

## 12. Generic constructor families

Current useful families, not all necessarily core primitives:

### Semantic core candidates

- Bind
- Select
- Compare
- Normalize
- Aggregate

### Analytical/mathematical constructors

- Differentiate / Rate
- Integrate
- Project
- Measure
- Gradient
- Divergence
- Curl
- TensorProduct
- Contract
- LinearAbstract

### Transport/process extension

- Crossing

### Geometric/reference families

- MomentN
- MomentAbout

### Domain mathematical transforms

- LegendreTransform and other established transforms when needed.

Do not add a constructor because it makes a list symmetric. Add it when multiple benchmarks need it.

## 13. Definition, Law, Constitutive Relation

This split is now mandatory.

### Definition

Creates/identifies a Feature Kind by semantic construction.

\[
Velocity := Rate(Position)
\]

\[
MassDensity := \lambda e.Mass(e)/Volume(e).
\]

### Physical law / balance law

Relates already meaningful Features.

Examples: Maxwell equations, momentum balance, conservation laws.

### Constitutive relation

Material/model-specific response relation.

Examples:

\[
D=\varepsilon E,
\quad J=\sigma E,
\quad \sigma=C:\epsilon,
\quad q=-k\nabla T.
\]

### Model-dependent relation

Do not silently promote `F=ma`, `p=mv`, `E=mv^2/2` into universal semantic definitions.

## 14. Fields and tensors

A Field is a Site-indexed family of Features:

\[
Field[F;D]:p\mapsto F(p).
\]

`Field` and `Tensor` are orthogonal structures: a stress field is a field of second-order tensor-valued Features.

Tensor order should be **derived from semantic/geometric slots whenever possible**, not stored only as an unexplained integer.

Stress example:

\[
t(n)=\sigma n.
\]

Thus stress is a linear map from surface normal/direction input to traction-vector output, giving a second-order tensor representation.

Linear response generalization:

\[
L:X\to Y,\qquad L\in Y\otimes X^*.
\]

Input/output tensor orders often explain the response coefficient order:

- vector → vector: rank/order 2 conductivity/permittivity-like tensor;
- vector → symmetric rank-2: order 3 piezoelectric-like tensor;
- rank-2 → rank-2: order 4 stiffness/viscosity-like tensor.

Symmetry can reduce independent parameters without reducing tensor order.

## 15. Balance / conservation grammar

Balance is a **Law Schema**, not a Definition.

Integral form:

\[
Rate(Content_Q(R))
=
-NetOutflow_Q(\partial R)+Production_Q(R).
\]

Local form after localization/Gauss:

\[
\partial_t \rho_Q + \nabla\cdot J_Q=s_Q.
\]

Conservation is Balance with zero production/source.

Under conventional tensor representation, transport of an order-`r` local quantity commonly introduces one oriented-surface transport slot:

\[
ord(Flux_Q)=ord(Q)+1,
\qquad
ord(Div(Flux_Q))=ord(Q).
\]

This explains scalar-density → vector-flux and vector-momentum → second-order momentum-flux structures. Treat this as a representation rule with geometry/formalism caveats, not a universal metaphysical theorem.

## 16. Electrodynamics stress-test result

Maxwell's equations fit cleanly when separated into:

1. grounded Field Features (`E,B,D,H,J,...`);
2. mathematical constructors (`Boundary`, line/surface integrals, Curl, Divergence, Rate);
3. Field Laws (Faraday, Gauss, Maxwell–Ampère);
4. constitutive relations (`D=εE`, `B=μH`, `J=σE`) where valid.

Integral ↔ differential forms share genealogy through Stokes/Gauss localization while preserving Region/Boundary dependency.

Important correction: current density `J` is a local charge-flux density; surface integration gives current. Do not define `J = Flux(Current)`.

## 17. Continuum mechanics stress-test result

Reference and current configurations are **configurations/Stages of the same material Entity**, not automatically separate Scopes.

Motion:

\[
\chi_t:\mathcal B_0\to\mathcal B_t.
\]

Finite deformation begins from deformation gradient `F=∂x/∂X`; infinitesimal strain is only a specialization.

Material derivative distinction is captured by held-fixed identity / pullback along motion.

Cauchy momentum:

\[
\rho Dv/Dt = \nabla\cdot\sigma + f_{body}.
\]

Stress enters balance independently of its constitutive relation to strain.

## 18. Moments and potentials

Moment families compress many named quantities.

\[
Moment_n(Q;o)=Aggregate(r_o^{\otimes n}\otimes Q).
\]

Examples:

- total quantity: zeroth moment;
- center of mass: normalized first mass moment;
- inertia tensor: geometric transform of second mass moment;
- electric dipole/quadrupole: charge moments;
- torque: `MomentAbout(Force)`;
- angular momentum: `MomentAbout(Momentum)`.

`Potential` is lexical overload, not one universal constructor:

- differential field potential (`Gradient`, `Curl`, exterior derivative/gauge structure);
- potential-energy normalization (`U/q`, `U/m`);
- thermodynamic potentials via Legendre transforms;
- conjugate quantities via constrained partial derivatives.

## 19. Projection / information loss

Central principle inherited from QSF:

> Same is not a property. It is a projection.

Important projection:

\[
\lambda e.\frac{Mass(e)}{Volume(e)}
\to
Mass/Volume
\to
ML^{-3}.
\]

The first map deletes Entity binding; the second deletes most semantic constructor identity.

Dimension is not wrong. It is a successful, intentionally coarse projection.

Optional richer dimensions may retain Count `C` or Angle `Θ`, then project to conventional SI dimensionless treatment.

## 20. Validation program

Freeze the grammar **before** testing.

Use a hidden 50–100 term corpus across mechanics, electromagnetism, thermodynamics, continuum mechanics, chemistry, radiation physics, metrology, acoustics, spectroscopy.

Classify reducibility:

- G0: generic grammar derives it;
- G1: generic external mathematics needed;
- G2: one domain-specific semantic seed needed, then grammar composes it;
- G3: model/law dependent;
- G4: current grammar fails / new mechanism required.

Adversarial sets should hold dimension or arithmetic skeleton fixed and vary Entity/Role structure.

The most important negative result is a repeated G4 pattern that demands one reusable new mechanism.

## 21. Research positioning

Do not claim to invent lambda calculus, dependent types, tensor calculus, dimensional analysis, mereotopology, or physical laws.

Candidate contribution:

> an Entity-grounded generative grammar that makes referential binding, constructor genealogy, value/tensor structure, and controlled projections explicit for scientific Feature/Quantity definitions and nomenclature.

Potential strongest demonstrations:

- density vs concentration despite identical `M/V` skeleton;
- size vs distance under Entity/Site refinement;
- integral ↔ differential Maxwell forms preserving Region/Boundary genealogy;
- Eulerian ↔ Lagrangian/material derivative as held-fixed identity distinction;
- stress tensor order generated from directional input/traction output;
- conservation/balance as a reusable law schema;
- same lexical morpheme `potential` resolving to multiple semantic families;
- blind reconstruction with minimal domain knowledge.

## 22. Immediate next work

1. Freeze Physical Grammar v0.2 syntax and current constructor list.
2. Build 50–100-term blind benchmark.
3. Keep already-discussed density/flux/stress examples in training/development, not hidden test.
4. Stress-test quantum/classical correspondence, thermodynamics, waves/acoustics, spectroscopy.
5. Prototype parser/checker only after benchmark annotation format is stable.
