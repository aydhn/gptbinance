from typing import List
from datetime import datetime
import uuid

from app.risk.base import BaseRiskEvaluator
from app.risk.models import (
    RiskEvaluationRequest,
    RiskDecision,
    RiskApprovalBundle,
    RiskConfig,
    RiskContext,
)
from app.risk.enums import RiskVerdict, VetoSeverity, ThrottleType
from app.risk.sizing import StandardPositionSizer
from app.risk.policies import MaxExposurePolicy, MaxConcurrentIntentsPolicy
from app.risk.guards import DrawdownGuard, StaleDataGuard
from app.risk.state import RiskStateManager


class RiskEngine(BaseRiskEvaluator):
    def __init__(self, config: RiskConfig, state_manager: RiskStateManager):
        self.config = config
        self.state_manager = state_manager

        self.sizer = StandardPositionSizer(config)
        self.policies = [MaxExposurePolicy(p) for p in config.policies]
        self.policies.append(MaxConcurrentIntentsPolicy(config.max_concurrent_intents))

        self.guards = [DrawdownGuard(), StaleDataGuard()]

    def evaluate_intent(self, request: RiskEvaluationRequest) -> RiskApprovalBundle:
        rejections = []

        # 1. Guards
        for guard in self.guards:
            reason = guard.check(request)
            if reason:
                rejections.append(reason)

        # 2. Policies
        for policy in self.policies:
            reason = policy.evaluate(request)
            if reason:
                rejections.append(reason)

        # Immediate reject if critical/high
        critical_rejections = [
            r
            for r in rejections
            if r.severity in (VetoSeverity.CRITICAL, VetoSeverity.HIGH)
        ]
        if critical_rejections:
            self.state_manager.record_veto(request.context.timestamp)
            decision = RiskDecision(
                verdict=RiskVerdict.REJECT,
                rejection_reasons=rejections,
                rationale="Critical/High veto encountered.",
            )
            return self._build_bundle(request.context.timestamp, decision)

        # 3. Sizing
        sizing_result = self.sizer.calculate_size(request)

        if sizing_result.approved_size == 0:
            rejections.append(
                # Use RiskRejectionReason, but we have to import it locally or use it correctly
            )
            decision = RiskDecision(
                verdict=RiskVerdict.REJECT,
                rejection_reasons=rejections,
                rationale="Approved size reduced to 0.",
            )
            return self._build_bundle(request.context.timestamp, decision)

        # Construct final approved intent
        approved_intent = request.intent.copy()
        approved_intent.quantity = sizing_result.approved_size

        verdict = RiskVerdict.APPROVE
        if sizing_result.approved_size < sizing_result.requested_size or rejections:
            verdict = RiskVerdict.REDUCE

        decision = RiskDecision(
            verdict=verdict,
            approved_intent=approved_intent,
            sizing=sizing_result,
            rejection_reasons=rejections,
            rationale=(
                "Approved with sizing adjustments."
                if verdict == RiskVerdict.REDUCE
                else "Approved."
            ),
        )

        return self._build_bundle(request.context.timestamp, decision)

    def _build_bundle(
        self, timestamp: datetime, decision: RiskDecision
    ) -> RiskApprovalBundle:
        return RiskApprovalBundle(
            timestamp=timestamp,
            request_id=str(uuid.uuid4()),
            decision=decision,
            kill_switch_state=self.state_manager.kill_switch_state,
        )
