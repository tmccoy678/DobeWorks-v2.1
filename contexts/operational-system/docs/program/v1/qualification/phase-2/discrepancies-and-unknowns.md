# Phase 2 Discrepancies and Unknowns

## Current observations

1. **Root free-space disagreement:** `P2-CP-009` reported `599871496` available 1024-blocks, while the reviewed `P2-CP-010` sanitizer reported `0` free bytes. The bounded method set does not establish the reason. Any reconciled usable-capacity claim remains `UNKNOWN`.
2. **Root read-only flags unavailable:** the `P2-CP-010` sanitized result did not include reviewed media-read-only or volume-read-only fields. Both remain `UNKNOWN`.
3. **Storage read-only flags unavailable:** the `P2-ST-002` sanitized result did not include reviewed media-read-only or volume-read-only fields. Both remain `UNKNOWN`.
4. **Storage fitness unresolved:** health, backup membership, snapshot state, redundancy, recovery fitness, permissions, and content state were outside the authorized metadata surface and remain `UNKNOWN`.
5. **Worker evidence blocked:** `WK-CANDIDATE-01` remains `BLOCKED_PENDING_EVIDENCE`; no physical or remote action was authorized.
6. **Observer feasibility bounded:** executable presence was established, but reliability, scheduling, retention, alerting, and operational fitness remain `UNKNOWN` because implementation was excluded.

## Controlled execution exception

The first `P2-CP-010` attempt could not access the DiskManagement framework inside the local command sandbox. The frozen catalog explicitly anticipated this condition and permitted the exact read-only command to be rerun outside the sandbox with approval. The approved exact rerun succeeded through the same reviewed sanitizer. No broader method, permission, or field set was used.

## Historical-value boundary

No August 30 measurement was reused as current evidence. Historical-to-current comparisons not established by this package remain `UNKNOWN`.

## Decision boundary

This package assigns no Role Disposition and makes no qualification or release claim. Resolving any item above requires a separately defined and authorized evidence step.
