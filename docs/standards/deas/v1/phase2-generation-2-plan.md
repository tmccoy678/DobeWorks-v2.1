# Phase 2 Generation 2 Correction Plan

- State: AUTHORIZED_FOR_EXECUTION
- Definition predecessor: C3 `47b32aeeb107584291f69ba90b11706c7cf3eae0`
- Definition correction task: `DEGS-T1-DW-ENGINEERING-ASSURANCE-V1-CORRECT-20260905`
- Predecessor: Phase 2 Generation 1
- Predecessor commit: f45ae80c64a0aa8c723a5a58b4fbc7073682d349
- Predecessor 28-path manifest SHA-256: 9ed515ac90cc100bae3d3a3baa674d6c2a200f5e18b3da4d7b4daaf979ac8d77
- Planned commit message: docs: add Phase 2 Generation 2 conforming correction
- Exceptions permitted: none

This plan defines C4 and records that Taylor separately authorized its exact
execution on 2026-09-05. The later definition-correction authority reconciles
this plan with the accepted lifecycle rule and authorizes resumption after the
correction checkpoint is refrozen and verified. Neither authorization permits
merge or any excluded action.

## Exact C4 paths

Modify:

1. contexts/operational-system/docs/program/v1/traceability-matrix.md
2. contexts/operational-system/docs/program/v1/phase-2-entry-criteria.md
3. contexts/operational-system/docs/program/v1/qualification/phase-2/qualification-plan.md
4. contexts/operational-system/docs/program/v1/qualification/phase-2/source-register.md
5. contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/current-mac-baseline.md
6. contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/seagate-device-volume.md
7. contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/worker-candidate.md
8. contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/observer-surface.md
9. contexts/operational-system/docs/program/v1/qualification/phase-2/validation/validate_phase2.py
10. contexts/operational-system/docs/program/v1/qualification/phase-2/validation/validation-report.md
11. contexts/operational-system/docs/program/v1/qualification/phase-2/handoff.md
12. contexts/operational-system/docs/program/v1/qualification/phase-2/evidence-sha256.txt

Add:

13. contexts/operational-system/docs/program/v1/qualification/phase-2/generation-history.md
14. contexts/operational-system/docs/program/v1/qualification/phase-2/generation-2-sha256.txt
15. contexts/operational-system/docs/program/v1/qualification/phase-2/degs/phase2-generation-2-task.json

No other path is in scope.

## Exact transformations

### Traceability

- Replace the false global reservation for Phase 2 with exact produced artifact identities.
- Update only Phase 2-related rows whose evidence exists.
- Distinguish evidence produced, evidence with unresolved discrepancy, blocked evidence, and future evidence.
- Link every changed state to the Generation 2 task, manifest, validator result, and any open discrepancy.

### Entry history

- Evaluate each unchecked Phase 2 prerequisite against contemporaneous task, route, privacy, promotion, validation, and handoff evidence.
- Mark a prerequisite complete only when an exact artifact proves it.
- Record NOT RECORDED or UNKNOWN where contemporaneous proof is absent.
- Separate historical entry sufficiency from present authorization; neither the correction nor a checked box authorizes another phase.

### Consequential evidence records

