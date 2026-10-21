"""Finite witnesses for M4 batch 1 and a retrospective B018 dependency sketch.

Run from any directory: python path/to/m4_checks.py. No third-party dependencies.
The functions evaluate declared mathematical examples, not a PG parser/type proof.
"""

from fractions import Fraction as F
import json

from pgcheck import Entity, Relation, closure, derivative, genealogy, math, prop


def collision(samples, project, query):
    """Find an actual same-projection/different-query pair; no pair means unknown.

    Callers supply a valid domain and pure, deterministic functions. Equality must
    be exact; these fixtures use rational numbers/tuples rather than float tolerances.
    """
    rows = [(project(x), query(x)) for x in samples]
    # ponytail: quadratic finite scan; suitable for witnesses, never a universal proof.
    for right, (p_right, q_right) in enumerate(rows):
        for left in range(right):
            p_left, q_left = rows[left]
            if p_left == p_right and q_left != q_right:
                return {"status": "unsafe", "pair": [left, right],
                        "projection": p_left, "query_values": [q_left, q_right]}
    return {"status": "unknown", "reason": "No counterexample in supplied samples"}


def pair_average(values):
    if not values or len(values) % 2:
        raise ValueError("Adjacent equal-volume pairs required")
    return tuple((values[i] + values[i + 1]) / 2 for i in range(0, len(values), 2))


def marginals(table):
    if len(table) != 2 or any(len(row) != 2 for row in table):
        raise ValueError("This witness uses a 2 by 2 table")
    if any(p < 0 for row in table for p in row) or sum(map(sum, table)) != 1:
        raise ValueError("Probabilities must be nonnegative and normalized")
    return tuple(map(sum, table)), tuple(sum(row[j] for row in table) for j in range(2))


def self_check():
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    # M010 input is reduced flux q*Phi/(2*pi*hbar); phase lives in R/Z.
    fluxes = (F(0), F(1, 2), F(1))
    local_fields = lambda flux: (0, 0)  # fixed field-free accessible domain
    phase_class = lambda flux: flux % 1
    ab = collision(fluxes, local_fields, phase_class)
    check("M010 local fields do not determine phase", ab["status"] == "unsafe")
    check("M010 full-turn control shares phase", phase_class(fluxes[0]) == phase_class(fluxes[2]))
    check("M010 shared phase not a false counterexample",
          collision((fluxes[0], fluxes[2]), local_fields, phase_class)["status"] == "unknown")

    # M015 equal fine-cell volumes v=1; positive density arrays.
    densities = (tuple(map(F, (1, 3, 1, 3))), tuple(map(F, (2, 2, 2, 2))))
    mean_square = lambda r: sum(x*x for x in r) / len(r)
    coarse = collision(densities, pair_average, mean_square)
    check("M015 positive admissible densities", all(x > 0 for r in densities for x in r))
    check("M015 identical coarse profiles", pair_average(densities[0]) == pair_average(densities[1]))
    check("M015 fluctuation query lost", coarse["query_values"] == [F(5), F(4)])
    check("M015 mass factorization holds on fixtures",
          all(sum(r) == 2*sum(pair_average(r)) for r in densities))
    check("No observed collision must not imply safe",
          collision(densities, pair_average, sum)["status"] == "unknown")
    check("Empty samples are unknown", collision((), pair_average, sum)["status"] == "unknown")

    correlated = ((F(1, 2), F(0)), (F(0), F(1, 2)))
    anticorrelated = ((F(0), F(1, 2)), (F(1, 2), F(0)))
    coincidence = lambda table: table[0][0] + table[1][1]
    pair = collision((correlated, anticorrelated), marginals, coincidence)
    check("M020 both marginals match", marginals(correlated) == marginals(anticorrelated))
    check("M020 pair query differs", pair["query_values"] == [F(1), F(0)])
    p_a, p_b = marginals(correlated)
    independent = tuple(tuple(x*y for y in p_b) for x in p_a)
    check("M020 product lift retains marginals", marginals(independent) == (p_a, p_b))
    check("M020 product lift does not restore correlation",
          coincidence(independent) == F(1, 2) and independent not in (correlated, anticorrelated))
    try:
        marginals(((F(1), F(1)), (F(0), F(0))))
    except ValueError:
        checks.append("M020 invalid probability table rejected")
    else:
        raise AssertionError("unnormalized table accepted")

    # B018 fixed-composition scope with two explicitly enumerated species.
    a, b = Entity("material_A"), Entity("unrelated_B")
    cp_total = derivative(prop("Enthalpy", a), prop("Temperature", a), fixed=(
        prop("Pressure", a), prop("Amount_species1", a), prop("Amount_species2", a)))
    cp_specific = math("Divide", cp_total, prop("Mass", a))
    right_relation = Relation("Definition", prop("SpecificHeatCapacityAtConstantPressure", a), cp_specific)
    wrong_relation = Relation("Definition", right_relation.left, math("Divide", cp_total, prop("Mass", b)))
    check("B018 reconstructed dependency closure", closure(right_relation) == {"unresolved": [], "untraced_left": []})
    check("B018 mass normalization preserved", genealogy(cp_specific) != genealogy(cp_total))
    check("B018 unrelated mass detected", closure(wrong_relation)["unresolved"] == ["unrelated_B"])
    check("B018 context closure is not physical correctness",
          closure(wrong_relation, context=(b,))["unresolved"] == [])
    return {"checks_passed": len(checks), "checks": checks,
            "witnesses": {"M010": ab, "M015": coarse, "M020": pair},
            "limit": "Finite witnesses prove specified reductions unsafe; absence of a witness is unknown. No grammar grades are inferred."}


if __name__ == "__main__":
    print(json.dumps(self_check(), indent=2, default=str))
