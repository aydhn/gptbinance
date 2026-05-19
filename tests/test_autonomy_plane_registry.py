import pytest
from app.autonomy_plane.registry import CanonicalAutonomyRegistry
from app.autonomy_plane.models import AutonomyObject
from app.autonomy_plane.enums import AutonomyClass

def test_autonomy_registry_integrity():
    registry = CanonicalAutonomyRegistry()
    obj = AutonomyObject(
        autonomy_id="test_id",
        agent_id="test_agent",
        autonomy_class=AutonomyClass.BOUNDED,
        owner="test_owner"
    )
    registry.register(obj)
    retrieved = registry.get("test_id")
    assert retrieved is not None
    assert retrieved.autonomy_id == "test_id"
    assert retrieved.agent_id == "test_agent"

def test_undocumented_autonomy_rejection():
    registry = CanonicalAutonomyRegistry()
    obj = AutonomyObject(
        autonomy_id="",
        agent_id="test_agent",
        autonomy_class=AutonomyClass.BOUNDED,
        owner="test_owner"
    )
    with pytest.raises(ValueError, match="No undocumented autonomy ids allowed."):
        registry.register(obj)
