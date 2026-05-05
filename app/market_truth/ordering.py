from app.market_truth.models import OrderingViolation
from app.market_truth.enums import OrderingSeverity
from typing import List


class OrderingEngine:
    def evaluate_ordering(self, events: List[dict]) -> List[OrderingViolation]:
        violations = []
        max_seen = -1
        for idx, ev in enumerate(events):
            ev_id = ev.get("id", -1)
            if ev_id < max_seen:
                severity = (
                    OrderingSeverity.SLIGHTLY_LATE
                    if max_seen - ev_id < 5
                    else OrderingSeverity.SEVERE_OUT_OF_ORDER
                )
                violations.append(
                    OrderingViolation(
                        event_id=str(ev_id),
                        expected_order=max_seen + 1,
                        actual_order=ev_id,
                        severity=severity,
                    )
                )
            else:
                max_seen = ev_id
        return violations
