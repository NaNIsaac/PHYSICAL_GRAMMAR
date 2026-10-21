# 07. Balance, Transport, Conservation

## 1. Crossing

`Crossing(Q,Σ)` is the cumulative amount/feature of `Q` crossing an oriented Site `Σ`.

It is especially useful because it separates:

- the carried Feature;
- the through-Site;
- transit Stage/geometry;
- accumulation vs rate.

Exact transport mathematics is delegated to continuum/transport theory.

## 2. Current / flux distinction

For charge:

\[
Current(\Sigma)=Rate(Crossing(Charge,\Sigma)).
\]

Local current density `J` is a charge-flux density Field satisfying, in ordinary vector notation:

\[
I(\Sigma)=\int_\Sigma J\cdot n\,dA.
\]

Do not define `J` as `Flux(Current)`.

## 3. Fluence and particle flux

\[
Fluence_X(\Sigma)
=
\frac{Crossing(Count_X,\Sigma)}{Area(\Sigma)}.
\]

\[
Flux_X(\Sigma)=Rate(Fluence_X(\Sigma))
\]

under suitable fixed-surface/local-uniformity conventions.

## 4. Balance Law Schema

For quantity/feature `Q` in Region `R`:

\[
Rate(Content_Q(R))
=
-NetOutflow_Q(\partial R)+Production_Q(R).
\]

Local form:

\[
\partial_t\rho_Q+\nabla\cdot J_Q=s_Q.
\]

The integral-to-local step uses established localization and Gauss/Stokes machinery.

## 5. Conservation

\[
Conservation(Q)=Balance(Q)\text{ with }s_Q=0.
\]

Thus conservation is a constrained balance schema rather than a separate primitive constructor family.

## 6. Examples

### Mass

\[
\partial_t\rho+\nabla\cdot(\rho v)=0
\]

for source-free mass in ordinary continuum conditions.

### Charge

\[
\partial_t\rho_q+\nabla\cdot J=0.
\]

### Species

\[
\partial_t c_i+\nabla\cdot J_i=R_i.
\]

### Momentum

\[
\partial_t g+\nabla\cdot\Pi=f.
\]

With continuum decomposition and mass continuity, one obtains Cauchy momentum form.

### Energy

\[
\partial_t u+\nabla\cdot J_E=s_E.
\]

The physical decomposition of `J_E` into advection, heat flux, stress work, EM transport, etc. is domain-specific.

## 7. Transport slot and tensor order

Under common tensor representation:

\[
ord(Flux_Q)=ord(Q)+1.
\]

Then:

\[
ord(Div(Flux_Q))=ord(Q).
\]

Examples:

- scalar mass/charge/energy density → vector flux;
- vector momentum density → second-order momentum flux.

Caveat: differential-form and geometry-specific representations may encode these slots differently. Treat this as a typed representation rule, not an ontology axiom.

## 8. Moving control regions

For moving Region/Boundary, use relative crossing and Reynolds transport theorem rather than inventing an independent moving-balance primitive.

The distinction again depends on what is held fixed: spatial control volume vs material body.
