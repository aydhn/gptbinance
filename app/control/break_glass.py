
from datetime import datetime, timezone
from typing import Dict, List
from app.control.models import (
    BreakGlassRequest,
    BreakGlassDecision,
    ActionRequest,
    OperatorIdentity,
    AuthorizationResult,
)
from app.control.enums import (
    BreakGlassSeverity,
    AuthorizationVerdict,
    SensitiveActionType,
)
from app.control.actions import registry as action_registry
from app.control.exceptions import BreakGlassViolation


class BreakGlassManager:
    def __init__(self):
        self._requests: Dict[str, BreakGlassRequest] = {}
        self._decisions: List[BreakGlassDecision] = []

    def request_break_glass(
        self, request_id: str, severity: BreakGlassSeverity, justification: str
    ) -> BreakGlassRequest:
        req = BreakGlassRequest(
            request_id=request_id, severity=severity, justification=justification
        )
        self._requests[request_id] = req
        return req

    def authorize_break_glass(
        self,
        request: ActionRequest,
        operator: OperatorIdentity,
        bg_request: BreakGlassRequest,
    ) -> AuthorizationResult:
        action = action_registry.get_action(request.action_type)
        if not action or not action.allow_break_glass:
            raise BreakGlassViolation(
                f"Break-glass not allowed for action type: {request.action_type.value}"
            )

        now = datetime.now(timezone.utc)
        decision = BreakGlassDecision(
            request_id=request.id, authorized_by=operator, timestamp=now
        )
        self._decisions.append(decision)

        return AuthorizationResult(
            request_id=request.id,
            verdict=AuthorizationVerdict.APPROVED,
            reason=f"Break-glass authorized by {operator.id}",
            timestamp=now,
            is_break_glass=True,
        )


manager = BreakGlassManager()
