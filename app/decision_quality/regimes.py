from typing import List, Dict
from .models import DecisionFunnelRecord, OpportunityCandidate


class RegimeQualityAnalyzer:
    """
    Analyzes decision quality based on market regimes.
    """

    def get_funnel_summary_by_regime(
        self,
        candidates: List[OpportunityCandidate],
        funnels: List[DecisionFunnelRecord],
    ) -> Dict[str, Dict[str, int]]:
        """
        Groups funnel outcomes by regime.
        """
        summary = {}
        funnel_map = {f.opportunity_id: f for f in funnels}

        for candidate in candidates:
            regime = candidate.regime
            if regime not in summary:
                summary[regime] = {
                    "total": 0,
                    "executed": 0,
                    "blocked": 0,
                    "skipped": 0,
                    "suppressed": 0,
                }

            summary[regime]["total"] += 1

            funnel = funnel_map.get(candidate.id)
            if funnel:
                class_val = funnel.final_class.value
                if class_val in summary[regime]:
                    summary[regime][class_val] += 1

        return summary
