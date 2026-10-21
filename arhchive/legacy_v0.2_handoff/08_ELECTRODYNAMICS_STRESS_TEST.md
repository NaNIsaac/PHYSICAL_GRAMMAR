# 08. Stress Test — Electrodynamics / Maxwell System

## 1. Purpose

Electrodynamics tests:

- local Fields;
- geometric differential operators;
- Region/Boundary binding;
- integral ↔ differential dual representations;
- constitutive vs field-law separation;
- transport/current semantics.

## 2. Field seeds

Treat the following as domain Feature Kinds/Fields unless a more specific formalism is imported:

\[
E(p),\quad B(p),\quad D(p),\quad H(p),\quad J(p),\quad \rho_q(p).
\]

Do not force one mathematical representation into the Feature ontology:

- ordinary 3D vector/pseudovector notation;
- covectors/bivectors;
- differential forms;
- spacetime tensor forms

are representations/formalisms connected by external mathematics.

## 3. Faraday law — integral genealogy

For oriented surface `Σ`:

\[
\Phi_B(\Sigma)=SurfaceIntegral(B,\Sigma).
\]

Boundary circulation:

\[
EMF(\partial\Sigma)=LineIntegral(E,Boundary(\Sigma)).
\]

Field law:

\[
\boxed{
LineIntegral(E,Boundary(\Sigma))
=
-Rate(SurfaceIntegral(B,\Sigma))
}
\]

The left and right Sites are not independent: `Boundary(Σ)` is derived from the same Region `Σ`.

## 4. Differential localization

Stokes theorem maps boundary circulation to surface integral of curl:

\[
\oint_{\partial\Sigma}E\cdot dl
=
\int_\Sigma (\nabla\times E)\cdot dA.
\]

Under suitable regularity/localization:

\[
\boxed{\nabla\times E=-\partial_t B.}
\]

Do not define Curl merely as "surface shrinks to a point"; treat localization as an established mathematical transformation.

## 5. Maxwell–Ampère

Integral form:

\[
\oint_{\partial\Sigma}H\cdot dl
=
I_f(\Sigma)
+
\frac{d}{dt}\int_\Sigma D\cdot dA.
\]

Local form:

\[
\boxed{\nabla\times H=J_f+\partial_t D.}
\]

Here `J_f` is local free-current density, and surface integration gives the free current through `Σ`.

## 6. Gauss laws

Electric displacement form:

\[
\int_{\partial V}D\cdot n\,dA=Q_f(V)
\]

localizes to:

\[
\nabla\cdot D=\rho_f.
\]

Magnetic law:

\[
\int_{\partial V}B\cdot n\,dA=0
\]

localizes to:

\[
\nabla\cdot B=0.
\]

Again the boundary Site is generated from one underlying Region `V`.

## 7. Constitutive separation

Relations such as

\[
D=\varepsilon E,
\qquad
B=\mu H,
\qquad
J=\sigma E
\]

are not Maxwell definitions. They are constitutive/material response relations valid under specific assumptions (e.g. locality, linearity, isotropy in the simplest scalar-coefficient form).

Anisotropic media naturally promote scalar coefficients to response tensors.

## 8. Grammar result

Electrodynamics supports a clean four-layer decomposition:

```text
Grounded Field Features
    -> geometric/math constructors
    -> Maxwell field laws
    -> material constitutive relations
```

The integral/differential forms preserve one semantic genealogy through Region/Boundary and Stokes/Gauss transformations.
