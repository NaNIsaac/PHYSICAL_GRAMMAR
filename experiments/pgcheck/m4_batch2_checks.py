"""Exact constructed witnesses for M008/M009/M016/M019; not a PG type proof."""

from fractions import Fraction as F
import json

from m4_checks import collision


def relay(history, initial=-1):
    """Normalized axial model; supplied points delimit monotone drive segments."""
    if initial not in (-1, 1) or not history:
        raise ValueError("A +/-1 initial branch and nonempty history are required")
    # ponytail: one axial switching element; richer minor loops need a new model.
    state = initial
    for field in history:
        if field >= 1:
            state = 1
        elif field <= -1:
            state = -1
    return state


def inverse2(matrix):
    """Exact inverse for the two-dimensional rational Hessian fixtures."""
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("A 2 by 2 matrix is required")
    (a, b), (c, d) = (tuple(map(F, row)) for row in matrix)
    determinant = a*d - b*c
    if not determinant:
        raise ValueError("Singular curvature has no finite inverse mass tensor")
    return ((d/determinant, -b/determinant), (-c/determinant, a/determinant))


def self_check():
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    histories = ((-2, 2, 0), (-2, 0))
    hysteresis = collision(histories, lambda h: h[-1], relay)
    check("M008 equal field, opposite magnetizations",
          hysteresis["status"] == "unsafe" and hysteresis["query_values"] == [1, -1])
    check("M008 subthreshold reversal retains state", relay((2, F(-1, 2), 0)) == 1)
    check("M008 negative threshold switches", relay((2, -1, 0)) == -1)
    check("M008 positive threshold switches", relay((-2, 1, 0)) == 1)
    check("M008 initial state matters without a switching event",
          relay((0,), 1) == 1 and relay((0,), -1) == -1)
    check("M008 final state suffices for model continuation",
          all(relay(h + (F(1, 2), -2, 0)) == relay((F(1, 2), -2, 0), relay(h))
              for h in histories))

    # phi=a*x+b*t, A=(d*x+e*t,0,0); E=(-a-e,0,0), B=0.
    # chi=c*x*t sends (a,b,d,e) to (a-c,b,d,e+c).
    fields = lambda p: (-p[0]-p[3], 0)
    gauge = lambda p, c: (p[0]-c, p[1], p[2], p[3]+c)
    zero = (F(0),)*4
    shifted = gauge(zero, F(2))
    gauge_loss = collision((zero, shifted), fields, lambda p: p[3])
    check("M009 same fields, distinct A_x at x=0,t=1",
          gauge_loss["status"] == "unsafe" and gauge_loss["query_values"] == [0, 2])
    nonzero = tuple(map(F, (3, 4, 5, 6)))
    check("M009 gauge inverse restores representative", gauge(gauge(nonzero, F(2)), F(-2)) == nonzero)
    check("M009 nonzero fields also invariant", fields(gauge(nonzero, F(2))) == fields(nonzero))
    check("M009 missing compensation changes E", fields((-2, 0, 0, 0)) != fields(zero))

    hessians = (((1, 0), (0, 1)), ((2, 1), (1, 2)))
    # e(q)=q^T H q/2; both e(0) and grad e(0) vanish.
    band = collision(hessians, lambda h: (0, (0, 0)), inverse2)
    check("M016 local energy and gradient do not determine mass", band["status"] == "unsafe")
    check("M016 off-diagonal matrix inverse",
          inverse2(hessians[1]) == ((F(2, 3), F(-1, 3)), (F(-1, 3), F(2, 3))))
    check("M016 inverse times Hessian is identity",
          all(sum(inverse2(h)[i][k]*h[k][j] for k in range(2)) == int(i == j)
              for h in hessians for i in range(2) for j in range(2)))
    check("M016 negative curvature is allowed", inverse2(((-1, 0), (0, 1)))[0][0] == -1)
    # e(q)=|q|^2/2+c*qx^4: same 2-jet at zero, different energy at (1,0).
    quartic = collision((F(0), F(1)), lambda c: hessians[0], lambda c: F(1, 2)+c)
    check("M016 quadratic view loses finite-displacement energy",
          quartic["status"] == "unsafe" and quartic["query_values"] == [F(1, 2), F(3, 2)])

    configurations = ((0, 1), (1, 0))
    orbit = lambda x: tuple(sorted(x))
    label = collision(configurations, orbit, lambda x: x[0])
    check("M019 slot coordinate does not descend", label["status"] == "unsafe")
    check("M019 separation and spatial occupancy survive on fixtures",
          all(abs(x[0]-x[1]) == orbit(x)[1]-orbit(x)[0]
              and sum(v < F(1, 2) for v in x) == sum(v < F(1, 2) for v in orbit(x))
              for x in configurations))
    check("M019 multiplicity retained", orbit((0, 0)) == (0, 0))
    # In |LL>,|LR>,|RL>,|RR>, conjugation by swap permutes diagonal entries.
    swap_diagonal = lambda d: (d[0], d[2], d[1], d[3])
    q1, occupation = (1, 1, 0, 0), (2, 1, 1, 0)
    check("M019 auxiliary label projector not permutation invariant", swap_diagonal(q1) != q1)
    check("M019 quantum occupation operator invariant", swap_diagonal(occupation) == occupation)
    check("Finite no-collision result remains unknown",
          collision(configurations, orbit, lambda x: abs(x[0]-x[1]))["status"] == "unknown")

    for name, operation in (
        ("M008 empty history rejected", lambda: relay(())),
        ("M008 invalid initial state rejected", lambda: relay((0,), 0)),
        ("M016 singular Hessian rejected", lambda: inverse2(((1, 1), (1, 1)))),
        ("M016 malformed Hessian rejected", lambda: inverse2(((1,), (0, 1)))),
    ):
        try:
            operation()
        except ValueError:
            checks.append(name)
        else:
            raise AssertionError(name)

    return {"checks_passed": len(checks), "checks": checks,
            "witnesses": {"M008": hysteresis, "M009": gauge_loss, "M016": band, "M019": label},
            "limit": "Constructed model/representation checks only; no grammar grades or universal safe verdicts inferred."}


if __name__ == "__main__":
    print(json.dumps(self_check(), indent=2, default=str))
