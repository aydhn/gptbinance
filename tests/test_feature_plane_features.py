import pytest
from datetime import datetime, timezone
from app.feature_plane.enums import FeatureDomain, FeatureTypeClass, FeatureWindowClass, FeatureSourceClass
from app.feature_plane.models import (
    FeatureDefinition, FeatureSchemaDef, FeatureSchemaVersion,
    FeatureWindow, FeatureInputSurface, FeatureComputationSpec
)
from app.feature_plane.features import CanonicalFeatureRegistry
from app.feature_plane.exceptions import InvalidFeatureDefinitionError

def test_canonical_feature_registry():
    registry = CanonicalFeatureRegistry()
    feature = FeatureDefinition(
        feature_id="f_test_001",
        name="Test Feature",
        domain=FeatureDomain.MOMENTUM,
        feature_schema=FeatureSchemaDef(
            schema_id="s_001",
            type_class=FeatureTypeClass.SCALAR_FLOAT,
            is_nullable=False,
            missing_value_policy="fail",
            version=FeatureSchemaVersion(version_id="v1", created_at=datetime.now(timezone.utc))
        ),
        input_surfaces=[FeatureInputSurface(source_class=FeatureSourceClass.MARKET_TRUTH_KLINE, source_id="kline_1m")],
        window=FeatureWindow(window_class=FeatureWindowClass.ROLLING_TIME),
        computation_spec=FeatureComputationSpec(transform_type="ma"),
        owner_domain="research"
    )
    registry.register(feature)

    assert registry.get("f_test_001") == feature

    with pytest.raises(InvalidFeatureDefinitionError):
        registry.register(feature)
