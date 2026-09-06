# Phase 3 Role Architecture

## Architecture rule

Operational roles are contracts, not device names. A candidate device or
component may implement a role only after its Role Disposition is
`QUALIFIED_FOR_BOUNDED_ROLE` for that exact contract. Every candidate in this
generation remains `BLOCKED_PENDING_EVIDENCE`; the mappings below therefore
define intended interfaces, not active assignments.

## Role topology

| Role / candidate | Source of truth and responsibility | Permitted interface | Prohibited authority | Current architecture state |
|---|---|---|---|---|
| Taylor | Human value, phase, credential, physical, destructive, exception, residual-risk, and System Release decisions | Explicit bounded instructions and human-executed steps | No decision inferred from status, gate, or convenience | `OWNER` |
| Control Plane / `CP-CANDIDATE-01` | Approved configuration, authoritative operational state, dispatch records, evidence indexes, Promotion Events, recovery orchestration | Job Envelope out; status, evidence, and Staged Output in; classified storage operations | No autonomous human-only decision; no automatic residual-risk acceptance | `BLOCKED_PENDING_EVIDENCE` |
| Storage Resource / `SR-CANDIDATE-01` | Device/volume substrate only after a qualified Storage Role is assigned | Operations allowed by one explicit Storage Role contract | Connection, mount, or diagnostics cannot create a backup/fitness claim | `BLOCKED_PENDING_EVIDENCE`; no Storage Role assigned |
| Worker device / `WK-CANDIDATE-01` | Replaceable execution substrate | Receive one valid Job Envelope; return status, evidence, and Staged Output | No sole-copy important data, authoritative state, broad credential, or promotion | `BLOCKED_PENDING_EVIDENCE` |
| Worker software / `WK-SW-CANDIDATE-01` | Validate envelopes; execute only defined job classes; stage output atomically | Bounded Control Plane protocol | No self-dispatch, source-of-truth mutation, or success-to-acceptance conversion | `BLOCKED_PENDING_EVIDENCE`; not implemented |
| Observer / `OBS-CANDIDATE-01` | Local minimum-necessary operational metadata and collector self-health | Read-only versioned signals to Taylor/Control Plane presentation | No content, private names, secrets, remediation, dispatch, promotion, or approval | `BLOCKED_PENDING_EVIDENCE`; not implemented |
| DEGS | External deterministic evaluator of the exact task record | Structured task/evidence input; structured gate result | No execution, truth, phase, role, risk, merge, or release authority | External interface |
| Independent auditor | Challenge a Frozen Evidence Set | Read-only review route | No package mutation or Taylor-only decision | Future external role |

## Storage Role candidates

No row is assigned to `SR-CANDIDATE-01`. A later exact Storage Role decision
must select one or more rows only after topology, copy relationship, capacity,
integrity, representative restore, lifecycle, and privacy evidence passes.

| Storage Role candidate | Purpose | Authoritative source | Allowed classes and operations | Retention / capacity | Recovery objective and retirement |
|---|---|---|---|---|---|
| `ST-BACKUP-CANDIDATE` | Hold protected recovery generations | Exact protected source is `UNKNOWN` until classified | Controlled backup and restore only; no agent content traversal; never sole-copy `R2`/`R3` | Generation retention and reserve threshold are `UNKNOWN`; assignment blocked | Source-class RPO/RTO from DEC-001; representative restore required; retire only after independent-copy confirmation |
| `ST-ARCHIVE-CANDIDATE` | Preserve an explicitly closed, classified corpus | Exact canonical source and closure event are `UNKNOWN` | Approved `C0`-`C2`; `C3` requires a separate Taylor-controlled content boundary; no `CX` | Retention, growth, and reserve are `UNKNOWN`; assignment blocked | Recovery objective follows recoverability class; migration required before support sunset |
| `ST-TRANSFER-CANDIDATE` | Temporary handoff between approved endpoints | Sending endpoint remains authoritative until receipt verifies | `C0`-`C2`, `R0`/`R1`; `R2` only as a non-sole copy; no `R3` or `CX` | Retain only through verified receipt; exact maximum duration is `UNKNOWN` | Retry from authoritative source; clear/disengage only under a separate bounded lifecycle action |
| `ST-SCRATCH-CANDIDATE` | Replaceable temporary workspace | Approved source remains elsewhere | `C0`/`C1` and specifically approved replaceable `C2`; `R0`/`R1` only | Task-bounded; reserve threshold is `UNKNOWN`; assignment blocked | Rebuild, not restore; no sanitization or deletion is authorized here |

