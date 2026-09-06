# Phase 4 Source and Provenance Register

## Authoritative repository inputs

| Source | SHA-256 | Use and boundary |
|---|---|---|
| `docs/standards/deas/v1/standard.md` | `df1644513d48022a3b9f01392fa33e391680b0d1e9341594fbc272ee44237586` | DEAS v1.0 rules and canonical evidence schema |
| `docs/standards/deas/v1/deas-v1-sha256.txt` | `3f40080f3cd725db8906385abb6f7db79fadef5a231cf6bc9206b2fa43863c88` | DEAS baseline identity |
| `contexts/operational-system/docs/program/v1/requirements.md` | `addb4d5c564866ad7115fa40b6e36189e3cb54397224d6c805a11fc431b168c0` | Normative Phase 4 requirements |
| `contexts/operational-system/docs/program/v1/decisions.md` | `21cd53b6f0c4fc8a1da7f08266553047dac4e801ecfe72b6e49842b5e7104fe2` | Accepted values, including `DEC-003` |
| `contexts/operational-system/docs/program/v1/evidence-and-audit-plan.md` | `531e5e1c60e032d27740962050b76dd285417993884ae7c4079efc8e4c90d537` | Required Phase 4 evidence classes |
| `contexts/operational-system/docs/program/v1/fault-test-matrix.md` | `f6e025c572bac2ad7ac4b22ba481f14aa6372b63f3a8fa67ae5cff39a7d59e89` | Applicable fault IDs and safe behavior |
| `contexts/operational-system/docs/program/v1/architecture/phase-3/phase-3-sha256.txt` | `ba00d974a9a982e750aef49a2cd52e3a57bc9bec7020ed7131c4ba575ebacb7d` | Accepted Phase 3 correction package identity |
| `contexts/operational-system/docs/program/v1/architecture/phase-3/handoff.md` | `a7b7c5b4c3b578067da9bcb8b932d175d15cd15288bf0ff4b2b52f4565ef8c56` | Phase 3 architecture/disposition boundary and gaps |

The Git base is commit `b24c6d677d80b5299f09cb087d263d69bd6b68af`,
tree `3008aab9ed2c86052ad35a24d4a1f108a2b07658`. The accepted Phase 3
correction commit is `f507e927cf98992b7679e46cf536a70fc2fd9c49` with the
same tree. The corrected external Phase 4 specification SHA-256 is
`49ebf76d993a8b9d02147df1786b2f2647a8773cb2a5e561babafdb4bc14dc92`.

## Synthetic input and expected-output identities

| Fixture | SHA-256 | Classification and purpose |
|---|---|---|
| `software/phase4/fixtures/job-envelope.json` | `57fe274106d1f3a129f6fe2c8bea1d3247925b1ba51f6221b3e8c8a35cc3d894` | Synthetic immutable job contract |
| `software/phase4/fixtures/input-records.json` | `d4dcacb9c25b2758e28a4cc218193645f004a8f880c42c515498a259e177aa36` | Synthetic non-content inventory metadata |
| `software/phase4/fixtures/expected-result.json` | `1099ce46272a14af8ba7372857c0f634a2feb2d20ade0ce2a96a6dfdc56d6fae` | Exact expected Worker result bytes |
| `software/phase4/fixtures/observer-policy.json` | `9246169419e7e0b8dee9280667208f2f632a83a97f13c065188df2ac5b32683b` | Exact accepted retention/timing policy values |
| `software/phase4/fixtures/observer-snapshot.json` | `2c0d8abdcaa3d63c7517b7768ebbb7121cc7472aa7c9956dd7bf3c420498ddd1` | Synthetic minimized telemetry input |
| `software/phase4/fixtures/expected-observer-record.json` | `711a2d9fdc2a253a672ca3e054af4e1dda3de5c295f95e4b12f8fe5ae832e6a3` | Exact expected Observer record bytes |

