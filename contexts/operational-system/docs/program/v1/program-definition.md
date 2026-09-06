# DobeWorks hardware/software v1 — Phase 1 Program Definition

- **Status:** `PHASE_1_BASELINE_ACCEPTED`
- **System status:** `NOT_YET_QUALIFIED`, `NOT_YET_RELEASED`
- **Phase:** 1 of 8 — Program Definition
- **Current governed package:** Phase 3 architecture and Role Dispositions,
  [frozen separately](architecture/phase-3/handoff.md)
- **Authority lane:** `TAYLOR_AI_WORKBENCH`
- **DEGS risk tier:** `TIER_1`
- **Canonical home:** `projects/dobeworks/contexts/operational-system/`
- **Canonical promotion:** completed as a separately authorized Tier 1 documentation task

## Outcome

Phase 1 defines the mission and lifecycle claim that later phases must prove. Canonical promotion establishes the accepted documentation source of truth only; it does not qualify a device, inspect protected content, implement software, deploy telemetry, modify storage, or authorize Phase 2.

The program is successful only if DobeWorks hardware/software v1 can support Taylor's private engineering work through explicit operational roles whose mission, authority, data, failure, recovery, maintenance, and retirement contracts are backed by objective evidence from the integrated system.

## Decision status

### Previously accepted and carried forward

- Completion is an integrated mission-and-lifecycle claim, not component presence or a one-time diagnostic result.
- The current Mac is the proposed authoritative Control Plane.
- The Seagate may receive only explicitly classified, non-sole-copy Storage Roles.
- The 2015 MacBook is a provisional Worker candidate with no sunk-cost exception.
- Worker jobs require explicit omission, duplication, idempotency, retry, interruption, timeout, cancellation, side-effect, and atomic handback semantics.
- Worker output remains Staged Output until an authorized Control Plane Promotion Event.
- The Observer is local, minimal, versioned, read-only, purpose-bound, retention-bounded, secret-free, self-observing, and unable to remediate.
- Important data may not exist only on the Seagate or Worker.
- Device disposition is one of `QUALIFIED_FOR_BOUNDED_ROLE`, `QUALIFIED_OUT`, or `BLOCKED_PENDING_EVIDENCE`.
- Destructive storage, backup, partition, sanitization, or wipe work is outside v1 qualification and requires a separate Tier 3 cutover.
- Completion follows `objective evidence -> deterministic DEGS result -> independent audit of fixed evidence -> Taylor's explicit acceptance`.

### Accepted by Taylor for the Phase 1 baseline

- The Operational System becomes a distinct bounded context inside the existing private DobeWorks repository at `projects/dobeworks/contexts/operational-system/`.
- A DobeWorks `CONTEXT-MAP.md` makes the existing root context, the new Operational System context, and their interfaces explicit.
- The cross-context decision is recorded as DobeWorks ADR 0013; context-specific operational ADRs live inside the new context.
- The quantitative and human-value policies in `open-decisions.md` were explicitly accepted on 2026-09-01. They govern later requirements but do not authorize later work or constitute residual-risk acceptance for an unbuilt system.

## Ownership and sources of truth

| Concern | Owner and canonical source | Operational System relationship |
|---|---|---|
| DobeWorks name, Private Use, identity, mark, and provenance | `projects/dobeworks/CONTEXT.md` and `projects/dobeworks/docs/adr/**` | Reference only; do not redefine |
| Operational mission, roles, requirements, configuration, evidence, recovery, maintenance, retirement | `projects/dobeworks/contexts/operational-system/**` | Own directly |
| Workbench and Command Center routing/control-plane vocabulary | AI-Workspace root domain documentation | External interface; the Operational System's Control Plane is a system role, not Command Center |
| DEGS policy, schemas, gates, risk tiers, lanes, and lifecycle | `governance/**` | External governance source; never copied as local policy |
| Current phase boundary | `handoffs/current-context.md` plus schema-v2 checkpoint | Read/verify/route input only |
| Historical device measurements and proposals | August 30 audit and optimization plan | Planning context only; refresh before qualification evidence |
| Frozen Phase 1 source evidence | Source package identity recorded in `provenance.md` | Noncanonical evidence of the accepted source and promotion |

No controlled state may have two active sources of truth. The validated canonical promotion recorded each staged source and transformation; the paths above now own the accepted program baseline while the frozen scratch package remains evidence only.

## Mission

Provide Taylor with a private, recoverable, evidence-backed operational foundation for DobeWorks engineering work in which:

1. a Taylor-supervised Control Plane preserves authoritative configuration, dispatch, evidence, output promotion, and recovery orchestration;
2. each Storage Resource has a bounded role, protected-copy relationship, capacity policy, recovery proof, and retirement path;
3. an optional Worker performs only approved, rebuildable jobs without holding authority or sole-copy important data;
4. a local read-only Observer supplies minimal decision-relevant metadata and reports its own loss of visibility; and
5. the integrated system can fail, degrade, recover, update, and retire without silently widening authority or making unsupported completion claims.

