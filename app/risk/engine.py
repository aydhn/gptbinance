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

    def evaluate_intent(self, request: RiskEvaluationRequest) -> RiskApprovalBundle:
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
            kill_switch_state=self.state_manager.get_kill_switch_state(),
        )

    def process_batch(
        self, requests: List[RiskEvaluationRequest]
    ) -> List[RiskApprovalBundle]:
        bundles = []
        for req in requests:
            bundles.append(self.evaluate_intent(req))
        return bundles
