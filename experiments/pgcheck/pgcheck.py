"""Disposable PG v0.4 dependency experiment. Python standard library only.

These Python records are an experimental encoding, not new grammar primitives.
No parser, numerical physics, dimension checker or complete type checker is claimed.
"""

from dataclasses import dataclass
import json
import math as numeric


@dataclass(frozen=True)
class Entity:
    key: str
    parents: tuple = ()

    def __post_init__(self):
        if not self.key or not all(isinstance(p, Entity) for p in self.parents):
            raise ValueError("Entity requires a key and Entity parents")


def entity_map(name, *parents):
    if not parents:
        raise ValueError("EntityMap requires at least one parent")
    return Entity(name, parents)


def roots(entity):
    if not entity.parents:
        return frozenset((entity,))
    return frozenset().union(*(roots(p) for p in entity.parents))


@dataclass(frozen=True)
class Expr:
    op: str
    args: tuple = ()
    slots: tuple = ()
    binder: Entity | None = None
    fixed: tuple = ()


def prop(name, *entities):
    if not all(isinstance(e, Entity) for e in entities):
        raise TypeError("Property slots must contain Entities in this experiment")
    return Expr(name, slots=entities)


def math(name, *args):
    if not all(isinstance(a, Expr) for a in args):
        raise TypeError("Math operands must be expressions")
    return Expr(name, args=args)


def bind(kind, variable, domain, body):
    if kind not in {"Integral", "Sum"}:
        raise ValueError("Only Integral and Sum binding are supported")
    # Distinct keys are explicit binder identities, not printed variable names.
    if not isinstance(variable, Entity) or variable.parents:
        raise ValueError("Binder must be a fresh root Entity")
    if not isinstance(domain, Expr) or not isinstance(body, Expr):
        raise TypeError("Domain and body must be expressions")
    if variable in dependencies(domain):
        raise ValueError("Binder cannot occur free in its own domain")
    return Expr(kind, args=(body, domain), binder=variable)


def derivative(body, wrt, *, fixed=()):
    if not all(isinstance(x, Expr) for x in (body, wrt, *fixed)):
        raise TypeError("Derivative arguments must be expressions")
    return Expr("Derivative", args=(body, wrt), fixed=tuple(fixed))


def dependencies(expr):
    """Free root Entities; binding removes only body dependencies, never domain."""
    if expr.binder is not None:
        body, domain = expr.args
        return (dependencies(body) - {expr.binder}) | dependencies(domain)
    return frozenset().union(
        *(roots(e) for e in expr.slots),
        *(dependencies(a) for a in (*expr.args, *expr.fixed)),
    )


@dataclass(frozen=True)
class Relation:
    kind: str
    left: Expr
    right: Expr

    def __post_init__(self):
        if self.kind not in {"Definition", "Law", "Constraint", "ConstitutiveRelation"}:
            raise ValueError("Unsupported relation kind")


def closure(relation, *, context=()):
    """Report traceability; matching dependencies do not prove a physical relation."""
    supplied = frozenset().union(*(roots(e) for e in context))
    left, right = dependencies(relation.left), dependencies(relation.right)
    return {
        "unresolved": sorted(e.key for e in right - left - supplied),
        "untraced_left": sorted(e.key for e in left - right - supplied),
    }


def entity_tree(entity):
    return (entity.key, tuple(entity_tree(p) for p in entity.parents))


def genealogy(expr):
    """Exact ordered syntax only: neither semantic equality nor alpha-equivalence."""
    # ponytail: explicit binder keys; add alpha-normalization only for semantic comparison.
    return (
        expr.op,
        tuple(entity_tree(e) for e in expr.slots),
        tuple(genealogy(a) for a in expr.args),
        entity_tree(expr.binder) if expr.binder else None,
        tuple(genealogy(f) for f in expr.fixed),
    )


@dataclass(frozen=True)
class Contract:
    name: str
    preserves: frozenset
    loses: frozenset

    def __post_init__(self):
        if self.preserves & self.loses:
            raise ValueError("A distinction cannot be both preserved and lost")


