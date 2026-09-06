# Normative Requirements Baseline

These are v1 system requirements, not claims that the current system satisfies them. `SHALL` is normative. A requirement is satisfied only by the acceptance method and objective evidence identified in the traceability matrix; prose agreement, component presence, or a DEGS result alone is insufficient.

Acceptance methods: `I` inspection, `A` analysis, `T` test, `D` demonstration, `R` independent review. Multiple letters require every listed method.

## Program and boundary

| ID | Normative requirement | Acceptance | Evidence owner | Earliest proof |
|---|---|---|---|---|
| `REQ-PGM-001` | The Operational System SHALL support Taylor's private DobeWorks engineering work and SHALL NOT imply Public Release, organizational adoption, commercial service, or external-user operation. | I,R | Taylor / program record | Phase 1 |
| `REQ-PGM-002` | A v1 completion claim SHALL cover mission, authority, data, failure, recovery, maintenance, and retirement for every accepted role in the integrated system. | I,A,R | Program owner | Phase 7 |
| `REQ-PGM-003` | Operational terminology and decisions SHALL remain in a distinct bounded context with explicit interfaces to, but no redefinition of, the existing DobeWorks context, root Workbench context, or DEGS. | I,R | DobeWorks project owner | Phase 1 |
| `REQ-PGM-004` | The system SHALL remain `NOT_YET_QUALIFIED` and `NOT_YET_RELEASED` until the complete evidence, DEGS, audit, and Taylor-acceptance chain finishes. | I,T,R | Release owner | Phase 8 |
| `REQ-PGM-005` | Unsupported facts and unresolved value judgments SHALL be represented as `UNKNOWN` and SHALL block any claim or action that depends on them. | I,T | Evidence owner | Phase 1 onward |
| `REQ-PGM-006` | Every candidate device or component SHALL receive exactly one evidence-backed Role Disposition: `QUALIFIED_FOR_BOUNDED_ROLE`, `QUALIFIED_OUT`, or `BLOCKED_PENDING_EVIDENCE`. | I,A,R | Architecture owner | Phase 3 |
| `REQ-PGM-007` | No handoff, gate result, lifecycle state, auditor verdict, role status, or completed phase SHALL automatically authorize the next phase or widen authority. | I,T | Taylor / governance owner | Phase 1 onward |
| `REQ-PGM-008` | Canonical promotion SHALL preserve one active source of truth per controlled concern and SHALL bind every promoted artifact to its staged source identity. | I,T,R | Configuration owner | Promotion after Phase 1 |

## Control Plane

| ID | Normative requirement | Acceptance | Evidence owner | Earliest proof |
|---|---|---|---|---|
| `REQ-CP-001` | The candidate current Mac SHALL be identified and remeasured under authorized read-only qualification before any historical measurement supports a Role Disposition. | I,T | Qualification owner | Phase 2 |
| `REQ-CP-002` | The qualified Control Plane SHALL own approved configuration, authoritative operational state, dispatch records, evidence indexes, output promotion records, and recovery orchestration. | I,A,T | Control Plane owner | Phase 5 |
| `REQ-CP-003` | The Control Plane SHALL enforce Taylor-only boundaries for credentials, authentication, physical action, destructive approval, exceptions, residual risk, phase authorization, and System Release Decision. | I,T,R | Taylor / Control Plane owner | Phase 6 |
| `REQ-CP-004` | The Control Plane SHALL dispatch Worker work only through an immutable, policy-conforming Job Envelope tied to exact input and configuration identities. | I,T | Software owner | Phase 4 |
| `REQ-CP-005` | The Control Plane SHALL keep Worker results staged until a Promotion Event verifies identity, integrity, completeness, semantics, and requirement-specific acceptance criteria. | I,T,D | Control Plane owner | Phase 5 |
| `REQ-CP-006` | The Control Plane's accepted authoritative state SHALL meet Taylor-approved RPO and RTO values and SHALL have a demonstrated known-state recovery or rebuild path. | A,T,D,R | Recovery owner | Phase 6 |
| `REQ-CP-007` | Clean bootstrap, restart, corruption, loss, replacement, and restoration scenarios SHALL preserve authority and source-of-truth boundaries. | T,D,R | Recovery owner | Phase 6 |
| `REQ-CP-008` | Every Control Plane update SHALL identify the prior and resulting configuration, supported source, pre-update recovery point, tests, verification, and rollback path. | I,T,D | Maintenance owner | Phase 6 |
| `REQ-CP-009` | Control Plane artifacts and telemetry SHALL contain no credential values, recovery keys, PRIVATE VAULT data, or full serial numbers and SHALL minimize private identifiers. | I,T,R | Security owner | Phase 4 onward |

