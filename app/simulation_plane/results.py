from app.simulation_plane.models import SimulationResult
from typing import Dict


class ResultBuilder:
    @staticmethod
    def build(
        run_id: str, ret: float, max_dd: float, metrics: Dict[str, float]
    ) -> SimulationResult:
        return SimulationResult(
            run_id=run_id,
            total_return=ret,
            max_drawdown=max_dd,
            metrics=metrics,
            caveats=["Results are approximation based on assumption manifest."],
        )
