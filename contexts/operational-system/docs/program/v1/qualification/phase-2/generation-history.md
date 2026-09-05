# Phase 2 Generation History

## Generation 1

- State: `EXPECTED_NONCONFORMING`
- Commit: `f45ae80c64a0aa8c723a5a58b4fbc7073682d349`
- Exact 28-path manifest SHA-256: `9ed515ac90cc100bae3d3a3baa674d6c2a200f5e18b3da4d7b4daaf979ac8d77`
- Package evidence-manifest SHA-256: `3901bb1d87659585092037d86d7f5291bd84091739f797dd56f51a4766476e80`
- DEAS result: `FAIL` with the exact frozen six findings.

Generation 1 is immutable. It remains the negative regression case for one
`DEAS-TRACE-001`, one `DEAS-PHASE-001`, and four `DEAS-EVIDENCE-001`
findings. Its original observations and uncertainty are not defects to erase.

## Generation 2

- State: `FIRST_CONFORMING_CANDIDATE`
- Task: `DEGS-T1-DW-HWSW-P2-GENERATION-2-20260902`
- Parent definition-correction commit: `ca8efcefe6568a7a64b5b6d930031dff0131efec`
- Parent definition tree: `e785cafa49bdfcc3ec5e660d3a87c943047d9ef5`
- Parent definition manifest-file SHA-256: `3f40080f3cd725db8906385abb6f7db79fadef5a231cf6bc9206b2fa43863c88`
- Identity manifest: `generation-2-sha256.txt`
- Identity-manifest SHA-256: supplied externally after the other 14 C4 artifacts are frozen
- Embedded task state: `READY_FOR_EXECUTION`
- Embedded independent review: `PENDING`
- Embedded post-action validation: `PENDING`
- Package handoff: `READY_FOR_GIT_DELIVERY`
- External gates: `G7`, `G8`, and `G9` pending
- Evidence collection: not repeated
- Role Disposition: not assigned
- Merge: not authorized

Generation 2 corrects traceability and historical entry state, adds the
canonical evidence-record contract to four records, strengthens the Phase 2
validator, and freezes a new task, report, handoff, and manifest. Every original
line of each consequential evidence record remains an ordered byte-identical
subsequence of its successor.

The active `evidence-sha256.txt` hashes the active package except itself and the
non-circular `generation-2-sha256.txt`. The Generation 2 manifest hashes exactly
the other 14 C4 paths. Its separately supplied SHA-256 binds the manifest
itself without a circular self-hash.
