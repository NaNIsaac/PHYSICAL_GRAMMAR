# M4 batch 5 — 2026-09-10

M011/M012/M017/M018 complete the first analysis of the frozen M4-01 selection:
**20/20 analyzed, not 20/20 independently validated passes**. Kernel v0.4 and
historical BB1 totals remain unchanged. All examples below are our constructions.

## 쉽게 읽는 이번 결과

- **M011:** 복소수 장이 한 바퀴 돌 때 위상이 몇 번 감기는지는 시작점과
  끝점의 값만으로 알 수 없다. 도중에 장의 값이 0이 되면 감김수가 바뀔 수 있다.
- **M012:** 양자 상태가 출발점으로 돌아와도 이동 경로에 따른 위상은 남는다.
  위상 표기법을 바꾼 것과 실제 경로를 바꾼 것은 다르다. Berry 위상은 일반적으로
  경로를 조금 변형해도 값이 유지되는 위상수학적 불변량은 아니다.
- **M017:** 계기의 표시와 측정하려는 대상의 물리량은 다르다. 같은 표시라도
  교정 관계가 다르면 추정한 값과 불확도가 달라진다.
- **M018:** Vickers 경도와 Knoop 경도는 시험 절차를 포함해서 정의해야 한다.
  절차를 구분하는 문법만으로 실제 재료의 환산식을 만들어낼 수는 없다.

| Case | Provisional G/E | Specific result |
|---|---|---|
| M011 | G1/E1 | Given a complex field, endpoint or magnitude-only retention loses winding. |
| M012 | G2/E2 | Closed-loop endpoints lose Berry holonomy; admissible gauge changes preserve it. |
| M017 | G3/E1 | Indication without the calibration relation loses the model-based estimate. |
| M018 | G2/E2 for procedure semantics | Cross-procedure physical conversion remains unknown without material evidence/model. |

M011 assumes a physically interpreted field as input. M012 scores the Berry
construction with its supplied quantum interpretation; an actual adiabatic
evolution prediction adds dynamical assumptions. M018 does not receive a fictional
conversion score or fabricated numerical material counterexample.

## M011 — winding and zeros

