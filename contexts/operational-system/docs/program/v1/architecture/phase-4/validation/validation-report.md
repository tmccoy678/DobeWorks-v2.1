# Phase 4 Software Core Validation Report

- **Evidence ID:** `EV-P4-SW-TEST`
- **Requirement/fault IDs:** `REQ-CP-004`, `REQ-CP-009`, `REQ-WK-004` through `REQ-WK-009`, `REQ-OBS-001` through `REQ-OBS-004`, `REQ-OBS-006` through `REQ-OBS-008`, `REQ-ASS-002`, `REQ-ASS-003`; `FLT-WK-004`, `FLT-JOB-001` through `FLT-JOB-008`, `FLT-OBS-001` through `FLT-OBS-005`, `FLT-NET-001`, `FLT-NET-002`, `FLT-SUP-001`, `FLT-SUP-002`; `DEAS-PRE-001` through `DEAS-PRE-010`
- **Claim under test:** The exact 25-path Phase 4 package implements the frozen synthetic Worker/Observer software-core interfaces, produces the exact 18 evidence identities, passes deterministic static/semantic/positive/negative/security/privacy/failure/boundary checks, preserves all authority limits, and is frozen without performing controlled integration or claiming qualification, release, merge, or human acceptance.
- **Acceptance method:** Public red/green Module and package-validator suites, exact fixture comparison, Python compile/AST/function bounds, JSON, link, source, manifest, DEGS schema/evaluation, Git diff/index, secret, historical-input preservation, identity, and independent-review checks listed below.
- **Exact source/configuration/role/device-safe identity/environment/target:** Base commit `b24c6d677d80b5299f09cb087d263d69bd6b68af`; base tree `3008aab9ed2c86052ad35a24d4a1f108a2b07658`; exact sources/configuration/fixtures in `../source-register.md`; Python 3.9.6; branch `operational-system/v1-phase4-software-core`; exactly 25 tracked paths; disposable synthetic staging roots; no device, collector, service, Promotion Event, or integration target.
- **Procedure or command identity:** Commands in this report; public package seam `python3 -B contexts/operational-system/docs/program/v1/architecture/phase-4/validation/validate_phase4.py --repository-root . --manifest-sha256 <external-digest> --external-spec /Users/taylor/AI-Workspace/.scratch/dobeworks-operational-system-phase4-software-core/spec.md --external-spec-sha256 49ebf76d993a8b9d02147df1786b2f2647a8773cb2a5e561babafdb4bc14dc92 --json`.
- **Start time:** 2026-09-06T01:12:37-05:00
- **End time:** 2026-09-06T09:14:06-05:00
- **Clock-quality basis:** Execution-host wall clock in America/Chicago with one-second display precision; individual test duration is recorded by the harness but external time attestation is NOT RECORDED.
- **Expected result:** Exact package-scoped PASS with zero findings, 48 passing Module cases, all 22 package-validator cases passing, exact sources/fixtures/manifest, `NOT_YET_QUALIFIED`, `NOT_YET_RELEASED`, `NOT_PERFORMED` integration, and G7/G8/G9 pending; negative mutations fail closed with stable findings.
- **Actual result:** Public G3 red evidence confirmed both absent Modules and the absent validator before implementation. Generation 1 passed its precommit checks but the exact clean commit then failed both independent reviews: its Git validator required dirty paths, staged-output filesystem errors escaped the Worker seam, the runner deadline was not enforced, validator diagnostics/tree traversal were not bounded, malformed Python could escape the JSON seam, the engineering-gate path was wrong, and evidence Artifact paths were not repository-relative. Generation 1 remains preserved and rejected. Correction Generation 2 passed all 48 Module cases and all 22 validator cases, including a real clean committed Git fixture and deterministic regressions for every review blocker, and returned package-scoped PASS with zero findings. The embedded Tier 2 task passed schema validation and its pre-delivery evaluation remained expectedly `BLOCKED` only on artifact identity and independent review; external records close those controls without rewriting the package.
- **Status:** PACKAGE_PASS_READY_FOR_GIT_DELIVERY
- **Discrepancy references:** `P4-OPEN-001` and `P4-OPEN-002` in the task and evidence records remain explicit later-phase limitations, not package-validation failures.
- **Artifact paths:** `contexts/operational-system/docs/program/v1/architecture/phase-4/validation/validation-report.md`, `contexts/operational-system/docs/program/v1/architecture/phase-4/validation/validate_phase4.py`, `contexts/operational-system/docs/program/v1/architecture/phase-4/validation/test_validate_phase4.py`, `contexts/operational-system/docs/program/v1/architecture/phase-4/phase-4-sha256.txt`, `contexts/operational-system/software/phase4/worker_core.py`, `contexts/operational-system/software/phase4/observer_core.py`, `contexts/operational-system/software/phase4/test_worker_core.py`, `contexts/operational-system/software/phase4/test_observer_core.py`
- **Cryptographic identities:** Twenty-four non-manifest paths are frozen by `../phase-4-sha256.txt`; its own SHA-256, commit, pushed ref, draft PR, and independent-review identities are recorded externally after freeze.
- **Evidence owner:** Codex in Taylor AI Workbench for deterministic execution and record integrity; external reviewers own their decisions; Taylor owns exact G9 acceptance.
- **Human/physical action owner:** Taylor for authority only; no physical, remote, device, credential, permission, destructive, promotion, integration, qualification, release, or merge action occurred.
- **Confidentiality classification:** `C1_PRIVATE_OPERATIONAL`; fixtures contain synthetic non-secret metadata only; PRIVATE PERSONAL USE - NOT FOR PUBLIC RELEASE.
- **Recoverability classification:** Complete-history bundle SHA-256 `5b8ef9cb0b2076be7a791070757a1f2a006937af4d9a1eaee3f0369e3b127abc`, Git source, exact fixtures, tests, and manifest; this is not an integrated-system recovery claim.
- **Limitations:** Software-core tests do not prove real process termination, transport, persistent state, device behavior, collector permissions/load, actual retention deletion/archive, alert delivery, Promotion Event, recovery, integration, end-to-end role behavior, qualification, or release fitness.
- **Unsupported inferences:** G7/G8/G9 closure inside immutable bytes, actual integration, accepted output, device or role qualification, Phase 5 authority, System Release, Public Release, compliance, certification, merge, or broader adoption.
- **Current freshness:** Current for the exact final non-self manifest and recorded environment after full rerun; any package/source/configuration/fixture/environment byte change invalidates the result and requires a new generation.
- **Supersession:** Corrects rejected Phase 4 Generation 1 at commit `c365171e3ae7aff184d5e2ade5ec470365765009`, tree `d66364645ab9a173a7ed4fe8b99b8c9cb4bda154`, manifest SHA-256 `6a50cbbdb713338dc61bc51840b5b7a40c0997029aa1905f6fae2e55624ca25c`; historical representative Worker jobs remain separate evidence.

