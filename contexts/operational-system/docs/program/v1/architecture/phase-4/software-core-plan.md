# Phase 4 Software Core with Synthetic Fixtures

## Package decision

Phase 4 implements and tests two deep Modules against synthetic fixtures:
Worker Core and Observer Core. It converts the Phase 3 interface design into
bounded executable policy without creating an actual Control Plane, deploying
to a Worker, collecting real telemetry, or integrating roles. The result is
software-core evidence only.

The exact work unit, authority, 25-path surface, sources, exclusions, gates,
and rollback are frozen in the external Phase 4 specification identified in
[source-register.md](source-register.md). This package remains
`NOT_YET_QUALIFIED` and `NOT_YET_RELEASED`.

Generation 1 (`c365171e3ae7aff184d5e2ade5ec470365765009`) is a preserved,
independently rejected predecessor. This correction generation retains the
same interface and 25-path boundary while closing its clean-commit validator,
bounded-diagnostic, filesystem-failure, timeout, provenance, and evidence-path
defects. It makes no retroactive PASS claim for Generation 1.

## Architecture

### Worker Core Module

The Module hides Job Envelope parsing, policy validation, input validation,
duplicate identity memory, the synthetic runner, state transitions, Staged
Output layout, and atomic handback behind `WorkerCore.execute`. Constructor
injection supplies only the approved configuration digest, allowed input root,
finite byte bounds, and a bounded runner adapter. This is a deep Module: the
caller does not reimplement authority, expiry, retry, ambiguity, integrity, or
promotion policy.

Invariant state flow:

```text
received
  -> rejected | cancelled-before-execution
  -> validated -> one-attempt-running
  -> failed | ambiguous | completed-unaccepted
completed-unaccepted -> staged handback only
staged handback -/-> promotion
```

| Condition | Deterministic state | Mutation |
|---|---|---|
| malformed, stale, mismatched, unsafe, or duplicate destination | `REJECTED_*` | none |
| identical already-observed envelope | `DUPLICATE_NO_EXECUTION` | none |
| changed envelope reusing job ID | `REJECTED_JOB_ID_REUSE` | none |
| pre-execution cancellation | `CANCELLED_BEFORE_EXECUTION` | none |
| timeout or unavailable dependency | `FAILED_*` | failure evidence in partial staging only |
| interruption, communication loss, or cancellation race | `AMBIGUOUS_*` | preserved partial staging only |
| invalid, oversized, or digest-mismatched result | `FAILED_OUTPUT_*` | preserved partial staging only |
| exact valid result | `COMPLETED_UNACCEPTED` | atomic rename to job-named Staged Output |

Every returned state fixes `promotion` to `NOT_PERFORMED` and `retry` to
`PROHIBITED_AUTOMATIC`. A successful process exit is not an accepted result.
The synthetic default runner has bounded iteration and no external I/O.
The core enforces the 1..30 second envelope deadline for its in-process runner
with the host's main-thread interval timer and fails closed when that facility
is unavailable or already occupied. Separate-process termination, restart,
persistent deduplication, dispatch, and Promotion Events remain later
integration/qualification concerns.

### Observer Core Module

The Module hides schema enforcement, privacy traversal, policy identity,
signal validation, signal-to-decision mapping, clock/freshness reasoning,
collector self-health, provenance, and retention boundaries behind
`ObserverCore.collect` and `ObserverCore.retention_decision`. Callers cannot
obtain an implicit healthy value from invalid evidence or ask the Module to
take action.

| Input state | Record state | Signal meaning |
|---|---|---|
| exact schema, fresh exact clock, collector OK, no drops, complete signals | `VALIDATED` | validated synthetic values |
| stale or collector failed | `TELEMETRY_UNAVAILABLE` | every signal `UNKNOWN` |
| clock uncertain, records dropped, or signal missing | `UNKNOWN` | every signal `UNKNOWN` |
| incompatible schema, prohibited data, invalid policy/path/value | rejection | no record |

