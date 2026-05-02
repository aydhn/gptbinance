import pytest
import os
from app.release.checksums import ChecksumManager


def test_generate_and_verify_checksum(tmp_path):
    mgr = ChecksumManager()
    p = tmp_path / "test.txt"
    p.write_text("hello world")

    manifest = mgr.create_manifest(str(tmp_path))
    assert mgr.verify_manifest(manifest, str(tmp_path)) == True

    p.write_text("modified")
    assert mgr.verify_manifest(manifest, str(tmp_path)) == False
