# Executable-formalism friction — 2026-09-09

This is implementation evidence from a disposable encoding, not a grammar revision.

| Observation | What the spike actually checks | Limit / next evidence needed |
|---|---|---|
| Root sets lose ordered roles | Exact ordered slot trees distinguish Force[A,B] and Force[B,A]. | Closure alone cannot reject a role reversal. No new Role primitive inferred. |
| EntityMaps need genealogy | Trees preserve map name and ordered parents; closure follows roots. | Maps sharing a root can have different semantic validity. No map signature checker yet. |
| Binding must be local | Body binder removal preserves domain dependencies and free siblings. | Keys must explicitly identify binders; no alpha-equivalence or coordinate typing. |
| Conditions carry dependencies | Derivative fixed expressions contribute dependencies and genealogy. | No proof of independent variables, admissible constrained path or complete held-fixed list. `OtherAmounts` in B013/B028 is an opaque declared seed needing expansion. |
| Matching roots is weak evidence | Twelve BB1-inspired sketches close. | Does not establish formula correctness, seed admissibility, value types or dimensions. B003's `LagrangianAlong` still hides trajectory evaluation. |
| Positive contracts are necessary | Required guaranteed distinction gives conditional safe; known loss unsafe; otherwise unknown. | Requires/Preserves are trusted external assertions. No automatic noninterference or factorization proof, and no contract composition. |
| Syntax is not physical identity | Constructor order and all slots survive serialization. | Equivalent formulas may compare unequal; same printed Entity key aliases the referent. |
| Elimination cannot be free erasure | Binding is implemented; unexplained missing LHS dependence is reported. | General normalization/invariance elimination deliberately remains unsupported until a concrete contract is specified. |
| History can be a function | M007 has an explicit input family and integral, plus an analytic loss witness. | Prototype sketches reify time/index referents; they do not implement M007's real-argument semantics. This mismatch is recorded rather than hidden. |

No result here justifies v0.6. The current experiment answers whether a few explicit
dependency mistakes can be caught, not whether the entire semantic IR has been formalized.

## First M4 batch continuation

- B018 confirms that supplying an unrelated bearer in context resolves availability
  without making its mass the right denominator. Closure is not a semantic proof.
- Finite exact collision search can establish a particular projection's insufficiency
  from two declared-domain examples. Failure to find a collision proves nothing;
  `m4_checks.py` explicitly returns unknown in that situation.
- The M010 phase and M020 marginal calculations are mathematical fixtures. Domain
  legitimacy and interpretation remain hand-reviewed. No fixture is a new grammar node.
- The combined two-file experiment remains small; real-time argument typing, map
  signatures, general elimination and proof-carrying contracts remain unsupported.