Source read 2026-09-10: Tong, [Statistical Field Theory, section 4.4.1](https://davidtong.org/teaching/statistical-field-theory/sfthtml/S4),
the displayed circulation 2*pi*n and the following vortex-core discussion.
The text connects integer phase winding to periodicity and notes that phase is
undefined at the core. The homotopy and examples below are our mathematical analysis.

Let C be a fixed oriented closed contour in a system S, parameterized by
t in [0,2*pi], with endpoints identified. Assume psi_C(t)=psi[S,C(t)] is C1,
periodic and nonzero on C. Define
`W[S,C] := (1/(2*pi))*integral_0^(2*pi) Im(psi_C'(t)/psi_C(t)) dt`.
The integrand is the derivative of a local phase; a single global real-valued phase
on the circle is not assumed. W is an integer degree. Zeros inside the contour
are allowed; nonvanishing is required on the contour itself.

| Field | Content |
|---|---|
| Property | Winding of the supplied complex field along C. |
| Grounding | System S, field configuration and oriented contour C. |
| Roles | Field being evaluated and traversal orientation. |
| Reference | Complex-plane orientation, phase convention, same contour. |
| Indices/resolution | Full continuous trace, not just sampled phases. |
| Conditions | C1 periodic nonzero trace; homotopies stay nonzero on C. |
| Prerequisites | Complex division, line integration and degree/homotopy mathematics. |
| Construction | Integral of imaginary logarithmic derivative divided by 2*pi. |
| Representation | Orientation-preserving regular reparameterization retains W. |
| Projection/elimination | Full trace -> magnitude trace or endpoint value. |
| Value structure | Signed integer. |
| Dimension/Quantify | Dimension one, normalized phase-turn count. |
| Naming | Winding of psi around oriented C. |

C identity includes its spatial path and orientation; t is a mathematical bound
parameter, not an invented physical Entity. Compose the grounded field with the
contour map, differentiate, divide and integrate using ordinary mathematics.
Binding t does not erase S or C. Record nonvanishing as Constraint and W as
Definition. The spike's Entity binder is only a dependency sketch, not this value typing.

Witnesses psi_0(t)=1 and psi_1(t)=exp(i*t) have the same unit magnitude at every
t and identical endpoints but W=0 and W=1. Both reductions are **unsafe** for W.
Continuous nonzero deformation is **safe** for W: degree varies continuously into
the discrete integers and therefore is constant. For
`psi_s(t)=(1-s)*exp(i*t)+s`, W=1 for 0<=s<1/2 and W=0 for 1/2<s<=1.
At s=1/2,t=pi, psi=0 and W is undefined. This crosses the admissible-domain
boundary; it is not a violation of homotopy invariance.

Reversing orientation negates W. Also, exp(i*4*t) and 1 agree at the four equally
spaced phases 0,pi/2,pi,3*pi/2 but wind differently. Finite samples alone cannot
certify a continuous winding without interpolation/regularity information.
The check script uses explicitly piecewise-linear nonzero polygons, not an
unqualified sampling algorithm for arbitrary physical fields.
[G]: grounding, composition and binding. [M]: winding/degree and nonzero homotopy.
[D]: the supplied field's physical interpretation, no field dynamics inferred.
**G1/E1**, no G4 established.

## M012 — Berry holonomy, gauge and loop dependence

Source read 2026-09-10: Tong, [Quantum Hall Effect, chapter 1](https://davidtong.org/pdfs/teaching/quantum-hall-effect/qhe1.pdf),
sections 1.5.1–1.5.2, printed pp. 28–32, equations (1.39)–(1.43) and the
two-state example. These give the gap condition, connection, loop phase and
gauge freedom. We declare our spinor/sign convention explicitly below.

Take a smooth nondegenerate eigenline of H(lambda) along an oriented closed loop
C, with a positive spectral gap. For normalized local eigenvector n(lambda), use
`A=i<n|dn>`, `gamma_C=integral_C A`, `holonomy=exp(i*gamma_C)`.
For a periodic section on C this expression is sufficient. With multiple patches,
include transition phases; for a nonperiodic section along [0,T], add
`arg(<n(0)|n(T)>)` to the connection integral. The endpoint ray is the same.
Under n -> exp(i*chi)*n, A -> A-dchi; the endpoint correction cancels the shift.
For a periodic gauge with chi(T)-chi(0)=2*pi*k, gamma changes by -2*pi*k,
while holonomy is unchanged. The value is a phase class, not an unqualified real number.

| Field | Content |
|---|---|
| Property | Abelian Berry holonomy of a specified eigenline and parameter loop. |
| Grounding | Quantum system S, eigenline selection and oriented loop C. |
| Roles | Hamiltonian parameters versus quantum dynamical degrees of freedom. |
| Reference | Eigenvector gauge, phase sign and endpoint/patch convention. |
| Indices/resolution | Complete parameter loop and eigenprojector family. |
| Conditions | Nondegenerate smooth eigenline; positive gap along loop. |
| Prerequisites | Complex inner product, line bundle connection and patch transitions. |
| Construction | Connection integral plus endpoint/transition correction, exponentiated. |
| Representation | Gauge-related local sections represent the same eigenline. |
| Projection/elimination | Full path -> common basepoint; real gamma -> phase modulo 2*pi. |
| Value structure | U(1) element or R/(2*pi*Z) class. |
| Dimension/Quantify | Phase in radians; normalized turns useful for exact examples. |
| Naming | Berry phase of the specified band/state along C. |

The eigenline is identified by its spectral projector over the parameter domain,
not an opaque object holding the answer. C is a map with orientation and basepoint.
Local eigenvectors, overlaps and transitions supply explicit mathematical data.
Ordinary composition/integration binds the path parameter while retaining S,C and
the eigenline. Definition gives the holonomy; the adiabatic theorem is separate
physical input if it is interpreted as an acquired phase after dynamical-phase removal.

Our fixture: H=-Delta*n_hat dot sigma, Delta>0, with ground spinor
`n=(cos(theta/2), exp(i*phi)*sin(theta/2))`. Its gap is 2*Delta,
`A_theta=0`, `A_phi=-(1-cos(theta))/2`. Construct a based loop by going from
the north pole down a meridian, once around a latitude, then back along the same
meridian. The meridian contributions vanish in this section. Thus
`gamma/(2*pi)=-(1-cos(theta))/2`.
Latitudes cos(theta)=0 and 1/2 give phase classes 1/2 and 3/4 turns, despite
the same basepoint, Hamiltonian and starting eigenray. Endpoint retention is
**unsafe** for holonomy. These loops can be continuously deformed into one another
without closing the gap: Berry phase is geometric and generally not homotopy invariant.

Gauge choice modulo endpoint corrections is **safe** for holonomy by the cancellation
above. Discarding integer full turns is safe for holonomy but unsafe for a chosen
real-valued lift; that lift is not gauge-invariant physics. No global gauge across
the whole parameter sphere is assumed. Degenerate subspaces/non-Abelian holonomy
are outside this minimal case.
[G]: preserved system/loop dependencies and representation distinction.
[M]: bundle connection, integration and phase quotient. [D]: Berry construction.
**G2/E2**: gauge/patch scaffolding is substantial. General patch consistency is
not implemented or independently checked; E2/E3 remains a real review question.

## M017 — indication, calibration and measurand

Sources checked 2026-09-10: VIM3 [2.3 measurand](https://jcgm.bipm.org/vim/en/2.3.html)
and [2.39 calibration](https://jcgm.bipm.org/vim/en/2.39.html), including note 1.
The [4.1 indication](https://jcgm.bipm.org/vim/en/4.1.html) definition and note 2
were available in the search-index excerpt; repeated direct page retrieval failed.
VIM separates the target quantity, instrument-provided quantity value and calibrated
measurement result. Calibration includes uncertainty and is not instrument adjustment.

Let the measurand be pressure X of sample S during trial R under fixed stated
conditions. Device D provides a voltage indication y, a quantity value of its
output-voltage Property, not itself the sample's pressure Property. A calibration
record K supplies the affine model `y=a*x+b`, a>0 on a declared working interval.
The estimated pressure is `x_hat=(y-b)/a`. K must identify device, calibration
conditions, coefficients, units, uncertainties and validity interval.

| Field | Content |
|---|---|
| Property | Sample pressure; separately device output voltage. |
| Grounding | Sample S, device D, trial R, calibration record K. |
| Roles | Measurand bearer, indicating device, calibration inputs. |
| Reference | Pressure convention, voltage reference, working conditions. |
| Indices/resolution | Same trial; resolved calibration version and validity interval. |
| Conditions | Invertible affine response, a>0, no saturation, stated validity domain. |
| Prerequisites | VIM quantity/value/result distinction and measurement model. |
| Construction | Infer x_hat from y,a,b; attach an uncertainty model. |
| Representation | Unit conversion with coefficients transformed consistently. |
| Projection/elimination | (y,K) -> y erases the calibration relation. |
| Value structure | Estimate plus uncertainty; indication is an input value. |
| Dimension/Quantify | y,b in mV; x in kPa; a in mV/kPa. |
| Naming | Indicated voltage versus calibrated pressure estimate. |

S/D are independently identified physical objects; R is the shared measurement
event. K is an independently referable calibration record whose contents were
specified above, not a new primitive. The affine relation is a model relation,
not an assertion that device and sample are the same bearer. The estimate and
its provenance do not redefine the identity of the measurand.

Construct two allowed calibration records a=1 or 2 mV/kPa, b=0, y=10 mV.
They infer 10 or 5 kPa: the same-indication projection is **unsafe** for x_hat.
With coefficients treated as exact in this idealized example and input standard
uncertainty u_y=1 mV, the propagated u_x is 1 or 1/2 kPa. Keeping only the point
estimate also cannot generally recover uncertainty: a fixed estimate 10 with
u_y=1 versus 2 gives unequal u_x. No real calibration or exact true pressure is claimed.
Given a,b,y and the stated domain the reduction to x_hat is **safe for that point
estimate**, not for arbitrary result/provenance queries. Actual coefficient
uncertainty and covariance must be supplied for a real measurement result.
[G]: distinct grounding and construction provenance. [M]: affine inversion and
linear uncertainty scaling. [D/model]: the pressure-sensor calibration relation.
**G3/E1**, no G4 established. The spike does not implement VIM value/result types.

## M018 — Vickers versus Knoop procedure semantics

Sources read 2026-09-10: ASTM's public [E92-17 page](https://store.astm.org/e0092-17.html),
sections 4.3–4.6 and 1.7, distinguishes indenter geometry, calculations and
force-dependent behavior. Its public [E140-12a page](https://store.astm.org/e0140-12a.html),
section 6.2, describes interscale conversion as approximate and material-dependent.
These are identified historical editions and public excerpts, not a review of
the full paid standards or a current test-compliance specification.
For a concrete calculation, [NIST SRM 2831 certificate](https://tsapps.nist.gov/srmext/certificates/2831.pdf),
page 1, supplies the ideal Vickers expression HV=1.8544*F/d^2 in SI pressure units.
The ideal coefficient is quoted to its stated precision, not treated as exact geometry.

Compare two prescribed indentation procedures on a specified material sample S:
P_V uses a square-pyramid Vickers indenter; P_K uses an elongated Knoop indenter.
Each procedure record must include geometry, force schedule, dwell, surface/sample
preparation, orientation, location rule, diagonal-reading rule, calculation and
reporting convention. Actual trials C_V,C_K use distinct indentation sites; neither
one local value nor reuse of a previously indented site defines a bulk material value.

| Field | Content |
|---|---|
| Property | Sample hardness as specified by P_V or P_K. |
| Grounding | Sample S, procedure P, indentation trial C and its site. |
| Roles | Sample bears the procedure-defined quantity; instrument applies/readouts. |
| Reference | Procedure version, material condition, axes and reporting convention. |
| Indices/resolution | Site and trial resolved; local versus bulk distinction retained. |
| Conditions | Procedure-specific loading, dwell, preparation and validity domain. |
| Prerequisites | Empirical indentation semantics and geometric reading rules. |
| Construction | Procedure's reduction of force/indentation data to reported hardness. |
| Representation | SI pressure-form Vickers value or specified conventional number. |
| Projection/elimination | Procedure-qualified expression -> generic hardness label. |
| Value structure | Procedure-specific scalar; conversion may yield an uncertain estimate. |
| Dimension/Quantify | Force/area forms need area and scale conventions; dimension alone is insufficient. |
| Naming | Explicit Vickers/Knoop qualifier plus required test metadata. |

P is an independently referenceable test prescription with the listed contents;
C is its execution on S, not a catch-all Entity. Ground force and indentation
geometry at C, use the prescribed arithmetic as Definition, and retain S/P/C
genealogy. Conversion is a separate empirical/model relation. A label `Hardness[P]`
without the procedure contents would be an escape hatch. Here only the semantic
signature and Vickers arithmetic are expanded; complete Knoop procedure encoding
and general procedural typing are unimplemented. E2/E3 deserves external review.

Specific comparison: a P_V record and a P_K record collapse to the same
`Hardness[S]` expression when P is erased, but answer “which indenter geometry?”
differently. That reduction is **unsafe for procedure identification**. It is not
a numerical witness that two real materials share HV but differ in HK.

Question: does supplied HV determine HK for an unspecified material and test setup?
The present record returns **unknown for a quantitative prediction**: no applicable
conversion data/model or tolerance is supplied. Source evidence rules out treating
conversion as a universal unit change; it does not give our missing material data.
No exact nonfactorization theorem over all physically possible materials is claimed.

The code checks only Vickers arithmetic and procedure loss. With an illustrative
force 1 N, mean diagonal 100 micrometres gives 185.44 MPa in the certificate's
SI convention; doubling d divides that by four. These values are not a conversion
table or actual measured sample. Retaining F,d and the coefficient suffices for this
specified arithmetic, not for HK. **G2/E2** for procedure semantics; an actual
conversion would require empirical/model input (G3 if supplied and assessed).
[G]: procedure/sample/trial grounding. [M]: geometric arithmetic. [D]: indentation
definitions. No G4 established; no conversion success reported.

## Campaign checkpoint

Run `python experiments/pgcheck/m4_batch5_checks.py` with standard-library Python.
All six scripts passed 159 checks (33 + 18 + 25 + 26 + 24 + 33) on 2026-09-10.
The checks test declared witnesses, gauge controls and simple dependency records.
They do not certify continuous physical data, general bundle consistency, actual
calibration uncertainty or interscale hardness conversion.

M4 selection analysis is complete; independent grading is not. Next work should
test a small fixed set against a matched baseline with the same supplied physical
information, and audit E2/E3 plus false-safe decisions. See
[research assessment](../ASSESSMENT_2026-09-10.md). BB1 evidence reconstruction
remains open; no kernel expansion is justified by this batch.
