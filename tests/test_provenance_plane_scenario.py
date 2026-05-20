import pytest
from app.scenario_plane.comparisons import check_scenario_provenance

def test_predicted_vs_realized_requires_provenance():
    assert "CAUTION" in check_scenario_provenance("scen-1", False)
    assert "TRUSTED" in check_scenario_provenance("scen-2", True)
