from typing import Dict, Any, List
from .models import TradeoffObject

class TradeoffQualityChecker:
    def check_quality(self, tradeoff_obj: TradeoffObject) -> Dict[str, Any]:
        warnings = []

        # Hidden burden check
        if any(b.is_hidden for b in tradeoff_obj.burden_posture):
            warnings.append("hidden_burden_shift_warning")

        # Single-metric theater warning (only 1 objective, but has burdens)
        if len(tradeoff_obj.objective_set.objectives) == 1 and len(tradeoff_obj.burden_posture) > 0:
             warnings.append("single_metric_theater_warning")

        # Sacrifice burial warning (burdens exist but no sacrifices)
        if len(tradeoff_obj.burden_posture) > 0 and len(tradeoff_obj.sacrifices) == 0:
            warnings.append("sacrifice_burial_warning")

        return {
            "tradeoff_id": tradeoff_obj.tradeoff_id,
            "warnings": warnings,
            "is_high_quality": len(warnings) == 0
        }

quality_checker = TradeoffQualityChecker()
