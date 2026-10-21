# Semantic Parse Sheet and 20-Item Calibration

**Purpose:** preserve the post-v0.4 calibration results without promoting every diagnostic category into the grammar.

## 1. Semantic Parse Sheet v0

For each quantity/property ask only the questions that matter. **N/A is a valid result; do not force every slot to be filled.**

1. Property — what is characterized?
2. Grounding — about what referent(s)?
3. Roles — do referents have semantically distinct roles?
4. Reference — relative to what?
5. Indices / Resolution — what distinctions remain independently resolved (`x,t,λ,Ω,...`)?
6. Conditions — what is held fixed or constrained?
7. Prerequisites — what structure is presupposed for meaningfulness?
8. Construction — ratio, derivative, integral, comparison, etc.?
9. Representation — how is the same meaning represented?
10. Projection / elimination — what distinctions are discarded/bound?
11. Value structure — scalar/vector/tensor/manifold/etc.?
12. Dimension — SI; optional RPD only when useful.
13. Naming — head, modifiers, lexicalized/omitted distinctions, transparency.

Benchmark record should additionally mark `[G]/[M]/[D]`, nearest minimal pairs, reducibility G0–G4, distinguishability, naming yield, and grammar pressure.

## 2. Calibration summary

| # | Quantity | Main stress point | Main finding | Naming yield |
|---:|---|---|---|---|
| 1 | mass | baseline | simple Entity-grounded Property | none |
| 2 | temperature field | Site/indexing | field-ness is orthogonal to scalar/vector/tensor value structure | explanatory |
| 3 | distance | multi-grounding | relation can be grounded in multiple referents; EntityMap genealogy matters | explanatory+ |
| 4 | force | asymmetric roles | dependency set `{A,B}` can lose Source/Target information | explanatory |
| 5 | volume | EntityMap | `Volume[OccupiedRegion[A]]`; material/interior/enclosed regions distinguish volume notions | productive candidate |
| 6 | mass density | normalization | recurring `dX/dμ` density family; denominator measure matters | productive |
| 7 | heat flux | transport/boundary | `/area` alone is insufficient; boundary/orientation and transport semantics matter | mixed |
| 8 | spectral radiance | resolution | spectral modifier preserves wavelength/frequency resolution; integration removes it | strong |
| 9 | susceptibility | response | derivative shape alone does not identify quantity; stimulus/response roles matter | productive candidate |
| 10 | isothermal compressibility | constrained response | held-fixed `T` is part of quantity identity and lexicalized by `isothermal` | strong |
| 11 | vorticity | differential operator | operator domain (`x`, `k`, parameter space...) matters | explanatory |
| 12 | total radiance | integration/binding | integration eliminates spectral resolution; modifier deletion mirrors semantic elimination | strong |
| 13 | work function | reference difference | same energy-difference skeleton can denote different Properties due to reference genealogy | opaque |
| 14 | chemical potential | constrained derivative | Property identity is not a particular derivative representation; held-fixed set matters | explanatory |
| 15 | frequency | periodicity | cyclic progression is not Entity cardinality | strong |
| 16 | angular frequency | phase representation | `ω=dφ/dt=2πf`; angular modifier corresponds to phase-angle progression, not mere scaling | strong |
| 17 | wavenumber | spatial periodicity | `k=∇φ` gets directional/covector structure from gradient, not dimension; naming is irregular | mixed |
| 18 | particle number | Count | cardinality of entities differs from fractional cycle progression | productive |
| 19 | radioactive activity | same-dimension collision | activity and frequency both SI `T^-1`; semantic construction distinguishes them | opaque |
| 20 | Debye temperature | model-derived quantity | same K/value/bearer need not mean same Property; Debye model is external semantic seed | model/eponym |

## 3. Calibration findings R1–R4

These are **benchmark findings, not new AST nodes**.

### R1 — Role and genealogy sensitivity
Grounding analysis must be able to preserve role and genealogy when downstream distinctions depend on them. `Force[A,B]` versus `Force[B,A]` shows why a plain dependency set may be insufficient.

### R2 — Condition sensitivity
Quantity identity may depend on held-fixed/constrained conditions that are neither ordinary Entity grounding nor value structure. `κ_T` versus `κ_S` is the canonical example.

### R3 — Semantic dependence beyond grounding
Grounding is central but not exhaustive. Index/resolution, reference, condition, operator domain and representation choices can carry semantics. Do not yet collapse these into one universal dependency object.

### R4 — Prerequisite sensitivity
Some Properties/constructions are meaningful only relative to prerequisite structures that need not be focal Entity groundings: metric structure for distance, cyclic structure for phase, differential structure for gradients. `Prerequisite` remains a diagnostic analysis notion.

## 4. Position / angle / phase clarification

### Position
A physical position is grounded in an object/site but requires spatial/reference structure. Coordinates are a representation of position, not the position itself. Distinguish a site `x` from the spatial structure `S` in which sites/positions are meaningful.

### Geometric angle
A geometric angle is typically relational between directions/orientations, or an orientation relative to a reference direction. It presupposes suitable directional/geometric structure.

### Phase
Phase is cyclic position in a periodic structure relative to a phase reference. It does not require physical space. Geometric angle and phase can share angular representation/RPD while differing in grounding genealogy.

### Reference versus prerequisite
For a pendulum angle, the pendulum is grounding, vertical may be the comparison reference, and spatial/directional geometry is prerequisite structure. Do not merge these roles.

## 5. Naming patterns found in calibration

1. **Lexical primitive:** `mass`, `force` — structure does not predict the conventional word.
2. **Construction head:** `mass density` — head such as `density` can encode a recurring construction family.
3. **Distinction modifier:** `spectral radiance`, `isothermal compressibility`, `angular frequency` — modifier lexicalizes a preserved distinction/condition/representation.
4. **Opaque/historical lexicalization:** `work function`, radioactive `activity` — semantic parse distinguishes the quantity even when the conventional name is not structurally transparent.
5. **Model/eponym modifier:** `Debye temperature` — name carries model provenance rather than generic grammar alone.

A useful research question is therefore:

> **Does a good physical-quantity name lexicalize the construction, preserved distinctions, grounding, or provenance that matter for distinguishing the quantity?**

## 6. Important negative conclusions

- Formula shape does not determine quantity identity.
- SI dimension does not determine quantity identity.
- Same numerical value + unit + bearer does not determine Property identity.
- A `2π` factor does not by itself imply angular semantics.
- A useful analysis category does not automatically deserve a grammar node.
