# M007 — memory response, first analysis

Date: 2026-09-09. Kernel v0.4 unchanged. Status: source-verified, single-analyst provisional assessment.
Selection was frozen in `CORPUS_M4_01.md` before this analysis.

## External basis and declared setup

David Tong, [Kinetic Theory, chapter 4](https://www.damtp.cam.ac.uk/user/tong/kintheory/four.pdf),
section 4.1.1, equations (4.4)–(4.6), treats linear response as an integral of a
response function against a source. Time-translation invariance permits dependence
on time difference. Section 4.1.2 treats causality. The first attempt used search
excerpts because Cambridge PDF retrieval failed. On continuation, the relevant
passages were read in the author's [chapter mirror](https://davidtong.org/pdfs/teaching/kinetic-theory/kinetic4.pdf),
printed pp. 80–83 (PDF pages 2–5). The integral, time-translation assumption and
vanishing response at negative time are verified against the full extracted text.

The following exponential relaxation model and pulse pair are our constructed
test instance, not examples attributed to Tong. Fix a causal scalar linear system,
zero remote-past response, unit static gain and relaxation time tau > 0:

`y(t) = integral_{-infinity}^{t} exp(-(t-s)/tau)/tau * f(s) ds`.

Equivalently this chosen model satisfies `tau dy/dt + y = f`. Treat that equation
as a model/constitutive commitment, not a grammar-derived identity. Input and output
have the same quantity dimension; the kernel has dimension inverse time.

## Semantic parse

- Property: response of system S in an identified trial R at observation time t.
- Grounding: S and R. A trial is a referent for a specified preparation and driving
  experiment; it is not an unspecified `History` object containing the answer.
- Roles: source input and response output remain distinct typed families.
- Reference: response measured from the same equilibrium baseline in both trials.
- Indices/resolution: f[S,R](s), y[S,R](t); s and t are real time arguments, not
  mandatory Entity slots. This uses ordinary mathematical application after grounding.
- Conditions: same S, kernel, tau, baseline and remote-past condition; small drive.
- Prerequisites: ordered time, integration measure and an integrable causal kernel.
- Construction: typed multiplication and integral binding s; t remains free.
- EntityMap genealogy: none is required for this instance.
- Representation: full input function and kernel; a frequency representation would
  require its own transform/domain contract and is not used in this test.
- Projection: retain only current drive f[S,R](0), dropping earlier samples.
- Value structure: scalar-valued time families and a response functional.
- Quantify/dimension: quantity-valued input/output; no numerical measurement inference.
- Naming yield: explanatory only; no prediction of conventional vocabulary claimed.

Schematic existing-grammar expression:

```text
ConstitutiveRelation(
  y[S,R](t),
  Integral(s in (-infinity,t], K[S](t-s) * f[S,R](s), ds)
)
```

S/R remain focal, s is mathematically bound, and t plus tau and the initial-condition
contract remain explicit. The time-function signatures are written as mathematical
metadata because v0.4 does not freeze their complete surface syntax. This is an
encoding proposal, not a new `History`, `TimeIndex` or `Condition` primitive.

## Concrete projection counterexample

Use time units tau=1. Let f_A(s)=0 everywhere. Let f_B(s)=a on [-2,-1] and zero
elsewhere, with a=0.01. At t=0 both current inputs are zero, but:

`y_A(0)=0`

`y_B(0)=a * (exp(-1)-exp(-2)) > 0`.

Let X be admissible input functions for the fixed model, pi(f)=f(0), and
P(f)=y_f(0). This pair has pi(f_A)=pi(f_B) but P(f_A)!=P(f_B). Therefore no
Pbar with P=Pbar composed with pi exists on X: **current-input-only is unsafe
for predicting current response**. Retaining a trial name alone cannot repair
this unless it provides access to additional data, which changes the projection.

This refutes that reduction, not the PG kernel. Full history plus the declared
kernel suffices for this question. Also, this exponential model permits a compact
state y(t): do not conclude that all future prediction requires the entire history,
or that arbitrary kernels admit the same finite state compression.

`experiments/pgcheck/pgcheck.py` checks the positive response by midpoint integration
against the analytic expression. It does not automatically derive the factorization
counterexample or validate the physical model.

## Knowledge and provisional assessment

- [G]: grounding, typed composition, binding, distinct constitutive relation,
  and explicit projection/factorization criterion.
- [M]: real-valued functions, integration, exponential kernel and elementary ODEs.
- [D/model]: which input/output are physically paired, linear regime, relaxation
  law and initial preparation. The input history is data, not an invented seed.
- Candidate grade: **G3 / E1**, for this explicitly model-conditioned instance.
  G3 follows from the relation under test, not from the word "history". E1 reflects
  ordinary function/domain annotations, with no opaque history wrapper.
- Assessment: **G3 / E1, provisional** after source and local encoding review.
  Independent review is still outstanding; this is not a second independent encoding.
- Pressure: formal non-Entity argument signatures and condition metadata remain
  underspecified; the current spike cannot check them. This alone is not G4.
- Revision decision: none. Next probe is whether M008's path-dependent preparation
  needs substantially less transparent structure than this linear case.

## Encoding review on continuation

The test's source space is the explicit input function, not a trial label. Thus
the counterexample remains valid after replacing R with two fully specified drives.
Ordinary function application and integration carry the history; a fresh History
primitive is unnecessary for this instance. A bare `y[S,R](t)` without the displayed
constitutive expression would be insufficient evidence of expressibility.

The spike's Entity-only binders do not implement the real-time argument of this
parse. We therefore retain the distinction between a hand-reviewed grammar encoding,
a numerical witness, and an executable PG type derivation. Only the first two are
provided here. General history dependence and hysteresis remain untested.
