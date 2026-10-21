# M4-01 — frozen adversarial selection

Frozen: 2026-09-09, before detailed PG parsing or G/E scoring in this run.
Kernel: v0.4. Selection: 20 cases, two per attack family.
This is intentionally adversarial and informed by BB1; it is **not a blind corpus**.
Freeze applies to IDs, targets and comparison questions. Source acquisition and
physical assumptions must be completed in case records before scoring. If a target
is ill-posed, retain it and record that outcome; do not silently substitute a case.

The prompts below are test designs, not established PG encodings or asserted
physical equivalences. At selection freeze all G/E grades were unassigned.
Subsequent provisional assessments are tracked below; the frozen targets remain unchanged.

| ID | Family | Frozen target and comparison question |
|---|---|---|
| M001 | A1 role | Cross response of two coupled subsystems: retain response-at-A / drive-at-B when comparing the reversed experiment. Declare reciprocity assumptions separately. |
| M002 | A1 role | Coefficient of restitution: distinguish ordered bodies and pre/post-collision relative normal velocity even under relabeling. |
| M003 | A2 condition | Compressibility under fixed temperature versus fixed entropy; preserve the complete constrained derivative specification. |
| M004 | A2 condition | Chemical response along a reaction-equilibrium constraint versus independently fixed species amounts; distinguish derivative paths at the same state. |
| M005 | A3 nonlocal | Spatially nonlocal linear response kernel: keep observation point and source point independently resolved before and after source integration. |
| M006 | A3 nonlocal | Two-point correlation versus coincident-point variance; determine which separation-dependent questions survive the coincident-point restriction. |
| M007 | A4 history | Linear response with a memory kernel: compare histories having the same current input but potentially different current response. |
| M008 | A4 history | Magnetic hysteresis: compare preparations with the same current applied field; specify the history information required for magnetization. |
| M009 | A5 gauge | Electromagnetic potentials connected by an admissible gauge transformation; distinguish gauge equivalence from equality of components. |
| M010 | A5 gauge | Aharonov–Bohm loop phase: compare locally field-free accessible regions with different enclosed flux, retaining topology and boundary assumptions. |
| M011 | A6 topology | Winding of a nonvanishing complex order parameter around a closed contour; compare winding sectors and deformations that cross a zero. |
| M012 | A6 topology | Berry phase on a closed parameter loop: distinguish local gauge choice, loop dependence and phase modulo a full turn. |
| M013 | A7 observer | Energy assigned to the same relativistic four-momentum by two observers; retain the observer and metric convention. |
| M014 | A7 observer | Electric/magnetic field decomposition for two inertial observers; distinguish observer components from the underlying field tensor. |
| M015 | A8 effective | Coarse-grained fluid density at two smoothing scales; specify which microscopic distinctions and scale-dependent queries remain. |
| M016 | A8 effective | Band effective mass near a specified crystal momentum; distinguish the effective tensor and approximation regime from bare particle mass. |
| M017 | A9 operational | Instrument indication versus the targeted measurand in a calibration model; retain which object each quantity characterizes. |
| M018 | A9 operational | Procedure-specified hardness under two indentation procedures; ask whether a conversion requires empirical/model information. |
| M019 | A10 Scope | Labeled identical particles versus permutation-invariant description; determine which label-specific queries cease to be admissible. |
| M020 | A10 Scope | Microscopic trajectories versus a one-particle distribution; ask whether a two-particle correlation can be recovered without a closure assumption. |

## Source acquisition queue

Use external definitions before PG construction. Each final record must cite a
specific section/page, state the minimal physical setup, and supply a comparison
pair or explicit insufficiency question. Source leads are not substitutes for this.

- M001, M005–M007, M015, M020: David Tong,
  [Kinetic Theory](https://www.damtp.cam.ac.uk/user/tong/kintheory/), including
  linear response and the BBGKY/Boltzmann material. Chapter/page matching pending.
- M009–M010: Tong,
  [Gauge Theory](https://www.damtp.cam.ac.uk/user/tong/gaugetheory/gt.pdf),
  electromagnetic gauge structure and loop observables. Exact setup matching pending.
- M017: [VIM 2.3, measurand](https://jcgm.bipm.org/vim/en/2.3.html).
- Other cases: authoritative textbook/standard definition still to acquire.

## Scoring discipline

Use the 13-field semantic parse sheet and [G]/[M]/[D] accounts. For every claim
that existing PG suffices, explain the Entity identity criterion, slots, binding
and relation structure. Naming an opaque `History` or `EffectiveSystem` is not
by itself an encoding. Record what it must contain and what operations are needed.

Record G0–G4 and E0–E4 independently under the existing campaign rubric. Treat
unresolved G4/E3/E4 boundaries explicitly; do not call missing implementation support
a grammar failure. Report `safe/unsafe/unknown` for a specific downstream question,
with the supporting contract or a counterexample. Never infer safe from the absence
of a known-loss annotation.

First analysis batch: M007, M010, M015, M020. Remaining work stays visible until
external definitions, parses and scores exist; this manifest is selection completion only.

## Analysis progress — 2026-09-10

[Batch 1](BATCH_01_RESULTS.md): M007/M010/M015/M020.
[Batch 2](BATCH_02_RESULTS.md): M008/M009/M016/M019.
[Batch 3](BATCH_03_RESULTS.md): M003/M004/M005/M006.
[Batch 4](BATCH_04_RESULTS.md): M001/M002/M013/M014.
[Batch 5](BATCH_05_RESULTS.md): M011/M012/M017/M018.
Twenty of twenty have source-supported first-pass analyses. M018 quantitative
conversion remains unknown; its grade covers procedure semantics only.
These are single-analyst results, not final passes or independent review.
