# Next steps: from the open items in STATUS.md to runnable work

Draft plan, 2026-10-22. It splits the items STATUS.md and
[the research assessment](ASSESSMENT_2026-09-10.md) list as open into steps that each end in a file
or a number. It changes no result, no grade and not the v0.4 kernel. Nothing here has been run.

Open items it covers (all quoted from STATUS.md and the assessment):

1. Actual M4 model encodings with matched operator/context declarations.
2. Independent encodings and review, in particular of E2/E3.
3. Measured annotation cost.
4. The full typed/context baseline comparison.
5. BB1 retrospective G1/G2 accounting.
6. The contract check trusts the user-supplied preserves/loses declarations (circular evaluation risk).

Rule for every step: freeze inputs and scoring before looking at any result, and keep the cases
already seen marked as development cases.

## Step 1. Make the contract check non-circular (item 6)

- Deliverable: `experiments/pgcheck/derive_loss.py`, which computes preserves/loses for the finite
  fixtures from the model values, not from a declaration.
- Method: for each finite fixture in `matched_models.py`, enumerate the supplied values and test
  whether two inputs that the representation maps to the same record differ in the target response.
- Done when: it reproduces the six decisions of `MATCHED_MODELS_02_RESULTS.json` without reading
  any safe/unsafe field, and a unit test fails if a declaration is added to its input.
- Why first: every later comparison is only meaningful if the checker cannot be handed the answer.

## Step 2. Freeze the comparison protocol (items 1, 4)

- Deliverable: `research/PROTOCOL_MATCHED_COMPARISON.md`.
- Contents, fixed before any new case is encoded:
  - the three methods: unit/dimension check; generic typed expression tree plus an explicit context
    record; PG encoding;
  - the allowed prior contract (what every method may be told) and the forbidden inputs (safe/unsafe
    labels, loss declarations that contain the answer);
  - outputs: safe, unsafe, unknown; the counts false-safe, false-unsafe and unknown reported
    separately, plus coverage, so an all-unknown method cannot win;
  - the annotation log schema for Step 4 (time, lines written, rules added, rules reused).
- Done when: the file is committed and Isaac has read it. Isaac's reading is a decision step, see
  the human-todo below.

## Step 3. Encode actual M4 models (item 1)

- Input: the M4 targets whose models are finite and already have source passages checked in
  `research/m4/BATCH_0*_RESULTS.md`. Candidates, with the reason each fits: M007 (memory response;
  an explicit pair already exists), M005 (invertible spring model), M014 (electromagnetic
  decomposition), M004 (reacting equilibrium; the hardest, last).
- Deliverable: `experiments/pgcheck/matched_models_03.py` and `research/MATCHED_MODELS_03.md`, in the
  format of `MATCHED_MODELS_02`, with all three representations from the protocol.
- Done when: each case has three encodings, the expected decision from an independent case-ledger
  oracle (as in `MATCHED_MODELS_02`), and results are written to a `_RESULTS.json`.
- Limit to keep in the write-up: finite exhaustive mathematics supplies the decisions, so it shows
  what each representation can express, not a PG advantage.

## Step 4. Record annotation cost (item 3)

- Deliverable: `research/ANNOTATION_COST_03.md` with one row per case and method from the log
  schema of Step 2.
- Method: the person encoding writes the log while encoding, in the same session. Rules are counted
  as new the first time they are written and as reused afterwards.
- Done when: every Step 3 case has a row for each method. Report the numbers with the single-analyst
  caveat; do not turn them into a ranking.

## Step 5. Independent review (item 2)

- Deliverable: a review packet `research/review/PACKET_01/` (case text, encodings without the
  expected decisions, a blank answer form) and the returned forms.
- Needs a person other than the author. Choosing and asking the reviewer is Isaac's step.
- Done when: at least one external review is returned for the Step 3 cases and for the E2/E3 grades
  of M010, M012 and M018 (the E2 cases in batches 1 and 5), and disagreements are listed, not
  resolved silently.

## Step 6. Re-run on unseen cases (item 4)

- Precondition: Step 5 returned and the rules frozen (git tag).
- Deliverable: `research/MATCHED_COMPARISON_RESULT.md`: a new set of cases the author has not
  analysed, drawn from sources outside the M4 corpus, scored with the frozen protocol.
- Decision rule from the assessment, written in advance: if PG catches more errors with the same
  information, or does the same checks with fewer annotations and reusable rules, the contribution
  is strengthened. If it matches a generic expression tree only with more records, the claim is
  narrowed to the case collection and the semantic-analysis guidance.

## Step 7. BB1 accounting (item 5)

- Facts: individual BB1 parses and citations are absent, and B018 has a target mismatch
  (`benchmark/analyses/BB1_AUDIT_2026-09-09.md`).
- Deliverable: `benchmark/analyses/BB1_RECONSTRUCTION.md`: for each of the 60 cases, whether an
  individual record can be reconstructed from the surviving material (yes, partial, no), and a G1/G2
  re-count over the reconstructible subset only.
- Done when: the table exists. The reported totals (0/7/49/4/0) stay unchanged and are labelled
  unreproduced for the cases marked no.
- Independent of Steps 1-6; can run in parallel.

## Order

1 -> 2 -> 3 -> 4 in sequence, 5 after 3, 6 after 5, 7 any time. Step 1 and Step 7 need no one
else. Steps 2 and 5 need Isaac.

## What stays out

New primitives (Role, Condition, Observer), more M4 targets, and any revision of the v0.4 kernel,
as in the assessment's "direction to keep". A revision is considered only after Step 6 shows repeated
failures that the generic baseline does not share.
