# Phase 3 Data and Signal Map

## Data-flow map

Every accepted flow carries both confidentiality and recoverability classes.
An `UNKNOWN` class blocks the flow. The following rows are architectural
contracts only; they do not prove an implementation or authorize placement.

| Flow ID | Source -> destination | Permitted object | Confidentiality / recoverability | Preconditions | Blocked cases |
|---|---|---|---|---|---|
| `FLOW-P3-001` | Taylor -> Control Plane | Explicit authority/value decision reference without secret value | `C1_PRIVATE_OPERATIONAL`; `R2_IMPORTANT` when release evidence | Exact scope, target, expiry if applicable, and human-only owner | Ambiguous authority, secret value, inferred permission, or residual-risk acceptance |
| `FLOW-P3-002` | Control Plane -> Worker | Immutable Job Envelope plus minimum approved input copy | `C0`-`C2`; `R0`/`R1`; non-sole-copy `R2` only when specifically approved | Qualified Worker, supported software, exact digests, expiry, job semantics, approved endpoint | `C3`, `CX`, `R3`, sole-copy `R2`, unknown class, broad credential, stale envelope |
| `FLOW-P3-003` | Worker -> Control Plane staging | Status, bounded evidence, Staged Output, integrity manifest | Input-compatible class; never authoritative until Promotion Event | Exact envelope and output identity; atomic staging; validation route | Partial handback, ambiguity, identity mismatch, prohibited data, direct canonical write |
| `FLOW-P3-004` | Control Plane -> authoritative target | One validated Staged Output through a Promotion Event | Exact accepted class; recoverability contract inherited and checked | Taylor-accepted policy, requirement-specific acceptance, recovery precondition, recorded event | Worker/Observer request, missing evidence, `RX_UNKNOWN`, source mismatch, partial replacement |
| `FLOW-P3-005` | Control Plane -> assigned Storage Role | Classified backup, archive, transfer, or scratch operation | Per selected Storage Role; never sole-copy `R2`/`R3` on Seagate | Qualified resource and role, exact source/copy relationship, capacity, integrity, retention, recovery contract | No assigned role, ambiguous device, unknown topology/class, content traversal outside contract |
| `FLOW-P3-006` | Roles -> Observer | Minimum necessary operational signal | `C1_PRIVATE_OPERATIONAL`; `R0_REPRODUCIBLE` except frozen release evidence | Versioned schema, pseudonymous IDs, field-to-decision mapping, read-only access | Contents, filenames, prompts, secrets, raw/full serials, user payloads, remediation channel |
| `FLOW-P3-007` | Observer -> Taylor/Control Plane view | Validated signal, freshness, clock quality, collector self-health | `C1_PRIVATE_OPERATIONAL`; `R0_REPRODUCIBLE` | Schema-compatible record with provenance | Silence as health, stale data as current, hidden loss, automated authority |
| `FLOW-P3-008` | Control Plane -> DEGS / auditor | Exact task record or Frozen Evidence Set | Minimum necessary class; release set may be `R2_IMPORTANT` | Fixed identity, privacy review, authorized read-only route | Mutable evidence, secrets, prohibited content, reviewer mutation, gate result treated as authority |

## Observer signal-to-decision map

These are the only candidate signal purposes admitted by Phase 3. Exact field
names, types, sampling, and thresholds remain Phase 4 work. A signal not mapped
here is prohibited until a new reviewed purpose is added.

| Signal purpose | Minimum value | Named decision or claim | Failure representation | Prohibited inference |
|---|---|---|---|---|
| Collector last success | Timestamp plus clock quality | Whether Observer evidence is fresh enough to use | `TELEMETRY_UNAVAILABLE` or `UNKNOWN` after the future accepted threshold | Overall role health |
| Collector heartbeat | Versioned liveness state | Whether the collector itself is available | `TELEMETRY_UNAVAILABLE` | Automatic restart authority |
| Dropped-record count | Bounded count for the interval | Whether an interval is complete enough for a claim | `UNKNOWN` for affected interval | Zero drops from silence |
| Schema version | Exact supported identifier | Whether a record can be interpreted | Reject and report `UNKNOWN` | Silent field reinterpretation |
| Clock quality | Bounded quality/status | Whether ordering and recency claims are valid | `UNKNOWN` for time-dependent claims | Correct clock from plausible timestamps |
| Configuration generation | Cryptographic or exact version identifier | Whether observed and approved configuration agree | `UNKNOWN` or stop on mismatch | Fitness from version presence |
| Role freshness/state | Pseudonymous role ID, state, observed time | Whether the next dependent dispatch/promotion claim may proceed | `UNKNOWN` on missing/stale value | Authority to change the role |
| Job state | Job ID, bounded state, last transition | Reconcile open, completed, failed, cancelled, or ambiguous work | Explicit `AMBIGUOUS` when signals conflict | Retry or promotion safety without the Job Envelope |
| Bounded resource/capacity | Aggregate amount/threshold state without paths or names | Warn or stop before an accepted reserve is crossed | `UNKNOWN` when measurement/threshold is absent | Deletion or capacity remediation authority |
| Storage presence/role state | Pseudonymous resource/role ID and validated presence/state | Permit or block an operation dependent on that Storage Role | `UNKNOWN` / unavailable | Backup, integrity, or recovery fitness from presence |
| Backup/restore recency | Generation ID and verified event time only | Whether an accepted RPO/restore-evidence claim is current | `UNKNOWN` when source, generation, or verification is missing | Content completeness from timestamp alone |
| Alert presentation self-test | Synthetic alert ID, displayed time, outcome | Whether the human alert route works within accepted timing | `TELEMETRY_UNAVAILABLE` | That the originating condition is safe |

