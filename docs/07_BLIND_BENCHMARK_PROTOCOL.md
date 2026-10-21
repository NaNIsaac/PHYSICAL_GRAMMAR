# Blind Benchmark Protocol — Post-v0.4 Gate

## 1. Purpose

The benchmark tests the frozen grammar rather than extending it.

Primary question:

> **How much physical-property semantics can a frozen Entity-grounded compositional grammar reconstruct, and which distinctions remain valid under its declared projections, before domain-specific physical knowledge is required?**

## 2. Freeze-before-test rule

Before inspecting the hidden benchmark, freeze:

- primitive semantic categories;
- Entity slot/grounding rules;
- EntityMap behavior;
- mathematical constructor set used by the grammar;
- semantic relation categories;
- representation/projection distinction;
- projection-equivalence rule;
- factorization-safety principle;
- terminology/lexicalization policy used by the benchmark implementation.

The benchmark corpus must not be used to retrofit the grammar term-by-term.

Workflow:

`grammar freeze → hidden benchmark → failure taxonomy → minimal revision`.

## 3. Corpus

Target 50–100 hidden terms/expressions across multiple domains, including:

- mechanics;
- electromagnetism;
- thermodynamics;
- continuum mechanics;
- chemistry;
- radiation physics;
- metrology;
- acoustics/waves;
- spectroscopy;
- statistical/quantum physics.

Previously discussed terms such as density, concentration, fraction, flux, stress, energy/torque, and angle-dimension examples are **development cases**, not primary hidden-test items.

## 4. Reducibility grades

### G0 — Grammar-derived

Generic grammar + seed Properties/relations suffice.

### G1 — Generic mathematics required

Requires established non-domain-specific mathematics such as metric, measure, topology, tensor operations, integration, or differentiation.

### G2 — Domain semantic seed required

One domain construction must be supplied, after which generic grammar composes it.

### G3 — Model/law dependent

The relevant relation depends on a physical law, constitutive model, or regime assumption and must not be misclassified as semantic definition.

### G4 — Grammar failure

The frozen grammar cannot naturally express the scientific definition. Repeated G4 failures may justify a new reusable mechanism after the benchmark.

## 5. Per-item record

For every hidden item, record at least:

- Entity signature and semantic roles;
- open/grounded Property structure;
- EntityMap genealogy;
- constructor/expression tree;
- bound/eliminated/context Entity dependencies;
- admissible value/operation structure;
- Quantity/Quantify status;
- available representations;
- physical dimension as a coarse view where applicable;
- projection path(s) used;
- projection guarantees relevant to the item;
- distinctions known to disappear along those paths;
- whether required downstream questions factor through the chosen projection;
- domain-specific semantic seeds required;
- reducibility grade G0–G4;
- lexicalization/naming result, evaluated separately from semantic construction.

## 6. Adversarial families

Include cases designed to defeat shallow dimensional or lexical matching.

### Same dimension, different semantics

Use hidden examples whose physical dimensions agree but grounding, construction, role, or process semantics differ.

### Same arithmetic skeleton, different Entity binding

Hold an algebraic form fixed while varying whether numerator/denominator or source/target refer to the same Entity, a part/whole relation, or unrelated Entities.

### Same conventional word, different semantic construction

Test overloaded terminology only after the semantic parse is hidden from the lexicalizer.

### Same rich semantics, different representation

Test whether the system avoids treating lossless coordinate/encoding changes as new physical Properties.

### Projection trap

Give a deliberately reduced representation and ask a question that may require a discarded distinction. The system should classify the use as licensed, unlicensed, or unknown rather than reconstructing erased semantics by guesswork.

## 7. Minimal-domain-knowledge test

Separate semantic construction from naming knowledge.

One protocol:

1. hide the conventional scientific name;
2. provide only annotated semantic slots/relations;
3. ask for the Physical Grammar construction;
4. evaluate Entity genealogy and typed composition;
5. only then ask a separate lexicalizer to recover or propose the conventional term.

This prevents vocabulary memorization from masquerading as grammar success.

## 8. Projection-validity evaluation

For a projection `π:X→Y` and required question `P:X→Z`, use the semantic standard:

`P = P̄ ∘ π`

when an appropriate `P̄:Y→Z` exists.

The benchmark does not require a checker to prove every case automatically. Implementation outcomes may be:

- `safe` — factorization/sufficiency is established by the available contracts/dependency rules;
- `unsafe` — the required distinction is known to be unavailable;
- `unknown` — the checker cannot establish either result.

Score conservative `unknown` separately from false `safe` claims.

## 9. Evaluation dimensions

### Compression

How many scientific terms/structures are generated by how many primitive seeds, constructors, and lexical rules?

### Derivability

Distribution across G0–G4.

### Semantic discrimination

Can the grammar distinguish adversarial terms that dimensional or algebraic skeletons collapse?

### Entity genealogy

Are referential dependencies preserved, bound, derived, or explicitly eliminated correctly?

### Projection discipline

Are representation changes correctly distinguished from lossy projections? Are induced equivalences qualified by their criterion?

### Safety

Does the system avoid answering questions from representations that no longer guarantee the required distinctions?

### Failure novelty

Does a proposed post-benchmark mechanism resolve a recurring family of failures, or merely one lexical exception?

## 10. Success criterion

The goal is not maximum semantic detail or maximum derivability at any cost.

A successful grammar should achieve reusable compression while obeying:

> **Preserve justified distinctions; do not invent unjustified ones.**

and:

> **Loss is allowed; dependence on lost distinctions is not.**

Only repeated benchmark failures should motivate changes to the frozen grammar.
