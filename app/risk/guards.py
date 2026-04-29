from typing import Optional
from app.risk.base import BaseRiskGuard
from app.risk.models import RiskEvaluationRequest, RiskRejectionReason
from app.risk.enums import VetoSeverity, DrawdownState


class DrawdownGuard(BaseRiskGuard):
    def check(self, request: RiskEvaluationRequest) -> Optional[RiskRejectionReason]:
        state = request.context.drawdown_state.current_state
        if state == DrawdownState.HARD_STOP:
            return RiskRejectionReason(
                source="DrawdownGuard",
                severity=VetoSeverity.CRITICAL,
                rationale="Drawdown hard stop active. No new entries allowed.",
            )
        elif state == DrawdownState.REDUCE:
            # We might not veto entirely, just let sizing reduce it,
            # but if it's an entry we could be strict.
            pass
        return None


class StaleDataGuard(BaseRiskGuard):
    def check(self, request: RiskEvaluationRequest) -> Optional[RiskRejectionReason]:
        # Imagine checking timestamp diff
        return None
