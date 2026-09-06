# Phase 3 Role Dispositions

- Package review state: `PENDING`
- System state: `NOT_YET_QUALIFIED`, `NOT_YET_RELEASED`
- Disposition method: frozen-source inspection and analysis under
  [the Phase 3 plan](architecture-plan.md)

## Decision rule

`BLOCKED_PENDING_EVIDENCE` is an evidence-backed Role Disposition, not an
observation-status synonym. It is used here only after considering both other
allowed results and finding that the frozen evidence supports neither
qualification nor disqualification. It activates no role and authorizes no
device, integration, remediation, Phase 4, qualification, or release action.

## Exact candidate inventory and dispositions

<!-- PHASE3-DISPOSITIONS:START -->
| Candidate | Intended bounded role | Frozen evidence basis | Role Disposition | Evidence required before reconsideration |
|---|---|---|---|---|
| `CP-CANDIDATE-01` | Control Plane | Current Mac metadata was observed, but free-space methods conflict; present capacity, read-only flags, authoritative-copy topology, recovery/rebuild, fault, update/rollback, and integrated fitness remain unproven | `BLOCKED_PENDING_EVIDENCE` | Fresh privacy-safe identity/capacity reconciliation; authoritative-state/copy map; known-state recovery; security, fault, maintenance, and integration evidence |
| `SR-CANDIDATE-01` | One or more explicit Storage Roles | Sanitized topology and historical capacity fragment exist; read-only flags, present topology, backup membership, health, redundancy, integrity, permissions, representative restore, lifecycle, and content-safe role fit remain `UNKNOWN` | `BLOCKED_PENDING_EVIDENCE` | Exact current topology/role target; diagnostics and integrity; copy relationship; capacity/retention; representative restore; lifecycle and privacy evidence |
| `WK-CANDIDATE-01` | Rebuildable Worker device | No physical or remote evidence step occurred; exact device, OS/support, storage, battery, power, thermal, network, recovery, and workload facts remain `UNKNOWN` | `BLOCKED_PENDING_EVIDENCE` | Separately defined Taylor-performed or authorized safe evidence step covering `REQ-WK-001`, followed by support, recovery, workload, exposure, and integration evidence |
| `WK-SW-CANDIDATE-01` | Worker software | Required Job Envelope, retry/cancellation, staging, promotion-denial, privacy, security, and rebuild behavior is specified only; no implementation or tests exist | `BLOCKED_PENDING_EVIDENCE` | Phase 4 source/configuration, protocol implementation, static/positive/negative/security/failure tests, provenance, and later hardware/integration evidence |
| `OBS-CANDIDATE-01` | Local read-only Observer | Four executable-presence fragments exist historically; no schema, collector, schedule, privacy enforcement, retention, self-health, alerting, failure behavior, or implementation exists | `BLOCKED_PENDING_EVIDENCE` | Phase 4 schema/collector and privacy/self-health/failure tests, followed by retention, alert, integration, and Phase 6 fault evidence |
<!-- PHASE3-DISPOSITIONS:END -->

These are the complete candidate devices/components in the accepted Phase 1
boundary. Taylor is the owner, not a candidate. DEGS and the independent
auditor are external assurance interfaces, not Operational System components.
The four possible Storage Roles are unassigned contracts rather than separate
implemented candidates; `SR-CANDIDATE-01` therefore remains the exact resource
candidate requiring later role-specific evidence.

## Rejected alternative results

| Candidate set | Why `QUALIFIED_FOR_BOUNDED_ROLE` is unsupported | Why `QUALIFIED_OUT` is unsupported |
|---|---|---|
| Current Mac | Required recovery, authoritative-copy, capacity reconciliation, fault, and integration evidence is absent | No evidence shows the candidate cannot meet the Control Plane contract after one bounded evidence/remediation cycle |
| Seagate | Required topology, redundancy, diagnostics, integrity, capacity, restore, lifecycle, and role-specific evidence is absent | No affirmative diagnostic/fitness evidence establishes failure of every bounded Storage Role candidate |
| 2015 MacBook | Exact device and representative evidence is absent | Age or prior ownership is not a no-sunk-cost fitness test; support/condition/workload facts are unknown |
| Worker software | No implementation or acceptance evidence exists | Nothing was implemented and then proven incapable under the defined contract |
| Observer | Executable presence is not an implementation or acceptance test | No implemented bounded Observer has been shown incapable of meeting the contract |

