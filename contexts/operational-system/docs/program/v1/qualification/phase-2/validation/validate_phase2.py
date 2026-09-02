#!/usr/bin/env python3
"""Validate the intrinsic Phase 2 canonical Evidence Set without device access."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_MANIFEST_HASH = "1843787bab9fc0fb1ab77d58246d0f55feab53fbc5090da3072b69289e90a59c"

EXPECTED_FILES = {
    "qualification-plan.md",
    "source-register.md",
    "evidence/current-mac-baseline.md",
    "evidence/seagate-device-volume.md",
    "evidence/worker-candidate.md",
    "evidence/observer-surface.md",
    "discrepancies-and-unknowns.md",
    "evidence/command-log.md",
    "validation/validate_phase2.py",
    "validation/validation-report.md",
    "degs/phase2-task.json",
    "handoff.md",
    "evidence-sha256.txt",
}
HASHED_FILES = EXPECTED_FILES - {"evidence-sha256.txt"}
EXACT_COPY_FILES = {
    "source-register.md",
    "evidence/current-mac-baseline.md",
    "evidence/seagate-device-volume.md",
    "evidence/worker-candidate.md",
    "evidence/observer-surface.md",
    "discrepancies-and-unknowns.md",
    "evidence/command-log.md",
    "degs/phase2-task.json",
}


def run(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=False)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def find_workspace() -> Path | None:
    for candidate in (ROOT, *ROOT.parents):
        if (
            (candidate / "governance/bin/engineering-gate.py").is_file()
            and (candidate / "projects/dobeworks").is_dir()
        ):
            return candidate
    return None


def load_json(path: Path, errors: list[str], label: str) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(value, dict):
            return value
        errors.append(f"{label} root is not an object")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{label} is unreadable or invalid: {exc.__class__.__name__}")
    return {}


def main() -> int:
    errors: list[str] = []
    workspace = find_workspace()
    if workspace is None:
        print("PHASE2_CANONICAL_EVIDENCE_VALIDATION: FAIL")
        print("- canonical workspace could not be located")
        return 1

    source = workspace / ".scratch/dobeworks-hardware-software-v1-phase2-evidence"
    candidate_root = workspace / ".scratch/dobeworks-hardware-software-v1-phase2-canonical-promotion-definition/candidate"
    canonical_root = workspace / "projects/dobeworks/contexts/operational-system/docs/program/v1/qualification/phase-2"
    allowed_roots = {candidate_root, canonical_root}
    if ROOT not in allowed_roots:
        errors.append("evidence root is neither the frozen candidate nor canonical destination")

    actual_files = {
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*")
        if path.is_file()
    }
    if actual_files != EXPECTED_FILES:
        errors.append(
            f"evidence file set mismatch: missing={sorted(EXPECTED_FILES - actual_files)}, "
            f"extra={sorted(actual_files - EXPECTED_FILES)}"
        )
    for relative in actual_files:
        path = ROOT / relative
        if path.is_symlink() or not path.is_file():
            errors.append(f"evidence path is not a regular non-symlink file: {relative}")

    manifest = ROOT / "evidence-sha256.txt"
    entries: dict[str, str] = {}
    if manifest.is_file():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
            if not match:
                errors.append("evidence manifest contains a malformed line")
                continue
            digest, relative = match.groups()
            if relative in entries:
                errors.append(f"evidence manifest contains a duplicate path: {relative}")
            entries[relative] = digest
        if set(entries) != HASHED_FILES:
            errors.append("evidence manifest path set does not match the 12 non-self artifacts")
        for relative, digest in entries.items():
            path = ROOT / relative
            if not path.is_file() or sha256(path) != digest:
                errors.append(f"evidence hash mismatch: {relative}")
    else:
        errors.append("evidence manifest is absent")

    source_manifest = source / "evidence-sha256.txt"
    if not source_manifest.is_file() or sha256(source_manifest) != SOURCE_MANIFEST_HASH:
        errors.append("frozen staged-evidence manifest identity drift")
    else:
        check = run("shasum", "-a", "256", "-c", str(source_manifest), cwd=source)
        if check.returncode != 0:
            errors.append("frozen staged Evidence Set verification failed")

    for relative in EXACT_COPY_FILES:
        source_path = source / relative
        target_path = ROOT / relative
        if not source_path.is_file() or not target_path.is_file() or sha256(source_path) != sha256(target_path):
            errors.append(f"exact-copy identity mismatch: {relative}")

    task_path = ROOT / "degs/phase2-task.json"
    task = load_json(task_path, errors, "qualification DEGS task")
    if not (
        task.get("task_id") == "DEGS-T1-DW-HWSW-P2-QUAL-20260901"
        and task.get("status") == "COMPLETE"
        and task.get("risk_tier") == "TIER_1"
        and task.get("authority_lane") == "TAYLOR_AI_WORKBENCH"
        and task.get("unresolved_items") == []
        and all(item.get("resolved") is True for item in task.get("warnings", []) if isinstance(item, dict))
    ):
        errors.append("qualification DEGS task is incomplete or inconsistent")

    gate = workspace / "governance/bin/engineering-gate.py"
    for label in ("validate", "evaluate"):
        completed = run("python3", str(gate), label, str(task_path), cwd=workspace)
        if completed.returncode != 0 or not completed.stdout.startswith("Decision: PASS\n"):
            errors.append(f"qualification DEGS {label} is not PASS")

    combined = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix in {".md", ".json"}
    )
    patterns = {
        "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
        "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "OpenAI-like secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
        "absolute user path": re.compile(r"/Users/[^/\s]+"),
        "absolute volume path": re.compile(r"/Volumes/[^\s]+"),
        "raw disk identifier": re.compile(r"\bdisk\d+(?:s\d+)?\b", re.IGNORECASE),
        "UUID": re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.IGNORECASE),
        "email address": re.compile(r"\b[^\s@]+@[^\s@]+\.[^\s@]+\b"),
        "MAC address": re.compile(r"\b(?:[0-9a-f]{2}:){5}[0-9a-f]{2}\b", re.IGNORECASE),
    }
    for label, pattern in patterns.items():
        if pattern.search(combined):
            errors.append(f"prohibited or secret-like material detected: {label}")
    for prohibited_key in ("VolumeUUID", "DiskUUID", "MediaUUID", "DeviceIdentifier", "SerialNumber"):
        if prohibited_key in combined:
            errors.append(f"raw prohibited field name detected: {prohibited_key}")

    required = {
        "qualification-plan.md": ["DEGS-T1-DW-HWSW-P2-PROMOTE-20260901", SOURCE_MANIFEST_HASH, "NOT_YET_QUALIFIED", "NOT_YET_RELEASED"],
        "validation/validation-report.md": ["Qualification validation result:** `PASS`", SOURCE_MANIFEST_HASH, "Canonicalization treatment"],
        "handoff.md": ["Canonical state:** effective only after separately authorized promotion", SOURCE_MANIFEST_HASH, "NOT_YET_QUALIFIED", "NOT_YET_RELEASED"],
        "evidence/current-mac-baseline.md": ["CP-CANDIDATE-01", "UNKNOWN", "Role Disposition:** not assigned"],
        "evidence/seagate-device-volume.md": ["SR-CANDIDATE-01", "UNKNOWN", "Role Disposition:** not assigned"],
        "evidence/worker-candidate.md": ["WK-CANDIDATE-01", "BLOCKED_PENDING_EVIDENCE"],
        "evidence/observer-surface.md": ["OBS-SURFACE-01", "EXECUTABLE_PRESENCE_ONLY"],
    }
    for relative, markers in required.items():
        text = (ROOT / relative).read_text(encoding="utf-8") if (ROOT / relative).is_file() else ""
        for marker in markers:
            if marker not in text:
                errors.append(f"missing required marker in {relative}: {marker}")

    if "QUALIFIED_FOR_BOUNDED_ROLE" in combined or "QUALIFIED_OUT" in combined:
        errors.append("a forbidden Role Disposition was recorded")

    if errors:
        print("PHASE2_CANONICAL_EVIDENCE_VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    location = "CANDIDATE" if ROOT == candidate_root else "CANONICAL"
    print("PHASE2_CANONICAL_EVIDENCE_VALIDATION: PASS")
    print(f"location={location}")
    print("evidence_files=13")
    print("manifest_entries=12")
    print("exact_copies=8")
    print("reviewed_transforms=4")
    print("generated_manifests=1")
    print("staged_source=VERIFIED")
    print("qualification_degs=PASS")
    print("privacy_scan=PASS")
    print("role_disposition=NONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