## Concept of operations

### Normal operation

1. Taylor makes any required value, authorization, credential, physical-action, or residual-risk decision.
2. The Control Plane records the approved configuration generation and creates an immutable Job Envelope when Worker execution is appropriate.
3. The Worker validates envelope identity, expiry, data class, and supported job semantics before execution.
4. The Worker executes within its bounded role and returns Staged Output plus status and evidence; it does not alter authoritative state.
5. The Control Plane validates identity, integrity, semantics, and acceptance criteria. Only an authorized Promotion Event may accept the output.
6. The Observer records permitted operational metadata, freshness, and collector self-health. A missing or stale signal produces `UNKNOWN` or `TELEMETRY_UNAVAILABLE`.
7. Storage, backup, restore, patch, diagnostic, rebuild, and retirement work follows explicit plans, evidence requirements, stop conditions, and authority boundaries.

### Faulted operation

1. The affected role detects or receives a fault indication and preserves relevant evidence.
2. Authority-bearing, destructive, privacy-sensitive, or ambiguous work stops by default.
3. Replaceable computation may retry only when the Job Envelope explicitly makes repetition safe.
4. The system enters only a predefined Safe Degradation state; an unavailable role is never silently treated as healthy.
5. Recovery follows a role-specific procedure and produces evidence tied to the exact configuration and target.
6. The required human or system authority reviews the evidence before service resumes.

## System boundary

### In scope for v1 qualification

- the candidate current Mac in the Control Plane role;
- the Seagate and each separately identified logical Storage Role proposed for it;
- the exact 2015 MacBook if evaluated as a Worker candidate, including a valid qualify-out outcome;
- Control Plane and Worker software/configuration required for bounded job delivery and staged output handback;
- local Observer schema, collector, retention, self-health, and alert presentation;
- approved operational repositories, manifests, evidence, runbooks, recovery procedures, and release records;
- representative backup/restore, rebuild, update/rollback, safe-degradation, maintenance, and retirement rehearsals; and
- the human procedures and authority decisions required to operate the integrated system.

### External interfaces

- Taylor as decision owner and operator;
- Taylor AI Workbench as the supervised implementation lane;
- Command Center as a routing and independent-auditor access path, not the Observer;
- DEGS as a deterministic evidence-record evaluator, not execution or truth authority;
- approved operating-system, package, repository, update, diagnostic, and time sources;
- replacement hardware or independent backup destinations selected in later authorized phases; and
- the existing DobeWorks identity/provenance context.

### Out of scope

- Public Release, organizational adoption, commercial operation, external users, or public services;
- PRIVATE VAULT contents or any agent access to them;
- storing credentials, tokens, recovery keys, private identifiers, or full serial numbers in artifacts or telemetry;
- autonomous remediation, unattended destructive action, worker self-promotion, or agent self-approval;
- deletion or consolidation of backups, repartitioning, reformatting, sanitization, erasure, or device wipe during v1 qualification;
- guaranteeing high availability, disaster recovery across every Taylor-controlled system, or universal backup coverage outside classified DobeWorks data;
- assuming the Seagate is a backup, the 2015 MacBook is fit, or historical measurements remain current; and
- claiming certification, compliance, SLSA level, safety-critical suitability, or professional assurance.

## Roles and current disposition

| Role or asset | Mission contract | Allowed authority/data | Current status |
|---|---|---|---|
| Taylor | Make value judgments; authorize phases, credentials, physical actions, destructive work, exceptions, residual risk, and final release | Human-only decisions and protected actions | `OWNER`; Phase 3 definition/freeze authorized; downstream action remains separate |
| Candidate current Mac | Proposed Control Plane and authoritative operational state | Approved private work products, configuration, evidence, dispatch, validation, promotion, recovery orchestration | `BLOCKED_PENDING_EVIDENCE`; Phase 3 disposition review pending |
| Seagate Portable Drive | Candidate Storage Resource for separately classified roles | No sole-copy important data; no role until topology, redundancy, capacity, integrity, restore, and retirement evidence exist | `BLOCKED_PENDING_EVIDENCE`; Phase 3 disposition review pending; contents not inspected |
| Candidate 2015 MacBook | Optional rebuildable Worker | Replaceable tooling, approved inputs, caches, job metadata, temporary artifacts; no authority or sole-copy important data | `BLOCKED_PENDING_EVIDENCE`; Phase 3 disposition review pending; exact device facts `UNKNOWN` |
| Worker software | Validate Job Envelopes, execute bounded job classes, stage output and status | Job-specific minimum data and privileges | `BLOCKED_PENDING_EVIDENCE`; Phase 3 disposition review pending; not implemented |
| Observer | Report local, minimal, read-only operational metadata and self-health | Permitted metadata only; no content, secrets, private names, remediation, or promotion | `BLOCKED_PENDING_EVIDENCE`; Phase 3 disposition review pending; not implemented |
| DEGS gate | Evaluate the form and recorded status of task evidence | Read defined task records; no execution, approval, or truth claim | External canonical system, policy 1.1.0 `ACTIVE` |
| Independent auditor | Challenge sufficiency, traceability, independence, and open issues in a Frozen Evidence Set | Read fixed evidence only; no mutation or residual-risk acceptance | Planned for completion review; readiness time-sensitive |

