# DobeWorks — v2.1 development draft

## Public-data benchmark

**318 of 318 public inputs produced controlled, unusable telemetry outcomes. Both native controls passed.** See [benchmark results and reproduction](benchmarks/benchmark.md).

DobeWorks brings engineering intent, bounded execution, evidence, and review into one inspectable workflow. Its current synthetic Worker checks a job's identity and limits before staging a result. Its Observer reports only permitted signals and marks unavailable or stale evidence explicitly.

**Private development draft. Not qualified or publicly released.** This copy starts from DobeWorks commit `7374f7e21251e17ff40ef0e5a334e7fdd3d31684`. The existing source and fixtures are unchanged. The companion [DEGS draft](https://github.com/tmccoy678/draftdegs) demonstrates the evidence gate and a small Sashiko-derived Python component.

## See it work

Use an Apple-silicon Mac with Python 3.9 or later. Python 3.9.6 on macOS 26.6.2 was tested. These examples use synthetic fixture data and historical fixture time, not your current device or live operational records. Private repository access is currently required.

From the checkout root, observe a fresh synthetic snapshot:

```sh
python3 -B contexts/operational-system/software/phase4/observer_core.py \
  --snapshot contexts/operational-system/software/phase4/fixtures/observer-snapshot.json \
  --policy contexts/operational-system/software/phase4/fixtures/observer-policy.json \
  --allowed-input-root contexts/operational-system/software/phase4/fixtures \
  --now 2026-09-06T00:01:00Z
```

Expected and observed: `status: VALIDATED`, `freshness: FRESH`, exit 0. The output includes the inspected snapshot and policy hashes and limits its claims to synthetic observation.

Repeat the command with `--now 2026-09-07T00:01:00Z`. Expected and observed: `status: TELEMETRY_UNAVAILABLE`, `freshness: STALE`, and signals set to `UNKNOWN`. Exit 0 means the structured observation was emitted; it does **not** mean the evidence is fresh or suitable for a decision. Read the status fields.

To stage a bounded synthetic job, create a disposable directory and run:

```sh
DEMO_STAGE=$(mktemp -d)
python3 -B contexts/operational-system/software/phase4/worker_core.py \
  --envelope contexts/operational-system/software/phase4/fixtures/job-envelope.json \
  --input contexts/operational-system/software/phase4/fixtures/input-records.json \
  --staging-root "$DEMO_STAGE" \
  --allowed-input-root contexts/operational-system/software/phase4/fixtures \
  --configuration-sha256 ba0e803fc49b7a78989a44c9c9beb9789e37980b7ce92654a89d3f364460873d \
  --now 2026-09-06T00:01:00Z
```

Expected and observed: `COMPLETED_UNACCEPTED`, one attempt, no promotion, exit 0. Inspect the files in `$DEMO_STAGE`. This example writes synthetic output there; it neither accepts the result nor deploys anything. The [core documentation](contexts/operational-system/software/phase4/README.md) explains the exact checks and limits.

## Understand the evidence

```sh
python3 -B -m unittest discover \
  -s contexts/operational-system/software/phase4 -p 'test_*.py' -v
```

The current run passes **70 Worker/Observer tests** and **six benchmark tests**. Across the existing 149-test suite, 145 pass and four historical package assertions fail: one DEAS README identity mismatch, one Phase 3 manifest mismatch, and two Phase 4 exact Git-diff scope checks. These failures occur at the supplied baseline too. Frozen manifests remain unchanged.

[Current validation and scope](docs/benchmark-correction.md) explains the distinction. [Current raw tests](benchmarks/results/validation-v2.json) and the [earlier draft report](docs/draft-test-report.md) preserve both observations. Test counts are bounded evidence, not a guarantee of correctness, safety, or qualification. Other platforms and clean-user installation have not been tested in this workflow.

## Context and next work

- [Operational System](contexts/operational-system/README.md) describes the current engineering program.
- [DEAS v1.0](docs/standards/deas/v1/standard.md) defines the assurance framework.
- [Citations and credit](CITATIONS.md) explain the source material and test-reporting research.
- [Security policy](SECURITY.md) explains how to request a private reporting channel.

The Sashiko-derived work lives in the companion DEGS draft. Muchun Song receives credit for dismissed concerns and conflict resolution; Chris Mason receives credit for the review-prompts foundation, alongside the Sashiko contributors. Those are distinct contributions. No Sashiko service or model review is running in this repository.

Taylor welcomes questions, corrections, and help making the work more useful and efficient, and will respond as quickly as possible. Use issues for non-sensitive questions. No response-time guarantee is promised.

Public Apache-2.0 distribution remains planned. This private snapshot retains historical project records, identity material, and original scope statements; copying it does not clear all of that material for public release or grant new rights to it. Resolve the inherited package-test failures, source/asset rights, public packaging, and fresh-user installation before publication. No public release tag or universal platform-support claim is made here.
