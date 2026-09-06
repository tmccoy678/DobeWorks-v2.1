# Phase 3 Architecture and Role Disposition Plan

- Task: `DEGS-T1-DW-HWSW-P3-ARCH-DISPOSITION-20260905`
- Package state: `CANDIDATE_PENDING_VALIDATION`
- Decision scope: `PACKAGE`
- System state: `NOT_YET_QUALIFIED`, `NOT_YET_RELEASED`
- Authority lane: `TAYLOR_AI_WORKBENCH`
- DEGS risk tier: `TIER_1`
- DEAS profile: `Strict`
- Overlays: `Document`, `Evidence`, `Validator`, `Python`, `AI-Assisted`, `Git`
- Base commit: `bb5a0c6cc807939621c9c6efa4dae8f1e7fc1cc7`
- Base tree: `6571d0c1101b9034c3c3e07deb788f85f810af92`

## Objective and authority

Define and freeze the Phase 3 minimum bundle required by the accepted
[evidence and audit plan](../../evidence-and-audit-plan.md): role architecture;
data, authority, and threat maps; recovery, capacity, and lifecycle policies;
fault and Safe Degradation architecture; per-candidate Role Dispositions; and
an updated requirement trace.

Taylor's controlling instruction is:

> exact architecture/disposition package must be defined and frozen.

The immediately preceding instruction authorized Phase 3 and Role Disposition
while limiting the expansion to merge, release, qualification, Role
Disposition, Phase 3, and device action only. Broader adoption was explicitly
excluded. This work unit uses only the Phase 3 and Role Disposition authority.

## Frozen inputs

The exact sources and their SHA-256 identities are recorded in the
[source register](source-register.md). The consequential inputs are:

- the accepted Operational System glossary, requirements, decisions, fault
  matrix, evidence plan, and C4-corrected Phase 2 package;
- C4 commit `43df9f5a0d403851242f52f817e5195ed2764543` and reviewed tree
  `6571d0c1101b9034c3c3e07deb788f85f810af92`;
- Generation 2 manifest SHA-256
  `4dd1d41da658a22386af04d31ed97a9a149c731c19f44e8c58fe5d1c62d5c296`;
  and
- merge commit `bb5a0c6cc807939621c9c6efa4dae8f1e7fc1cc7`, whose tree is the reviewed
  C4 tree.

No evidence is recollected, and no observation is normalized or treated as
current merely because it was canonicalized or merged.

## Package outputs

| Output | Evidence identities | Responsibility |
|---|---|---|
| [Role architecture](role-architecture.md) | `EV-P3-ARCH`, `EV-P3-STORAGE-ARCH`, `EV-P3-WORKER-ARCH`, `EV-P3-OBSERVER-ARCH` | Define roles and interfaces without assigning unqualified hardware |
| [Data and signal map](data-and-signal-map.md) | `EV-P3-DATA-MAP`, `EV-P3-SIGNAL-DECISION-MAP` | Classify each permitted flow and map each proposed signal to a decision |
| [Authority and threat map](authority-and-threat-map.md) | `EV-P3-AUTHORITY` | Preserve Taylor-only decisions and enumerate architecture threats |
| [Recovery and capacity policy](recovery-and-capacity-policy.md) | `EV-P3-RECOVERY-DESIGN`, `EV-P3-CAPACITY-POLICY` | Apply accepted RPO/RTO values and retain unsupported capacity facts as `UNKNOWN` |
| [Operations lifecycle policy](operations-lifecycle-policy.md) | `EV-P3-MAINTENANCE`, `EV-P3-RETENTION-POLICY`, `EV-P3-ALERT-CONTRACT`, `EV-P3-LIFECYCLE`, `EV-P3-RETIREMENT` | Define accepted lifecycle controls and identify unresolved human values |
| [Fault and Safe Degradation](fault-and-safe-degradation.md) | `EV-P3-FMEA`, `EV-P3-SAFE-DEGRADATION` | Bind every applicable fault family to safe states without claiming a test |
| [Role Dispositions](role-dispositions.md) | `EV-P3-DISPOSITIONS` | Assign exactly one evidence-backed value to every candidate device/component |
| [Traceability matrix](../../traceability-matrix.md) | Updated `EV-P3-*` paths and states | Preserve bidirectional requirements-to-artifact trace |

## Disposition method

For each candidate, inspect only the frozen source evidence and apply exactly
one result:

- `QUALIFIED_FOR_BOUNDED_ROLE` only when every requirement necessary for the
  named role has sufficient objective evidence;
- `QUALIFIED_OUT` only when affirmative evidence establishes that the
  candidate cannot meet the bounded role under the accepted no-sunk-cost
  decision; or
- `BLOCKED_PENDING_EVIDENCE` when neither qualification nor disqualification
  is supportable because evidence is absent, stale, discrepant, untested, or
  not implemented.

No successful command, mount, component presence, design prose, or DEGS result
substitutes for device or integrated qualification evidence.

## Deterministic bounds

- Exact tracked mutation surface: the 18 paths in the task record.
- Evidence variants: one architecture/disposition candidate.
- Correction passes: at most two after the first full validation run.
- Public validation cases: eleven, each with a ten-second subprocess timeout.
- Input size: at most four MiB per validator input.
- Package manifest: exactly 17 sorted non-self entries.
- Candidate inventory: exactly five devices/components.
- Disposition values: exactly the three glossary-defined values; this package's
  evidence supports only `BLOCKED_PENDING_EVIDENCE`.

## Preconditions and postconditions

Preconditions are the exact merged base, verified private remote, clean tracked
state, no relevant writer, owned task lock, verified complete-history backup,
and Taylor's Phase 3 instruction. A failed precondition is a stop, not an
assumption.

Package postconditions are satisfied only when the public validator, its
positive and negative tests, canonical DEGS validation/evaluation, link and
JSON checks, manifest verification, diff checks, and secret scan pass on one
identity. The package remains pre-review and pre-delivery: G7, G8, and G9 stay
external.

## Explicit exclusions

This package performs no device, storage, permission, authentication,
credential, physical, destructive, installation, configuration, service,
Observer, Worker, recovery, restore, fault-injection, Phase 4, qualification,
System Release, Public Release, or broader-adoption action. It neither accepts
residual risk nor authorizes a later phase.

## Failure and safe-stop state

On drift, an extra path, unsupported fact, failed source identity, unresolved
validation error, exception need, or excluded action, preserve the branch,
bundle, task lock, candidate bytes, and findings. Do not amend, reset, rebase,
force-push, delete, merge, or relabel an unknown as resolved.
