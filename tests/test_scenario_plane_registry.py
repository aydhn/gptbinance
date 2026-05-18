import pytest
from app.scenario_plane.registry import ScenarioRegistry
from app.scenario_plane.models import ScenarioObject
from app.scenario_plane.enums import ScenarioClass

def test_registry():
    registry = ScenarioRegistry()
    obj = ScenarioObject(scenario_id="s1", scenario_class=ScenarioClass.RELEASE, owner="test", scope="all", objective="test")
    registry.register(obj)
    assert registry.get_scenario("s1") is not None
