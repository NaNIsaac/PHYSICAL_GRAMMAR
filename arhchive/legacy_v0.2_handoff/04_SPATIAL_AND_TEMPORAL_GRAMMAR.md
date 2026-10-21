# 04. Spatial and Temporal Grammar

## A. Spatial grammar

### 1. Background / Stage

A named spatial frame/background `S` may be an Entity. In a construction it plays the `Stage` or `Reference` role.

Associated Features may include:

\[
Origin(S),\quad Orientation(S),\quad Metric(S),\quad Geometry(S).
\]

Do not make `Stage` a huge ontology hierarchy.

### 2. Occupancy

\[
Occupancy(E;S)
\]

is the Site/Region occupied by Entity `E` in Stage `S`.

`Occupancy` is deliberately more general than a hardcoded Euclidean `SpatialRegion`.

### 3. Site

A Site is a first-class designated part/location of a Stage.

Working families:

- Spot — point-like Site;
- CurveSite;
- SurfaceSite;
- RegionSite.

Exact formal status remains open: Site may become a distinct sort or a structured Feature-like term.

### 4. Boundary and Surface

Use existing topology/mereotopology:

\[
Boundary(E;S):=\partial Occupancy(E;S).
\]

A boundary surface is a special SurfaceSite selected from that boundary.

But not every SurfaceSite is a material boundary: measurement/control surfaces can be arbitrary embedded surfaces.

### 5. Distance

Canonical distance acts on Sites/points, not vague bare Entities:

\[
Distance(p,q;S)=d_S(p,q).
\]

`Distance(A,B)` is shorthand requiring an implicit/explicit Site selector such as center or reference point.

### 6. Extent / size

\[
Extent(E,u;S)
:=
Distance(Extreme^-_u(E),Extreme^+_u(E);S).
\]

Height, width, thickness, diameter are specialized/lexicalized Extent notions subject to geometry and convention.

This explains how one observable can be described as a single-Entity size Feature or a distance between finer Sites/Entities depending on Scope.

### 7. Area and Volume

General definitions are measure-based:

\[
Area(\Sigma)=Measure_2(\Sigma),
\qquad
Volume(E)=Measure_3(Occupancy(E)).
\]

`width × height` and `x × y × z` are special formulas, not universal definitions.

## B. Temporal grammar

### 8. Time structure vs clock value

Do not identify:

- temporal ordering/structure;
- coordinate time;
- clock reading;
- duration;
- proper time.

The exact physics of synchronization and relativity is delegated to established spacetime theory.

### 9. Feature occurrence

A grounded Feature may have temporal occurrences:

\[
Occurrence(F,t)\equiv F@t.
\]

History:

\[
History(F): t\mapsto F@t.
\]

### 10. Change

General Change compares occurrences:

\[
Change(F;t_1,t_2)
:=
Compare_K(F@t_2,F@t_1).
\]

Required constraints typically include same grounded Feature identity and temporal ordering.

Additive specialization:

\[
Delta(F;t_1,t_2)=F@t_2-F@t_1.
\]

Thus `Change` is not simply generic subtraction.

### 11. Rate

Rate is partial:

\[
Rate(F)=dF/dt
\]

only if the Feature/value structure supports local comparison and differentiation.

This distinguishes a categorical phase transition from a differentiable mass/position history.

### 12. Position, velocity, acceleration

\[
Velocity(E;S):=Rate(Position(E;S))
\]

\[
Acceleration(E;S):=Rate(Velocity(E;S)).
\]

Curved spaces may require comparison maps/parallel transport; delegate exact implementation to differential geometry.

### 13. Eulerian vs Lagrangian/material

For a field `f(x,t)`:

- Eulerian/spatial rate: hold spatial Site `x` fixed;
- material rate: hold material Entity/label `X` fixed and evaluate along motion `x=χ(X,t)`.

The material derivative is therefore modeled as a **held-fixed / pullback-along-motion distinction**, with chain-rule details imported from continuum mechanics.
