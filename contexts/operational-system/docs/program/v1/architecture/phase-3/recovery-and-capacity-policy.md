# Phase 3 Recovery and Capacity Policy

## Accepted service classes

These values reproduce Taylor's accepted `DEC-001`; they are policy targets,
not evidence that any device or integrated recovery path meets them.

| Service class | Scope | RPO | RTO | Acceptance boundary |
|---|---|---:|---:|---|
| `S0_ACCEPTED_STATE` | Accepted requirements, configuration, manifests, evidence index, and promoted authoritative artifacts | `0` after Promotion Event | 24 hours | State is accepted only after an independently recoverable copy is evidenced |
| `S1_ACTIVE_WORK` | Active private engineering work not yet promoted | 24 hours | 24 hours | Bounded personal-work loss; no continuous-replication inference |
| `S2_IRREPLACEABLE` | In-scope `R3_IRREPLACEABLE` data | `0` after controlled intake | 72 hours | Source retirement prohibited until two independent protected copies and representative restore are proven |
| `S3_REBUILDABLE` | Worker tooling, clones, caches, temporary artifacts, reproducible telemetry views | Not applicable; source must remain available | 72 hours | Recovery is rebuild from approved source, not backup of disposable state |

`RPO 0` is a commit/acceptance rule, not a continuous-availability claim.

## Recovery architecture

| Recovery object | Authoritative source | Required protected relationship | Acceptance evidence | Current state |
|---|---|---|---|---|
| Control Plane accepted state | Exact approved configuration and authoritative repository/state generation | Independent recoverable copy before acceptance | Known-state restore/rebuild, integrity and semantic verification, RTO demonstration | `BLOCKED_PENDING_EVIDENCE` |
| Active work | Current authoritative work location | Copy cadence meeting 24-hour RPO | Generation evidence and representative restore | Copy topology `UNKNOWN` |
| Irreplaceable intake | Exact controlled source | Two independently protected copies before source retirement | Two-copy identity plus representative restore and 72-hour RTO evidence | In-scope inventory and topology `UNKNOWN` |
| Worker software/tooling | Approved source/configuration manifest | Rebuild source remains available; no unique local state | Clean rebuild and representative workload within 72 hours | Not implemented; `BLOCKED_PENDING_EVIDENCE` |
| Observer implementation/views | Approved source/schema; views are reproducible | Rebuild source and retained release evidence where applicable | Clean rebuild, self-health, retention, and alert verification | Not implemented; `BLOCKED_PENDING_EVIDENCE` |
| Storage Role generation | Exact protected source and role contract | Relationship depends on backup/archive/transfer/scratch role | Identity, integrity, capacity, retention, and restore evidence | No role assigned to Seagate |

## Recovery procedure contract

Every later recovery procedure must bind the source and target identities,
configuration generation, service class, RPO/RTO, privacy boundary, pre-state,
allowed mutations, rollback/safe stop, expected byte and semantic results,
evidence owner, and resume authority. A representative restore goes to a
controlled destination and verifies bytes where meaningful plus application or
semantic usability where byte equality is insufficient.

Failure, mismatch, inaccessible evidence, or an ambiguous source leaves the
claim `UNKNOWN`, preserves the source and failed result, and prevents promotion,
source retirement, deletion, or a clean completion claim.

## Capacity policy

| Capacity value | Current value | Policy consequence |
|---|---|---|
| Control Plane reconciled usable capacity | `UNKNOWN` because Phase 2 methods disagreed | No capacity-dependent Role Disposition or recovery claim |
| Seagate current usable capacity | Historical point value only; present value `UNKNOWN` | No current reserve or growth claim |
| Minimum absolute reserve | `UNKNOWN`; Taylor has not accepted a value | No Storage Role assignment or clean capacity result |
| Minimum percentage reserve | `UNKNOWN`; Taylor has not accepted a value | No threshold-based health or alert claim |
| Forecast horizon and growth rate | `UNKNOWN` | No retention-sufficiency claim |
| Backup/archive generation count | `UNKNOWN` until an exact Storage Role and source are selected | No generation-deletion, retention, or overwrite decision |

No customary percentage, vendor capacity, mount result, historical free-space
value, or successful write may fill these gaps. Phase 6 must prove the selected
policy under representative retention and growth without silently dropping a
required recovery point.

## Copy and storage invariants

