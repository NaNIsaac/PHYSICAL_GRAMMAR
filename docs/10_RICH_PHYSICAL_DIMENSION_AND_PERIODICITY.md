# Rich Physical Dimension, Angle, Count, and Periodicity

## 1. Status

`rich_physical_dimension` (RPD) is a **working internal projection/view**, not a new universal dimension system.

`[D]_R` means a task-/Scope-relative dimensional view that preserves selected distinctions useful for the current comparison. Ordinary SI remains the default user-facing dimensional system.

Conceptual pipeline:

`Physical Grammar semantics -> selected RPD view -> ordinary SI dimension`

RPD intentionally does **not** preserve full grounding/reference/model genealogy; that belongs in PG semantics.

## 2. Typical useful distinctions

Angle, SolidAngle, and Count are the most plausible recurring enrichments. Others should be introduced only when a task demonstrates need.

Examples:

- `[f]_R = T^-1`
- `[ω]_R = Angle T^-1`
- `[1/λ]_R = L^-1`
- `[k]_R = Angle L^-1`
- `[θ_geom]_R = [φ_phase]_R = Angle`

The last equality is deliberate: RPD may collapse geometric angle and phase because their different genealogy is handled by PG.

## 3. 2π doctrine

> **2π is evidence, not semantics.**

Use reference-first reasoning:

1. identify the reference physical quantity/phenomenon;
2. identify what is being counted or progressed;
3. determine whether cyclic/phase-angle representation is introduced;
4. only then interpret `2π`.

`ω = dφ/dt = 2πf` expresses cycle progression versus phase-angle progression. `C = 2πr` contains `2π` but circumference is not an angular quantity.

## 4. Phase versus geometric angle

- **Geometric angle:** relation between directions/orientations in geometric structure.
- **Phase:** cyclic position in a periodic structure relative to a phase reference.

They may share an `S^1`/angular mathematical representation without sharing physical grounding.

## 5. Count versus cycle progression

- `37 particles` is Entity cardinality and can legitimately be treated as Count.
- `3.7 cycles` is a coordinate/progression through periodic structure, not cardinality of 3.7 objects.

Do not introduce `Cycle` as a default independent RPD dimension merely to explain frequency.

## 6. Same-property conversion test

An equation `X = C Y` does not imply that X and Y are the same physical Property or should share RPD identity. Ask whether the relation is merely a unit/scale representation of the same Property.

`N = N_A n` can be treated as a scale-like correspondence between entity count and amount-of-substance views in an appropriate Scope. By contrast, `E = k_B T` is a physical cross-kind correspondence and does not make Energy and Temperature the same Property.

Natural-unit conventions are powerful representational/dimensional identifications, not automatic semantic identity.