The Job Envelope configuration digest
`ba0e803fc49b7a78989a44c9c9beb9789e37980b7ce92654a89d3f364460873d`
is SHA-256 of the exact bytes `phase4-synthetic-config-v1` followed by one LF.

## Historical input evidence, preserved without relabeling

| Input | Exact observed identity | Phase 4 use |
|---|---|---|
| Initial representative Worker job | job `wk69-repo-analysis-20260906T033104Z-022eafea`; state `FAILED_UNACCEPTED_NO_RETRY`; evidence-manifest SHA-256 `627235d58f46e0b686e5fd92ae87413f3d76d06dad710627eabbd751d6d10b67` | Historical fault/contract design input only |
| Corrected representative Worker job | job `wk69-repo-analysis-corrected-20260906T040623Z-2d76f5c1`; state `HAND_BACK_VERIFIED_COMPLETED_UNACCEPTED`; result SHA-256 `ca48b7ffc9c607fd535a6fcb49fe3d563e5862b1c583f589dee676a2bffbbc46`; evidence-manifest SHA-256 `0cc9410ad8ad9541b98532afdb726d2930819c9ce102a533733ba498a823e7ca` | Historical contract/example input only |
| Corrected-job acceptance package | manifest SHA-256 `bea6b7a8e0ce02563399e47e3b9fd4aeea8099a3431514ee6b6e0f3489cdf702`; state `COMPLETED_UNACCEPTED`; promotion `NOT_PERFORMED` | Confirms bounded historical acceptance and explicit non-Phase-4 scope |

These `.scratch` sources remain outside Git and were not changed, copied into
the package, re-executed, or treated as Phase 4 proof. Their original labels,
uncertainty, and no-promotion boundary are preserved.

## Correction-generation provenance

- Rejected Generation 1 commit:
  `c365171e3ae7aff184d5e2ade5ec470365765009`; tree
  `d66364645ab9a173a7ed4fe8b99b8c9cb4bda154`; manifest SHA-256
  `6a50cbbdb713338dc61bc51840b5b7a40c0997029aa1905f6fae2e55624ca25c`.
- Initial Standards review: external `review/initial-standards.md`, SHA-256
  `269d18d08ca9480fd96069b20b5e28c7874c040e1ba9201979d3ce0263150bd1`,
  decision `FAIL`.
- Initial Spec review: external `review/initial-spec.md`, SHA-256
  `352b858fe69b54e8959cbe7451b1bc729a566d77f2ee9740373b1204effd04d5`,
  decision `FAIL`.
- Generation 1 is preserved in Git history and is not amended, rebased,
  relabeled, accepted, or merged. Fresh tests, identity freeze, and both fresh
  independent reviews are required for Generation 2.

## Build and dependency provenance

- Generator: Codex in Taylor AI Workbench; one initial generation after
  public-seam red evidence and one bounded correction generation after two
  identity-bound independent review failures.
- Runtime: Apple-provided Python `3.9.6`; language target Python 3.9.
- Shell used for orchestration: Bash `3.2.57` / Zsh host shell.
- Git: `2.50.1`.
- Runtime dependencies: Python standard library only.
- Third-party packages, lockfiles, registries, downloads, installers, build
  services, containers, network endpoints, and update substitutions: `NONE`.
- Default Worker runner: repository-local pure synthetic transformation with
  finite record iteration and no network or subprocess interface.
- Observer: repository-local read-only transformation with finite privacy-node
  traversal and no action interface.
- Canonical engineering gate: `/Users/taylor/AI-Workspace/governance/bin/engineering-gate.py`,
  SHA-256 `44c33ba743851d7befe11ebf93f2f4d9021b126f951a4587562adfca21f65c1e`.
- AI boundary: one variant, exact 25 paths, deterministic tests and manifest,
  no unsupported fact completion, no self-approval, and Taylor retains exact
  acceptance, merge, phase, qualification, and release decisions.
