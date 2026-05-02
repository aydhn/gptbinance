import pytest
from app.resilience.scenarios import get_scenario, list_scenarios
from app.resilience.exceptions import InvalidExperimentDefinitionError


def test_list_scenarios():
    scenarios = list_scenarios()
    assert len(scenarios) >= 4
    ids = [s.id for s in scenarios]
    assert "stale_stream_scenario" in ids
    assert "reject_storm_scenario" in ids


def test_get_scenario_valid():
    scenario = get_scenario("stale_stream_scenario")
    assert scenario.id == "stale_stream_scenario"
    assert len(scenario.assertions) > 0


def test_get_scenario_invalid():
    with pytest.raises(InvalidExperimentDefinitionError):
        get_scenario("invalid_scenario_xyz")
