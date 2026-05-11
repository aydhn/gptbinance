import pytest
from app.migration_plane.shims import ShimManager
from app.migration_plane.enums import ShimClass

def test_create_shim():
    manager = ShimManager()
    result = manager.create_shim(ShimClass.READ_SHIM, "Read shim desc", 3600, "Cleanup soon")
    assert result.shim_class == ShimClass.READ_SHIM
    assert result.ttl_seconds == 3600
