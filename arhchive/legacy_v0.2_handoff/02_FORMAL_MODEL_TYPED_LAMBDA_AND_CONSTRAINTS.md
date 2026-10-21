# 02. Formal Model — Typed Lambda, Dependent Slots, Constraints

## 1. Working syntax

A Derived Feature Kind is represented as a constrained typed lambda-like definition:

\[
K := \lambda e_1\ldots e_n.\;\mathcal E
\quad \text{where }P(e_1,\ldots,e_n).
\]

This notation makes Entity identity explicit through bound-variable reuse.

Example:

\[
MassDensity := \lambda e.\frac{Mass(e)}{Volume(e)}.
\]

No extra `same_entity` predicate is required because both arguments reuse `e`.

Concentration:

\[
MassConcentration :=
\lambda c,w.\frac{Mass(c)}{Volume(w)}
\quad where\ PartOf(c,w).
\]

The arithmetic skeleton is the same; the binding graph differs.

## 2. Dependent interpretation

Feature Kinds often behave like dependent functions/types:

\[
Mass : \prod_{e:Entity} Quantity(e)
\]

\[
Position : \prod_{e:Entity}\prod_{s:StageEntity} PositionValue(s).
\]

Exact dependent-type foundations are not frozen, but this direction captures the essential fact that Feature existence/type depends on Entity/context slots.

## 3. Generalized algebraic theory analogy

The current grammar resembles a Generalized Algebraic Theory (GAT):

- sorts/types may depend on preceding variables;
- constructors have typed arity;
- contexts matter;
- substitutions instantiate definitions.

Use GAT/Categories-with-Families as mathematical reference, not as a novelty claim.

## 4. Constructor schema

Generic constructor:

\[
C:(F_1,\ldots,F_n)\rightharpoonup F'
\]

where the arrow may be partial because constraints must be satisfied.

Working constructor record:

```text
Constructor C:
    slots:
        a : TypeA
        b : TypeB
    roles:
        ...
    constraints:
        ...
    output:
        Feature
    synthesized_attributes:
        refs, dimension, value_structure, ...
```

## 5. Cross-slot equality is multidimensional

Do not conflate:

- same physical dimension;
- same Feature/Quantity Kind;
- same Entity;
- same occurrence/token;
- same numerical value;
- same Stage/reference.

Useful conceptual predicates:

```text
same_dimension(A,B)
same_kind(A,B)
same_entity(A,B)
same_occurrence(A,B)
same_value(A,B)
same_stage(A,B)
```

Two coordinate directions can have the same kind and dimension while being distinct occurrences/roles and accidentally equal in value.

## 6. Roles are not sorts

`Source`, `Target`, `Reference`, `Component`, `Whole`, `Stage`, `Focus`, `Through` are primarily **roles in a construction**, not necessarily ontology classes.

The same Entity can play different roles in different constructions.

## 7. Feature Kind as higher-order function

Many scientific modifiers are higher-order constructors:

\[
Specific := \lambda Q.\lambda e.\frac{Q(e)}{Mass(e)}
\]

\[
Volumic := \lambda Q.\lambda e.\frac{Q(e)}{Volume(e)}.
\]

Then:

\[
SpecificEnergy=Specific(Energy),
\qquad
MassDensity=Volumic(Mass).
\]

Named Feature Kinds can be treated as lexical aliases of reusable semantic expressions without implying that every physical law is a definition.

## 8. Definition expansion / reduction

Definitions may be unfolded to a finer semantic resolution:

```text
Height(E)
-> Extent(E, vertical)
-> Distance(ExtremeMinus(E), ExtremePlus(E))
-> metric(...)
```

This resembles definitional reduction but does not require one absolute normal form for every scientific context.

## 9. Attribute grammar analogy

Some information is naturally synthesized:

- referent set;
- dimension;
- tensor/value order;
- component signature;
- allowed representation.

Some context can be inherited:

- Stage;
- reference scheme;
- held-fixed variables;
- unit/view profile.

Attribute grammars are therefore a useful implementation analogy.

## 10. Constraint hierarchy

Before adding a new type, test:

1. re-expression;
2. composition;
3. view/projection change;
4. definition generalization;
5. existing type + constraint;
6. only then add a new primitive/sort.

But do not force inclusion: if a concept needs repeated special hacks, it may deserve a separate construction.