- The Seagate is a Storage Resource candidate, not an accepted backup.
- No `R2_IMPORTANT` or `R3_IRREPLACEABLE` information may exist only on the
  Seagate or Worker.
- Backup evidence identifies exact protected source, independent-copy
  relationship, generation, protections, and service-class coverage.
- Missing, read-only, corrupt, disconnected, low-reserve, or unavailable
  storage enters Safe Degradation; it never triggers automatic deletion or
  silent role substitution.
- Actual deletion, consolidation, repartitioning, reformatting, sanitization,
  erasure, or wipe remains a separate Tier 3 cutover.

## DEAS evidence-record contract

- **Evidence ID:** `EV-P3-RECOVERY-DESIGN`, `EV-P3-CAPACITY-POLICY`
- **Requirement/fault IDs:** `REQ-CP-006`, `REQ-ST-003`, `REQ-ST-004`, `REQ-ST-005`, `REQ-ST-006`, `REQ-ST-008`, `REQ-WK-010`, `REQ-OPS-002`, `FLT-ST-003`, `FLT-ST-005`, `FLT-ST-006`, `FLT-ST-007`, `FLT-CP-002`, `FLT-CP-004`, `FLT-WK-005`
- **Claim under test:** The Phase 3 recovery design applies Taylor's accepted service classes, prevents sole-copy and unsupported restore claims, and preserves every unaccepted capacity value as `UNKNOWN`.
- **Acceptance method:** Inspection and analysis against `DEC-001`, the storage/recovery requirements, Phase 2 observations, and the fault matrix; later tests, demonstrations, and review remain required.
- **Exact source/configuration/role/device-safe identity/environment/target:** Frozen sources in `source-register.md`; service classes `S0`-`S3`; candidates `CP-CANDIDATE-01`, `SR-CANDIDATE-01`, `WK-CANDIDATE-01`, `WK-SW-CANDIDATE-01`, and `OBS-CANDIDATE-01`; documentation environment only.
- **Procedure or command identity:** One bounded recovery/capacity policy derivation checked by `validation/validate_phase3.py`; no backup, restore, write, benchmark, diagnostic, deletion, or device command.
- **Start time:** 2026-09-05T19:24:10-05:00
- **End time:** 2026-09-05T20:34:39-05:00
- **Clock-quality basis:** Execution-host wall clock in America/Chicago with one-second display precision; no external time attestation.
- **Expected result:** Accepted RPO/RTO values are reproduced exactly, recovery claims require representative evidence, sole-copy important data is prohibited, and unsupported capacity thresholds remain `UNKNOWN`.
- **Actual result:** Four accepted service classes, six recovery-object contracts, a fail-closed recovery procedure contract, and six explicit capacity gaps are defined; no recovery or capacity fitness is claimed.
- **Status:** DESIGN_DEFINED_NOT_IMPLEMENTED
- **Discrepancy references:** [Phase 2 discrepancies and unknowns](../../qualification/phase-2/discrepancies-and-unknowns.md), including the current-Mac free-space disagreement and unresolved Seagate fitness.
- **Artifact paths:** `contexts/operational-system/docs/program/v1/architecture/phase-3/recovery-and-capacity-policy.md`
- **Cryptographic identities:** Frozen by `phase-3-sha256.txt`; its non-circular SHA-256 is supplied by the external freeze record.
- **Evidence owner:** Codex in Taylor AI Workbench for the recorded analysis; future recovery and storage owners remain assigned by the requirements.
- **Human/physical action owner:** Taylor for any physical, device, permission, destructive, source-retirement, or loss-budget decision; none occurred.
- **Confidentiality classification:** `C1_PRIVATE_OPERATIONAL`; PRIVATE PERSONAL USE - NOT FOR PUBLIC RELEASE
- **Recoverability classification:** `R0_REPRODUCIBLE` from the frozen sources and package manifest.
- **Limitations:** No copy topology, backup generation, restore, rebuild, capacity threshold, forecast, or RPO/RTO performance was observed or tested.
- **Unsupported inferences:** Backup coverage, device fitness, available capacity, recoverability, source retirement safety, qualification, System Release, or destructive authority.
- **Current freshness:** Policy values are current for `DEC-001`; device and capacity facts remain historical or `UNKNOWN` and require new evidence.
- **Supersession:** First Phase 3 recovery and capacity policy; supersedes no earlier Phase 3 artifact.
