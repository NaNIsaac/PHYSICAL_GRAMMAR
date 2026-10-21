# 10. Constitutive Relations and Response Maps

## 1. Generic pattern

A constitutive relation specifies how a material/system responds:

\[
Y=\mathcal C_M(X;State,History,Parameters,\ldots).
\]

`M` is the material Entity/kind/context.

This is distinct from both Feature definition and universal field/balance law.

## 2. Linear Response Map

If the response is linear:

\[
\mathcal C_M:X\to Y.
\]

Its tensor structure follows from input/output spaces.

Working constructor idea:

\[
ConstitutiveMap[M;X\to Y].
\]

## 3. Examples

### Electrical conduction

\[
J=\sigma_e E.
\]

Anisotropy can make `σ_e` a second-order tensor.

### Dielectric response

\[
D=\varepsilon E.
\]

### Magnetic response

\[
B=\mu H.
\]

### Fourier heat conduction

\[
q=-k\nabla T.
\]

### Fick diffusion

\[
J_i=-D_i\nabla c_i
\]

in simple models.

### Linear elasticity

\[
\sigma=C:\epsilon.
\]

### Newtonian viscosity

\[
\tau=\mathcal V:D
\]

in general tensor form; isotropy reduces the parameterization.

## 4. Symmetry as compression

Symmetry does not necessarily lower tensor order, but it can greatly reduce independent parameters.

Examples:

- isotropic stress `-pI` parameterized by scalar pressure;
- isotropic elastic tensor parameterized by two Lamé-type constants;
- isotropic conductivity parameterized by scalar `k` times identity.

Thus:

\[
\boxed{Symmetry\to value-structure compression.}
\]

## 5. Driving-gradient family

Many transport laws share:

\[
State/Potential
\xrightarrow{Gradient}
DrivingFeature
\xrightarrow{ConstitutiveMap}
Flux.
\]

Examples: Fourier, Fick, Ohm in potential-gradient formulation.

This is a strong candidate for cross-domain grammar reuse.
