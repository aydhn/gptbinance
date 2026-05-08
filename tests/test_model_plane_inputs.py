import pytest
from app.model_plane.inputs import ModelInputRegistry, ModelInputDescriptor
from app.model_plane.exceptions import ModelPlaneError


def test_input_registry_valid():
    registry = ModelInputRegistry()
    descriptor = ModelInputDescriptor(
        input_id="in_1", feature_manifest_id="feat_1", freshness_ms=100
    )
    registry.register_input(descriptor)
    assert registry.get_input("in_1") == descriptor


def test_input_registry_missing_id():
    registry = ModelInputRegistry()
    with pytest.raises(ModelPlaneError):
        registry.register_input(
            ModelInputDescriptor(input_id="", feature_manifest_id="feat_1")
        )


def test_validate_freshness():
    registry = ModelInputRegistry()
    descriptor = ModelInputDescriptor(
        input_id="in_1", feature_manifest_id="feat_1", freshness_ms=150
    )
    registry.register_input(descriptor)

    assert registry.validate_freshness("in_1", 200) is True
    assert descriptor.is_stale is False

    assert registry.validate_freshness("in_1", 100) is False
    assert descriptor.is_stale is True
