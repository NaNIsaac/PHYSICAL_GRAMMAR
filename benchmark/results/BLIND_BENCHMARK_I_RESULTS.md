# Blind Benchmark I — Results

Status: complete, 60/60 cases. Grades are provisional until a dedicated audit of borderline G1/G2 cases.

## Grade definition
- **G0** — generic grammar + existing seed Properties/relations suffice.
- **G1** — established non-domain-specific mathematics is additionally required.
- **G2** — a domain semantic construction/seed must be supplied, after which generic grammar composes it.
- **G3** — the relevant relation depends on a physical law, constitutive model, regime assumption, or comparable model commitment.
- **G4** — frozen grammar cannot naturally express the scientific definition.

## Ledger
| ID | Quantity | Grade | Main semantic test |
|---|---|---:|---|
| B001 | moment of inertia | G2 | Body/Axis grounding; bound Site |
| B002 | impulse | G2 | time binding; Definition vs Law |
| B003 | action | G2 | trajectory/history functional |
| B004 | compliance | G2 | response/input roles |
| B005 | coefficient of restitution | G2 | before/after role-sensitive grounding |
| B006 | radius of gyration | G2 | construction genealogy |
| B007 | electric displacement | G2 | constitutive relation separation |
| B008 | polarization density | G2 | density construction |
| B009 | magnetic vector potential | G2 | gauge-related representation equivalence |
| B010 | electric susceptibility | G3 | constitutive/model dependence |
| B011 | mutual inductance | G2 | ordered two-entity grounding |
| B012 | characteristic impedance | G2 | matched-mode response ratio |
| B013 | chemical potential | G2 | held-fixed derivative conditions |
| B014 | fugacity | G3 | reference state + regime relation |
| B015 | activity coefficient | G3 | convention/reference state |
| B016 | isothermal compressibility | G2 | condition-sensitive derivative |
| B017 | thermal expansion coefficient | G2 | held-fixed condition |
| B018 | heat capacity at constant pressure | G2 | named condition ↔ constraint |
| B019 | dynamic viscosity | G2 | constitutive response coefficient |
| B020 | kinematic viscosity | G2 | matched grounding + construction |
| B021 | vorticity | G1 | differential operator preserves Site |
| B022 | circulation | G1 | integral binds Site, preserves Contour |
| B023 | strain-rate tensor | G1 | tensor differential construction |
| B024 | bulk modulus | G2 | response direction + condition |
| B025 | ionic strength | G2 | species binding under sum |
| B026 | molality | G2 | normalization genealogy |
| B027 | osmotic coefficient | G3 | convention/reference behavior |
| B028 | partial molar volume | G2 | focal variable + held-fixed conditions |
| B029 | reaction quotient | G2 | signed stoichiometric roles; Constraint separation |
| B030 | extent of reaction | G2 | stoichiometric normalization |
| B031 | radionuclide activity | G2 | Definition vs decay Law |
| B032 | absorbed dose | G2 | energy imparted to matter / mass |
| B033 | kerma | G2 | transfer genealogy vs absorbed dose |
| B034 | equivalent dose | G2 | conventional radiation weighting |
| B035 | stopping power | G2 | energy lost by particle / path |
| B036 | linear energy transfer | G2 | local transferred energy / path |
| B037 | acoustic impedance | G2 | matched-mode pressure/velocity response |
| B038 | group velocity | G1 | derivative of dispersion relation |
| B039 | phase velocity | G2 | ratio construction vs group velocity |
| B040 | quality factor | G2 | multiple equivalent representations |
| B041 | refractive index | G2 | reference propagation comparison |
| B042 | optical path length | G2 | path integration + MediumAt EntityMap |
| B043 | oscillator strength | G2 | transition relational grounding |
| B044 | linewidth | G2 | width convention vs broadening model |
| B045 | scattering cross section | G2 | interaction/process vs geometric area |
| B046 | differential cross section | G2 | angular distinction and integration loss |
| B047 | structure factor | G2 | coherent sum; phase loss under magnitude-square |
| B048 | spectral radiance | G2 | density coordinate representation + Jacobian |
| B049 | partition function | G2 | ensemble context + state binding |
| B050 | occupation number | G2 | mode/state grounding |
| B051 | density of states | G1 | measure-relative density |
| B052 | expectation value | G1 | generic expectation construction |
| B053 | purity | G2 | state representation + Tr(rho^2) |
| B054 | von Neumann entropy | G2 | same grounding, different constructor |
| B055 | measurement uncertainty | G2 | measurement-process grounding |
| B056 | standard uncertainty | G2 | metrological representation |
| B057 | sensitivity coefficient | G1 | derivative + evaluation point |
| B058 | calibration function | G2 | function/relation as Physical Expression |
| B059 | indication | G2 | instrument-output genealogy |
| B060 | measurand | G2 | contextual target role |

## Totals
G0=0, G1=7, G2=49, G3=4, G4=0.

## Interpretation guardrails
- G4=0 is not proof of completeness.
- The corpus is named-quantity heavy, so G0=0 is unsurprising.
- A grammar can avoid G4 by using overly permissive encodings; M4 therefore adds a naturalness/escape-hatch score.
- No new primitive is promoted from this table alone.