## Storage and recovery

| ID | Normative requirement | Acceptance | Evidence owner | Earliest proof |
|---|---|---|---|---|
| `REQ-ST-001` | Each Seagate device, partition, volume, backup set, and proposed Storage Role SHALL have a privacy-safe identity and topology established without inferring inaccessible content. | I,T | Storage qualification owner | Phase 2 |
| `REQ-ST-002` | Each logical Storage Role SHALL declare its purpose, authoritative source, confidentiality and recoverability classes, allowed operations, retention, capacity policy, recovery objective, and retirement path. | I,A | Storage architecture owner | Phase 3 |
| `REQ-ST-003` | No `R2_IMPORTANT` or `R3_IRREPLACEABLE` data SHALL exist only on the Seagate or Worker. | I,T,D,R | Data owner | Phase 6 |
| `REQ-ST-004` | Every accepted backup claim SHALL identify the protected source, independent copy relationship, backup generation, confidentiality/integrity/availability protection, and Taylor-approved RPO/RTO coverage. | I,A,T | Recovery owner | Phase 6 |
| `REQ-ST-005` | Each accepted backup or archive role SHALL have format-aware capacity, retention, reserve, and growth evidence sufficient to show required recovery points will not be silently lost. | I,A,T | Storage owner | Phase 6 |
| `REQ-ST-006` | Every accepted recovery claim SHALL include a representative restore to a controlled destination with byte-level verification where meaningful and semantic/application verification where byte identity is insufficient. | T,D,R | Recovery owner | Phase 6 |
| `REQ-ST-007` | A mount, SMART result, vendor diagnostic, or file-system check SHALL be treated as an evidence fragment and SHALL NOT by itself establish fitness or recoverability. | I,A,R | Qualification owner | Phase 2 onward |
| `REQ-ST-008` | The integrated system SHALL safely handle missing, read-only, corrupt, unexpectedly disconnected, low-reserve, and unavailable Storage Resources without authority or data-integrity bypass. | T,D,R | Storage / recovery owner | Phase 6 |
| `REQ-ST-009` | Backup deletion, consolidation, repartitioning, reformatting, sanitization, erasure, or wipe SHALL be excluded from v1 qualification execution and routed through a separate Tier 3 cutover. | I,T,R | Taylor / governance owner | Phase 1 onward |
| `REQ-ST-010` | The Seagate SHALL receive a Role Disposition based on topology, redundancy, diagnostics, integrity, capacity, representative restore, and lifecycle evidence; no sunk-cost exception applies. | I,A,T,R | Architecture owner | Phase 3 / 6 |
| `REQ-ST-011` | Storage evidence SHALL omit content, prohibited private filenames, full serials, credential values, and PRIVATE VAULT information while retaining enough pseudonymous identity for traceability. | I,T,R | Evidence owner | Phase 2 onward |

## Worker and job delivery