## Control and data invariants

1. The Control Plane is the only system role that may create a Job Envelope or
   perform a Promotion Event, and only within Taylor-accepted policy.
2. A Worker can return Staged Output but cannot make it authoritative.
3. An Observer reports validated metadata or `UNKNOWN` /
   `TELEMETRY_UNAVAILABLE`; it never remediates.
4. A Storage Resource receives no semantic role from its name, connection,
   mount, capacity, diagnostic, or historical use.
5. `R2_IMPORTANT` and `R3_IRREPLACEABLE` information never exists only on a
   Worker or the Seagate.
6. `RX_UNKNOWN` blocks new placement, deletion, migration, promotion, and a
   clean completion claim.
7. No system component inherits Taylor-only credential, physical, destructive,
   exception, residual-risk, phase, or release authority.

## State transitions

`CANDIDATE -> BLOCKED_PENDING_EVIDENCE` records an incomplete decision without
activating a role. A later transition to either
`QUALIFIED_FOR_BOUNDED_ROLE` or `QUALIFIED_OUT` requires a new evidence
generation, requirement-specific acceptance methods, independent review where
required, and Taylor's applicable decision. No Role Disposition automatically
authorizes integration or a later phase.

## DEAS evidence-record contract

- **Evidence ID:** `EV-P3-ARCH`, `EV-P3-STORAGE-ARCH`, `EV-P3-WORKER-ARCH`, `EV-P3-OBSERVER-ARCH`
- **Requirement/fault IDs:** `REQ-CP-002`, `REQ-ST-002`, `REQ-WK-002`, `REQ-OBS-001`, `REQ-PGM-003`, `REQ-PGM-007`
- **Claim under test:** The Phase 3 package defines bounded role responsibilities, interfaces, storage-role candidates, and authority exclusions without treating any candidate as active or qualified.
- **Acceptance method:** Inspection and analysis against the accepted glossary, program definition, requirements, decisions, and Phase 2 evidence boundaries; later independent review remains external.
- **Exact source/configuration/role/device-safe identity/environment/target:** Source identities in `source-register.md`; roles and candidates `CP-CANDIDATE-01`, `SR-CANDIDATE-01`, `WK-CANDIDATE-01`, `WK-SW-CANDIDATE-01`, and `OBS-CANDIDATE-01`; private DobeWorks repository Phase 3 documentation environment.
- **Procedure or command identity:** One bounded architecture derivation under `architecture-plan.md`, checked by `validation/validate_phase3.py`; no device command or operational execution.
- **Start time:** 2026-09-05T19:24:10-05:00
- **End time:** 2026-09-05T20:34:39-05:00
- **Clock-quality basis:** Execution-host wall clock in America/Chicago with one-second display precision; no external time attestation.
- **Expected result:** Roles are contract-first, every interface preserves source-of-truth and Taylor-only boundaries, and no candidate is represented as active or qualified.
- **Actual result:** The role topology, four unassigned Storage Role candidates, invariants, and disposition transition rules are defined; every candidate remains blocked and no implementation occurred.
- **Status:** DESIGN_DEFINED_NOT_IMPLEMENTED
- **Discrepancy references:** [Phase 2 discrepancies and unknowns](../../qualification/phase-2/discrepancies-and-unknowns.md) and [Phase 3 Role Dispositions](role-dispositions.md)
- **Artifact paths:** `contexts/operational-system/docs/program/v1/architecture/phase-3/role-architecture.md`
- **Cryptographic identities:** Frozen by `phase-3-sha256.txt`; its non-circular SHA-256 is supplied by the external freeze record.
- **Evidence owner:** Codex in Taylor AI Workbench for package integrity; Taylor retains human-only decisions.
- **Human/physical action owner:** Taylor; no physical or device action was required or performed.
- **Confidentiality classification:** `C1_PRIVATE_OPERATIONAL`; PRIVATE PERSONAL USE - NOT FOR PUBLIC RELEASE
- **Recoverability classification:** `R0_REPRODUCIBLE` from the frozen sources and package manifest.
- **Limitations:** This is architecture analysis, not implementation, device fitness, integration, recovery, fault, workload, or end-to-end evidence.
- **Unsupported inferences:** Active role assignment, device suitability, implementation completeness, qualification, Phase 4 authority, System Release, Public Release, or broader adoption.
- **Current freshness:** Current only for the source identities in `source-register.md`; any source, requirement, candidate, or authority change makes this record stale.
- **Supersession:** First Phase 3 architecture generation; supersedes no earlier Phase 3 artifact.