## Deterministic check record

| Check | Expected | Recorded result |
|---|---:|---|
| Worker/Observer G3 red | missing implementations rejected through public suites | PASS; exact external record preserved |
| 48 Module public cases | exit 0 | PASS |
| Package validator public cases | exit 0 | PASS; 22 cases |
| Generation 1 independent reviews | exact identity / findings preserved | PASS; both `FAIL` decisions preserved externally as correction inputs |
| Exact package validator | exit 0 / `PACKAGE` `PASS` / zero findings | PASS |
| Python compile and function bounds | exit 0 | PASS; six Python paths |
| JSON and relative links | exit 0 | PASS; seven JSON paths and all package links |
| Source identities and non-self manifest | exit 0 | PASS |
| Embedded DEGS task schema | `PASS` | PASS |
| Embedded Tier 2 evaluation | expected `BLOCKED` only on external identity/review | PASS; exact expected two unmet controls |
| Exact 25-path diff and index | exit 0 | PASS |
| Secret scan | exit 0 / no unexplained finding | PASS; no leaks found |
| Historical input identities | unchanged exact hashes | PASS |
| External Standards and Spec review | no blocking finding on frozen identity | EXTERNAL / PENDING |
| External derived Tier 2 delivery task | `PASS` after exact identity/review binding | EXTERNAL / PENDING |

## Command set

```sh
python3 -B -m unittest discover -s contexts/operational-system/software/phase4 -p 'test_*_core.py' -v
python3 -B contexts/operational-system/docs/program/v1/architecture/phase-4/validation/test_validate_phase4.py -v
python3 -B contexts/operational-system/docs/program/v1/architecture/phase-4/validation/validate_phase4.py --repository-root . --manifest-sha256 <external-digest> --external-spec /Users/taylor/AI-Workspace/.scratch/dobeworks-operational-system-phase4-software-core/spec.md --external-spec-sha256 49ebf76d993a8b9d02147df1786b2f2647a8773cb2a5e561babafdb4bc14dc92 --json
python3 /Users/taylor/AI-Workspace/governance/bin/engineering-gate.py validate contexts/operational-system/docs/program/v1/architecture/phase-4/degs/phase4-task.json
python3 /Users/taylor/AI-Workspace/governance/bin/engineering-gate.py evaluate contexts/operational-system/docs/program/v1/architecture/phase-4/degs/phase4-task.json
python3 -B -m py_compile <six Phase 4 Python paths>
python3 -m json.tool <seven Phase 4 JSON paths>
shasum -a 256 -c contexts/operational-system/docs/program/v1/architecture/phase-4/phase-4-sha256.txt
git diff --check
gitleaks git --no-banner --redact --timeout 30 .
```

Bytecode caches are directed outside the repository or removed before freeze.
The manifest's own digest and all external gates remain external.
