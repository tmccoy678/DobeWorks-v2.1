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
failed it. Generation 2 commit
`a9f11d8d92d3b3ae1b04d80e3ef9de31233f4c4c`, tree
`ce78377371ec994721a67ca1880f1a5e313181d2`, and manifest SHA-256
`fc4c7d13d6e06529dff8fb10a67d2f35ab1a2502d26877c3a8c2a476ea6c788c`
also remain an immutable rejected predecessor after both fresh reviews failed.
Generation 3 commit `6a989b8807c376e45b6345da54d6603d495ad3cd`,
tree `3a3be3bb029dac9917d7f1028423822e15960629`, and manifest SHA-256
`15855832d880abcfd0945ba9b251610ce29448ea7139d090689005f875db9a8e`
remain a third immutable rejected predecessor after both fresh reviews failed.
Generation 4 commit `4cb086fbc1f22fe4b8c2a920f20af5ad0c3b4a9b`,
tree `b8f7cf5bb4c05a23afa5543bfb74fac0133af81f`, and manifest SHA-256
`e8853c87b362220965f9c937afc978bf62b9c4721d4d9943718ee419540b8837`
remain a fourth immutable rejected predecessor after both fresh reviews failed.
Generation 5 commit `e81ad8f97bff79bed0ae44ad14a170b3f0c8c403`,
tree `120e38752e198fd3408d0fc5279b11ee2655af40`, and manifest SHA-256
`00de173d50c2ab59d9037cb18e10d56fb53db600d7ab27066999be2255807001`
remain a fifth immutable rejected predecessor after both fresh reviews failed.
Generation 6 commit `d41338a762e221c8a72d8ee5ce30a7ee23664f3b`,
tree `2b8954c57c4e604ac9ff0057dd3a6e3ed18ea82a`, and manifest SHA-256
`483234342271123a6b185bd1da892ce43b020cb5067a7e85db3ea5c01250b8b9`
remain a sixth immutable rejected predecessor after both fresh reviews failed.
This handoff describes Generation 7 only; final external records must bind its
new commit, tree, manifest, and fresh reviews.

## Historical evidence disposition

The initial failed Worker job remains `FAILED_UNACCEPTED_NO_RETRY`. The
corrected Worker job remains `HAND_BACK_VERIFIED_COMPLETED_UNACCEPTED`, and its
acceptance package remains `COMPLETED_UNACCEPTED` with promotion
`NOT_PERFORMED`. They informed the Phase 4 fault and state contracts but were
not modified, copied, re-executed, relabeled, or treated as Phase 4 evidence.
Exact identities are in [source-register.md](source-register.md).

## What passed and what remains future

The final immutable package is intended to record successful Python compile,
69 Module tests, 32 package-validator positive/negative/failure cases, exact
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
