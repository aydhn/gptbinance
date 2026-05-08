from app.allocation.models import AllocationTrustVerdictReport
from app.allocation.enums import TrustVerdict


class TrustEvaluator:
    def evaluate(
        self, signals_healthy: bool, budgets_healthy: bool
    ) -> AllocationTrustVerdictReport:
        verdict = TrustVerdict.TRUSTED
        caveats = []
        blockers = []

        if not budgets_healthy:
            verdict = TrustVerdict.DEGRADED
            blockers.append("budget_integrity_degraded")

        if not signals_healthy:
            verdict = TrustVerdict.CAUTION
            caveats.append("signals_health_warning")

        return AllocationTrustVerdictReport(
            verdict=verdict,
            signal_trust=1.0 if signals_healthy else 0.5,
            model_trust=1.0,
            feature_trust=1.0,
            budget_integrity_score=1.0 if budgets_healthy else 0.0,
            caveats=caveats,
            blockers=blockers,
        )
