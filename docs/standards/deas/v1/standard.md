# DobeWorks Engineering Assurance Standard v1.0

- Standard: DEAS
- Version: 1.0
- Status: ACCEPTED FOR THIS REPOSITORY
- Scope: DobeWorks code, documents, validators, evidence, AI-assisted work, and Git phase records
- Effective behavior: prospective; historical artifacts are corrected when touched, promoted, or materially risky

## Purpose and authority

DEAS is a preventive engineering standard: constrain the work before execution, make failure observable, and require exact evidence before acceptance. It applies inside the private DobeWorks repository. It does not grant task authority, accept residual risk, qualify a system, authorize release, or establish compliance or certification.

The source design adapts Gerard J. Holzmann's Power of Ten principles beyond C software. The adaptation preserves their preventive intent while replacing language-specific mechanisms with controls suitable for DobeWorks artifacts. No NASA, JPL, IEEE, or author endorsement is claimed.

The words SHALL, SHALL NOT, SHOULD, SHOULD NOT, and MAY are normative. A work item conforms only when every applicable SHALL has objective evidence and every approved exception is valid.

## Assurance objects

**DEAS v1.0 Baseline** is the exact Git commit containing this standard and the artifact identities in deas-v1-sha256.txt.

**Work unit** is one bounded change with an objective, exact mutation surface, inputs, outputs, tests, stop conditions, and acceptance decision.

**Generation** is an immutable artifact set with one exact identity. A correction creates a later generation and never silently rewrites the reviewed predecessor.

**Conformance** is the overall result that all selected profile, overlay, and
applicable gate requirements pass for one exact generation. **Package
validation** is the deterministic pre-delivery result for the immutable bytes;
it is an input to conformance and cannot itself satisfy external gates.

**Exception** is a temporary, human-approved deviation from one named DEAS rule. An exception cannot authorize a task or weaken an external security, privacy, release, credential, physical, or destructive boundary.

## Profile selection

Select one profile before mutation. An overlay or task rule may strengthen the selected profile and may not weaken it.

### Core

Core is mandatory for accepted DobeWorks work. The work SHALL have a bounded objective and path set, applicable tests, input and output validation, an explicit acceptance decision, and no unexplained warning.

### Strict

Strict applies when work changes canonical artifacts, executable code, validators, evidence, manifests, governance interfaces, security or privacy controls, phase boundaries, release-adjacent material, or any result where a silent defect could corrupt later decisions. Strict includes Core and requires:

- exact input and output identities;
- deterministic resource, iteration, retry, and mutation bounds;
- negative and failure-path tests at public seams;
- static and semantic enforcement;
- a verified backup and explicit rollback or safe-stop procedure;
- a short-lived Git branch, coherent commits, an early private remote checkpoint, and review before merge; and
- no active exception for a first conforming correction.

### Exploratory

Exploratory applies to bounded learning artifacts. It SHALL record the question, assumptions, allowed surface, time or event expiry, and disposition. It cannot modify canonical state, represent itself as evidence, waive a gate, or promote itself. Promotion requires a new Core or Strict work unit and fresh validation against the intended destination.

## Context overlays

Apply every overlay whose trigger matches the work.

### Python overlay

- Use Python standard-library facilities unless an approved requirement justifies a dependency.
- Keep functions single-purpose and structurally bounded.
- Under Strict, each function SHALL contain no more than 60 logical code lines unless an approved exception names the function and compensating tests.
- Check subprocess exits, file operations, decoding, parsed values, and public return results. A successful subprocess SHALL have empty standard error unless an exact diagnostic grammar is explicitly accepted, and structured standard output SHALL be parsed as one complete result rather than matched by prefix.
- A validator SHALL fail closed on missing, malformed, ambiguous, or out-of-root input.

### Document overlay

- Separate normative requirements, evidence, decisions, plans, and historical facts.
- Use stable identifiers for enforceable rules and cross-references.
- Preserve exact source wording where authority or provenance depends on it.
- Mark unknown, proposed, historical, superseded, and not-authorized states explicitly.
- Resolve relative links and prohibit completion language unsupported by evidence.

### Evidence overlay

- Follow the canonical evidence-record contract below.
- Bind claims to exact requirements, methods, times, identities, owners, limitations, classifications, freshness, and supersession.
- Freeze reviewed bytes with a sorted cryptographic manifest.
- Corrections create a new generation; original observations remain attributable and unchanged.

### Validator overlay

- Test through the command-line or other public validation seam.
- Derive decisions from inspected artifacts rather than fixture-only constants.
- Emit deterministic machine-readable findings with stable rule IDs and paths.
- Distinguish expected nonconformance from validator execution error by exit code.
- Exercise negative and failure behavior before acceptance.

### AI-Assisted overlay

- Record human authority, source boundaries, expected output, prohibited inference, and acceptance responsibility.
- Treat model output as proposed until deterministic checks and human-required decisions complete.
- Bound variants, retries, context, tools, destinations, and retained data.
- Preserve uncertainty and source language; never convert absence into fact.
- An agent cannot approve its own exception, residual risk, release, or expanded authority.

