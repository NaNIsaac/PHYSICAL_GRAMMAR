# Project Conversation Synthesis — 2026-10-25

**Status:** conversation-derived research synthesis.  
**Scope:** consolidates the three Physical Grammar / 물리량 명명학 project conversations that continued beyond the repository's original v0.5 package.  
**Evidence warning:** this document preserves decisions, examples, hypotheses, and reported trial outcomes from the project conversations. It is **not** a substitute for repository-native benchmark records or independent validation.

## 1. Why this document exists

The repository had become temporally split:

- the historical v0.4 kernel and v0.5 research package were well preserved;
- later project conversations substantially changed the research architecture;
- nomenclature/identity work, structural-erasure tests, and several interface audits existed mainly in conversation state;
- some later terminology would collide with established repository terminology if copied verbatim.

This file records the later state **without rewriting the historical specification**.

The governing compatibility rule remains:

> old frozen decisions stay historical facts; later work is added with explicit Working/Candidate status.

## 2. Current problem statement

A recurring project observation is that physical formulas leave much of their semantic context implicit.

Readers often have to infer from definitions, disciplinary convention, notation, and surrounding prose:

- what entity a quantity is about;
- whether a denominator is a spatial measure, total system quantity, reference quantity, or something else;
- whether the numerator refers to the whole system or a component;
- what process, reference, condition, resolution variable, or geometry is involved;
- which distinctions have already been averaged, bound, projected, or otherwise removed.

This is not the claim that humans cannot understand physics notation. The point is that **the notation itself is often underdetermined without external context**, so interpretation depends on reconstruction from convention and context.

Physical Grammar investigates whether those semantic relations can be made explicit enough that the resulting structures can support:

- comparison;
- search;
- consistency checking;
- relation discovery;
- controlled abstraction;
- terminology assistance;
- scientific-AI context handling.

The project therefore aims beyond dimensional analysis without treating dimensional analysis as obsolete.

## 3. Practical motivating family: density, concentration, fraction, normalization

Several conversations converged on the same useful public example.

Surface expressions such as

`ρ = m / V`

`n = N / V`

`c_i = n_i / V`

`w_i = m_i / m_total`

share an arithmetic quotient skeleton, but not necessarily the same physical semantics.

A more explicit semantic form can distinguish:

`MassDensity[A] := Mass[A] / Volume[OccupiedRegion[A]]`

`NumberDensity[X in A] := Count[X in A] / Volume[OccupiedRegion[A]]`

`AmountConcentration[X in S] := Amount[X in S] / Volume[S]`

`MassFraction[X in M] := Mass[X in M] / Mass[M]`

Important distinctions include:

- whole-system bearer versus component;
- spatial normalization versus part/whole normalization;
- denominator genealogy;
- role of the numerator;
- whether integration over a measure recovers an extensive content.

### Communication example: salt solution

A deliberately intuitive example used in discussion was a salt solution:

- total solution: approximately `105 g / 100 mL = 1.05 g/mL`;
- salt content per solution volume: `5 g / 100 mL = 0.05 g/mL`.

The same mass/volume dimension can therefore support very different physical readings depending on **what mass is being referred to**. The useful pedagogical move is to let the calculation reveal the semantic distinction instead of beginning with an abstract ontology lecture.

This example is a communication device, not a benchmark case.

## 4. Dimension is informative but not identity

Repeated minimal pairs were used to make this point:

- energy vs torque;
- pressure vs energy density;
- frequency vs radionuclide activity;
- absorbed dose vs kerma;
- angle vs fraction vs refractive index in coarse dimensionless treatment.

The project position is:

> same unit or dimension is evidence of mathematical compatibility, not proof of semantic identity.

Dimension can be viewed as a coarse projection of richer semantic structure, but public explanations should not make projection theory the whole identity of the project.

## 5. Referential grammar and partial grounding

The grounding syntax remains one of the most characteristic ideas.

