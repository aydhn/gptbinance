from app.stressrisk.enums import ScenarioConfidence
from app.stressrisk.scenarios import ScenarioRegistry


def test_scenario_registry():
    registry = ScenarioRegistry()
    scenario = registry.get_scenario("macro_gap_down")
    assert scenario is not None
    assert scenario.name == "Macro Gap Down"
    assert scenario.confidence == ScenarioConfidence.HIGH