### Git overlay

- Begin substantive work from a verified base on a short-lived branch.
- Freeze exact paths before staging and verify the index before every commit.
- Use the smallest coherent commit sequence that preserves provenance.
- Push an accepted safe checkpoint promptly to the approved private remote.
- Open a draft pull request at the earliest reviewable checkpoint and maintain it as evidence.
- Require non-force updates, an unchanged base, passing gates, and explicit merge authority.

## Canonical evidence-record contract

Each consequential evidence record SHALL contain exactly one Markdown list item in the form `- <required label> <value>` for every row below. A value SHALL contain at least one non-whitespace character. `UNKNOWN` and `NOT RECORDED` are valid values when they truthfully preserve an evidentiary gap; an empty value, an omitted row, or a duplicated row is nonconforming. This table is the single machine-readable source for contract labels; plans and validators SHALL reference it rather than maintain another label list.

<!-- DEAS-EVIDENCE-SCHEMA:START -->
| Order | Required Markdown label | Minimum meaning |
|---:|---|---|
| 1 | `**Evidence ID:**` | Stable record identity |
| 2 | `**Requirement/fault IDs:**` | Requirements and fault cases supported |
| 3 | `**Claim under test:**` | Bounded claim evaluated by the record |
| 4 | `**Acceptance method:**` | Inspection, analysis, test, review, or other named method |
| 5 | `**Exact source/configuration/role/device-safe identity/environment/target:**` | Minimum-safe identity of every consequential input and target |
| 6 | `**Procedure or command identity:**` | Reproducible procedure, command, or method identity |
| 7 | `**Start time:**` | Observation or execution start, or a truthful gap marker |
| 8 | `**End time:**` | Observation or execution end, or a truthful gap marker |
| 9 | `**Clock-quality basis:**` | Time-source precision and limitations |
| 10 | `**Expected result:**` | Predetermined acceptance expectation |
| 11 | `**Actual result:**` | Observed result without normalization |
| 12 | `**Status:**` | PASS, FAIL, BLOCKED, ERROR, or a context-defined non-acceptance state |
| 13 | `**Discrepancy references:**` | Linked discrepancy identities or NONE |
| 14 | `**Artifact paths:**` | Repository-relative evidence artifact paths |
| 15 | `**Cryptographic identities:**` | Hashes or a truthful reason identity is unavailable |
| 16 | `**Evidence owner:**` | Owner accountable for record integrity |
| 17 | `**Human/physical action owner:**` | Human owner or NOT APPLICABLE |
| 18 | `**Confidentiality classification:**` | Handling classification |
| 19 | `**Recoverability classification:**` | Recovery or irreversibility classification |
| 20 | `**Limitations:**` | Known evidence and method limitations |
| 21 | `**Unsupported inferences:**` | Conclusions the record does not support |
| 22 | `**Current freshness:**` | Freshness state and basis |
| 23 | `**Supersession:**` | Predecessor, successor, or NONE |
<!-- DEAS-EVIDENCE-SCHEMA:END -->

## Preventive invariants

### DEAS-PRE-001 — Explicit flow

Work SHALL use explicit state transitions and structurally bounded control flow. Hidden fallthrough between lifecycle states, recursion without a proven bound, and implicit promotion are nonconforming.

### DEAS-PRE-002 — Bounded work

Iterations, recursion, retries, waits, input size, output size, generated variants, and touched paths SHALL have finite limits or a named stop condition. Open-ended agent effort is not an engineering bound.

### DEAS-PRE-003 — Frozen resources and side effects

Before execution, the work SHALL freeze its inputs, destinations, authority, side effects, external services, and mutation surface. A newly discovered write, permission, credential, physical, destructive, or release need is a stop.

### DEAS-PRE-004 — Small units

Functions, documents, commits, tasks, and evidence records SHALL remain small enough for one responsibility and complete review. Strict Python functions are limited to 60 logical code lines absent an approved exception. Large documents SHALL use clear sections and disclosed references rather than duplicate controls.

### DEAS-PRE-005 — Preconditions and postconditions

Every consequential work unit SHALL state inspectable preconditions, postconditions, invariants, acceptance criteria, and failure state. Executable assertions are preferred where they can test behavior without replacing error handling.

### DEAS-PRE-006 — Least scope

Files, data, tools, privileges, roles, and retained outputs SHALL use the minimum scope needed for the objective. Scope expansion requires a new boundary and authority.

### DEAS-PRE-007 — Validate inputs and results

Validate each untrusted input, trust-boundary result, external command exit, transformation, manifest, and final artifact. Ignoring a result requires an explicit reason that is itself reviewed.

### DEAS-PRE-008 — Constrained generation

Generated content, preprocessing, templating, model variation, and nondeterminism SHALL be bounded and inspectable. Accepted output SHALL identify the generator or method, configuration, sources, validation, and exact bytes where identity matters.

### DEAS-PRE-009 — Constrained indirection

Keep ownership, authority, provenance, data flow, and call or reference chains directly traceable. An indirection that hides the source of truth, reviewer, mutation target, or failure is nonconforming.

