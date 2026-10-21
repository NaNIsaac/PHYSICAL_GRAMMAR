"""M011/M012/M017/M018 constructed checks; no external dependencies."""

from cmath import exp
from fractions import Fraction as F
import json
from math import isclose, sqrt

from m4_checks import collision
from pgcheck import Entity, dependencies, genealogy, prop


def polygon_winding(points):
    """Exact ray crossings for an explicitly closed rational polygon avoiding zero."""
    if len(points) < 4 or points[0] != points[-1] or any(len(p) != 2 for p in points):
        raise ValueError("Closed 2D polygon required")
    winding = 0
    for (ax, ay), (bx, by) in zip(points, points[1:]):
        cross = ax*by-ay*bx
        if cross == 0 and ax*bx+ay*by <= 0:
            raise ValueError("Origin on contour; winding undefined")
        if ay <= 0 < by and cross > 0:
            winding += 1
        elif by <= 0 < ay and cross < 0:
            winding -= 1
    return winding


def self_check():
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    def rejects(name, action):
        try:
            action()
        except ValueError:
            checks.append(name)
        else:
            raise AssertionError(name)

    # ponytail: polygon interpolation is explicit; arbitrary sampled fields need extra regularity bounds.
    diamond = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 0))
    check("M011 positive oriented winding", polygon_winding(diamond) == 1)
    check("M011 reversed orientation", polygon_winding(diamond[::-1]) == -1)
    check("M011 double traversal", polygon_winding(diamond+diamond[1:]) == 2)
    constant = ((1, 0),)*5
    check("M011 constant contour", polygon_winding(constant) == 0)
    endpoint_loss = collision((constant, diamond), lambda p: p[0], polygon_winding)
    check("M011 endpoint loses winding", endpoint_loss["status"] == "unsafe")
    deform = lambda s: tuple((s+(1-s)*x, (1-s)*y) for x, y in diamond)
    check("M011 nonzero homotopy before crossing", polygon_winding(deform(F(1, 4))) == 1)
    check("M011 nonzero homotopy after crossing", polygon_winding(deform(F(3, 4))) == 0)
    rejects("M011 zero vertex rejected", lambda: polygon_winding(deform(F(1, 2))))
    rejects("M011 zero along edge rejected", lambda: polygon_winding(((1, 0), (-1, 0), (0, 1), (1, 0))))
    rejects("M011 open path rejected", lambda: polygon_winding(diamond[:-1]))
    # Exact phase turns for exp(2*pi*i*k*t), t in {0,1/4,1/2,3/4}.
    samples = lambda k: tuple((k*F(j, 4)) % 1 for j in range(4))
    check("M011 identical samples can hide different continuous winding",
          collision((0, 4), samples, lambda k: k)["status"] == "unsafe")

    turns = lambda cosine: -(1-cosine)/2
    phase = lambda cosine: turns(cosine) % 1
    loops = (F(0), F(1, 2))
    berry_loss = collision(loops, lambda c: "north_pole_basepoint", phase)
    check("M012 same basepoint different holonomy", berry_loss["query_values"] == [F(1, 2), F(3, 4)])
    check("M012 periodic gauge winding preserves phase",
          all((turns(c)-k) % 1 == phase(c) for c in loops for k in (-2, 0, 3)))
    endpoint_shift = F(1, 3)
    check("M012 nonperiodic gauge needs endpoint correction",
          (turns(F(1, 2))-endpoint_shift+endpoint_shift) % 1 == phase(F(1, 2))
          and (turns(F(1, 2))-endpoint_shift) % 1 != phase(F(1, 2)))
    check("M012 reversing loop negates phase", (-turns(F(1, 2))) % 1 == F(1, 4))
    # Independent spinor derivative/eigenvector control for H=-n_hat dot sigma, Delta=1.
    cosine, phi = 0.5, 0.7
    spinor = (sqrt((1+cosine)/2), exp(1j*phi)*sqrt((1-cosine)/2))
    dphi = (0, 1j*spinor[1])
    connection = 1j*sum(z.conjugate()*dz for z, dz in zip(spinor, dphi))
    sine = sqrt(1-cosine*cosine)
    hpsi = (-cosine*spinor[0]-sine*exp(-1j*phi)*spinor[1],
            -sine*exp(1j*phi)*spinor[0]+cosine*spinor[1])
    check("M012 spinor normalized", isclose(sum(abs(z)**2 for z in spinor), 1))
    check("M012 declared ground eigenvector", all(abs(h+z) < 1e-12 for h, z in zip(hpsi, spinor)))
    check("M012 connection sign from spinor", abs(connection+0.25) < 1e-12)

    def estimate(y, a, b):
        if a <= 0:
            raise ValueError("Positive calibration slope required in this fixture")
        return (F(y)-b)/a

    records = ((10, F(1), F(0)), (10, F(2), F(0)))
    calibration_loss = collision(records, lambda r: r[0], lambda r: estimate(*r))
    check("M017 same indication different estimates", calibration_loss["query_values"] == [F(10), F(5)])
    check("M017 forward inverse consistency", all(a*estimate(y, a, b)+b == y for y, a, b in records))
    check("M017 offset retained", estimate(10, F(2), F(2)) == 4)
    rejects("M017 zero slope rejected", lambda: estimate(10, 0, 0))
    rejects("M017 negative slope outside declared domain", lambda: estimate(10, -1, 0))
    check("M017 uncertainty scales with inverse slope", [F(1)/r[1] for r in records] == [F(1), F(1, 2)])
    check("M017 point estimate loses uncertainty",
          collision((F(1), F(2)), lambda uncertainty: F(10), lambda uncertainty: uncertainty)["status"] == "unsafe")
    sample, device, trial = Entity("sample"), Entity("device"), Entity("trial")
    check("M017 instrument output and sample pressure have different roots",
          dependencies(prop("OutputVoltage", device, trial)) != dependencies(prop("Pressure", sample, trial)))

    vickers, knoop = Entity("Vickers_procedure"), Entity("Knoop_procedure")
    expressions = (prop("Hardness", sample, vickers, trial), prop("Hardness", sample, knoop, trial))
    check("M018 procedure genealogy differs", genealogy(expressions[0]) != genealogy(expressions[1]))
    procedure_loss = collision(("Vickers", "Knoop"), lambda p: "Hardness[sample]", lambda p: p)
    check("M018 generic label loses procedure", procedure_loss["status"] == "unsafe")
    # NIST certificate rounded ideal coefficient, SI F/d^2; no interscale conversion.
    def vickers_si(force, diagonal):
        if force <= 0 or diagonal <= 0:
            raise ValueError("Positive load and mean diagonal required")
        return F("1.8544")*force/diagonal**2

    d = F(1, 10000)
    check("M018 declared Vickers arithmetic", vickers_si(F(1), d) == F(185440000))
    check("M018 diagonal doubling quarters value", vickers_si(F(1), 2*d) == vickers_si(F(1), d)/4)
    rejects("M018 zero diagonal rejected", lambda: vickers_si(F(1), 0))
    rejects("M018 negative load rejected", lambda: vickers_si(F(-1), d))
    check("M018 absent physical conversion evidence stays unknown",
          collision((), lambda hv: hv, lambda hk: hk)["status"] == "unknown")

    return {"checks_passed": len(checks), "checks": checks,
            "witnesses": {"M011": endpoint_loss, "M012": berry_loss, "M017": calibration_loss, "M018": procedure_loss},
            "limit": "Polygon/spinor/calibration fixtures and procedure labels; no measured material conversion or full grammar proof."}


if __name__ == "__main__":
    print(json.dumps(self_check(), indent=2, default=str))
