# 18. Worked Vocabulary Reference

This is a compact, non-normative vocabulary table.

| Term | Current grammar form | Notes |
|---|---|---|
| Mass | `Mass(e)` | seed Quantity Kind |
| Material | `Material(e)` | non-quantitative Feature |
| Count | `Count(x,e)` | counted-kind + bearer Entity |
| Position | `Position(e;s)` | subject + Stage/reference |
| Occupancy | `Occupancy(e;s)` | Site/Region occupied by Entity |
| Distance | `MetricDistance(p,q;s)` | acts canonically on Sites |
| Extent | `Distance(Extreme-(e,u), Extreme+(e,u))` | single-Entity size as internal distance |
| Height | `Extent(e,vertical)` | lexicalized Extent |
| Surface | `SurfaceSite(Σ;s)` | not necessarily a material boundary |
| Boundary surface | `SurfacePart(Boundary(Occupancy(e;s)))` | specialization |
| Area | `Measure2(Σ)` | measure-based |
| Volume | `Measure3(Occupancy(e))` | measure-based |
| Mass density | `λe. Mass(e)/Volume(e)` | same-Entity normalization |
| Number density | `λe. Count_x(e)/Volume(e)` | same-Entity normalization |
| Specific energy | `λe. Energy(e)/Mass(e)` | specific family |
| Mass fraction | `λp,w. Mass(p)/Mass(w) where PartOf(p,w)` | part/whole ratio |
| Mass concentration | `λp,w. Mass(p)/Volume(w) where PartOf(p,w)` | part/whole normalization |
| Difference | `Compare_additive(F1,F2)` | compatibility required |
| Relative difference | `(Q(a)-Q(r))/Q(r)` | reference Role matters |
| Change | `Compare(F@t2,F@t1)` | same grounded Feature across occurrences |
| Delta | `F@t2-F@t1` | additive Change specialization |
| Rate | `Differentiate(F,time)` | partial constructor |
| Velocity | `Rate(Position)` | definition-like |
| Acceleration | `Rate(Velocity)` | definition-like |
| Speed | `Magnitude(Velocity)` | projection |
| Current | `Rate(Crossing(Charge,Σ))` | surface-grounded current |
| Fluence | `Crossing(Count,Σ)/Area(Σ)` | areal cumulative crossing |
| Flux | `Rate(Fluence)` / local flux field | exact form context-dependent |
| Field | `p -> F(p)` | Site-indexed family |
| Stress | `LinearAbstract_n(Traction(n))` | second-order tensor-valued local Feature |
| Pressure | isotropic coefficient of stress | scalar; `σ=-pI` in hydrostatic case |
| Strain | geometric measure derived from deformation | family; infinitesimal/finite variants |
| Deformation gradient | `∂x/∂X` | reference→current configuration map derivative |
| Material derivative | derivative along material motion | held-fixed Entity vs Site distinction |
| Heat capacity | domain-seeded derivative/process response | not merely bare `Energy/Temperature` |
| Specific heat capacity | `Specific(HeatCapacity)` | generic after seed |
| Molar heat capacity | `Molar(HeatCapacity)` | generic after seed |
| Torque | `MomentAbout(Force)` | reference Site/axis required |
| Angular momentum | `MomentAbout(Momentum)` | model/domain momentum seed |
| Center of mass | normalized first mass moment | refinement-dependent aggregate |
| Inertia tensor | geometric transform of second mass moment | not identical to raw second moment |
| Electric dipole moment | first charge moment | reference/origin convention matters |
| Field potential | `P such that D(P)=Field` | derivative/gauge family |
| Electric potential | field-potential and/or energy-per-charge relation | context/model distinctions needed |
| Chemical potential | constrained derivative of thermo potential | thermodynamic conjugate family |
| Thermodynamic potential | Legendre-transform family | external thermodynamics |
| Conductivity | constitutive response map `E -> J` | tensor order from input/output |
| Permittivity | constitutive response map `E -> D` | scalar only in simple isotropic case |
| Stiffness | constitutive response map `strain -> stress` | order 4 in standard representation |
| Piezoelectric coefficient | vector↔rank2 response map | order 3 in standard representation |
| Balance law | accumulation = -outflow + production | law schema |
| Conservation law | Balance with zero source/production | specialization |
