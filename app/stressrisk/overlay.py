from app.stressrisk.models import StressOverlayDecision, StressBudgetResult
from app.stressrisk.enums import StressOverlayVerdict, BudgetVerdict
import uuid


class StressOverlayEngine:
    def generate_overlay(
        self, profile: str, budget_result: StressBudgetResult
    ) -> StressOverlayDecision:
        verdict = StressOverlayVerdict.ALLOW
        reasons = []
        if budget_result.verdict == BudgetVerdict.BREACH:
            verdict = (
                StressOverlayVerdict.BLOCK
                if profile in ["live", "canary_live_caution"]
                else StressOverlayVerdict.REDUCE
            )
            reasons.append("Stress budget breached.")
        elif budget_result.verdict == BudgetVerdict.CAUTION:
            verdict = StressOverlayVerdict.CAUTION
            reasons.append("Caution: high tail risk.")

        return StressOverlayDecision(
            run_id=str(uuid.uuid4()),
            profile=profile,
            verdict=verdict,
            reasons=reasons,
            evidence_refs=["run_x"],
        )
