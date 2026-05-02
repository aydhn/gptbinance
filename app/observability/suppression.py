from typing import Dict, List, Optional
from datetime import datetime, timezone, timedelta
from app.observability.models import AlertSuppressionState, AlertEvent
from app.observability.enums import SuppressionAction


class SuppressionEngine:
    def __init__(self):
        self._suppressions: Dict[str, AlertSuppressionState] = {}

    def suppress_rule(
        self, rule_id: str, duration_minutes: int, reason: str, created_by: str
    ) -> None:
        until = datetime.now(timezone.utc) + timedelta(minutes=duration_minutes)
        state = AlertSuppressionState(
            alert_rule_id=rule_id,
            suppressed_until=until,
            reason=reason,
            created_by=created_by,
        )
        self._suppressions[rule_id] = state

    def check_suppression(self, rule_id: str) -> SuppressionAction:
        if rule_id in self._suppressions:
            state = self._suppressions[rule_id]
            if datetime.now(timezone.utc) < state.suppressed_until:
                return SuppressionAction.SUPPRESS
            else:
                del self._suppressions[rule_id]  # Expired
        return SuppressionAction.ALLOW

    def get_active_suppressions(self) -> List[AlertSuppressionState]:
        now = datetime.now(timezone.utc)
        active = []
        expired = []
        for rule_id, state in self._suppressions.items():
            if now < state.suppressed_until:
                active.append(state)
            else:
                expired.append(rule_id)

        for rule_id in expired:
            del self._suppressions[rule_id]

        return active


engine = SuppressionEngine()
