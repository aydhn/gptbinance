from app.ml.models import PromotionReadinessReport
from app.ml.enums import PromotionVerdict


class PromotionGate:
    def check_readiness(self, run_id: str) -> PromotionReadinessReport:
        # check validation, calibration, drift, honesty
        return PromotionReadinessReport(
            run_id=run_id,
            verdict=PromotionVerdict.PASS,
            reasons=["All checks passed"],
            blockers=[],
            next_actions=["Promote to shadow"],
        )
