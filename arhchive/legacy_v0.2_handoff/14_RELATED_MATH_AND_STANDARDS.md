# 14. Related Mathematics and Standards to Reuse

This project should **borrow mature mathematics** rather than recreating it.

## 1. Dependent types / Categories with Families / contextual categories

Useful for:

- Scope/context;
- Entity-dependent Feature types;
- substitution/instantiation;
- context refinement.

## 2. Generalized Algebraic Theories (GATs)

Strong foundation candidate for dependent sorts, typed constructors, equations, and contextual syntax.

## 3. Essentially algebraic theories / partial operations

Useful when a constructor exists only under compatibility conditions, e.g. difference, flux through compatible surfaces, geometric pairings.

## 4. Refinement types / typed feature structures

Useful for cross-slot constraints:

- same/different Entity;
- part/whole;
- same Stage;
- orientation/geometric compatibility;
- held-fixed conditions.

## 5. Multicategories / coloured operads

Useful for constructor trees and typed multi-input composition. Probably a constructor layer rather than the entire Entity/context foundation.

## 6. Attribute grammars

Useful implementation analogy for synthesized/inherited attributes such as dimension, referents, tensor order, Stage, context, validity.

## 7. Mereology / mereotopology

Use for part/whole, overlap, Region, boundary, surface, contact. Avoid inventing a spatial-part theory from scratch.

## 8. Differential geometry / geometric measure theory

Use for:

- manifolds/metrics;
- gradients/divergence/curl in generalized settings;
- parallel transport/comparison;
- surfaces/areas/volumes;
- continuum kinematics.

## 9. Tensor calculus / multilinear algebra

Use for tensor products, contraction, duals, response maps, symmetry.

## 10. Quantity calculus / units-of-measure type systems

Use established mathematics for:

- physical dimensions;
- unit conversion;
- exponent-vector/free-Abelian-group-like structure;
- dimension checking.

Physical Grammar adds semantic structure **above** this layer.

## 11. Category-theoretic projection / forgetful maps

QSF projection ideas are naturally analogous to structure-forgetting maps/functors and quotient/equivalence constructions. Do not claim every projection is literally a functor until formal objects/morphisms are fixed.

## 12. Institution theory

Potential later tool for translating among formal scientific vocabularies/logics while preserving satisfaction/semantics. Not needed in the immediate core.

## 13. Scientific semantic standards to map to

### QUDT

Reuse/align with distinctions such as Quantity Kind, Quantity, Quantity Value, Unit, Dimension Vector.

### I-ADOPT

Strong precedent for semantic roles including object of interest/system/part/matrix/context, numerator/denominator, source/target, constraints/modifiers.

### CSDMS Scientific Variables / Standard Names / SVO-like compositional systems

Relevant for compositional variable naming, operator chaining, participant/role/context/process vocabulary.

### IUPAC / NPU terminology

Useful for systematic quantity nomenclature and modifiers such as specific/massic, volumic, areic, lineic, molar, component/whole conventions.

### OPB

Useful precedent for distinguishing physical entities/properties from physical dependencies/laws.

## 14. Validation languages / semantic web

OWL/RDF can express vocabulary/relations; SHACL-like constraint systems may be more appropriate for well-formedness and cross-slot validation.

## 15. Rule of use

> Existing formalism is a compatibility target and source of machinery, not an unquestionable ontology of reality.

Do not rebuild mature mathematics merely to keep the project self-contained.
