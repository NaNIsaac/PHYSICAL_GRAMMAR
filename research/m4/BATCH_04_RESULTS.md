# M4 batch 4 — 2026-09-10

Frozen targets M001/M002/M013/M014. Single-analyst provisional analysis;
16/20 targets analyzed, four unassessed. Kernel v0.4 and historical BB1 totals
unchanged. Numerical pairs below are our constructions, not source experiments.

## 쉽게 읽는 이번 결과

- **M001:** A를 밀어 B에서 읽는 실험과 B를 밀어 A에서 읽는 실험은 역할이
  다르다. 대칭적인 스프링에서는 값이 같지만, 그 대칭은 모델에서 나온다.
- **M002:** 두 물체 이름을 일관되게 바꾸면 반발계수는 변하지 않는다.
  그렇다고 어느 물체의 속도인지, 충돌 전인지 후인지 지워도 된다는 뜻은 아니다.
- **M013:** 같은 입자의 같은 사차원 운동량이라도 관측자에 따라 에너지가
  다르다. 반면 입자와 관측자를 함께 다른 좌표로 표현하면 에너지는 같다.
- **M014:** 같은 전자기장을 관측자마다 전기장·자기장으로 다르게 분해한다.
  두 장을 모두 보존하는 좌표변환은 되돌릴 수 있지만 전기장만 남기면 일반적으로 부족하다.

이번에도 특정 정보 생략의 실패와 문법 자체의 실패를 구분한다.
검증 코드는 아래 계산과 제한적인 의존성 기록을 확인하며 G/E 등급을 판정하지 않는다.

| Case | Provisional G/E | Result |
|---|---|---|
| M001 | G3/E1 | Reciprocal spring values coincide; ordered response/drive roles remain distinct. |
| M002 | G2/E1 | Consistent relabeling preserves e; e alone cannot recover body-specific velocity. |
| M013 | G2/E1 | Erasing observer from (p,u) is unsafe for assigned energy. |
| M014 | G2/E1 | Complete field transformation is reversible; electric-only reduction is unsafe. |

G2 scores supplied physical definitions and transformation semantics, not their
derivation from PG. M001 scores the chosen spring prediction and its reciprocity
assumptions, hence G3. Naturalness and final grading require independent review.

## M001 — reversed cross response

