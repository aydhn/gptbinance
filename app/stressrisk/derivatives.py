from app.crossbook.overlay import CrossBookOverlay
from app.crossbook.enums import CrossBookVerdict
from app.stressrisk.models import FundingStressSnapshot


class DerivativesStressEngine:
    def evaluate(self, positions: dict) -> FundingStressSnapshot:
# Cross-book integration: fake hedge under stress
        overlay = CrossBookOverlay()
        decision = overlay.decide()
        if decision.verdict == CrossBookVerdict.BLOCK:
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(f"Derivatives stress flagged by cross-book blocks: {decision.reasons}")

        return FundingStressSnapshot(
            total_funding_burden_jump=500.0,
            borrow_cost_jump=100.0,
            liquidation_proximity_tightening=0.05,
        )
