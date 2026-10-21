# M4 batch 2 — 2026-09-10

Four frozen targets: M008/M009/M016/M019. These are newly constructed,
single-analyst provisional analyses, not a blind run or independent replication.
Kernel v0.4 remains frozen. With batch 1, 8/20 targets have provisional analyses;
12 remain unassessed. BB1 historical grades and totals are unchanged.

| Case | Provisional G/E | Tested reduction | Result for the specified query |
|---|---|---|---|
| M008 | G3/E1 | Preparation history -> current applied field | Unsafe for current magnetization in the declared switching model. |
| M009 | G2/E1 | Potential representative -> gauge orbit | Safe for E/B; unsafe for representative components. |
| M016 | G2/E1 | Local band function -> energy and gradient at k0 | Unsafe for band-curvature mass. |
| M019 | G1/E1 | Labeled configurations -> permutation orbit | Safe for symmetric queries; label query does not descend. |

G grades apply to the exact relation and declared inputs below. E1 assesses the
explicit mathematical encoding, not executable support in pgcheck. No parser or
general type checker has verified these encodings. E3/E4 remain review questions
if the declared structures cannot be expressed transparently under the frozen
mathematical-constructor allowance; no new primitive is proposed here.

## M008 — magnetic hysteresis

### External basis and declared model

