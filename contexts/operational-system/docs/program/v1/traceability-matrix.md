# Requirements-to-Evidence Traceability Matrix

This matrix plans the evidence needed to prove each normative requirement. `DEFINED` means the requirement and evidence contract exist; it does not mean the system complies. Future evidence IDs are reservations until an exact artifact is produced and frozen.

| Requirement | Source basis | Planned evidence | Phase | Current state |
|---|---|---|---:|---|
| `REQ-PGM-001` | DobeWorks private scope; research boundary | `EV-P1-SPEC`, `EV-P7-AUDIT` | 1,7 | `DEFINED` |
| `REQ-PGM-002` | Research completion proposition | `EV-P1-SPEC`, `EV-P7-TRACE`, `EV-P7-AUDIT` | 1,7 | `DEFINED` |
| `REQ-PGM-003` | Handoff Q2; root/project domain rules | `EV-P1-CONTEXT`, `EV-P1-ADR`, `EV-P1-DECISIONS` | 1 | `DEFINED; DEC-007 ACCEPTED` |
| `REQ-PGM-004` | Handoff status and phase gates | `EV-P1-DEGS`, `EV-P7-DEGS`, `EV-P8-ACCEPTANCE` | 1,7,8 | `DEFINED` |
| `REQ-PGM-005` | Research unknowns; fail-safe default | `EV-P1-VALIDATION`, `EV-P2-QUALIFICATION`, `EV-P7-AUDIT` | 1,2,7 | `DEFINED` |
| `REQ-PGM-006` | Accepted exact-device decision | `EV-P3-DISPOSITIONS`, `EV-P6-QUALIFICATION` | 3,6 | `PLANNED` |
| `REQ-PGM-007` | Handoff authority boundary | `EV-P1-SPEC`, `EV-P1-PHASE2-GATE`, `EV-P7-DEGS` | 1,7 | `DEFINED` |
| `REQ-PGM-008` | DEGS controlled-state invariant | `EV-PROMOTION-MANIFEST`, `EV-P7-ARTIFACT-IDENTITY` | promotion,7 | `PLANNED` |
| `REQ-CP-001` | Historical-baseline limitation | `EV-P2-CP-BASELINE` | 2 | `PLANNED` |
| `REQ-CP-002` | Accepted Control Plane role | `EV-P3-ARCH`, `EV-P5-INTEGRATION`, `EV-P6-CP-TEST` | 3,5,6 | `PLANNED` |
| `REQ-CP-003` | DEGS authority lanes and security invariants | `EV-P3-AUTHORITY`, `EV-P4-SECURITY-TEST`, `EV-P6-FAULT` | 3,4,6 | `PLANNED` |
| `REQ-CP-004` | Worker-delivery research | `EV-P4-JOB-CONTRACT`, `EV-P4-WORKER-TEST` | 4 | `PLANNED` |
| `REQ-CP-005` | Accepted output-authority decision | `EV-P4-PROMOTION-CONTRACT`, `EV-P5-INTEGRATION`, `EV-P6-FAULT` | 4,5,6 | `PLANNED` |
| `REQ-CP-006` | Recovery research and DEC-001 | `EV-P3-RECOVERY-DESIGN`, `EV-P6-CP-RECOVERY` | 3,6 | `DEFINED; DEC-001 ACCEPTED` |
| `REQ-CP-007` | Accepted fault set | `EV-P6-CP-RECOVERY`, `EV-P6-FAULT` | 6 | `PLANNED` |
| `REQ-CP-008` | Patch/release research and DEC-004 | `EV-P3-MAINTENANCE`, `EV-P6-UPDATE-ROLLBACK` | 3,6 | `DEFINED; DEC-004 ACCEPTED` |
| `REQ-CP-009` | Security invariants and minimization research | `EV-P4-SECRET-HYGIENE`, `EV-P7-PRIVACY-REVIEW` | 4,7 | `PLANNED` |
| `REQ-ST-001` | Historical Seagate unknowns | `EV-P2-ST-TOPOLOGY` | 2 | `PLANNED` |
| `REQ-ST-002` | Research storage-role contract | `EV-P3-STORAGE-ARCH`, `EV-P3-DATA-MAP` | 3 | `PLANNED` |
| `REQ-ST-003` | Accepted no-sole-copy rule | `EV-P2-COPY-MAP`, `EV-P6-REDUNDANCY-TEST` | 2,6 | `PLANNED` |
| `REQ-ST-004` | NIST backup/RPO/RTO synthesis | `EV-P3-RECOVERY-DESIGN`, `EV-P6-BACKUP-EVIDENCE` | 3,6 | `DEFINED; DEC-001 ACCEPTED` |
| `REQ-ST-005` | Capacity/retention research | `EV-P3-CAPACITY-POLICY`, `EV-P6-CAPACITY-TEST` | 3,6 | `DEFINED; DEC-001 ACCEPTED` |
| `REQ-ST-006` | Restore evidence research | `EV-P6-RESTORE` | 6 | `PLANNED` |
| `REQ-ST-007` | Apple/Seagate/Google diagnostic limits | `EV-P2-QUALIFICATION-PLAN`, `EV-P7-AUDIT` | 2,7 | `PLANNED` |
| `REQ-ST-008` | Accepted fault set | `EV-P6-STORAGE-FAULT` | 6 | `PLANNED` |
| `REQ-ST-009` | Accepted destructive-scope boundary | `EV-P1-SPEC`, `EV-P4-SECURITY-TEST`, `EV-P7-AUDIT` | 1,4,7 | `DEFINED` |
| `REQ-ST-010` | Accepted exact-device disposition | `EV-P3-DISPOSITIONS`, `EV-P6-QUALIFICATION` | 3,6 | `PLANNED` |
| `REQ-ST-011` | Evidence privacy boundary | `EV-P2-SANITIZED-EVIDENCE`, `EV-P7-PRIVACY-REVIEW` | 2,7 | `PLANNED` |
| `REQ-WK-001` | Research 2015 MacBook unknowns | `EV-P2-WK-BASELINE`, `EV-P5-WK-WORKLOAD` | 2,5 | `PLANNED` |
| `REQ-WK-002` | Accepted bounded-worker decision | `EV-P3-WORKER-ARCH`, `EV-P5-INTEGRATION`, `EV-P6-WK-REBUILD` | 3,5,6 | `PLANNED` |
| `REQ-WK-003` | Data trust ceiling and DEC-002 | `EV-P3-DATA-MAP`, `EV-P4-SECURITY-TEST`, `EV-P5-INTEGRATION` | 3,4,5 | `DEFINED; DEC-002 ACCEPTED` |
| `REQ-WK-004` | Worker-delivery research | `EV-P4-JOB-CONTRACT`, `EV-P4-WORKER-TEST` | 4 | `PLANNED` |
| `REQ-WK-005` | Google/Amazon job-semantics synthesis | `EV-P4-JOB-CONTRACT`, `EV-P4-WORKER-TEST` | 4 | `PLANNED` |
| `REQ-WK-006` | Idempotency and ambiguous-result synthesis | `EV-P4-WORKER-NEGATIVE-TEST` | 4 | `PLANNED` |
| `REQ-WK-007` | Accepted fault set | `EV-P4-WORKER-FAILURE-TEST`, `EV-P6-FAULT` | 4,6 | `PLANNED` |
| `REQ-WK-008` | Accepted staged-output decision | `EV-P4-HANDBACK-TEST`, `EV-P5-INTEGRATION` | 4,5 | `PLANNED` |
| `REQ-WK-009` | Accepted promotion-authority decision | `EV-P4-PROMOTION-NEGATIVE-TEST`, `EV-P5-INTEGRATION` | 4,5 | `PLANNED` |
| `REQ-WK-010` | Worker recoverability research | `EV-P6-WK-REBUILD` | 6 | `DEFINED; DEC-001 ACCEPTED` |
| `REQ-WK-011` | Support/exposure research and DEC-002/004 | `EV-P2-WK-SUPPORT`, `EV-P3-DISPOSITIONS`, `EV-P6-QUALIFICATION` | 2,3,6 | `DEFINED; DEC-002/004 ACCEPTED` |
| `REQ-WK-012` | Accepted no-sunk-cost disposition | `EV-P3-DISPOSITIONS`, `EV-P6-QUALIFICATION` | 3,6 | `DEFINED; DEC-005 ACCEPTED` |
| `REQ-OBS-001` | Accepted read-only observer decision | `EV-P3-OBSERVER-ARCH`, `EV-P4-OBSERVER-SECURITY-TEST` | 3,4 | `PLANNED` |
| `REQ-OBS-002` | NIST monitoring/minimization synthesis | `EV-P3-SIGNAL-DECISION-MAP`, `EV-P7-PRIVACY-REVIEW` | 3,7 | `PLANNED` |
| `REQ-OBS-003` | OpenTelemetry and privacy synthesis | `EV-P4-OBSERVER-SCHEMA`, `EV-P4-OBSERVER-TEST` | 4 | `PLANNED` |
| `REQ-OBS-004` | Security invariants and research exclusions | `EV-P4-OBSERVER-PRIVACY-TEST`, `EV-P7-PRIVACY-REVIEW` | 4,7 | `PLANNED` |
| `REQ-OBS-005` | Candidate signal set and validation boundary | `EV-P3-SIGNAL-DECISION-MAP`, `EV-P5-TELEMETRY-INTEGRATION` | 3,5 | `PLANNED` |
| `REQ-OBS-006` | Accepted unknown-state behavior | `EV-P4-OBSERVER-FAILURE-TEST`, `EV-P6-FAULT` | 4,6 | `PLANNED` |
| `REQ-OBS-007` | Collector self-health research | `EV-P4-OBSERVER-SCHEMA`, `EV-P4-OBSERVER-FAILURE-TEST` | 4 | `PLANNED` |
| `REQ-OBS-008` | Retention/minimization research and DEC-003 | `EV-P3-RETENTION-POLICY`, `EV-P4-RETENTION-TEST` | 3,4 | `DEFINED; DEC-003 ACCEPTED` |
| `REQ-OBS-009` | Actionable-alert research and DEC-003 | `EV-P3-ALERT-CONTRACT`, `EV-P5-ALERT-DEMO` | 3,5 | `DEFINED; DEC-003 ACCEPTED` |
| `REQ-OBS-010` | Accepted fault set and OTel limit | `EV-P4-OBSERVER-FAILURE-TEST`, `EV-P6-FAULT`, `EV-P7-AUDIT` | 4,6,7 | `PLANNED` |
| `REQ-OPS-001` | Phase 1 data model | `EV-P1-SPEC`, `EV-P3-DATA-MAP`, `EV-P5-DATA-FLOW-TEST` | 1,3,5 | `DEFINED` |
| `REQ-OPS-002` | Research rejects universal values | `EV-P1-DECISIONS`, `EV-P1-TAYLOR-DECISION` | 1 | `DEFINED; DEC-001..006 ACCEPTED` |
| `REQ-OPS-003` | Failure-handling research | `EV-P1-FAULT`, `EV-P3-FMEA`, `EV-P6-FAULT` | 1,3,6 | `DEFINED` |
| `REQ-OPS-004` | Fail-safe defaults and accepted boundaries | `EV-P3-SAFE-DEGRADATION`, `EV-P6-FAULT` | 3,6 | `PLANNED` |
| `REQ-OPS-005` | Patch/rollback research and DEC-004 | `EV-P3-MAINTENANCE`, `EV-P6-UPDATE-ROLLBACK` | 3,6 | `DEFINED; DEC-004 ACCEPTED` |
| `REQ-OPS-006` | Lifecycle exercise research | `EV-P3-LIFECYCLE`, `EV-P6-OPS-EXERCISES` | 3,6 | `DEFINED; DEC-003/004 ACCEPTED` |
| `REQ-OPS-007` | Retirement/sanitization research and DEC-005 | `EV-P3-RETIREMENT`, `EV-P6-RETIREMENT-REHEARSAL` | 3,6 | `DEFINED; DEC-005 ACCEPTED` |
| `REQ-OPS-008` | Assurance discrepancy closure | `EV-P6-DISCREPANCY-LOG`, `EV-P7-AUDIT` | 6,7 | `PLANNED` |
| `REQ-ASS-001` | NASA traceability synthesis | `EV-P1-TRACE`, `EV-P7-TRACE` | 1,7 | `DEFINED` |
| `REQ-ASS-002` | Release/provenance research | `EV-P4-ARTIFACT-IDENTITY`, `EV-P7-ARTIFACT-IDENTITY` | 4,7 | `PLANNED` |
| `REQ-ASS-003` | Research acceptance evidence stack | `EV-P4-SW-TEST`, `EV-P5-INTEGRATION`, `EV-P6-FAULT`, `EV-P6-E2E` | 4,5,6 | `PLANNED` |
| `REQ-ASS-004` | Independent assurance research | `EV-P7-FROZEN-MANIFEST` | 7 | `PLANNED` |
| `REQ-ASS-005` | Accepted completion chain and DEGS limits | `EV-P7-DEGS` | 7 | `PLANNED` |
| `REQ-ASS-006` | NASA/NIST independent assurance synthesis | `EV-P7-AUDIT` | 7 | `PLANNED` |
| `REQ-ASS-007` | Accepted critical-unknown boundary and DEC-006 | `EV-P7-AUDIT`, `EV-P8-RISK-REVIEW` | 7,8 | `DEFINED; DEC-006 ACCEPTED` |
| `REQ-ASS-008` | Accepted Taylor release authority | `EV-P8-ACCEPTANCE` | 8 | `PLANNED` |

## Planned evidence identities

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
| `EV-P2-*` through `EV-P8-*` | Future exact artifacts defined by their authorized phase | Reserved only; no evidence yet |
