# Program Definition Provenance

- **Program baseline:** Phase 1 — Program Definition
- **System status:** `NOT_YET_QUALIFIED`, `NOT_YET_RELEASED`
- **Canonical-promotion status:** `COMPLETE`
- **Canonical-promotion task:** `DEGS-T1-DW-OPS-PROMOTE-20260901`

## Frozen source

- Noncanonical source package: `/Users/taylor/AI-Workspace/.scratch/dobeworks-hardware-software-v1/`
- Source package manifest: `validation/package-sha256.txt`
- Manifest SHA-256: `0b9cad7e97e61e1ba38c9019fe68ef312c6d3d0f851ccfd796483f491de9805f`
- Source verification: all 16 manifested files `OK`
- Phase 1 completion validation: `PASS`
- Phase 1 DEGS Tier 1 evaluation: `PASS`, no unmet requirements or warnings

The frozen scratch package remains evidence only and is not an active program source of truth after promotion.

## Promotion baseline

- DobeWorks baseline commit: `450fb23581611115a2b7a04b39153d07e9b5b4c8`
- DobeWorks baseline tree: `84b77ff94a6cae75a26a23c472ae35dcaad6a519`
- Promotion readiness evaluation: `PASS`, no unmet requirements or warnings
- Post-promotion validation: `PASS` — exactly 15 canonical targets, comprising 3 modified tracked files and 12 created files
- Promotion completion DEGS evaluation: `PASS`, no unmet requirements or warnings
- Post-lock tracked backup bundle SHA-256: `91a6dc8cf2954336fab429f6b8f706a7dc5cfcba10ab2a750f44cd7639b18abb`
- Commit and push authority: none

The canonical working-tree promotion is intentionally uncommitted. Git HEAD remains `450fb23581611115a2b7a04b39153d07e9b5b4c8`, and no path is staged.

## Transformation boundary

- Five accepted Phase 1 files were promoted byte-for-byte: the Operational System glossary, decisions, requirements, fault matrix, and evidence/audit plan.
- The program definition, traceability matrix, Phase 2 entry criteria, and ADR 0013 were transformed only to reflect canonical location and completed decision/promotion state.
- The context map, Operational System README, this provenance record, and the three project wayfinding/domain files were synthesized from the accepted context-boundary decision.
- The existing root `CONTEXT.md`, ADRs 0001–0012, private references, research, governance, and unrelated files were protected from change.

## Authority limit

Canonical promotion establishes documentation ownership only. It does not qualify a device, inspect hardware or storage, authorize Phase 2, implement or deploy software, accept later residual risk, declare System Release, or authorize Public Release.
