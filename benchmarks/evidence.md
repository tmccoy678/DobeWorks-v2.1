# Benchmark evidence record

- **Evidence ID:** draftdobeworks-public-benchmark-v1
- **Requirement/fault IDs:** Spec user stories 1–16; OBSERVER-INPUT-BOUNDARY-001
- **Claim under test:** dobeworks-observer-rejection-v1
- **Acceptance method:** Pinned public-data execution and native controls
- **Exact source/configuration/role/device-safe identity/environment/target:** Pinned corpus and source/harness digests in results/apple-silicon.json; Apple silicon arm64, macOS 26.6.2, Python 3.9.6
- **Procedure or command identity:** python3 -B benchmarks/run_benchmark.py --output benchmarks/results/apple-silicon.json
- **Start time:** 2026-09-11T19:29:04.855637+00:00
- **End time:** 2026-09-11T19:29:12.537192+00:00
- **Clock-quality basis:** Host wall clock; UTC timestamps, independent synchronization not verified
- **Expected result:** Every selected case matches its stated oracle; controls pass
- **Actual result:** 318/318 cases matched; 0 mismatches; controls passed: True
- **Status:** PASS
- **Discrepancy references:** NONE
- **Artifact paths:** benchmarks/results/apple-silicon.json; benchmarks/manifest.json
- **Cryptographic identities:** Exact hashes in the raw run and manifest; raw run SHA-256 1bd78553b0ff09a221b45a0c328e0a02a03fa2738ec4b85e8bde1980110bbcde
- **Evidence owner:** Taylor; Codex prepared the measurement
- **Human/physical action owner:** Taylor retains release and acceptance decisions
- **Confidentiality classification:** Public-source test data and synthetic controls in a private draft
- **Recoverability classification:** Reproducible from pinned data; previous main commits retained
- **Limitations:** Narrow component benchmark; unsupported features excluded before execution; host-specific observation
- **Unsupported inferences:** Full-system assurance, full schema/parser conformance, security efficacy, release approval, or other-platform compatibility
- **Current freshness:** Fixed observation at recorded times; rerun after source or harness changes
- **Supersession:** NONE; first public-data benchmark generation

## Change controls

DEAS Strict; Python, Document, Evidence, Validator, AI-Assisted, Git overlays. Authorized surface: benchmark data, runners, tests, reports, citations, notices, and exact APA PDF copies in these private drafts. At this first observation, runtime sources remained unchanged. Rollback: revert the bounded benchmark commit; retained upstream main commits remain the source baseline. Runs are bounded by the pinned 241/318 inventories and five seconds per candidate invocation; no retries or network calls occur during measurement. Existing Phase 3 nonconformance is not waived by this record.

## Corrected measurement generation

The first observation above remains historical. The user authorized a bounded staged comparator correction and benchmark reliability fixes. The current observation is in results/apple-silicon-v2.json; tests are in results/validation-v2.json, and exact before/after identities are in results/measurement-comparison.json. DEAS Strict and all six listed overlays continue to apply. The comparator descends only into smaller finite decoded JSON subtrees; cyclic or arbitrary Python objects are outside its contract. Existing input parsing and recursion limits are unchanged. The benchmark bounds each candidate process to five seconds and the same fixed corpus.

Current result: 318/318; failures 0; controls passed True. Current run SHA-256: 0bc86c770df25f1b9c9831fde543ec299e8d95bcb47c6fc565c22ec62144375d. This supersedes the first run for current-source claims while retaining it as evidence. Historical package-test failures remain disclosed; release approval is not implied.

## Corrected measurement generation

The first observation above remains historical. The user authorized a bounded staged comparator correction and benchmark reliability fixes. The current observation is in results/apple-silicon-v2.json; tests are in results/validation-v2.json, and exact before/after identities are in results/measurement-comparison.json. DEAS Strict and all six listed overlays continue to apply. The comparator descends only into smaller finite decoded JSON subtrees; cyclic or arbitrary Python objects are outside its contract. Existing input parsing and recursion limits are unchanged. The benchmark bounds each candidate process to five seconds and the same fixed corpus.

Current result: 318/318; failures 0; controls passed True. Current run SHA-256: 0bc86c770df25f1b9c9831fde543ec299e8d95bcb47c6fc565c22ec62144375d. This supersedes the first run for current-source claims while retaining it as evidence. Historical package-test failures remain disclosed; release approval is not implied.