Source checked 2026-09-10: Tong, [Kinetic Theory, chapter 4](https://davidtong.org/pdfs/teaching/kinetic-theory/kinetic4.pdf),
section 4.1.1, printed pp. 80–81, equations (4.4), (4.6). The first matrix index
selects the responding observable and the second the source. This passage supplies
the linear-response setup, not a general reciprocity guarantee.

Our static model consists of two displacement coordinates x_A,x_B with matching
force controls f_A,f_B, common fixed axes and supports. Let
`V=k*(x_A^2+x_B^2+(x_A-x_B)^2)/2`, k>0. Equilibrium is
`K*x=f`, `K=k*((2,-1),(-1,2))`; thus
`chi=K^-1=((2,1),(1,2))/(3k)` and
`chi[A,B] := (partial x_A/partial f_B)_(f_A)=1/(3k)`.
The reversed experiment has `chi[B,A]=1/(3k)` too. Symmetry follows here from
the smooth conservative quadratic potential, conjugate force/displacement
coordinates and invertible stiffness. It is a model consequence, not a syntax rule;
no general Onsager claim or nonreciprocal material example is inferred.

| Field | Content |
|---|---|
| Property | Static cross compliance. |
| Grounding | Coupled system S and its physically identified subsystems A,B. |
| Roles | First slot responds, second is driven. |
| Reference | Same supports, axes and zero-load baseline. |
| Indices/resolution | Two separate displacement/force coordinates. |
| Conditions | Static equilibrium, k>0; other force held fixed. |
| Prerequisites | Differentiable potential and invertible Hessian. |
| Construction | Differentiate response coordinate with respect to drive coordinate. |
| Representation | Ordered matrix in the declared subsystem basis. |
| Projection/elimination | Ordered pair -> unordered pair; separately, coefficient -> value. |
| Value structure | Scalar entry in a two-by-two linear map. |
| Dimension/Quantify | m/N. |
| Naming | Compliance at A due to force at B, and its reversal. |

S identity is the same coupled assembly; A/B identity follows the mounted bodies,
not their printed names. Ground `Displacement[S,A]`, `Force[S,B]`, retaining the
other force in the derivative condition. Declare Kx=f as ConstitutiveRelation;
the derivative is a Definition. No binder or new Role Entity is needed.

For the pair of experiment specifications (A,B),(B,A), forgetting order is
**unsafe** for the query “which body is driven”: answers B and A differ. It is
**safe for the cross-compliance value on this restricted spring domain**, since
both orders factor through 1/(3k). The finite collision search correctly returns
unknown for that value query; the analytic symmetry supplies the safe proof.
Equal values must not be advertised as a numerical role-loss counterexample.

[G]: ordered grounding and derivative genealogy. [M]: Hessian inversion and
differentiation. [D/model]: potential, force conjugacy and static regime.
**G3/E1**, no G4 established. Root-dependency sets alone cannot detect reversal.

## M002 — restitution and relabeling

Source checked 2026-09-10: Steeneken, [Introductory Dynamics, section 8.5](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Introductory_Dynamics:_2D_Kinematics_and_Kinetics_of_Point_Masses_and_Rigid_Bodies_(Steeneken)/02:_Dynamics_of_Point_Masses/08:_Impulse_and_Momentum/8.05:_Collisions),
sections 8.5.1 and 8.5.3, equations (8.25)–(8.26). The authored textbook
specifies the impact axis and before/after velocities in the center-of-mass frame.
Subtracting the two equations yields the relative-normal ratio used here.

Restrict to isolated, head-on collisions of two equal positive masses, smooth
nonrotating bodies, fixed impact normal n from A toward B, and passive restitution.
Set `g_minus=(v_B_minus-v_A_minus) dot n<0`,
`g_plus=(v_B_plus-v_A_plus) dot n>=0`, `e=-g_plus/g_minus`.
Require 0<=e<=1 in this restricted domain; this is not a universal claim excluding
superelastic collisions. Grazing/zero-approach events are outside the ratio domain.

| Field | Content |
|---|---|
| Property | Normal coefficient of restitution for a specified impact. |
| Grounding | Bodies A,B and collision event C. |
| Roles | Ordered velocity subtraction; before denominator, after numerator. |
| Reference | Common inertial frame and normal oriented A -> B. |
| Indices/resolution | Immediate pre/post stages selected from the same C. |
| Conditions | Head-on impact, nonzero approach, isolated equal masses, passive domain. |
| Prerequisites | Contact geometry and normal-velocity definition. |
| Construction | Negative ratio of post/pre relative-normal velocities. |
| Representation | Consistent body renaming and normal reversal. |
| Projection/elimination | Full velocity record -> e; or discard pre/post annotations. |
| Value structure | Nonnegative scalar in this domain. |
| Dimension/Quantify | Dimensionless quantity; not a complete collision description. |
| Naming | Normal restitution of C between A and B. |

Reuse `Before[C]` and `After[C]` EntityMaps from B005's existing sketch. Expand
each relative-normal velocity into the ordered velocity difference and dot product
with `Normal[A,B,C]`. C identity is the same encounter of those bodies; its two
stages are not arbitrary containers. The ratio is Definition; momentum conservation
is Law. No binding occurs. Existing spike B005 does not validate the normal or domain.

Construct trial 1 (velocity units retained): before (1,-1), after (-1/2,1/2).
Trial 2 adds a common +1 velocity: before (2,0), after (1/2,3/2).
Both conserve momentum and have e=1/2; their A post-velocities differ. Projection
to e is **unsafe** for that body-specific query. Consistent A/B exchange together
with n -> -n preserves both g values and e, hence is **safe for e**.
It is a renaming operation, not a new asymmetric material response.

Swapping the pre/post arithmetic slots produces 2 instead of 1/2, but also
violates the stated approaching/separating domain. That is an invalid encoding
control, **not a pair of admissible passive collisions** proving information loss.
[G]: ordered bodies and derived stages. [M]: subtraction, dot product, ratio.
[D]: collision and normal-restitution definitions; conservation is extra physical
input for our constructed trials. **G2/E1** for the definition, no G4 established.

## M013 — energy relative to an observer

Source checked 2026-09-10: Tong, [Dynamics and Relativity, chapter 7](https://davidtong.org/pdfs/teaching/dynamics-and-relativity/dynrel7.pdf),
sections 7.4.2–7.4.3, printed pp. 134–137, equations (7.20)–(7.30).
It gives four-velocity normalization, p=(E/c,p_vec) and invariant inner products
with signature (+---). We derive the observer formula below by evaluating the
contraction in that observer's rest frame; it is not a verbatim source formula.

At one event q in Minkowski spacetime, take future timelike p for a particle A
of fixed mass m>0, and a future observer four-velocity u with g(u,u)=c^2.
With g=diag(1,-1,-1,-1), `Energy[A,O,q] := g(p[A,q],u[O,q])`.
In O's rest frame u=(c,0,0,0), so the contraction equals E. With signature
(-+++), use -g(p,u) instead. Metric and sign must change consistently.

| Field | Content |
|---|---|
| Property | Energy assigned by observer O to particle momentum at q. |
| Grounding | Same particle A, event q, observer O. |
| Roles | Momentum bearer and measuring observer are distinct slots. |
| Reference | Minkowski metric (+---), future orientation and c convention. |
| Indices/resolution | Both vectors belong to the tangent space at the same q. |
| Conditions | Massive particle and normalized future timelike observer. |
| Prerequisites | Lorentz metric and observer four-velocity. |
| Construction | Metric contraction p with u. |
| Representation | Simultaneous Lorentz component transformation of p and u. |
| Projection/elimination | (p,u) -> p erases observer; fixed-u energy also discards momentum detail. |
| Value structure | Scalar for a fixed physical observer. |
| Dimension/Quantify | J; p in momentum units times u in velocity units. |
| Naming | Energy of A measured by O at q. |

O refers to an independently specified observer worldline; u is its tangent at q,
not a substitute Entity invented to store an energy answer. Ground p and u as
Properties and contract them with the declared metric as ordinary mathematics.
The relation is a Definition. No observer binding or elimination is licensed.

In retained units c=m=1, use p=(1,0,0,0), u0=(1,0,0,0) and
u1=(5/4,3/4,0,0). Both observers are normalized. The projection (p,u)->p
coincides while energies are 1 and 5/4: **unsafe** for observed energy.
Apply any common Lorentz matrix to both vectors and the contraction stays equal:
this coordinate change is **safe**, a representation change, not observer erasure.

For a separate fixed-u projection, p_plus=(5/4,3/4,0,0) and
p_minus=(5/4,-3/4,0,0) have the same mass and u0-energy but different u1-energies
1 and 17/8. Retaining just one observer's energy is **unsafe** for another's.
[G]: observer-grounded composition. [M]: bilinear contraction and Lorentz algebra.
[D]: physical meanings of momentum, observer and energy. **G2/E1**; no G4.

## M014 — observer decomposition of the electromagnetic field

Source checked 2026-09-10: Tong, [Electromagnetism and Relativity](https://davidtong.org/pdfs/teaching/electromagnetism/electro4.pdf),
internal section 5.3.2, printed pp. 107–108, equations (5.15)–(5.18).
Although the download filename is electro4, this PDF uses chapter 5 numbering.
It displays the antisymmetric field tensor, its Lorentz transformation and the
x-boost electric/magnetic component formulas.

Take a field F at the same event q and two inertial frames with parallel spatial
axes, O' moving with velocity +v along O's x-axis, |v|<c. Fix the source's
component conventions and spacetime orientation. Then
`E'_x=E_x`, `E'_y=gamma*(E_y-v*B_z)`, `E'_z=gamma*(E_z+v*B_y)`;
`B'_x=B_x`, `B'_y=gamma*(B_y+v*E_z/c^2)`,
`B'_z=gamma*(B_z-v*E_y/c^2)`.

| Field | Content |
|---|---|
| Property | Electric and magnetic fields resolved by a specified observer frame. |
| Grounding | Electromagnetic field system S, event q and observer frame O. |
| Roles | Field bearer versus observer whose time/space splitting is used. |
| Reference | Orthonormal frame, metric, handedness, SI convention and boost direction. |
| Indices/resolution | Six independent tensor components at one event; no spatial averaging. |
| Conditions | Inertial frames, |v|<c, same event, known relative axes. |
| Prerequisites | Lorentz tensor algebra and electromagnetic tensor interpretation. |
| Construction | Represent F in O's tetrad; extract electric and magnetic triples. |
| Representation | Complete six-component boost, inverse obtained by v -> -v. |
| Projection/elimination | (E,B) -> E discards magnetic components. |
| Value structure | Two three-vectors, jointly encoding an antisymmetric tensor. |
| Dimension/Quantify | E in V/m, B in T; use cB to compare like-dimensional entries. |
| Naming | Electric/magnetic field measured in O at q. |

S refers to the same field configuration, q the same event; O supplies a worldline
and oriented orthonormal tetrad. Ground `FieldTensor[S,q]` and the frame data,
then use Represent and ordinary component extraction. The electromagnetic meaning
of those components is a supplied Definition. No new observer primitive, opaque
answer-bearing Entity or binder is required. A full decomposition with frame data
is invertible, so is not a lossy PG Projection despite geometric projection terminology.

Use c=1 in retained field units, v=3/5, gamma=5/4. A constant field with
E=(0,1,0), B=0 gives E'=(0,5/4,0), B'=(0,0,-3/4).
This is one field viewed by two observers, not two unequal underlying tensors.
Inverse boost restores the complete pair; E^2-B^2=1 and E dot B=0 are controls.

For an actual insufficiency pair, choose two constant fields with the same
E=(0,1,0), but B=(0,0,0) versus B=(0,0,1). Both are locally valid source-free
constant Maxwell fields. Their O' electric y-components are 5/4 and 1/2.
Thus electric-only projection is **unsafe** for another observer's electric field.
The complete pair with known frame transform is **safe** by the displayed inverse;
neither invariant pair alone is claimed to identify F.
[G]: field and observer grounding, representation versus explicit loss.
[M]: tensor/component transformations. [D]: electromagnetic decomposition.
**G2/E1**, no G4 established. Component typing remains outside the spike.

## Validation and continuation

All five scripts passed 126 checks (33 + 18 + 25 + 26 + 24) on 2026-09-10.
Run `python experiments/pgcheck/m4_batch4_checks.py`. It reuses existing collision,
matrix-inversion and genealogy helpers. Exact rational fixtures check both losses
and symmetry controls; no parser, tensor type checker or grade inference is added.
The remaining frozen targets are M011/M012/M017/M018. BB1 retrospective accounting
and independent review remain open. No new grammar primitive is justified here.
