# DEAS v1.0 Enforcement Matrix

## Profile legend

- M: mandatory
- S: strengthened beyond Core
- B: bounded exploratory form; must pass Core or Strict before promotion

| Rule | Core | Strict | Exploratory | Static enforcement | Semantic enforcement | Required evidence |
|---|---:|---:|---:|---|---|---|
| DEAS-PRE-001 | M | S | B | syntax, forbidden-flow patterns, state labels | lifecycle transitions cannot imply authority or promotion | flow or state map; negative transition test |
| DEAS-PRE-002 | M | S | B | numeric bounds, timeout/retry/variant presence | bounds cover every repeated or open-ended operation | bound register; exhaustion test |
| DEAS-PRE-003 | M | S | B | exact paths, inputs, destinations, dependencies | observed writes and authority stay within the frozen surface | baseline, allowlist, backup, side-effect record |
| DEAS-PRE-004 | M | S | B | function logical-line count; document and commit inventory | each unit has one reviewable responsibility | size report; exception if applicable |
| DEAS-PRE-005 | M | S | B | required gate and assertion fields | criteria distinguish PASS, FAIL, BLOCKED, and ERROR | pre/postcondition and stop-state tests |
| DEAS-PRE-006 | M | S | B | path, data, tool, and permission allowlists | collected and changed material is minimum necessary | scope diff; prohibited-target negative test |
| DEAS-PRE-007 | M | S | B | checked exits, schemas, hashes, required reads | cross-boundary results support the recorded claim | input, intermediate, and output validation |
| DEAS-PRE-008 | M | S | B | variant, retry, generator, configuration inventory | accepted bytes are traceable despite nondeterminism | source/configuration record; exact output hash |
| DEAS-PRE-009 | M | S | B | reference depth, ownership and provenance links | no indirection hides authority, owner, or source of truth | trace map and resolved links |
| DEAS-PRE-010 | M | S | B | syntax, lint, schema, link, diff, secret and test output | every warning has a truthful disposition | clean reports and warning register |

## Overlay enforcement

| Overlay | Trigger | Additional mandatory checks |
|---|---|---|
| Python | Python source or executable Python validator | compile; public-seam tests; checked I/O and subprocess results; Strict function limit; fail-closed inputs |
| Document | Markdown, policy, plan, ADR, handoff, or specification | link resolution; normative/state vocabulary; source wording; unknown and authority boundaries |
| Evidence | evidence record, report, manifest, or evidence-generating method | complete record contract; exact claim and requirement trace; freshness; immutable generation; hash verification |
| Validator | validator, schema, test harness, or gate | red before green; deterministic exits/findings; negative inputs; public interface; no fixture-only decision |
| AI-Assisted | model contributes interpretation or artifact bytes | source and prompt boundary; prohibited inference; bounded variants; deterministic acceptance; human-only decisions |
| Git | tracked substantive change, branch, commit, push, PR, or merge | verified base; exact staged paths; coherent commits; non-force push; private remote; draft PR; explicit merge authority |

## Gate evidence

| Gate | PASS evidence | Blocking examples |
|---|---|---|
| G0 Authority | exact task, lane, profile, overlays, allowed and excluded actions | lifecycle readiness mistaken for execution authority |
| G1 Baseline | branch, HEAD, tree, status, hashes, remote, locks, writer check | drift, ambiguous target, unexpected branch |
| G2 Backup | verified repository history and exact changed-byte snapshot | missing or unverified recovery input |
| G3 Red | public-seam test fails for the intended absent or defective behavior | test passes before implementation or fails for setup noise |
| G4 Static | syntax, schema, paths, links, manifests, diff and secret checks pass | malformed artifact, extra path, unresolved link, secret finding |
| G5 Semantic | cross-artifact invariants and evidence contracts agree | completed work remains planned; incomplete prerequisite represented complete |
| G6 Positive and negative | expected accept/reject/failure behavior passes | tautological fixture or untested rejection path |
| G7 Identity | tested, reviewed, staged, committed, pushed and handed-off artifacts match | regenerated or edited bytes after review |
| G8 Review | Standards and Spec axes have no blocking finding | requirement missing, scope creep, documented-standard breach |
| G9 Acceptance | authorized acceptance for the exact identity | inferred merge, release, phase, exception, or residual-risk authority |

## Phase 2 Generation 1 semantic checks

| Finding | Condition | Current expected instances | Passing condition for a later generation |
|---|---|---:|---|
| DEAS-TRACE-001 | evidence collection is complete while Phase 2 evidence remains planned or globally reserved | 1 | exact produced artifacts and current states replace the contradictory reservation |
| DEAS-PHASE-001 | evidence collection is complete while required Phase 2 entry items remain unchecked | 1 | each prerequisite has an evidence-backed historical disposition and no false completion |
| DEAS-EVIDENCE-001 | a consequential record lacks one or more fields in the canonical evidence-record contract | 4 | every required field is explicit; missing values remain UNKNOWN or NOT RECORDED |

The expected Generation 1 decision is FAIL with six ordered findings. validation/generation-1-expected-findings.json freezes the exact result. A validator execution problem exits separately and never satisfies the negative proof.

## Phase 2 Generation 2 compound conformance

| Control | DEAS-independent enforcement | Passing evidence |
|---|---|---|
| Exact identity | require the canonical generation-2-sha256.txt path, its externally supplied SHA-256, and exactly the other 14 C4 paths | sorted manifest, external digest, and zero hash mismatch |
| Semantic correction | inspect collection state, traceability, entry history, and all four evidence contracts | zero `DEAS-TRACE-001`, `DEAS-PHASE-001`, and `DEAS-EVIDENCE-001` findings |
| Phase 2 validator | execute the exact public CLI and require silent standard error plus its exact schema-v2 compound JSON | bounded exit 0, empty diagnostics, and exact result object |
| Task and report | inspect the exact task ID and canonical evidence-record fields; independently run DEGS validation and evaluation with closed-schema JSON parsing | COMPLETE/PASS task states, report status PASS, literal commands, stable discrepancy IDs, and two silent exact DEGS PASS results |
| Historical preservation | compare all four C2 records with their successors as ordered byte-identical line subsequences | all original lines present unchanged and in order |
| Role boundary | parse every Role Disposition field in the four records | exactly one `not assigned` value per record |
| DEAS baseline | re-run definition validation against the committed C3 identity and historical C2 findings | definition PASS and exact six-finding Generation 1 regression |
| Resource bounds | stream stdout and stderr concurrently, cap combined output at four MiB, kill stalled process groups, and reject unexpected diagnostics | Git and Phase 2 timeout, exhaustion, and diagnostic tests pass |

## Exception enforcement

No exception applies unless its file exists at the canonical exception path, validates structurally, names one rule and exact scope, records Taylor's human approval, remains unexpired, and has passing compensating controls. The first Phase 2 Generation 2 conformance attempt accepts zero exceptions.