Feynman, Leighton and Sands, [Lectures on Physics II, chapter 36](https://www.feynmanlectures.caltech.edu/II_36.html),
sections 36-3 and 36-5, especially Fig. 36-12 and its following discussion,
describe different magnetic fields at the same drive current after different
preparations, including residual magnetism. This supports history sensitivity;
it does not supply the switching rule used below. The HTML passage was read on
2026-09-10. Its H convention differs from SI; no numerical H value is transferred.

Our model: a uniform uniaxial magnetic element, fixed temperature, easy axis and
geometry, with SI applied field H along that axis and negligible demagnetizing
correction. Specify the energy density

`f(theta,H) = K sin(theta)^2 - mu0 Ms H cos(theta)`, with K, Ms > 0.

This is a constitutive/model assumption, not a PG definition of magnetization.
Assume quasistatic following of a local energy minimum, negligible thermal
activation, and switching when that minimum loses stability. At theta=0 and pi,
the angular curvatures are `2K+mu0 Ms H` and `2K-mu0 Ms H`. Therefore the two
branches coexist for `-Hk < H < Hk`, where `Hk=2K/(mu0 Ms)`.

The idealized axial dynamics becomes a two-state relay: let h=H/Hk and s=+1/-1.
On each monotone segment of the drive, set s=+1 at h>=1, s=-1 at h<=-1,
otherwise retain s. At the exactly marginal endpoints, switching is an explicit
convention. M=Ms*s. This ideal model predicts rectangular loops; domain-wall
motion, thermal escape, rate effects and general minor-loop memory are outside it.

### Semantic parse

| Field | Content |
|---|---|
| Property | Axial magnetization of the specified sample after preparation. |
| Grounding | Sample S; preparation process R, identified by initial state and ordered drive path on S. |
| Roles | S is bearer; R supplies drive and initial-state provenance. |
| Reference | Fixed easy axis, sign convention and laboratory drive. |
| Indices/resolution | Ordered turning points of piecewise-monotone h(t); segment index j is bound in recurrence. |
| Conditions | Fixed K/Ms/temperature/geometry; quasistatic metastable following and switching convention above. |
| Prerequisites | Angular energy, local stability, ordered sequence and two-state recurrence. |
| Construction | s0[R] plus s_j=update(s_(j-1),h_j[R]); M[S,R]=Ms[S]*s_final. |
| Representation | Dimensionless h and s; equivalent physical values use retained Hk and Ms. |
| Projection/elimination | pi(R)=H_final[R]; erase earlier drive and initial state. Recurrence binds j without erasing sample genealogy. |
| Value structure | Real axial scalar; s is a model state, not an additional Entity category. |
| Dimension/Quantify | SI M and H: A/m; magnetization admits a quantity view. No measurement result is inferred. |
| Naming | Magnetization with explicit preparation qualifier; the word alone omits history. |

R is not an opaque History object: identity includes the initial state and the
ordered monotone segments. Two differently timed versions can have equal output
in this rate-independent model without being identical preparation processes.
The existing Physical Expression and ConstitutiveRelation categories host the
recurrence and model; they do not derive the physical model.

### Witness, factorization and account

Start both preparations at s0=-1. R+ has h=(-2,2,0); R- has h=(-2,0).
Both end at H=0, but M(R+)=+Ms and M(R-)=-Ms. Thus pi is **unsafe** for M.
Retaining the final branch s is sufficient for current M via Mbar(s)=Ms*s,
and for continuation under this relay rule with retained model parameters.
This sufficiency is model-specific, not a claim that one bit summarizes every
ferromagnet's history. A reversal below threshold leaves the branch unchanged.

[G]: grounded process/bearer, ordered construction, binding and explicit loss.
[M]: trigonometric derivatives, local stability and recurrence.
[D/model]: energy, metastability and switching assumptions. **G3/E1** scores
the magnetization prediction. No G4 is established by a failed memoryless law.

## M009 — gauge equivalence versus component equality

### External basis and domain

Tong, [Electromagnetism, relativity chapter](https://davidtong.org/pdfs/teaching/electromagnetism/electro4.pdf),
sections 5.3.1-5.3.2, printed pp. 105-106, equation (5.13), gives
`A'=A+grad chi`, `phi'=phi-partial_t chi` and the invariant electromagnetic
tensor. The linked chapter labels itself chapter 5 despite its filename.
The relevant full-text passage was read on 2026-09-10.

Fix a contractible spacetime patch U, an inertial chart, smooth real potentials,
and all single-valued C2 functions chi on U. No boundary gauge fixing or boundary
charges are imposed. The comparison concerns local classical E/B. A different
boundary or topological domain requires a fresh admissibility contract; see M010.

### Semantic parse

| Field | Content |
|---|---|
| Property | Electromagnetic field configuration and its potential representation. |
| Grounding | Configuration C, region U and reference frame R, kept fixed under gauge transformation. |
| Roles | C is represented; U restricts admissibility; R gives components. |
| Reference | Fixed inertial coordinates and SI potential signs. |
| Indices/resolution | x,t retained as mathematical arguments; vector components retain their chart. |
| Conditions | Smooth potentials and single-valued C2 chi; no extra boundary restrictions. |
| Prerequisites | Differential calculus, function spaces, group action and quotient. |
| Construction | T_chi(phi,A)=(phi-dt chi,A+grad chi); E=-grad phi-dt A; B=curl A. |
| Representation | A specified T_chi is invertible by T_(-chi); it changes representatives. |
| Projection/elimination | pi maps a representative to its orbit under the declared transformations; chi is quantified over in orbit membership. |
| Value structure | Scalar/vector fields and an orbit, not one scalar quantity. |
| Dimension/Quantify | phi in volts, A in V s/m, chi in V s; components admit quantity views in a fixed chart. |
| Naming | Gauge-equivalent potentials is a qualified relation, not component equality. |

Orbit identity is explicit: p~p' iff an admissible chi satisfies p'=T_chi(p).
This mathematical quotient is a value structure; no opaque GaugeClass EntityMap
or assertion that equal local fields always identify a global configuration is used.
E'=E follows by commuting mixed derivatives; B'=B by curl grad chi=0.
Consequently E/B descend to the orbit: **safe** by an algebraic factorization proof.

### Witness and account

Our pair starts with phi=0,A=0 and takes chi=c*x*t, for nonzero constant c with
units V/m. The transformed potentials are phi'=-c*x and A'=(c*t,0,0).
Their E/B remain zero, but at t=t0!=0 the x potential component differs by c*t0.
That component is **unsafe** to recover from the orbit without choosing a gauge.
This loss is representative information, not a lost gauge-invariant measurement.
As a physical control, phi=-c*x,A=0 produces E=(c,0,0); dropping the compensating
time-dependent vector potential is not this gauge transformation.

[G]: grounding, typed representation, qualified equivalence and projection.
[M]: derivatives and group quotient.
[D]: electromagnetic potential/field interpretation and admissible gauge action.
**G2/E1**, with the physical semantic seed supplied; the invariance calculation
requires no constitutive dynamics. A bare gauge transformation is invertible;
quotienting representatives is many-to-one. Conflating those operations is the
tested error, not a demonstrated kernel failure.

## M016 — band effective mass

### External basis and domain

Tong, [Electron Dynamics in Solids](https://davidtong.org/pdfs/teaching/solid-state-physics/solidstate3.pdf),
section 3.2.2, printed p. 94, defines the effective mass tensor using the matrix
inverse of the band-energy Hessian. Section 3.2.3, printed p. 95, states the
single-band, weak, spatially slowly varying external-potential regime for the
semiclassical equation of motion. These passages were read on 2026-09-10.

Fix crystal C, a specified isolated nondegenerate band n, a Cartesian reciprocal
chart, and k0 in a C2 neighborhood. Define inverse mass
`D_ij[C,n](k0)=hbar^(-2) partial_ki partial_kj E_n[C](k0)`.
Only when this matrix is nonsingular define `m*=inverse(D)`.
The inverse is a matrix inverse, never entrywise reciprocation. Negative curvature
is allowed; a singular Hessian has no ordinary finite inverse mass tensor.

### Semantic parse

| Field | Content |
|---|---|
| Property | Local band-curvature inverse mass tensor and, if invertible, effective mass tensor. |
| Grounding | Crystal C in a fixed physical configuration; the band is selected from its spectrum. |
| Roles | C supplies the band structure; n selects the band, k0 its evaluation point. |
| Reference | Fixed reciprocal Cartesian axes and energy zero. |
| Indices/resolution | n, i/j and k are mathematical indices/arguments; differentiation is in k, evaluated at k0. |
| Conditions | C2 isolated band; nonsingularity for inversion; fixed crystal configuration. Dynamics needs extra regime assumptions. |
| Prerequisites | Band-energy function, Hessian and matrix inversion. |
| Construction | D=hbar^-2 Hess_k E_n[C] at k0; m*=D^-1 if defined. |
| Representation | Tensor components in the chart; chart changes must also transform k and derivatives. |
| Projection/elimination | pi(E)=(E(k0),grad E(k0)); a separate local quadratic view retains the Hessian but erases higher-order behavior. |
| Value structure | Symmetric inverse-mass tensor; ordinary tensor inverse on its nonsingular domain. |
| Dimension/Quantify | D: kg^-1; m*: kg. Selected directional/component quantities depend on the declared tensor representation. |
| Naming | Band effective mass, qualified by crystal, band and k0; bare electron mass is a different property. |

Genealogy is `C -> E_n[C](k) -> Hessian at k0 -> inverse`. The band index does
not create an ungrounded new material Entity. No EffectiveParticle object is needed.
Definition of curvature mass is distinct from the law/approximation that uses it
to predict acceleration, and from whatever calculation or measurement supplied E.

### Witness and account

Our local dimensionless coordinates are q=(k-k0)/k_scale and e=(E-E0)/E_scale,
where both positive scales are retained. Use two admissible local band models:
`e1=(qx^2+qy^2)/2`, `e2=(2*qx^2+2*qx*qy+2*qy^2)/2`.
At q=0 both have zero value and gradient. Their Hessians are I and
`[[2,1],[1,2]]`, giving normalized masses I and `[[2,-1],[-1,2]]/3`.
The physical mass scale is `hbar^2*k_scale^2/E_scale`. These are constructed
local models, not reported dispersions of a named material. Thus pi is **unsafe**
for curvature mass. Bare species mass can also be held fixed in this comparison.

For a second control, e1 and `e1+qx^4` have identical local masses at q=0 yet
differ at q=(1,0). A local quadratic view is **unsafe** for exact finite-displacement
band energy. No finite-neighborhood error bound follows from the local mass alone.
It is **safe** for mass on the nonsingular domain because it retains the Hessian.

[G]: grounding/genealogy, expression composition and explicit projection.
[M]: Hessian, evaluation and matrix inverse.
[D]: band-energy meaning and curvature-mass definition. **G2/E1** for this
definition; an acceleration prediction using semiclassical dynamics would be G3.
The pair shows why matching energy, gradient, dimension or bearer cannot replace
construction information. No kernel revision is justified by this pair.

## M019 — permutation quotient and label-sensitive questions

### External basis and scope

Garrison, [Quantum Statistics of Identical Particles](https://link.springer.com/article/10.1007/s10701-022-00596-4),
Foundations of Physics 52, 77 (2022), section 3, equation (14) and the following
Permutation-Invariance Rule, requires observables to commute with particle-label
permutations. Section 2 distinguishes labels in a product representation from
intrinsic species properties. The relevant HTML sections were read on 2026-09-10.

Our explicit quotient test uses classical configurations of two identical point
particles in a fixed frame at one instant, with artificial slot labels and no
tags or trajectory records. It is a test of the frozen label-versus-invariance
question, not a construction of a quantum state space. A quantum comparison is
given below to avoid equating classical unordered tuples with Bose/Fermi states.

### Semantic parse

| Field | Content |
|---|---|
| Property | Configuration of an identical-particle system and queries on that configuration. |
| Grounding | System S and observation frame/time in context. Artificial slots 1/2 belong to the representation. |
| Roles | Two interchangeable particle slots; spatial reference remains fixed. |
| Reference | Fixed spatial chart; identical intrinsic species properties. |
| Indices/resolution | Slot i is removed by permutation quotient; spatial sites remain distinguishable. |
| Conditions | Same species, no distinguishing tags; instantaneous configurations, no path history. |
| Prerequisites | Product configuration space and S2 action. |
| Construction | sigma(x1,x2)=(x2,x1); pi(x)={x,sigma(x)}. |
| Representation | Ordered tuple is a redundant representative; in 1D sorted tuple is a canonical orbit representative. |
| Projection/elimination | pi forgets slot assignment; the orbit relation explicitly binds the permutation. |
| Value structure | Unordered configurations with multiplicity retained, not a set of occupied positions alone. |
| Dimension/Quantify | Position/separation: length; occupancy: dimensionless count. An orbit is not a scalar measurement value. |
| Naming | Label-specific position differs from occupation of a named spatial region. |

S retains system identity. Slots do not become independently observable physical
bearers merely because the input notation numbers them. A label-preserving Scope
may track those representational slots, but cannot turn them into measurable tags.
Orbit identity is given by a concrete group action, not an opaque Same predicate.

### Witness, quantum boundary and account

Our pair x=(0,1) and x'=(1,0), in one fixed length unit, gives the same orbit
but Q1(x)=x1 equals 0 and 1. Recovering the original slot-1 coordinate is
**unsafe**. It is not an admissible observable of the declared untagged quotient.
The symmetric distance `abs(x1-x2)` and occupancy
`N_left=sum_i 1[x_i<1/2]` factor through pi and are **safe**. Sorting recovers
the leftmost coordinate, not the lost identity of slot 1. Keeping multiplicity
matters: (0,0) is a two-particle configuration, not a one-element configuration.

Quantum boundary: on the two-mode auxiliary product space with basis
|LL>,|LR>,|RL>,|RR>, swap U exchanges |LR> and |RL>. The operator
`Q1=|L><L| tensor I` does not commute with U, while
`N_L=Q1+I tensor |L><L|` does. On a fixed bosonic/fermionic sector the physical
states are (anti)symmetrized; |LR> and |RL> are not two independently preparable
states in that sector. The classical pair is therefore not evidence of lost
quantum observables. Symmetrization, exchange phase, coherence and entanglement
cannot be recovered or modeled by sorting classical coordinates.

[G]: scope/header, grounded system, representation and qualified reduction.
[M]: finite group action, invariance and factorization (plus linear algebra for
the quantum boundary check). [D]: supplied same-species untagged configuration
interpretation. **G1/E1** scores the classical quotient query with this physical
input seed; deriving quantum exchange restrictions would require a separate
domain account. Scope does not manufacture distinguishability or its absence.

## Findings and next gate

1. Loss of a representative is distinct from loss of a physical observable.
   M009/M019 show redundant descriptions; M008 loses predictive state information.
   Unsafe must always name its query and whether that query is physically admissible.
2. Sufficient history summaries are model-relative. The one-bit M008 state works
   only because its explicit recurrence closes; a History label proves nothing.
3. A local effective parameter carries a construction and a validity domain.
   M016 does not license finite-neighborhood predictions from a local Hessian.

Run `python experiments/pgcheck/m4_batch2_checks.py` (standard library only).
The script reuses batch 1's finite collision search and tests original mathematical
witnesses and negative controls. Algebraic proofs above establish stated safe
factorizations; finite absence of a collision still returns unknown. No executable
result validates a physical constitutive model or assigns grammar grades.

Next bounded M4 batch: M003/M004 (constraint paths) and M005/M006 (nonlocality).
The BB1 G1/G2 retrospective queue remains B021/B022/B023/B038/B051/B052/B057,
with B014/B015 definition-versus-model review also open. None was reconstructed
in this batch. Independent scientific review and final G/E grading remain open.
