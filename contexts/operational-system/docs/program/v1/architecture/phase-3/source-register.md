# Phase 3 Source Register

## Repository and authority inputs

| Source | Exact identity | Use and boundary |
|---|---|---|
| Merged Phase 3 base | commit `bb5a0c6cc807939621c9c6efa4dae8f1e7fc1cc7`; tree `6571d0c1101b9034c3c3e07deb788f85f810af92` | Exact private-repository baseline; merge tree equals reviewed C4 tree |
| C4 source | commit `43df9f5a0d403851242f52f817e5195ed2764543`; Generation 2 manifest SHA-256 `4dd1d41da658a22386af04d31ed97a9a149c731c19f44e8c58fe5d1c62d5c296` | Frozen Phase 2 Generation 2 package |
| C4 delivery record | workspace `.scratch/dobeworks-deas-v1-generation-2/delivery.md`; SHA-256 `a3afa5077f27e00e79437f9796d6a41cec766ea24609f4baac1113dab2d63c7b` | External G7/G9 evidence for C4 only |
| C4 review index | workspace `.scratch/dobeworks-deas-v1-generation-2/review/final-review-index.md`; SHA-256 `dbdd8ca674c83c847f266a795af21105457fe896bff99d810331cff66aa8902c` | External C4 G8 evidence only |
| C4 merge record | workspace `.scratch/dobeworks-deas-v1-generation-2-merge/delivery.md`; SHA-256 `bb2fc50770cf68b42566560f3c6f1f387b9de6c2c45ef3cb7643bd0d1f9fe185` | Exact private merge evidence; grants no later-phase fact |
| Post-C4 authorization assessment | workspace `.scratch/dobeworks-operational-system-post-c4-authorization/spec.md`; SHA-256 `d33265651692254e00fcad3a9f570492e949e8ab7045ce13706bca8c6d68ae41` | Records merge complete and later gates/evidence gaps |
| Phase 3 definition authority | workspace `.scratch/dobeworks-operational-system-phase3/spec.md`; SHA-256 `82d297f1eebd18ed2f69b3db47c4a4769f23ebafb6ded06bafc000334053674e` | Exact 18-path definition/freeze authority and exclusions |
| Pre-Phase 3 complete-history backup | workspace `.scratch/dobeworks-operational-system-phase3/backup/dobeworks-pre-phase3.bundle`; SHA-256 `a0c73287bd9ad6abf101044195b987f1bb1c0bdc08a2eb517cdd7cd10fd59236` | Verified rollback/safe-stop input; not a sole backup strategy |
| Phase 3 generation 1 predecessor | commit `327b9aa73d16c0d012d4a5d694915984cca9e67a`; tree `0fd19c3eb7ed5adef6a333a64bd6617d920f7d03`; manifest SHA-256 `ccdbd883a5755b45b2735b1982bce8b6b0a613fcdba16c410a88fccf47552290` | Immutable reviewed predecessor; retains the two confirmed audit defects |
| Phase 3 generation 1 independent audit | workspace `audits/dobeworks-phase3-architecture-independent-audit-20260905.md`; SHA-256 `84532bc89254b38c465eb330a435e4820973d87684cbb82d701d87e7dc6eb69c` | Exact audit input; no blocker claimed, two low defects and three risks recorded; does not close corrected-generation review |
| Phase 3 correction authority | workspace `.scratch/dobeworks-operational-system-phase3-correction-1/spec.md`; SHA-256 `1e5393902e2488c7b78b00b8d75e71521051876be9116ef9ca82177412659458` | Exact nine-path correction, TDD, review, commit, and private delivery authority; downstream actions excluded |
| Pre-correction complete-history backup | workspace `.scratch/dobeworks-operational-system-phase3-correction-1/backup/dobeworks-pre-phase3-correction-1.bundle`; SHA-256 `4e4045bd8edb47108ffdcd142e7548a67565439f43f313fca84edb1f842514b6` | Verified complete-history reconstruction input for generation 2 |
| Canonical DEGS gate | workspace `governance/bin/engineering-gate.py`; SHA-256 `44c33ba743851d7befe11ebf93f2f4d9021b126f951a4587562adfca21f65c1e` | Validate/evaluate task record only; never execution or release authority |

