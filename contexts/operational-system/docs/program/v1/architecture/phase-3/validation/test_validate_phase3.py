#!/usr/bin/env python3
"""Public-seam tests for the Phase 3 package validator."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PACKAGE_PREFIX = "contexts/operational-system/docs/program/v1/architecture/phase-3"
VALIDATOR_RELATIVE = f"{PACKAGE_PREFIX}/validation/validate_phase3.py"
MANIFEST_RELATIVE = f"{PACKAGE_PREFIX}/phase-3-sha256.txt"
SOURCE_REPOSITORY = Path(__file__).resolve().parents[8]
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
SOURCE_FILES = (
    "CONTEXT-MAP.md",
    "docs/adr/0013-distinct-operational-system-context.md",
    "docs/standards/deas/v1/standard.md",
    "docs/standards/deas/v1/deas-v1-sha256.txt",
    "contexts/operational-system/CONTEXT.md",
    "contexts/operational-system/docs/program/v1/requirements.md",
    "contexts/operational-system/docs/program/v1/decisions.md",
    "contexts/operational-system/docs/program/v1/evidence-and-audit-plan.md",
    "contexts/operational-system/docs/program/v1/fault-test-matrix.md",
    "contexts/operational-system/docs/program/v1/phase-2-entry-criteria.md",
    "contexts/operational-system/docs/program/v1/provenance.md",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/handoff.md",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/discrepancies-and-unknowns.md",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/degs/phase2-generation-2-task.json",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/generation-2-sha256.txt",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/validation/validation-report.md",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/current-mac-baseline.md",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/seagate-device-volume.md",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/worker-candidate.md",
    "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/observer-surface.md",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def refresh_manifest(root: Path) -> str:
    manifest = root / MANIFEST_RELATIVE
    paths = [line.split("  ", 1)[1] for line in manifest.read_text(encoding="utf-8").splitlines()]
    manifest.write_text(
        "".join(f"{sha256(root / relative)}  {relative}\n" for relative in paths),
        encoding="utf-8",
    )
    return sha256(manifest)


class Phase3PublicCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "repo"
        for relative in (*PACKAGE_FILES, *SOURCE_FILES):
            source = SOURCE_REPOSITORY / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_cli(
        self,
        *,
        root: Path | None = None,
        digest: str | None = None,
    ) -> subprocess.CompletedProcess[str]:
        validator = self.root / VALIDATOR_RELATIVE
        return subprocess.run(
            [
                sys.executable,
                "-B",
                str(validator),
                "--repository-root",
                str(self.root if root is None else root),
                "--manifest-sha256",
                sha256(self.root / MANIFEST_RELATIVE) if digest is None else digest,
                "--json",
            ],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=False,
            timeout=10,
        )

    def assert_rejected(self, result: subprocess.CompletedProcess[str], marker: str) -> None:
        self.assertIn(result.returncode, {1, 2})
        self.assertEqual("", result.stderr)
        payload = json.loads(result.stdout)
        self.assertIn(payload["decision"], {"FAIL", "ERROR"})
        self.assertGreaterEqual(payload["finding_count"], 1)
        self.assertIn(marker, "\n".join(item["message"] for item in payload["findings"]))

    def test_exact_package_passes(self) -> None:
        result = self.run_cli()
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual("", result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual("PASS", payload["decision"])
        self.assertEqual("PACKAGE", payload["decision_scope"])
        self.assertEqual(5, payload["candidate_count"])
        self.assertEqual({candidate: "BLOCKED_PENDING_EVIDENCE" for candidate in (
            "CP-CANDIDATE-01", "SR-CANDIDATE-01", "WK-CANDIDATE-01",
            "WK-SW-CANDIDATE-01", "OBS-CANDIDATE-01",
        )}, payload["role_dispositions"])

    def test_missing_package_file_is_rejected(self) -> None:
        (self.root / f"{PACKAGE_PREFIX}/role-architecture.md").unlink()
        self.assert_rejected(self.run_cli(), "missing or non-regular required file")

    def test_unexpected_package_file_is_rejected(self) -> None:
        (self.root / f"{PACKAGE_PREFIX}/unexpected.md").write_text("unexpected\n", encoding="utf-8")
        self.assert_rejected(self.run_cli(), "file set differs")

    def test_invalid_disposition_is_rejected_after_rehash(self) -> None:
        path = self.root / f"{PACKAGE_PREFIX}/role-dispositions.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace(
            "| `BLOCKED_PENDING_EVIDENCE` |",
            "| `QUALIFIED_FOR_BOUNDED_ROLE` |",
            1,
        ), encoding="utf-8")
        digest = refresh_manifest(self.root)
        self.assert_rejected(self.run_cli(digest=digest), "unsupported disposition")

    def test_missing_evidence_field_is_rejected_after_rehash(self) -> None:
        path = self.root / f"{PACKAGE_PREFIX}/data-and-signal-map.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(line for line in lines if not line.startswith(
            "- **Current freshness:**"
        )) + "\n", encoding="utf-8")
        digest = refresh_manifest(self.root)
        self.assert_rejected(self.run_cli(digest=digest), "evidence label count/value differs")

    def test_manifest_hash_mismatch_is_rejected(self) -> None:
        path = self.root / f"{PACKAGE_PREFIX}/role-architecture.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
        self.assert_rejected(self.run_cli(), "manifest hash mismatch")

    def test_external_manifest_digest_mismatch_is_rejected(self) -> None:
        self.assert_rejected(self.run_cli(digest="0" * 64), "external digest differs")

    def test_false_qualification_claim_is_rejected_after_rehash(self) -> None:
        path = self.root / f"{PACKAGE_PREFIX}/handoff.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("NOT_YET_QUALIFIED", "QUALIFIED", 1), encoding="utf-8")
        digest = refresh_manifest(self.root)
        self.assert_rejected(self.run_cli(digest=digest), "required system state missing")

    def test_source_drift_is_rejected(self) -> None:
        path = self.root / "contexts/operational-system/docs/program/v1/requirements.md"
        path.write_text(path.read_text(encoding="utf-8") + "\ndrift\n", encoding="utf-8")
        self.assert_rejected(self.run_cli(), "source identity differs")

    def test_out_of_root_request_is_rejected(self) -> None:
        self.assert_rejected(self.run_cli(root=self.root.parent), "repository root differs")

    def test_invalid_digest_argument_is_structured(self) -> None:
        self.assert_rejected(self.run_cli(digest="not-a-digest"), "must be 64 lowercase")


if __name__ == "__main__":
    unittest.main()
