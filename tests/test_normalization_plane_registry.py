import pytest
from app.normalization_plane.registry import NormalizationRegistry
from app.normalization_plane.enums import NormalizationClass

def test_normalization_registry_families():
    registry = NormalizationRegistry()
    families = registry.get_families()
    assert NormalizationClass.POST_RESOLUTION in families
    assert NormalizationClass.FULL_NORMAL in families