Taylor's definition and correction instructions are preserved in the two
external Phase 3 authority records. They authorize the exact package and this
correction generation, not a device target, Phase 4, qualification result,
System Release result, Public Release, or broader adoption.

## Canonical source identities

| Repository-relative source | SHA-256 | Claim supported |
|---|---|---|
| `docs/standards/deas/v1/standard.md` | `df1644513d48022a3b9f01392fa33e391680b0d1e9341594fbc272ee44237586` | Strict profile, overlays, evidence contract, lifecycle gates |
| `docs/standards/deas/v1/deas-v1-sha256.txt` | `3f40080f3cd725db8906385abb6f7db79fadef5a231cf6bc9206b2fa43863c88` | Corrected DEAS definition manifest identity |
| `contexts/operational-system/docs/program/v1/requirements.md` | `addb4d5c564866ad7115fa40b6e36189e3cb54397224d6c805a11fc431b168c0` | Normative Phase 3 and later acceptance requirements |
| `contexts/operational-system/docs/program/v1/decisions.md` | `21cd53b6f0c4fc8a1da7f08266553047dac4e801ecfe72b6e49842b5e7104fe2` | Taylor-accepted RPO/RTO, exposure, retention, support, replacement, and risk boundaries |
| `contexts/operational-system/docs/program/v1/evidence-and-audit-plan.md` | `531e5e1c60e032d27740962050b76dd285417993884ae7c4079efc8e4c90d537` | Minimum Phase 3 bundle and completion chain |
| `contexts/operational-system/docs/program/v1/fault-test-matrix.md` | `f6e025c572bac2ad7ac4b22ba481f14aa6372b63f3a8fa67ae5cff39a7d59e89` | Complete applicable fault set and resume authorities |
| `contexts/operational-system/docs/program/v1/qualification/phase-2/handoff.md` | `89eafe6a547a3e75e1c75a1cbdba6db88f1edf97375bfac24ae794187273cf0b` | Frozen C4 Phase 2 state and explicit unknown/action boundary |
| `contexts/operational-system/docs/program/v1/qualification/phase-2/discrepancies-and-unknowns.md` | `f218d8b2441fee8b47f212ebeaf3a66cdc840e2dc055d58724dfe20bd88071fb` | Current-Mac, Seagate, Worker, and Observer gaps |
| `contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/current-mac-baseline.md` | `213ca5d2b87832c3694cbe988d8d2c02a0526e4fac36654684e5fdca12834875` | Historical privacy-safe current-Mac observations and limits |
| `contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/seagate-device-volume.md` | `117bcee90efae84ab4803886247e8563069f5c12454957ef7564cb3c6f0db169` | Historical privacy-safe Seagate topology fragment and limits |
| `contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/worker-candidate.md` | `e015cce0e1a58e5e608251fe38befc040ac681c7725f449eac9cc1a54df308d3` | No authorized Worker evidence step; device facts `UNKNOWN` |
| `contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/observer-surface.md` | `b2177563e81dd1dbd57cf5dafad286e5b1abf1f6d4f5b8c9a0d8efea9fc21fb2` | Historical executable-presence fragments only |

## Source-use rules

- Current repository bytes override memory or summaries.
- An accepted decision supplies a policy value, not proof that the system meets
  it.
- A Phase 2 observation supports only its stated historical claim and limits.
- A missing or conflicting value remains `UNKNOWN`.
- No source in this register authorizes content traversal, credentials,
  permission changes, physical action, device mutation, Phase 4, qualification,
  System Release, Public Release, or broader adoption.
- Any source-byte, authority, requirement, candidate, or base-identity change
  invalidates this generation and requires a new manifest and validation.
