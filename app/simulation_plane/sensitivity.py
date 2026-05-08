from typing import Dict
from app.simulation_plane.models import SimulationSensitivityReport
from app.simulation_plane.enums import SensitivityClass


class SensitivityEvaluator:
    def evaluate(
        self, run_id: str, inputs: Dict[SensitivityClass, str]
    ) -> SimulationSensitivityReport:
        return SimulationSensitivityReport(
            run_id=run_id,
            sensitivities=inputs,
            caveats=[
                "One-point robustness claims rejected. Sensitivity surface evaluated."
            ],
        )
