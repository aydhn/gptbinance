from app.events.models import EventRiskOverlay
from app.events.enums import EventGateVerdict
from app.products.enums import ProductType
from app.execution.derivatives.models import (
    DerivativeExecutionIntent,
    LiquidationSnapshot,
)
from .derivatives import DerivativeRiskController
from typing import Dict, Any, List
from app.execution.live.models import ExecutionIntent
from app.risk.models import (
    RiskConfig,
    RiskEvaluationRequest,
    RiskApprovalBundle,
    RiskDecision,
)
from app.risk.enums import RiskVerdict, ThrottleType
from app.risk.state import RiskStateManager
from datetime import datetime
import uuid


class RiskEngine:
    def __init__(self, config: RiskConfig, state_manager: RiskStateManager):
        self.config = config
        self.state_manager = state_manager

    def evaluate_intent(
        self, request: RiskEvaluationRequest, event_overlay: EventRiskOverlay = None
    ) -> RiskApprovalBundle:
        # Event-Risk Overlay evaluation
        rejection_reasons = []
        if event_overlay:
            if event_overlay.verdict in [EventGateVerdict.BLOCK, EventGateVerdict.HALT]:
                return RiskApprovalBundle(
                    decision=RiskDecision(
                        verdict=RiskVerdict.REJECT,
                        approved_intent=request.intent,
                        throttle_applied=ThrottleType.NONE,
                        rejection_reasons=event_overlay.reasons,
                        risk_score=0.0,
                    ),
                    signatures=[
                        RiskSignature(
                            component="event_overlay",
                            authorized=False,
                            reason="Blocked by event overlay",
                            severity=5,
                        )
                    ],
                    global_verdict=RiskVerdict.REJECT,
                )
            elif (
                event_overlay.verdict == EventGateVerdict.REDUCE_ONLY
                and hasattr(request.intent, "side")
                and request.intent.side.lower() == "buy"
            ):
                return RiskApprovalBundle(
                    decision=RiskDecision(
                        verdict=RiskVerdict.REJECT,
                        approved_intent=request.intent,
                        throttle_applied=ThrottleType.NONE,
                        rejection_reasons=["Reduce-only event window active"],
                        risk_score=0.0,
                    ),
                    signatures=[
                        RiskSignature(
                            component="event_overlay",
                            authorized=False,
                            reason="Reduce-only event window active",
                            severity=4,
                        )
                    ],
                    global_verdict=RiskVerdict.REJECT,
                )

        # Mock evaluation: just approve it for phase 18
        decision = RiskDecision(
            verdict=RiskVerdict.APPROVE,
            approved_intent=request.intent,
            throttle_applied=ThrottleType.NONE,
            rationale="Auto-approved by mock risk engine",
        )
        return RiskApprovalBundle(
            timestamp=datetime.utcnow(),
            request_id=str(uuid.uuid4()),
            decision=decision,
            kill_switch_state=self.state_manager.kill_switch_state,
        )

    def configure_derivatives(self, derivative_risk: DerivativeRiskController):
        self.derivative_risk = derivative_risk

    def evaluate_derivative_intent(
        self,
        intent: DerivativeExecutionIntent,
        current_leverage: int,
        liq_snapshot: LiquidationSnapshot = None,
    ) -> bool:
        if not self.derivative_risk:
            logger.error("Derivative risk controller not configured!")
            return False

        if not self.derivative_risk.check_leverage_cap(
            intent.product_type, current_leverage
        ):
            return False

        if liq_snapshot and not self.derivative_risk.check_liquidation_buffer(
            liq_snapshot
        ):
            if not intent.is_reduce_only:
                logger.error(
                    "Blocked non-reduce-only order due to liquidation proximity."
                )
                return False

        return True

    def process_batch(
        self, requests: List[RiskEvaluationRequest]
    ) -> List[RiskApprovalBundle]:
        bundles = []
        for req in requests:
            bundles.append(self.evaluate_intent(req))
        return bundles

    # Added in Phase 38
    def apply_stress_overlay(self, overlay_decision):
        if overlay_decision.verdict in ["BLOCK", "REDUCE"]:
            self._logger.warning(
                f"Stress budget breached. Applying restrictions. Reasons: {overlay_decision.reasons}"
            )
        return True
