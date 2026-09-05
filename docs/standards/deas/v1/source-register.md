# DEAS v1.0 Source Register

## External design sources

| ID | Source | Identity and access | Use |
|---|---|---|---|
| DEAS-SRC-001 | Gerard J. Holzmann, The Power of 10: Rules for Developing Safety-Critical Code, IEEE Computer | DOI 10.1109/MC.2006.212; author-hosted PDF at https://spinroot.com/gerard/pdf/Power_of_Ten.pdf; inspected 2026-09-02 | Primary preventive design basis |
| DEAS-SRC-002 | Gerard J. Holzmann, The Power of Ten — Rules for Developing Safety Critical Code, experience report | Author-hosted PDF at https://spinroot.com/gerard/pdf/P10exp.pdf; inspected 2026-09-02 | Experience context for practical adaptation |

DEAS paraphrases and adapts these sources. It does not reproduce their checklist verbatim, claim safety-critical suitability, or claim endorsement, certification, or affiliation.

## Adaptation map

| Source principle | DEAS adaptation |
|---|---|
| Simple control flow | DEAS-PRE-001 applies explicit flow to code and lifecycle states |
| Fixed loop bounds | DEAS-PRE-002 bounds iteration, retry, waits, generation, and scope |
| No post-initialization dynamic allocation | DEAS-PRE-003 freezes resources, destinations, side effects, and authority before execution |
| Small functions | DEAS-PRE-004 governs small code, documents, tasks, evidence records, and commits |
| Assertion density | DEAS-PRE-005 requires inspectable preconditions, postconditions, invariants, and stops |
| Smallest variable scope | DEAS-PRE-006 generalizes least scope across files, data, tools, and authority |
| Check return values | DEAS-PRE-007 validates inputs, trust-boundary results, transformations, and outputs |
| Constrained preprocessing | DEAS-PRE-008 constrains templating, generation, model variation, and nondeterminism |
| Limited pointer indirection | DEAS-PRE-009 constrains ownership, provenance, authority, and reference indirection |
| Highest warning level and static analysis | DEAS-PRE-010 requires continuous applicable analysis with no unexplained warning |

## Internal normative sources

| ID | Path or record | Role |
|---|---|---|
| DEAS-INT-001 | AGENTS.md | Repository invocation pointer |
| DEAS-INT-002 | docs/agents/domain.md and CONTEXT-MAP.md | Cross-context ownership |
| DEAS-INT-003 | contexts/operational-system/docs/program/v1/evidence-and-audit-plan.md | Evidence-record and generation contract |
| DEAS-INT-004 | contexts/operational-system/docs/program/v1/traceability-matrix.md | Generation 1 traceability baseline |
| DEAS-INT-005 | contexts/operational-system/docs/program/v1/phase-2-entry-criteria.md | Generation 1 phase-gate baseline |
| DEAS-INT-006 | contexts/operational-system/docs/program/v1/qualification/phase-2/ | Frozen Generation 1 evidence |
| DEAS-INT-007 | docs/adr/0014-adopt-deas-v1.md | Repository adoption decision |
| DEAS-INT-008 | DEGS-T1-DW-ENGINEERING-ASSURANCE-V1-DEFINE-20260902 | Exact Taylor-authorized definition task |
| DEAS-INT-009 | DEGS-T1-DW-ENGINEERING-ASSURANCE-V1-CORRECT-20260905 | Exact Taylor-authorized lifecycle-consistency correction task |
| DEAS-INT-010 | workspace `governance/bin/engineering-gate.py`; SHA-256 `44c33ba743851d7befe11ebf93f2f4d9021b126f951a4587562adfca21f65c1e` | Frozen executable input for DEGS validate and evaluate |

## Definition-correction authority

Taylor supplied the following instruction on 2026-09-05. Line wrapping is
normalized; wording and capitalization are preserved:

> i approve define and authorize a DEAS definition-correction checkpoint that reconciles the standard, C4 plan, and C3 validator, refreezes their identities, and then resumes C4.

The bounded source specification and later external review/delivery evidence
live at workspace-relative
`.scratch/dobeworks-deas-v1-definition-correction/`. That control-plane record
does not belong to the immutable repository package and does not authorize
merge or any excluded action.

## Bound identities

- Base main commit: 450fb23581611115a2b7a04b39153d07e9b5b4c8
- C1 Phase 1 commit: 56a54533bf88118c121d8e9ea4770a66ce9d2376
- C2 Generation 1 commit: f45ae80c64a0aa8c723a5a58b4fbc7073682d349
- C3 DEAS definition predecessor: 47b32aeeb107584291f69ba90b11706c7cf3eae0
- C3 definition-manifest file SHA-256: 97e3e2689dd7fc3a7ecdd835b6370253574b9975160693cd0d577be74fc9d3c8
- Frozen 28-path manifest SHA-256: 9ed515ac90cc100bae3d3a3baa674d6c2a200f5e18b3da4d7b4daaf979ac8d77
- Phase 2 evidence manifest SHA-256: 3901bb1d87659585092037d86d7f5291bd84091739f797dd56f51a4766476e80
- Canonical DEGS engineering-gate SHA-256: 44c33ba743851d7befe11ebf93f2f4d9021b126f951a4587562adfca21f65c1e
- DEAS v1.0 artifact identities: deas-v1-sha256.txt

The exact approval evidence is retained in the authorized local task record
outside Git. This repository records the task ID and bounded result without
treating Git metadata as proof of human identity. The corrected DEAS manifest
file's own SHA-256, independent review decisions, and Git delivery identities
remain external so the package neither self-hashes nor self-certifies.