## Review and transition boundary

The dispositions are the Phase 3 candidate results frozen for independent
review. `REQ-PGM-006` requires inspection, analysis, and review; therefore the
package does not label them accepted while G8 is pending. A later disposition
change requires a new generation tied to new objective evidence and complete
revalidation. No disposition automatically authorizes Phase 4 or any device
action.

## DEAS evidence-record contract

- **Evidence ID:** `EV-P3-DISPOSITIONS`
- **Requirement/fault IDs:** `REQ-PGM-005`, `REQ-PGM-006`, `REQ-PGM-007`, `REQ-CP-001`, `REQ-ST-001`, `REQ-ST-007`, `REQ-ST-010`, `REQ-WK-001`, `REQ-WK-011`, `REQ-WK-012`, `REQ-OBS-005`, `REQ-ASS-007`
- **Claim under test:** Every in-scope candidate device/component receives exactly one evidence-backed Role Disposition without converting absence, age, presence, prose, or a gate result into fitness or failure.
- **Acceptance method:** Inspection and analysis of the exact C4 Phase 2 records, requirements, decisions, architecture contracts, and discrepancies; independent review is required and remains pending externally.
- **Exact source/configuration/role/device-safe identity/environment/target:** Frozen sources in `source-register.md`; candidates `CP-CANDIDATE-01`, `SR-CANDIDATE-01`, `WK-CANDIDATE-01`, `WK-SW-CANDIDATE-01`, and `OBS-CANDIDATE-01`; private documentation environment only.
- **Procedure or command identity:** The three-result decision rule in `architecture-plan.md`, exact five-row table above, and deterministic checks in `validation/validate_phase3.py`; no device command or evidence recollection.
- **Start time:** 2026-09-05T19:24:10-05:00
- **End time:** 2026-09-05T20:34:39-05:00
- **Clock-quality basis:** Execution-host wall clock in America/Chicago with one-second display precision; no external time attestation.
- **Expected result:** Exactly five unique candidate rows, each with one allowed value supported by frozen evidence; no role activation, qualification, disqualification, or device action is inferred.
- **Actual result:** All five candidates receive `BLOCKED_PENDING_EVIDENCE`; neither `QUALIFIED_FOR_BOUNDED_ROLE` nor `QUALIFIED_OUT` is supported for any candidate on the frozen inputs.
- **Status:** CANDIDATE_DISPOSITIONS_PRODUCED_REVIEW_PENDING
- **Discrepancy references:** [Phase 2 discrepancies and unknowns](../../qualification/phase-2/discrepancies-and-unknowns.md), [recovery/capacity gaps](recovery-and-capacity-policy.md), and [lifecycle gaps](operations-lifecycle-policy.md)
- **Artifact paths:** `contexts/operational-system/docs/program/v1/architecture/phase-3/role-dispositions.md`
- **Cryptographic identities:** Frozen by `phase-3-sha256.txt`; its non-circular SHA-256 is supplied by the external freeze record.
- **Evidence owner:** Codex in Taylor AI Workbench for analysis and record integrity; independent reviewer and Taylor retain their stated decisions.
- **Human/physical action owner:** Taylor; no physical, remote, device, credential, permission, destructive, residual-risk, or release action occurred.
- **Confidentiality classification:** `C1_PRIVATE_OPERATIONAL`; PRIVATE PERSONAL USE - NOT FOR PUBLIC RELEASE
- **Recoverability classification:** `R0_REPRODUCIBLE` from the frozen sources and package manifest.
- **Limitations:** Dispositions are bounded to the frozen sources and await independent review; they provide no missing device, implementation, recovery, fault, or integrated evidence.
- **Unsupported inferences:** Candidate failure, active role assignment, device fitness, qualification, Phase 4 authority, System Release, Public Release, or broader adoption.
- **Current freshness:** Current only for the frozen source identities; new device facts, implementation, requirement change, or review finding requires a new generation.
- **Supersession:** First formal Phase 3 disposition generation; supersedes the Phase 2 `not assigned` state only for this candidate package and does not rewrite Phase 2 history.
