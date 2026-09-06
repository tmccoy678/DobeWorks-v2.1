#!/usr/bin/env python3
"""Validate the frozen Phase 3 architecture and disposition package."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


MAX_TEXT_BYTES = 4 * 1024 * 1024
TASK_ID = "DEGS-T1-DW-HWSW-P3-ARCH-DISPOSITION-20260905"
PACKAGE_PREFIX = "contexts/operational-system/docs/program/v1/architecture/phase-3"
VALIDATOR_RELATIVE = f"{PACKAGE_PREFIX}/validation/validate_phase3.py"
MANIFEST_RELATIVE = f"{PACKAGE_PREFIX}/phase-3-sha256.txt"
SCRIPT_ROOT = Path(__file__).resolve().parents[8]
MANIFEST_LINE = re.compile(r"^([0-9a-f]{64})  ([^\s].*)$")
SHA256_VALUE = re.compile(r"^[0-9a-f]{64}$")
EVIDENCE_SCHEMA_START = "<!-- DEAS-EVIDENCE-SCHEMA:START -->"
EVIDENCE_SCHEMA_END = "<!-- DEAS-EVIDENCE-SCHEMA:END -->"
DISPOSITION_START = "<!-- PHASE3-DISPOSITIONS:START -->"
DISPOSITION_END = "<!-- PHASE3-DISPOSITIONS:END -->"

PACKAGE_FILES = (
    "contexts/operational-system/README.md",
    "contexts/operational-system/docs/program/v1/program-definition.md",
    "contexts/operational-system/docs/program/v1/traceability-matrix.md",
    f"{PACKAGE_PREFIX}/architecture-plan.md",
    f"{PACKAGE_PREFIX}/authority-and-threat-map.md",
    f"{PACKAGE_PREFIX}/data-and-signal-map.md",
    f"{PACKAGE_PREFIX}/degs/phase3-task.json",
    f"{PACKAGE_PREFIX}/fault-and-safe-degradation.md",
    f"{PACKAGE_PREFIX}/handoff.md",
    f"{PACKAGE_PREFIX}/operations-lifecycle-policy.md",
    f"{PACKAGE_PREFIX}/phase-3-sha256.txt",
    f"{PACKAGE_PREFIX}/recovery-and-capacity-policy.md",
    f"{PACKAGE_PREFIX}/role-architecture.md",
    f"{PACKAGE_PREFIX}/role-dispositions.md",
    f"{PACKAGE_PREFIX}/source-register.md",
    f"{PACKAGE_PREFIX}/validation/test_validate_phase3.py",
    f"{PACKAGE_PREFIX}/validation/validate_phase3.py",
    f"{PACKAGE_PREFIX}/validation/validation-report.md",
)
MANIFESTED_FILES = tuple(path for path in PACKAGE_FILES if path != MANIFEST_RELATIVE)
EVIDENCE_FILES = {
    f"{PACKAGE_PREFIX}/role-architecture.md": (
        "EV-P3-ARCH",
        "EV-P3-STORAGE-ARCH",
        "EV-P3-WORKER-ARCH",
        "EV-P3-OBSERVER-ARCH",
    ),
    f"{PACKAGE_PREFIX}/data-and-signal-map.md": (
        "EV-P3-DATA-MAP",
        "EV-P3-SIGNAL-DECISION-MAP",
    ),
    f"{PACKAGE_PREFIX}/authority-and-threat-map.md": ("EV-P3-AUTHORITY",),
    f"{PACKAGE_PREFIX}/recovery-and-capacity-policy.md": (
        "EV-P3-RECOVERY-DESIGN",
        "EV-P3-CAPACITY-POLICY",
    ),
    f"{PACKAGE_PREFIX}/operations-lifecycle-policy.md": (
        "EV-P3-MAINTENANCE",
        "EV-P3-RETENTION-POLICY",
        "EV-P3-ALERT-CONTRACT",
        "EV-P3-LIFECYCLE",
        "EV-P3-RETIREMENT",
    ),
    f"{PACKAGE_PREFIX}/fault-and-safe-degradation.md": (
        "EV-P3-FMEA",
        "EV-P3-SAFE-DEGRADATION",
    ),
    f"{PACKAGE_PREFIX}/role-dispositions.md": ("EV-P3-DISPOSITIONS",),
}
CANDIDATES = (
    "CP-CANDIDATE-01",
    "SR-CANDIDATE-01",
    "WK-CANDIDATE-01",
    "WK-SW-CANDIDATE-01",
    "OBS-CANDIDATE-01",
)
SOURCE_IDENTITIES = {
    "docs/standards/deas/v1/standard.md": "df1644513d48022a3b9f01392fa33e391680b0d1e9341594fbc272ee44237586",
    "docs/standards/deas/v1/deas-v1-sha256.txt": "3f40080f3cd725db8906385abb6f7db79fadef5a231cf6bc9206b2fa43863c88",
    "contexts/operational-system/docs/program/v1/requirements.md": "addb4d5c564866ad7115fa40b6e36189e3cb54397224d6c805a11fc431b168c0",
    "contexts/operational-system/docs/program/v1/decisions.md": "21cd53b6f0c4fc8a1da7f08266553047dac4e801ecfe72b6e49842b5e7104fe2",
    "contexts/operational-system/docs/program/v1/evidence-and-audit-plan.md": "531e5e1c60e032d27740962050b76dd285417993884ae7c4079efc8e4c90d537",
    "contexts/operational-system/docs/program/v1/fault-test-matrix.md": "f6e025c572bac2ad7ac4b22ba481f14aa6372b63f3a8fa67ae5cff39a7d59e89",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/handoff.md": "89eafe6a547a3e75e1c75a1cbdba6db88f1edf97375bfac24ae794187273cf0b",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/discrepancies-and-unknowns.md": "f218d8b2441fee8b47f212ebeaf3a66cdc840e2dc055d58724dfe20bd88071fb",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/current-mac-baseline.md": "213ca5d2b87832c3694cbe988d8d2c02a0526e4fac36654684e5fdca12834875",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/seagate-device-volume.md": "117bcee90efae84ab4803886247e8563069f5c12454957ef7564cb3c6f0db169",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/worker-candidate.md": "e015cce0e1a58e5e608251fe38befc040ac681c7725f449eac9cc1a54df308d3",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/observer-surface.md": "b2177563e81dd1dbd57cf5dafad286e5b1abf1f6d4f5b8c9a0d8efea9fc21fb2",
}


class ValidationError(Exception):
    """A deterministic input or execution failure."""

    def __init__(self, message: str, path: str = VALIDATOR_RELATIVE) -> None:
        super().__init__(message)
        self.path = path


class Phase3ArgumentParser(argparse.ArgumentParser):
    """Route argument failures through the structured error seam."""

    def error(self, message: str) -> None:
        raise ValidationError(f"invalid arguments: {message}", "command-line")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def rooted_path(root: Path, relative: str) -> Path:
    candidate = Path(relative)
    if candidate.is_absolute():
        raise ValidationError(f"absolute path is prohibited: {relative}", relative)
    resolved = (root / candidate).resolve()
    if resolved != root and root not in resolved.parents:
        raise ValidationError(f"path escapes repository root: {relative}", relative)
    return resolved


def read_bytes(root: Path, relative: str) -> bytes:
    path = rooted_path(root, relative)
    if path.is_symlink() or not path.is_file():
        raise ValidationError(f"missing or non-regular required file: {relative}", relative)
    try:
        size = path.stat().st_size
        if size > MAX_TEXT_BYTES:
            raise ValidationError(f"input exceeds {MAX_TEXT_BYTES} bytes: {relative}", relative)
        return path.read_bytes()
    except OSError as error:
        raise ValidationError(f"cannot read required file: {relative}", relative) from error


def read_text(root: Path, relative: str) -> str:
    try:
        return read_bytes(root, relative).decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValidationError(f"required file is not UTF-8: {relative}", relative) from error


def load_json(root: Path, relative: str) -> dict[str, object]:
    def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
        parsed: dict[str, object] = {}
        for key, item in pairs:
            if key in parsed:
                raise ValidationError(f"duplicate JSON key: {key}", relative)
            parsed[key] = item
        return parsed

    try:
        value = json.loads(read_text(root, relative), object_pairs_hook=reject_duplicate_keys)
    except json.JSONDecodeError as error:
        raise ValidationError(f"required file is not valid JSON: {relative}", relative) from error
    if not isinstance(value, dict):
        raise ValidationError(f"JSON root must be an object: {relative}", relative)
    return value


def finding(rule_id: str, path: str, message: str) -> dict[str, str]:
    return {"rule_id": rule_id, "path": path, "message": message}


def verify_package_file_set(root: Path) -> None:
    for relative in PACKAGE_FILES:
        read_bytes(root, relative)
    package_root = rooted_path(root, PACKAGE_PREFIX)
    observed = tuple(
        sorted(str(path.relative_to(root)) for path in package_root.rglob("*") if path.is_file())
    )
    expected = tuple(sorted(path for path in PACKAGE_FILES if path.startswith(PACKAGE_PREFIX)))
    if observed != expected:
        raise ValidationError("Phase 3 package file set differs from the exact allowlist", PACKAGE_PREFIX)


def verify_sources(root: Path) -> None:
    register = read_text(root, f"{PACKAGE_PREFIX}/source-register.md")
    for relative, expected in SOURCE_IDENTITIES.items():
        actual = sha256_bytes(read_bytes(root, relative))
        if actual != expected:
            raise ValidationError(f"source identity differs: {relative}", relative)
        if relative not in register or expected not in register:
            raise ValidationError(f"source register omits exact identity: {relative}", relative)


def verify_manifest(root: Path, expected_digest: str) -> None:
    raw = read_bytes(root, MANIFEST_RELATIVE)
    if sha256_bytes(raw) != expected_digest:
        raise ValidationError("Phase 3 manifest external digest differs", MANIFEST_RELATIVE)
    entries: list[tuple[str, str]] = []
    for number, line in enumerate(raw.decode("utf-8").splitlines(), start=1):
        match = MANIFEST_LINE.fullmatch(line)
        if match is None:
            raise ValidationError(f"malformed manifest line {number}", MANIFEST_RELATIVE)
        entries.append((match.group(1), match.group(2)))
    paths = tuple(path for _, path in entries)
    if paths != tuple(sorted(MANIFESTED_FILES)) or len(set(paths)) != len(paths):
        raise ValidationError("manifest path set or order differs", MANIFEST_RELATIVE)
    for expected, relative in entries:
        if sha256_bytes(read_bytes(root, relative)) != expected:
            raise ValidationError(f"manifest hash mismatch: {relative}", relative)


def evidence_labels(root: Path) -> tuple[str, ...]:
    standard = read_text(root, "docs/standards/deas/v1/standard.md")
    if EVIDENCE_SCHEMA_START not in standard or EVIDENCE_SCHEMA_END not in standard:
        raise ValidationError("DEAS evidence schema markers are missing", "docs/standards/deas/v1/standard.md")
    section = standard.split(EVIDENCE_SCHEMA_START, 1)[1].split(EVIDENCE_SCHEMA_END, 1)[0]
    labels = tuple(re.findall(r"\|\s*\d+\s*\|\s*`([^`]+)`\s*\|", section))
    if len(labels) != 23 or len(set(labels)) != 23:
        raise ValidationError("DEAS evidence schema does not contain 23 unique labels", "docs/standards/deas/v1/standard.md")
    return labels


def verify_evidence_contracts(root: Path) -> list[dict[str, str]]:
    labels = evidence_labels(root)
    findings: list[dict[str, str]] = []
    for relative, identifiers in EVIDENCE_FILES.items():
        text = read_text(root, relative)
        lines = text.splitlines()
        for label in labels:
            matches = [line for line in lines if line.startswith(f"- {label} ")]
            if len(matches) != 1 or not matches[0].removeprefix(f"- {label} ").strip():
                findings.append(finding("DEAS-EVIDENCE-001", relative, f"evidence label count/value differs: {label}"))
        evidence_line = next((line for line in lines if line.startswith("- **Evidence ID:** ")), "")
        for identifier in identifiers:
            if identifier not in evidence_line:
                findings.append(finding("DEAS-TRACE-001", relative, f"evidence identity missing: {identifier}"))
    return findings


def parse_dispositions(root: Path) -> tuple[dict[str, str], list[dict[str, str]]]:
    relative = f"{PACKAGE_PREFIX}/role-dispositions.md"
    text = read_text(root, relative)
    findings: list[dict[str, str]] = []
    if DISPOSITION_START not in text or DISPOSITION_END not in text:
        return {}, [finding("DEAS-PHASE-001", relative, "disposition table markers are missing")]
    section = text.split(DISPOSITION_START, 1)[1].split(DISPOSITION_END, 1)[0]
    rows: dict[str, str] = {}
    for line in section.splitlines():
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] in CANDIDATES and len(cells) >= 5:
            if cells[0] in rows:
                findings.append(finding("DEAS-PHASE-001", relative, f"duplicate candidate: {cells[0]}"))
            rows[cells[0]] = cells[3]
    if set(rows) != set(CANDIDATES):
        findings.append(finding("DEAS-PHASE-001", relative, "candidate disposition set differs"))
    for candidate, value in rows.items():
        if value != "BLOCKED_PENDING_EVIDENCE":
            findings.append(finding("DEAS-PHASE-001", relative, f"unsupported disposition for {candidate}: {value}"))
    return rows, findings


def verify_task(root: Path) -> list[dict[str, str]]:
    relative = f"{PACKAGE_PREFIX}/degs/phase3-task.json"
    task = load_json(root, relative)
    findings: list[dict[str, str]] = []
    expectations = {
        "task_id": TASK_ID,
        "risk_tier": "TIER_1",
        "authority_lane": "TAYLOR_AI_WORKBENCH",
        "status": "READY_FOR_EXECUTION",
    }
    for field, value in expectations.items():
        if task.get(field) != value:
            findings.append(finding("DEAS-PHASE-001", relative, f"task {field} differs"))
    if set(task.get("affected_files", [])) != set(PACKAGE_FILES):
        findings.append(finding("DEAS-PRE-003", relative, "task affected_files differs from exact package"))
    review = task.get("independent_review")
    post_action = task.get("post_action_validation")
    if not isinstance(review, dict) or review.get("status") != "PENDING":
        findings.append(finding("DEAS-PHASE-001", relative, "embedded review must remain PENDING"))
    if not isinstance(post_action, dict) or post_action.get("status") != "PENDING":
        findings.append(finding("DEAS-PHASE-001", relative, "post-action validation must remain PENDING"))
    return findings


def verify_lifecycle_and_trace(root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    plan_path = f"{PACKAGE_PREFIX}/architecture-plan.md"
    lifecycle_fields = (
        (
            plan_path,
            "Package state:",
            "- Package state: `PACKAGE_PASS_READY_FOR_GIT_DELIVERY`",
            "architecture plan package state differs",
        ),
        (
            f"{PACKAGE_PREFIX}/handoff.md",
            "Package state:",
            "- Package state: `READY_FOR_GIT_DELIVERY`",
            "handoff package state differs",
        ),
        (
            f"{PACKAGE_PREFIX}/validation/validation-report.md",
            "**Status:**",
            "- **Status:** PACKAGE_PASS_READY_FOR_GIT_DELIVERY",
            "validation report package state differs",
        ),
    )
    for relative, marker, expected, message in lifecycle_fields:
        text = read_text(root, relative)
        if [line for line in text.splitlines() if marker in line] != [expected]:
            findings.append(finding("DEAS-PHASE-001", relative, message))
    program_path = "contexts/operational-system/docs/program/v1/program-definition.md"
    program = read_text(root, program_path)
    if "`open-decisions.md`" in program:
        findings.append(finding("DEAS-PRE-009", program_path, "stale decisions source reference remains"))
    if program.count("`decisions.md`") != 2:
        findings.append(finding("DEAS-PRE-009", program_path, "canonical decisions source reference count differs"))
    required_states = (
        "contexts/operational-system/README.md",
        "contexts/operational-system/docs/program/v1/program-definition.md",
        f"{PACKAGE_PREFIX}/architecture-plan.md",
        f"{PACKAGE_PREFIX}/role-dispositions.md",
        f"{PACKAGE_PREFIX}/handoff.md",
        f"{PACKAGE_PREFIX}/validation/validation-report.md",
    )
    for relative in required_states:
        text = read_text(root, relative)
        for state in ("NOT_YET_QUALIFIED", "NOT_YET_RELEASED"):
            if state not in text:
                findings.append(finding("DEAS-PHASE-001", relative, f"required system state missing: {state}"))
    trace_path = "contexts/operational-system/docs/program/v1/traceability-matrix.md"
    trace = read_text(root, trace_path)
    for identifiers in EVIDENCE_FILES.values():
        for identifier in identifiers:
            if identifier not in trace:
                findings.append(finding("DEAS-TRACE-001", trace_path, f"trace identity missing: {identifier}"))
    if "`EV-P3-*` through `EV-P8-*`" in trace:
        findings.append(finding("DEAS-TRACE-001", trace_path, "stale aggregate Phase 3 future reservation remains"))
    return findings


def verify_links(root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for relative in PACKAGE_FILES:
        if not relative.endswith(".md"):
            continue
        text = read_text(root, relative)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            path_text = target.split("#", 1)[0]
            if not path_text or "://" in path_text or path_text.startswith("mailto:"):
                continue
            resolved = (rooted_path(root, relative).parent / path_text).resolve()
            if (resolved != root and root not in resolved.parents) or not resolved.exists():
                findings.append(finding("DEAS-PRE-009", relative, f"unresolved local link: {target}"))
    return findings


def validate(root: Path, manifest_digest: str) -> tuple[dict[str, object], int]:
    verify_package_file_set(root)
    verify_sources(root)
    verify_manifest(root, manifest_digest)
    findings = verify_evidence_contracts(root)
    dispositions, disposition_findings = parse_dispositions(root)
    findings.extend(disposition_findings)
    findings.extend(verify_task(root))
    findings.extend(verify_lifecycle_and_trace(root))
    findings.extend(verify_links(root))
    decision = "PASS" if not findings else "FAIL"
    payload: dict[str, object] = {
        "schema_version": 1,
        "decision": decision,
        "decision_scope": "PACKAGE",
        "package": "PHASE_3_ARCHITECTURE_AND_DISPOSITION",
        "manifest_sha256": manifest_digest,
        "candidate_count": len(dispositions),
        "role_dispositions": dispositions,
        "system_status": ["NOT_YET_QUALIFIED", "NOT_YET_RELEASED"],
        "external_gates_pending": ["G7", "G8", "G9"],
        "finding_count": len(findings),
        "findings": findings,
    }
    return payload, 0 if not findings else 1


def error_payload(error: ValidationError) -> dict[str, object]:
    return {
        "schema_version": 1,
        "decision": "ERROR",
        "decision_scope": "PACKAGE",
        "package": "PHASE_3_ARCHITECTURE_AND_DISPOSITION",
        "finding_count": 1,
        "findings": [finding("DEAS-PRE-007", error.path, str(error))],
    }


def parse_arguments(arguments: list[str]) -> argparse.Namespace:
    parser = Phase3ArgumentParser()
    parser.add_argument("--repository-root", required=True)
    parser.add_argument("--manifest-sha256", required=True)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args(arguments)


def main(arguments: list[str] | None = None) -> int:
    use_arguments = sys.argv[1:] if arguments is None else arguments
    json_requested = "--json" in use_arguments
    try:
        parsed = parse_arguments(use_arguments)
        root = Path(parsed.repository_root).resolve()
        if root != SCRIPT_ROOT:
            raise ValidationError("repository root differs from validator root", "command-line")
        if SHA256_VALUE.fullmatch(parsed.manifest_sha256) is None:
            raise ValidationError("manifest SHA-256 must be 64 lowercase hexadecimal characters", "command-line")
        payload, exit_code = validate(root, parsed.manifest_sha256)
    except ValidationError as error:
        payload, exit_code = error_payload(error), 2
    if json_requested:
        print(json.dumps(payload, sort_keys=True))
    else:
        print(f"PHASE3_PACKAGE_VALIDATION: {payload['decision']}")
        for item in payload.get("findings", []):
            print(f"- {item['rule_id']} {item['path']}: {item['message']}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
