# Complete Handoff and Next Steps

## 1. One-sentence project

> **Physical Grammar is a typed compositional semantic IR / semantic dependency calculus that represents physical Properties through explicit Entity grounding, preserves their genealogy through composition, and makes scientifically relevant distinction loss explicit and task-checkable.**

## 2. Design principles to remember

1. **Make scientific distinctions explicit.**
2. **Construct distinctions explicitly; erase them explicitly.**
3. **Loss is allowed; dependence on lost distinctions is not.**
4. **Distinction is an organizing principle, not an AST node.**
5. **Scope chooses relevance; it does not manufacture truth.**
6. **Representation != Projection.**
7. **Same formula/dimension/unit/value does not guarantee same Property.**
8. **2π is evidence, not semantics.**
9. **A useful analysis term is not automatically a grammar primitive.**
10. **Failure to predict a conventional name is not automatically grammar failure.**

## 3. Current kernel

`Scope -> Entity -> Property grounding/composition -> Representation/Projection -> Quantify -> VIM-compatible Quantity layer -> naming/rendering downstream`

Core semantic objects remain deliberately small: Scope, Entity, Property, EntityMap, Physical Expression plus semantic relations such as Definition/Law/Constraint/ConstitutiveRelation/Representation/Projection. Do not add a Distinction node or universal Same.

## 4. Current research questions

- Is role-sensitive grounding representable cleanly without proliferating AST objects?
- How should non-Entity arguments/indices such as time, wavelength and mode index appear?
- How should held-fixed/constrained derivative semantics be represented?
- Is Site simply an Entity role/subtype or a distinct sort?
- How should reference and prerequisite structure be represented, if at all, without a background-ontology dump?
- Can a general semantic-dependency judgment subsume grounding, conditions, references and indices while keeping grounding special?
- How should geometric/probabilistic/manifold value spaces be typed?
- How useful is RPD in real benchmark tasks?
- How much naming morphology is productive versus lexical/historical?

## 5. Immediate next gate

**Do not expand the grammar first.** Freeze the current kernel and run a genuinely blind 30–100 item corpus drawn from external standards/textbooks across mechanics, electromagnetism, thermodynamics, continuum mechanics, chemistry, radiation, waves, spectroscopy, quantum/statistical physics.

For each item use `09_SEMANTIC_PARSE_AND_CALIBRATION.md`; mark `[G]/[M]/[D]`; grade G0–G4; identify nearest minimal pair; record naming yield and grammar pressure. Only repeated G4 failures justify grammar revision.

## 6. Fairness rule for blind benchmark

The corpus must be fixed before semantic decomposition. Do not choose terms because they fit known construction families. If a “domain seed” can be invented arbitrarily to rescue every item, the benchmark is invalid; domain seeds must be recognizable domain concepts, not ad-hoc wrappers such as `CharacteristicScale` or `ResponseCoefficient` created solely to avoid G4.

## 7. Post-benchmark revision rule

When a failure appears:

1. check whether it is merely missing `[D]` domain knowledge;
2. check whether established generic mathematics `[M]` suffices;
3. check whether an existing PG construction can express it with better grounding/Scope;
4. classify the recurring missing semantic distinction;
5. only then consider promoting an analysis concept into Grammar.

Prefer the smallest revision that fixes multiple independent failures.

## 8. Source-deletion statement

This package is intended as a **self-contained restart point**. It includes the v0.4 canonical specification, projection/equivalence doctrine, VIM alignment, worked examples, decisions/open questions, blind benchmark protocol, the post-v0.4 meta-terminology, semantic parse/calibration results, RPD/angle/count doctrine, literature/novelty map, and this handoff.

The old source chats and intermediate summaries should no longer be necessary for continuing the project. Keep them only if historical provenance or exact conversational wording matters.
