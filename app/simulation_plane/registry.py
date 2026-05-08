from typing import Dict, List, Optional
from app.simulation_plane.models import SimulationDefinition, SimulationRun
from app.simulation_plane.exceptions import InvalidSimulationDefinitionError


class SimulationRegistry:
    def __init__(self):
        self._definitions: Dict[str, SimulationDefinition] = {}
        self._runs: Dict[str, SimulationRun] = {}

    def register_definition(self, definition: SimulationDefinition) -> None:
        if definition.sim_id in self._definitions:
            raise InvalidSimulationDefinitionError(
                f"Definition {definition.sim_id} already exists"
            )
        self._definitions[definition.sim_id] = definition

    def register_run(self, run: SimulationRun) -> None:
        if run.sim_ref.sim_id not in self._definitions:
            raise InvalidSimulationDefinitionError(
                f"Simulation {run.sim_ref.sim_id} not registered"
            )
        self._runs[run.run_id] = run

    def get_definition(self, sim_id: str) -> Optional[SimulationDefinition]:
        return self._definitions.get(sim_id)

    def get_run(self, run_id: str) -> Optional[SimulationRun]:
        return self._runs.get(run_id)

    def list_definitions(self) -> List[SimulationDefinition]:
        return list(self._definitions.values())

    def list_runs(self) -> List[SimulationRun]:
        return list(self._runs.values())
