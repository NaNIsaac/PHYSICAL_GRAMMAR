# Matched model fixtures 02 — 2026-09-10

This continuation replaces two abstract families from [pilot 01](MATCHED_BASELINE_01.md)
with derivative records from the existing M001 and M003 model witnesses. It is a
development experiment with six queries on two two-state domains, not six
independent physical cases or an unseen benchmark.

## Inputs and mathematical expectations

M001 uses the spring stiffness matrix `[[2,-1],[-1,2]]` in fixed reference units.
The two experiments exchange displacement-observation and force-drive bodies,
holding the other force fixed. Both cross-compliances are 1/3. Keeping only the
unordered body pair therefore determines this numerical response on the supplied
domain, but cannot determine which body was driven. Full ordered derivative
records distinguish the experiments.

M003 uses the existing normalized ideal-gas fixture, p=V=nR=T=1 and gamma=5/3.
Fixed-temperature and fixed-entropy derivatives give dV/dp=-1 and -3/5;
compressibilities are 1 and 3/5. Erasing the held-fixed conditions loses the
information needed for this query. Keeping them, including in reversed record
order, retains it. The reversal is an injective record transformation, not an
implemented theorem that arbitrary derivative constraints commute.

The source/model trail is inherited from [M4 batch 3](m4/BATCH_03_RESULTS.md)
and [M4 batch 4](m4/BATCH_04_RESULTS.md), with exact fixtures in their corresponding
check scripts. No new literature verification is claimed in this continuation.

## Equal information and attribution

The generic baseline has Property(name, ordered slots, unit) and
Derivative(body, differentiation variable, fixed conditions, unit) records.
Both paths receive the same property arities, units, fixed reference units,
model constants and derivative evaluation rules. A small shared validator checks
the declared signatures and derivative unit strings. It is not a dimensional
algebra, constraint solver, or full typed physical IR.

The adapter maps these records to existing PG properties and derivatives. Units
remain external shared declarations, not new PG fields. Full-record comparison
uses generic structural equality or PG genealogy respectively. Lossy record
operations and numerical evaluators are shared and operate on the original
fixture records. Consequently the lossy rows do not independently test a PG
projection implementation. Both methods use the same exhaustive finite-pair
algorithm; all sufficiency decisions belong to that supplied mathematics.

The expected outcome is agreement: two unsafe and four safe queries. Unlike pilot
01, this experiment uses exhaustive finite classification, so its completion rate
must not be interpreted as an improvement due to model encoding or PG. Analytic
matrix and thermodynamic tangent assertions check supplied numerical constants,
and a separate case ledger now reproduces every decision without Property/PG
objects. That ledger is an implementation cross-check over the same supplied
values, not an independent physical evaluator or reviewer.

## Reproduction and remaining gate

Run `python experiments/pgcheck/matched_models.py` (Python 3.10+). The program
prints per-case decisions, collision indices and exact rational answers, and
asserts representation agreement and model identities. Execution status is
recorded in STATUS.md; mathematical expectations here are not an execution log.

The compact machine-readable result ledger is
[MATCHED_MODELS_02_RESULTS.json](MATCHED_MODELS_02_RESULTS.json). The executable
script remains the authoritative reproduction path.

Encoding was authored once and translated automatically. Manual annotation time
was not instrumented; no human cost comparison can be reported. Independent
encodings, measured effort, a full typed/context comparator, and independent
input/oracle review remain open. These fixtures supply no evidence for a kernel
revision or a PG-specific advantage.
