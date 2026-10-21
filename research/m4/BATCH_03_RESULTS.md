# M4 batch 3 — 2026-09-10

Frozen targets M003/M004/M005/M006. Source passages checked; all comparisons
below are our constructions, not measurements or examples attributed to the sources.
Single-analyst provisional assessment, not independent replication. Kernel v0.4
unchanged; 12/20 M4 targets now analyzed, eight unassessed. BB1 totals unchanged.

## 쉽게 읽는 이번 결과

- **M003 — 어떻게 누르느냐도 물리량의 일부다.** 같은 기체를 같은 상태에서
  눌러도 온도를 유지할 때와 엔트로피를 유지할 때의 압축률은 다를 수 있다.
  따라서 `부피를 압력으로 미분`이라는 모양만 남기면 부족하다.
- **M004 — 반응을 허용하는지도 기록해야 한다.** 혼합물을 데울 때 성분의
  양을 고정하는 경우와 화학반응으로 성분 비율이 바뀌도록 두는 경우를 비교했다.
  출발 상태가 같아도 열에 대한 반응이 다르다.
- **M005 — 이쪽의 움직임은 저쪽에서 누른 힘에도 달려 있다.** 두 지점이
  연결되어 있으면 A에서 가한 힘만 알아서는 A의 변위를 예측할 수 없다.
  계산에서 B에 대한 합을 끝냈다고 B의 영향까지 사라지는 것은 아니다.
- **M006 — 각각 얼마나 흔들리는지와 함께 어떻게 흔들리는지는 다르다.**
  두 지점의 흔들림 크기가 같아도, 함께 움직이거나 반대로 움직일 수 있다.
  각 지점의 분산만 남기면 둘 사이의 상관관계는 복원되지 않는다.

여기서 발견한 반례는 **정보를 지나치게 생략한 표현의 실패**다. 아직은
Physical Grammar 자체가 이런 차이를 표현할 수 없다는 반례가 아니다.
또한 “검증 통과”는 아래 예제의 계산과 일부 의존성 기록이 맞다는 뜻이며,
문법 전체의 완전성이나 실제 물질 모델의 정확성을 입증한다는 뜻은 아니다.

| Case | Provisional G/E | Specific unsafe reduction |
|---|---|---|
| M003 | G2/E1 | Constrained compressibility expression -> derivative with its fixed condition erased |
| M004 | G3/E2 | Thermal response specification -> same starting state and dH/dT skeleton without reaction path |
| M005 | G3/E1 | Full applied force vector -> force at observation site alone |
| M006 | G1/E1 | Two-point covariance -> coincident-point variances |

G2 in M003 scores the definitions; its numerical gas witness additionally uses a
G3 model. M004/M005 score the chosen physical response predictions. M006 takes
physically interpreted finite joint distributions as input, as in M020. No grades
are inferred by code. E2 in M004 records explicit constraint-manifold scaffolding
and a real encoding ceiling; it is not silently counted as effortless success.

## M003 — isothermal versus isentropic compressibility

### Source and domain