## Placement rules

- `C3_RESTRICTED_CONTENT`, `CX_EXCLUDED_SECRET`, and `R3_IRREPLACEABLE` are
  prohibited on the Worker; `C3` and `CX` are prohibited from Observer records.
- The Seagate may not become an authoritative or sole-copy home for `R2` or
  `R3`; the current copy topology is `UNKNOWN`.
- Observer raw permitted events may be retained for 30 days and daily
  aggregates for 180 days only after the Observer is implemented and the
  deletion/archive behavior is tested.
- Release/audit evidence follows its own evidence-retention policy and never
  inherits Observer telemetry deletion by accident.
- An unmapped flow, field, class, destination, or repurposing request is a hard
  stop requiring a new architecture generation and authority.

## DEAS evidence-record contract

- **Evidence ID:** `EV-P3-DATA-MAP`, `EV-P3-SIGNAL-DECISION-MAP`
- **Requirement/fault IDs:** `REQ-WK-003`, `REQ-OBS-002`, `REQ-OBS-005`, `REQ-OBS-008`, `REQ-OPS-001`, `REQ-ST-003`, `REQ-ST-011`, `FLT-OBS-001`, `FLT-OBS-004`, `FLT-OBS-005`
- **Claim under test:** Every admitted Phase 3 data flow carries both classification axes and every candidate Observer signal maps to a named decision while prohibited content and inferences remain excluded.
- **Acceptance method:** Inspection and analysis against the accepted classifications, exposure ceiling, retention decision, privacy boundary, requirements, and Phase 2 unknowns; later implementation tests remain required.
- **Exact source/configuration/role/device-safe identity/environment/target:** Frozen sources in `source-register.md`; flows `FLOW-P3-001` through `FLOW-P3-008`; candidate roles in `role-architecture.md`; private documentation environment only.
- **Procedure or command identity:** One bounded data-flow and purpose-minimization analysis checked by `validation/validate_phase3.py`; no collection or data movement command.
- **Start time:** 2026-09-05T19:24:10-05:00
- **End time:** 2026-09-05T20:34:39-05:00
- **Clock-quality basis:** Execution-host wall clock in America/Chicago with one-second display precision; no external time attestation.
- **Expected result:** Every flow has a source, destination, object, dual classification, precondition, and blocked case; every signal has one minimum value, purpose, failure representation, and prohibited inference.
- **Actual result:** Eight bounded flows and twelve candidate signal purposes are defined; unknown classes, prohibited data, missing freshness, and unmapped purposes fail closed.
- **Status:** DESIGN_DEFINED_NOT_IMPLEMENTED
- **Discrepancy references:** [Phase 2 discrepancies and unknowns](../../qualification/phase-2/discrepancies-and-unknowns.md) and [capacity unknowns](recovery-and-capacity-policy.md)
- **Artifact paths:** `contexts/operational-system/docs/program/v1/architecture/phase-3/data-and-signal-map.md`
- **Cryptographic identities:** Frozen by `phase-3-sha256.txt`; its non-circular SHA-256 is supplied by the external freeze record.
- **Evidence owner:** Codex in Taylor AI Workbench for package integrity; future data and Observer owners remain assigned by the requirements.
- **Human/physical action owner:** Taylor for any new authority, protected-content, credential, permission, or physical step; none occurred.
- **Confidentiality classification:** `C1_PRIVATE_OPERATIONAL`; PRIVATE PERSONAL USE - NOT FOR PUBLIC RELEASE
- **Recoverability classification:** `R0_REPRODUCIBLE` from the frozen sources and package manifest.
- **Limitations:** No schema, collector, storage placement, job flow, alert route, deletion behavior, or end-to-end data path is implemented or tested.
- **Unsupported inferences:** Data-placement approval, Observer fitness, Worker dispatch approval, backup coverage, privacy acceptance, qualification, release, or broader adoption.
- **Current freshness:** Current only for the frozen source identities; any class, flow, signal purpose, requirement, or authority change makes this record stale.
- **Supersession:** First Phase 3 data and signal map; supersedes no earlier Phase 3 artifact.