The six allowed signals map one-to-one to named decision purposes. They carry
no file content, private filename, prompt, credential, token, recovery key,
full serial, user-content payload, or PRIVATE VAULT data. Self-health includes
last success, heartbeat, dropped-record count, schema, clock quality, and
failure status. `retention_decision` implements accepted 30-day and 180-day
expiry thresholds but has no deletion interface.

## Job contract

The only Phase 4 job class is `synthetic_repository_inventory`.

| Contract concern | Frozen behavior |
|---|---|
| Omission | A missing field, input, record, or expected digest rejects before execution; missing Observer signal becomes explicit `UNKNOWN` |
| Duplication | Identical observed job identity deduplicates without execution; semantic reuse rejects |
| Delivery intent | `ANALYSIS_ONLY` |
| Idempotency | `IDEMPOTENT` for the pure synthetic transform; no general job-class inference |
| Side effects | New files under one caller-provided disposable staging root only |
| Retry/backoff | zero retries; no backoff because automatic retry is prohibited |
| Interruption | preserve partial staging and report `AMBIGUOUS_INTERRUPTED` |
| Timeout | envelope value 1..30 seconds; Worker-enforced in-process deadline; no retry or promotion |
| Cancellation | before execution: no mutation; race: preserve partial result and report ambiguity |
| Stale job | expired envelope rejects before execution |
| Checkpoint | `NONE`; partial staging is evidence, not a resumable checkpoint |
| Output handback | exact result digest and manifest inside an atomically renamed staging directory |
| Acceptance/promotion | always external; Worker reports `COMPLETED_UNACCEPTED` only |

## Requirement and fault boundary

Synthetic evidence covers the software-core acceptance methods for
`REQ-CP-004`, `REQ-CP-009`, `REQ-WK-004` through `REQ-WK-009`,
`REQ-OBS-001` through `REQ-OBS-004`, `REQ-OBS-006` through `REQ-OBS-008`,
and `REQ-ASS-002`. It tests the Phase 4 behavior assigned to `FLT-WK-004`,
`FLT-JOB-001` through `FLT-JOB-008`, `FLT-OBS-001` through `FLT-OBS-005`,
`FLT-NET-001`, `FLT-NET-002`, `FLT-SUP-001`, and `FLT-SUP-002`.

This does not satisfy later `D` or `R` methods, actual-system integration,
device recovery/rebuild, service exposure, alert delivery, persistent state,
or end-to-end behavior. Those remain future and cannot be inferred from unit
tests or a DEGS result.

## Preventive controls

- Inputs, output paths, schemas, sizes, records, signals, time values, retries,
  attempts, traversed nodes, function size, and package paths are finite.
- JSON duplicate keys and extra fields fail closed.
- Resolved inputs must be regular non-symlink files below an explicit allowed
  root; Staged Output uses a non-symlink existing directory.
- The Worker/Observer Modules import no network client or subprocess facility.
- Python 3.9.6 standard library is the complete dependency set; no package
  resolution, download, or update occurs.
- Exact fixtures and expected bytes make nondeterminism observable.
- The public validator independently runs Module tests, verifies sources,
  evidence contracts, lifecycle semantics, code bounds, links, path allowlist,
  and the manifest. Its filesystem walk, child output, child time, and Git
  identity output are explicitly bounded; unexpected test diagnostics fail.
- Independent Standards and Spec reviewers examine the frozen identity outside
  the immutable package.

## Gates and disposition

G0 through G6 may be evidenced inside the immutable package. G7 delivery, G8
independent review, and G9 human acceptance are external. The package task
therefore remains `READY_FOR_EXECUTION`, embedded review/post-action fields
remain `PENDING`, and the handoff remains `READY_FOR_GIT_DELIVERY`.

If package validation, identity delivery, and both independent reviews pass,
the Phase 4 control-plane disposition is
`NO_CONTROLLED_INTEGRATION_ACTION_SELECTED`. This means no controlled
integration action is warranted or performed under this work unit. It does
not mean actual integration passed, and it does not authorize Phase 5, merge,
qualification, or release.
