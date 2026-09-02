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
