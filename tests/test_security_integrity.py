import os
from app.security.integrity import IntegrityChecker


def test_integrity_check(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("hello")

    checker = IntegrityChecker()
    manifest = checker.generate_manifest(str(tmp_path))
    assert str(test_file) in manifest

    results = checker.verify_manifest(manifest)
    assert len(results) == 0

    test_file.write_text("modified")
    results = checker.verify_manifest(manifest)
    assert len(results) == 1
    assert results[0].expected_hash != results[0].actual_hash
