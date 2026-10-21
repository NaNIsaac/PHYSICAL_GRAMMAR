# M010 — local fields versus loop phase

Date: 2026-09-09. Kernel v0.4. Status: source-verified, single-analyst provisional.

## External basis

Tong, [Quantum Hall Effect, chapter 1](https://davidtong.org/pdfs/teaching/quantum-hall-effect/qhe1.pdf),
section 1.5.3, printed pp. 35–38, especially equation (1.49) and the following
general-charge statement: transport around enclosed magnetic flux contributes
the phase factor exp(i q Phi / hbar). The setup keeps the particle out of the
magnetic-field region. This record uses that physical input; the comparison below
is our test construction. The full chapter's relevant text was retrieved.

## Declared domain and semantic parse

Fix a static, impenetrable flux tube and an accessible annular region U. There are
no electric or magnetic fields in U. Fix charge q != 0, an oriented closed loop C
of winding one, and matching boundary/preparation conventions. Compare backgrounds
with different flux; do not change the topology or observation loop.

| Parse field | Explicit content |
|---|---|
| Property | Electromagnetic loop phase factor for C and a charge-q probe. |
| Grounding | Background configuration B, accessible region U, loop C, probe species Q. Each has a specified referent, not a wrapper for the answer. |
| Roles | B supplies the connection, C is the oriented integration path, Q supplies charge. |
| Reference | Orientation and sign of q fixed; compare relative interference phase. |
| Indices/resolution | Path parameter s is bound; connection retains position dependence on U. |
| Conditions | Static excluded tube, fixed U/C, admissible gauge transformations with single-valued probe transformation. |
| Prerequisites | U(1) connection, loop topology, complex phase and line integration. |
| Construction | W[B,C,Q] := exp(i q[Q]/hbar * integral_C A[B](x) dot dx). |
| Representation | A is gauge-dependent; W is invariant under the declared admissible transformations. |
| Projection | pi(B)=(E restricted to U, Bfield restricted to U), with U, C and q fixed as context. |
| Value structure | W is a unit complex number; its angle is defined modulo 2 pi. |
| Dimension/Quantify | Phase exponent is dimensionless in the conventional view; this is a phase representation, not a measurement value. |
| Naming | “Loop phase” explains construction; conventional eponym is external vocabulary. |

The formula is a definition of the loop functional. Identifying it with the
interference phase uses the electromagnetic quantum coupling law. Keep those two
relations distinct. No claim is made that a single W identifies the whole background.

## Counterexample and controls

Choose fluxes Phi_0=0 and Phi_1=pi*hbar/q. Both projected field pairs are zero
everywhere in U, while W_0=1 and W_1=-1. Consequently W cannot factor through pi
on this domain: **unsafe** for the loop-phase query. Stokes' theorem is not violated:
a surface spanning C cannot lie wholly inside the field-free annulus.

As a negative control, Phi_2=2*pi*hbar/q gives W_2=1. Different enclosed fluxes
do not always produce different loop phases. Gauge equivalence is likewise not
equivalent to equality of local field tensors without global/domain conditions.

The executable witness uses the exact coordinate a=q*Phi/(2*pi*hbar), with phase
class a modulo 1. Values 0, 1/2 and 1 avoid numerical trigonometric tolerances.
This is a representation of the stated U(1) phase, not a new physical law.

## Knowledge accounting and assessment

[G]: ordered grounding, binding, relation classification and explicit projection.
[M]: one-forms/line integration, topology, complex exponential and quotient R/Z.
[D/model]: electromagnetic connection and the charged-probe phase law.

**G3 / E2, provisional**, scoring the physical phase prediction, not just the
mathematical definition of W. E2 reflects the explicit domain, admissible gauge
group and quotient typing required. These are transparent established mathematics;
no opaque `GaugeClass` seed is used. v0.4 can host this mathematical expression,
but it does not provide an executable gauge-equivalence judgment. This distinction
needs independent review before any pass or kernel-failure conclusion.

Pressure: a generic claim that field strength preserves all physical semantics
would be false on this domain. The successful counterexample targets that contract,
not the existing factorization principle. No kernel change is proposed.
