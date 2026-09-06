# Phase 3 Fault and Safe Degradation Architecture

## Safe Degradation states

| State | Entry condition | Permitted work | Prohibited work | Exit evidence and authority |
|---|---|---|---|---|
| `SD-NO-DISPATCH` | Worker, input, network, configuration, support, or job state is unavailable/unsafe | Independent Control Plane work whose sources and recovery do not depend on Worker | New Worker dispatch; implicit retry | Exact fault reconciled; tested contract permits resume; Taylor decides disposition where required |
| `SD-NO-PROMOTION` | Output, evidence, source identity, or authoritative state is invalid/ambiguous | Preserve staging and evidence; read-only diagnosis within authority | Promotion Event or authoritative replacement | Identity/integrity/semantic checks pass and ambiguity is closed |
| `SD-STORAGE-UNAVAILABLE` | Storage Resource missing, read-only, corrupt, disconnected, low-reserve, or role-ambiguous | Work independent of the affected Storage Role | Affected read/write/backup/restore claim; automatic deletion/remount/retry | Resource and role re-identified; operation state reconciled; required integrity/capacity/recovery evidence passes |
| `SD-TELEMETRY-UNAVAILABLE` | Observer data missing, stale, dropped, schema-incompatible, clock-uncertain, or collector/alert route failed | Work not dependent on the missing signal; direct stop at originating control | Telemetry-dependent health, dispatch, promotion, or release claim | Fresh schema-valid signals and self-health restored; blind interval dispositioned |
| `SD-OFFLINE-ONLY` | Approved network path unavailable or exposure/support boundary is not met | Explicitly defined local work with no network/data exposure dependency | Networked Worker role, substitute endpoint, broad credential, public listener | Approved path/support/exposure evidence and security retest; Taylor for compensating design |
| `SD-RECOVERY-HOLD` | Authoritative source, protected copy, restore/rebuild, or post-update state is unknown/failed | Preserve known-good source and evidence | Risk-bearing mutation, source retirement, cleanup, qualification, or release | Recovery source and procedure pass complete acceptance; Taylor closes critical ambiguity |
| `SD-RETIREMENT-HOLD` | Retirement inventory, copies, evidence, disengagement, or sanitization route is incomplete | Continued controlled service if safe, or powered-off retention under Taylor direction | Sanitization, wipe, deletion, or disposal | Non-destructive rehearsal passes; separate Tier 3 cutover handles any destructive step |

Safe Degradation is explicit loss of capability, never a weaker acceptance
standard. Multiple states may apply simultaneously; the union of their
prohibitions controls.

## Fault applicability map

All 37 Phase 1 fault rows remain applicable. No role or fault is removed by
this architecture, and no planned test is relabeled as passing evidence.

| Fault family | Exact fault IDs | Primary state(s) | Detection / containment architecture | Required later recovery evidence |
|---|---|---|---|---|
| Storage | `FLT-ST-001` through `FLT-ST-007` | `SD-STORAGE-UNAVAILABLE`, `SD-RECOVERY-HOLD` | Presence/state, I/O, integrity, capacity, generation, and restore checks; stop affected operations and preserve source/evidence | Storage fault tests, capacity test, protected-generation evidence, representative restore |
| Worker | `FLT-WK-001` through `FLT-WK-005` | `SD-NO-DISPATCH`, `SD-OFFLINE-ONLY`, `SD-RECOVERY-HOLD` | Freshness, support/configuration, resource/thermal/power, job reconciliation, and rebuild checks | Representative workload, support evidence, clean rebuild, integrated qualification |
| Job | `FLT-JOB-001` through `FLT-JOB-008` | `SD-NO-DISPATCH`, `SD-NO-PROMOTION` | Immutable IDs/digests, expiry, completeness, atomic handback, cancellation/timeout/ambiguity states | Positive, negative, timeout, interruption, duplicate, cancellation, and handback tests |
| Observer | `FLT-OBS-001` through `FLT-OBS-006` | `SD-TELEMETRY-UNAVAILABLE` | Freshness, heartbeat, clock, schema, dropped-record, and alert-route self-health | Observer failure tests, retention tests, alert demonstration, telemetry fault evidence |
| Control Plane | `FLT-CP-001` through `FLT-CP-004` | `SD-NO-DISPATCH`, `SD-NO-PROMOTION`, `SD-RECOVERY-HOLD` | Boot/session generation, open-work reconciliation, source/manifest integrity, recovery result | Restart/reconciliation tests, known-state recovery, loss/replacement exercise |
| Network | `FLT-NET-001`, `FLT-NET-002` | `SD-OFFLINE-ONLY`, `SD-NO-DISPATCH` | Approved-endpoint connection and exposure/listener checks | Network failure and security/exposure tests |
| Supply source | `FLT-SUP-001`, `FLT-SUP-002` | `SD-OFFLINE-ONLY`, `SD-RECOVERY-HOLD` | Approved-source availability, integrity, provenance, and compatibility checks | Supply failure, mismatch, and rollback tests |
| Update | `FLT-UPD-001` | `SD-RECOVERY-HOLD` | Installer/result plus post-update acceptance; isolate failed generation | Update and rollback demonstration with known-good verification |
| Power | `FLT-PWR-001` | `SD-NO-PROMOTION`, `SD-STORAGE-UNAVAILABLE`, `SD-RECOVERY-HOLD` | Recovered operation/generation ambiguity and source/target integrity checks | Power-loss fault test at safe boundary; critical ambiguity closure |
| Retirement | `FLT-RET-001` | `SD-RETIREMENT-HOLD` | Non-destructive inventory/copy/evidence/disengagement checklist | Retirement rehearsal; any sanitization remains separate Tier 3 |

