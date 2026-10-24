# Nomenclature and Identity Registry Continuation — 2026-10-25

**Status:** working downstream design; not a v0.4 kernel change.

## 1. Why nomenclature is downstream

The current design treats scientific naming as a lossy lexicalization of richer semantic structure.

A useful schematic is:

`physical meaning → semantic parse → naming projection → surface name`

or abstractly:

`N(Q) = L(π_N(S(Q)))`

where `S(Q)` is a richer semantic structure, `π_N` selects distinctions worth lexicalizing in the current naming scope, and `L` renders them into a conventional label.

A good name therefore need not contain the full definition. It should expose enough distinctions for the intended naming context.

## 2. Two naming surfaces

Keep two surfaces distinct:

1. **Semantic descriptor** — compositional and explicit.
2. **Conventional label** — established or concise terminology.

Examples:

- semantic descriptor: `vacuum-referenced electron removal energy`
- conventional label: `work function`

- semantic descriptor: `wavelength-resolved radiance`
- conventional label: `spectral radiance`
- symbol: `L_λ`

- semantic descriptor: `frequency-resolved radiance`
- conventional label: `spectral radiance`
- symbol: `L_ν`

The collision in the last two examples is useful data: conventional names are not guaranteed unique identifiers.

## 3. Identity is not a label

The registry should preserve the invariant:

`semantic identity ≠ label ≠ symbol ≠ descriptor ≠ historical identifier`

Consequences:

- renaming a concept need not change its identity;
- changing the preferred symbol need not change identity;
- synonyms/translations belong to the same identity;
- an invertible transform between two quantities does not automatically merge their identities;
- same unit/dimension does not establish identity;
- a legacy identifier that once covered several later concepts must not silently redirect to one of them.

## 4. Working identifier families

### PQP — proposal identity

Use a proposal identifier before adjudication.

A submitted candidate does **not** receive a permanent concept identity immediately.

Possible decisions:

- `MERGE_AS_ALIAS`
- `REGISTER_DISTINCT`
- `HOLD_AMBIGUOUS`
- `REJECT_UNDERSPECIFIED`

### PGQ — registered quantity identity

Stable opaque identifier for a registered quantitative concept.

Human-readable names/slugs remain metadata, not the identity key.

### PGE — terminology/lifecycle event

Records post-registration changes such as:

- preferred-name change;
- symbol change;
- deprecation;
- replacement;
- split/merge event;
- descriptor revision.

### PGS — source snapshot

A versioned external source snapshot or source record.

### PGC — scoped claim

A claim supported by a particular source/version/scope.

### PGR — relation assertion

A versioned typed assertion connecting registered identities.

If the meaning of a relation changes, issue a new relation assertion rather than silently reusing the old edge identity.

These prefixes are working conventions, not yet a finalized public namespace.

## 5. Alias policy

### Same identity

Synonyms, translations, and historical names can resolve to one identity when the underlying semantic concept is unchanged.

### Distinct but related

Concepts remain distinct when the identity-bearing structure differs, even if a direct transform exists.

Examples:

- wavelength-resolved radiance ↔ frequency-resolved radiance;
- isothermal compressibility ↔ isentropic compressibility;
- heat capacity ↔ specific heat capacity.

### Ambiguous surface term

A surface string may intentionally resolve to multiple candidates.

Example:

`spectral radiance` → wavelength-resolved or frequency-resolved form depending on context.

A resolver without enough context should return ambiguity rather than manufacture certainty.

## 6. Registration examples

### Heat capacity under constant pressure

If the semantic parse matches an existing constant-pressure heat-capacity identity, register the submitted wording as an alias rather than a new PGQ.

### Specific heat capacity at constant pressure

Mass normalization changes the concept boundary, so this is a distinct identity even though it is closely related to heat capacity at constant pressure.

### Differential cross section

The surface term may remain collision-prone because the resolved variable/measure can differ. The registry should preserve the resolution context rather than force one universal referent for the name.

## 7. Lifecycle rules

1. **Semantic boundary changes must not be silent.**
2. Preferred names/symbols/descriptors may change while the concept identity remains stable.
3. Deprecated aliases should remain resolvable with warnings and replacement hints.
4. A legacy identifier may redirect automatically only when the mapping is semantically 1→1.
5. A legacy 1→many split must require explicit disambiguation.
6. Historical provenance should remain queryable after terminology cleanup.

## 8. Authority and provenance

External authorities support **scoped claims**; they do not create semantic identity merely by naming something.

A provenance record should distinguish:

- source;
- source version/date;
- domain/authority scope;
- claim type;
- whether support is direct or partial.

This avoids statements such as “source X defines the one true identity globally.”

Examples motivating scoped authority:

- two quantities can share the same SI unit while remaining distinct;
- a term such as `activity` can denote unrelated concepts in different domains;
- terminology conventions can differ by field while the semantic distinction still matters.

## 9. Semantic linter direction

The most promising practical output may be a semantic terminology linter rather than an automatic name generator.

Candidate checks:

- a name omits a distinction that is essential in the current scope;
- one surface name maps to multiple registered identities;
- a modifier is inconsistent with the construction/restriction/resolution;
- a symbol collides with another identity in the same context;
- a deprecated alias is used when a preferred term exists;
- a candidate name suggests a construction different from the registered semantic structure.

## 10. Relation to the core project

The nomenclature registry consumes semantic structure; it should not become the source of that structure.

Preferred direction:

`R/T/C/A/G/D/K/... semantic structure → S-ID identity → registry → descriptor/name/symbol`

This preserves the original naming motivation while keeping nomenclature downstream of semantic analysis.