Examples:

`Mass[A]`

`Distance[A,B]`

`Force[A,B]`

A multi-referent property can be partially grounded:

`Distance[A, □]`

This represents an open physical relation with one referent bound, not a missing measured value.

A useful conceptual analogy is partial application, but the physical interpretation is **referential binding**.

Entity-producing maps remain equally important:

`OccupiedRegion[A] → Region`

which permits constructions such as:

`Volume[OccupiedRegion[A]]`.

This preserves a genealogy that ordinary algebraic notation often omits.

## 6. Construction families explored in conversation

Several candidate recurring constructions were used as analysis patterns:

- `Velocity := Rate(Position)`
- `Speed := Magnitude(Velocity)`
- `Acceleration := Rate(Velocity)`
- `Torque := MomentAbout(Force)`
- density-like constructions as normalization by a measure;
- part/whole ratios;
- response derivatives;
- aggregation/integration;
- reference differences;
- resolution-indexed quantities.

These are **analysis families**, not automatically grammar primitives.

Two important anti-reduction examples were emphasized:

- stress should not be treated as nothing more than `Force / Area`; traction mapping, orientation, tensor structure, and momentum-transfer semantics matter;
- flux should not be treated as nothing more than `Flow / Area`; oriented surfaces, local density, crossing semantics, and integration structure matter.

## 7. Physical Feature as the current semantic umbrella

The conversations explicitly reopened the earlier Feature idea because the project should include non-scalar and non-numerical physical features.

Current conversation-level convention:

- **Physical Feature** is the broad semantic umbrella;
- **Quantity** is an important quantitative inhabitant, not necessarily the root category;
- feature values may be real, integer, complex, vector, tensor, cyclic, ordered, categorical, nominal, distributional, or set-valued.

Examples that motivated the broader scope:

- mass;
- electric field;
- phase;
- impedance;
- crystal phase;
- color.

This does **not** retroactively alter the v0.4 kernel's historical `Property` decision. Repository status should therefore be read as:

- v0.4 kernel: historical canonical `Property` vocabulary;
- current research layer: `Physical Feature` accepted as a useful semantic umbrella, still not promoted into the old kernel.

## 8. SFLP-inspired design lesson: erase before adding

A major later influence came from a substance-free-phonology-style design question.

The project did **not** adopt the source theory. It borrowed a methodological challenge:

> before adding domain meaning, remove the physical names and ask what formal structure survives.

Example:

`MassDensity[A] := Mass[A] / Volume[OccupiedRegion[A]]`

becomes

`P3[A] := P1[A] / P2[R[A]]`.

Even after lexical erasure, some structure remains:

- application;
- referential binding;
- composition;
- dependency;
- typed combination.

The intended stance is **substance-minimal grammar with explicitly grounded physics**, not substance-free physics.

Physics-specific information such as dimensions, transformation laws, conservation laws, process identity, measurement accessibility, and model/law status may remain genuinely semantic.

## 9. Three diagnostic tests

### 9.1 Renaming Test

Ask what survives progressively stronger semantic erasure.

- **R0 lexical renaming:** remove conventional names.
- **R1 domain erasure, signatures retained:** preserve typing/signatures while removing domain labels.
- **R2 type weakening:** collapse rich physical types toward generic Feature-like types.
- **R3 grounding restoration:** reattach physical identity/roles/restrictions and observe what judgments return.

Reported structural-invariance trial:

- R0 retained analyzability in 18/18 reported cases;
- R1 retained analyzability in 18/18;
- R2 retained the relevant judgment in only 5/18.

These figures are conversation-derived and require repository-native reconstruction.

### 9.2 Realization Test

Separate the target semantic feature from the way it is measured, inferred, or simulated.

Example target:

`Temperature[A]`

possible realizations:

- thermocouple → voltage → calibration;
- resistance thermometer → resistance → calibration;
- optical method → spectrum → inference.