def sufficiency(contract, requires):
    """Conditional on trusted, task-specific annotations; no factorization proof."""
    # ponytail: one trusted contract; composition needs source/target guarantee mapping.
    if requires & contract.loses:
        return "unsafe"
    if requires <= contract.preserves:
        return "safe"
    return "unknown"


def fixtures():
    """12 retrospective BB1 sketches, not recovered benchmark case records.

    The domain terms below are declared inputs. This code does not derive them.
    Conditions, time/state roles and domain predicates are manually specified.
    """
    body, axis, interval = Entity("body"), Entity("axis"), Entity("interval")
    site, time, species = Entity("site@sum1"), Entity("time@integral1"), Entity("species@sum1")
    system, contour, state = Entity("system"), Entity("contour"), Entity("state")
    a, b, collision = Entity("A"), Entity("B"), Entity("collision")
    trajectory = Entity("trajectory")
    volume = entity_map("OccupiedRegion", body)
    cases = []

    def add(case_id, label, lhs, rhs):
        cases.append((case_id, label, Relation("Definition", lhs, rhs)))

    add("B001", "moment of inertia", prop("MomentOfInertia", body, axis),
        bind("Integral", site, prop("VolumeDomain", volume),
             math("Mul", prop("MassDensity", body, site),
                  math("Square", prop("DistanceToAxis", site, axis)))))
    add("B002", "impulse", prop("Impulse", body, interval),
        bind("Integral", time, prop("TimeDomain", interval), prop("Force", body, time)))
    add("B003", "action", prop("Action", trajectory, interval),
        bind("Integral", time, prop("TimeDomain", interval),
             prop("LagrangianAlong", trajectory, time)))
    before, after = entity_map("Before", collision), entity_map("After", collision)
    add("B005", "coefficient of restitution", prop("Restitution", a, b, collision),
        math("Negate", math("Divide", prop("RelativeNormalVelocity", a, b, after),
                            prop("RelativeNormalVelocity", a, b, before))))
    add("B006", "radius of gyration", prop("RadiusOfGyration", body, axis),
        math("Sqrt", math("Divide", prop("MomentOfInertia", body, axis), prop("Mass", body))))
    component = Entity("component")
    add("B013", "chemical potential", prop("ChemicalPotential", system, component),
        derivative(prop("GibbsEnergy", system), prop("Amount", system, component),
                   fixed=(prop("Temperature", system), prop("Pressure", system),
                          prop("OtherAmounts", system, component))))
    add("B021", "vorticity", prop("Vorticity", body, site),
        math("SpatialCurl", prop("Velocity", body, site)))
    add("B022", "circulation", prop("Circulation", body, contour),
        bind("Integral", site, prop("OrientedLineDomain", contour),
             prop("TangentialVelocity", body, site, contour)))
    add("B025", "ionic strength", prop("IonicStrength", system),
        math("Half", bind("Sum", species, prop("SpeciesDomain", system),
                          math("Mul", prop("Concentration", system, species),
                               math("Square", prop("ChargeNumber", species))))))
    add("B028", "partial molar volume", prop("PartialMolarVolume", system, component),
        derivative(prop("Volume", system), prop("Amount", system, component),
                   fixed=(prop("Temperature", system), prop("Pressure", system),
                          prop("OtherAmounts", system, component))))
    wavevector, scatterer = Entity("wavevector"), Entity("scatterer@sum1")
    add("B047", "structure factor amplitude", prop("StructureFactor", system, wavevector),
        bind("Sum", scatterer, prop("ScattererDomain", system),
             math("Mul", prop("ScatteringAmplitude", scatterer, wavevector),
                  prop("PhaseFactor", scatterer, wavevector))))
    add("B054", "von Neumann entropy", prop("VonNeumannEntropy", state),
        math("MinusBoltzmannTimes", math("Trace", math("Mul", prop("DensityOperator", state),
                                                          math("Log", prop("DensityOperator", state))))))
    return cases


