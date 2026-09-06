#!/usr/bin/env python3
"""Public-seam tests for the exact Phase 4 package validator."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[8]
VALIDATOR_RELATIVE = "contexts/operational-system/docs/program/v1/architecture/phase-4/validation/validate_phase4.py"
MANIFEST_RELATIVE = "contexts/operational-system/docs/program/v1/architecture/phase-4/phase-4-sha256.txt"
VALIDATOR = ROOT / VALIDATOR_RELATIVE
SPEC = Path("/Users/taylor/AI-Workspace/.scratch/dobeworks-operational-system-phase4-software-core/spec.md")
SPEC_SHA256 = "e95b8369c7abaf80948e34c61c1b5f803f4ad2ecc2138d78d62a98a81135af9b"
PACKAGE_FILES = (
    "contexts/operational-system/README.md",
    "contexts/operational-system/docs/program/v1/program-definition.md",
    "contexts/operational-system/docs/program/v1/traceability-matrix.md",
    "contexts/operational-system/docs/program/v1/architecture/phase-4/software-core-plan.md",
    "contexts/operational-system/docs/program/v1/architecture/phase-4/worker-core-evidence.md",
    "contexts/operational-system/docs/program/v1/architecture/phase-4/observer-core-evidence.md",
    "contexts/operational-system/docs/program/v1/architecture/phase-4/security-and-supply-evidence.md",
    "contexts/operational-system/docs/program/v1/architecture/phase-4/source-register.md",
    "contexts/operational-system/docs/program/v1/architecture/phase-4/handoff.md",
    "contexts/operational-system/docs/program/v1/architecture/phase-4/degs/phase4-task.json",
    VALIDATOR_RELATIVE,
    "contexts/operational-system/docs/program/v1/architecture/phase-4/validation/test_validate_phase4.py",
    "contexts/operational-system/docs/program/v1/architecture/phase-4/validation/validation-report.md",
    MANIFEST_RELATIVE,
    "contexts/operational-system/software/phase4/README.md",
    "contexts/operational-system/software/phase4/worker_core.py",
    "contexts/operational-system/software/phase4/observer_core.py",
    "contexts/operational-system/software/phase4/test_worker_core.py",
    "contexts/operational-system/software/phase4/test_observer_core.py",
    "contexts/operational-system/software/phase4/fixtures/job-envelope.json",
    "contexts/operational-system/software/phase4/fixtures/input-records.json",
    "contexts/operational-system/software/phase4/fixtures/observer-snapshot.json",
    "contexts/operational-system/software/phase4/fixtures/observer-policy.json",
    "contexts/operational-system/software/phase4/fixtures/expected-result.json",
    "contexts/operational-system/software/phase4/fixtures/expected-observer-record.json",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Phase4ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.repo = Path(self.temporary.name) / "repo"
        subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(ROOT), str(self.repo)], timeout=20, check=True)
        for relative in PACKAGE_FILES:
            destination = self.repo / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, destination)
        self.rehash()
        subprocess.run(["git", "-C", str(self.repo), "config", "user.name", "Phase4 Test"], timeout=10, check=True)
        subprocess.run(["git", "-C", str(self.repo), "config", "user.email", "phase4-test@invalid"], timeout=10, check=True)
        subprocess.run(["git", "-C", str(self.repo), "add", "--", *PACKAGE_FILES], timeout=10, check=True)
        status = subprocess.run(["git", "-C", str(self.repo), "status", "--porcelain"], text=True, capture_output=True, timeout=10, check=True)
        if status.stdout:
            subprocess.run(["git", "-C", str(self.repo), "commit", "--quiet", "-m", "Phase 4 validator fixture"], timeout=20, check=True)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def rehash(self) -> str:
        manifest = self.repo / MANIFEST_RELATIVE
        lines = [f"{digest(self.repo / relative)}  {relative}\n" for relative in sorted(PACKAGE_FILES) if relative != MANIFEST_RELATIVE]
        manifest.write_text("".join(lines), encoding="utf-8")
        return digest(manifest)

    def run_validator(self, manifest_sha=None, spec_sha=SPEC_SHA256, root=None):
        selected_root = root or self.repo
        selected_manifest = manifest_sha or digest(selected_root / MANIFEST_RELATIVE)
        selected_validator = selected_root / VALIDATOR_RELATIVE
        command = [sys.executable, "-B", str(selected_validator), "--repository-root", str(selected_root), "--manifest-sha256", selected_manifest, "--external-spec", str(SPEC), "--external-spec-sha256", spec_sha, "--json"]
        completed = subprocess.run(command, text=True, capture_output=True, timeout=30, check=False)
        return completed, json.loads(completed.stdout)

    def mutate_text(self, relative: str, old: str, new: str) -> None:
        path = self.repo / relative
        value = path.read_text(encoding="utf-8")
        self.assertIn(old, value)
        path.write_text(value.replace(old, new, 1), encoding="utf-8")

    def assert_finding(self, result: dict, rule_id: str) -> None:
        self.assertIn(rule_id, {item["rule_id"] for item in result["findings"]})

    def test_valid_package_passes(self) -> None:
        self.assertTrue(VALIDATOR.is_file(), "Phase 4 validator implementation is absent")
        completed, result = self.run_validator()
        self.assertEqual((completed.returncode, completed.stderr), (0, ""))
        self.assertEqual(result["decision"], "PASS")
        self.assertEqual(result["decision_scope"], "PACKAGE")
        self.assertEqual(result["external_gates_pending"], ["G7", "G8", "G9"])
        self.assertEqual(result["findings"], [])

    def test_clean_committed_candidate_passes(self) -> None:
        status = subprocess.run(["git", "-C", str(self.repo), "status", "--porcelain"], text=True, capture_output=True, timeout=10, check=True)
        self.assertEqual((status.stdout, status.stderr), ("", ""))
        completed, result = self.run_validator()
        self.assertEqual((completed.returncode, completed.stderr), (0, ""))
        self.assertEqual((result["decision"], result["findings"]), ("PASS", []))

    def test_missing_git_metadata_fails_closed(self) -> None:
        target = Path(self.temporary.name) / "no-git-repo"
        shutil.copytree(self.repo, target, ignore=shutil.ignore_patterns(".git"))
        completed, result = self.run_validator(root=target)
        self.assertEqual(completed.returncode, 1)
        self.assert_finding(result, "DEAS-GIT-001")

    def test_missing_and_extra_package_files_fail(self) -> None:
        (self.repo / PACKAGE_FILES[-1]).unlink()
        completed, result = self.run_validator()
        self.assertEqual(completed.returncode, 1)
        self.assert_finding(result, "DEAS-PATH-001")
        shutil.copy2(ROOT / PACKAGE_FILES[-1], self.repo / PACKAGE_FILES[-1])
        self.rehash()
        extra = self.repo / "contexts/operational-system/docs/program/v1/architecture/phase-4/extra.md"
        extra.write_text("extra\n", encoding="utf-8")
        completed, result = self.run_validator()
        self.assertEqual(completed.returncode, 1)
        self.assert_finding(result, "DEAS-PATH-002")

    def test_manifest_content_and_external_identity_fail_closed(self) -> None:
        path = self.repo / "contexts/operational-system/software/phase4/README.md"
        path.write_text(path.read_text(encoding="utf-8") + "drift\n", encoding="utf-8")
        completed, result = self.run_validator()
        self.assertEqual(completed.returncode, 1)
        self.assert_finding(result, "DEAS-MANIFEST-001")
        completed, result = self.run_validator(manifest_sha="0" * 64)
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(result["decision"], "ERROR")

    def test_external_spec_identity_is_required(self) -> None:
        completed, result = self.run_validator(spec_sha="0" * 64)
        self.assertEqual(completed.returncode, 2)
        self.assert_finding(result, "DEAS-IDENTITY-001")

    def test_source_drift_fails(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/requirements.md"
        (self.repo / relative).write_text((self.repo / relative).read_text(encoding="utf-8") + "\n", encoding="utf-8")
        completed, result = self.run_validator()
        self.assertEqual(completed.returncode, 1)
        self.assert_finding(result, "DEAS-SOURCE-001")

    def test_missing_and_duplicate_evidence_fields_fail(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/worker-core-evidence.md"
        self.mutate_text(relative, "- **Limitations:**", "- **Omitted limitations:**")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-EVIDENCE-001")
        source = self.repo / relative
        source.write_text(source.read_text(encoding="utf-8") + "\n- **Status:** PASS\n", encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-EVIDENCE-001")

    def test_duplicate_task_json_key_fails(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/degs/phase4-task.json"
        self.mutate_text(relative, "{\n", "{\n  \"status\": \"COMPLETE\",\n")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-LIFECYCLE-001")

    def test_deep_task_json_is_deterministic_nonconformance(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/degs/phase4-task.json"
        (self.repo / relative).write_text('{"nested":' * 1500 + "0" + "}" * 1500 + "\n", encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual((completed.returncode, completed.stderr, result["decision"]), (1, "", "FAIL"))
        self.assert_finding(result, "DEAS-LIFECYCLE-001")

    def test_unhashable_task_status_is_deterministic_nonconformance(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/degs/phase4-task.json"
        path = self.repo / relative
        value = json.loads(path.read_text(encoding="utf-8"))
        value["verification"]["status"] = {}
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual((completed.returncode, completed.stderr, result["decision"]), (1, "", "FAIL"))
        self.assert_finding(result, "DEAS-LIFECYCLE-001")

    def test_false_task_and_handoff_lifecycle_fail(self) -> None:
        task = "contexts/operational-system/docs/program/v1/architecture/phase-4/degs/phase4-task.json"
        self.mutate_text(task, '"status": "READY_FOR_EXECUTION"', '"status": "COMPLETE"')
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-LIFECYCLE-001")
        handoff = "contexts/operational-system/docs/program/v1/architecture/phase-4/handoff.md"
        self.mutate_text(handoff, "READY_FOR_GIT_DELIVERY", "COMPLETE")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-LIFECYCLE-001")

    def test_false_qualification_release_and_integration_claims_fail(self) -> None:
        handoff = "contexts/operational-system/docs/program/v1/architecture/phase-4/handoff.md"
        self.mutate_text(handoff, "NOT_YET_QUALIFIED", "QUALIFIED_FOR_OPERATION")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-AUTHORITY-001")
        self.mutate_text(handoff, "NOT_YET_RELEASED", "SYSTEM_RELEASED")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-AUTHORITY-001")
        self.mutate_text(handoff, "NOT_PERFORMED", "INTEGRATION_PERFORMED")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-AUTHORITY-001")

    def test_trace_gap_fails(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/traceability-matrix.md"
        self.mutate_text(relative, "EV-P4-JOB-CONTRACT", "EV-P4-JOB-CONTRACT-MISSING")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-TRACE-001")

    def test_suffixed_evidence_identity_fails(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/worker-core-evidence.md"
        self.mutate_text(relative, "`EV-P4-JOB-CONTRACT`", "`EV-P4-JOB-CONTRACT-SUFFIX`")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual(completed.returncode, 1)
        self.assert_finding(result, "DEAS-EVIDENCE-001")

    def test_source_register_requires_exact_path_digest_pair(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/source-register.md"
        self.mutate_text(relative, "`df1644513d48022a3b9f01392fa33e391680b0d1e9341594fbc272ee44237586`", "`3f40080f3cd725db8906385abb6f7db79fadef5a231cf6bc9206b2fa43863c88`")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual(completed.returncode, 1)
        self.assert_finding(result, "DEAS-SOURCE-001")

    def test_forbidden_network_import_fails(self) -> None:
        relative = "contexts/operational-system/software/phase4/worker_core.py"
        path = self.repo / relative
        path.write_text(path.read_text(encoding="utf-8") + "\nimport socket\n", encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-SECURITY-001")

    def test_forbidden_subprocess_import_fails(self) -> None:
        relative = "contexts/operational-system/software/phase4/observer_core.py"
        path = self.repo / relative
        path.write_text(path.read_text(encoding="utf-8") + "\nimport subprocess\n", encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-SECURITY-001")

    def test_unbounded_subprocess_wait_fails(self) -> None:
        self.mutate_text(VALIDATOR_RELATIVE, "process.wait(timeout=2)", "process.wait()")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual(completed.returncode, 1)
        self.assert_finding(result, "DEAS-PRE-004")

    def test_malformed_python_fails_without_validator_traceback(self) -> None:
        relative = "contexts/operational-system/software/phase4/worker_core.py"
        (self.repo / relative).write_text("def malformed(:\n", encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual((completed.returncode, completed.stderr), (1, ""))
        self.assertEqual(result["decision"], "FAIL")
        self.assert_finding(result, "DEAS-STATIC-001")

    def test_artifact_paths_must_be_exact_and_repository_relative(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/worker-core-evidence.md"
        self.mutate_text(relative, "`contexts/operational-system/software/phase4/worker_core.py`", "`worker_core.py`")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-EVIDENCE-001")

    def test_package_tree_entry_bound_fails_closed(self) -> None:
        base = self.repo / "contexts/operational-system/docs/program/v1/architecture/phase-4"
        for number in range(129):
            (base / f"synthetic-extra-{number:03d}").mkdir()
        completed, result = self.run_validator()
        self.assertEqual(completed.returncode, 1)
        self.assert_finding(result, "DEAS-BOUND-002")

    def test_unexpected_module_test_diagnostics_fail(self) -> None:
        relative = "contexts/operational-system/software/phase4/test_worker_core.py"
        path = self.repo / relative
        path.write_text(path.read_text(encoding="utf-8") + '\nsys.stderr.write("unexpected diagnostic\\n")\n', encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual(completed.returncode, 1)
        self.assert_finding(result, "DEAS-TEST-001")

    def test_function_bound_fails(self) -> None:
        relative = "contexts/operational-system/software/phase4/worker_core.py"
        path = self.repo / relative
        body = "\ndef oversized_function():\n" + "".join(f"    value_{number} = {number}\n" for number in range(61))
        path.write_text(path.read_text(encoding="utf-8") + body, encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-PRE-004")

    def test_file_size_bound_fails(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/software-core-plan.md"
        path = self.repo / relative
        path.write_text(path.read_text(encoding="utf-8") + ("x" * (1024 * 1024)), encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-BOUND-001")

    def test_module_regression_is_detected(self) -> None:
        relative = "contexts/operational-system/software/phase4/fixtures/job-envelope.json"
        self.mutate_text(relative, '"input_sha256": "d4dc', '"input_sha256": "0000')
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-TEST-001")

    def test_unresolved_relative_link_fails(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/software-core-plan.md"
        path = self.repo / relative
        path.write_text(path.read_text(encoding="utf-8") + "\n[missing](missing.md)\n", encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assert_finding(result, "DEAS-LINK-001")

    def test_symlink_loop_link_is_deterministic_nonconformance(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/software-core-plan.md"
        path = self.repo / relative
        loop = path.parent / "link-loop"
        loop.symlink_to(loop)
        path.write_text(path.read_text(encoding="utf-8") + "\n[loop](link-loop)\n", encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual((completed.returncode, completed.stderr, result["decision"]), (1, "", "FAIL"))
        self.assert_finding(result, "DEAS-LINK-001")

    def test_nul_link_is_deterministic_nonconformance(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/software-core-plan.md"
        path = self.repo / relative
        path.write_bytes(path.read_bytes() + b"\n[nul](invalid\x00target)\n")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual((completed.returncode, completed.stderr, result["decision"]), (1, "", "FAIL"))
        self.assert_finding(result, "DEAS-LINK-001")

    def test_overlong_link_is_deterministic_nonconformance(self) -> None:
        relative = "contexts/operational-system/docs/program/v1/architecture/phase-4/software-core-plan.md"
        path = self.repo / relative
        path.write_text(path.read_text(encoding="utf-8") + f"\n[long]({'x' * 300})\n", encoding="utf-8")
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual((completed.returncode, completed.stderr, result["decision"]), (1, "", "FAIL"))
        self.assert_finding(result, "DEAS-LINK-001")

    def test_repository_root_symlink_is_rejected_as_execution_error(self) -> None:
        link = Path(self.temporary.name) / "repo-link"
        link.symlink_to(self.repo, target_is_directory=True)
        completed, result = self.run_validator(root=link)
        self.assertEqual((completed.returncode, result["decision"]), (2, "ERROR"))
        self.assert_finding(result, "DEAS-INPUT-001")

    def test_in_root_symlinked_package_file_fails(self) -> None:
        relative = "contexts/operational-system/software/phase4/fixtures/job-envelope.json"
        path = self.repo / relative
        target = self.repo / ".git" / "phase4-symlink-target.json"
        shutil.copy2(path, target)
        path.unlink()
        path.symlink_to(target)
        completed, result = self.run_validator(manifest_sha=self.rehash())
        self.assertEqual((completed.returncode, result["decision"]), (1, "FAIL"))
        self.assert_finding(result, "DEAS-PATH-001")


if __name__ == "__main__":
    unittest.main()
