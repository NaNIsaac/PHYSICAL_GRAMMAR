# M015 — density at two scales

Date: 2026-09-09. Kernel v0.4. Status: source-verified, single-analyst provisional.

## External basis and specified construction

Tong, [Fluid Mechanics, chapter 1](https://davidtong.org/pdfs/teaching/fluid-mechanics/fluids1.pdf),
section 1.1, printed pp. 5–6 (PDF pages 9–10), describes continuum density and
velocity as approximations at scales containing many molecules, and distinguishes
fixed spatial locations from material parcels. Relevant full text was read.

Our test specifies an exact **cell-average** operator; it does not infer that all
possible smoothing operators have the same information loss. At one fixed time,
take a region partitioned into four equal-volume cells C1,...,C4, each of volume v.
Fine density is r_i=Mass[C_i]/v. Coarse cells D1=C1 union C2 and D2=C3 union C4
have volume 2v, so pi(r)=((r1+r2)/2,(r3+r4)/2). Interfaces have zero volume;
all cells use the same spatial frame and partition convention.

## Semantic parse

| Field | Content |
|---|---|
| Property/grounding | Density of material system S within an explicitly selected cell and time. |
| Roles | Material bearer, averaging region and measure are distinct. |
| Reference | Common spatial frame and boundary convention. |
| Indices/resolution | Cell index and scale remain explicit; time is fixed in this test. |
| Conditions | Equal fine volumes, positive densities, nested disjoint partition. |
| Prerequisites | Volume measure, additive mass and spatial regions. |
| Construction | rho[S,C](t) := MassWithin[S,C](t)/Volume[C]. Coarse cell EntityMap is Union[C1,C2]. |
| Binding/genealogy | Internal cell index is summed; S and the union's constituent genealogy remain traceable. |
| Representation | Fine versus coarse cell averages are explicitly different views. |
| Projection | Ordered adjacent pairs are replaced by their volume-weighted average. |
| Value structure | Finite scalar density arrays over declared cells. |
| Dimension/Quantify | Both scales have dimension M L^-3; numerical examples use one common density unit. |
| Naming | Scale/averaging-region modifiers carry relevant distinctions. |

## Exact witness and safe query

Take r_A=(1,3,1,3) and r_B=(2,2,2,2). Both map to (2,2), but the fine spatial
mean square P(r)=sum(r_i^2)/4 is 5 and 4 respectively. Thus fine mean square,
and hence the within-cell fluctuation variance here, cannot factor through pi.
This is **unsafe** without extra retained second moments or an added model.

Total mass is **safe** under this same projection: for arbitrary r,
M(r)=v*sum(r_i)=2v*sum(pi(r)). The displayed equality proves factorization on the
whole declared finite-vector domain. Testing a few vectors alone would not prove it.

These arrays may represent mesoscopic fluid density profiles; they do not claim to
resolve individual molecules or establish a closed coarse-fluid evolution equation.
No invented effective-system Entity is required just to define these averages.

## Important negative result

Smoothing is not intrinsically a many-to-one map. For example, on periodic smooth
fields with the complete exact output retained, Gaussian convolution multiplies
Fourier modes by strictly nonzero factors. It is injective there, although inverse
recovery can be ill-conditioned. This is an elementary Fourier argument, not a
result attributed to the fluid text. Finite sampling, rounding, mode truncation or
another operator can create actual loss. The operator, domain and retained precision
must therefore be stated before asserting an exact projection collision.

## Knowledge and assessment

[G]: cell/system grounding, EntityMap genealogy, summation, explicit projection.
[M]: weighted averages, measure, sums and a finite-dimensional nullspace.
[D]: physical meaning of mass density and the chosen spatial averaging convention.

**G2 / E1, provisional**, with G1 conditional on an environment that already
contains the density seed and regional-mass construction. The seed inventory is
declared here rather than retroactively inferred from BB1. No closure law or
emergent constitutive parameter is claimed. Pressure is on projection contracts
and scale metadata, not yet on the kernel. The finite checks cannot classify a
general smoothing operator as safe or unsafe.
