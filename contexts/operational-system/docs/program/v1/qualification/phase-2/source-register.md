# Phase 2 Source Register

## Governing identities

| Source | Workspace-relative identity | SHA-256 | Use |
|---|---|---|---|
| Canonical context handoff | `handoffs/current-context.md` | `6936cbbf618ccf96b1f570c897a2047829d3a8df84ec8c2aebbcc5a72cde2604` | Current phase and boundaries |
| Canonical checkpoint | `command-center/state/context-checkpoint.json` | `738b78c29d6732abc2d4d28f32770961652b5b38e9833e9097e8f9dff06ac26d` | Schema-v2 governance state |
| Fresh-context receipt | `command-center/state/context-resume.json` | `a81193debe897eb1b4097fef0197495636d77250c5fef11e2941e1e89d4de0fa` | `READY/NONE` route evidence |
| Frozen Phase 2 definition manifest | `.scratch/dobeworks-hardware-software-v1-phase2-definition/validation/package-sha256.txt` | `363f7f6b3fc501eb85f02c95b7117f02048789095437d34fe563e22ddf1915e9` | Exact execution contract |
| Phase 1 canonical-target manifest | `.scratch/dobeworks-operational-system-canonical-promotion/validation/canonical-target-sha256.txt` | `385b5f08b4248f115e6f04932400c864f6c1bf5135662e2fc4bb0c7e938b82cc` | Exact 15-path baseline |
| Method catalog | `.scratch/dobeworks-hardware-software-v1-phase2-definition/method-catalog.md` | `acc89df80dc6237739cc35242b7cc32d132ef3d8f159d6e1160c50b272e4a34a` | Exact observation methods |
| Disk-metadata sanitizer | `.scratch/dobeworks-hardware-software-v1-phase2-definition/methods/sanitize_diskutil_plist.py` | `fb32e38c7cdab001a845825cdb46b67894fa3b9c1406ac36af31d7d279f895ba` | Reviewed field allowlist |
| Privacy boundary | `.scratch/dobeworks-hardware-software-v1-phase2-definition/privacy-boundary.md` | `f5f20a207ed10c4e8aff73be81e652f7726a18c60fc7711140bff07230538250` | Allowed and prohibited fields |
| Evidence route | `.scratch/dobeworks-hardware-software-v1-phase2-definition/canonical-evidence-route.md` | `d5ede59b99663daa24ac9be1c5340e02bea54599c8bf1a01eed08aef5e49daf8` | Exact 13-path route |

Taylor's exact execution authorization is preserved verbatim in `qualification-plan.md`. No session identifier, thread identifier, or window title is retained.

## Observation identities

The exact command text is bound by the frozen method-catalog identity above. Execution used these catalog identities:

- Current Mac: `P2-CP-001` through `P2-CP-013`.
- Storage metadata: `P2-ST-001` and `P2-ST-002`.
- Observer executable-presence trace IDs: `P2-OBS-001` (`memory_pressure`), `P2-OBS-002` (`vm_stat`), `P2-OBS-003` (`sysctl`), and `P2-OBS-004` (`diskutil`). These trace IDs label the four exact tests already fixed in the catalog; they do not add methods.
- Worker candidate: no command exists or ran.

## Evidence handling

Only role IDs `CP-CANDIDATE-01`, `SR-CANDIDATE-01`, `WK-CANDIDATE-01`, and `OBS-SURFACE-01` identify observed targets. Raw outputs have zero intended retention. Command-output hashes establish execution traceability without persisting prohibited fields.

## Generation 2 correction sources

Generation 2 is a documentation correction, not evidence recollection.

| Source | Identity | Use |
|---|---|---|
| Immutable Generation 1 | commit `f45ae80c64a0aa8c723a5a58b4fbc7073682d349`; 28-path manifest `9ed515ac90cc100bae3d3a3baa674d6c2a200f5e18b3da4d7b4daaf979ac8d77` | Historical negative regression and original observations |
| Corrected DEAS v1.0 definition | commit `ca8efcefe6568a7a64b5b6d930031dff0131efec`; tree `e785cafa49bdfcc3ec5e660d3a87c943047d9ef5`; manifest-file SHA-256 `3f40080f3cd725db8906385abb6f7db79fadef5a231cf6bc9206b2fa43863c88` | Reconciled package lifecycle, public validator seam, C4 rules, and correction boundary |
| Exact C4 plan | `docs/standards/deas/v1/phase2-generation-2-plan.md` at commit `ca8efcefe6568a7a64b5b6d930031dff0131efec` | Exact paths, transformations, proof sequence, and exclusions |
| Generation 2 task | `degs/phase2-generation-2-task.json`; task `DEGS-T1-DW-HWSW-P2-GENERATION-2-20260902` | Taylor authority, scope, tests, stops, and acceptance |
| Canonical DEGS engineering gate | workspace `governance/bin/engineering-gate.py`; SHA-256 `44c33ba743851d7befe11ebf93f2f4d9021b126f951a4587562adfca21f65c1e` | Frozen executable input for Generation 2 DEGS validate and evaluate |
| Resumed-C4 backup | workspace `.scratch/dobeworks-deas-v1-generation-2/backup/dobeworks-pre-c4-resumed.bundle`; SHA-256 `8a01883b463ae85fddeebf0b78cc0e601903a1350567c761a5d1241ee3065200` | Complete-history recovery source rooted at the correction predecessor |
| Active package manifest | `evidence-sha256.txt` | Active canonical package identities, excluding itself and the non-circular Generation 2 manifest |
| Generation 2 identity manifest | `generation-2-sha256.txt` | Exact other 14 C4 artifacts; its SHA-256 is supplied externally after freezing |
| Generation 2 validation | `validation/validation-report.md` | Compound public-seam result and limitations |
| Independent review | workspace `.scratch/dobeworks-deas-v1-generation-2/review/final-review-index.md` | External Standards and Spec decisions bound after package freeze; canonical state remains `PENDING` |

The predecessor `evidence-sha256.txt` has SHA-256
`3901bb1d87659585092037d86d7f5291bd84091739f797dd56f51a4766476e80`.
Taylor's exact C4 instruction is preserved in `qualification-plan.md`. No
session, window, or model identity is used as authority evidence.
