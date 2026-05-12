import pytest
from app.observability_plane.aggregations import AggregationRulesRegistry
from app.observability_plane.exceptions import ObservabilityPlaneError

def test_aggregation_rules_enforcement():
    reg = AggregationRulesRegistry()
    with pytest.raises(ObservabilityPlaneError):
        reg.register_aggregation("t1", "OPAQUE_MATH")

    reg.register_aggregation("t1", "SUM")
    assert reg.get_aggregation("t1") == "SUM"
