import pytest
from app.research.features.base import BaseFeatureCalculator
from app.research.features.registry import FeatureRegistry
from app.research.features.models import FeatureSpec
from app.research.features.enums import FeatureCategory
from app.research.features.exceptions import UnsupportedFeatureError


class DummyFeature(BaseFeatureCalculator):
    @classmethod
    def get_name(cls) -> str:
        return "dummy"

    @classmethod
    def get_category(cls) -> str:
        return FeatureCategory.CUSTOM

    @classmethod
    def get_min_history_required(cls, spec) -> int:
        return 1

    def calculate(self, df, spec):
        return df["close"] * 2


def test_registry_registration():
    if "dummy" in FeatureRegistry._calculators:
        del FeatureRegistry._calculators["dummy"]

    FeatureRegistry.register(DummyFeature)

    assert "dummy" in FeatureRegistry.get_all_names()

    instance = FeatureRegistry.get("dummy")
    assert isinstance(instance, DummyFeature)

    with pytest.raises(ValueError):
        FeatureRegistry.register(DummyFeature)


def test_registry_unsupported():
    with pytest.raises(UnsupportedFeatureError):
        FeatureRegistry.get("nonexistent_feature")
