from app.stressrisk.models import StressOverlayDecision, StressBudgetResult
from app.stressrisk.enums import StressOverlayVerdict, BudgetVerdict
from app.policy_kernel.enums import PolicyDomain, PolicyVerdict
from typing import Dict, Any
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

    def stress_collateral_truth_caution(self):
        pass

    def get_policy_domain_outputs(
        self, overlay: StressOverlayDecision
    ) -> Dict[str, Any]:
        """Expose Stress Overlay outputs for Policy Kernel Domain format"""
        verdict = PolicyVerdict.ALLOW
        if overlay.verdict == StressOverlayVerdict.BLOCK:
            verdict = PolicyVerdict.BLOCK
        elif overlay.verdict == StressOverlayVerdict.REDUCE:
            verdict = PolicyVerdict.CAUTION
        elif overlay.verdict == StressOverlayVerdict.CAUTION:
            verdict = PolicyVerdict.ADVISORY

        return {
            "domain": PolicyDomain.STRESS_RISK,
            "reasons": overlay.reasons,
            "verdict": verdict,
        }
