# Phase 4 Software Core Handoff

- Package state: `READY_FOR_GIT_DELIVERY`
- Decision scope: `PACKAGE`
- System status: `NOT_YET_QUALIFIED`
- Release status: `NOT_YET_RELEASED`
- Controlled integration action: `NOT_PERFORMED`
- Conditional disposition after package, delivery, and review PASS:
  `NO_CONTROLLED_INTEGRATION_ACTION_SELECTED`
- External gates pending in immutable bytes: `G7`, `G8`, `G9`

## Exact result

The package defines two deep, synthetic-only Modules. Worker Core validates
one exact Job Envelope contract, performs one bounded synthetic transform, and
atomically stages an integrity-identified result as
`COMPLETED_UNACCEPTED`. Observer Core validates one minimized schema and exact
policy, produces decision-bound signals plus self-health, and fails closed to
`UNKNOWN` or `TELEMETRY_UNAVAILABLE`. Neither Module can promote, integrate,
qualify, release, remediate, dispatch to a device, or widen authority.

The 18 Phase 4 evidence identities, exact sources, fixture/configuration
digests, public tests, task record, validation report, and 24 non-manifest
paths are bound by [phase-4-sha256.txt](phase-4-sha256.txt). The manifest's own
SHA-256, Git commit, pushed ref, draft PR, unchanged base, and independent
review decisions are intentionally bound by external delivery records after
freeze; this handoff does not predict them.

The first candidate commit
`c365171e3ae7aff184d5e2ade5ec470365765009`, tree
`d66364645ab9a173a7ed4fe8b99b8c9cb4bda154`, and manifest SHA-256
`6a50cbbdb713338dc61bc51840b5b7a40c0997029aa1905f6fae2e55624ca25c`
remain an immutable rejected predecessor. Both initial independent reviews
failed it. This handoff describes the correction generation only; final
external records must bind its new commit, tree, manifest, and fresh reviews.

## Historical evidence disposition

The initial failed Worker job remains `FAILED_UNACCEPTED_NO_RETRY`. The
corrected Worker job remains `HAND_BACK_VERIFIED_COMPLETED_UNACCEPTED`, and its
acceptance package remains `COMPLETED_UNACCEPTED` with promotion
`NOT_PERFORMED`. They informed the Phase 4 fault and state contracts but were
not modified, copied, re-executed, relabeled, or treated as Phase 4 evidence.
Exact identities are in [source-register.md](source-register.md).

## What passed and what remains future

The final immutable package is intended to record successful Python compile,
48 Module tests, package-validator positive/negative/failure cases, exact
fixtures, source identities, evidence contracts, traceability, links, size and
function bounds, manifest, diff hygiene, secret scan, DEGS validation and
evaluation. External delivery and review records determine G7 and G8. Taylor
alone may accept the exact result at G9.

These results do not test an actual Control Plane/Worker transport, device,
collector, service, persistent registry, process termination, Promotion Event,
alert path, retention deletion/archive, recovery, or end-to-end workflow.
Phase 5 integration and Phase 6 qualification evidence remain future. A gate,
handoff, review, or `NO_CONTROLLED_INTEGRATION_ACTION_SELECTED` disposition
does not authorize them.

## Next decision

After exact external identity binding and independent review, present the
commit, tree, manifest digest, pushed ref, draft PR head, and review records to
Taylor for G9 acceptance. Do not merge without separate exact merge authority.
Do not initiate a controlled integration action when all Phase 4 checks pass.
If any check fails, preserve the candidate and create a correction generation
within the same frozen surface or stop for new authority if the surface would
change.

## Safe stop and rollback

Preserve the complete-history bundle SHA-256
`5b8ef9cb0b2076be7a791070757a1f2a006937af4d9a1eaee3f0369e3b127abc`,
the isolated branch, external red/green/review records, immutable candidate,
and any non-force private remote checkpoint. Do not amend, reset, rebase,
force-push, delete, merge, operate a device, promote output, or erase a failed
generation automatically. Restoration or later execution requires an exact,
identity-checked, separately scoped action.
