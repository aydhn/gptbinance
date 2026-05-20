import pytest
from app.provenance_plane.configs import get_config_influence
from app.provenance_plane.registry import registry

def test_get_config_influence():
    registry.register("config-1", {"provenance_id": "config-1", "is_active": True})
    assert get_config_influence("config-1") is True