If several realization chains target the same semantic feature, measurement procedure should not define the feature identity by itself.

### 9.3 Minimal-Operations Test

Try to express recurring structures with a small operation basis before inventing a new primitive.

Candidate basis:

- `APPLY`
- `BIND`
- `COMPOSE`
- `COMBINE`
- `AGGREGATE`
- `PROJECT`
- `ASSERT`

Possible reductions under test:

- partial grounding ≈ `APPLY + BIND`;
- normalization ≈ typed `COMBINE(/)` plus semantic classification;
- integration/sum ≈ `AGGREGATE + BIND`.

## 10. Semantic-dependence strata: renamed to avoid G0–G4 collision

The conversations temporarily used a second `G0–G3` classification:

- structural;
- physically typed;
- semantically grounded;
- realization dependent.

The repository already uses `G0–G4` for a different reducibility grading system. Reusing the same labels would be unsafe.

Therefore this synthesis renames the later strata:

- **SD0 — structural**
- **SD1 — physically typed**
- **SD2 — semantically grounded**
- **SD3 — realization dependent**

This is a terminology repair only; it does not change the underlying idea.

## 11. Why a federation rather than one universal grammar

Later comparisons with other formal traditions reinforced the idea that PG may need several cooperating calculi rather than one universal AST.

### Institution-style abstraction

Lesson: do not force all scientific domains into one logic. Define stable interfaces between signature, expression, model/interpretation, and invariance under notation change.

### Typed lambda calculus / type theory

Lesson: application, binding, composition, and well-formedness can be formalized independently of full domain semantics. This supports a distinct physical-type layer.

### Operads / PROPs / compositional systems

Lesson: typed inputs/outputs and composition can be studied abstractly while concrete physical interpretation is supplied separately. This supports a Construction layer.

### Process algebra

Lesson: behavioral/process structure can form a specialized calculus rather than being embedded into every static object. This motivated the Process Structure candidate.

### Abstract interpretation

Lesson: abstraction, information loss, soundness, and downstream sufficiency are separable questions. This closely matches Scope/Projection/Safe Projection.

The conclusion was not that PG is secretly any one of these formalisms. The useful lesson is architectural:

> use a federation of narrow formalisms with explicit interfaces.

## 12. Current candidate federation

The current research map is:

- **R — Referential / Grounding**
- **T — Physical Type**
- **C — Construction**
- **A — Abstraction / Scope**
- **G — Geometry / Localization**
- **D — Process Structure**
- **K — Restriction Context**
- **S-ID — Semantic Identity convergence/certificate**
- **Q? — Assertion / Law status**
- **M — Realization / Measurement**
- **X — Expression / Nomenclature**

This is a graph of cooperating responsibilities, not a strict pipeline.

## 13. Reported interface audit

Reported scope: 20 cases plus 6 adversarial pairs.

Conversation-level module-use counts:

- R: 18/20
- T: 20/20
- C: 13/20
- A: 6/20
- grounded semantic interpretation S: 20/20
- G: 9/20
- M: 1/20
- X: 3/20

Interpretation at the time:

- Physical typing appeared universal in the sample;
- Construction was common but not universal;
- Geometry appeared too generative to be mere metadata;
- final concept identity still required grounded semantics;
- the architecture looked like a network/federation rather than `R → T → C → A`.

These counts remain unreproduced conversation evidence.

## 14. Semantic-domain decomposition

The later semantic audit found that “grounded semantics” was itself heterogeneous.

Responsibilities observed:

- concept identity seed;
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

The response was **not** to add twelve primitives.

Instead:

- process semantics may be delegated to D;
- restrictions to K;
- assertion/law semantics to Q?;
- realization to M;
- terminology/provenance to X;
- identity can be treated as a convergence/certificate problem in S-ID.

## 15. Restriction Context trial

Reported scope: 16 cases plus 4 adversarial controls.

