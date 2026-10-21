# Research Positioning and Literature Map

**Purpose:** preserve the intellectual map needed to restart the project without the source chats. Verify bibliographic details against primary sources before publication.

## 1. Project evolution

Original motivation came from linguistic grammar and physical-quantity naming: treat physical quantity expressions like sentences whose semantic roles, arguments, modifiers and omitted context can be parsed. The early Quantity Semantics Framework (QSF) focused on quantity vocabulary and naming. Physical Grammar (PG) emerged as the deeper layer required to represent grounding and composition before naming.

Current layered view:

`PG core -> physics semantic patterns -> physical quantity semantics (QSF-like layer) -> naming/rendering`

Central naming principle: **Name is a result of structure**, but conventional lexicons may be opaque or historical, so name generation is not guaranteed.

## 2. Linguistic precedents

Useful analogies/design precedents, not claims that PG is a linguistic theory:

- noun/noun phrase ↔ Entity
- predicate/adjectival component ↔ Property
- argument ↔ Entity slot
- semantic/thematic role ↔ Source, Target, Bearer, Reference
- modifier ↔ spectral, directional, local, held-fixed/reference-conditioned qualifiers
- relation/preposition ↔ between, per, relative to
- phrase/clause ↔ Physical Expression
- omitted argument/context ↔ Scope-supplied information
- lexicon/morphology ↔ quantity vocabulary and naming patterns

Key references to retain: Charles Fillmore, **Frame Semantics** (1982); Adele Goldberg, **Constructions: A Construction Grammar Approach to Argument Structure** (1995). Relevant future areas: argument structure, thematic/semantic roles, construction grammar, compositional semantics, lexical semantics, terminology science.

## 3. Metrology and quantity ontologies

### BIPM SI / VIM
Retain strict separation of Quantity, Quantity Value, numerical quantity value, measurand and measurement result. SI unit-one practice already exposes semantic pressure points: Hz versus Bq, Gy versus Sv, rad/sr, explicit ratio units, percent/ppm. Current project note: SI Brochure 9th edition was revised in 2026; verify exact current version when citing. VIM4 was still in development during this project snapshot.

### QUDT
QUDT explicitly separates Quantity/QuantityKind/Unit/dimension vector and recognizes quantities associated with objects/events/systems as properties. Therefore PG must **not** claim that existing systems know only number+unit or that quantity kind ≠ dimension is novel. PG's target difference is compositional grounding genealogy and controlled semantic loss.

### OM (Ontology of units of Measure)
Rijgersberg, van Assem & Top, “Ontology of units of measure and related concepts” (2013), DOI `10.3233/SW-2012-0069`. OM supports particular quantities linked to phenomena/bearers. Hence Property→bearer grounding itself is not PG novelty.

### BFO / OntoCAPE
Bearer-dependent qualities and system/property modeling are established ontology territory. Do not import large realist hierarchies unless a benchmark forces them.

## 4. Programming-language/type-system precedents

### F# Units of Measure / dimensional type systems
Compile-time dimensional annotations, inference and erasure establish the precedent that semantic distinctions can be preserved statically and erased when safe. Dimension alone cannot distinguish energy/torque or frequency/activity.

### Dependent types
Atkey et al., “Models for Polymorphism over Physical Dimension” (2015), DOI `10.4230/LIPIcs.TLCA.2015.45`, and related work show that physical dimensions can index types. PG should say: **Entity dependency is a semantic commitment; dependent typing is one possible formal realization.** Do not define PG as a dependent type theory.

### Coeffects
Petricek, Orchard & Mycroft, “Coeffects: Unified Static Analysis of Context-Dependence” (2013), DOI `10.1007/978-3-642-39212-2_35`. This is a close PL precedent for tracking what an expression requires from context. A candidate judgment such as `Γ;Σ ⊢ e : P ▷ D` may eventually model Entity context, Scope/prerequisites and residual dependencies, but it is **not canonical**.

## 5. Provenance / information flow / compositionality

### Provenance and lineage
Green, Karvounarakis & Tannen (2007) provenance semirings and later fine-grained lineage work establish that composition + genealogy tracking is not novel generically. PG's distinction is **physical grounding provenance**, not data provenance: `A -> OccupiedRegion[A] -> Volume[...]` is semantic grounding, not “this output came from file row 42”.

### Information flow / noninterference analogy
Projection safety is structurally analogous to information-flow reasoning: a downstream query must not depend on discarded information. This is precedent/analogy, not a claim of new factorization mathematics.

### Applied Category Theory
Fong & Spivak, *An Invitation to Applied Category Theory* / *Seven Sketches in Compositionality* (arXiv `1803.05316`) provides compositional-system precedents. ACT asks how systems/processes compose; PG's characteristic question is what the resulting physical expression remains **about**. PG may admit categorical semantics but should not be defined by category theory.

## 6. Count and unit-one quantities

David Flater (2023), “Dealing with counts and other quantal quantities in quantity calculus” (Measurement/NIST context), is relevant to count/quantal quantities and the limitations of purely continuous quantity calculus. This supports treating Count as a useful distinction in some views without committing to a universal replacement dimension ontology.

## 7. Modelica / FMI / OpenMath

Modelica variables distinguish `quantity`, `unit`, `displayUnit`, and its documentation notes that a unit expression alone may not distinguish physical meanings such as torque and energy. Connector roles (potential/flow/stream) are useful precedents for explicit semantic roles. Modelica's goal is executable system modeling; PG's is semantic dependency/grounding of physical expressions.

FMI examples involving torque/energy, angle/angular velocity/frequency and percent/ppm show that these semantic collisions are practical interchange problems. OpenMath is relevant as an extensible semantic serialization/backend precedent.

## 8. Novelty ledger

### Do not claim as novel
- unit/dimension checking;
- quantity kind distinct from dimension;
- Property→bearer or particular-entity quantities;
- semantic mathematical expressions;
- physical-system composition;
- semantic roles generically;
- count/unit-one enrichment;
- dependency tracking/provenance/compositionality generically.

### Stronger PG contribution candidates
- compositional tracking of **physical grounding** dependencies;
- Grounding Closure specialized to physical referents;
- grounding genealogy through physical constructions;
- task-relative projection safety specialized to physical semantics;
- integration of grounding genealogy and explicit semantic projection/loss in a typed compositional IR;
- use of the semantic parse as an upstream substrate for physical-quantity nomenclature.

Recommended positioning:

> **Physical Grammar is a semantic dependency calculus for physical expressions, implemented as a typed compositional IR.**

Purpose:

> **Track the introduction, propagation, binding, elimination, representation and projection of scientifically relevant distinctions.**

## 9. Adopt / Extend / Reject / Compare discipline

For every related field/reference record whether PG should:

- **Adopt** an established concept/terminology;
- **Extend** it for physical grounding/composition;
- **Compare** as a neighboring formalism;
- **Reject** unnecessary ontology/formalism.

This prevents novelty inflation and unnecessary reinvention.
