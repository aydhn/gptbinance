from typing import Optional
from app.risk.base import BaseRiskPolicy
from app.risk.models import RiskEvaluationRequest, RiskRejectionReason, RiskPolicy
from app.risk.enums import VetoSeverity


class MaxExposurePolicy(BaseRiskPolicy):
    def __init__(self, policy_def: RiskPolicy):
        self.policy_def = policy_def

    def evaluate(self, request: RiskEvaluationRequest) -> Optional[RiskRejectionReason]:
        # Simple gross exposure check
        snap = request.context.exposure_snapshot

        # If we had price, we'd add the intent notional. For now, check current.
        if self.policy_def.max_fraction:
            limit = snap.total_equity * self.policy_def.max_fraction
            if snap.total_gross_exposure > limit:
                return RiskRejectionReason(
                    source=self.policy_def.name,
                    severity=(
                        VetoSeverity.HIGH
                        if self.policy_def.is_hard_limit
                        else VetoSeverity.MEDIUM
                    ),
                    rationale=f"Gross exposure {snap.total_gross_exposure} exceeds limit {limit}",
                )

        return None


class MaxConcurrentIntentsPolicy(BaseRiskPolicy):
    def __init__(self, max_concurrent: int):
        self.max_concurrent = max_concurrent

    def evaluate(self, request: RiskEvaluationRequest) -> Optional[RiskRejectionReason]:
        # A real implementation would track pending intents
        return None