## Trust boundaries and stable interfaces

| Boundary | Permitted interface | Prohibited shortcut |
|---|---|---|
| Taylor ↔ Control Plane | Explicit authorizations, value decisions, physical/credential actions, and acceptance records | Inferring approval from a gate, handoff, status, or convenience |
| Control Plane ↔ Worker | Immutable Job Envelope in; status, evidence, and Staged Output out | Shared authoritative state, broad credentials, worker self-promotion |
| Control Plane ↔ Storage Resource | Classified role contract, controlled read/write operation, integrity and restore evidence | Treating mount state, diagnostic pass, or free-space number as recoverability |
| Observer ↔ Roles | Read-only, versioned, minimum-necessary metadata collection | Remediation, content capture, private filenames, secret values, silent health on missing data |
| Operational System ↔ Workbench/Command Center | Phase routing, supervised implementation, audit routing | Redefining Command Center state as hardware telemetry |
| Operational System ↔ DEGS | Versioned task records and evidence paths | Treating gate PASS as execution authority or sufficient proof |
| Operational System ↔ DobeWorks root context | Explicit context map and cross-context references | Renaming DobeWorks or absorbing identity/provenance terms |

## Data classification

Confidentiality and recoverability are separate axes. Every accepted data flow must carry both classifications; `UNKNOWN` blocks promotion into a new role.

### Confidentiality

| Class | Meaning | Examples | Worker | Observer |
|---|---|---|---|---|
| `C0_PUBLIC_REFERENCE` | Publicly available, non-secret input retained for provenance | Public documentation, open-source dependency metadata | Job-specific copy allowed | Source identity only if needed |
| `C1_PRIVATE_OPERATIONAL` | Private metadata needed to operate or prove the system | Pseudonymous role IDs, configuration hashes, job status, capacity measurements | Minimum necessary | Primary permitted class |
| `C2_PRIVATE_WORK_PRODUCT` | Taylor's private engineering source or output | Repositories, research drafts, generated artifacts | Only for an approved job; staged and replaceable copy | Content prohibited |
| `C3_RESTRICTED_CONTENT` | Sensitive personal or backup-related content whose disclosure would materially harm privacy | Private filenames, backup listings, personal files, source portraits, account metadata | Denied by default in v1 | Prohibited |
| `CX_EXCLUDED_SECRET` | Secret values or isolation boundaries outside agent/system artifacts | Credentials, tokens, recovery keys, full serials, PRIVATE VAULT | Prohibited | Prohibited |

### Recoverability

| Class | Meaning | Placement rule |
|---|---|---|
| `R0_REPRODUCIBLE` | Recreated deterministically from an approved source | May be cached on Worker; no backup claim required if rebuild is proven |
| `R1_REPLACEABLE_WITH_COST` | Recreated with bounded time or compute but not byte-identical by default | May be staged on Worker; promotion requires acceptance criteria |
| `R2_IMPORTANT` | Loss would materially disrupt DobeWorks work or evidence | Never sole-copy on Worker or Seagate; mapped backup and restore evidence required |
| `R3_IRREPLACEABLE` | Loss cannot be acceptably recreated | Two independently protected copies before source retirement; no Worker placement by default |
| `RX_UNKNOWN` | Recoverability value or copy topology has not been established | No deletion, migration, sole-copy placement, or clean completion claim |

## Authority map

| Decision or action | Taylor | Workbench agent | Control Plane role | Worker | Observer | DEGS | Auditor |
|---|---:|---:|---:|---:|---:|---:|---:|
| Define requirements and propose design | A | E | C | — | — | C | C |
| Accept RPO/RTO, exposure, retention, support, replacement, residual risk | A | P | — | — | — | — | C |
| Access credentials or authenticate | A/E | — | Reference dependency only | — | — | — | — |
| Perform physical action or grant macOS permission | A/E | — | — | — | — | — | — |
| Dispatch an approved job | A for policy | E within approved config | E | Receive | Observe | — | — |
| Validate and promote Worker output | A for policy/exception | Assist | E within approved config | — | Observe | Evaluate evidence record only | Review fixed evidence |
| Remediate automatically | — | — | — | — | Prohibited | — | — |
| Approve destructive action | A, separate Tier 3 | — | — | — | — | Validate record only | Review |
| Declare System Release | A | — | — | — | — | Prior deterministic result | Prior independent audit |

