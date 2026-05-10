import pytest
from app.release_plane.registry import CanonicalReleaseRegistry
from app.release_plane.models import ReleaseDefinition, EnvironmentTarget
from app.release_plane.enums import ReleaseClass, EnvironmentClass
from app.release_plane.exceptions import InvalidReleaseDefinition

def test_registry_register_and_get():
    registry = CanonicalReleaseRegistry()
    target = EnvironmentTarget(environment_class=EnvironmentClass.REPLAY, isolation_rules={}, metadata={})
    release = ReleaseDefinition(
        release_id="rel-123",
        objective="Update model",
        release_class=ReleaseClass.DATA_FEATURE_MODEL_BUNDLE,
        target_environments=[target]
    )
    registry.register(release)
    fetched = registry.get("rel-123")
    assert fetched is not None
    assert fetched.release_id == "rel-123"

def test_registry_rejects_duplicate():
    registry = CanonicalReleaseRegistry()
    release = ReleaseDefinition(
        release_id="rel-dup",
        objective="x",
        release_class=ReleaseClass.STRATEGY_BUNDLE,
        target_environments=[]
    )
    registry.register(release)
    with pytest.raises(InvalidReleaseDefinition):
        registry.register(release)

def test_registry_rejects_undocumented():
    registry = CanonicalReleaseRegistry()
    release = ReleaseDefinition(
        release_id="undocumented-fix",
        objective="x",
        release_class=ReleaseClass.STRATEGY_BUNDLE,
        target_environments=[]
    )
    with pytest.raises(InvalidReleaseDefinition):
        registry.register(release)
