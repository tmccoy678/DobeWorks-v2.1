# Recorded capability demonstration and tests

Date: September 11, 2026. Environment: Apple silicon (`arm64`), macOS 26.6.2, Python 3.9.6. Source baseline: `7374f7e21251e17ff40ef0e5a334e7fdd3d31684`. Existing Python source, fixtures, and validators remain unchanged.

## What ran

Each suite was invoked through `python3 -B -m unittest discover -s <directory> -p 'test_*.py' -v`. Exact directories, full output, and exits are in [raw evidence](draft-test-evidence.json).

| Suite | Observed result |
| --- | --- |
| DEAS definition validator | 28 passed |
| Phase 3 package validator | 18 passed, 1 failed |
| Phase 4 package validator | 32 passed |
| Worker and Observer cores | 70 passed |

Total: 148 passed, 1 failed. There were no skipped tests in these suites. The failing test is `test_exact_package_passes`: its frozen Phase 3 manifest reports `DEAS-PRE-007`, a hash mismatch for `contexts/operational-system/README.md`.

The same 19-test suite was rerun against a pristine archive of the source baseline, without the draft's documentation changes. It produced the same failure. This is inherited source drift, not a regression introduced by these README/SECURITY changes. It remains a public-release blocker. Neither the expected result nor the historical manifest was rewritten to conceal it.

## Readable behavior

The README's Worker example produced COMPLETED_UNACCEPTED with one attempt and no promotion. Its output hash was `1099ce46272a14af8ba7372857c0f634a2feb2d20ade0ce2a96a6dfdc56d6fae`. Only a disposable staging directory was written. The transcript substitutes `$DEMO_STAGE` for its random path; no other output normalization was performed.

The Observer example emitted VALIDATED/FRESH for the fixture time and TELEMETRY_UNAVAILABLE/STALE with UNKNOWN signals for the later time. Both exits were 0 because a structured record was emitted. The record's status determines whether evidence is usable; process exit alone is insufficient.

## Interpretation

These demonstrations show bounded synthetic behavior in the recorded environment. They do not demonstrate live device observation, deployment, qualification, public release, or safe execution of arbitrary jobs. Test counts do not prove all defects absent. A clean-user installer and other platforms were not tested. [Citations](../CITATIONS.md) explain the reporting method, not validation of this specific system by the cited authors.