[NIST REFPROP 8 manual](https://www.nist.gov/system/files/documents/srd/REFPROP8_manua3.htm),
section headed **Properties**, paragraph beginning “Derivative thermodynamic
properties”, gives the normalized negative volume derivative at fixed T and at
fixed entropy. Its latter label is adiabatic compressibility. We use **isentropic**
to name the fixed-S derivative precisely. Tong, [Classical Thermodynamics](https://davidtong.org/pdfs/teaching/statistical-physics/statphys4.pdf),
section 4.3.3, printed pp. 122-123, distinguishes entropy preservation in reversible
adiabatic processes from entropy increase allowed in irreversible insulated ones.
These passages were read on 2026-09-10. No assumption that all adiabatic processes
are isentropic is made here.

Fix a closed, single-phase simple compressible system A, fixed species amounts
n_i, no reaction, and a differentiable equilibrium neighborhood away from phase
boundaries. All additional work coordinates, if present, must be fixed explicitly;
our minimal system has none. Require V>0 and an admissible pressure derivative.

`kappa_T[A]=-(1/V[A])*(partial V[A]/partial p[A])_(T[A], all n_i[A])`

`kappa_S[A]=-(1/V[A])*(partial V[A]/partial p[A])_(S[A], all n_i[A])`.

### Semantic parse

| Field | Content |
|---|---|
| Property | Fractional volume response to pressure under a specified constraint. |
| Grounding | Same closed material system A and evaluation state q. |
| Roles | V is response; p is varied control; T or S specifies the path. |
| Reference | Same equilibrium branch and state coordinates. |
| Indices/resolution | Every species i is enumerated in the fixed-composition header. |
| Conditions | Fixed T or fixed S, all n_i fixed; positive V and smooth single-phase domain. |
| Prerequisites | State manifold and constrained differentiation. |
| Construction | Negative pressure derivative divided by the same bearer's volume. |
| Representation | V(T,p,n) or V(S,p,n) are coordinate descriptions with explicit constraints. |
| Projection/elimination | Erase T/S from the derivative record; retain bearer, state, dimension and arithmetic skeleton. |
| Value structure | Scalar response coefficient. |
| Dimension/Quantify | Pa^-1; each constrained definition admits a quantity view. |
| Naming | Isothermal/isentropic modifiers preserve the differentiating condition. |

No EntityMap is required. A and its species genealogy remain on both sides of
each definition. T/S are Properties of A, not newly invented Condition Entities.

### Witness and knowledge

Our calorically perfect ideal gas has pV=nRT and constant positive Cv, with
gamma=Cp/Cv>1. At fixed n, `dS=Cv*dT/T+nR*dV/V`. Setting dT=0 yields
`kappa_T=1/p`; setting dS=0 yields `kappa_S=1/(gamma*p)`.
Choose gamma=5/3 at the same p0,T0,V0 and composition: normalized values p0*kappa
are 1 and 3/5. The two inputs to the erasure map are **expression-plus-condition
records**, not two different thermodynamic states. Their erasures coincide but
their evaluated responses differ: **unsafe** to recover the specified coefficient.

Retaining the constraint and the equation of state plus caloric relation suffices
for this calculation. Merely retaining the word compressibility does not.
Equal numerical coefficients in a special material would not erase the semantic
difference between the definitions.

[G]: grounded definitions and condition-preserving construction. [M]: derivative,
chain rule and normalization. [D]: thermodynamic meanings of V,p,T,S and the two
compressibility definitions. **G2/E1** for definitions; ideal-gas/caloric physics
is extra [D/model] used for the witness. No G4 found.

## M004 — equilibrium reaction path versus frozen composition

### Source and domain

Howard DeVoe, [Thermodynamics and Chemistry, section 11.9](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/DeVoes_Thermodynamics_and_Chemistry/11%3A_Reactions_and_Other_Chemical_Processes/11.09%3A_Effects_of_Temperature_and_Pressure_on_Equilibrium_Position),
equations (11.9.1), (11.9.5)-(11.9.8), expresses reaction equilibrium as a minimum
of G along the extent coordinate and derives the temperature-induced change of
equilibrium extent. This authored textbook reproduction was read on 2026-09-10.
IUPAC entry retrieval was unsuccessful; no full-text verification of those entries
is claimed. The construction below instantiates the frozen target using enthalpy
response rather than leaving “chemical response” unspecified.

Fix a closed system A with one reaction X <-> Y, pressure p0, total amount N>0,
and x=n_Y/N in (0,1). Species balance is n_X=N(1-x), n_Y=Nx; an extent increment
d_xi=N*dx has stoichiometric changes (-d_xi,+d_xi). Conserved total N is not the
same constraint as independently fixed n_X and n_Y.

Define two derivatives at the same initial equilibrium state:

- Frozen composition: `C_fr=(partial H/partial T)_(p,n_X,n_Y)`.
- Equilibrated reaction: `C_eq=d H(T,p0,x_eq(T))/dT`, with N fixed,
  `G_x(T,p0,x_eq)=0`, `G_xx>0`.

The second is a derivative of a composition along a constrained branch. Locally,
the implicit function theorem gives `dx_eq/dT=-G_xT/G_xx` and hence
`C_eq=H_T-H_x*G_xT/G_xx`, while `C_fr=H_T`. The branch and regularity condition
are essential. At G_xx=0 this formula cannot be applied by dividing by zero.

### Semantic parse

| Field | Content |
|---|---|
| Property | Isobaric enthalpy response with frozen or equilibrated composition. |
| Grounding | Closed sample A; reaction R with identified species and stoichiometry. |
| Roles | T drives response; H responds; x is the internal composition coordinate. |
| Reference | Same p0,T0,N,x0 and same enthalpy convention. |
| Indices/resolution | Species X/Y resolved; x_eq(T) obtained on a specified local branch. |
| Conditions | Fixed p,N and G_x=0,G_xx>0 for equilibrium; fixed p,n_X,n_Y for frozen case. |
| Prerequisites | Differentiable G/H, mass balance, implicit function theorem and chain rule. |
| Construction | Differentiate H composed with T -> (T,p0,x_eq(T)); contrast with fixed-x derivative. |
| Representation | x or extent xi, with retained N and stoichiometric conversion. |
| Projection/elimination | Erase the branch/constraint while retaining starting state and dH/dT skeleton. |
| Value structure | Scalar response coefficient; x_eq is a derived mathematical function. |
| Dimension/Quantify | J/K for both C values; x dimensionless, xi in mol. |
| Naming | Frozen-composition versus reaction-equilibrated heat response must remain qualified. |

R identity is the declared reaction and species balance, not an opaque container
for the answer. A remains traceable through G,H and both amount functions. Existing
Constraint relations record G_x=0 and the admissible domain; ordinary composition
and differentiation build C_eq. The spike's `derivative(fixed=...)` alone does
**not** encode the full implicit branch. No new grammar node is added to hide that
limitation. E2 records this substantial, transparent mathematical scaffolding.

### Thermodynamically consistent constructed pair

At fixed p0 use an ideal-mixture model (all energies per mole before multiplication
by N): `g0(T)=-c*T*ln(T/T0)`, `Delta g0(T)=h*(1-T/T0)`, with c,T0>0.

`G=N*(g0(T)+x*Delta g0(T)+R*T*(x ln x+(1-x) ln(1-x)))`.

This is a model on the p0 slice; it does not prescribe pressure dependence.
Using `H=G-T*G_T` at fixed p,x yields `H=N*(c*T+h*x)`.
At T0 the equilibrium is x0=1/2, with G_xx=4NRT0>0. Its tangent is
`dx_eq/dT=h/(4RT0^2)`, giving

`C_fr=Nc`, `C_eq=Nc+N*h^2/(4RT0^2)`.

Choose c=R,h=RT0. Normalized by NR the two results are **1 and 5/4** at the
same starting state. The constraint-erasing projection is **unsafe** for thermal
response. These are alternative allowed paths from one state, not a claim that
two different states share one full thermodynamic identity. Frozen composition
can be approximated on times shorter than chemical relaxation while allowing
thermal equilibration; reaction equilibrium describes the slow limit. No actual
relaxation times or experimental realization are predicted by this static model.

The h=0 control gives equal thermal responses. A valid generic descriptor must
still preserve the path even when one special model gives coincident numbers.
Keeping G_xT/G_xx and H_T/H_x at the state is **safe** for this regular local
derivative through the displayed formula; it does not determine finite paths.

[G]: grounding, separate Constraint/Definition/ConstitutiveRelation statements.
[M]: implicit differentiation and composition. [D/model]: reacting ideal-mixture
G, enthalpy identity and equilibrium/frozen regimes. **G3/E2** for the specified
prediction. The general constrained-derivative construction is not itself a new
physical law. Independent review of this E2 versus E3 boundary remains open.

## M005 — spatially nonlocal linear response

### Source and domain

Tong, [Kinetic Theory, chapter 4](https://davidtong.org/pdfs/teaching/kinetic-theory/kinetic4.pdf),
section 4.4, printed p. 99, equations (4.39)-(4.41), retains independent observation
and source coordinates in a response integral; translation invariance is stated
before replacing them by coordinate differences. The passage was read on
2026-09-10. Our static mechanical example is not a QFT prediction from that text.

For a static response family write
`u[A,R](x)=integral_U K[A](x,x') f[A,R](x') dmu(x')`.
Require an integrable kernel/source on the declared domain and measure. R identifies
the loading trial. x is the observation site and x' the source site; they need not
coincide. No translation invariance or reciprocity is assumed by the grammar.

### Semantic parse

| Field | Content |
|---|---|
| Property | Response field, given a source field and a response kernel. |
| Grounding | Mechanical system A, loading trial R, observation/source sites in its domain. |
| Roles | First kernel slot receives response; second receives drive. |
| Reference | Fixed geometry, support conditions, coordinate axes and unloaded baseline. |
| Indices/resolution | x remains free; x' is bound by integration, with dmu retained. |
| Conditions | Declared linear static regime, domain and boundary conditions. |
| Prerequisites | Linear maps, integration or finite sums, admissible function spaces. |
| Construction | Multiply K(x,x') by f(x') and bind only the source coordinate. |
| Representation | Kernel integral or finite-site matrix; matrix rows/columns retain physical roles. |
| Projection/elimination | Test pi(f)=f(x_A). Binding x' in the complete expression is not itself this projection. |
| Value structure | Linear response operator and displacement/source fields. |
| Dimension/Quantify | In the finite force/displacement example K: m/N; continuous kernel units also include inverse measure units. |
| Naming | Compliance from source site to observation site; a scalar compliance label can hide these slots. |

### Witness, retained genealogy and account

Our system has two displacement coordinates u_A,u_B, each attached to a support
by stiffness k>0 and connected to each other by another spring k. Its potential is
`W=(k/2)*(u_A^2+u_B^2+(u_A-u_B)^2)-f_A*u_A-f_B*u_B`.
Minimizing gives `k*[[2,-1],[-1,2]]*u=f`; therefore
`K=(1/(3k))*[[2,1],[1,2]]`. Positive stiffness eigenvalues k,3k ensure a unique
stable response. The finite site domain carries counting measure.

With force scale F0, drives (F0,0) and (F0,F0) agree at A but give u_A equal to
2F0/(3k) and F0/k. Thus local-force projection is **unsafe** for local response.
The output expression still contains `K_AA*f_A+K_AB*f_B`; the source-site binder
has closed a free index without discarding the source function's contribution.

For a second reduction retaining only u_A, drives (F0,0) and (0,2F0) produce the
same u_A but different f_B, so that source-recovery query is **unsafe**. However,
the **full** response vector retains the full force vector here via the invertible
stiffness matrix. Summation/integration is not automatically information loss.
This example is reciprocal because of its specified spring energy; symmetry of
this K does not license swapping semantic source/response roles in other models.

[G]: ordered grounding, source binding, retained system/trial genealogy.
[M]: linear algebra, finite sum and minimization. [D/model]: Hookean spring
potential and static equilibrium. **G3/E1** for the displacement prediction.
Dependency sketches test correct source binding and surviving observation site;
they do not validate physical kernel units or reciprocity.

## M006 — two-point covariance versus local variance

### Source and domain

Tong, [Statistical Field Theory, chapter 2](https://davidtong.org/pdfs/teaching/statistical-field-theory/sft2.pdf),
section 2.2, printed pp. 39-40, equation (2.16) and the following source-derivative
calculation, separates the connected two-point function from the product of means.
The relevant passage was read on 2026-09-10. We use finite, real classical random
variables so coincident products exist; no continuum ultraviolet limit or quantum
operator ordering is being presumed.

For preparation ensemble R on system A with two sites x_A,x_B at fixed separation
d>0, define `C_R(x,y)=E_R[(X(x)-E_R X(x))*(X(y)-E_R X(y))]`.
Then C_R(x,x)=Var_R X(x). Require finite second moments. The coincident-point
restriction retains both local variances, not just a single averaged variance.

### Semantic parse

| Field | Content |
|---|---|
| Property | Connected spatial covariance and its diagonal variance view. |
| Grounding | System A, preparation ensemble R, two identified sites. |
| Roles | First/second evaluation sites; classical covariance symmetry does not remove their references. |
| Reference | Fixed sampling time, site geometry and value calibration. |
| Indices/resolution | x and y resolved independently; expectation binds random outcome omega. |
| Conditions | Normalized joint probability, finite second moments, same spatial separation d. |
| Prerequisites | Probability, expectation, centering and product sample space. |
| Construction | Product of centered fields followed by expectation; then restrict y=x for variance. |
| Representation | Joint table -> symmetric covariance matrix; the table-to-covariance step can itself lose higher moments. |
| Projection/elimination | pi(C)=(C_AA,C_BB), discarding the off-diagonal relation at separation d. |
| Value structure | Positive-semidefinite covariance matrix; diagonal entries nonnegative. |
| Dimension/Quantify | Covariance has the square of the field's units; normalized +/-1 site readings here are dimensionless. |
| Naming | Two-point covariance versus local variance; neither is automatically normalized correlation. |

### Exact comparison and account

Use normalized site readings X_A,X_B in {-1,+1}. In row/column order (-1,+1),
our preparation tables are `p_plus=((3/8,1/8),(1/8,3/8))` and
`p_minus=((1/8,3/8),(3/8,1/8))`. All probabilities are strictly positive and both
site marginals are uniform. Both means are zero and local variances are one,
but C_AB=+1/2 and -1/2. The covariance matrices have eigenvalues 1/2 and 3/2,
so the pair does not rely on inadmissible or singular covariance data.

Thus pi is **unsafe** for the sign/value of covariance at separation d, even if
both local means are also retained. Conversely Var_A+Var_B is **safe** from the
diagonal. The variance of X_A+X_B is 3 versus 1 and is **unsafe**, because it
contains the missing cross term 2C_AB. Choosing independence would insert C_AB=0,
not recover either ensemble. These finite joint tables are valid preparations;
no equilibrium interaction law is assumed or derived for them.

[G]: grounded ensemble/sites and explicit outcome binding/restriction.
[M]: finite probability, centering and covariance. [D]: supplied physical meaning
of calibrated site readings and their joint preparation. **G1/E1** given that
input, not a derivation of statistical physics. This is complementary to M020:
M020 projects a joint distribution to marginals; here the specified map is the
diagonal restriction of a covariance function. No decay length is inferred from
just two sites. No G4 established.

## Evidence and next work

Run `python experiments/pgcheck/m4_batch3_checks.py`. The existing finite collision
finder is reused. New checks cover exact comparison pairs, thermodynamic tangent
conditions, a finite-difference check of the reacting model, source binding,
covariance domain validity and controls. They do not solve arbitrary constraints,
check value types/dimensions or certify G/E scores.

Validation checkpoint: 26 batch 3 checks passed; together with the existing
33 + 18 + 25 checks, the four scripts pass **102 checks**.

The main new pressure is M004: a list of fixed variables is insufficient to
describe a reacting equilibrium branch. The frozen language can provisionally
host its explicit mathematical construction, but this needs an independent
naturalness review before claiming broad constraint support.

Next bounded batch: M001/M002 (roles) and M013/M014 (observer dependence).
Then M011/M012/M017/M018 remain. BB1 retrospective accounting is still open.
No new primitive or kernel revision is justified by the current evidence.
