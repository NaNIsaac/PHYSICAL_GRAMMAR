# M020 — one-particle marginal versus pair correlation

Date: 2026-09-09. Kernel v0.4. Status: source-verified, single-analyst provisional.

## External basis

Tong, [Kinetic Theory, chapter 2](https://davidtong.org/pdfs/teaching/kinetic-theory/kinetic2.pdf),
section 2.1.1, printed pp. 16–19, constructs reduced particle distributions;
section 2.2.1, equation (2.22), printed p. 22, explicitly introduces a factorization
assumption to close a two-particle expression using one-particle functions. The
relevant full text was retrieved. Our finite comparison below is a constructed
probability example, not a numerical result from that source.

## Scope clarification

An exact empirical one-particle measure containing every phase-space atom in a
single microstate may retain the entire unordered configuration. A blanket claim
that every object called “one-particle distribution” loses pair information would
therefore be unsound. Here the projection is specifically an **ensemble marginal**
of a joint distribution of trajectories/states. This instantiates the frozen target
without equating empirical, smoothed and ensemble distributions.

Consider two distinguishable classical particles in separate traps, each with a
binary coarse state z=0 or 1. At the observation time, different preparation
ensembles can correlate the trap states. Trajectory details are first reduced to
these states, then the joint distribution is marginalized. This static slice suffices
to test recovery of equal-time pair correlation; it does not model time evolution.

## Semantic parse

| Field | Content |
|---|---|
| Property | Joint state probabilities, individual marginals and a pair observable. |
| Grounding | Specified preparation ensemble R, particles A/B and their traps. |
| Roles | First and second random-variable slots are explicit. |
| Reference | Same binary-state partition and common observation time. |
| Indices/resolution | z_A/z_B are mathematical outcomes; the eliminated outcome is summed. |
| Conditions | Nonnegative normalized probabilities; no independence assumption. |
| Prerequisites | Product sample space, probability measure and marginalization. |
| Construction | p_A[R](i)=sum_j p_AB[R](i,j), p_B[R](j)=sum_i p_AB[R](i,j). |
| Genealogy | Marginals remain about the same preparation and respective particles. |
| Representation | Exact rational tables in fixed outcome order. |
| Projection | pi(p_AB)=(p_A,p_B); this even retains both single-particle marginals. |
| Value structure/Quantify | Probability arrays and an expectation; no measurement result inferred. |
| Dimension/naming | Dimensionless; “joint”, “marginal” and “pair” encode distinct constructions. |

## Exact witness

Let p_AA be the table ((1/2,0),(0,1/2)) and p_AB be ((0,1/2),(1/2,0)). Both
are normalized, nonnegative and have both marginals (1/2,1/2). However the observable
Q(p)=Pr(z_A=z_B), the sum of diagonal entries, equals 1 and 0 respectively.
Thus Q cannot factor through pi on the full admissible probability simplex:
**unsafe** to recover pair coincidence from the marginals alone.

An independence lift would give ((1/4,1/4),(1/4,1/4)) and Q=1/2. It reproduces
the marginals but neither original pair correlation. This is extra structure,
not an inverse of the projection. Under an explicitly restricted independent
domain, Q=sum_i p_A(i)*p_B(i) is instead a valid factorization. The domain restriction
must be visible; it cannot be licensed merely by choosing a coarse Scope.

## Knowledge and assessment

[G]: grounded families, typed binding, preserved genealogy and projection discipline.
[M]: finite probability, marginalization, expectation and product measures.
[D]: physical meaning of trap states and preparation ensembles. No dynamical law
is required for this static counterexample. Applying molecular chaos to collisions
would be a separate model-dependent assertion.

**G1 / E1, provisional**, with the two-particle joint probability as the declared
physical input seed. If that input seed were unavailable, physical interpretation
would require a separate G2 account. The test does not derive statistical mechanics
from grammar. Ensembles are specified by probability tables, avoiding an opaque
Entity that encodes unknown correlations. Normalization conventions for Tong's
particle-count distributions differ from our probability-one tables; no N factor
has been silently identified with one.
