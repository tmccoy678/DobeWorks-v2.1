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
