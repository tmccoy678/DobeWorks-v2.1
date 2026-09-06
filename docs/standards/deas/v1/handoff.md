# DEAS v1.0 Definition-Correction Handoff

- Task: DEGS-T1-DW-ENGINEERING-ASSURANCE-V1-CORRECT-20260905
- State: READY_FOR_GIT_DELIVERY
- Decision scope: PACKAGE
- External gates pending in this package: G7, G8, G9
- Candidate baseline: C3 `47b32aeeb107584291f69ba90b11706c7cf3eae0` plus exactly the 10 correction paths bound by `deas-v1-sha256.txt`
- Branch: deas/v1-phase2-generation-2
- Draft pull request: 1
- Phase 2 Generation 1: EXPECTED_NONCONFORMING
- Phase 2 Generation 2: AUTHORIZED_SUSPENDED_UNTIL_CORRECTION_DELIVERY
- Merge: NOT_AUTHORIZED

## What the correction establishes

The standard, enforcement matrix, C4 plan, definition task, evidence record,
and public DEAS validator now use one lifecycle:

- immutable task state remains `READY_FOR_EXECUTION`;
- immutable handoff state remains `READY_FOR_GIT_DELIVERY`;
- embedded independent-review and post-action-validation states remain
  `PENDING`;
- deterministic validator PASS is explicitly scoped to `PACKAGE` and names
  G7/G8/G9 as pending; and
- external control-plane evidence binds review, acceptance, commit, pushed ref,
  and draft-PR identities without rewriting reviewed bytes.

The public suite has 28 passing cases, including three independent lifecycle
mutations, unfrozen-DEGS-gate rejection, and structured argument/runtime error
paths. The exact canonical engineering-gate digest is verified before and after
each Generation 2 DEGS execution. The
definition validator preserves three profiles, six overlays, ten preventive
invariants, the exact six-finding Generation 1 regression, and the sorted
13-artifact definition manifest. The package validation report records the
exact commands, exits, hashes, warnings, and safe stop.

## External review and delivery

Canonical bytes do not claim their independent review or Git delivery already
passed. The external review index at workspace-relative
`.scratch/dobeworks-deas-v1-definition-correction/review/final-review-index.md`
must bind the exact manifest-file SHA-256 and both no-blocker review decisions
before commit. After the authorized non-force commit and push, external
delivery evidence must verify local HEAD, remote branch head, draft PR 1 head,
unchanged `main`, and unmerged state before G7 closes.

## C4 resumption boundary

Taylor separately authorized the exact C4 work unit and explicitly authorized
its resumption after this correction is refrozen and delivered. Resume C4 only
after the correction commit and remote identity agree. Rebind C4 to that
correction predecessor, preserve its 15-path allowlist and pre-correction patch
identity, apply the corrected package lifecycle, rerun all required checks, and
obtain fresh external Standards and Spec reviews before its own delivery.

This handoff does not authorize merge, main mutation, release, Phase 3, Role
Disposition, qualification, exception, root adoption, device/storage work,
credential/permission work, physical action, destructive action, repository
settings, collaborators, or unrelated work. Stop on drift, extra paths,
manifest disagreement, review blocker, authentication interaction,
non-fast-forward push, or any need for wider authority. Preserve C3, the
verified complete-history bundle, the exact pre-correction C4 patch, the
candidate, and review evidence; do not amend, reset, rebase, force-push,
delete, or merge automatically.
