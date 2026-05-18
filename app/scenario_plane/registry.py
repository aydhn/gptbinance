from app.scenario_plane.models import ScenarioObject
from app.scenario_plane.enums import ScenarioClass
from app.scenario_plane.exceptions import InvalidScenarioObjectError

class ScenarioRegistry:
    def __init__(self):
        self.scenarios = {}

    def register(self, scenario: ScenarioObject):
        if not scenario.scenario_id:
            raise ValueError("No undocumented scenario ids allowed.")
        self.scenarios[scenario.scenario_id] = scenario

    def get_scenario(self, scenario_id: str) -> ScenarioObject:
        return self.scenarios.get(scenario_id)
