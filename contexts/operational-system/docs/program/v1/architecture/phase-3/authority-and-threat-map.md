# Phase 3 Authority and Threat Map

## Authority map

Legend: `DECIDE` is a Taylor-only human decision; `EXECUTE` is bounded system
execution under an accepted contract; `PROPOSE` is non-authoritative analysis;
`OBSERVE` is read-only; `REVIEW` challenges fixed evidence; `DENIED` means the
role cannot perform the action.

| Decision or action | Taylor | Workbench agent | Control Plane | Worker | Observer | DEGS | Auditor |
|---|---|---|---|---|---|---|---|
| Define requirements or propose architecture | `DECIDE` | `PROPOSE` | Consulted | `DENIED` | `DENIED` | Evaluate record only | `REVIEW` |
| Accept RPO/RTO, exposure, retention, support, replacement, or residual risk | `DECIDE` | `DENIED` | `DENIED` | `DENIED` | `DENIED` | `DENIED` | Advise only |
| Authorize phase, device, physical, credential, permission, or destructive action | `DECIDE` / human execution | `DENIED` | `DENIED` | `DENIED` | `DENIED` | `DENIED` | `DENIED` |
| Create an approved Job Envelope | Policy owner | Assist within approved configuration | `EXECUTE` | Receive/validate | `OBSERVE` | `DENIED` | `REVIEW` fixed evidence |
| Execute bounded job | Supervise/stop | Assist within task | Dispatch/control | `EXECUTE` | `OBSERVE` | `DENIED` | `DENIED` |
| Validate Staged Output | Policy/exception owner | Assist | `EXECUTE` | `DENIED` | `OBSERVE` | Evaluate evidence form | `REVIEW` |
| Perform Promotion Event | Policy/exception owner | Assist only | `EXECUTE` within accepted configuration | `DENIED` | `DENIED` | `DENIED` | `DENIED` |
| Select or change Storage Role | `DECIDE` | `PROPOSE` | Execute accepted configuration only | `DENIED` | `OBSERVE` | Evaluate record only | `REVIEW` |
| Remediate automatically | `DENIED` by v1 | `DENIED` | `DENIED` unless a later exact tested contract says otherwise | `DENIED` | `DENIED` | `DENIED` | `DENIED` |
| Assign Role Disposition | Accept where human judgment applies | Architecture analysis within exact evidence | `DENIED` | `DENIED` | `DENIED` | Gate only | Required review where specified |
| Declare System Release | `DECIDE` | `DENIED` | `DENIED` | `DENIED` | `DENIED` | Prior deterministic result only | Prior independent review only |
| Authorize Public Release or broader adoption | Separate future scope only | `DENIED` | `DENIED` | `DENIED` | `DENIED` | `DENIED` | `DENIED` |

No `READY`, `ACTIVE`, `AUTHORIZED`, gate, lifecycle state, handoff, review, or
Role Disposition transfers an authority shown as `DENIED`.

## Trust boundaries

| Boundary | Trusted contract | Threat if crossed | Mandatory response |
|---|---|---|---|
| Taylor -> system roles | Exact human decision reference; no secret value retained | Authority spoofing or scope inference | Stop; obtain exact human instruction; preserve evidence |
| Control Plane -> Worker | Immutable Job Envelope and approved endpoint | Stale/tampered job, broad credential, unauthorized input | Reject before execution; no side effect |
| Worker -> Control Plane | Integrity-identified staged handback | Partial, duplicate, ambiguous, or self-promoted output | Quarantine staging; no Promotion Event |
| Control Plane -> Storage Resource | Qualified Storage Role and classified operation | Wrong device/volume, sole copy, content exposure, ambiguous write | Stop operation; preserve source; require exact target evidence |
| Roles -> Observer | Versioned minimum-necessary read-only signals | Content/secret capture, privilege creep, false health | Reject field/access; emit visibility failure |
| Operational System -> DEGS/auditor | Fixed minimum-necessary task or Evidence Set | Mutable evidence, source mismatch, reviewer mutation | Invalidate review; create a new generation |
| Operational System -> external source/network | Approved source, identity, and egress contract | Untrusted dependency, exposure, silent substitution | Reject source/result; remain on known-good state |

## Threat register

