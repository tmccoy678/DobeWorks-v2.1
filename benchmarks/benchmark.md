# DobeWorks Observer rejection benchmark

**318 of 318 public inputs produced controlled, unusable telemetry outcomes. Both native controls passed.**

This measures application rejection robustness at the actual Observer CLI. All public files fall outside its snapshot contract. JSONTestSuite parser labels remain descriptive strata: 188 `n_`, 95 `y_`, and 35 `i_`. Rejecting a syntactically valid JSON value can be correct for this application. This is not a JSON parser conformance score.

Correct outcomes are structured ERROR/exit 2 without signals, or schema-incompatible UNKNOWN/exit 0 with all six signals UNKNOWN. Crashes, timeouts, invalid output, stderr, inconsistent exits, or usable telemetry fail the case. Fresh native input must produce its six expected validated values; stale input must suppress them. Controls are separate from the 318-case denominator and prevent a reject-everything candidate from earning success.

No Worker execution, real device observation, autonomous remediation, source-code review, or whole-system assurance is measured. Historical package validators are separate from this current-source benchmark. See the [current validation scope](../docs/benchmark-correction.md).

## Reproduce

From this repository root, with Python 3:

```bash
python3 -B benchmarks/run_benchmark.py --output benchmarks/results/rerun.json
python3 -B -m unittest discover -s benchmarks -p 'test_*.py' -v
```

Exit 0 means all corpus cases and both controls matched their stated expectations. Harness exit 1 indicates measured mismatches or failed controls; exit 2 indicates input/configuration error. A failed control invalidates interpretation of the corpus score. Each candidate process has a five-second timeout. There are no automatic retries. Corpus and selection integrity must pass before scoring. The fixed selection manifest is hashed in the harness; changing it creates a new benchmark version and must be disclosed.

Recorded host: macOS 26.6.2, arm64, Python 3.9.6. Corrected run started 2026-09-11T20:05:31.049239+00:00 and ended 2026-09-11T20:05:38.788821+00:00. Other platforms were not tested. This is an observed result for these exact source bytes, not a performance leaderboard or certification.

## Inspect the evidence

- [Corrected machine-readable run](results/apple-silicon-v2.json): all case outcomes, stdout/stderr, exits, controls, identities, and environment.
- [Original observation, preserved unchanged](results/apple-silicon.json). Its command field was a hard-coded recipe; the new run records actual script arguments and interpreter state.
- [Before/after comparison](results/measurement-comparison.json): exact changed outcomes and run hashes.
- [Current tests and limitations](../docs/benchmark-correction.md).
- [Pinned input manifest](manifest.json): upstream commit and exact input SHA-256 hashes.
- [Selection and research](selection.md): source fit, exclusions, and license inspection.
- [Full upstream MIT notice](data/LICENSE): retained unchanged with the copied data.
- [Original APA reference collection](../references/dobeworks-apa-references.pdf): unchanged; benchmark sources supplement it.

Source: [nst/JSONTestSuite at the pinned commit](https://github.com/nst/JSONTestSuite/tree/1ef36fa01286573e846ac449e8683f8833c5b26a). Credit Nicolas Seriot and JSONTestSuite contributors. No endorsement is implied. Only selected data files and the license were copied; the report distinguishes local controls from public inputs.

[Evidence contract and change controls](evidence.md).

Timeouts retain partial stdout and stderr. Stale controls require literal STALE freshness. Invocation provenance records executable, script arguments, working directory, and effective interpreter flags; original interpreter arguments are unavailable on Python 3.9. Corpus inputs and denominators are unchanged.
