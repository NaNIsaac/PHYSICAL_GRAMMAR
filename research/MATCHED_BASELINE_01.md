# Matched-information pilot 01 — 2026-09-10

## Finding / 판단

**이 작은 개발 실험에서 PG의 추가 판정 이득은 없었다.** 일반 식 트리와 PG
인코딩은 10개 유한 진단에서 모두 8개를 맞게 판정하고 2개를 unknown으로 남겼다.
단위 호환성만으로는 이 실험의 정보 충분성 질문에 답하지 못했다. 이 결과는
PG가 쓸모없다는 결론도, 기존 체계보다 우수하다는 증거도 아니다. 공통 수학
알고리즘의 성과와 PG 자체의 성과를 분리한 첫 실행 기준점이다.

This is an executed, single-author development pilot of the proposal in
[the assessment](ASSESSMENT_2026-09-10.md), not the full proposed comparison.
The ten inputs were designed after seeing M4. No preregistration, independent
review, blind evaluation, or physical regrading is claimed.

## Fixed task and inputs

Given a finite state domain X, retained record π(x), and downstream query P(x),
decide whether P is constant on every fiber of π. Safe means exactly that finite
statement; unsafe requires an explicit pair with equal records and unequal answers.

Every coordinate ranges independently over {0,1}. The four named families use
P=a-b (role and observer) or P=a+b (constraint and history). Each has a drop case
π=(a,) and a complete-record reordering π=(b,a). The two controls are P=x with
π=(x+y,x-y), and P=x-x with π=(y,).

M001/M003/M013/M007 motivate the names only. These scalar expressions are **not**
spring response, thermodynamic derivatives, relativistic energy, or a constitutive
memory model. In particular, a binary coordinate called branch is not a solved
constraint manifold. The four families are structurally duplicated diagnostics:
ten rows are not ten independent mechanisms or ten validated physical cases.

Inputs provide the same expressions, coordinate identities, tuple ordering and
complete finite domains to every method. No safe/unsafe label, preserves/loses
contract or list of query-specific required distinctions is supplied. Dependency
sets are computed from the expressions. The output JSON contains reference labels;
it must never be reused as checker input.

## Methods and attribution

- **Dimension-only abstention baseline:** all selected expressions have compatible
  supplied dimensions. Returns unknown for semantic sufficiency. This is a narrowly
  specified baseline, not an implementation or evaluation of a unit-checking library.
- **Generic expression tree with explicit context:** named scalar coordinates and
  ordered arithmetic constructors; computes syntactic free variables.
- **PG adapter:** translates the same input to existing `Entity`, `prop`, and `math`
  records, then calls existing `pgcheck.dependencies`. No kernel code changed.

Both expression methods use identical decision rules: direct retention of every
syntactically used coordinate proves safe; otherwise a finite collision proves
unsafe; otherwise return unknown. They share the same evaluator and collision
search. All four unsafe decisions therefore belong to shared mathematics, not a
PG-specific detector. All four safe decisions use the same dependency criterion.
PG's existing declaration-based `sufficiency` function is deliberately not used.

The reference oracle exhaustively checks all state pairs using a separate pairwise
algorithm after predictions are collected. It shares expression evaluation and
input construction with the methods, so evaluator/input errors remain a correlated
risk. There is no independent implementation or external reviewer.

## Results

| Method | Correct decisions / 10 | False-safe | False-unsafe | Unknown / 10 |
|---|---:|---:|---:|---:|
| Dimension-only | 0 | 0 | 0 | 10 |
| Generic expression tree | 8 | 0 | 0 | 2 |
| PG adapter | 8 | 0 | 0 | 2 |

The oracle finds six safe and four unsafe inputs. The two expression methods
decide four of six safe cases and all four unsafe cases. Both abstain on invertible
mixing and cancellation: syntactic dependence overapproximates semantic dependence,
and the fixed predictor does not infer inverse maps or simplify arithmetic.
An exhaustive finite-fiber classifier could decide all ten; that shared mathematical
extension would not establish a PG advantage either.

Machine-readable per-case decisions and collision witnesses are in
[MATCHED_BASELINE_01_RESULTS.json](MATCHED_BASELINE_01_RESULTS.json).

## Cost accounting and limits

All ten inputs are authored once and translated automatically to PG. There are no
per-case detector rules or manually entered loss labels. Each paired family uses
two named coordinates, one binary query constructor and one or two retained
coordinate references; the controls use the same arithmetic vocabulary. The PG
adapter adds a `Coordinate` property wrapper and Entity construction, reusing the
existing dependency walker. These are visible implementation choices, not measured
human annotation savings. Authoring/review time was not instrumented and is **not
available**. Source-line counts would not substitute for that measurement.

This generic baseline is a minimal scalar expression record, not a full typed IR.
The PG adapter exercises root dependencies only, not role validation, derivative
conditions, grounding genealogy, tensor types or binder handling. Consequently this
pilot does not complete the assessment's proposed typed-tree/physical-encoding
comparison. It tests that the comparison harness can expose equality of capabilities
without rewarding supplied answer labels.

## Reproduction and next gate

Run `python experiments/pgcheck/matched_baseline.py` from the repository root with
Python 3.10+. It prints JSON and validates encoding dependency agreement, expected
reference class counts, and every reported collision. No external packages needed.
The ten diagnostic rows are reported separately from the inherited 159 self-checks.

Validation on 2026-09-10: the pilot completed with its integrity assertions passing;
all six existing check scripts also passed (159 inherited checks). This validates
the runnable checkpoint, not physical truth or the general adequacy of PG.

Next: replace the duplicated scalar patterns with a small set of actual existing
M4 model expressions, including ordered role use and fixed derivative conditions;
retain legitimate transformations as controls. Specify operator signatures and
context conventions equally for the generic and PG encodings, then record actual
manual encoding effort. Obtain independent input/oracle review before freezing any
new unseen evaluation. Keep v0.4 and historical BB1 totals unchanged.
