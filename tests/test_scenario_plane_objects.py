import pytest
from app.scenario_plane.models import ScenarioObject
from app.scenario_plane.enums import ScenarioClass

def test_object():
    obj = ScenarioObject(scenario_id="s1", scenario_class=ScenarioClass.ACTIVATION, owner="me", scope="local", objective="none")
    assert obj.scenario_id == "s1"