A universal `Condition` primitive looked too broad.

A coherent held-fixed family did emerge:

- `HOLD(T)`
- `HOLD(S)`
- `HOLD(V)`
- `HOLD(p)`

but these differ from:

- `BIND(T=T0)`
- `FREE(λ)`
- `REFERENCE(standard_state)`
- boundary conditions;
- gauge conditions;
- equilibrium/model regimes;
- cutoffs.

Current candidate: **thin cross-cutting Restriction Context**, not a giant Condition ontology.

## 16. Process Structure trial

Reported scope: 20 cases plus 5 adversarial controls.

Reusable skeletons:

- `PROCESS`
- `PARTICIPATE`
- `CHANGE`
- `TRANSFER`
- `RATE`
- `BALANCE`
- `SEQUENCE`

Important minimal pairs:

### Frequency vs radionuclide activity

Both can look like reciprocal-time rates, but:

- frequency → rate of oscillatory/cycle process;
- activity → rate of radioactive-decay events.

### Absorbed dose vs kerma

Both can share energy-per-mass structure and Gy units, yet differ in transfer genealogy.

### Stopping power vs LET

Both can share energy-per-length structure, but one centers change in projectile energy while the other centers transferred/deposited energy in material.

Conclusion: process semantics showed stronger evidence for an independent subformalism than generic Condition did.

## 17. Assertion / law status is a separate unresolved layer

The same equation-shaped surface can denote very different kinds of scientific statements.

Candidate distinctions:

- definition;
- mathematical identity/equality;
- constraint;
- constitutive relation;
- evolution law;
- conservation law;
- model relation;
- empirical fit.

A process-bearing concept is not itself a law:

- radionuclide activity ≠ decay law;
- heat flux ≠ Fourier constitutive law.

A dedicated assertion/law-status audit remains a high-priority next step.

## 18. Projection/equivalence remains important but should not dominate the public story

The historical principle remains:

`A ~_π B iff π(A)=π(B)`

and safe projection for downstream `P` requires factorization:

`P = P̄ ∘ π`.

Interpretation:

> distinctions may be discarded, but a downstream judgment must not depend on distinctions that were discarded.

This remains a strong formal principle.

However, later communication work concluded that public explanations should lead with **concrete semantic ambiguity and practical structure**, not with projection theory. Projection is one powerful module of the project, not its entire public identity.

## 19. Nomenclature program recovered from the conversations

The original naming motivation remains active downstream.

Working model:

`physical meaning → semantic parse → naming projection → surface name`

A name is a lossy lexical projection of a richer semantic structure.

### Semantic descriptor vs conventional label

Examples:

- `vacuum-referenced electron removal energy` → work function;
- `wavelength-resolved radiance` → spectral radiance, `L_λ`;
- `frequency-resolved radiance` → spectral radiance, `L_ν`.

The conventional label can be shorter, opaque, or ambiguous while the descriptor stays compositional.

### Naming atoms explored

Analysis vocabulary included:

- head/content;
- role;
- reference;
- condition/restriction;
- resolution;
- aggregation;
- representation;
- domain qualifier.

These are naming-analysis atoms, not automatically semantic-kernel primitives.

### Early naming stress result

A conversation-level naming stress set reported:

- 16 development cases;
- one direct/simple case;
- seven compositional cases;
- eight fallback cases;
- no forced failure category;
- a renderer produced 16/19 targets and abstained on three difficult cases rather than inventing names.

These numbers should be treated as historical conversation notes until reconstructed from source artifacts.

The later conclusion was that a **semantic linter** may be more practically valuable than an automatic pretty-name generator.

## 20. Identity registry and lifecycle

The downstream registry design distinguishes:

`semantic identity ≠ label ≠ symbol ≠ descriptor ≠ historical identifier`.

Working ID families:

