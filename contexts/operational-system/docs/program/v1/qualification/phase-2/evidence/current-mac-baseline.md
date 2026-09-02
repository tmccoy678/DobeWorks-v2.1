# Current Mac Baseline

- **Role ID:** `CP-CANDIDATE-01`
- **Observation window:** `2026-09-02T01:49:15Z` through `2026-09-02T01:57:21Z`
- **Evidence status:** `OBSERVED_WITH_UNRESOLVED_DISCREPANCY`
- **Role Disposition:** not assigned

## Operating-system and hardware fields

| Field | Observed value | Source |
|---|---:|---|
| Product name | `macOS` | `P2-CP-001` |
| Product version | `26.6.2` | `P2-CP-001` |
| Build version | `25G83` | `P2-CP-001` |
| Architecture | `arm64` | `P2-CP-002` |
| Model identifier | `Mac17,2` | `P2-CP-003` |
| Physical memory bytes | `25769803776` | `P2-CP-004` |
| Logical CPU count | `10` | `P2-CP-005` |

No serial, hardware UUID, network identity, hostname, or account field was collected.

## Aggregate memory and swap

`P2-CP-006` reported aggregate swap totals of `0.00M` total, `0.00M` used, and `0.00M` free, with encrypted swap indicated.

`P2-CP-007` reported:

- page size `16384` bytes and total physical memory `25769803776` bytes;
- system-wide memory-free percentage `76%`;
- pages free `7143`, active `577840`, inactive `568492`, speculative `8163`, throttled `0`, and wired `161128`;
- compressor pages used `194022`, pages compressed `922564`, and pages decompressed `285062`;
- swapins `0`, swapouts `0`, pageins `1782277`, and pageouts `31233`.

`P2-CP-008` independently reported aggregate virtual-memory counters at its observation instant:

- pages free `6823`, active `577866`, inactive `568588`, speculative `8207`, throttled `0`, wired `161128`, and purgeable `26241`;
- file-backed pages `429706`, anonymous pages `724955`, pages stored in compressor `464680`, and pages occupied by compressor `194022`;
- compressions `922564`, decompressions `285062`, pageins `1782372`, pageouts `31233`, swapins `0`, and swapouts `0`.

The two commands ran at different instants; their differing counters are preserved without normalization.

## Root-filesystem fields

`P2-CP-009` reported POSIX root-filesystem values:

- 1024-block total: `971298980`;
- used: `12336700`;
- available: `599871496`;
- reported capacity: `3%`;
- mount point: root.

The reviewed sanitizer for `P2-CP-010` reported:

- filesystem type `apfs`;
- filesystem name `APFS`;
- total size `994610155520` bytes;
- free space `0` bytes; and
- mounted `true`.

The `0`-byte sanitizer result conflicts with the nonzero POSIX available-block result. The authorized surface does not establish why; usable root free space is therefore `UNKNOWN` for any later decision that requires reconciliation.

## Security-control status

| Control | Observed state | Source |
|---|---|---|
| FileVault | enabled | `P2-CP-011` |
| System Integrity Protection | enabled | `P2-CP-012` |
| Gatekeeper assessments | enabled | `P2-CP-013` |

These observations establish status only. No recovery, configuration, or key material was accessed.