Legend: `A` accountable human authority, `E` executes within explicit authority, `P` proposes, `C` contributes or checks, `—` no authority.

## Lifecycle policy baseline

### Control Plane

- Maintain a privacy-safe inventory, approved configuration generation, authoritative-data map, source and dependency identities, last known-good state, and recovery procedure.
- Bind every release, test, and handoff to the same exact source/configuration/artifact identities.
- Permit no automatic phase promotion, policy exception, destructive act, credential act, or residual-risk acceptance.
- Qualify through clean bootstrap, representative work, restart, loss, rebuild, and known-state recovery evidence.

### Storage and recovery

- Assign each logical volume one or more explicit, non-conflicting Storage Roles with authoritative-source, copy, confidentiality, recoverability, retention, capacity, integrity, restore, and retirement contracts.
- Treat every current Seagate backup identity, topology, per-set cost, redundancy, recoverability, and deletion candidate as `UNKNOWN` until authorized evidence establishes it.
- Require representative restore to a controlled destination plus byte-level and semantic verification appropriate to the data.
- Prohibit important data from existing only on the Seagate or Worker.
- Separate any future destructive migration or sanitization into a Tier 3 cutover.

### Worker and output promotion

- Define each allowed job class before use, including omission, duplication, delivery intent, idempotency, retry/backoff, interruption, timeout, cancellation, stale-job, checkpoint, side-effect, and atomic handback behavior.
- Use immutable job IDs and input/configuration digests; reject semantic reuse of an ID with different inputs.
- Keep Worker state rebuildable and non-authoritative.
- Hold every result as Staged Output until an evidenced Promotion Event validates exact identity, completeness, integrity, semantics, and acceptance criteria.
- An ambiguous completion state blocks automatic retry unless the job contract proves retry safety.

### Observer

- Collect only fields mapped to a named decision or required evidence claim.
- Remain local, read-only, secret-free, content-free, versioned, retention-bounded, and least privilege.
- Report schema version, clock quality, last successful collection, dropped records, and collector health.
- Represent missing/stale data as `UNKNOWN` or `TELEMETRY_UNAVAILABLE`; never infer health from silence.
- Add logs or traces only when a named failure question cannot be answered with smaller metadata.

### Updates, maintenance, and support

- Record supported update sources, priority, preconditions, maintenance window, pre-update recovery state, test, verification, rollback, and resulting configuration generation.
- Exercise restore, Worker rebuild, diagnostics, Observer self-health, capacity review, and fault response on a Taylor-accepted schedule.
- Suspend an exposed role when required security support, rollback, or safe-degradation evidence is absent.
- Treat numerical patch windows, reserve thresholds, exercise cadence, and support-sunset conditions as Taylor decisions, not universal facts.

### Retirement

- Define retirement triggers before qualification, including support sunset, diagnostic failure, unstable power/thermal behavior, failed recovery/rebuild, insufficient workload fitness, unacceptable exposure, and uneconomic repair or replacement judgment.
- Plan authoritative-copy confirmation, restore verification, service/account disengagement, sanitization selection and validation, evidence retention, and final reuse/recycle disposition.
- Execute no wipe, erase, repartition, sanitization, or deletion under this program-definition authority.

## Requirements, evidence, and fault coverage

- Normative requirements are in `requirements.md`.
- Bidirectional requirements-to-evidence planning is in `traceability-matrix.md`.
- The complete accepted applicable fault set and planned tests are in `fault-test-matrix.md`.
- Evidence freezing, independent review, and completion chain are in `evidence-and-audit-plan.md`.
- Quantitative and human-value decisions are isolated in `open-decisions.md`.
- Phase 2 is governed by `phase-2-entry-criteria.md`; its C4-corrected evidence
  package is complete with unresolved gaps.
- Phase 3 architecture and candidate dispositions are defined in
  `architecture/phase-3/` and remain pending external review and delivery.
- Phase 4, device action, qualification, and System Release remain separate and
  are not authorized by the Phase 3 package.

## Phase 1 acceptance record

The Phase 1 baseline was accepted after:

1. Taylor resolved every identified value judgment required before Phase 2;
2. Taylor accepted the canonical home and context relationship;
3. requirements, traceability, fault coverage, evidence/audit plan, and Phase 2 criteria validated deterministically;
4. the Phase 1 DEGS record reached an evidence-backed passing result;
5. no canonical or out-of-scope mutation occurred during staging; and
6. the package was presented to Taylor and Phase 1 stopped without beginning Phase 2.

Canonical promotion occurred later under its own bounded authorization and does not change the Phase 1 system status.
