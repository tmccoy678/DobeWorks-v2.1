# Requirements-to-Evidence Traceability Matrix

This matrix distinguishes produced evidence, produced evidence with unresolved
items, blocked evidence, and future evidence. `DEFINED` means the requirement
and evidence contract exist; it does not mean the system complies. A produced
artifact proves only its bounded claim.

| Requirement | Source basis | Planned evidence | Phase | Current state |
|---|---|---|---:|---|
| `REQ-PGM-001` | DobeWorks private scope; research boundary | `EV-P1-SPEC`, `EV-P7-AUDIT` | 1,7 | `DEFINED` |
| `REQ-PGM-002` | Research completion proposition | `EV-P1-SPEC`, `EV-P7-TRACE`, `EV-P7-AUDIT` | 1,7 | `DEFINED` |
| `REQ-PGM-003` | Handoff Q2; root/project domain rules | `EV-P1-CONTEXT`, `EV-P1-ADR`, `EV-P1-DECISIONS` | 1 | `DEFINED; DEC-007 ACCEPTED` |
| `REQ-PGM-004` | Handoff status and phase gates | `EV-P1-DEGS`, `EV-P7-DEGS`, `EV-P8-ACCEPTANCE` | 1,7,8 | `DEFINED`; Phase 3 preserves `NOT_YET_QUALIFIED`, `NOT_YET_RELEASED` |
| `REQ-PGM-005` | Research unknowns; fail-safe default | `EV-P1-VALIDATION`, `EV-P2-QUALIFICATION`, `EV-P7-AUDIT` | 1,2,7 | `EV-P2-QUALIFICATION PRODUCED_WITH_UNRESOLVED_ITEMS`; [G2 basis](#phase-2-generation-2-status-basis) |
| `REQ-PGM-006` | Accepted exact-device decision | `EV-P3-DISPOSITIONS`, `EV-P6-QUALIFICATION` | 3,6 | `EV-P3-DISPOSITIONS PRODUCED_REVIEW_PENDING`; five candidates `BLOCKED_PENDING_EVIDENCE`; Phase 6 evidence `FUTURE`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-PGM-007` | Handoff authority boundary | `EV-P1-SPEC`, `EV-P1-PHASE2-GATE`, `EV-P7-DEGS` | 1,7 | `DEFINED` |
| `REQ-PGM-008` | DEGS controlled-state invariant | `EV-PROMOTION-MANIFEST`, `EV-P7-ARTIFACT-IDENTITY` | promotion,7 | `PLANNED` |
| `REQ-CP-001` | Historical-baseline limitation | `EV-P2-CP-BASELINE` | 2 | `PRODUCED_WITH_UNRESOLVED_DISCREPANCY`; [G2 basis](#phase-2-generation-2-status-basis) |
| `REQ-CP-002` | Accepted Control Plane role | `EV-P3-ARCH`, `EV-P5-INTEGRATION`, `EV-P6-CP-TEST` | 3,5,6 | `EV-P3-ARCH PRODUCED_DESIGN_ONLY`; integration and qualification evidence `FUTURE`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-CP-003` | DEGS authority lanes and security invariants | `EV-P3-AUTHORITY`, `EV-P4-SECURITY-TEST`, `EV-P6-FAULT` | 3,4,6 | `EV-P3-AUTHORITY PRODUCED_DESIGN_ONLY`; `EV-P4-SECURITY-TEST PRODUCED_SOFTWARE_CORE`; integrated enforcement/fault evidence `FUTURE`; [P3 basis](#phase-3-package-status-basis), [P4 basis](#phase-4-package-status-basis) |
| `REQ-CP-004` | Worker-delivery research | `EV-P4-JOB-CONTRACT`, `EV-P4-WORKER-TEST` | 4 | `PRODUCED_SOFTWARE_CORE`; synthetic contract/tests only; actual Control Plane dispatch enforcement `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-CP-005` | Accepted output-authority decision | `EV-P4-PROMOTION-CONTRACT`, `EV-P5-INTEGRATION`, `EV-P6-FAULT` | 4,5,6 | `EV-P4-PROMOTION-CONTRACT PRODUCED_SOFTWARE_CORE`; Promotion Event integration/fault evidence `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-CP-006` | Recovery research and DEC-001 | `EV-P3-RECOVERY-DESIGN`, `EV-P6-CP-RECOVERY` | 3,6 | `EV-P3-RECOVERY-DESIGN PRODUCED_DESIGN_ONLY`; recovery evidence `FUTURE`; `DEC-001 ACCEPTED`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-CP-007` | Accepted fault set | `EV-P6-CP-RECOVERY`, `EV-P6-FAULT` | 6 | `PLANNED` |
| `REQ-CP-008` | Patch/release research and DEC-004 | `EV-P3-MAINTENANCE`, `EV-P6-UPDATE-ROLLBACK` | 3,6 | `EV-P3-MAINTENANCE PRODUCED_DESIGN_ONLY`; update/rollback evidence `FUTURE`; `DEC-004 ACCEPTED`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-CP-009` | Security invariants and minimization research | `EV-P4-SECRET-HYGIENE`, `EV-P7-PRIVACY-REVIEW` | 4,7 | `EV-P4-SECRET-HYGIENE PRODUCED_SOFTWARE_CORE`; deployed privacy review `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-ST-001` | Historical Seagate unknowns | `EV-P2-ST-TOPOLOGY` | 2 | `PRODUCED_WITH_UNKNOWNS`; [G2 basis](#phase-2-generation-2-status-basis) |
| `REQ-ST-002` | Research storage-role contract | `EV-P3-STORAGE-ARCH`, `EV-P3-DATA-MAP` | 3 | `EV-P3-STORAGE-ARCH` and `EV-P3-DATA-MAP PRODUCED_DESIGN_ONLY`; no Storage Role assigned; [P3 basis](#phase-3-package-status-basis) |
| `REQ-ST-003` | Accepted no-sole-copy rule | `EV-P2-COPY-MAP`, `EV-P6-REDUNDANCY-TEST` | 2,6 | `EV-P2-COPY-MAP NOT_PRODUCED`; later evidence `FUTURE`; [G2 basis](#phase-2-generation-2-status-basis) |
| `REQ-ST-004` | NIST backup/RPO/RTO synthesis | `EV-P3-RECOVERY-DESIGN`, `EV-P6-BACKUP-EVIDENCE` | 3,6 | `EV-P3-RECOVERY-DESIGN PRODUCED_DESIGN_ONLY`; backup evidence `FUTURE`; `DEC-001 ACCEPTED`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-ST-005` | Capacity/retention research | `EV-P3-CAPACITY-POLICY`, `EV-P6-CAPACITY-TEST` | 3,6 | `EV-P3-CAPACITY-POLICY PRODUCED_WITH_EXPLICIT_UNKNOWNS`; capacity test `FUTURE`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-ST-006` | Restore evidence research | `EV-P6-RESTORE` | 6 | `PLANNED` |
| `REQ-ST-007` | Apple/Seagate/Google diagnostic limits | `EV-P2-QUALIFICATION-PLAN`, `EV-P7-AUDIT` | 2,7 | `EV-P2-QUALIFICATION-PLAN PRODUCED`; later audit `FUTURE`; [G2 basis](#phase-2-generation-2-status-basis) |
| `REQ-ST-008` | Accepted fault set | `EV-P6-STORAGE-FAULT` | 6 | `PLANNED` |
| `REQ-ST-009` | Accepted destructive-scope boundary | `EV-P1-SPEC`, `EV-P4-SECURITY-TEST`, `EV-P7-AUDIT` | 1,4,7 | `DEFINED`; `EV-P4-SECURITY-TEST PRODUCED_SOFTWARE_CORE`; no destructive interface/action; final audit `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-ST-010` | Accepted exact-device disposition | `EV-P3-DISPOSITIONS`, `EV-P6-QUALIFICATION` | 3,6 | `SR-CANDIDATE-01 BLOCKED_PENDING_EVIDENCE_REVIEW_PENDING`; qualification evidence `FUTURE`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-ST-011` | Evidence privacy boundary | `EV-P2-SANITIZED-EVIDENCE`, `EV-P7-PRIVACY-REVIEW` | 2,7 | `EV-P2-SANITIZED-EVIDENCE PRODUCED_WITH_UNKNOWNS`; later review `FUTURE`; [G2 basis](#phase-2-generation-2-status-basis) |
| `REQ-WK-001` | Research 2015 MacBook unknowns | `EV-P2-WK-BASELINE`, `EV-P5-WK-WORKLOAD` | 2,5 | `EV-P2-WK-BASELINE RECORD_PRODUCED; BLOCKED_PENDING_EVIDENCE`; later workload evidence `FUTURE`; [G2 basis](#phase-2-generation-2-status-basis) |
| `REQ-WK-002` | Accepted bounded-worker decision | `EV-P3-WORKER-ARCH`, `EV-P5-INTEGRATION`, `EV-P6-WK-REBUILD` | 3,5,6 | `EV-P3-WORKER-ARCH PRODUCED_DESIGN_ONLY`; integration/rebuild evidence `FUTURE`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-WK-003` | Data trust ceiling and DEC-002 | `EV-P3-DATA-MAP`, `EV-P4-SECURITY-TEST`, `EV-P5-INTEGRATION` | 3,4,5 | `EV-P3-DATA-MAP PRODUCED_DESIGN_ONLY`; `EV-P4-SECURITY-TEST PRODUCED_SOFTWARE_CORE` for synthetic `PUBLIC_METADATA`; actual placement/integration `FUTURE`; `DEC-002 ACCEPTED`; [P3 basis](#phase-3-package-status-basis), [P4 basis](#phase-4-package-status-basis) |
| `REQ-WK-004` | Worker-delivery research | `EV-P4-JOB-CONTRACT`, `EV-P4-WORKER-TEST` | 4 | `PRODUCED_SOFTWARE_CORE`; synthetic immutable envelope and exact identity tests; persistent dispatch enforcement `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-WK-005` | Google/Amazon job-semantics synthesis | `EV-P4-JOB-CONTRACT`, `EV-P4-WORKER-TEST` | 4 | `PRODUCED_SOFTWARE_CORE`; exact synthetic job-class semantics tested; additional real job classes `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-WK-006` | Idempotency and ambiguous-result synthesis | `EV-P4-WORKER-NEGATIVE-TEST` | 4 | `PRODUCED_SOFTWARE_CORE`; in-memory duplicate/reuse and no-retry semantics tested; persistent registry `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-WK-007` | Accepted fault set | `EV-P4-WORKER-FAILURE-TEST`, `EV-P6-FAULT` | 4,6 | `EV-P4-WORKER-FAILURE-TEST PRODUCED_SOFTWARE_CORE`; actual device/restart/overload demonstration and Phase 6 fault evidence `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-WK-008` | Accepted staged-output decision | `EV-P4-HANDBACK-TEST`, `EV-P5-INTEGRATION` | 4,5 | `EV-P4-HANDBACK-TEST PRODUCED_SOFTWARE_CORE`; synthetic atomic directory handback tested; authoritative-target integration `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-WK-009` | Accepted promotion-authority decision | `EV-P4-PROMOTION-NEGATIVE-TEST`, `EV-P5-INTEGRATION` | 4,5 | `EV-P4-PROMOTION-NEGATIVE-TEST PRODUCED_SOFTWARE_CORE`; no Worker promotion interface and `NOT_PERFORMED` tested; actual Control Plane promotion `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-WK-010` | Worker recoverability research | `EV-P6-WK-REBUILD` | 6 | `DEFINED; DEC-001 ACCEPTED` |
| `REQ-WK-011` | Support/exposure research and DEC-002/004 | `EV-P2-WK-SUPPORT`, `EV-P3-DISPOSITIONS`, `EV-P6-QUALIFICATION` | 2,3,6 | `EV-P2-WK-SUPPORT NOT_PRODUCED`; `WK-CANDIDATE-01 BLOCKED_PENDING_EVIDENCE_REVIEW_PENDING`; later evidence `FUTURE`; `DEC-002/004 ACCEPTED`; [G2 basis](#phase-2-generation-2-status-basis), [P3 basis](#phase-3-package-status-basis) |
| `REQ-WK-012` | Accepted no-sunk-cost disposition | `EV-P3-DISPOSITIONS`, `EV-P6-QUALIFICATION` | 3,6 | `WK-CANDIDATE-01 BLOCKED_PENDING_EVIDENCE_REVIEW_PENDING`; qualification evidence `FUTURE`; `DEC-005 ACCEPTED`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-OBS-001` | Accepted read-only observer decision | `EV-P3-OBSERVER-ARCH`, `EV-P4-OBSERVER-SECURITY-TEST` | 3,4 | `EV-P3-OBSERVER-ARCH PRODUCED_DESIGN_ONLY`; `EV-P4-OBSERVER-SECURITY-TEST PRODUCED_SOFTWARE_CORE`; deployed least-privilege review `FUTURE`; [P3 basis](#phase-3-package-status-basis), [P4 basis](#phase-4-package-status-basis) |
| `REQ-OBS-002` | NIST monitoring/minimization synthesis | `EV-P3-SIGNAL-DECISION-MAP`, `EV-P4-OBSERVER-SCHEMA`, `EV-P4-OBSERVER-TEST`, `EV-P7-PRIVACY-REVIEW` | 3,4,7 | `EV-P3-SIGNAL-DECISION-MAP PRODUCED_DESIGN_ONLY`; Phase 4 schema/map `PRODUCED_SOFTWARE_CORE`; deployed privacy review `FUTURE`; [P3 basis](#phase-3-package-status-basis), [P4 basis](#phase-4-package-status-basis) |
| `REQ-OBS-003` | OpenTelemetry and privacy synthesis | `EV-P4-OBSERVER-SCHEMA`, `EV-P4-OBSERVER-TEST` | 4 | `PRODUCED_SOFTWARE_CORE`; versioned synthetic schema, provenance, clock semantics, and exact output tested; actual collector/OTel integration `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-OBS-004` | Security invariants and research exclusions | `EV-P4-OBSERVER-PRIVACY-TEST`, `EV-P7-PRIVACY-REVIEW` | 4,7 | `EV-P4-OBSERVER-PRIVACY-TEST PRODUCED_SOFTWARE_CORE`; prohibited nested data tests pass; deployed privacy review `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-OBS-005` | Candidate signal set and validation boundary | `EV-P2-OBS-SURFACE`, `EV-P3-SIGNAL-DECISION-MAP`, `EV-P5-TELEMETRY-INTEGRATION` | 2,3,5 | `EV-P2-OBS-SURFACE PRODUCED_EXECUTABLE_PRESENCE_ONLY`; `EV-P3-SIGNAL-DECISION-MAP PRODUCED_DESIGN_ONLY`; integration `FUTURE`; [G2 basis](#phase-2-generation-2-status-basis), [P3 basis](#phase-3-package-status-basis) |
| `REQ-OBS-006` | Accepted unknown-state behavior | `EV-P4-OBSERVER-FAILURE-TEST`, `EV-P6-FAULT` | 4,6 | `EV-P4-OBSERVER-FAILURE-TEST PRODUCED_SOFTWARE_CORE`; stale, failed, uncertain, dropped, and missing synthetic cases tested; actual collector fault evidence `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-OBS-007` | Collector self-health research | `EV-P4-OBSERVER-SCHEMA`, `EV-P4-OBSERVER-FAILURE-TEST` | 4 | `PRODUCED_SOFTWARE_CORE`; exact self-health schema and failure meanings tested; live collector demonstration `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-OBS-008` | Retention/minimization research and DEC-003 | `EV-P3-RETENTION-POLICY`, `EV-P4-RETENTION-TEST` | 3,4 | `EV-P3-RETENTION-POLICY PRODUCED_DESIGN_ONLY`; `EV-P4-RETENTION-TEST PRODUCED_SOFTWARE_CORE` for decisions only; real deletion/archive verification `FUTURE`; `DEC-003 ACCEPTED`; [P3 basis](#phase-3-package-status-basis), [P4 basis](#phase-4-package-status-basis) |
| `REQ-OBS-009` | Actionable-alert research and DEC-003 | `EV-P3-ALERT-CONTRACT`, `EV-P5-ALERT-DEMO` | 3,5 | `EV-P3-ALERT-CONTRACT PRODUCED_DESIGN_ONLY`; alert demo `FUTURE`; `DEC-003 ACCEPTED`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-OBS-010` | Accepted fault set and OTel limit | `EV-P4-OBSERVER-FAILURE-TEST`, `EV-P6-FAULT`, `EV-P7-AUDIT` | 4,6,7 | `EV-P4-OBSERVER-FAILURE-TEST PRODUCED_SOFTWARE_CORE`; permission denial, alert delivery, live collector, Phase 6 fault evidence, and final audit `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-OPS-001` | Phase 1 data model | `EV-P1-SPEC`, `EV-P3-DATA-MAP`, `EV-P5-DATA-FLOW-TEST` | 1,3,5 | `EV-P3-DATA-MAP PRODUCED_DESIGN_ONLY`; data-flow test `FUTURE`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-OPS-002` | Research rejects universal values | `EV-P1-DECISIONS`, `EV-P1-TAYLOR-DECISION` | 1 | `DEFINED; DEC-001..006 ACCEPTED` |
| `REQ-OPS-003` | Failure-handling research | `EV-P1-FAULT`, `EV-P3-FMEA`, `EV-P6-FAULT` | 1,3,6 | `EV-P3-FMEA PRODUCED_DESIGN_ONLY`; fault evidence `FUTURE`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-OPS-004` | Fail-safe defaults and accepted boundaries | `EV-P3-SAFE-DEGRADATION`, `EV-P6-FAULT` | 3,6 | `EV-P3-SAFE-DEGRADATION PRODUCED_DESIGN_ONLY`; tests `FUTURE`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-OPS-005` | Patch/rollback research and DEC-004 | `EV-P3-MAINTENANCE`, `EV-P6-UPDATE-ROLLBACK` | 3,6 | `EV-P3-MAINTENANCE PRODUCED_DESIGN_ONLY`; update/rollback evidence `FUTURE`; `DEC-004 ACCEPTED`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-OPS-006` | Lifecycle exercise research | `EV-P3-LIFECYCLE`, `EV-P6-OPS-EXERCISES` | 3,6 | `EV-P3-LIFECYCLE PRODUCED_WITH_UNKNOWN_CADENCES`; exercises `FUTURE`; `DEC-003/004 ACCEPTED`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-OPS-007` | Retirement/sanitization research and DEC-005 | `EV-P3-RETIREMENT`, `EV-P6-RETIREMENT-REHEARSAL` | 3,6 | `EV-P3-RETIREMENT PRODUCED_DESIGN_ONLY`; rehearsal `FUTURE`; `DEC-005 ACCEPTED`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-OPS-008` | Assurance discrepancy closure | `EV-P6-DISCREPANCY-LOG`, `EV-P7-AUDIT` | 6,7 | `PLANNED` |
| `REQ-ASS-001` | NASA traceability synthesis | `EV-P1-TRACE`, `EV-P3-VALIDATION`, `EV-P7-TRACE` | 1,3,7 | `EV-P3-VALIDATION PRODUCED_PACKAGE_SCOPE`; completion trace/audit `FUTURE`; [P3 basis](#phase-3-package-status-basis) |
| `REQ-ASS-002` | Release/provenance research | `EV-P4-ARTIFACT-IDENTITY`, `EV-P7-ARTIFACT-IDENTITY` | 4,7 | `EV-P4-ARTIFACT-IDENTITY PRODUCED_SOFTWARE_CORE`; exact source/config/environment/target/procedure/result/artifact identities; completion identity `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-ASS-003` | Research acceptance evidence stack | `EV-P4-SW-TEST`, `EV-P5-INTEGRATION`, `EV-P6-FAULT`, `EV-P6-E2E` | 4,5,6 | `EV-P4-SW-TEST PRODUCED_SOFTWARE_CORE`; integration, actual fault, and actual end-to-end evidence `FUTURE`; [P4 basis](#phase-4-package-status-basis) |
| `REQ-ASS-004` | Independent assurance research | `EV-P7-FROZEN-MANIFEST` | 7 | `PLANNED` |
| `REQ-ASS-005` | Accepted completion chain and DEGS limits | `EV-P7-DEGS` | 7 | `PLANNED` |
| `REQ-ASS-006` | NASA/NIST independent assurance synthesis | `EV-P7-AUDIT` | 7 | `PLANNED` |
| `REQ-ASS-007` | Accepted critical-unknown boundary and DEC-006 | `EV-P7-AUDIT`, `EV-P8-RISK-REVIEW` | 7,8 | `DEFINED; DEC-006 ACCEPTED` |
| `REQ-ASS-008` | Accepted Taylor release authority | `EV-P8-ACCEPTANCE` | 8 | `PLANNED` |

## Phase 2 Generation 2 status basis

Every changed Phase 2 state above is bound to the exact
[Generation 2 task](qualification/phase-2/degs/phase2-generation-2-task.json),
[Generation 2 manifest](qualification/phase-2/generation-2-sha256.txt), and
[Generation 2 validation result](qualification/phase-2/validation/validation-report.md).
Open historical discrepancies and unknowns remain in
[discrepancies-and-unknowns.md](qualification/phase-2/discrepancies-and-unknowns.md).
The task is a documentation correction; it did not recollect evidence, resolve
an unknown, assign a Role Disposition, or authorize a later phase.

## Phase 3 package status basis

Every Phase 3 state above is bound to the exact
[Phase 3 task](architecture/phase-3/degs/phase3-task.json),
[non-self manifest](architecture/phase-3/phase-3-sha256.txt), and
[validation report](architecture/phase-3/validation/validation-report.md).
The manifest's own SHA-256 is supplied externally after freeze. The
[Role Dispositions](architecture/phase-3/role-dispositions.md) assign all five
candidates `BLOCKED_PENDING_EVIDENCE` and remain pending independent review.
Phase 3 design evidence does not substitute for Phase 4 implementation, Phase
5 integration, Phase 6 qualification, Phase 7 completion review, or Phase 8
Taylor acceptance.

## Phase 4 package status basis

Every Phase 4 software-core state above is bound to the exact
[Phase 4 task](architecture/phase-4/degs/phase4-task.json),
[non-self manifest](architecture/phase-4/phase-4-sha256.txt),
[validation report](architecture/phase-4/validation/validation-report.md), and
[handoff](architecture/phase-4/handoff.md). The manifest's own SHA-256 and the
external identity/review/delivery records are supplied after immutable freeze.
`PRODUCED_SOFTWARE_CORE` means only that exact synthetic Module behavior was
implemented and tested. It does not mean a device, Control Plane, transport,
collector, service, Promotion Event, persistent state, integration, or
qualification was tested. Controlled integration is `NOT_PERFORMED`.

## Evidence identities

| Evidence ID | Planned artifact or bundle | Status |
|---|---|---|
| `EV-P1-SPEC` | `program-definition.md` | Canonical, accepted |
| `EV-P1-CONTEXT` | `../../../CONTEXT.md` | Canonical, accepted |
| `EV-P1-ADR` | `../../../../../docs/adr/0013-distinct-operational-system-context.md` | Canonical, accepted |
| `EV-P1-DECISIONS` | `decisions.md` | Canonical, accepted |
| `EV-P1-TRACE` | This matrix | Canonical, accepted |
| `EV-P1-FAULT` | `fault-test-matrix.md` | Canonical, accepted |
| `EV-P1-PHASE2-GATE` | `phase-2-entry-criteria.md` | Canonical, active gate |
| `EV-P1-VALIDATION` | `provenance.md` references the frozen validation report | Verified source evidence |
| `EV-P1-DEGS` | `provenance.md` references the frozen Phase 1 DEGS task and PASS result | Verified source evidence |
| `EV-P1-TAYLOR-DECISION` | `decisions.md` records Taylor's exact decision without inference | Canonical, accepted |
| `EV-P2-QUALIFICATION` | `qualification/phase-2/qualification-plan.md` and `qualification/phase-2/validation/validation-report.md` | Produced; validation `PASS`; unresolved historical items preserved; [G2 basis](#phase-2-generation-2-status-basis) |
| `EV-P2-CP-BASELINE` | `qualification/phase-2/evidence/current-mac-baseline.md` | Produced with unresolved free-space discrepancy and explicit unknowns; [G2 basis](#phase-2-generation-2-status-basis) |
| `EV-P2-ST-TOPOLOGY` | `qualification/phase-2/evidence/seagate-device-volume.md` | Produced with explicit unknowns; [G2 basis](#phase-2-generation-2-status-basis) |
| `EV-P2-SANITIZED-EVIDENCE` | `qualification/phase-2/evidence/` and `qualification/phase-2/evidence/command-log.md` | Produced within the frozen privacy boundary; [G2 basis](#phase-2-generation-2-status-basis) |
| `EV-P2-OBS-SURFACE` | `qualification/phase-2/evidence/observer-surface.md` | Produced; executable presence only; [G2 basis](#phase-2-generation-2-status-basis) |
| `EV-P2-WK-BASELINE` | `qualification/phase-2/evidence/worker-candidate.md` | Evidence record produced; observation `BLOCKED_PENDING_EVIDENCE`; [G2 basis](#phase-2-generation-2-status-basis) |
| `EV-P2-QUALIFICATION-PLAN` | `qualification/phase-2/qualification-plan.md` | Produced; [G2 basis](#phase-2-generation-2-status-basis) |
| `EV-P2-COPY-MAP` | No Phase 2 artifact | Future; not produced |
| `EV-P2-WK-SUPPORT` | No Phase 2 artifact | Future; not produced because Worker evidence is blocked |
| `EV-P3-ARCH`, `EV-P3-STORAGE-ARCH`, `EV-P3-WORKER-ARCH`, `EV-P3-OBSERVER-ARCH` | `architecture/phase-3/role-architecture.md` | Produced; design only; no role active or qualified |
| `EV-P3-DATA-MAP`, `EV-P3-SIGNAL-DECISION-MAP` | `architecture/phase-3/data-and-signal-map.md` | Produced; design only; no data flow or Observer implemented |
| `EV-P3-AUTHORITY` | `architecture/phase-3/authority-and-threat-map.md` | Produced; authority/threat design only; enforcement evidence future |
| `EV-P3-RECOVERY-DESIGN`, `EV-P3-CAPACITY-POLICY` | `architecture/phase-3/recovery-and-capacity-policy.md` | Produced; accepted policy values plus explicit capacity/recovery unknowns |
| `EV-P3-MAINTENANCE`, `EV-P3-RETENTION-POLICY`, `EV-P3-ALERT-CONTRACT`, `EV-P3-LIFECYCLE`, `EV-P3-RETIREMENT` | `architecture/phase-3/operations-lifecycle-policy.md` | Produced; design only; unaccepted cadences remain `UNKNOWN` |
| `EV-P3-FMEA`, `EV-P3-SAFE-DEGRADATION` | `architecture/phase-3/fault-and-safe-degradation.md` | Produced; all 37 faults remain applicable; no fault test passed from prose |
| `EV-P3-DISPOSITIONS` | `architecture/phase-3/role-dispositions.md` | Produced, review pending; five exact `BLOCKED_PENDING_EVIDENCE` results |
| `EV-P3-VALIDATION` | `architecture/phase-3/validation/validation-report.md` | Produced; package scope; G7/G8/G9 external |
| `EV-P4-JOB-CONTRACT`, `EV-P4-WORKER-TEST`, `EV-P4-WORKER-NEGATIVE-TEST`, `EV-P4-WORKER-FAILURE-TEST`, `EV-P4-HANDBACK-TEST`, `EV-P4-PROMOTION-NEGATIVE-TEST` | `architecture/phase-4/worker-core-evidence.md` and `../../../software/phase4/` | Produced software core; synthetic-only; actual integration/qualification future; [P4 basis](#phase-4-package-status-basis) |
| `EV-P4-OBSERVER-SECURITY-TEST`, `EV-P4-OBSERVER-SCHEMA`, `EV-P4-OBSERVER-TEST`, `EV-P4-OBSERVER-PRIVACY-TEST`, `EV-P4-OBSERVER-FAILURE-TEST`, `EV-P4-RETENTION-TEST` | `architecture/phase-4/observer-core-evidence.md` and `../../../software/phase4/` | Produced software core; synthetic-only; live collector/retention/integration future; [P4 basis](#phase-4-package-status-basis) |
| `EV-P4-SECURITY-TEST`, `EV-P4-PROMOTION-CONTRACT`, `EV-P4-SECRET-HYGIENE`, `EV-P4-ARTIFACT-IDENTITY`, `EV-P4-SUPPLY-FAILURE-TEST` | `architecture/phase-4/security-and-supply-evidence.md` | Produced software core; static/synthetic identity and denial evidence only; [P4 basis](#phase-4-package-status-basis) |
| `EV-P4-SW-TEST` | `architecture/phase-4/validation/validation-report.md` | Produced package-scope evidence; G7/G8/G9 external; [P4 basis](#phase-4-package-status-basis) |
| `EV-P5-*` through `EV-P8-*` | Future exact artifacts defined by separately authorized phases | Future; not produced |
