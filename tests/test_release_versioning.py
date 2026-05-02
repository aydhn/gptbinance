import pytest
from app.release.versioning import VersionManager

def test_get_current_version():
    mgr = VersionManager()
    v = mgr.get_current_version()
    assert v.version == "1.0.0"

def test_get_schema_snapshot():
    mgr = VersionManager()
    s = mgr.get_schema_snapshot()
    assert s.config_schema_version == "v1"
