import pytest
import os
from app.release.bundle import BundleGenerator


def test_generate_bundle(tmp_path):
    gen = BundleGenerator()
    bundle = gen.generate_bundle(str(tmp_path))
    assert os.path.exists(bundle.archive_path)
    assert bundle.checksum is not None
