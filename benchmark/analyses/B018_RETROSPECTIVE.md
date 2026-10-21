# B018 — retrospective reconstruction, not recovered evidence

Date: 2026-09-09. Original frozen target: **specific heat capacity at constant pressure**.
Historical reported grade: G2. This record does not replace the missing original parse.

## Verified external definition

IUPAC, [Green Book, 4th edition abridged](https://iupac.org/wp-content/uploads/2025/03/IUPAC-GB4Abridged.pdf),
printed p. 4 (PDF page 16) explicitly gives cp=Cp/m; section 4.11, printed p. 49
(PDF page 61) gives Cp=(partial H/partial T)_p and unit J/K. Both passages were
retrieved. Therefore cp has unit J/(kg K), while Cp has unit J/K. The result-ledger
title's omission of “specific” changes the stated quantity, not just capitalization.

## Declared scope and parse

Use one closed, fixed-composition material system A in a differentiable equilibrium
state family, away from a phase-transition singularity. Pressure p and all species
amounts n_i are fixed in the derivative. Declare the species index set I explicitly.
These are the reconstruction's scope conditions, not claims about the lost original.

```text
Cp[A] := Derivative(H[A], T[A], fixed=[p[A], n_i[A] for i in I])
cp[A] := Cp[A] / Mass[A]
```

Grounding: A throughout; enthalpy, temperature, pressure and mass refer to the same
system. Composition is a specified indexed family, not an unexplained context label.
The derivative is evaluated at the declared state; state coordinates and I are
mathematical arguments/context. There is no eliminated Entity dependency. Constructor
genealogy retains the derivative and subsequent normalization. Value structure is
scalar for this scope. Quantify exposes the specific quantity; no measured numerical
value is inferred. Reference is the stated thermodynamic state convention.

The minimal pair cp[A] versus Cp[A] differs by mass normalization; cp[A] versus
cv[A] also changes held-fixed conditions and the differentiated potential. Replacing
Mass[A] with unrelated Mass[B] is an unresolved dependency unless separately supplied.
Supplying B in context resolves reference availability, not correctness of the
physical definition. A dependency-only checker cannot establish that normalization
uses the intended bearer merely because all referents are available.

## Knowledge, projection and disposition

[G]: same-bearer composition, genealogy and explicit conditions. [M]: partial
differentiation and division. [D]: enthalpy/heat-capacity semantics, equilibrium
state specification and the specific-quantity convention. **Reconstructed G2 / E1**
is consistent with the historical G2 under these declared inputs, but cannot certify
the original grading without its seed inventory and parse.

The SI dimensions already distinguish cp and Cp. Dimensional projection still loses
the bearer, composition conditions and genealogy, so it cannot answer those queries.
No normalization may be dropped as mere unit conversion between the same Property.
Naming yield is productive here: “specific” corresponds to division by the bearer's
mass. The original ledger is preserved; a future erratum should cite this record
and explicitly acknowledge whether the original analysis itself can be recovered.
