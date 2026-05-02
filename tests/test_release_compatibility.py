import pytest
from app.release.compatibility import CompatibilityChecker
from app.release.manifest import ManifestGenerator
from app.release.enums import CompatibilityVerdict

def test_check_compatibility():
    checker = CompatibilityChecker()
    target_manifest = ManifestGenerator().create_manifest()
    target_manifest.version.config_schema_version = "v99" # Force mismatch

    report = checker.check(target_manifest)
    assert report.verdict == CompatibilityVerdict.MIGRATION_REQUIRED