def self_check():
    a, b, site, region = Entity("A"), Entity("B"), Entity("x@1"), Entity("region")
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    bad = Relation("Definition", prop("KineticEnergy", a),
                   math("Mul", prop("Mass", b), math("Square", prop("Speed", a))))
    check("wrong bearer detected", closure(bad)["unresolved"] == ["B"])
    check("explicit context recognized", closure(bad, context=(b,))["unresolved"] == [])
    check("missing focal dependency reported",
          closure(Relation("Definition", prop("P", a), math("Constant")))["untraced_left"] == ["A"])
    mapped = prop("Volume", entity_map("OccupiedRegion", a))
    check("derived root retained", dependencies(mapped) == {a})
    check("EntityMap genealogy retained", genealogy(mapped) != genealogy(prop("Volume", a)))
    integral = bind("Integral", site, prop("Domain", region), prop("P", a, site))
    check("binder removed and domain retained", dependencies(integral) == {a, region})
    derived_body = prop("P", entity_map("Neighborhood", site), a)
    check("bound derived roots removed",
          dependencies(bind("Sum", site, prop("Domain", region), derived_body)) == {a, region})
    outside = math("Add", integral, prop("P", site))
    check("binding does not leak to sibling", dependencies(outside) == {a, region, site})
    check("ordered slots differ despite equal dependency sets",
          dependencies(prop("Force", a, b)) == dependencies(prop("Force", b, a))
          and genealogy(prop("Force", a, b)) != genealogy(prop("Force", b, a)))
    p, t = prop("Pressure", a), prop("Temperature", a)
    check("held-fixed conditions retained",
          genealogy(derivative(p, t, fixed=(prop("Volume", a),)))
          != genealogy(derivative(p, t, fixed=(prop("Entropy", a),))))
    check("held-fixed dependency checked", b in dependencies(derivative(p, t, fixed=(prop("Q", b),))))
    check("constructor order retained",
          genealogy(math("Rate", math("Density", p))) != genealogy(math("Density", math("Rate", p))))
    dim = Contract("DimensionProjection", frozenset({"dimension"}), frozenset({"grounding", "construction"}))
    check("declared guarantee safe", sufficiency(dim, {"dimension"}) == "safe")
    check("known loss unsafe", sufficiency(dim, {"construction"}) == "unsafe")
    check("missing guarantee unknown", sufficiency(dim, {"reference"}) == "unknown")
    for name, action in (
        ("contradictory contract rejected", lambda: Contract("bad", frozenset({"x"}), frozenset({"x"}))),
        ("self-dependent domain rejected", lambda: bind("Sum", site, prop("Domain", site), p)),
        ("unknown relation rejected", lambda: Relation("Same", p, t)),
    ):
        try:
            action()
        except ValueError:
            checks.append(name)
        else:
            raise AssertionError(name)
    rows = []
    for case_id, label, relation in fixtures():
        result = closure(relation)
        check(case_id + " dependency closure", result == {"unresolved": [], "untraced_left": []})
        rows.append({"id": case_id, "sketch": label, **result})
    # M007: independent midpoint integration checks the analytic memory witness.
    # Dimensionless time in relaxation-time units; small input stays in linear regime.
    amplitude, count = 0.01, 10000
    def input_b(t):
        return amplitude if -2 <= t <= -1 else 0.0
    response_b = sum(numeric.exp(-2 + (i + 0.5) / count)
                     * input_b(-2 + (i + 0.5) / count) / count for i in range(count))
    expected = amplitude * (numeric.exp(-1) - numeric.exp(-2))
    check("M007 identical current inputs", input_b(0) == 0.0)
    check("M007 distinct responses", response_b > 0.0)
    check("M007 analytic witness verified", numeric.isclose(response_b, expected, rel_tol=1e-8))
    return {"checks_passed": len(checks), "checks": checks, "sketches": rows,
            "M007_witness": {"input_A_now": 0.0, "input_B_now": input_b(0),
                             "response_A": 0.0, "response_B": response_b,
                             "analytic_response_B": expected},
            "meaning": "Annotated dependency sketches only; not semantic validation or BB1 regrading."}


if __name__ == "__main__":
    print(json.dumps(self_check(), indent=2))
