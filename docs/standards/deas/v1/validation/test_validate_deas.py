#!/usr/bin/env python3
"""Behavior tests for the DEAS validator command-line interface."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[5]
VALIDATOR = Path(__file__).with_name("validate_deas.py")
EXPECTED_FINDINGS = Path(__file__).with_name("generation-1-expected-findings.json")
GENERATION_2_PLAN = VALIDATOR.parents[1] / "phase2-generation-2-plan.md"
STANDARD = VALIDATOR.parents[1] / "standard.md"
DEFINITION_TASK = VALIDATOR.parents[1] / "degs/definition-task.json"
GENERATION_2_MANIFEST = Path(
    "contexts/operational-system/docs/program/v1/qualification/phase-2/"
    "generation-2-sha256.txt"
)
PHASE2_REPORT_COMMAND = (
    "python3 contexts/operational-system/docs/program/v1/qualification/phase-2/"
    "validation/validate_phase2.py --repository-root . --generation 2 --json"
)
DEAS_REPORT_COMMAND = (
    "python3 docs/standards/deas/v1/validation/validate_deas.py conformance "
    f"--generation 2 --identity-manifest {GENERATION_2_MANIFEST} "
    '--identity-manifest-sha256 "$DEAS_GENERATION_2_MANIFEST_SHA256" '
    "--json --repository-root ."
)
MAX_GIT_BLOB_BYTES = 4 * 1024 * 1024


class DeasValidatorCliTests(unittest.TestCase):
    def run_cli(
        self,
        *arguments: str,
        repository_root: Path = REPOSITORY_ROOT,
        environment: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                *arguments,
                "--repository-root",
                str(repository_root),
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
            env=environment,
        )

    def materialize_git_blob(
        self,
        commit: str,
        relative: str,
        target: Path,
    ) -> None:
        object_name = f"{commit}:{relative}"
        size_result = subprocess.run(
            ["git", "cat-file", "-s", object_name],
            cwd=REPOSITORY_ROOT,
            check=False,
            capture_output=True,
            timeout=10,
        )
        self.assertEqual(0, size_result.returncode)
        self.assertEqual(b"", size_result.stderr)
        self.assertLessEqual(len(size_result.stdout), 80)
        self.assertRegex(size_result.stdout, rb"^[0-9]+\n$")
        expected_size = int(size_result.stdout)
        self.assertLessEqual(expected_size, MAX_GIT_BLOB_BYTES)

        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("wb") as output, tempfile.TemporaryFile() as diagnostics:
            result = subprocess.run(
                ["git", "cat-file", "blob", object_name],
                cwd=REPOSITORY_ROOT,
                check=False,
                stdout=output,
                stderr=diagnostics,
                timeout=10,
            )
            diagnostics.seek(0, os.SEEK_END)
            diagnostic_size = diagnostics.tell()
        self.assertEqual(0, result.returncode)
        self.assertEqual(0, diagnostic_size)
        self.assertEqual(expected_size, target.stat().st_size)

    def materialize_generation_1(self, destination: Path) -> None:
        expected = json.loads(EXPECTED_FINDINGS.read_text(encoding="utf-8"))
        commit = expected["baseline"]["commit"]
        for relative in expected["baseline"]["artifacts"]:
            self.materialize_git_blob(
                commit,
                relative,
                destination / relative,
            )

    def generation_2_paths(self) -> tuple[str, ...]:
        plan = GENERATION_2_PLAN.read_text(encoding="utf-8")
        path_section = plan.split("## Exact C4 paths", 1)[1].split(
            "No other path is in scope.",
            1,
        )[0]
        paths = tuple(
            line.split(". ", 1)[1]
            for line in path_section.splitlines()
            if line and line[0].isdigit() and ". " in line
        )
        self.assertEqual(15, len(paths))
        self.assertIn(str(GENERATION_2_MANIFEST), paths)
        return paths

    def evidence_contract_labels(self) -> tuple[str, ...]:
        schema = STANDARD.read_text(encoding="utf-8").split(
            "<!-- DEAS-EVIDENCE-SCHEMA:START -->",
            1,
        )[1].split("<!-- DEAS-EVIDENCE-SCHEMA:END -->", 1)[0]
        labels = tuple(
            line.split("`")[1]
            for line in schema.splitlines()
            if " | `**" in line
        )
        self.assertEqual(23, len(labels))
        return labels

    def fake_git_environment(self, directory: Path, script: str) -> dict[str, str]:
        fake_git = directory / "git"
        fake_git.write_text(f"#!/bin/sh\n{script}\n", encoding="utf-8")
        fake_git.chmod(0o700)
        environment = os.environ.copy()
        environment["PATH"] = f"{directory}:{environment['PATH']}"
        return environment

    def write_generation_2_manifest(self, destination: Path) -> str:
        paths = self.generation_2_paths()
        manifest = destination / GENERATION_2_MANIFEST
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(
            "".join(
                f"{hashlib.sha256((destination / relative).read_bytes()).hexdigest()}  {relative}\n"
                for relative in sorted(set(paths) - {str(GENERATION_2_MANIFEST)})
            ),
            encoding="utf-8",
        )
        return hashlib.sha256(manifest.read_bytes()).hexdigest()

    def materialize_malformed_generation_2(self, destination: Path) -> str:
        paths = self.generation_2_paths()
        for source in (VALIDATOR.resolve(), Path(__file__).resolve()):
            target = destination / source.relative_to(REPOSITORY_ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
        for relative in paths:
            if relative == str(GENERATION_2_MANIFEST):
                continue
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("", encoding="utf-8")
        return self.write_generation_2_manifest(destination)

    def materialize_semantic_pass_generation_2(self, destination: Path) -> str:
        self.materialize_malformed_generation_2(destination)
        paths = self.generation_2_paths()
        (destination / next(path for path in paths if path.endswith("qualification-plan.md"))).write_text(
            "- **Evidence collection:** `COMPLETE`\n",
            encoding="utf-8",
        )
        (destination / next(path for path in paths if path.endswith("traceability-matrix.md"))).write_text(
            "# Corrected trace\n",
            encoding="utf-8",
        )
        (destination / next(path for path in paths if path.endswith("phase-2-entry-criteria.md"))).write_text(
            "# Historical entry disposition complete\n",
            encoding="utf-8",
        )
        record = "\n".join(
            f"- {label} UNKNOWN" for label in self.evidence_contract_labels()
        ) + "\n"
        for relative in paths:
            if "/evidence/" in relative and relative.endswith(".md"):
                (destination / relative).write_text(record, encoding="utf-8")
            if relative.endswith("degs/phase2-generation-2-task.json"):
                (destination / relative).write_text("{}\n", encoding="utf-8")
        return self.write_generation_2_manifest(destination)

    def write_passing_phase2_stub(
        self,
        destination: Path,
        *,
        diagnostic: str | None = None,
    ) -> str:
        validator_path = next(
            path
            for path in self.generation_2_paths()
            if path.endswith("validation/validate_phase2.py")
        )
        payload = {
            "decision": "PASS",
            "generation": 2,
            "identity_verified": True,
            "original_observations_preserved": True,
            "phase2_degs_decision": "PASS",
            "role_disposition": "NONE",
            "schema_version": 2,
            "validation_report_decision": "PASS",
        }
        script = (
            "import json\n"
            "import sys\n"
            f"print(json.dumps({payload!r}, sort_keys=True))\n"
        )
        if diagnostic is not None:
            script += f"print({diagnostic!r}, file=sys.stderr)\n"
        (destination / validator_path).write_text(script, encoding="utf-8")
        return self.write_generation_2_manifest(destination)

    def write_superficially_complete_generation_2_task(self, destination: Path) -> str:
        task_path = next(
            path
            for path in self.generation_2_paths()
            if path.endswith("degs/phase2-generation-2-task.json")
        )
        task = {
            "authority_lane": "TAYLOR_AI_WORKBENCH",
            "handoff": {"status": "PASS"},
            "independent_review": {"status": "PASS"},
            "post_action_validation": {"status": "PASS"},
            "risk_tier": "TIER_1",
            "status": "COMPLETE",
            "task_id": "DEGS-T1-DW-HWSW-P2-GENERATION-2-20260902",
            "unresolved_items": [],
            "validation": {"status": "PASS"},
        }
        (destination / task_path).write_text(
            json.dumps(task, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return self.write_generation_2_manifest(destination)

    def write_superficially_complete_generation_2_report(
        self,
        destination: Path,
        *,
        procedure: str = "UNKNOWN",
        discrepancies: str = "UNKNOWN",
        include_commands: bool = False,
    ) -> str:
        report_path = next(
            path
            for path in self.generation_2_paths()
            if path.endswith("validation/validation-report.md")
        )
        values = {
            "**Requirement/fault IDs:**": "DEGS-T1-DW-HWSW-P2-GENERATION-2-20260902",
            "**Status:**": "PASS",
            "**Cryptographic identities:**": str(GENERATION_2_MANIFEST),
            "**Procedure or command identity:**": procedure,
            "**Discrepancy references:**": discrepancies,
        }
        report = "\n".join(
            f"- {label} {values.get(label, 'UNKNOWN')}"
            for label in self.evidence_contract_labels()
        ) + "\n"
        if include_commands:
            report += (
                "\n## Exact validation commands\n\n"
                "```sh\n"
                f"{PHASE2_REPORT_COMMAND}\n"
                "DEAS_GENERATION_2_MANIFEST_SHA256="
                "<externally-frozen-sha256>\n"
                f"{DEAS_REPORT_COMMAND}\n"
                "```\n"
            )
        (destination / report_path).write_text(report, encoding="utf-8")
        return self.write_generation_2_manifest(destination)

    def preserve_generation_1_evidence(self, destination: Path) -> str:
        expected = json.loads(EXPECTED_FINDINGS.read_text(encoding="utf-8"))
        commit = expected["baseline"]["commit"]
        contract = "\n".join(
            f"- {label} UNKNOWN" for label in self.evidence_contract_labels()
        ).encode()
        evidence_paths = tuple(
            path
            for path in self.generation_2_paths()
            if "/evidence/" in path and path.endswith(".md")
        )
        self.assertEqual(4, len(evidence_paths))
        for relative in evidence_paths:
            target = destination / relative
            self.materialize_git_blob(commit, relative, target)
            separator = b"" if target.read_bytes().endswith(b"\n") else b"\n"
            with target.open("ab") as output:
                output.write(separator + contract + b"\n")
        return self.write_generation_2_manifest(destination)

    def test_generation_1_fails_with_exact_semantic_findings(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            self.materialize_generation_1(source_root)
            result = self.run_cli(
                "conformance",
                "--generation",
                "1",
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(1, result.returncode, result.stderr)
        self.assertEqual(
            {
                "decision": "FAIL",
                "finding_count": 6,
                "findings": [
                    {
                        "message": "Completed Phase 2 evidence is still represented as planned or reserved.",
                        "path": "contexts/operational-system/docs/program/v1/traceability-matrix.md",
                        "rule_id": "DEAS-TRACE-001",
                    },
                    {
                        "message": "Phase 2 entry prerequisites remain unchecked although evidence collection is complete.",
                        "path": "contexts/operational-system/docs/program/v1/phase-2-entry-criteria.md",
                        "rule_id": "DEAS-PHASE-001",
                    },
                    {
                        "message": "Consequential evidence record omits one or more required contract fields.",
                        "path": "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/current-mac-baseline.md",
                        "rule_id": "DEAS-EVIDENCE-001",
                    },
                    {
                        "message": "Consequential evidence record omits one or more required contract fields.",
                        "path": "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/seagate-device-volume.md",
                        "rule_id": "DEAS-EVIDENCE-001",
                    },
                    {
                        "message": "Consequential evidence record omits one or more required contract fields.",
                        "path": "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/observer-surface.md",
                        "rule_id": "DEAS-EVIDENCE-001",
                    },
                    {
                        "message": "Consequential evidence record omits one or more required contract fields.",
                        "path": "contexts/operational-system/docs/program/v1/qualification/phase-2/evidence/worker-candidate.md",
                        "rule_id": "DEAS-EVIDENCE-001",
                    },
                ],
                "generation": 1,
                "identity_verified": True,
                "schema_version": 1,
            },
            json.loads(result.stdout),
        )

    def test_generation_1_rejects_a_tampered_baseline(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            self.materialize_generation_1(source_root)
            relative = Path(
                "contexts/operational-system/docs/program/v1/"
                "traceability-matrix.md"
            )
            target = source_root / relative
            target.write_text(
                target.read_text(encoding="utf-8") + "\n",
                encoding="utf-8",
            )
            result = self.run_cli(
                "conformance",
                "--generation",
                "1",
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn(
            f"Generation 1 identity mismatch: {relative}",
            result.stderr,
        )

    def test_generation_2_requires_an_exact_identity_manifest(self) -> None:
        result = self.run_cli("conformance", "--generation", "2", "--json")

        self.assertEqual(2, result.returncode)
        self.assertIn(
            "Generation 2 requires an identity manifest and its SHA-256",
            result.stderr,
        )

    def test_generation_2_rejects_an_incomplete_identity_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            artifact = source_root / "placeholder.txt"
            artifact.write_text("not a Generation 2 package\n", encoding="utf-8")
            manifest = source_root / GENERATION_2_MANIFEST
            manifest.parent.mkdir(parents=True, exist_ok=True)
            artifact_hash = hashlib.sha256(artifact.read_bytes()).hexdigest()
            manifest.write_text(
                f"{artifact_hash}  placeholder.txt\n",
                encoding="utf-8",
            )
            manifest_hash = hashlib.sha256(manifest.read_bytes()).hexdigest()
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn(
            "Generation 2 identity manifest path set differs",
            result.stderr,
        )

    def test_generation_2_rejects_a_malformed_identity_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            manifest = source_root / GENERATION_2_MANIFEST
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text("not a manifest line\n", encoding="utf-8")
            manifest_hash = hashlib.sha256(manifest.read_bytes()).hexdigest()
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("invalid identity manifest line", result.stderr)

    def test_generation_2_rejects_an_out_of_root_identity_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as repository_directory:
            with tempfile.TemporaryDirectory() as outside_directory:
                source_root = Path(repository_directory)
                manifest = Path(outside_directory) / "identity.txt"
                manifest.write_text("not inspected\n", encoding="utf-8")
                manifest_hash = hashlib.sha256(manifest.read_bytes()).hexdigest()
                result = self.run_cli(
                    "conformance",
                    "--generation",
                    "2",
                    "--identity-manifest",
                    str(manifest),
                    "--identity-manifest-sha256",
                    manifest_hash,
                    "--json",
                    repository_root=source_root,
                )

        self.assertEqual(2, result.returncode)
        self.assertIn("identity manifest escapes repository root", result.stderr)

    def test_generation_2_requires_the_exact_manifest_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            manifest_hash = self.materialize_malformed_generation_2(source_root)
            exact_manifest = source_root / GENERATION_2_MANIFEST
            alternate_manifest = source_root / "identity.txt"
            alternate_manifest.write_bytes(exact_manifest.read_bytes())
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                "identity.txt",
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Generation 2 identity manifest path differs", result.stderr)

    def test_generation_2_rejects_missing_collection_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            manifest_hash = self.materialize_malformed_generation_2(source_root)
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("evidence collection state is missing or duplicated", result.stderr)

    def test_generation_2_rejects_an_inert_phase2_validator(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            manifest_hash = self.materialize_semantic_pass_generation_2(source_root)
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Phase 2 validator result is not valid JSON", result.stderr)

    def test_generation_2_terminates_a_stalled_phase2_validator(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            self.materialize_semantic_pass_generation_2(source_root)
            validator_path = next(
                path
                for path in self.generation_2_paths()
                if path.endswith("validation/validate_phase2.py")
            )
            (source_root / validator_path).write_text(
                "import time\ntime.sleep(5)\n",
                encoding="utf-8",
            )
            manifest_hash = self.write_generation_2_manifest(source_root)
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Phase 2 validator read timed out", result.stderr)

    def test_generation_2_rejects_phase2_validator_diagnostics(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            self.materialize_semantic_pass_generation_2(source_root)
            manifest_hash = self.write_passing_phase2_stub(
                source_root,
                diagnostic="unexpected diagnostic",
            )
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Phase 2 validator emitted diagnostics", result.stderr)

    def test_generation_2_independently_rejects_an_incomplete_task(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            self.materialize_semantic_pass_generation_2(source_root)
            manifest_hash = self.write_passing_phase2_stub(source_root)
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Generation 2 task is incomplete or inconsistent", result.stderr)

    def test_generation_2_independently_rejects_an_incomplete_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            self.materialize_semantic_pass_generation_2(source_root)
            self.write_passing_phase2_stub(source_root)
            manifest_hash = self.write_superficially_complete_generation_2_task(
                source_root
            )
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Generation 2 validation report is incomplete", result.stderr)

    def test_generation_2_rejects_report_without_literal_commands(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            self.materialize_semantic_pass_generation_2(source_root)
            self.write_passing_phase2_stub(source_root)
            self.write_superficially_complete_generation_2_task(source_root)
            manifest_hash = self.write_superficially_complete_generation_2_report(
                source_root
            )
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Generation 2 report command evidence differs", result.stderr)

    def test_generation_2_rejects_unstable_discrepancy_references(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            self.materialize_semantic_pass_generation_2(source_root)
            self.write_passing_phase2_stub(source_root)
            self.write_superficially_complete_generation_2_task(source_root)
            manifest_hash = self.write_superficially_complete_generation_2_report(
                source_root,
                procedure="See Exact validation commands below.",
                include_commands=True,
            )
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn(
            "Generation 2 report discrepancy evidence differs",
            result.stderr,
        )

    def test_generation_2_rejects_changed_original_observations(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            self.materialize_semantic_pass_generation_2(source_root)
            self.write_passing_phase2_stub(source_root)
            self.write_superficially_complete_generation_2_task(source_root)
            manifest_hash = self.write_superficially_complete_generation_2_report(
                source_root,
                procedure="See Exact validation commands below.",
                discrepancies="NONE",
                include_commands=True,
            )
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Generation 2 original observations differ", result.stderr)

    def test_generation_2_rejects_a_role_disposition_addition(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            self.materialize_semantic_pass_generation_2(source_root)
            self.preserve_generation_1_evidence(source_root)
            self.write_passing_phase2_stub(source_root)
            self.write_superficially_complete_generation_2_task(source_root)
            self.write_superficially_complete_generation_2_report(
                source_root,
                procedure="See Exact validation commands below.",
                discrepancies="NONE",
                include_commands=True,
            )
            evidence_path = next(
                path
                for path in self.generation_2_paths()
                if path.endswith("evidence/current-mac-baseline.md")
            )
            with (source_root / evidence_path).open("ab") as handle:
                handle.write(b"- **Role Disposition:** QUALIFIED_FOR_BOUNDED_ROLE\n")
            manifest_hash = self.write_generation_2_manifest(source_root)
            result = self.run_cli(
                "conformance",
                "--generation",
                "2",
                "--identity-manifest",
                str(GENERATION_2_MANIFEST),
                "--identity-manifest-sha256",
                manifest_hash,
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Generation 2 Role Disposition differs", result.stderr)

    def test_evidence_record_cli_rejects_empty_and_duplicate_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            record = source_root / "record.md"
            record.write_text("- **Evidence ID:**\n", encoding="utf-8")
            empty = self.run_cli(
                "evidence-record",
                "--record",
                "record.md",
                "--json",
                repository_root=source_root,
            )
            record.write_text(
                "- **Evidence ID:** one\n- **Evidence ID:** two\n",
                encoding="utf-8",
            )
            duplicate = self.run_cli(
                "evidence-record",
                "--record",
                "record.md",
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(1, empty.returncode, empty.stderr)
        self.assertEqual(1, duplicate.returncode, duplicate.stderr)
        self.assertEqual("FAIL", json.loads(empty.stdout)["decision"])
        self.assertEqual("FAIL", json.loads(duplicate.stdout)["decision"])

    def test_validation_report_satisfies_the_evidence_record_contract(self) -> None:
        result = self.run_cli(
            "evidence-record",
            "--record",
            "docs/standards/deas/v1/validation/validation-report.md",
            "--json",
        )

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("PASS", json.loads(result.stdout)["decision"])

    def test_evidence_record_cli_rejects_oversize_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source_root = Path(directory)
            record = source_root / "record.md"
            record.write_bytes(b"x" * (4 * 1024 * 1024 + 1))
            result = self.run_cli(
                "evidence-record",
                "--record",
                "record.md",
                "--json",
                repository_root=source_root,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("input exceeds 4194304 bytes", result.stderr)

    def test_definition_cli_terminates_a_stalled_git_read(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            environment = self.fake_git_environment(
                Path(directory),
                "exec /bin/sleep 5",
            )
            result = self.run_cli(
                "definition",
                "--json",
                environment=environment,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Generation 1 Git read timed out", result.stderr)

    def test_definition_cli_prevents_oversize_git_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            environment = self.fake_git_environment(
                Path(directory),
                "/usr/bin/python3 -c 'import sys; sys.stdout.buffer.write(b\"x\" * 4194305)'",
            )
            result = self.run_cli(
                "definition",
                "--json",
                environment=environment,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Generation 1 Git output limit exceeded", result.stderr)

    def test_definition_cli_rejects_successful_git_diagnostics(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            environment = self.fake_git_environment(
                Path(directory),
                "printf 'unexpected diagnostic\\n' >&2\n"
                'exec /usr/bin/git "$@"',
            )
            result = self.run_cli(
                "definition",
                "--json",
                environment=environment,
            )

        self.assertEqual(2, result.returncode)
        self.assertIn("Generation 1 Git emitted diagnostics", result.stderr)

    def test_definition_passes_with_frozen_generation_1_regression(self) -> None:
        task = json.loads(DEFINITION_TASK.read_text(encoding="utf-8"))
        self.assertEqual("READY_FOR_EXECUTION", task["status"])
        result = self.run_cli("definition", "--json")

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(
            {
                "artifact_manifest_verified": True,
                "decision": "PASS",
                "generation_1_decision": "FAIL",
                "generation_1_findings_match": True,
                "overlay_count": 6,
                "preventive_invariant_count": 10,
                "profile_count": 3,
                "schema_version": 1,
            },
            json.loads(result.stdout),
        )


if __name__ == "__main__":
    unittest.main()
