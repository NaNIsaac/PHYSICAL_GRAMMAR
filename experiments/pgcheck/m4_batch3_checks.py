"""M003-M006 constructed witnesses; run directly with standard-library Python."""

from fractions import Fraction as F
import json
from math import exp, isclose, log

from m4_checks import collision, marginals
from m4_batch2_checks import inverse2
from pgcheck import Entity, Relation, bind, closure, dependencies, derivative, genealogy, math, prop


def covariance(table):
    """Covariance of two normalized +/-1 site readings from a valid joint table."""
    pa, pb = marginals(table)  # Reuse probability shape/normalization validation.
    a, b = pa[1]-pa[0], pb[1]-pb[0]
    cross = sum(table[i][j]*(2*i-1)*(2*j-1) for i in range(2) for j in range(2)) - a*b
    return ((1-a*a, cross), (cross, 1-b*b))


def self_check():
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    # M003 p0=T0=V0=nR=1 in retained reference units; gamma=5/3.
    gamma = F(5, 3)
    gas = collision(("fixed_T", "fixed_S"), lambda path: ("same_state", "-dV/dp/V"),
                    lambda path: F(1) if path == "fixed_T" else 1/gamma)
    check("M003 erased condition hides unequal compressibilities",
          gas["status"] == "unsafe" and gas["query_values"] == [F(1), F(3, 5)])
    dt_dp = (gamma-1)/gamma
    dv_dp = dt_dp-1  # derivative of pV=T at the normalized state
    check("M003 isentropic tangent obeys entropy constraint", gamma/(gamma-1)*dt_dp-1 == 0)
    check("M003 isentropic tangent obeys equation of state", -dv_dp == 1/gamma)
    system = Entity("M003_sample")
    d_t = derivative(prop("Volume", system), prop("Pressure", system),
                     fixed=(prop("Temperature", system), prop("Amount", system)))
    d_s = derivative(prop("Volume", system), prop("Pressure", system),
                     fixed=(prop("Entropy", system), prop("Amount", system)))
    check("M003 same dependencies can carry different constraints",
          dependencies(d_t) == dependencies(d_s) and genealogy(d_t) != genealogy(d_s))

    # M004 retained units N=R=T0=c=h=1. The exact tangent uses G_xx=4,G_xT=-1.
    dx_dt = -F(-1)/F(4)
    chemical = collision((F(0), dx_dt), lambda tangent: ("same_state", "dH/dT"),
                         lambda tangent: 1+tangent)
    check("M004 equilibrium and frozen responses differ",
          chemical["status"] == "unsafe" and chemical["query_values"] == [F(1), F(5, 4)])
    check("M004 equilibrium tangent satisfies differentiated constraint", -1+4*dx_dt == 0)
    check("M004 species balance maintained", -dx_dt+dx_dt == 0)

    # ponytail: local normalized thermodynamic fixture, not a general equilibrium solver.
    x_eq = lambda t, h=1: 1/(1+exp(h*(1/t-1)))
    gibbs = lambda t, x: -t*log(t)+x*(1-t)+t*(x*log(x)+(1-x)*log(1-x))
    enthalpy = lambda t, x: t+x
    epsilon = 1e-5
    diff = lambda f, x: (f(x+epsilon)-f(x-epsilon))/(2*epsilon)
    check("M004 initial state is equilibrium", x_eq(1) == 0.5)
    check("M004 implicit solution obeys equilibrium near initial state",
          all(isclose(1-t+t*log(x_eq(t)/(1-x_eq(t))), 0, abs_tol=1e-12)
              for t in (0.9, 1.0, 1.1)))
    check("M004 Gibbs to enthalpy consistency",
          isclose(gibbs(1, 0.5)-diff(lambda t: gibbs(t, 0.5), 1), enthalpy(1, 0.5), abs_tol=1e-8))
    check("M004 equilibrium enthalpy derivative matches exact tangent",
          isclose(diff(lambda t: enthalpy(t, x_eq(t)), 1), float(F(5, 4)), abs_tol=1e-8))
    check("M004 frozen composition derivative is one",
          isclose(diff(lambda t: enthalpy(t, 0.5), 1), 1, abs_tol=1e-8))
    check("M004 zero reaction enthalpy removes extra response",
          x_eq(0.9, 0) == x_eq(1.1, 0) == 0.5
          and isclose(diff(lambda t: t+0*x_eq(t, 0), 1), 1, abs_tol=1e-8))

    # M005 finite sites use counting measure, k=F0=1 in retained units.
    stiffness = ((2, -1), (-1, 2))
    kernel = inverse2(stiffness)
    multiply = lambda matrix, vector: tuple(sum(a*b for a, b in zip(row, vector)) for row in matrix)
    response = lambda force: multiply(kernel, force)
    loads = ((1, 0), (1, 1))
    nonlocal_response = collision(loads, lambda f: f[0], lambda f: response(f)[0])
    check("M005 remote force changes local response",
          nonlocal_response["status"] == "unsafe" and nonlocal_response["query_values"] == [F(2, 3), F(1)])
    check("M005 full response preserves full source in this invertible model",
          all(multiply(stiffness, response(f)) == f for f in (*loads, (0, 2))))
    check("M005 one response does not identify remote force",
          collision(((1, 0), (0, 2)), lambda f: response(f)[0], lambda f: f[1])["status"] == "unsafe")
    model, trial, obs, src = (Entity(name) for name in ("M005_system", "trial", "observation", "source@sum"))
    body = math("Mul", prop("Kernel", model, obs, src), prop("Force", model, trial, src))
    integrated = bind("Sum", src, prop("SiteDomain", model), body)
    check("M005 source binder closes only source slot", dependencies(integrated) == frozenset((model, trial, obs)))
    check("M005 response dependency closure",
          closure(Relation("ConstitutiveRelation", prop("Displacement", model, trial, obs), integrated))
          == {"unresolved": [], "untraced_left": []})
    wrong = bind("Sum", obs, prop("SiteDomain", model), body)
    check("M005 wrong-site binding is detected",
          closure(Relation("ConstitutiveRelation", prop("Displacement", model, trial, obs), wrong))
          == {"unresolved": ["source@sum"], "untraced_left": ["observation"]})

    # M006 positive probability tables, order (-1,+1) at each site.
    tables = (((F(3, 8), F(1, 8)), (F(1, 8), F(3, 8))),
              ((F(1, 8), F(3, 8)), (F(3, 8), F(1, 8))))
    covariances = tuple(map(covariance, tables))
    diagonal = lambda c: (c[0][0], c[1][1])
    correlation = collision(covariances, diagonal, lambda c: c[0][1])
    check("M006 same local variances, opposite covariance",
          correlation["status"] == "unsafe" and correlation["query_values"] == [F(1, 2), F(-1, 2)])
    check("M006 both local marginals match", marginals(tables[0]) == marginals(tables[1]))
    check("M006 positive definite covariance witnesses",
          all(c[0][0] > 0 and c[0][0]*c[1][1]-c[0][1]**2 == F(3, 4) for c in covariances))
    check("M006 summed-field variance depends on lost covariance",
          [sum(map(sum, c)) for c in covariances] == [F(3), F(1)])
    # Biased independent marginals distinguish covariance from the raw second moment.
    biased = ((F(1, 16), F(3, 16)), (F(3, 16), F(9, 16)))
    check("M006 centering subtracts nonzero mean product",
          covariance(biased) == ((F(3, 4), F(0)), (F(0), F(3, 4))))
    check("M006 no collision is still unknown",
          collision(covariances, diagonal, lambda c: c[0][0]+c[1][1])["status"] == "unknown")
    try:
        covariance(((F(1), F(1)), (F(0), F(0))))
    except ValueError:
        checks.append("M006 invalid joint probabilities rejected")
    else:
        raise AssertionError("Invalid probability input accepted")

    return {"checks_passed": len(checks), "checks": checks,
            "witnesses": {"M003": gas, "M004": chemical, "M005": nonlocal_response, "M006": correlation},
            "limit": "Exact witnesses and local numeric controls; dependency sketches are not constraint/type proofs or grammar grades."}


if __name__ == "__main__":
    print(json.dumps(self_check(), indent=2, default=str))
