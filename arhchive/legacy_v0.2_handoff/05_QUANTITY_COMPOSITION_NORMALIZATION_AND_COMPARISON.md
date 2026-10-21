# 05. Quantity Composition, Normalization, Comparison

## 1. NormalizeBy

Higher-order constructor:

\[
NormalizeBy(D)(Q)
:=
\lambda e.\frac{Q(e)}{D(e)}.
\]

This automatically enforces same-Entity binding.

Examples:

\[
Volumic(Q)=NormalizeBy(Volume)(Q)
\]

\[
Specific(Q)=NormalizeBy(Mass)(Q).
\]

### Generated kinds

- `Volumic(Mass)` → mass density;
- `Volumic(Charge)` → charge density;
- `Volumic(Energy)` → energy density;
- `Specific(Energy)` → specific energy;
- `Specific(Volume)` → specific volume.

## 2. Count / Amount

\[
Count(X;E)
\]

requires both counted kind `X` and bearer Entity `E`.

Amount of substance may remain a seed quantity kind connected to Count by an exact conversion. Do not force its ontology to be merely `Count/NA` unless that design survives metrology review.

Potential richer signature:

\[
[Count]=\mathsf C
\]

with conventional projection `C -> 1`.

## 3. Part-whole ratio

\[
PartWholeRatio(Q)
:=
\lambda p,w.\frac{Q(p)}{Q(w)}
\quad where\ PartOf(p,w).
\]

Examples:

- mass fraction;
- amount fraction;
- count/number fraction;
- volume fraction where appropriate.

Fraction is therefore a constrained ratio with component/whole roles.

## 4. Concentration family

General part/whole normalization pattern:

\[
ConcentrationLike(Q,D)
:=
\lambda p,w.\frac{Q(p)}{D(w)}
\quad where\ PartOf(p,w).
\]

Examples:

- mass concentration: `Mass(part)/Volume(whole)`;
- amount concentration: `Amount(part)/Volume(whole)`;
- number concentration: `Count(part)/Volume(whole)`;
- molality-like constructions use a solvent-mass denominator and therefore demonstrate that concentration cannot be globally defined as "per volume".

## 5. Density vs concentration

\[
MassDensity=\lambda e.Mass(e)/Volume(e)
\]

\[
MassConcentration=\lambda p,w.Mass(p)/Volume(w),\quad PartOf(p,w).
\]

Erase Entity binding:

\[
Mass/Volume.
\]

Erase kind semantics further:

\[
ML^{-3}.
\]

This is a central adversarial benchmark.

## 6. Molar family

Once `Amount(X;E)` exists:

\[
Molar(Q)
:=
\lambda x,e.\frac{Q(x\text{-component of }e)}{Amount(x;e)}
\]

with exact binding details determined by the domain definition.

Examples: molar mass, molar volume, molar energy, molar heat capacity.

## 7. Difference / ratio / relative

Generic comparison families:

\[
Difference_Q(a,b)=Q(a)-Q(b)
\]

\[
Ratio_Q(a,r)=Q(a)/Q(r)
\]

\[
RelativeDifference_Q(a,r)=\frac{Q(a)-Q(r)}{Q(r)}.
\]

Roles matter: `r` is reference, and swapping subject/reference generally changes meaning even if dimension stays unchanged.

## 8. Efficiency and other dimensionless quantities

Efficiency-like construction:

\[
UsefulOutput/Input
\]

shares a quotient skeleton with fraction but has output/input roles rather than component/whole roles.

Dimensionless does not mean semantically empty.

Also preserve:

\[
0\neq dimensionless\neq absent/undefined.
\]

## 9. Mean / aggregate

For Entity collection `G`:

\[
Mean(Q;G)=\frac{1}{|G|}\sum_{e\in G}Q(e).
\]

The result remains grounded collectively in `G`.

Center of mass is a weighted aggregate and a key example of coarse Feature ↔ fine sub-Entity decomposition.
