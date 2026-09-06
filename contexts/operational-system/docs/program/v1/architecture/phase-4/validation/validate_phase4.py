#!/usr/bin/env python3
"""Validate the exact Phase 4 Software Core package through a public seam."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import selectors
import subprocess
import sys
import time
from pathlib import Path


TASK_ID = "DEGS-T2-DW-HWSW-P4-SOFTWARE-CORE-20260906"
BASE_COMMIT = "b24c6d677d80b5299f09cb087d263d69bd6b68af"
SPEC_SHA256 = "a55cf68fd597767da88b0ab768d5c58469c612924a70e2f299dd285feb9293d5"
PREFIX = "contexts/operational-system/docs/program/v1/architecture/phase-4"
SOFTWARE = "contexts/operational-system/software/phase4"
MANIFEST_RELATIVE = f"{PREFIX}/phase-4-sha256.txt"
VALIDATOR_RELATIVE = f"{PREFIX}/validation/validate_phase4.py"
MAX_FILE_BYTES = 1024 * 1024
MAX_COMMAND_OUTPUT = 64 * 1024
MAX_TREE_ENTRIES = 128
EXPECTED_MODULE_TESTS = 63
SHA256 = re.compile(r"^[0-9a-f]{64}$")
MANIFEST_LINE = re.compile(r"^([0-9a-f]{64})  ([^\s].*)$")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EVIDENCE_START = "<!-- DEAS-EVIDENCE-SCHEMA:START -->"
EVIDENCE_END = "<!-- DEAS-EVIDENCE-SCHEMA:END -->"
PACKAGE_FILES = (
    "contexts/operational-system/README.md",
    "contexts/operational-system/docs/program/v1/program-definition.md",
    "contexts/operational-system/docs/program/v1/traceability-matrix.md",
    f"{PREFIX}/software-core-plan.md",
    f"{PREFIX}/worker-core-evidence.md",
    f"{PREFIX}/observer-core-evidence.md",
    f"{PREFIX}/security-and-supply-evidence.md",
    f"{PREFIX}/source-register.md",
    f"{PREFIX}/handoff.md",
    f"{PREFIX}/degs/phase4-task.json",
    VALIDATOR_RELATIVE,
    f"{PREFIX}/validation/test_validate_phase4.py",
    f"{PREFIX}/validation/validation-report.md",
    MANIFEST_RELATIVE,
    f"{SOFTWARE}/README.md",
    f"{SOFTWARE}/worker_core.py",
    f"{SOFTWARE}/observer_core.py",
    f"{SOFTWARE}/test_worker_core.py",
    f"{SOFTWARE}/test_observer_core.py",
    f"{SOFTWARE}/fixtures/job-envelope.json",
    f"{SOFTWARE}/fixtures/input-records.json",
    f"{SOFTWARE}/fixtures/observer-snapshot.json",
    f"{SOFTWARE}/fixtures/observer-policy.json",
    f"{SOFTWARE}/fixtures/expected-result.json",
    f"{SOFTWARE}/fixtures/expected-observer-record.json",
)
MANIFESTED_FILES = tuple(path for path in PACKAGE_FILES if path != MANIFEST_RELATIVE)
SOURCE_IDENTITIES = {
    "docs/standards/deas/v1/standard.md": "df1644513d48022a3b9f01392fa33e391680b0d1e9341594fbc272ee44237586",
    "docs/standards/deas/v1/deas-v1-sha256.txt": "3f40080f3cd725db8906385abb6f7db79fadef5a231cf6bc9206b2fa43863c88",
    "contexts/operational-system/docs/program/v1/requirements.md": "addb4d5c564866ad7115fa40b6e36189e3cb54397224d6c805a11fc431b168c0",
    "contexts/operational-system/docs/program/v1/decisions.md": "21cd53b6f0c4fc8a1da7f08266553047dac4e801ecfe72b6e49842b5e7104fe2",
    "contexts/operational-system/docs/program/v1/evidence-and-audit-plan.md": "531e5e1c60e032d27740962050b76dd285417993884ae7c4079efc8e4c90d537",
    "contexts/operational-system/docs/program/v1/fault-test-matrix.md": "f6e025c572bac2ad7ac4b22ba481f14aa6372b63f3a8fa67ae5cff39a7d59e89",
    "contexts/operational-system/docs/program/v1/architecture/phase-3/phase-3-sha256.txt": "ba00d974a9a982e750aef49a2cd52e3a57bc9bec7020ed7131c4ba575ebacb7d",
    "contexts/operational-system/docs/program/v1/architecture/phase-3/handoff.md": "a7b7c5b4c3b578067da9bcb8b932d175d15cd15288bf0ff4b2b52f4565ef8c56",
    f"{SOFTWARE}/fixtures/job-envelope.json": "57fe274106d1f3a129f6fe2c8bea1d3247925b1ba51f6221b3e8c8a35cc3d894",
    f"{SOFTWARE}/fixtures/input-records.json": "d4dcacb9c25b2758e28a4cc218193645f004a8f880c42c515498a259e177aa36",
    f"{SOFTWARE}/fixtures/expected-result.json": "1099ce46272a14af8ba7372857c0f634a2feb2d20ade0ce2a96a6dfdc56d6fae",
    f"{SOFTWARE}/fixtures/observer-policy.json": "9246169419e7e0b8dee9280667208f2f632a83a97f13c065188df2ac5b32683b",
    f"{SOFTWARE}/fixtures/observer-snapshot.json": "2c0d8abdcaa3d63c7517b7768ebbb7121cc7472aa7c9956dd7bf3c420498ddd1",
    f"{SOFTWARE}/fixtures/expected-observer-record.json": "711a2d9fdc2a253a672ca3e054af4e1dda3de5c295f95e4b12f8fe5ae832e6a3",
}
EVIDENCE_FILES = {
    f"{PREFIX}/worker-core-evidence.md": (
        "EV-P4-JOB-CONTRACT", "EV-P4-WORKER-TEST", "EV-P4-WORKER-NEGATIVE-TEST",
        "EV-P4-WORKER-FAILURE-TEST", "EV-P4-HANDBACK-TEST", "EV-P4-PROMOTION-NEGATIVE-TEST",
    ),
    f"{PREFIX}/observer-core-evidence.md": (
        "EV-P4-OBSERVER-SECURITY-TEST", "EV-P4-OBSERVER-SCHEMA", "EV-P4-OBSERVER-TEST",
        "EV-P4-OBSERVER-PRIVACY-TEST", "EV-P4-OBSERVER-FAILURE-TEST", "EV-P4-RETENTION-TEST",
    ),
    f"{PREFIX}/security-and-supply-evidence.md": (
        "EV-P4-SECURITY-TEST", "EV-P4-PROMOTION-CONTRACT", "EV-P4-SECRET-HYGIENE",
        "EV-P4-ARTIFACT-IDENTITY", "EV-P4-SUPPLY-FAILURE-TEST",
    ),
    f"{PREFIX}/validation/validation-report.md": ("EV-P4-SW-TEST",),
}
EVIDENCE_ARTIFACTS = {
    f"{PREFIX}/worker-core-evidence.md": (
        f"{PREFIX}/worker-core-evidence.md",
        f"{PREFIX}/validation/validation-report.md",
        f"{SOFTWARE}/worker_core.py", f"{SOFTWARE}/test_worker_core.py",
        f"{SOFTWARE}/fixtures/job-envelope.json", f"{SOFTWARE}/fixtures/input-records.json",
        f"{SOFTWARE}/fixtures/expected-result.json",
    ),
    f"{PREFIX}/observer-core-evidence.md": (
        f"{PREFIX}/observer-core-evidence.md",
        f"{PREFIX}/validation/validation-report.md",
        f"{SOFTWARE}/observer_core.py", f"{SOFTWARE}/test_observer_core.py",
        f"{SOFTWARE}/fixtures/observer-snapshot.json", f"{SOFTWARE}/fixtures/observer-policy.json",
        f"{SOFTWARE}/fixtures/expected-observer-record.json",
    ),
    f"{PREFIX}/security-and-supply-evidence.md": (
        f"{PREFIX}/security-and-supply-evidence.md", f"{PREFIX}/source-register.md",
        f"{PREFIX}/software-core-plan.md", f"{PREFIX}/validation/validation-report.md",
        MANIFEST_RELATIVE, f"{SOFTWARE}/worker_core.py", f"{SOFTWARE}/observer_core.py",
        f"{SOFTWARE}/test_worker_core.py", f"{SOFTWARE}/test_observer_core.py",
    ),
    f"{PREFIX}/validation/validation-report.md": (
        f"{PREFIX}/validation/validation-report.md", VALIDATOR_RELATIVE,
        f"{PREFIX}/validation/test_validate_phase4.py", MANIFEST_RELATIVE,
        f"{SOFTWARE}/worker_core.py", f"{SOFTWARE}/observer_core.py",
        f"{SOFTWARE}/test_worker_core.py", f"{SOFTWARE}/test_observer_core.py",
    ),
}
TRACE_REQUIREMENTS = {
    "REQ-CP-004": ("EV-P4-JOB-CONTRACT", "EV-P4-WORKER-TEST"),
    "REQ-CP-009": ("EV-P4-SECRET-HYGIENE",),
    "REQ-WK-004": ("EV-P4-JOB-CONTRACT", "EV-P4-WORKER-TEST"),
    "REQ-WK-005": ("EV-P4-JOB-CONTRACT", "EV-P4-WORKER-TEST"),
    "REQ-WK-006": ("EV-P4-WORKER-NEGATIVE-TEST",),
    "REQ-WK-007": ("EV-P4-WORKER-FAILURE-TEST",),
    "REQ-WK-008": ("EV-P4-HANDBACK-TEST",),
    "REQ-WK-009": ("EV-P4-PROMOTION-NEGATIVE-TEST",),
    "REQ-OBS-001": ("EV-P4-OBSERVER-SECURITY-TEST",),
    "REQ-OBS-003": ("EV-P4-OBSERVER-SCHEMA", "EV-P4-OBSERVER-TEST"),
    "REQ-OBS-004": ("EV-P4-OBSERVER-PRIVACY-TEST",),
    "REQ-OBS-006": ("EV-P4-OBSERVER-FAILURE-TEST",),
    "REQ-OBS-007": ("EV-P4-OBSERVER-SCHEMA", "EV-P4-OBSERVER-FAILURE-TEST"),
    "REQ-OBS-008": ("EV-P4-RETENTION-TEST",),
    "REQ-ASS-002": ("EV-P4-ARTIFACT-IDENTITY",),
    "REQ-ASS-003": ("EV-P4-SW-TEST",),
}


class ValidationError(Exception):
    """A deterministic validator input or execution error."""

    def __init__(self, message: str, path: str = VALIDATOR_RELATIVE, rule_id: str = "DEAS-INPUT-001") -> None:
        super().__init__(message)
        self.path = path
        self.rule_id = rule_id


class Phase4ArgumentParser(argparse.ArgumentParser):
    """Route command-line errors through structured output."""

    def error(self, message: str) -> None:
        raise ValidationError(f"invalid arguments: {message}", "command-line")


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _finding(rule_id: str, path: str, message: str) -> dict:
    return {"message": message, "path": path, "rule_id": rule_id}


def _rooted(root: Path, relative: str) -> Path:
    candidate = Path(relative)
    if candidate.is_absolute():
        raise ValidationError("absolute repository-relative path is prohibited", relative)
    path = root / candidate
    parent = path.parent.resolve()
    if parent != root and root not in parent.parents:
        raise ValidationError("path escapes repository root", relative)
    return path


def _read(root: Path, relative: str, findings: list) -> bytes:
    try:
        path = _rooted(root, relative)
        if path.is_symlink() or not path.is_file():
            findings.append(_finding("DEAS-PATH-001", relative, "required regular file is missing"))
            return b""
        size = path.stat().st_size
        if size > MAX_FILE_BYTES:
            findings.append(_finding("DEAS-BOUND-001", relative, f"file exceeds {MAX_FILE_BYTES} bytes"))
            return b""
        return path.read_bytes()
    except (OSError, RuntimeError, ValidationError):
        findings.append(_finding("DEAS-PATH-001", relative, "required file cannot be read"))
        return b""


def _text(root: Path, relative: str, findings: list) -> str:
    raw = _read(root, relative, findings)
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        findings.append(_finding("DEAS-STATIC-001", relative, "required file is not UTF-8"))
        return ""


def _json_object(root: Path, relative: str, findings: list):
    def reject_duplicates(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key: {key}")
            result[key] = value
        return result

    try:
        value = json.loads(_text(root, relative, findings), object_pairs_hook=reject_duplicates)
    except (json.JSONDecodeError, RecursionError, ValueError) as error:
        findings.append(_finding("DEAS-LIFECYCLE-001", relative, f"invalid or duplicate-key JSON: {error}"))
        return None
    if not isinstance(value, dict):
        findings.append(_finding("DEAS-LIFECYCLE-001", relative, "JSON root is not an object"))
        return None
    return value


def _bounded_files(root: Path, base: Path, findings: list) -> set:
    observed = set()
    pending = [base]
    entries_seen = 0
    while pending:
        current = pending.pop()
        try:
            with os.scandir(current) as entries:
                for entry in entries:
                    entries_seen += 1
                    relative = str(Path(entry.path).relative_to(root))
                    if entries_seen > MAX_TREE_ENTRIES:
                        findings.append(_finding("DEAS-BOUND-002", str(base.relative_to(root)), "package tree exceeds its entry bound"))
                        return observed
                    if entry.is_symlink():
                        observed.add(relative)
                    elif entry.is_dir(follow_symlinks=False):
                        pending.append(Path(entry.path))
                    elif entry.is_file(follow_symlinks=False):
                        observed.add(relative)
        except OSError:
            findings.append(_finding("DEAS-PATH-001", str(current.relative_to(root)), "package tree cannot be read"))
    return observed


def _verify_file_set(root: Path, findings: list) -> None:
    for relative in PACKAGE_FILES:
        _read(root, relative, findings)
    expected = {path for path in PACKAGE_FILES if path.startswith((PREFIX, SOFTWARE))}
    observed = set()
    for base in (_rooted(root, PREFIX), _rooted(root, SOFTWARE)):
        if base.is_symlink():
            findings.append(_finding("DEAS-PATH-001", str(base.relative_to(root)), "package directory is a symlink"))
        elif base.is_dir():
            observed.update(_bounded_files(root, base, findings))
    for extra in sorted(observed - expected):
        findings.append(_finding("DEAS-PATH-002", extra, "file is outside the exact package allowlist"))


def _verify_manifest(root: Path, expected_digest: str, findings: list) -> None:
    raw = _read(root, MANIFEST_RELATIVE, findings)
    if _sha256(raw) != expected_digest:
        raise ValidationError("supplied manifest digest does not identify the manifest", MANIFEST_RELATIVE)
    entries = []
    for number, line in enumerate(raw.decode("utf-8", errors="replace").splitlines(), start=1):
        match = MANIFEST_LINE.fullmatch(line)
        if match is None:
            findings.append(_finding("DEAS-MANIFEST-001", MANIFEST_RELATIVE, f"malformed line {number}"))
        else:
            entries.append((match.group(1), match.group(2)))
    paths = tuple(path for _, path in entries)
    if paths != tuple(sorted(MANIFESTED_FILES)) or len(paths) != len(set(paths)):
        findings.append(_finding("DEAS-MANIFEST-001", MANIFEST_RELATIVE, "manifest path set or order differs"))
    for expected, relative in entries:
        if relative in MANIFESTED_FILES and _sha256(_read(root, relative, findings)) != expected:
            findings.append(_finding("DEAS-MANIFEST-001", relative, "manifest hash differs"))


def _verify_external_spec(path: Path, supplied_digest: str) -> None:
    if not SHA256.fullmatch(supplied_digest) or supplied_digest != SPEC_SHA256:
        raise ValidationError("external specification identity differs", str(path), "DEAS-IDENTITY-001")
    try:
        if path.is_symlink() or not path.is_file() or _sha256(path.read_bytes()) != SPEC_SHA256:
            raise ValidationError("external specification bytes differ", str(path), "DEAS-IDENTITY-001")
    except OSError as error:
        raise ValidationError("external specification cannot be read", str(path), "DEAS-IDENTITY-001") from error


def _verify_sources(root: Path, findings: list) -> None:
    register = _text(root, f"{PREFIX}/source-register.md", findings)
    for relative, expected in SOURCE_IDENTITIES.items():
        actual = _sha256(_read(root, relative, findings))
        if actual != expected:
            findings.append(_finding("DEAS-SOURCE-001", relative, "frozen source identity differs"))
        row = f"| `{relative}` | `{expected}` |"
        if not any(line.startswith(row) for line in register.splitlines()):
            findings.append(_finding("DEAS-SOURCE-001", f"{PREFIX}/source-register.md", f"source identity omitted: {relative}"))


def _evidence_labels(root: Path, findings: list) -> tuple:
    relative = "docs/standards/deas/v1/standard.md"
    standard = _text(root, relative, findings)
    if EVIDENCE_START not in standard or EVIDENCE_END not in standard:
        findings.append(_finding("DEAS-EVIDENCE-001", relative, "canonical evidence schema markers are missing"))
        return ()
    section = standard.split(EVIDENCE_START, 1)[1].split(EVIDENCE_END, 1)[0]
    labels = tuple(re.findall(r"\|\s*\d+\s*\|\s*`([^`]+)`\s*\|", section))
    if len(labels) != 23 or len(set(labels)) != 23:
        findings.append(_finding("DEAS-EVIDENCE-001", relative, "canonical evidence labels differ"))
    return labels


def _verify_evidence(root: Path, findings: list) -> None:
    labels = _evidence_labels(root, findings)
    observed_ids = []
    for relative, expected_ids in EVIDENCE_FILES.items():
        lines = _text(root, relative, findings).splitlines()
        for label in labels:
            matches = [line for line in lines if line.startswith(f"- {label} ")]
            if len(matches) != 1 or not matches[0].removeprefix(f"- {label} ").strip():
                findings.append(_finding("DEAS-EVIDENCE-001", relative, f"label count/value differs: {label}"))
        identity = next((line for line in lines if line.startswith("- **Evidence ID:** ")), "")
        status = next((line for line in lines if line.startswith("- **Status:** ")), "")
        artifacts = next((line for line in lines if line.startswith("- **Artifact paths:** ")), "")
        accepted_status = "PACKAGE_PASS_READY_FOR_GIT_DELIVERY" if relative.endswith("validation-report.md") else "PASS"
        if status != f"- **Status:** {accepted_status}":
            findings.append(_finding("DEAS-LIFECYCLE-001", relative, "evidence status is not final package PASS"))
        if tuple(re.findall(r"`([^`]+)`", artifacts)) != EVIDENCE_ARTIFACTS[relative]:
            findings.append(_finding("DEAS-EVIDENCE-001", relative, "Artifact paths are not the exact repository-relative set"))
        identities = tuple(re.findall(r"`([^`]+)`", identity))
        if identities != expected_ids:
            findings.append(_finding("DEAS-EVIDENCE-001", relative, "Evidence ID set or order differs"))
        else:
            observed_ids.extend(identities)
    if len(observed_ids) != 18 or len(set(observed_ids)) != 18:
        findings.append(_finding("DEAS-EVIDENCE-001", PREFIX, "exact 18-identity evidence set differs"))


def _verify_task(root: Path, findings: list) -> None:
    relative = f"{PREFIX}/degs/phase4-task.json"
    task = _json_object(root, relative, findings)
    if task is None:
        return
    exact = {"task_id": TASK_ID, "authority_lane": "TAYLOR_AI_WORKBENCH", "risk_tier": "TIER_2", "status": "READY_FOR_EXECUTION"}
    for field, expected in exact.items():
        if task.get(field) != expected:
            findings.append(_finding("DEAS-LIFECYCLE-001", relative, f"task {field} differs"))
    if task.get("affected_files") != list(PACKAGE_FILES):
        findings.append(_finding("DEAS-PATH-001", relative, "affected_files differs from exact ordered package"))
    review, post = task.get("independent_review"), task.get("post_action_validation")
    if not isinstance(review, dict) or review.get("status") != "PENDING":
        findings.append(_finding("DEAS-LIFECYCLE-001", relative, "embedded independent review must remain PENDING"))
    if not isinstance(post, dict) or post.get("status") != "PENDING":
        findings.append(_finding("DEAS-LIFECYCLE-001", relative, "embedded post-action validation must remain PENDING"))
    for field in ("verification", "validation", "documentation", "handoff", "secret_handling"):
        value = task.get(field)
        status = value.get("status") if isinstance(value, dict) else None
        if not isinstance(status, str) or status not in {"PASS", "VERIFIED"}:
            findings.append(_finding("DEAS-LIFECYCLE-001", relative, f"task {field} is not final package PASS"))
    artifact = task.get("artifact_identity")
    if artifact != {"status": "PENDING"}:
        findings.append(_finding("DEAS-LIFECYCLE-001", relative, "embedded delivery artifact identity must remain PENDING"))


def _verify_lifecycle(root: Path, findings: list) -> None:
    handoff_relative = f"{PREFIX}/handoff.md"
    report_relative = f"{PREFIX}/validation/validation-report.md"
    handoff = _text(root, handoff_relative, findings)
    report = _text(root, report_relative, findings)
    expected = ("READY_FOR_GIT_DELIVERY", "NOT_YET_QUALIFIED", "NOT_YET_RELEASED", "Controlled integration action: `NOT_PERFORMED`", "NO_CONTROLLED_INTEGRATION_ACTION_SELECTED")
    for token in expected:
        if token not in handoff:
            findings.append(_finding("DEAS-AUTHORITY-001", handoff_relative, f"required lifecycle boundary is missing: {token}"))
    if "- **Status:** PACKAGE_PASS_READY_FOR_GIT_DELIVERY" not in report:
        findings.append(_finding("DEAS-LIFECYCLE-001", report_relative, "validation report package status differs"))
    prohibited = ("SYSTEM_RELEASED", "QUALIFIED_FOR_OPERATION", "INTEGRATION_PERFORMED")
    for token in prohibited:
        if token in handoff:
            findings.append(_finding("DEAS-AUTHORITY-001", handoff_relative, f"false authority claim: {token}"))


def _trace_row(text: str, requirement: str) -> str:
    prefix = f"| `{requirement}` |"
    return next((line for line in text.splitlines() if line.startswith(prefix)), "")


def _verify_trace(root: Path, findings: list) -> None:
    relative = "contexts/operational-system/docs/program/v1/traceability-matrix.md"
    text = _text(root, relative, findings)
    for requirement, identities in TRACE_REQUIREMENTS.items():
        row = _trace_row(text, requirement)
        if not row or any(f"`{identity}`" not in row for identity in identities) or "PRODUCED_SOFTWARE_CORE" not in row:
            findings.append(_finding("DEAS-TRACE-001", relative, f"Phase 4 trace differs: {requirement}"))
    if "| `EV-P4-*` through `EV-P8-*`" in text:
        findings.append(_finding("DEAS-TRACE-001", relative, "Phase 4 evidence remains globally represented as future"))


def _python_tree(root: Path, relative: str, findings: list):
    try:
        return ast.parse(_text(root, relative, findings), filename=relative)
    except SyntaxError as error:
        findings.append(_finding("DEAS-STATIC-001", relative, f"Python syntax error at line {error.lineno}"))
        return None


def _verify_python(root: Path, findings: list) -> None:
    module_paths = (f"{SOFTWARE}/worker_core.py", f"{SOFTWARE}/observer_core.py")
    python_paths = tuple(path for path in PACKAGE_FILES if path.endswith(".py"))
    forbidden = {"socket", "urllib", "http", "requests", "multiprocessing", "subprocess"}
    for relative in python_paths:
        tree = _python_tree(root, relative, findings)
        if tree is None:
            continue
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.end_lineno - node.lineno + 1 > 60:
                findings.append(_finding("DEAS-PRE-004", relative, f"function exceeds 60 lines: {node.name}"))
            if relative == VALIDATOR_RELATIVE and isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "wait":
                if not any(keyword.arg == "timeout" for keyword in node.keywords):
                    findings.append(_finding("DEAS-PRE-004", relative, "subprocess wait is not explicitly bounded"))
            if relative in module_paths and isinstance(node, (ast.Import, ast.ImportFrom)):
                names = [alias.name.split(".")[0] for alias in node.names] if isinstance(node, ast.Import) else [(node.module or "").split(".")[0]]
                if any(name in forbidden for name in names):
                    findings.append(_finding("DEAS-SECURITY-001", relative, "Module imports a prohibited network/process facility"))
    interfaces = {module_paths[0]: {"execute"}, module_paths[1]: {"collect", "retention_decision"}}
    for relative, allowed in interfaces.items():
        tree = _python_tree(root, relative, findings)
        if tree is None:
            continue
        target = "WorkerCore" if relative.endswith("worker_core.py") else "ObserverCore"
        class_node = next((node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == target), None)
        public = {node.name for node in class_node.body if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")} if class_node else set()
        if public != allowed:
            findings.append(_finding("DEAS-ARCH-001", relative, "public Module interface differs"))


def _verify_links(root: Path, findings: list) -> None:
    for relative in PACKAGE_FILES:
        if not relative.endswith(".md"):
            continue
        for target in MARKDOWN_LINK.findall(_text(root, relative, findings)):
            clean = target.split("#", 1)[0]
            if not clean or re.match(r"^[a-z]+://", clean) or clean.startswith("/"):
                continue
            try:
                destination = (_rooted(root, relative).parent / clean).resolve()
            except (OSError, RuntimeError, ValidationError):
                findings.append(_finding("DEAS-LINK-001", relative, f"link cannot be resolved: {target}"))
                continue
            if destination != root and root not in destination.parents:
                findings.append(_finding("DEAS-LINK-001", relative, f"link escapes repository: {target}"))
            elif not destination.exists():
                findings.append(_finding("DEAS-LINK-001", relative, f"unresolved link: {target}"))


def _bounded_command(command: list, root: Path, timeout: float):
    try:
        process = subprocess.Popen(command, cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0)
    except OSError:
        return None, b"", b"", "START_FAILED"
    selector = selectors.DefaultSelector()
    outputs = {process.stdout: bytearray(), process.stderr: bytearray()}
    for stream in outputs:
        selector.register(stream, selectors.EVENT_READ)
    deadline = time.monotonic() + timeout
    error = None
    while selector.get_map() and error is None:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            error = "TIMEOUT"
            break
        for key, _ in selector.select(min(remaining, 0.1)):
            chunk = os.read(key.fileobj.fileno(), min(65536, MAX_COMMAND_OUTPUT + 1 - sum(map(len, outputs.values()))))
            if chunk:
                outputs[key.fileobj].extend(chunk)
                if sum(map(len, outputs.values())) > MAX_COMMAND_OUTPUT:
                    error = "OUTPUT_LIMIT"
                    break
            else:
                selector.unregister(key.fileobj)
    if error is not None and process.poll() is None:
        process.kill()
    for stream in outputs:
        stream.close()
    selector.close()
    try:
        returncode = process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        process.kill()
        error = error or "TERMINATION_TIMEOUT"
        try:
            returncode = process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            returncode = None
    return returncode, bytes(outputs[process.stdout]), bytes(outputs[process.stderr]), error


def _run_module_tests(root: Path, findings: list) -> None:
    command = [sys.executable, "-B", "-m", "unittest", "discover", "-s", SOFTWARE, "-p", "test_*_core.py", "-q"]
    code, stdout, stderr, error = _bounded_command(command, root, 30)
    if error is not None or code != 0:
        detail = (stdout + stderr)[:1000].decode("utf-8", errors="replace").replace("\n", " ")
        findings.append(_finding("DEAS-TEST-001", SOFTWARE, f"Module public tests failed, timed out, or exceeded output bound: {error or code}; {detail}"))
        return
    grammar = rb"-{70}\nRan " + str(EXPECTED_MODULE_TESTS).encode() + rb" tests in [0-9.]+s\n\nOK\n?"
    if stdout or re.fullmatch(grammar, stderr) is None:
        findings.append(_finding("DEAS-TEST-001", SOFTWARE, "Module test diagnostics differ from the exact quiet-success grammar"))


def _git_paths(root: Path, arguments: list, findings: list):
    code, stdout, stderr, error = _bounded_command(["git", *arguments], root, 10)
    if error is not None or code != 0 or stderr:
        findings.append(_finding("DEAS-GIT-001", ".git", f"Git identity command failed: {error or code}"))
        return None
    try:
        return {item.decode("utf-8") for item in stdout.split(b"\0") if item}
    except UnicodeDecodeError:
        findings.append(_finding("DEAS-GIT-001", ".git", "Git path output is not UTF-8"))
        return None


def _verify_git_diff(root: Path, findings: list) -> None:
    if not (root / ".git").exists():
        findings.append(_finding("DEAS-GIT-001", ".git", "Git metadata is required for exact package identity"))
        return
    commands = (
        ["diff", "--name-only", "-z", f"{BASE_COMMIT}...HEAD", "--"],
        ["diff", "--name-only", "-z", "--"],
        ["diff", "--cached", "--name-only", "-z", "--"],
        ["ls-files", "--others", "--exclude-standard", "-z"],
    )
    observed = set()
    for command in commands:
        paths = _git_paths(root, command, findings)
        if paths is None:
            return
        observed.update(paths)
    if tuple(sorted(observed)) != tuple(sorted(PACKAGE_FILES)):
        findings.append(_finding("DEAS-GIT-001", ".git", "Git diff identity differs from exact package"))


def validate(root: Path, manifest_digest: str, spec: Path, spec_digest: str) -> dict:
    if Path(root).is_symlink():
        raise ValidationError("repository root symlink is prohibited", str(root))
    resolved = Path(root).resolve(strict=True)
    if not resolved.is_dir() or not SHA256.fullmatch(manifest_digest):
        raise ValidationError("repository root or manifest digest is invalid", str(root))
    _verify_external_spec(Path(spec), spec_digest)
    findings = []
    _verify_file_set(resolved, findings)
    _verify_manifest(resolved, manifest_digest, findings)
    _verify_sources(resolved, findings)
    _verify_evidence(resolved, findings)
    _verify_task(resolved, findings)
    _verify_lifecycle(resolved, findings)
    _verify_trace(resolved, findings)
    _verify_python(resolved, findings)
    _verify_links(resolved, findings)
    _run_module_tests(resolved, findings)
    _verify_git_diff(resolved, findings)
    findings.sort(key=lambda item: (item["rule_id"], item["path"], item["message"]))
    return _payload("PASS" if not findings else "FAIL", manifest_digest, findings)


def _payload(decision: str, manifest_digest: str, findings: list) -> dict:
    return {
        "controlled_integration_action": "NOT_PERFORMED",
        "decision": decision,
        "decision_scope": "PACKAGE",
        "external_gates_pending": ["G7", "G8", "G9"],
        "findings": findings,
        "manifest_sha256": manifest_digest,
        "schema_version": "dobeworks.phase4.validation.v1",
        "task_id": TASK_ID,
    }


def _parser() -> Phase4ArgumentParser:
    parser = Phase4ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", required=True)
    parser.add_argument("--manifest-sha256", required=True)
    parser.add_argument("--external-spec", required=True)
    parser.add_argument("--external-spec-sha256", required=True)
    parser.add_argument("--json", action="store_true", required=True)
    return parser


def main(argv=None) -> int:
    try:
        args = _parser().parse_args(argv)
        result = validate(Path(args.repository_root), args.manifest_sha256, Path(args.external_spec), args.external_spec_sha256)
        exit_code = 0 if result["decision"] == "PASS" else 1
    except (ValidationError, OSError) as error:
        digest = "UNKNOWN"
        rule_id = getattr(error, "rule_id", "DEAS-INPUT-001")
        result = _payload("ERROR", digest, [_finding(rule_id, getattr(error, "path", VALIDATOR_RELATIVE), str(error))])
        exit_code = 2
    except Exception as error:
        result = _payload("ERROR", "UNKNOWN", [_finding("DEAS-EXEC-001", VALIDATOR_RELATIVE, f"unexpected validator error: {type(error).__name__}")])
        exit_code = 2
    sys.stdout.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
