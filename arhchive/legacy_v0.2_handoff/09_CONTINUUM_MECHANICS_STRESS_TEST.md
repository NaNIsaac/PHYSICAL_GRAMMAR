# 09. Stress Test — Continuum Mechanics

## 1. Purpose

Continuum mechanics tests:

- Entity identity under changing configuration;
- Site-indexed Fields;
- deformation maps;
- tensor generation;
- Eulerian vs Lagrangian viewpoints;
- material derivative;
- balance laws;
- constitutive response.

## 2. Same Entity, different configurations

Let material body `B` be one Entity.

Reference and current configurations:

\[
\mathcal B_0,\qquad \mathcal B_t.
\]

These are not automatically distinct Scopes. They are configurations/Stages/geometric realizations of the same material Entity.

Motion:

\[
\chi_t:\mathcal B_0\to\mathcal B_t,
\qquad
x=\chi(X,t).
\]

Material label `X` preserves Entity/material-point identity while spatial Site `x` changes.

## 3. Displacement and deformation gradient

Reference-based displacement:

\[
u(X,t)=\chi(X,t)-X
\]

when the chosen geometry supports this subtraction.

Finite deformation starts from:

\[
F=\frac{\partial x}{\partial X}.
\]

Do not identify all strain with the infinitesimal expression.

## 4. Strain family

Small-strain specialization:

\[
\epsilon=\frac12(\nabla u+\nabla u^T).
\]

Finite-strain example:

\[
C=F^TF,
\qquad
E=\frac12(C-I).
\]

Thus `Strain` is a family of geometric measures generated from deformation/configuration structure, not one universal primitive formula.

## 5. Material derivative

For Eulerian field `f(x,t)`:

Spatial rate:

\[
\left.\partial_t f\right|_x.
\]

Material rate:

\[
\left.\frac{d}{dt}f(\chi(X,t),t)\right|_X.
\]

For a scalar field in ordinary coordinates:

\[
\frac{Df}{Dt}=\frac{\partial f}{\partial t}+v\cdot\nabla f.
\]

Physical Grammar interpretation:

- the same field history is compared under different held-fixed anchors;
- Eulerian: spatial Site fixed;
- Lagrangian/material: material identity fixed;
- exact pullback/chain-rule machinery belongs to continuum/differential geometry.

## 6. Stress / traction

At Site `x`, oriented normal `n`:

\[
t(x,n)=\sigma(x)n.
\]

Stress is a local second-order tensor-valued Feature because it abstracts the linear dependence of traction on surface orientation.

## 7. Cauchy momentum balance

A common local form:

\[
\boxed{
\rho\frac{Dv}{Dt}
=\nabla\cdot\sigma+f_{body}
}
\]

where `f_body` is force per volume. If one uses body force per mass `b`, write `ρb`.

Type/dimension check under ordinary SI:

\[
[\rho Dv/Dt]=ML^{-2}T^{-2}
\]

\[
[\nabla\cdot\sigma]=ML^{-2}T^{-2}.
\]

## 8. Balance vs constitutive law

Momentum balance requires a stress Feature but does not define stress as a function of strain.

Constitutive model supplies that relation, e.g. linear elasticity:

\[
\sigma=C:\epsilon.
\]

This separation is essential.

## 9. Newtonian fluid

Rate-of-deformation:

\[
D=\frac12(\nabla v+\nabla v^T).
\]

Viscous stress is supplied by a constitutive map; in a simple isotropic Newtonian fluid it reduces to a small set of scalar coefficients.

Full stress often decomposes into isotropic pressure part plus deviatoric/viscous part:

\[
\sigma=-pI+\tau.
\]

## 10. Result

Continuum mechanics strongly supports:

- Entity identity distinct from configuration;
- Site/Field semantics;
- held-fixed roles for derivative meaning;
- tensor order from semantic slots;
- balance law distinct from constitutive response.
