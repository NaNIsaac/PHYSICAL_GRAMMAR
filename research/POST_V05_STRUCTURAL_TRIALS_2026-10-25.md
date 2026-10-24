# Post-v0.5 Structural Trials — Working Summary, 2026-10-25

**Evidence status:** this file records project-discussion results that are **not yet reconstructed as repository-native case files**. Treat all counts and classifications below as working summaries to be reproduced before publication or kernel revision.

## 1. Structural invariance trial

Reported scope: 18 examples.

Working observations:

- R0 lexical renaming: 18/18 reported cases retained analyzability;
- R1 domain erasure with signatures retained: 18/18 retained analyzability;
- R2 weakening rich types to a generic Feature-like type: 5/18 retained the relevant operation judgment;
- division, differentiation, integration, geometry and measure-sensitive operations typically required richer typing.

The conversations also used a four-level semantic-dependence classification. Because `G0–G3` would collide with the repository's established G0–G4 reducibility grades, this repository records it as:

- `SD0` structural;
- `SD1` physically typed;
- `SD2` semantically grounded;
- `SD3` realization dependent.

Interpretation:

- Referential structure and Physical Type are meaningfully separable.
- A pure structural grammar cannot by itself license all physical/mathematical operations.
- Construction appears partly grammar-like and partly typed-mathematical, suggesting an interface rather than a single universal semantic engine.

## 2. Interface audit

Reported scope: 20 cases plus 6 adversarial pairs.

Working module-use pattern:

- R — Referential: 18/20
- T — Physical Type: 20/20
- C — Construction: 13/20
- A — Abstraction/Scope: 6/20
- S — grounded semantic interpretation: 20/20
- G — Geometry: 9/20
- M — Realization/Measurement: 1/20
- X — Nomenclature/Expression: 3/20

These counts were reported in conversation and are not yet repository-native evidence.

Important adversarial pairs included:

- pressure vs energy density;
- frequency vs radionuclide activity;
- absorbed dose vs kerma.

These pairs support the claim that lower-level structural/type similarity does not establish semantic identity.

## 3. Semantic-domain audit

The label “grounded physical semantics” was found to carry several different responsibilities:

- concept seed;
- referent kind;
- participant/context role;
- reference/baseline;
- restriction;
- resolved-variable identity;
- construction class;
- process/transfer semantics;
- assertion/law status;
- model/regime context;
- convention;
- semantic equivalence policy.

Current response: do **not** promote all of these to primitives.

Instead, test whether some are supplied by independent calculi/services and whether semantic identity is a convergence/certificate layer.

## 4. Restriction/Condition trial

Reported scope: 16 cases plus 4 adversarial controls.

Working result:

A single universal `Condition` node was too coarse.

Held-fixed constraints grouped naturally:

- `HOLD(T)`
- `HOLD(S)`
- `HOLD(V)`
- `HOLD(p)`

but other superficially similar notions were structurally different:

- `BIND(T=T0)`
- `FREE(λ)`
- `REFERENCE(standard_state)`
- boundary conditions;
- gauge conditions;
- equilibrium/model regime assumptions;
- cutoffs.

Current candidate: a thin **Restriction Context** service, with other semantics delegated to the relevant provider.

## 5. Process/Dynamics trial

Reported scope: 20 cases plus 5 adversarial controls.

Reusable process skeletons observed:

- `PROCESS`
- `PARTICIPATE`
- `CHANGE`
- `TRANSFER`
- `RATE`
- `BALANCE`
- `SEQUENCE`

Key minimal pairs:

- frequency vs activity — shared rate structure, different process seed;
- absorbed dose vs kerma — shared energy-per-mass skeleton, different transfer genealogy;
- stopping power vs LET — related energy/length skeleton, but one emphasizes projectile change and the other transfer/deposition semantics.

Current inference: Process Structure has stronger evidence for an independent subformalism than a universal Condition calculus.

## 6. Assertion/law-status next target

The next unresolved distinction is statement-level status.

Candidate classes include:

- definition;
- mathematical identity/equality;
- constraint;
- constitutive relation;
- evolution law;
- conservation law;
- model relation;
- empirical fit.

The same mathematical surface relation can play different roles. Therefore law/assertion status should not be inferred from algebraic shape alone.

## 7. Reproduction requirement

Before any of these working summaries justify a kernel change, reconstruct them as repository-native artifacts:

1. freeze the case list;
2. record the semantic parse and minimal pair;
3. specify what R/T/C/A/G/D/K/etc. information is supplied;
4. run an explicit generic baseline where possible;
5. record whether a claimed distinction changes a real decision;
6. obtain independent review for ambiguous classifications.

This follows the existing repository principle that an interesting analysis is not automatically a grammar revision.
