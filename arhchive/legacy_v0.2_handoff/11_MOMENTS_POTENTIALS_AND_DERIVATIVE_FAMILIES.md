# 11. Moments, Potentials, Derivative Families

## A. Moment families

### 1. Distribution moment

For distributed Feature `Q` relative to reference Site `o`:

\[
Moment_n(Q;o)
=
Aggregate(r_o^{\otimes n}\otimes Q).
\]

This is a higher-order constructor family combining reference, displacement, tensor product, and aggregation.

### 2. Zeroth / first / second

- zeroth moment → total/aggregate quantity;
- first mass moment normalized by total mass → center of mass;
- second mass moment → precursor to inertia tensor via a geometric transform;
- first charge moment → dipole moment;
- higher charge moments → multipole families, with trace/symmetry conventions delegated to multipole theory.

### 3. MomentAbout

For localized vector-like Feature:

\[
MomentAbout(Q;O)=r_O\times Q.
\]

Examples:

\[
Torque=MomentAbout(Force),
\]

\[
AngularMomentum=MomentAbout(Momentum).
\]

Keep distribution moments and cross-product moments as related but not forcibly identical constructors.

## B. Potential families

`Potential` is a major lexical-overload benchmark.

### 4. Differential field potential

A potential may be an object whose derivative generates a field:

\[
D(P)=F.
\]

Examples include scalar and vector potentials under gradient/curl/exterior-derivative structures.

Gauge non-uniqueness means multiple potential representations may map to the same field.

### 5. Potential energy normalized by carrier

Examples:

\[
ElectricPotential\sim PotentialEnergy/Charge
\]

\[
GravitationalPotential\sim PotentialEnergy/Mass.
\]

This reuses NormalizeBy but should not be confused with every field-potential definition.

### 6. Thermodynamic potentials

Internal energy, enthalpy, Helmholtz/Gibbs free energies form a different family connected by Legendre transforms and changes of natural variables.

Use established thermodynamic mathematics; do not collapse them into the field-potential constructor.

### 7. Conjugate derivative quantities

General family:

\[
Conjugate(F,X;C)
:=
\left.\frac{\partial F}{\partial X}\right|_C.
\]

Chemical potential is a key example under the appropriate thermodynamic potential/held-fixed variables.

## C. General derivative constructor

`Rate` can be viewed as a specialization of a more general derivative family:

\[
Differentiate(F,X;HeldFixed).
\]

Then:

- velocity: derivative of position with respect to time;
- acceleration: derivative of velocity with respect to time;
- thermodynamic response coefficients: constrained derivatives with respect to state variables;
- chemical potential: constrained derivative of a thermodynamic potential with respect to amount/composition variable.

The `HeldFixed` slot is semantically important and can distinguish quantities with identical algebraic derivative skeletons.