## Transition and resume rules

1. Detection records the exact affected role, fault, observation time, clock
   quality, evidence freshness, and configuration generation.
2. The system enters every applicable Safe Degradation state before further
   affected work.
3. Containment preserves authoritative sources, staged results, and sanitized
   evidence while performing no unauthorized repair or retry.
4. Recovery follows only a role-specific tested procedure with exact source and
   target identities.
5. Acceptance repeats the complete requirement-specific test, not only the
   failed step.
6. Resume authority follows the canonical fault matrix. Taylor decides any
   physical, destructive, credential, critical ambiguity, role, exception, or
   residual-risk question.

No fault state permits Worker self-promotion, Observer remediation, automatic
device repair, silent endpoint substitution, or a release claim.

## DEAS evidence-record contract

- **Evidence ID:** `EV-P3-FMEA`, `EV-P3-SAFE-DEGRADATION`
- **Requirement/fault IDs:** `REQ-OPS-003`, `REQ-OPS-004`, all `FLT-ST-001` through `FLT-ST-007`, `FLT-WK-001` through `FLT-WK-005`, `FLT-JOB-001` through `FLT-JOB-008`, `FLT-OBS-001` through `FLT-OBS-006`, `FLT-CP-001` through `FLT-CP-004`, `FLT-NET-001`, `FLT-NET-002`, `FLT-SUP-001`, `FLT-SUP-002`, `FLT-UPD-001`, `FLT-PWR-001`, and `FLT-RET-001`
- **Claim under test:** Every applicable fault family maps to explicit detection/containment architecture, one or more fail-safe states, required recovery evidence, and bounded resume authority without claiming a test passed.
- **Acceptance method:** Inspection and analysis against all 37 rows in the canonical fault-test matrix and the accepted authority and Safe Degradation requirements; Phase 6 tests and independent review remain future.
- **Exact source/configuration/role/device-safe identity/environment/target:** Frozen fault matrix and requirements in `source-register.md`; seven Safe Degradation states; all five candidate devices/components; documentation environment only.
- **Procedure or command identity:** One bounded fault-family coverage analysis checked by `validation/validate_phase3.py`; no fault injection, device action, process interruption, network change, restore, update, or retirement action.
- **Start time:** 2026-09-05T19:24:10-05:00
- **End time:** 2026-09-05T20:34:39-05:00
- **Clock-quality basis:** Execution-host wall clock in America/Chicago with one-second display precision; no external time attestation.
- **Expected result:** All 37 faults remain applicable, each family enters explicit Safe Degradation, recovery requires later objective evidence, and resume authority never expands silently.
- **Actual result:** Seven Safe Degradation states, ten complete fault-family mappings, and six transition/resume rules are defined; no fault was removed and no test result is claimed.
- **Status:** DESIGN_DEFINED_NOT_TESTED
- **Discrepancy references:** [Phase 2 discrepancies and unknowns](../../qualification/phase-2/discrepancies-and-unknowns.md) and [canonical fault-test matrix](../../fault-test-matrix.md)
- **Artifact paths:** `contexts/operational-system/docs/program/v1/architecture/phase-3/fault-and-safe-degradation.md`
- **Cryptographic identities:** Frozen by `phase-3-sha256.txt`; its non-circular SHA-256 is supplied by the external freeze record.
- **Evidence owner:** Codex in Taylor AI Workbench for architecture coverage; future assurance and role owners retain test responsibilities.
- **Human/physical action owner:** Taylor for physical, power, device, destructive, credential, critical ambiguity, exception, residual-risk, and final resume decisions; none occurred.
- **Confidentiality classification:** `C1_PRIVATE_OPERATIONAL`; PRIVATE PERSONAL USE - NOT FOR PUBLIC RELEASE
- **Recoverability classification:** `R0_REPRODUCIBLE` from the frozen sources and package manifest.
- **Limitations:** Grouped architecture coverage is not static, simulated, hardware, integration, recovery, workload, or end-to-end fault evidence.
- **Unsupported inferences:** Fault tolerance, availability, recoverability, safe device operation, tested Safe Degradation, qualification, or System Release.
- **Current freshness:** Current only for the 37 fault rows and architecture sources frozen in `source-register.md`; a new role, fault, or interface makes this analysis stale.
- **Supersession:** First Phase 3 fault and Safe Degradation architecture; supersedes no earlier Phase 3 artifact.
