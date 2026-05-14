from app.cost_plane.models import CostTrustVerdictReport
from app.cost_plane.enums import CostTrustVerdict
from app.cost_plane.base import TrustEvaluatorBase

class TrustManager(TrustEvaluatorBase):
    def evaluate(self, metrics: dict) -> CostTrustVerdictReport:
        blockers = []
        caveats = []
        verdict = CostTrustVerdict.TRUSTED

        if metrics.get("unattributed_spend_ratio", 0) > 0.1:
            blockers.append("High unattributed spend ratio")
            verdict = CostTrustVerdict.BLOCKED

        if metrics.get("budget_breached", False):
            caveats.append("Budget guardrail breached")
            if verdict == CostTrustVerdict.TRUSTED:
                 verdict = CostTrustVerdict.CAUTION

        return CostTrustVerdictReport(
            verdict=verdict,
            factors=metrics,
            blockers=blockers,
            caveats=caveats
        )
