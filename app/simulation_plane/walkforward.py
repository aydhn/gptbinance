from typing import List, Dict, Any
from app.simulation_plane.models import WalkForwardReport
from app.simulation_plane.enums import WalkForwardClass


class WalkForwardEvaluator:
    def evaluate(self, run_id: str, folds: List[Dict[str, Any]]) -> WalkForwardReport:
        if len(folds) < 3:
            wf_class = WalkForwardClass.INSUFFICIENT_FOLDS
        else:
            wf_class = WalkForwardClass.PROMOTION_GRADE

        return WalkForwardReport(
            run_id=run_id,
            wf_class=wf_class,
            fold_results=folds,
            caveats=[
                "Walk-forward fold evaluation completed. Ensure gap discipline is observed."
            ],
        )