| ID | Normative requirement | Acceptance | Evidence owner | Earliest proof |
|---|---|---|---|---|
| `REQ-WK-001` | The exact 2015 MacBook model, configuration, OS/security-support state, storage, battery, power, thermal, network, recoverability, and representative workload behavior SHALL be established before qualification. | I,T,D | Worker qualification owner | Phase 2 / 5 |
| `REQ-WK-002` | A Worker SHALL be rebuildable and non-authoritative and SHALL hold no sole-copy important data, authoritative configuration, promotion authority, or broad credential. | I,T,D,R | Worker owner | Phase 5 / 6 |
| `REQ-WK-003` | Worker exposure and permitted confidentiality/recoverability classes SHALL conform to Taylor's accepted exposure ceiling; unknown class or unsupported exposure SHALL block dispatch. | I,T | Security owner | Phase 5 |
| `REQ-WK-004` | Every Worker execution SHALL use an immutable Job Envelope containing job ID, input and configuration digests, data classes, dispatch authority, expiry, and expected output identity. | I,T | Software owner | Phase 4 |
| `REQ-WK-005` | Every allowed job class SHALL define omission, duplication, delivery intent, idempotency, side effects, retry/backoff, interruption, timeout, cancellation, stale-job, checkpoint, and output handback semantics. | I,A,T | Software owner | Phase 4 |
| `REQ-WK-006` | Reuse of a job ID with semantically different input or configuration SHALL be rejected, and ambiguous completion SHALL not trigger automatic retry unless repetition is proven safe. | T | Software owner | Phase 4 |
| `REQ-WK-007` | Worker cancellation, timeout, interruption, restart, overload, duplicate dispatch, and stale job behavior SHALL preserve authoritative state and produce unambiguous or explicitly ambiguous status. | T,D | Software / Worker owner | Phase 4 / 6 |
| `REQ-WK-008` | Worker output SHALL be written through a staged, integrity-identified handback that cannot partially replace authoritative output. | I,T,D | Software owner | Phase 4 / 5 |
| `REQ-WK-009` | The Worker SHALL NOT perform its own Promotion Event, modify the Control Plane source of truth, or represent successful process exit as accepted completion. | I,T | Security / Software owner | Phase 4 |
| `REQ-WK-010` | Worker bootstrap and rebuild from approved sources SHALL meet the accepted rebuild RTO without depending on unique local state. | T,D,R | Worker / Recovery owner | Phase 6 |
| `REQ-WK-011` | A networked Worker SHALL run software within the accepted security-support boundary; otherwise it SHALL be suspended, qualified out, or placed in a separately accepted lower-exposure role. | I,A,T,R | Taylor / Security owner | Phase 3 / 6 |
| `REQ-WK-012` | The 2015 MacBook SHALL receive `QUALIFIED_FOR_BOUNDED_ROLE`, `QUALIFIED_OUT`, or `BLOCKED_PENDING_EVIDENCE` without a sunk-cost exception. | I,A,R | Architecture owner | Phase 3 / 6 |

## Observer and telemetry

| ID | Normative requirement | Acceptance | Evidence owner | Earliest proof |
|---|---|---|---|---|
| `REQ-OBS-001` | The Observer SHALL be local, read-only, least privilege, and unable to remediate, dispatch, promote, approve, or widen access. | I,T,R | Observer / Security owner | Phase 4 |
| `REQ-OBS-002` | Every collected field SHALL map to a named operational decision, acceptance claim, or collector self-health need and SHALL be minimum necessary for that purpose. | I,A,R | Data owner | Phase 3 / 4 |
| `REQ-OBS-003` | Telemetry SHALL use a versioned schema, pseudonymous purpose-bound identifiers, explicit provenance, and defined clock-quality semantics. | I,T | Observer owner | Phase 4 |
| `REQ-OBS-004` | Telemetry SHALL exclude file contents, private filenames, prompts, credentials, tokens, recovery keys, raw/full serials, user-content payloads, and PRIVATE VAULT data. | I,T,R | Security owner | Phase 4 |
| `REQ-OBS-005` | The Observer SHALL report only validated meanings for role freshness, job state, bounded resource/capacity signals, storage presence/state, backup/restore recency, and configuration generation. | I,T,D | Observer / Role owner | Phase 5 / 6 |
| `REQ-OBS-006` | Missing, stale, dropped, schema-incompatible, or collector-unavailable data SHALL produce `UNKNOWN` or `TELEMETRY_UNAVAILABLE`, never implicit health. | T,D | Observer owner | Phase 4 / 6 |
| `REQ-OBS-007` | The Observer SHALL expose its own last successful collection, heartbeat, dropped-record count, schema version, clock quality, and failure status. | I,T,D | Observer owner | Phase 4 / 6 |
| `REQ-OBS-008` | Sampling, aggregation, retention, deletion, and alert timing SHALL conform to Taylor's accepted policy and SHALL have verifiable deletion or archival behavior. | I,A,T | Data / Observer owner | Phase 4 / 6 |
| `REQ-OBS-009` | Every alert SHALL identify the condition, affected role, evidence freshness, expected human action, timing, and safe-degradation or stop response. | I,T,D | Operations owner | Phase 5 / 6 |
| `REQ-OBS-010` | Observer acceptance SHALL cover permission denial, stale data, collector failure, clock skew, schema mismatch, dropped records, and alert-delivery failure; using OpenTelemetry SHALL not itself count as acceptance. | T,D,R | Observer / Assurance owner | Phase 6 |