| Threat ID | Threat | Preventive control | Detection / stop trigger | Remaining evidence gap |
|---|---|---|---|---|
| `THR-P3-001` | Human authority inferred from a gate, status, or prior action | Explicit authority map and exact task boundary | Requested action lacks exact Taylor instruction | Whole-system denial tests are Phase 4/6 evidence |
| `THR-P3-002` | Worker gains authoritative state or promotion ability | Non-authoritative Worker contract; staged-only handback | Direct canonical path, promotion token, or sole-copy input requested | Worker software is not implemented |
| `THR-P3-003` | Secrets or restricted content enter Worker/Observer/evidence | Dual classifications, prohibited-field lists, minimum necessary inputs | `C3`, `CX`, raw/full serial, content, private filename, or broad credential detected | Security/privacy tests are future evidence |
| `THR-P3-004` | Storage presence is mistaken for backup or recovery fitness | Storage Role assignment requires topology, copy, integrity, capacity, restore, lifecycle evidence | Role claim lacks any required evidence | Seagate fitness and copy topology are `UNKNOWN` |
| `THR-P3-005` | Sole-copy important data is placed on Worker or Seagate | `R2`/`R3` no-sole-copy invariant | Copy relationship is `UNKNOWN` or source retirement is proposed | `EV-P2-COPY-MAP` was not produced |
| `THR-P3-006` | Ambiguous completion triggers duplicate work or promotion | Immutable Job Envelope and explicit ambiguity state | Conflicting status, missing acknowledgement, digest mismatch | Job protocol/failure tests are Phase 4/6 work |
| `THR-P3-007` | Missing or stale telemetry becomes false health | `UNKNOWN` / `TELEMETRY_UNAVAILABLE` fail-closed rule | Freshness, schema, clock, self-health, or completeness invalid | Observer is not implemented |
| `THR-P3-008` | Unsupported or exposed Worker handles private data | Support/exposure ceiling and network-role suspension | OS support or network exposure cannot be proven | Exact Worker device/support evidence is absent |
| `THR-P3-009` | Tested, reviewed, executed, and handed-off identities diverge | Sorted manifest and immutable generation rule | Any post-freeze byte change or identity mismatch | External G7/G8/G9 are pending |
| `THR-P3-010` | Destructive or physical work is hidden inside qualification | Separate action class and Tier 3 boundary | Erase, repartition, wipe, repair, permission, login, or physical step appears | No device action is selected by this package |
| `THR-P3-011` | Public Release or adoption is inferred from private readiness | Private Use boundary and explicit exclusion | External distribution, public service, collaborator, or cross-workspace mutation requested | Public Release remains out of scope |

## Threat disposition

All threats remain applicable. Phase 3 defines preventive controls and stop
responses but does not close implementation, device, integration, recovery, or
fault-test evidence. Any material architecture, data-class, authority, target,
or external-interface change requires a new threat review and package identity.

## DEAS evidence-record contract

- **Evidence ID:** `EV-P3-AUTHORITY`
- **Requirement/fault IDs:** `REQ-PGM-003`, `REQ-PGM-007`, `REQ-CP-003`, `REQ-ST-009`, `REQ-WK-009`, `REQ-OBS-001`, `REQ-OPS-004`, `REQ-ASS-007`, `REQ-ASS-008`, `FLT-NET-002`, `FLT-CP-003`
- **Claim under test:** The Phase 3 authority model keeps Taylor-only decisions nontransferable and identifies architecture threats, preventive controls, stop triggers, and unresolved evidence gaps.
- **Acceptance method:** Inspection and threat analysis against the accepted authority, privacy, exposure, source-of-truth, and release requirements; independent review remains external.
- **Exact source/configuration/role/device-safe identity/environment/target:** Frozen sources in `source-register.md`; the seven role columns and seven trust boundaries above; private DobeWorks documentation environment.
- **Procedure or command identity:** One bounded authority and threat analysis checked by `validation/validate_phase3.py`; no operational, security-setting, device, credential, or network action.
- **Start time:** 2026-09-05T19:24:10-05:00
- **End time:** 2026-09-05T20:34:39-05:00
- **Clock-quality basis:** Execution-host wall clock in America/Chicago with one-second display precision; no external time attestation.
- **Expected result:** Human-only decisions remain Taylor-only, system roles have least authority, trust-boundary failures stop safely, and every material threat retains truthful open evidence.
- **Actual result:** An eleven-action authority map, seven trust boundaries, and eleven architecture threats are defined; no role receives inferred authority and all implementation evidence gaps remain open.
- **Status:** DESIGN_DEFINED_NOT_IMPLEMENTED
- **Discrepancy references:** [Phase 2 discrepancies and unknowns](../../qualification/phase-2/discrepancies-and-unknowns.md) and [Role Dispositions](role-dispositions.md)
- **Artifact paths:** `contexts/operational-system/docs/program/v1/architecture/phase-3/authority-and-threat-map.md`
- **Cryptographic identities:** Frozen by `phase-3-sha256.txt`; its non-circular SHA-256 is supplied by the external freeze record.
- **Evidence owner:** Codex in Taylor AI Workbench for the recorded analysis; Taylor owns human authority decisions.
- **Human/physical action owner:** Taylor; no human-performed device, permission, credential, physical, destructive, or release action occurred.
- **Confidentiality classification:** `C1_PRIVATE_OPERATIONAL`; PRIVATE PERSONAL USE - NOT FOR PUBLIC RELEASE
- **Recoverability classification:** `R0_REPRODUCIBLE` from the frozen sources and package manifest.
- **Limitations:** Threat enumeration and design controls do not prove enforcement, resistance, detection, recovery, or security fitness.
- **Unsupported inferences:** Permission, authentication, device access, tested security, accepted residual risk, qualification, System Release, Public Release, or broader adoption.
- **Current freshness:** Current only for the frozen architecture and sources; any material role, interface, class, authority, or threat change requires reassessment.
- **Supersession:** First Phase 3 authority and threat map; supersedes no earlier Phase 3 artifact.