Add one evidence-record-contract section to each of the four records. Each section SHALL implement every row of the single canonical table in [DEAS v1.0, Canonical evidence-record contract](standard.md#canonical-evidence-record-contract), using its exact required Markdown labels and one nonblank value per label. Use `UNKNOWN` or `NOT RECORDED` when the source does not establish a value; never use an empty value.

Every original observation line in each record SHALL remain byte-identical and in the same order. Additions may explain provenance and missing fields; they may not recollect evidence, normalize observations, infer a value, assign a Role Disposition, or convert UNKNOWN or NOT RECORDED into a fact.

### Generation records and validators

- Add generation-history.md to distinguish immutable Generation 1 from corrected Generation 2.
- Add the Generation 2 DEGS task as `DEGS-T1-DW-HWSW-P2-GENERATION-2-20260902` and a sorted generation-2-sha256.txt. The manifest SHALL contain exactly the other 14 C4 paths; its separately supplied SHA-256 binds the manifest itself and SHALL remain external to avoid a circular self-hash.
- Regenerate evidence-sha256.txt only for the active canonical package and record its predecessor.
- Refactor validate_phase2.py so every function contains no more than 60 logical code lines with no exception, then extend it to verify the evidence contract, traceability, entry history, original-line subsequences, generation identities, and no-role-disposition boundary.
- Invoke validate_phase2.py and validate_deas.py only through their public command-line seams in acceptance tests. Require explicit rejection tests for missing, malformed, oversize, out-of-root, manifest-mismatched, original-line-altered, invalid-argument, and runtime-error inputs, plus any subprocess timeout or execution-error path introduced by the implementation. In JSON mode, parsing and runtime errors SHALL exit 2, keep standard error empty, and emit one error object with stable rule ID and path.
- Update validation-report.md and handoff.md with exact commands, exits, artifact hashes, warnings, and stop state.
- Update source-register.md and qualification-plan.md to identify Generation 2 as a documentation correction, not evidence recollection.

### Compound conformance protocol

The Phase 2 validator SHALL accept exactly the public invocation `python3 validate_phase2.py --repository-root <root> --generation 2 --json`. On success it SHALL exit 0 and emit one JSON object with exactly these values:

```json
{
  "decision": "PASS",
  "generation": 2,
  "identity_verified": true,
  "original_observations_preserved": true,
  "phase2_degs_decision": "PASS",
  "role_disposition": "NONE",
  "schema_version": 2,
  "validation_report_decision": "PASS"
}
```

The DEAS validator SHALL not trust that assertion alone. Before it can emit
Generation 2 package-validation PASS, it independently SHALL:

1. verify the exact generation-2-sha256.txt path, external manifest SHA-256, and other 14 C4 artifacts;
2. require zero `DEAS-TRACE-001`, `DEAS-PHASE-001`, and `DEAS-EVIDENCE-001` findings;
3. execute the Phase 2 CLI in a killed-on-timeout process group with a two-second wait limit and a combined four-MiB streaming output cap;
4. require the Generation 2 task to remain `READY_FOR_EXECUTION` with package validation PASS, post-action validation PENDING, independent review PENDING, handoff PASS, no unresolved item, and the exact task ID above;
5. locate workspace `governance/bin/engineering-gate.py`, require SHA-256 `44c33ba743851d7befe11ebf93f2f4d9021b126f951a4587562adfca21f65c1e` before and after each execution, then run its canonical `validate` and `evaluate` commands with `--json`; require silent standard error and an exact seven-field JSON object from each with decision PASS, risk tier TIER_1, authority lane TAYLOR_AI_WORKBENCH, empty warnings and unmet requirements, and typed nonempty rule and typed evidence-path lists;
6. require the Phase 2 validation report to implement the canonical evidence contract, record status `PACKAGE_PASS_READY_FOR_GIT_DELIVERY`, cite the exact Generation 2 task and manifest path, and include the two literal commands below. Its single `**Discrepancy references:**` value SHALL be `NONE` or a comma-and-space-separated list of backticked stable IDs matching `P2-G2-DISC-NNN` exactly;
7. compare all four predecessor evidence records from C2 against their successors as ordered byte-identical line subsequences and require their sole Role Disposition value to remain `not assigned`; and
8. revalidate the active corrected DEAS definition, including its historical Generation 1 negative proof and artifact manifest; and
9. emit `decision_scope: PACKAGE` and
   `external_gates_pending: [G7, G8, G9]`, leaving those gates to external
   records that bind the frozen Generation 2 manifest, independent review
   decisions, authorized acceptance, commit, pushed ref, and
   draft-pull-request identity without rewriting the package.

The two literal report commands are:

```sh
python3 contexts/operational-system/docs/program/v1/qualification/phase-2/validation/validate_phase2.py --repository-root . --generation 2 --json
DEAS_GENERATION_2_MANIFEST_SHA256=<externally-frozen-sha256>
python3 docs/standards/deas/v1/validation/validate_deas.py conformance --generation 2 --identity-manifest contexts/operational-system/docs/program/v1/qualification/phase-2/generation-2-sha256.txt --identity-manifest-sha256 "$DEAS_GENERATION_2_MANIFEST_SHA256" --json --repository-root .
```

Any missing, nonzero, malformed, oversize, timed-out, diagnostically noisy,
inconsistent, or unbounded component is validation ERROR and cannot become
package or conformance PASS. With `--json`, a DEAS execution or argument error
SHALL exit 2 with empty standard error and exactly one JSON object containing
`decision: ERROR`, `finding_count: 1`, one finding with nonempty `message`,
`path`, and stable `rule_id`, and `schema_version: 1`. The Phase 2 validator
SHALL not call the DEAS Generation 2 conformance command recursively.

## Required proof sequence

1. Verify branch, C3 parent, private remote, lock, no writer, and all predecessor hashes.
2. Materialize a read-only Generation 1 snapshot from commit f45ae80c64a0aa8c723a5a58b4fbc7073682d349 and verify its 28-path identity.
3. Run the DEAS conformance CLI against that snapshot as generation 1; require exactly the six frozen findings and exit 1.
4. Apply only the 15-path transformation with no exception.
5. Prove each original observation file is an ordered byte-identical line subsequence of its Generation 2 successor.
6. Run the exact compound Phase 2 and DEAS public CLI protocol against
   Generation 2; require the structured Phase 2 result, independent DEAS
   corroboration, package-scoped PASS with G7/G8/G9 explicitly pending, and zero
   semantic finding.
7. Verify exact manifests, links, schema, diff hygiene, secret scan, and no prohibited state.
8. Complete Standards and Spec review against the separately approved C4 specification; bind both decisions to the frozen manifest externally while the embedded review state remains PENDING.
9. Commit and push only under the recorded authorization; bind Git delivery externally, and keep merge separately controlled.

## Acceptance criteria

- Generation 1 retains its exact commit and artifact identity and fails exactly the frozen six findings.
- Generation 2 is the first generation to pass all three semantic finding
  families; overall conformance exists only after the external G7/G8/G9 record
  binds the exact package.
- The 15-path set is exact and no original observation line changes or moves.
- Every added fact has an identified source; unsupported values remain UNKNOWN or NOT RECORDED.
- Current Phase 2 validation, DEGS evaluation, DEAS definition validation, secret scan, manifests, and reviews pass.
- No Role Disposition, Phase 3, system qualification, release, device/storage action, credential/permission action, destructive action, root adoption, merge, or exception occurs.

## Rollback and stop

Before commit, preserve the candidate, index, Generation 1 snapshot, and validation evidence for review; do not reset or delete automatically. After commit or push, preserve the exact branch and remote state; do not amend, force-push, reset, rebase, delete, or merge automatically.

Stop on any predecessor drift, original-line change, unsupported fact, extra path, validator disagreement, exception request, authentication interaction, non-fast-forward remote, review finding, or need for authority beyond the exact future C4 instruction.

## Later adoption

AI-Workspace root or cross-workspace adoption remains a nonmutating plan. After the committed DEAS baseline is reviewed, a separate task must name each destination, owning context, profile mapping, compatibility test, rollback, and authority. DobeWorks terms and controls are not copied into UW or another workspace by implication.
