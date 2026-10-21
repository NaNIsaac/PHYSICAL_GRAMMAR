# 06. Fields, Tensors, Higher-Order Generation

## 1. Field

A Field is a Site-indexed Feature family:

\[
Field[F;D]:p\mapsto F(p).
\]

Examples:

- temperature field;
- density field;
- displacement field;
- electric/magnetic fields;
- stress field.

Fieldness is independent of tensor order. A scalar field and tensor field are both Fields.

## 2. Value structure

Feature semantics must preserve more than physical dimension.

Useful value-structure families include:

- scalar;
- vector/covector;
- tensor/multilinear map;
- point/affine value;
- rotation/orientation;
- categorical/structural value;
- field/distribution family.

Avoid storing only `rank=N` where the order can be derived from semantic slots.

## 3. Stress from traction

At a continuum Site `x` with oriented surface normal `n`:

\[
t(x,n)=\sigma(x)n.
\]

Working semantic abstraction:

\[
Stress(B;x)
:=
LinearAbstract_n(Traction(B;x,n)).
\]

Input is direction/vector-like; output is traction vector. Thus the representing linear map is second order.

This explains why `stress = force/area` is dimensionally suggestive but semantically incomplete.

## 4. Pressure from isotropy

Hydrostatic/isotropic stress:

\[
\sigma=-pI.
\]

Pressure is a scalar coefficient parameterizing the isotropic stress family.

For a general stress tensor, `-tr(σ)/3` may represent mean/hydrostatic pressure component under 3D conventions, but it is not equivalent to the full stress unless isotropy holds.

## 5. Tensor-order generation mechanisms

### Tensor product

\[
ord(A\otimes B)=ord(A)+ord(B).
\]

### Gradient

Under common coordinate/tensor representations, differentiation with respect to spatial direction adds an index/slot:

\[
scalar\ field \xrightarrow{Gradient} vector/covector,
\]

\[
vector\ field \xrightarrow{Gradient} second-order\ tensor.
\]

### Contraction

Removes paired slots, e.g. divergence and trace.

### Projection

Selects components or lower-structure observables such as magnitude or normal component.

### Linear abstraction / response map

For linear `L:X→Y`:

\[
L\in Y\otimes X^*.
\]

The input/output semantic structure explains tensor order.

## 6. Constitutive coefficient orders

Examples under standard tensor representations:

- conductivity/permittivity/permeability: vector → vector → order 2;
- piezoelectric coupling: vector ↔ symmetric order-2 → order 3;
- elasticity/stiffness: order-2 strain → order-2 stress → order 4;
- general viscosity: order-2 rate-of-deformation → order-2 viscous stress → order 4.

Symmetry may drastically reduce independent coefficients without changing tensor order.

## 7. Stress and momentum flux

In continuum balance, momentum is vector-valued. Its transport across oriented surfaces naturally has one additional transport slot, producing a second-order momentum-flux representation.

Cauchy stress is closely connected to the internal/non-advective momentum-transfer part, subject to sign and decomposition conventions.

Maxwell stress provides an electromagnetic analogue in momentum balance.

Treat these as physically informed interpretations, not universal definitions detached from the relevant field theory.

## 8. Tensor rank terminology

Use `tensor order` or `tensor valence` where possible to avoid confusion with matrix rank.
