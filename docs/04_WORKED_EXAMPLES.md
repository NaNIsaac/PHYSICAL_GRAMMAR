# Worked Examples — v0.4

These are development/doctrine examples, not substitutes for the future blind benchmark.

## 1. Density versus concentration

Density:

`MassDensity[A] := Mass[A] / Volume[OccupiedRegion[A]]`

Concentration:

`MassConcentration[C,W] := Mass[C] / Volume[OccupiedRegion[W]]  where PartOf[C,W]`

Both may reduce dimensionally to `M L^-3`; grounding structure distinguishes them.

Projection chain, schematically:

`grounded semantics → Mass/Volume skeleton → M L^-3`.

The dimensional projection is useful but cannot recover the component/whole relation that it discarded.

## 2. Height and resolution

Coarse:

`Height[P]`

Fine:

`Height[P] := Distance[CrownSite[P], SoleSite[P]]`

Primitive/derived status is resolution-relative. A Scope may retain explicit endpoint Sites or use a coarser lexicalized Property.

## 3. Internal force in a system

`S := System[A,B]`

`InternalForceA[S] := Force[PartA[S], PartB[S]]`

System construction does not automatically erase internal interactions. They disappear only under an admissible aggregate projection/law for the target question.

## 4. Center of mass

`CenterOfMass[S] := Sum_{A in Members[S]}(Mass[A] Position[A]) / Sum_{A in Members[S]} Mass[A]`

Member Entity dependencies are bound by the summation; `S` remains the focal grounding.

This is an example of dependency elimination by binding, not arbitrary forgetting.

## 5. Field snapshot

`Temperature[System,Site,Time]`

Ground System:

`Temperature[System]` — field family over Site × Time.

Fix Time as well:

`Temperature[System,t0]` — spatial snapshot.

The exact syntax for non-Entity coordinates remains provisional. The semantic point is that partial grounding/fixing exposes structured families.

## 6. Position, Site, and representation

`RelativePosition[A,R]`

where `R` is a reference/background Entity.

`Distance[A,B] := Norm(RelativePosition[A,B])`

Coordinates are representations of Site/position semantics, not the referents themselves.

A coordinate transformation may be information-preserving while changing numerical representation; it is not automatically a lossy projection.

## 7. Orientation: representation is not projection

`Orientation[A,R]`

may admit:

`Represent[Orientation[A,R], RotationMatrix]`

`Represent[Orientation[A,R], Quaternion]`

`Represent[Orientation[A,R], EulerAngles]`

These illustrate why representation is separate from Property identity and why the general representation graph need not be a DAG.

## 8. Stress: local projection chain

`Traction[x,n] = StressTensor[x] n`

`NormalStress[x,n] = n · StressTensor[x] n`

For an isotropic fluid under a chosen convention/model:

`StressTensor[x] = -Pressure[x] I`

Tensor → vector → scalar is a local projection chain. The constitutive/isotropy assumption is not a general definition of stress.

If only `NormalStress[x,n]` is retained, questions requiring the full stress tensor need not factor through that projection.

## 9. Heat and constitutive relations

`Temperature[State]` — state Property.

`HeatTransferred[Process]` — process-grounded Property.

`HeatFlux[Body,Site]` — local transport Property.

Fourier relation:

`HeatFlux = - Conductivity * Grad(Temperature)`

is constitutive/model-dependent, not definitional.

## 10. Electromagnetism and binding

A local current-density Property is grounded to the relevant field/system and Site. Surface integration binds local Site dependence and yields current through the selected surface.

Maxwell differential and integral forms should preserve the Entity genealogy between Region and Boundary under Gauss/Stokes transformations.

The integral transformation is not licensed to silently create or destroy unrelated Entity dependencies.

## 11. Thermodynamic constrained derivative

`C_V = (∂U/∂T)_V`

The held-fixed condition is semantic and must not be erased as decorative notation. A future generic constrained-derivative constructor may encode this without making thermodynamic names primitive grammar.

## 12. River depth: specification before value

Natural language:

“the depth of the river”

is underspecified. Candidate Properties include:

`Depth[River,Site,Time]`

`MeanDepth[River,Region,Time]`

`MaxDepth[River,Region,Interval]`

These are not merely different measurement procedures; they can be different Property/quantity specifications.

A Scope may later project a rich specification to a coarser summary, but that summary must not be used to answer questions that require the discarded Site/time/extremum distinction.

## 13. Quantity versus quantity value

`Mass[A]`

`-- Quantify --> m_A`  (VIM-compatible individual quantity/view)

`-- Determine/Measure --> 3.00 kg`  (quantity value / measurement result as appropriate)

Do not write `Quantify(Mass[A]) = 3 kg` as the canonical semantics unless intentionally collapsing the quantity/value distinction.

## 14. Projection-induced sameness: dimension

Suppose two rich semantic objects `A` and `B` have:

`DimensionProjection(A) = DimensionProjection(B)`.

Then:

`A ~_DimensionProjection B`.

This states only that the chosen dimension representation cannot distinguish them. It does not imply identical grounding, construction, role, or physical interpretation.

Examples in the benchmark family include density/concentration, frequency-like quantities, pressure/stress, and energy/torque.

## 15. Angle doctrine example

Optional rich internal view:

`[Angle]=Θ`.

Conventional projection:

`Θ → 1`.

After projection, dimensional distinctions that depended on `Θ` are no longer available. In particular, an angle-aware dimension view can distinguish structures that conventional dimensional analysis later identifies.

The project doctrine is:

> **Make angle dimensionless if you want. Just do not ask dimensional analysis to remember the distinction you erased.**

This is not an argument that SI practice is wrong; it is an example of explicit projection cost.

## 16. Deliberate coarse equivalence

Physical Grammar is not distinction-maximalist.

If a declared task does not use a distinction, a coarser representation may intentionally identify objects with respect to that task.

Operationally, for a fixed observable set `O_T`:

`A ~_T B` means every declared observable gives the same result.

If an experiment/model requires finite tolerance instead, write `A ≈_{T,ε} B`; do not call the tolerance relation an exact equivalence without proving the needed properties.

## 17. Projection error / use-after-projection

Consider:

```text
x : rich semantic object

d = DimensionProjection(x)

ask_semantic_kind(d)
```

The semantic question may require information not guaranteed by `DimensionProjection`.

Provisional diagnostic:

```text
ProjectionError:
    requested distinction: semantic construction
    unavailable after: DimensionProjection
```

This demonstrates the safety principle:

> **Loss is allowed; dependence on lost distinctions is not.**

## 18. Natural-language decompilation

Sentence:

“A block sliding down an incline experiences friction proportional to the normal force.”

Possible IR decomposition:

- Entities: `B:Block`, `P:Plane`, `C:Contact[B,P]`.
- Properties: contact force, surface normal, tangential/normal projections.
- Stated law: magnitude of friction is proportional to magnitude of normal component.
- Unresolved: friction regime and coefficient unless stated.

Principle:

`stated semantics != inferred physics`.

A decompiler should distinguish EXPLICIT, DERIVED (grammar/definition only), and ASSUMED/UNRESOLVED content.

## 19. Scientific data reduction — application only

Possible pipeline:

`RawFrame → CorrectedFrame → ROI → IntegratedProfile → PeakParameters`.

Each reduction can be annotated by its guarantees. If a future analysis needs to refit with a different ROI, a representation retaining only `PeakParameters` may be insufficient.

This does not make data archiving part of the Physical Grammar core. It demonstrates that the same factorization principle can guide scientific-data reduction and provenance design.
