# Phase 3 Operations and Lifecycle Policy

## Accepted retention and action timing

The following values reproduce Taylor's accepted `DEC-003`; they do not prove
an Observer or retention mechanism exists.

| Record / condition | Accepted policy | Required evidence before operational claim |
|---|---|---|
| Raw permitted operational events | Retain locally for 30 days | Schema, privacy, access, expiry, deletion/archive, and clock tests |
| Daily aggregates | Retain for 180 days | Aggregation correctness, minimization, expiry, and deletion/archive tests |
| Release and audit evidence | Use the separate evidence-retention policy, not telemetry retention | Artifact-class retention and recoverability decision before Phase 7 freeze |
| Stop-relevant condition | Block the next affected dispatch immediately | End-to-end detection and stop-path test |
| Actionable warning | Present within one day | Alert timing and presentation evidence |
| Trend-only finding | Review weekly | Aggregation, scheduling, and review-record evidence |

No content, private filename, secret value, full serial, or PRIVATE VAULT data
may be retained for any duration.

## Alert contract

Every future alert must identify the condition, affected pseudonymous role,
evidence freshness and clock quality, expected human action, response timing,
Safe Degradation/stop behavior, source schema, and alert-delivery self-test
state. Missing, stale, dropped, incompatible, or collector-unavailable data
produces `UNKNOWN` or `TELEMETRY_UNAVAILABLE`; silence is never health.

An alert presents evidence and required response. It never grants remediation,
device, credential, permission, exception, dispatch, promotion, or release
authority.

## Maintenance and support policy

These values reproduce Taylor's accepted `DEC-004`:

- Control Plane and any networked Worker must run an operating-system release
  receiving applicable security updates.
- Apply actively exploited or critical applicable security fixes within 72
  hours.
- Apply other applicable security fixes within 14 days.
- Apply feature updates only after a supported recovery point, compatibility
  test, and rollback plan.
- Suspend an unsupported networked Worker or qualify it out unless Taylor later
  accepts a separately analyzed lower-exposure design.

Every update record must bind the approved source, prior and resulting
configuration identities, applicability decision, priority window,
preconditions, pre-update recovery point, test set, verification, rollback,
failure state, and post-change identity. Silent source substitution, partial
adoption, or an unverified successful exit is prohibited.

## Lifecycle exercise policy

| Procedure | Required exercise | Current cadence | Current evidence state |
|---|---|---|---|
| Representative restore | Controlled destination; byte and semantic verification | `UNKNOWN`; Taylor has not accepted a schedule | Not performed |
| Control Plane recovery/rebuild | Known-state recovery preserving authority/source boundaries | `UNKNOWN`; Taylor has not accepted a schedule | Not performed |
| Worker clean rebuild | Approved sources; no unique local state; within accepted RTO | `UNKNOWN`; Taylor has not accepted a schedule | Software/device blocked |
| Diagnostics and capacity review | Role-specific, privacy-safe, no fitness inference from one fragment | `UNKNOWN`; Taylor has not accepted a schedule | Phase 2 fragments only |
| Observer self-health/alert route | Failure, freshness, clock, schema, drop, retention, and delivery tests | `UNKNOWN`; Taylor has not accepted a schedule | Not implemented |
| Update and rollback | Supported source, recovery point, update, verification, rollback, re-verification | At each applicable update; periodic rehearsal cadence `UNKNOWN` | Not performed |
| Retirement rehearsal | Non-destructive inventory, copy, evidence, disengagement, and sanitization routing | `UNKNOWN`; Taylor has not accepted a schedule | Not performed |

An `UNKNOWN` cadence blocks a claim that periodic exercise obligations are
satisfied. Phase 3 does not invent customary schedules.

## Support-sunset and retirement triggers

A role leaves normal service and enters a hold or blocked state when any of the
following applies: security-support sunset; diagnostic or integrity failure;
unstable power, battery, thermal, storage, or workload behavior; failed
restore/rebuild; insufficient capacity; unacceptable exposure; persistent
configuration drift; lost authoritative source; failed Observer visibility
where the role depends on it; or Taylor's separately made repair/replacement
decision.

The non-destructive retirement plan is:

1. stop new dependent work and identify the exact role/configuration;
2. inventory only minimum necessary role metadata;
3. confirm authoritative sources and independent protected copies;
4. preserve required evidence and perform representative restore/rebuild proof;
5. disengage services, dispatch, storage assignment, and network exposure;
6. route any sanitization method, target, hazard analysis, recovery proof, and
   Taylor confirmation to a separate Tier 3 cutover; and
7. record final reuse, replacement, recycle, or retained-offline decision.

This plan performs no deletion, erase, repartition, format, sanitization, wipe,
credential revocation, or device action.

## DEAS evidence-record contract

- **Evidence ID:** `EV-P3-MAINTENANCE`, `EV-P3-RETENTION-POLICY`, `EV-P3-ALERT-CONTRACT`, `EV-P3-LIFECYCLE`, `EV-P3-RETIREMENT`
- **Requirement/fault IDs:** `REQ-CP-008`, `REQ-OBS-008`, `REQ-OBS-009`, `REQ-OPS-002`, `REQ-OPS-005`, `REQ-OPS-006`, `REQ-OPS-007`, `FLT-OBS-002`, `FLT-OBS-006`, `FLT-SUP-001`, `FLT-SUP-002`, `FLT-UPD-001`, `FLT-RET-001`
- **Claim under test:** The Phase 3 lifecycle policy reproduces accepted retention, alert, patch, and support values; specifies maintenance and non-destructive retirement contracts; and preserves unaccepted exercise cadences as `UNKNOWN`.
- **Acceptance method:** Inspection and analysis against `DEC-003`, `DEC-004`, `DEC-005`, lifecycle requirements, and the fault matrix; future implementation, rehearsal, and independent review remain required.
- **Exact source/configuration/role/device-safe identity/environment/target:** Frozen sources in `source-register.md`; all Operational System roles and five candidates; private documentation environment only.
- **Procedure or command identity:** One bounded operations/lifecycle derivation checked by `validation/validate_phase3.py`; no update, alert, retention, deletion, retirement, sanitization, credential, or device command.
- **Start time:** 2026-09-05T19:24:10-05:00
- **End time:** 2026-09-05T20:34:39-05:00
- **Clock-quality basis:** Execution-host wall clock in America/Chicago with one-second display precision; no external time attestation.
- **Expected result:** Accepted numerical policies are exact, every lifecycle action has prerequisites and evidence, unknown cadences remain explicit, and destructive retirement remains separately governed.
- **Actual result:** Retention/action timing, alert, maintenance/support, seven exercise classes, support-sunset triggers, and a seven-step non-destructive retirement route are defined; all unaccepted cadences remain `UNKNOWN`.
- **Status:** DESIGN_DEFINED_NOT_IMPLEMENTED
- **Discrepancy references:** [Phase 2 discrepancies and unknowns](../../qualification/phase-2/discrepancies-and-unknowns.md) and [Role Dispositions](role-dispositions.md)
- **Artifact paths:** `contexts/operational-system/docs/program/v1/architecture/phase-3/operations-lifecycle-policy.md`
- **Cryptographic identities:** Frozen by `phase-3-sha256.txt`; its non-circular SHA-256 is supplied by the external freeze record.
- **Evidence owner:** Codex in Taylor AI Workbench for the recorded analysis; future operations, maintenance, data, and lifecycle owners remain assigned by the requirements.
- **Human/physical action owner:** Taylor for schedule/value decisions, device/physical action, credentials, destructive approval, residual risk, and final retirement disposition; none occurred.
- **Confidentiality classification:** `C1_PRIVATE_OPERATIONAL`; PRIVATE PERSONAL USE - NOT FOR PUBLIC RELEASE
- **Recoverability classification:** `R0_REPRODUCIBLE` from the frozen sources and package manifest.
- **Limitations:** No scheduler, collector, update, rollback, retention deletion, alert, exercise, support-state check, or retirement rehearsal is implemented or tested.
- **Unsupported inferences:** Operational compliance, supported device state, alert delivery, retention enforcement, recovery fitness, retirement authority, sanitization authority, qualification, or release.
- **Current freshness:** Accepted values are current for `DEC-003` through `DEC-005`; device/support facts and unaccepted exercise cadences remain `UNKNOWN`.
- **Supersession:** First Phase 3 operations and lifecycle policy; supersedes no earlier Phase 3 artifact.