- **PQP** — pre-registration proposal;
- **PGQ** — registered quantity identity;
- **PGE** — lifecycle/terminology event;
- **PGS** — source snapshot;
- **PGC** — scoped claim;
- **PGR** — typed relation assertion.

Adjudication outcomes:

- `MERGE_AS_ALIAS`
- `REGISTER_DISTINCT`
- `HOLD_AMBIGUOUS`
- `REJECT_UNDERSPECIFIED`

Important invariants:

- invertibly related concepts are not automatically the same identity;
- same unit/dimension is not identity;
- synonyms/translations can share one identity;
- semantic-boundary changes must not be silent;
- legacy 1→many splits must require disambiguation;
- deprecated terminology should remain resolvable with provenance.

External authorities support **scoped claims**; they do not define global semantic identity merely by naming something.

## 21. Public-facing project definition

Later writing work converged on a less defensive description.

Preferred positive framing:

> Physical Grammar studies how the meaning of physical features and quantities can be represented as explicit structure.

The public problem is not “physics notation is bad” or “humans cannot understand equations.”

It is:

> important semantic relations are often distributed across formula, prose, convention, diagrams, definitions, and disciplinary habits; making some of those relations explicit may allow physical concepts to be searched, compared, checked, and related structurally.

Useful public sequence:

`problem → concrete example → structural representation → larger practical benefit`.

Avoid beginning with long disclaimers about not replacing SI/VIM or with a full projection formalism.

## 22. Project naming status

**Physical Grammar is still a working/codename**, not a final project name.

Name families discussed included:

- Grammar;
- Semantics;
- Structure;
- Calculus;
- Framework.

The naming decision was intentionally deferred until the architecture clarifies whether the project's center is best described as:

- a grammar;
- a typed semantic calculus;
- a compositional framework;
- a federation/interface architecture;
- or a combination of these.

Do not let the current codename force the theory into “one grammar” merely to fit the name.

## 23. Communication/writing lessons relevant to the repository

Project communication should emphasize the actual semantic problem before the machinery.

A useful contrast is:

- humans do **not** receive complete semantics directly from the formula;
- they infer missing relations from convention, definitions, diagrams, and local context;
- those inferences are usually easy in familiar settings, but can become ambiguous across fields or detached contexts;
- machine processing exposes the missing structure even more clearly.

For examples, prefer immediate situations over abstract slogan-like exposition.

The project also benefits from asymmetric prose structure:

- short setup;
- heavy body with examples and consequences;
- modest conclusion.

This is a communication convention, not a formal part of the grammar.

## 24. Current research questions carried forward

High-priority questions after merging the conversations:

1. Can the R/T/C/A/G/D/K/M/X interfaces be made explicit and minimal?
2. Should Physical Feature enter a future kernel or remain an analysis umbrella?
3. Which semantic operations survive renaming and domain erasure?
4. Which operations require physical typing rather than generic structure?
5. Can Process Structure generalize across enough domains to justify a dedicated calculus?
6. Can Restriction Context remain thin?
7. How should Assertion/Law status be represented?
8. Can semantic identity be computed/validated as a certificate assembled from multiple providers?
9. Which structure-based search/lint tasks beat generic typed expression trees or ontology/lexical baselines?
10. Which conversation-derived trials should be reconstructed first as repository-native benchmarks?
11. How should the identity registry extend beyond quantities if non-quantity Physical Features become first-class registry objects?
12. What final project name best reflects the mature architecture?

## 25. Merge discipline

This synthesis must not be used to retroactively claim:

- the v0.4 kernel already contained the federation architecture;
- BB1/M4 tested the later R/T/C/A/G/D/K architecture;
- conversation-reported audit counts are independently reproduced;
- Physical Feature was already canonical in the frozen v0.4 kernel;
- the nomenclature registry is production-ready;
- the current architecture has proven superiority over matched generic baselines.

The next trustworthy step is still:

`conversation result → frozen case record → explicit baseline → reproducible check → independent review → theory decision`.
