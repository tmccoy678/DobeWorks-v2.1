# Benchmark correction and validation scope

The first benchmark observation remains unchanged in [apple-silicon.json](../benchmarks/results/apple-silicon.json). The corrected observation is [apple-silicon-v2.json](../benchmarks/results/apple-silicon-v2.json); [comparison](../benchmarks/results/measurement-comparison.json) records both run hashes and every changed case. Corpus pins, input bytes, labels, and denominators are unchanged. [Current test output](../benchmarks/results/validation-v2.json) retains commands, timestamps, exits, and diagnostics.

Both harnesses now preserve partial timeout diagnostics and actual script invocation arguments. The Observer stale control requires literal STALE freshness. Negative tests inject a real delayed process, contradictory freshness, broken candidates, and changed corpus/selection bytes. They failed for the intended reasons before the fixes and pass afterward. Python 3.9 cannot report original interpreter argv; the report records that limitation, the executable, effective interpreter flags, working directory, and exact script arguments.

## Observer and historical package checks

The Observer source and fixtures remain unchanged. All 318 public out-of-contract inputs still produce controlled unusable outcomes; both native controls pass. This is application rejection evidence, not JSON parser conformance or whole-system assurance. All 70 Worker/Observer tests and six benchmark tests pass.

The existing 149-test suite has 145 passes and four failures: DEAS 27/28, Phase 3 18/19, Phase 4 package validation 30/32, Worker/Observer 70/70. These reproduce at the approved base 793ed01. The DEAS manifest expects an older README identity; Phase 3 likewise expects its frozen Operational System README. Phase 4's positive package tests assert an exact diff against their historical baseline, but the supplied draft base already contains documentation paths outside that package. The current benchmark commit adds more paths outside that historical package; it cannot qualify as that exact package either.

The earlier draft report describes its earlier observation and is retained; its 148/149 summary does not describe current main or these changes. Historical assertions need their original complete package tree and specified external identities. Current runtime tests and the new benchmark use current draft source. Passing either set cannot substitute for the other. No historical manifest has been rehashed to hide drift.

The frozen 792-line Phase 2 validator refers to an externally pinned DEGS identity. It contains no copy of the defective comparator. Its historical hash is not repinned by this fix; a future current-system integration package must explicitly bind the corrected DEGS source and generate new evidence.

## Remaining work

The user approved correction of staged system v1 and v2. The verified working pair is draftdobeworks/draftdegs, labeled v2.1 development drafts. A separate pre-Generation-2 staged v1 pair has not been identified. A component directory named v1 does not establish that system version. Apply the same behavioral regression and a minimal backport after its exact repository or commit is identified.

For the complete release, include the original integrated Trash Pickup, Treasure Pickup, and FigureMe. Preserve FigureMe's core behavior and visual essence while removing personal identifiers from release copies. The standalone Draft2Staged Pickup pair remains available independently. Packaging, accessible figure finalization, rights review, Apple-silicon fresh-user installation, and public publication are separate unfinished work. Nothing here changes repository visibility or qualifies a public release.
