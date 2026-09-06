# Storage Resource Device and Volume Metadata

- **Role ID:** `SR-CANDIDATE-01`
- **Observation window:** `2026-09-02T01:57:54Z` through `2026-09-02T02:07:51Z`
- **Evidence status:** `OBSERVED_WITH_UNKNOWNS`
- **Role Disposition:** not assigned

## Sanitized topology

`P2-ST-001` returned a unique target match through the reviewed sanitizer:

- external physical disk count: `1`;
- target match count: `1`;
- match status: `UNIQUE_MATCH`;
- device content type: `GUID_partition_scheme`;
- device size: `1000204885504` bytes;
- partition 1: content type `EFI`, size `209715200` bytes, target volume `false`;
- partition 2: content type `Apple_HFS`, size `999860912128` bytes, target volume `true`.

No device identifier, partition identifier, UUID, serial, other volume name, or content path was retained.

## Sanitized target-volume metadata

`P2-ST-002` returned:

- filesystem type `hfs`;
- filesystem name `Case-sensitive Journaled HFS+`;
- total size `999860912128` bytes;
- free space `98903109632` bytes; and
- mounted `true`.

The sanitizer output did not contain reviewed values for media-read-only or volume-read-only flags. Both remain `UNKNOWN`.

## Explicit unknowns

Device health, backup membership, backup dates, snapshot state, redundancy, recovery fitness, filesystem integrity, permissions, Time Machine contents, and user-content state remain `UNKNOWN`. No traversal, repair, First Aid, benchmark, write, mount change, or permission request occurred.

## DEAS evidence-record contract

- **Evidence ID:** EV-P2-ST-TOPOLOGY
- **Requirement/fault IDs:** `REQ-PGM-005`, `REQ-ST-001`, `REQ-ST-007`, `REQ-ST-011`, `DEAS-EVIDENCE-001`
- **Claim under test:** The authorized Phase 2 observation recorded only the listed sanitized Storage Resource topology and volume metadata while retaining all unobserved fitness and content facts as UNKNOWN.
- **Acceptance method:** Inspection of the frozen sanitizer outputs and canonical record without evidence recollection.
- **Exact source/configuration/role/device-safe identity/environment/target:** `SR-CANDIDATE-01` in the 2026-09-02 supervised qualification environment; exact safe identities are in `../source-register.md`.
- **Procedure or command identity:** `P2-ST-001` and `P2-ST-002` as frozen in the method catalog; no command was rerun for Generation 2.
- **Start time:** 2026-09-02T01:57:54Z
- **End time:** 2026-09-02T02:07:51Z
- **Clock-quality basis:** UTC execution-host timestamps recorded by the historical command log; per-command subsecond precision is NOT RECORDED.
- **Expected result:** Only allowlisted sanitized fields, explicit UNKNOWN values for inaccessible facts, and no traversal, mutation, permission request, or Role Disposition.
- **Actual result:** One unique sanitized topology match and allowed volume fields were recorded; read-only flags and all fitness, backup, recovery, permission, and content facts remain UNKNOWN.
- **Status:** OBSERVED_WITH_UNKNOWNS
- **Discrepancy references:** [Storage flags and fitness unknowns](../discrepancies-and-unknowns.md#current-observations)
- **Artifact paths:** `evidence/seagate-device-volume.md`, `evidence/command-log.md`, and `discrepancies-and-unknowns.md`
- **Cryptographic identities:** Generation 1 file SHA-256 `0be85cc8856ea610cad9239b8d163be0b4049e768bb170f852eb7b7909b76514`; the successor is bound by `../generation-2-sha256.txt`.
- **Evidence owner:** UNKNOWN; contemporaneous evidence does not name the owner accountable for record integrity.
- **Human/physical action owner:** Taylor for authorization; physical action NOT APPLICABLE.
- **Confidentiality classification:** PRIVATE PERSONAL USE - NOT FOR PUBLIC RELEASE
- **Recoverability classification:** Recoverable from Generation 1 commit `f45ae80c64a0aa8c723a5a58b4fbc7073682d349` and the frozen manifests; observations were not recollected.
- **Limitations:** The privacy-filtered metadata does not inspect contents, backups, health, redundancy, recovery fitness, permissions, integrity, or current post-observation state.
- **Unsupported inferences:** Storage Role fitness, backup membership, recoverability, redundancy, health, Role Disposition, qualification, release, and any content claim.
- **Current freshness:** Historical observation window ending 2026-09-02T02:07:51Z; no Generation 2 remeasurement occurred, so present storage values are UNKNOWN.
- **Supersession:** Generation 2 supersedes only the evidence-contract omission in the Generation 1 record; every original observation line remains preserved in order.
