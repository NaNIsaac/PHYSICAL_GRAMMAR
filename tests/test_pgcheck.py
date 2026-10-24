"""Rerun the pgcheck scripts and compare them with the counts and ledgers the docs report.

The scripts assert their own checks and exit nonzero on failure. These tests pin what
STATUS.md and experiments/pgcheck/README.md say about them, so a changed script or
ledger shows up as a failing test instead of a silently stale document.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
PGCHECK = ROOT / "experiments" / "pgcheck"

# Check counts as reported in STATUS.md and experiments/pgcheck/README.md (159 in total).
REPORTED_CHECKS = {
    "pgcheck": 33,
    "m4_checks": 18,
    "m4_batch2_checks": 25,
    "m4_batch3_checks": 26,
    "m4_batch4_checks": 24,
    "m4_batch5_checks": 33,
}


def run(script):
    proc = subprocess.run(
        [sys.executable, "-B", str(PGCHECK / f"{script}.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=120,
    )
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


def load(name):
    return json.loads((ROOT / "research" / name).read_text(encoding="utf-8"))


@pytest.mark.parametrize(("script", "count"), REPORTED_CHECKS.items())
def test_check_counts_match_the_reported_numbers(script, count):
    out = run(script)
    assert out["checks_passed"] == count == len(out["checks"])


def test_reported_total():
    assert sum(REPORTED_CHECKS.values()) == 159


def test_matched_baseline_reproduces_its_results_file():
    assert run("matched_baseline") == load("MATCHED_BASELINE_01_RESULTS.json")


def test_matched_models_reproduces_the_ledger_decisions():
    out = run("matched_models")
    ledger = load("MATCHED_MODELS_02_RESULTS.json")
    assert [c["id"] for c in out["cases"]] == [c["id"] for c in ledger["cases"]]
    for got, want in zip(out["cases"], ledger["cases"], strict=True):
        for method in ("generic", "pg", "oracle"):
            assert got[method]["decision"] == want[method], (got["id"], method)
        if "answers" in want:
            assert got["generic"]["answers"] == want["answers"]
    decisions = [c["oracle"]["decision"] for c in out["cases"]]
    assert decisions.count("safe") == ledger["counts"]["safe"]
    assert decisions.count("unsafe") == ledger["counts"]["unsafe"]
