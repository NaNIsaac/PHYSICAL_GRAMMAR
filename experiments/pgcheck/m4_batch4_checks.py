"""Exact M001/M002/M013/M014 witnesses; standard-library self-check."""

from fractions import Fraction as F
import json

from m4_checks import collision
from m4_batch2_checks import inverse2
from pgcheck import Entity, dependencies, derivative, genealogy, prop


def self_check():
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    compliance = inverse2(((2, -1), (-1, 2)))
    orders = ((0, 1), (1, 0))
    roles = collision(orders, lambda pair: tuple(sorted(pair)), lambda pair: pair[1])
    check("M001 unordered bodies lose drive role", roles["status"] == "unsafe")
    check("M001 conservative model is reciprocal", compliance[0][1] == compliance[1][0] == F(1, 3))
    check("M001 equal values are not a loss witness",
          collision(orders, lambda pair: tuple(sorted(pair)),
                    lambda pair: compliance[pair[0]][pair[1]])["status"] == "unknown")
    a, b, s = Entity("A"), Entity("B"), Entity("system")
    ab = derivative(prop("Displacement", s, a), prop("Force", s, b), fixed=(prop("Force", s, a),))
    ba = derivative(prop("Displacement", s, b), prop("Force", s, a), fixed=(prop("Force", s, b),))
    check("M001 root sets miss ordered experiment difference", dependencies(ab) == dependencies(ba))
    check("M001 genealogy retains ordered experiment", genealogy(ab) != genealogy(ba))

    # ponytail: fixed one-dimensional passive fixtures; extend geometry only for a new case.
    def restitution(before, after, normal=1):
        if len(before) != 2 or len(after) != 2 or normal not in (-1, 1):
            raise ValueError("Two velocities and a unit 1D normal required")
        incoming = (before[1]-before[0])*normal
        outgoing = (after[1]-after[0])*normal
        if not incoming < 0 or not 0 <= outgoing <= -incoming:
            raise ValueError("Outside approaching passive-collision domain")
        return -F(outgoing)/F(incoming)

    trials = (((1, -1), (F(-1, 2), F(1, 2))),
              ((2, 0), (F(1, 2), F(3, 2))))
    restitution_loss = collision(trials, lambda t: restitution(*t), lambda t: t[1][0])
    check("M002 restitution alone loses body velocity", restitution_loss["status"] == "unsafe")
    check("M002 both trials have e one half", all(restitution(*t) == F(1, 2) for t in trials))
    check("M002 equal-mass momentum conserved", all(sum(pre) == sum(post) for pre, post in trials))
    check("M002 consistent relabeling preserves e",
          all(restitution(pre[::-1], post[::-1], -1) == restitution(pre, post) for pre, post in trials))
    check("M002 center-of-mass kinetic energy ratio is e squared",
          sum(v*v for v in trials[0][1])/sum(v*v for v in trials[0][0]) == F(1, 4))
    for name, args in (("zero approach", ((0, 0), (0, 0))),
                       ("reversed stages", (trials[0][1], trials[0][0])),
                       ("invalid normal", (*trials[0], 0))):
        try:
            restitution(*args)
        except ValueError:
            checks.append("M002 rejects " + name)
        else:
            raise AssertionError(name)

    # c=1; all components remain in the declared reference units.
    dot = lambda p, u: p[0]*u[0]-sum(x*y for x, y in zip(p[1:], u[1:]))
    p, u0, u1 = (F(1), 0, 0, 0), (F(1), 0, 0, 0), (F(5, 4), F(3, 4), 0, 0)
    energy_loss = collision(((p, u0), (p, u1)), lambda pair: pair[0], lambda pair: dot(*pair))
    check("M013 observer erasure loses energy", energy_loss["query_values"] == [F(1), F(5, 4)])
    check("M013 observer normalization", dot(u0, u0) == dot(u1, u1) == 1)
    boost = lambda w: (F(5, 4)*w[0]-F(3, 4)*w[1], F(5, 4)*w[1]-F(3, 4)*w[0], *w[2:])
    check("M013 common coordinate boost preserves energy", dot(boost(p), boost(u1)) == dot(p, u1))
    check("M013 boosted observer is at rest", boost(u1) == u0)
    momenta = (u1, (F(5, 4), F(-3, 4), 0, 0))
    energy_only = collision(momenta, lambda w: dot(w, u0), lambda w: dot(w, u1))
    check("M013 same mass in energy-only pair", all(dot(w, w) == 1 for w in momenta))
    check("M013 one energy cannot predict another", energy_only["query_values"] == [F(1), F(17, 8)])

    # Fixed beta=+/-3/5 avoids square-root rounding in the inverse control.
    def field_boost(pair, direction=1):
        e, bfield = pair
        v, gamma = direction*F(3, 5), F(5, 4)
        return ((e[0], gamma*(e[1]-v*bfield[2]), gamma*(e[2]+v*bfield[1])),
                (bfield[0], gamma*(bfield[1]+v*e[2]), gamma*(bfield[2]-v*e[1])))

    fields = (((0, 1, 0), (0, 0, 0)), ((0, 1, 0), (0, 0, 1)))
    transformed = field_boost(fields[0])
    check("M014 same field acquires observer magnetic component",
          transformed == ((0, F(5, 4), 0), (0, 0, F(-3, 4))))
    controls = (*fields, ((1, 2, 3), (4, 5, 6)))
    check("M014 inverse boost restores all six components",
          all(field_boost(field_boost(f), -1) == f for f in controls))
    invariants = lambda f: (sum(x*x for x in f[0])-sum(x*x for x in f[1]),
                            sum(x*y for x, y in zip(*f)))
    check("M014 both scalar invariants retained",
          all(invariants(field_boost(f)) == invariants(f) for f in controls))
    field_loss = collision(fields, lambda f: f[0], lambda f: field_boost(f)[0][1])
    check("M014 electric-only reduction fails", field_loss["query_values"] == [F(5, 4), F(1, 2)])
    check("M014 parallel field components unchanged",
          all(field_boost(f)[0][0] == f[0][0] and field_boost(f)[1][0] == f[1][0] for f in controls))

    return {"checks_passed": len(checks), "checks": checks,
            "witnesses": {"M001": roles, "M002": restitution_loss, "M013": energy_loss, "M014": field_loss},
            "limit": "Declared rational fixtures, not tensor typing, physical validation or G/E grading."}


if __name__ == "__main__":
    print(json.dumps(self_check(), indent=2, default=str))