### DEAS-PRE-010 — Continuous analysis

Run applicable syntax, static, semantic, link, schema, test, secret, and diff checks at the earliest useful boundary and again on the accepted identity. Every warning is resolved, explicitly dispositioned, or blocks conformance.

## Enforcement classes

**Static enforcement** checks artifact presence, syntax, schema, paths, counts, bounds, hashes, links, and prohibited patterns without interpreting lifecycle truth.

**Semantic enforcement** compares claims across artifacts, including completion versus trace state, gate history versus execution state, evidence contracts versus records, authority versus action, and generation identity versus conformance.

**Review enforcement** challenges source-to-claim fit, scope, maintainability, uncertainty, and task fidelity after deterministic checks.

Tool availability does not weaken a rule. If a required enforcement method is unavailable, the result is BLOCKED or UNKNOWN, not PASS.

## Validation gates

1. G0 Authority — exact objective, profile, overlays, scope, exclusions, and human-required decisions are recorded.
2. G1 Baseline — branch, base, paths, hashes, dependencies, locks, and relevant writers are verified.
3. G2 Backup — required backup and recovery or safe-stop procedure are verified before mutation.
4. G3 Red — the first behavioral or regression test fails for the intended reason.
5. G4 Static — syntax, schema, links, sizes, path allowlists, manifests, diff hygiene, and secret checks pass.
6. G5 Semantic — cross-artifact claims, lifecycle state, authority, traceability, and evidence contracts agree.
7. G6 Positive and negative — expected success, rejection, failure paths, and boundary cases pass through public seams.
8. G7 Identity — reviewed, tested, staged, committed, pushed, and handed-off identities agree.
9. G8 Review — Standards and specification reviews have no blocking finding.
10. G9 Acceptance — the authorized human or process accepts the exact result; release and merge remain separate authorities when specified.

Failure at any gate stops later mutation. A known negative regression may satisfy evidence for a nonconforming historical generation but never converts that generation to PASS.

Package validation and delivery completion are distinct when the commit, pushed ref, or pull request is itself an acceptance input. An immutable candidate may record package-validation PASS only while its task remains `READY_FOR_EXECUTION` and its handoff remains `READY_FOR_GIT_DELIVERY`; that state does not satisfy G7 or complete the overall delivery task. After the commit, push, and pull-request state exist and are verified, a control-plane record external to the immutable package SHALL bind those identities and may close the overall task. A canonical package SHALL NOT predict its own commit, pushed ref, or completed delivery.

The immutable pre-delivery package SHALL keep embedded independent-review and
post-action-validation states `PENDING`. Independent reviewers SHALL bind their
decision to the frozen package identity in an external control-plane record;
their decision SHALL NOT require rewriting the bytes they reviewed. A package
validator MAY report deterministic package PASS only with an explicit
`PACKAGE` decision scope and the unsatisfied external gates named. It SHALL NOT
represent that result as overall conformance, G7, G8, G9, embedded task
completion, or embedded review PASS.

## Exceptions

Exception records live at docs/standards/deas/exceptions/DEAS-EXC-YYYYMMDD-NNN.json. Each record SHALL contain:

- schema version, exception ID, DEAS version, and rule ID;
- selected profile and overlays;
- exact files, functions, artifacts, generation, and task scope;
- technical reason and rejected conforming alternatives;
- compensating controls and tests;
- risk and affected-party analysis;
- approver Taylor, human role, approval evidence, and approval time;
- start, expiry, reassessment trigger, and closure evidence; and
- status PROPOSED, APPROVED, EXPIRED, REVOKED, or CLOSED.

Only APPROVED and unexpired records apply. An exception is invalid if any field is unknown, its scope expands, its compensating control fails, or its authority source cannot be verified. The Phase 2 Generation 2 first correction permits no exception.

## Generation and correction control

A reviewed generation is immutable. Correction work SHALL:

1. identify the predecessor by Git commit and artifact manifest;
2. reproduce its expected findings;
3. preserve historical observations and uncertainty;
4. create a new generation with an exact transformation map;
5. prove the predecessor still fails and the candidate passes;
6. freeze new identities and review evidence; and
7. obtain separate authority before promotion, merge, release, or later phase work.

Phase 2 Generation 1 is the first DEAS negative regression case. It fails the semantic checks defined in the enforcement matrix. Phase 2 Generation 2 is planned as the first conforming case but is not created or authorized by this baseline.

## Conformance decision

Overall conformance PASS requires all applicable profile, overlay, gate,
identity, and exception controls to pass on one exact generation. A package
validator SHALL emit `decision_scope: PACKAGE` and
`external_gates_pending: [G7, G8, G9]` when those gates are deliberately closed
by external control-plane records. A nested validator's PASS assertion is not
sufficient by itself: compound package validation SHALL independently
corroborate consequential task, report, identity, preservation, authority, and
validator results. FAIL means inspected artifacts violate a rule. BLOCKED means
a required input, authority, tool, identity, or decision is unavailable. ERROR
means validation could not complete deterministically. No result carries merge,
release, phase, credential, physical, destructive, or residual-risk authority.