## Operations, maintenance, and retirement

| ID | Normative requirement | Acceptance | Evidence owner | Earliest proof |
|---|---|---|---|---|
| `REQ-OPS-001` | Every accepted data flow and placement SHALL carry both a confidentiality class and recoverability class; `UNKNOWN` SHALL block new placement or promotion. | I,T | Data owner | Phase 3 / 5 |
| `REQ-OPS-002` | RPO, RTO, exposure, retention, patch/support, replacement, and residual-risk values SHALL be explicitly accepted by Taylor rather than inferred from customary numbers. | I,R | Taylor | Phase 1 |
| `REQ-OPS-003` | Every applicable fault SHALL define detection, containment, allowed Safe Degradation, recovery, evidence, escalation, and resume authority. | I,A,T,R | Assurance owner | Phase 3 / 6 |
| `REQ-OPS-004` | Authority-bearing, destructive, privacy-sensitive, or ambiguous work SHALL stop and preserve evidence unless an explicit tested contract permits a safer bounded behavior. | I,T,D | Operations owner | Phase 6 |
| `REQ-OPS-005` | Patch and update operations SHALL use accepted priority windows, supported sources, maintenance preconditions, pre-update recovery, verification, rollback, and post-change identity records. | I,T,D | Maintenance owner | Phase 6 |
| `REQ-OPS-006` | Restore, Control Plane recovery, Worker rebuild, diagnostic, Observer self-health, capacity, update rollback, and retirement procedures SHALL be exercised on an accepted schedule. | I,T,D,R | Operations owner | Phase 6 / lifecycle |
| `REQ-OPS-007` | Every qualified role SHALL have support-sunset and retirement triggers plus an approved non-destructive plan for authoritative-copy confirmation, evidence retention, service disengagement, and later sanitization routing. | I,A,R | Lifecycle owner | Phase 3 / 7 |
| `REQ-OPS-008` | Incidents, discrepancies, failed tests, warnings, and deviations SHALL be recorded, dispositioned, retested where applicable, and retained with the affected release evidence. | I,T,R | Assurance owner | Phase 6 / 7 |

## Assurance and release

| ID | Normative requirement | Acceptance | Evidence owner | Earliest proof |
|---|---|---|---|---|
| `REQ-ASS-001` | Requirements SHALL be bidirectionally traceable to exact design/configuration artifacts, acceptance methods, tests, evidence, open discrepancies, and release claims. | I,T,R | Assurance owner | Phase 1 onward |
| `REQ-ASS-002` | Evidence SHALL identify the exact source/configuration generation, role, environment, target, procedure, result, and artifact identity under test. | I,T,R | Evidence owner | Phase 4 onward |
| `REQ-ASS-003` | Acceptance SHALL include static, positive, negative, security, failure-path, integration, and actual end-to-end evidence in proportion to the claim; lower-level and integrated tests SHALL NOT substitute for each other. | I,A,T,D,R | Assurance owner | Phase 6 |
| `REQ-ASS-004` | The completion Evidence Set SHALL be frozen with a complete manifest and cryptographic identities before independent review, and any material change SHALL invalidate or supersede the review. | I,T,R | Evidence custodian | Phase 7 |
| `REQ-ASS-005` | A deterministic DEGS evaluation SHALL be run against the exact fixed task record and evidence identities and SHALL be interpreted as a gate result, not truth or authority. | I,T,R | Governance owner | Phase 7 |
| `REQ-ASS-006` | An independent auditor SHALL review the Frozen Evidence Set without changing it, disclose actual reviewer/model identity, challenge sufficiency and traceability, disposition open issues, and require retest after correction. | I,R | Audit owner | Phase 7 |
| `REQ-ASS-007` | Critical unknowns or findings concerning recovery, privacy, security, data loss, source identity, or role fitness SHALL block a clean completion claim and SHALL NOT be waived by a gate, auditor, or Taylor acceptance. | I,T,R | Taylor / Assurance owner | Phase 7 / 8 |
| `REQ-ASS-008` | Only Taylor SHALL make the System Release Decision for the exact reviewed baseline after objective evidence, deterministic DEGS result, independent audit, and explicit bounded residual-risk review. | I,R | Taylor | Phase 8 |
