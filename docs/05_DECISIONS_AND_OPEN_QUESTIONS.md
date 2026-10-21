# Decisions, Freeze Status, and Open Questions — v0.4

## 1. Version charter

v0.4 is an integration version:

`v0.4 = v0.3 Entity/Property kernel + selected v0.2 Projection/Equivalence restoration + minimal formal bridge`.

It is **not** an ontology-expansion version.

## 2. FREEZE for v0.4

| Decision | Frozen statement |
|---|---|
| Scope-relative relevance | Scope determines relevant/tracked distinctions and resolution; Scope changes representation, not physical truth. |
| Entity | Unit of reference distinguished for independent treatment within Scope. |
| Property / Grounding | Property has Entity slots; Entity application to Property slots is grounding. |
| EntityMap / genealogy | EntityMaps construct/select Entities and preserve referential genealogy through composition. |
| Grounding continuity/closure | Entity dependencies must remain traceable, bound, derived, explicitly eliminated, or supplied by Scope. |
| Representation ≠ Projection | Representation change is not automatically information loss; projection explicitly reduces represented distinctions. |
| Projection/refinement DAG | Information-reducing refinement/projection relations are organized as a DAG/partial-order-like structure where appropriate, not a universal ladder. |
| Projection equivalence | `A ~_π B iff π(A)=π(B)`. |
| Factorization safety | `P=P̄∘π` is the semantic criterion that `P` does not depend on distinctions erased by `π`. |
| Exact vs approximate | Exact equivalence-like relations use `~`; tolerance-relative substitutability uses `≈` and is not assumed transitive. |
| Qualified sameness | Do not use one unqualified `same` judgment when the criterion matters. |
| Definition/law/model distinction | Definition, mathematical equality, physical law, constraint, constitutive relation, and representation are distinct semantic relations in the IR. |
| VIM boundary | Preserve VIM Quantity/Quantity Value/measurand terminology and keep `Quantify` distinct from value determination. |

## 3. PROVISIONAL in v0.4

| Topic | Provisional status |
|---|---|
| Projection static checking | Add as a target of static semantics, but no completeness claim. |
| Checker result | `safe / unsafe / unknown` is a promising conservative interface. |
| Projection contracts | Prefer positive `Preserves(π,I)` guarantees plus non-exhaustive known-loss diagnostics. |
| Task-relative exact equivalence | `A ~_T B` via a declared observable set is mathematically clean; whether `Task` belongs in the core grammar is open. |
| Approximate substitutability | `A ≈_{T,ε} B` is useful but its metric/tolerance structure is domain/task-dependent. |
| `use-after-projection` diagnostic | Useful compiler metaphor; not a semantic primitive. |
| Angle/count rich dimensions | Candidate internal views only; compatibility and benchmark value remain to be tested. |
| Projection contract syntax | Semantics are clearer than final DSL surface syntax. |

## 4. DO NOT ADD to v0.4 core

- `Distinction` AST object/type.
- universal `Same` operator.
- exhaustive `Lost(π)` calculus.
- detailed universal Scope tuple/schema.
- universal semantic distance metric.
- large new ontology hierarchy.
- automatic reification of every relation.
- a universal `PropertyValue` umbrella.

## 5. DO NOT PROMISE

- complete automatic factorization checking;
- complete detection of every invalid projection use;
- that every representation relation forms a DAG;
- that every scientific notion of sameness is reducible to projection equivalence;
- that optional rich angle/count dimensions are required by Physical Grammar;
- that Physical Grammar replaces VIM, SI, ontology standards, or established mathematics.

## 6. Terminology migrations retained from v0.3

### Feature → Property

**Status:** strong candidate, not yet irreversible.

Use established `Property` unless blind benchmark failure reveals a recurring concept that is naturally neither Property, Entity, relation, law, operator, state/process Entity, nor representation.

### Feature Kind

**Status:** demoted.

Prefer ordinary open/general Property plus type/classification metadata.

### Quantity ⊂ Feature

**Status:** retired as a core axiom.

Use a VIM-aligned relation:

`Quantify : admissible Property → Quantity`.

### Generic Feature/Property Value

**Status:** not frozen.

Do not conflate semantic object, quantity, quantity value, coordinate representation, categorical result, and measurement result.

## 7. Open formal questions

1. **Property ontology:** Is `Quantify` a genuine map, a view/interface, or identity on a quantity-bearing subclass?
2. **Relation versus Property:** Which structural relations should remain predicates rather than Properties?
3. **Non-Entity arguments:** How should time coordinates, integer mode indices, outcomes, and parameters appear syntactically alongside Entity slots?
4. **Site status:** Entity subtype/role or distinct sort?
5. **Representation taxonomy:** Exact typing of lossless coordinate representation, encoding, observation, and lossy projection.
6. **Projection contracts:** Which guarantees are generic enough for the core checker?
7. **Task semantics:** Is Task/observable-set notation part of the language or external analysis metadata?
8. **Constrained derivative:** Is held-fixed semantics generic enough for a core constructor?
9. **Reification:** Formal constructor or Scope/modeling operation?
10. **Quantity structure:** Interaction with ordinal quantities and other VIM cases.
11. **Geometric/probabilistic value spaces:** Type affine spaces, SO(3), tensors, distributions, etc. without forcing scalar quantity language.
12. **Angle/count views:** Are richer internal generators empirically useful enough to retain?

## 8. Static semantics target

### Established checks

1. Type/value-structure consistency.
2. Physical dimension consistency.
3. Entity-dependency consistency.

### Added provisional check

4. Projection validity: does the downstream operation require a distinction not guaranteed by the current representation?

Important boundary:

`Projection Validity Principle ≠ Complete Projection Validity Algorithm`.

## 9. Benchmark rule

After v0.4 documentation integration, freeze the grammar before inspecting a hidden benchmark.

Workflow:

`freeze grammar → blind corpus/domain benchmark → failure taxonomy → minimal revision`.

A new constructor/role should be added because repeated benchmark failures require it, not because it is aesthetically attractive.

## 10. Evaluation dimensions

Retain v0.2/v0.3 metrics and add explicit projection validity:

- compression: named terms generated per seed/constructor complexity;
- derivability: generic grammar vs generic math vs domain seed vs model/law vs failure;
- semantic discrimination: adversarial same-dimension/same-form cases;
- Entity genealogy preservation;
- recoverability/projection cost;
- representation/projection classification;
- whether downstream questions are licensed on the chosen reduced representation;
- failure novelty: whether a new mechanism resolves a family of failures or one lexical exception.

## 11. Claims to avoid

- “Physics lacks Entity semantics.”
- “VIM forgot the object of a quantity.”
- “Physical Grammar discovers the true ontology of properties.”
- “Dimension determines physical meaning.”
- “Every relation is a Property.”
- “Every Property is a Quantity.”
- “Same is literally always a projection.”
- “All approximate sameness relations are equivalence relations.”
- “Every projection-validity question is statically decidable.”

## 12. Recommended dual statement

### What the project implements

> **Physical Grammar is a typed compositional semantic IR that represents physical Properties through explicit Entity grounding and preserves their semantic dependencies through composition.**

### Why it is designed this way

> **Physical Grammar makes scientific distinctions explicit—how they are introduced, preserved, composed, represented, and selectively discarded.**
