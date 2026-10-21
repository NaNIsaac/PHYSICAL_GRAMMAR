"""Matched M001/M003 development fixtures; exact arithmetic, no kernel changes.

Finite record sufficiency is shared mathematics. Typed records are experimental
baseline syntax, not a general physical type system or independent PG encoding.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
import json

from pgcheck import Entity, derivative, genealogy, prop


@dataclass(frozen=True)
class Property:
    name: str
    slots: tuple[str, ...]
    unit: str


@dataclass(frozen=True)
class Derivative:
    body: Property
    wrt: Property
    fixed: tuple[Property, ...]
    unit: str


# Identical signatures/context are supplied to both representations.
UNITS = {"Displacement": "m", "Force": "N", "Volume": "m3",
         "Pressure": "Pa", "Temperature": "K", "Entropy": "J/K", "Amount": "mol"}
ARITIES = {name: (2 if name in ("Displacement", "Force") else 1) for name in UNITS}


def validate(expr):
    for p in (expr.body, expr.wrt, *expr.fixed):
        if p.name not in UNITS or p.unit != UNITS[p.name] or len(p.slots) != ARITIES[p.name]:
            raise ValueError("Invalid property signature")
    if expr.unit != expr.body.unit + "/" + expr.wrt.unit:
        raise ValueError("Invalid derivative unit")
    if expr.wrt in expr.fixed:
        raise ValueError("Differentiation variable is held fixed")


def pg_encode(expr):
    validate(expr)
    def encode(p):
        return prop(p.name, *(Entity(s) for s in p.slots))
    return derivative(encode(expr.body), encode(expr.wrt), fixed=tuple(map(encode, expr.fixed)))


def property_(name, *slots):
    return Property(name, slots, UNITS[name])


def deriv(body, wrt, *fixed):
    return Derivative(body, wrt, fixed, body.unit + "/" + wrt.unit)


def fixtures():
    # M001: x = inverse([[2,-1],[-1,2]]) F in fixed reference units.
    spring = tuple(deriv(property_("Displacement", "spring", target),
                         property_("Force", "spring", source),
                         property_("Force", "spring", target))
                   for target, source in (("A", "B"), ("B", "A")))
    # M003: pV=nRT, normalized p=V=nR=T=1, gamma=5/3.
    gas = tuple(deriv(property_("Volume", "gas"), property_("Pressure", "gas"),
                      property_(condition, "gas"), property_("Amount", "gas"))
                for condition in ("Temperature", "Entropy"))
    return spring, gas


def finite_decision(states, retained, query):
    # No required-distinction or safe/unsafe annotation is consumed.
    for a, b in combinations(range(len(states)), 2):
        if retained(states[a]) == retained(states[b]) and query(states[a]) != query(states[b]):
            return {"decision": "unsafe", "witness_indices": [a, b],
                    "answers": [query(states[a]), query(states[b])]}
    return {"decision": "safe", "witness_indices": None}


def oracle_decision(case_id):
    """Independent case ledger: explicit values, no Property/PG objects.

    This is an independent decision path over the supplied fixtures, not an
    independent physical model or reviewer. Keeping it separate catches a
    projection/genealogy implementation mistake in the main comparison.
    """
    if case_id.startswith("M001"):
        records = [("A", "B", F(1, 3)), ("B", "A", F(1, 3))]
        if case_id == "M001_drive_role":
            projected = [("A", "B"), ("A", "B")]
            answers = ["B", "A"]
        elif case_id == "M001_reciprocal_value":
            projected = [("A", "B"), ("A", "B")]
            answers = [r[2] for r in records]
        else:
            projected = records
            answers = ["B", "A"]
    elif case_id.startswith("M003"):
        records = [("Volume", "Pressure", "Temperature", "Amount", F(1)),
                   ("Volume", "Pressure", "Entropy", "Amount", F(3, 5))]
        if case_id == "M003_condition_erased":
            projected = [(r[0], r[1]) for r in records]
        elif case_id == "M003_condition_reordered":
            projected = [(r[0], r[1], r[3], r[2]) for r in records]
        else:
            projected = records
        answers = [r[4] for r in records]
    else:
        raise ValueError(case_id)
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            if projected[i] == projected[j] and answers[i] != answers[j]:
                return {"decision": "unsafe", "witness_indices": [i, j],
                        "answers": answers[i:j + 1]}
    return {"decision": "safe", "witness_indices": None}


def run():
    spring, gas = fixtures()
    for expr in (*spring, *gas):
        validate(expr)
    # Input-boundary checks: malformed declarations must fail before comparison.
    invalid = (
        Derivative(Property("Force", ("spring",), "N"), spring[0].wrt,
                   spring[0].fixed, "N/m"),
        Derivative(spring[0].body, spring[0].wrt, spring[0].fixed, "bad/unit"),
        Derivative(spring[0].body, spring[0].fixed[0], spring[0].fixed, "m/N"),
    )
    rejected = 0
    for expr in invalid:
        try:
            validate(expr)
        except ValueError:
            rejected += 1
    assert rejected == len(invalid)
    spring_value = lambda expr: F(1, 3)
    # Derived tangents: fixed T gives dV/dp=-1; fixed S gives -1/gamma.
    gas_value = lambda expr: -F(1) if expr.fixed[0].name == "Temperature" else -F(3, 5)
    # Query is compressibility -(1/V)dV/dp at V=1, not the bare derivative.
    compressibility = lambda expr: -gas_value(expr)
    unordered = lambda expr: tuple(sorted((expr.body.slots[1], expr.wrt.slots[1])))
    erased_condition = lambda expr: (expr.body, expr.wrt)
    rows = []
    specs = (
        ("M001_drive_role", spring, unordered, lambda e: e.wrt.slots[1]),
        ("M001_reciprocal_value", spring, unordered, spring_value),
        ("M001_full_record", spring, None, lambda e: e.wrt.slots[1]),
        ("M003_condition_erased", gas, erased_condition, compressibility),
        ("M003_full_record", gas, None, compressibility),
        ("M003_condition_reordered", gas, lambda e: (e.body, e.wrt, tuple(reversed(e.fixed))), compressibility),
    )
    for name, states, projection, query in specs:
        # Lossy projections are shared externally declared record operations.
        # Full records exercise each representation's exact syntax identity.
        generic = finite_decision(states, projection or (lambda e: e), query)
        pg = finite_decision(states, projection or (lambda e: genealogy(pg_encode(e))), query)
        oracle = oracle_decision(name)
        assert generic == pg == oracle
        rows.append({"id": name, "domain_size": len(states), "generic": generic,
                     "pg": pg, "oracle": oracle})
    # Analytic checks independent of the finite-fiber search.
    assert F(2, 3)*2 - F(1, 3) == 1
    assert -F(2, 3) + 2*F(1, 3) == 0
    gamma = F(5, 3)
    dt_dp = (gamma-1)/gamma
    assert dt_dp-1 == -1/gamma
    assert gamma/(gamma-1)*dt_dp-1 == 0
    assert len(set(spring)) == len({genealogy(pg_encode(e)) for e in spring}) == 2
    assert len(set(gas)) == len({genealogy(pg_encode(e)) for e in gas}) == 2
    assert sum(r["generic"]["decision"] == "unsafe" for r in rows) == 2
    return {"scope": "Six two-state diagnostics from two supplied M4 models; not unseen evaluation",
            "cases": rows, "finding": "Both encodings agree; shared exhaustive finite mathematics decides all six.",
            "input_boundary": {"malformed_records_rejected": rejected},
            "limits": ["No continuous-domain safety inference", "No general type or constraint solver",
                       "Automatic PG translation; human annotation cost unmeasured",
                       "Shared model evaluator; no independent oracle review"]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, default=str))
