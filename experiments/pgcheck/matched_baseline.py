"""Matched-information development comparison; exact finite domains, no packages.

Inputs contain expressions and domains, never safe/unsafe or loss annotations.
The exhaustive reference oracle runs only after predictions have been collected.
"""
from dataclasses import dataclass
from itertools import product
import json

from pgcheck import Entity, dependencies, math, prop


@dataclass(frozen=True)
class Node:
    op: str
    args: tuple = ()
    key: str = ""


def var(key):
    return Node("var", key=key)


def op(name, *args):
    return Node(name, args)


def free(node):
    return {node.key} if node.op == "var" else set().union(*(free(a) for a in node.args))


def evaluate(node, state):
    if node.op == "var":
        return state[node.key]
    a, b = (evaluate(x, state) for x in node.args)
    return {"add": lambda: a + b, "sub": lambda: a - b,
            "mul": lambda: a * b}[node.op]()


def pg_encode(node):
    if node.op == "var":
        return prop("Coordinate", Entity(node.key))
    return math(node.op, *(pg_encode(a) for a in node.args))


@dataclass(frozen=True)
class Case:
    key: str
    source: str
    variables: tuple
    query: Node
    retained: tuple
    # All coordinates in each case share one supplied abstract dimension.
    # Domains are explicitly finite; no continuous-domain safety claim follows.
    values: tuple = (0, 1)

    def states(self):
        return [dict(zip(self.variables, xs))
                for xs in product(self.values, repeat=len(self.variables))]


def cases():
    rows = []
    specs = (
        ("role", "M001", ("source", "target"), "sub"),
        ("constraint", "M003", ("state", "branch"), "add"),
        ("observer", "M013", ("body", "observer"), "sub"),
        ("history", "M007", ("present", "memory"), "add"),
    )
    for name, source, keys, operation in specs:
        a, b = map(var, keys)
        q = op(operation, a, b)
        rows.append(Case(name + "_drop", source, keys, q, (a,)))
        # Reordering a complete coordinate record is a legitimate representation.
        rows.append(Case(name + "_reorder", source, keys, q, (b, a)))
    x, y = var("x"), var("y")
    rows.append(Case("invertible_mix", "mathematical control", ("x", "y"),
                     x, (op("add", x, y), op("sub", x, y))))
    rows.append(Case("cancellation", "mathematical control", ("x", "y"),
                     op("sub", x, x), (y,)))
    return rows


def collision(case):
    seen = {}
    for state in case.states():
        retained = tuple(evaluate(x, state) for x in case.retained)
        answer = evaluate(case.query, state)
        if retained in seen and seen[retained][1] != answer:
            return {"left": seen[retained][0], "right": state,
                    "retained": retained, "answers": [seen[retained][1], answer]}
        seen[retained] = (state, answer)
    return None


def predict(case, method):
    if method == "dimension":
        # All expressions are dimensionally compatible. Compatibility alone
        # cannot prove that the retained record determines the query.
        return "unknown"
    if method == "generic_ast":
        required = free(case.query)
    elif method == "pg":
        required = {e.key for e in dependencies(pg_encode(case.query))}
    else:
        raise ValueError(method)
    # Shared, fixed rule: retaining every syntactically used coordinate suffices.
    retained_keys = {n.key for n in case.retained if n.op == "var"}
    if required <= retained_keys:
        return "safe"
    # Shared exact mathematical capability, credited equally to both encodings.
    if collision(case) is not None:
        return "unsafe"
    return "unknown"


def reference(case):
    # Deliberately separate pairwise algorithm from the checker's hash-fiber search.
    states = case.states()
    for a in states:
        for b in states:
            same_record = all(evaluate(n, a) == evaluate(n, b) for n in case.retained)
            if same_record and evaluate(case.query, a) != evaluate(case.query, b):
                return "unsafe"
    return "safe"


def run():
    corpus = cases()
    methods = ("dimension", "generic_ast", "pg")
    predictions = {m: [predict(c, m) for c in corpus] for m in methods}
    # Independent decision path for truth: exhaustive fibers, no dependency test.
    truth = [reference(c) for c in corpus]
    metrics = {}
    for method, results in predictions.items():
        metrics[method] = {
            "false_safe": sum(p == "safe" and t == "unsafe" for p, t in zip(results, truth)),
            "false_unsafe": sum(p == "unsafe" and t == "safe" for p, t in zip(results, truth)),
            "unknown": results.count("unknown"),
            "correct_decisions": sum(p == t for p, t in zip(results, truth)),
            "total": len(corpus),
        }
    # Experiment integrity checks, distinct from diagnostic-case counts.
    assert predictions["generic_ast"] == predictions["pg"]
    assert truth.count("safe") == 6 and truth.count("unsafe") == 4
    for c in corpus:
        assert free(c.query) == {e.key for e in dependencies(pg_encode(c.query))}
        witness = collision(c)
        if witness:
            assert witness["answers"][0] != witness["answers"][1]
            assert tuple(evaluate(n, witness["left"]) for n in c.retained) == tuple(
                evaluate(n, witness["right"]) for n in c.retained)
    return {
        "scope": "10 finite abstract development diagnostics, not physical regrading",
        "metrics": metrics,
        "cases": [{"id": c.key, "inspiration": c.source, "reference": t,
                   "predictions": {m: predictions[m][i] for m in methods},
                   "witness": collision(c)} for i, (c, t) in enumerate(zip(corpus, truth))],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
