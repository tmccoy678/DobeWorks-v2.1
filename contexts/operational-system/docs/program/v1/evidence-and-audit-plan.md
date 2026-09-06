# Evidence Freeze and Independent-Audit Plan

## Purpose

Build an evidence chain that a reviewer can reproduce and challenge without relying on mutable folders, model self-report, or unsupported completion language.

## Evidence record contract

Every consequential evidence record must identify:

- evidence ID and requirement/fault IDs;
- claim under test and acceptance method;
- exact source, configuration, role, device-safe identity, environment, and target;
- procedure or command identity without secret values;
- start/end time and clock-quality basis;
- expected result, actual result, status, and discrepancy references;
- artifact paths plus cryptographic identities where byte identity applies;
- evidence owner and any human/physical action owner;
- confidentiality and recoverability classification;
- limitations, unsupported inferences, and current freshness; and
- supersession relationship if later evidence replaces it.

A screenshot, diagnostic result, gate output, or successful process exit is never sufficient by itself unless the requirement's acceptance method explicitly says so and the surrounding identity/context record is present.

## Phase evidence bundles

| Phase | Minimum bundle before exit |
|---:|---|
| 1 — Program Definition | Accepted decisions; canonical-home decision; mission/ConOps; requirements; traceability; fault matrix; DEGS task record; validation report; Phase 2 gate |
| 2 — Read-Only Qualification | Refreshed privacy-safe Control Plane baseline; Seagate device/topology evidence within authorized permissions; exact Worker baseline if Taylor performs required action; explicit unknowns; no mutation proof |
| 3 — Architecture and Disposition | Role architecture; data/authority/threat maps; RPO/RTO and lifecycle policies; per-candidate Role Disposition; updated requirement trace |
| 4 — Software Core with Synthetic Fixtures | Exact source/config identity; unit/static/positive/negative/security/failure tests; job and promotion contracts; Observer schema/privacy/self-health tests; build/dependency provenance |
| 5 — Controlled Hardware Integration | Authorized integration plan; exact target identities; preconditions; bounded data flows; representative workload and handback evidence; no sole-copy/authority violation |
| 6 — Integrated Qualification and Proving | Complete fault evidence; representative restore; Control Plane recovery; Worker rebuild; update/rollback; telemetry failure; lifecycle rehearsals; discrepancy closure; actual end-to-end validation |
| 7 — Completion Review | Complete trace; fixed evidence index; manifests/hashes; deterministic DEGS result; independent audit; retest evidence; residual-risk register |
| 8 — Taylor Release Decision | Exact reviewed baseline; critical-unknown check; named noncritical warnings; Taylor's explicit acceptance or rejection; no inferred Public Release |

## Freeze procedure

1. Stop all evidence-producing and artifact-mutating work for the candidate baseline.
2. Resolve exact roots and exclude credentials, PRIVATE VAULT, content not authorized for evidence, and transient caches.
3. Produce a sorted inventory and SHA-256 manifest for every reviewed artifact; record file modes and required symlink resolution.
4. Validate the manifest against the exact candidate tree and record the configuration/release identity.
5. Run the complete deterministic validation and DEGS evaluation against that identity.
6. Record open discrepancies, warnings, limitations, and evidence freshness without relabeling unknowns.
7. Copy or expose the fixed read-only evidence package to the independent-auditor route using an authorized mechanism.
8. During review, permit no mutation of the evidence package. Corrections create a new generation, new manifest, retest, and new review.

## Independent-auditor requirements

- The task author and independent reviewer must differ.
- The actual reviewer role and model/provider identity must be recorded; no silent substitution is allowed.
- Provider/model readiness is checked immediately before audit without reconfiguration that could compromise independence.
- The reviewer receives the mission baseline, architecture and authority map, requirement trace, fault analysis, exact evidence index, device dispositions, recovery/rebuild/update/retirement evidence, privacy review, discrepancy log, DEGS output, and proposed residual-risk register.
- The reviewer challenges evidence truth limits, sufficiency, freshness, traceability, actual independence, unsupported inferences, and source-to-claim fit.
- Findings are classified as critical, noncritical, or informational with rationale. Recovery, privacy, security, data-loss, source-identity, or device-fitness unknowns are critical unless objective evidence proves otherwise.
- The reviewer cannot mutate the system, authorize execution, accept Taylor's risk, or declare release.
- Corrections require a new evidence generation and passing retest before the finding can close.

## Completion chain and stop rules

The only valid completion chain is:

`task-specific objective evidence -> deterministic DEGS result -> independent audit of the Frozen Evidence Set -> Taylor's explicit System Release Decision`

Stop without a clean completion claim when:

- any required evidence is absent, stale, mismatched, unauthenticated beyond its claimed method, or not tied to an exact identity;
- a critical unknown or open finding remains;
- the evidence changed after freeze;
- the reviewer is not independent or was silently substituted;
- DEGS evaluates the record as blocked/failed or its reviewed identity differs;
- Taylor has not explicitly accepted the exact residual-risk register; or
- any step attempts to infer credential, physical, destructive, exception, phase, or Public Release authority.

## Retention and privacy

Evidence retention must be decided by artifact class and release need, not inherited from Observer retention. Evidence must contain the minimum necessary privacy-safe identity, omit secret values and prohibited content, and retain enough provenance to reproduce the claim. Destruction or archival of evidence is a separately governed lifecycle action.
