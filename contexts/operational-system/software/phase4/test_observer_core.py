#!/usr/bin/env python3
"""Public-seam tests for the bounded synthetic Observer Core."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from observer_core import ObserverCore, ObserverRejected


BASE = Path(__file__).resolve().parent
FIXTURES = BASE / "fixtures"
NOW = "2026-09-06T00:01:00Z"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


class ObserverCoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.inputs = self.root / "inputs"
        self.inputs.mkdir()
        self.snapshot = self.inputs / "observer-snapshot.json"
        self.policy = self.inputs / "observer-policy.json"
        shutil.copy2(FIXTURES / "observer-snapshot.json", self.snapshot)
        shutil.copy2(FIXTURES / "observer-policy.json", self.policy)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def core(self, **kwargs) -> ObserverCore:
        return ObserverCore(allowed_input_root=self.inputs, **kwargs)

    def collect(self, core=None) -> dict:
        return (core or self.core()).collect(self.snapshot, self.policy, NOW)

    def mutate_snapshot(self, **updates) -> None:
        value = load(self.snapshot)
        value.update(updates)
        write_json(self.snapshot, value)

    def test_valid_fixture_matches_exact_expected_record(self) -> None:
        actual = json.dumps(self.collect(), indent=2, sort_keys=True) + "\n"
        self.assertEqual(actual.encode(), (FIXTURES / "expected-observer-record.json").read_bytes())

    def test_result_is_deterministic(self) -> None:
        self.assertEqual(self.collect(), self.collect())

    def test_nested_prohibited_field_is_rejected(self) -> None:
        value = load(self.snapshot)
        value["signals"][0]["token"] = "synthetic-secret"
        write_json(self.snapshot, value)
        with self.assertRaisesRegex(ObserverRejected, "PROHIBITED_DATA"):
            self.collect()

    def test_credential_and_secret_aliases_are_rejected(self) -> None:
        for field in ("credentials", "password", "private-key", "secret_value"):
            with self.subTest(field=field):
                value = load(FIXTURES / "observer-snapshot.json")
                value["signals"][0][field] = "synthetic-placeholder"
                write_json(self.snapshot, value)
                with self.assertRaisesRegex(ObserverRejected, "PROHIBITED_DATA"):
                    self.collect()

    def test_private_vault_text_is_rejected(self) -> None:
        value = load(self.snapshot)
        value["signals"][0]["value"] = "PRIVATE VAULT"
        write_json(self.snapshot, value)
        with self.assertRaisesRegex(ObserverRejected, "PROHIBITED_DATA"):
            self.collect()

    def test_unknown_top_level_field_is_rejected(self) -> None:
        self.mutate_snapshot(remediation="restart")
        with self.assertRaisesRegex(ObserverRejected, "INVALID_SCHEMA"):
            self.collect()

    def test_schema_mismatch_is_rejected(self) -> None:
        self.mutate_snapshot(schema_version="dobeworks.observer-snapshot.v2")
        with self.assertRaisesRegex(ObserverRejected, "SCHEMA_INCOMPATIBLE"):
            self.collect()

    def test_duplicate_json_key_is_rejected(self) -> None:
        raw = self.policy.read_text(encoding="utf-8")
        self.policy.write_text(raw.replace('{\n', '{\n  "raw_event_retention_days": 99,\n', 1), encoding="utf-8")
        with self.assertRaisesRegex(ObserverRejected, "DUPLICATE_KEY"):
            self.collect()

    def test_deep_json_is_rejected_without_traceback(self) -> None:
        self.snapshot.write_text("[" * 1500 + "]" * 1500 + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ObserverRejected, "INVALID_JSON"):
            self.collect()

    def test_stale_snapshot_never_implies_health(self) -> None:
        self.mutate_snapshot(sampled_at="2026-09-05T23:00:00Z")
        record = self.collect()
        self.assertEqual((record["status"], record["freshness"]), ("TELEMETRY_UNAVAILABLE", "STALE"))
        self.assertTrue(all(value == "UNKNOWN" for value in record["signals"].values()))

    def test_collector_failure_is_unavailable(self) -> None:
        self.mutate_snapshot(collector_status="FAILED")
        record = self.collect()
        self.assertEqual(record["status"], "TELEMETRY_UNAVAILABLE")
        self.assertEqual(record["self_health"]["failure_status"], "COLLECTOR_FAILED")

    def test_clock_uncertainty_marks_meanings_unknown(self) -> None:
        self.mutate_snapshot(clock_quality="UNKNOWN")
        record = self.collect()
        self.assertEqual((record["status"], record["freshness"]), ("UNKNOWN", "UNKNOWN"))
        self.assertTrue(all(value == "UNKNOWN" for value in record["signals"].values()))

    def test_dropped_records_mark_interval_unknown(self) -> None:
        self.mutate_snapshot(dropped_records=1)
        record = self.collect()
        self.assertEqual(record["status"], "UNKNOWN")
        self.assertEqual(record["self_health"]["failure_status"], "DROPPED_RECORDS")

    def test_missing_signal_is_explicit_unknown(self) -> None:
        value = load(self.snapshot)
        value["signals"] = value["signals"][:-1]
        write_json(self.snapshot, value)
        record = self.collect()
        self.assertEqual(record["status"], "UNKNOWN")
        self.assertEqual(record["signals"]["storage_presence"], "UNKNOWN")

    def test_duplicate_and_unknown_signals_are_rejected(self) -> None:
        value = load(self.snapshot)
        value["signals"].append(value["signals"][0])
        write_json(self.snapshot, value)
        with self.assertRaisesRegex(ObserverRejected, "INVALID_SIGNALS"):
            self.collect()
        value = load(FIXTURES / "observer-snapshot.json")
        value["signals"][0]["name"] = "private_filename"
        write_json(self.snapshot, value)
        with self.assertRaises(ObserverRejected):
            self.collect()

    def test_unhashable_signal_and_api_values_are_rejected(self) -> None:
        value = load(self.snapshot)
        value["signals"][3]["value"] = {}
        write_json(self.snapshot, value)
        with self.assertRaisesRegex(ObserverRejected, "INVALID_SIGNALS"):
            self.collect()
        with self.assertRaisesRegex(ObserverRejected, "INVALID_RETENTION_REQUEST"):
            self.core().retention_decision({}, 30)

    def test_policy_must_equal_accepted_decision(self) -> None:
        value = load(self.policy)
        value["raw_event_retention_days"] = 31
        write_json(self.policy, value)
        with self.assertRaisesRegex(ObserverRejected, "POLICY_MISMATCH"):
            self.collect()

    def test_retention_boundaries_decide_without_deleting(self) -> None:
        core = self.core()
        self.assertEqual(core.retention_decision("RAW_EVENT", 29), "RETAIN")
        self.assertEqual(core.retention_decision("RAW_EVENT", 30), "EXPIRE")
        self.assertEqual(core.retention_decision("DAILY_AGGREGATE", 179), "RETAIN")
        self.assertEqual(core.retention_decision("DAILY_AGGREGATE", 180), "EXPIRE")
        self.assertFalse(hasattr(core, "delete"))

    def test_invalid_retention_request_is_rejected(self) -> None:
        with self.assertRaisesRegex(ObserverRejected, "INVALID_RETENTION_REQUEST"):
            self.core().retention_decision("UNKNOWN", -1)

    def test_retention_age_has_a_fixed_upper_bound(self) -> None:
        core = self.core()
        self.assertEqual(core.retention_decision("RAW_EVENT", 36500), "EXPIRE")
        for age in (36501, True):
            with self.subTest(age=age):
                with self.assertRaisesRegex(ObserverRejected, "INVALID_RETENTION_REQUEST"):
                    core.retention_decision("RAW_EVENT", age)

    def test_oversized_input_is_rejected(self) -> None:
        with self.assertRaisesRegex(ObserverRejected, "INPUT_LIMIT"):
            self.collect(self.core(max_input_bytes=1))

    def test_out_of_root_and_symlink_inputs_are_rejected(self) -> None:
        outside = self.root / "outside.json"
        shutil.copy2(self.snapshot, outside)
        with self.assertRaisesRegex(ObserverRejected, "PATH_REJECTED"):
            self.core().collect(outside, self.policy, NOW)
        linked = self.inputs / "linked.json"
        linked.symlink_to(self.snapshot)
        with self.assertRaisesRegex(ObserverRejected, "PATH_REJECTED"):
            self.core().collect(linked, self.policy, NOW)

    def test_symlink_loop_input_is_rejected(self) -> None:
        loop = self.inputs / "loop.json"
        loop.symlink_to(loop)
        with self.assertRaisesRegex(ObserverRejected, "PATH_REJECTED"):
            self.core().collect(loop, self.policy, NOW)

    def test_core_exposes_no_action_authority(self) -> None:
        core = self.core()
        self.assertFalse(any(hasattr(core, name) for name in ("remediate", "dispatch", "promote", "approve", "delete")))
        self.assertEqual(self.collect()["limitations"][-1], "NO_ACTION_AUTHORITY")

    def test_cli_emits_one_complete_json_result(self) -> None:
        command = [sys.executable, "-B", str(BASE / "observer_core.py"), "--snapshot", str(self.snapshot), "--policy", str(self.policy), "--allowed-input-root", str(self.inputs), "--now", NOW]
        completed = subprocess.run(command, text=True, capture_output=True, timeout=10, check=False)
        parsed = json.loads(completed.stdout)
        self.assertEqual((completed.returncode, completed.stderr, parsed["status"]), (0, "", "VALIDATED"))


if __name__ == "__main__":
    unittest.main()
