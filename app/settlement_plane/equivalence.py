from typing import Dict, Any
from app.settlement_plane.enums import EquivalenceVerdict
from app.settlement_plane.models import SettlementEquivalenceReport

class SettlementEquivalenceEvaluator:
    def evaluate(self, replay_env: Dict[str, Any], live_env: Dict[str, Any]) -> SettlementEquivalenceReport:
        divergences = []
        if replay_env.get("instruction") != live_env.get("instruction"):
            divergences.append("instruction_divergence")
        if replay_env.get("ssi") != live_env.get("ssi"):
            divergences.append("ssi_divergence")
        if replay_env.get("matching") != live_env.get("matching"):
            divergences.append("matching_divergence")
        if replay_env.get("finality") != live_env.get("finality"):
            divergences.append("finality_divergence")

        if divergences:
            return SettlementEquivalenceReport(
                id="eq_report",
                verdict=EquivalenceVerdict.DIVERGENT,
                divergence_sources=divergences
            )
        return SettlementEquivalenceReport(
            id="eq_report",
            verdict=EquivalenceVerdict.EQUIVALENT,
            divergence_sources=[]
        )
