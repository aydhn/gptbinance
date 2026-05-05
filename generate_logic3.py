import os

files = {
    "app/order_lifecycle/timeouts.py": """from app.order_lifecycle.models import OrderAttempt, TimeoutResolution
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType, TimeoutClass
from datetime import datetime, timezone

class TimeoutManager:
    def mark_timeout_unknown(self, attempt: OrderAttempt, tclass: TimeoutClass) -> tuple[OrderAttempt, TimeoutResolution]:
        new_state, _ = LifecycleStateMachine.transition(
            attempt.attempt_id, attempt.state, LifecycleState.TIMEOUT_UNKNOWN, TransitionType.MARK_TIMEOUT
        )
        attempt.state = new_state
        res = TimeoutResolution(
             attempt_id=attempt.attempt_id,
             timeout_class=tclass,
             resolved_state=LifecycleState.TIMEOUT_UNKNOWN,
             timestamp=datetime.now(timezone.utc)
        )
        return attempt, res
""",
    "app/order_lifecycle/orphans.py": """from app.order_lifecycle.models import OrphanOrderRecord, DeadLetterEvent
from app.order_lifecycle.enums import OrphanSeverity
from datetime import datetime, timezone
import uuid

class OrphanManager:
    def register_orphan(self, venue_order_id: str, severity: OrphanSeverity, notes: str) -> OrphanOrderRecord:
        return OrphanOrderRecord(
             orphan_id=f"orph_{uuid.uuid4()}",
             venue_order_id=venue_order_id,
             severity=severity,
             timestamp=datetime.now(timezone.utc),
             remediation_notes=notes
        )
""",
    "app/order_lifecycle/dedup.py": """from app.order_lifecycle.enums import DedupVerdict

class DedupEngine:
    def check_event(self, event_id: str) -> DedupVerdict:
        return DedupVerdict.NEW_EVENT
""",
    "app/order_lifecycle/reconciliation.py": """class LifecycleReconciler:
    def reconcile(self) -> dict:
        return {"status": "ok", "unresolved": 0}
""",
    "app/order_lifecycle/policies.py": """class LifecyclePolicyHook:
    pass
""",
    "app/order_lifecycle/reporting.py": """class LifecycleReporter:
    pass
""",
    "app/order_lifecycle/storage.py": """class LifecycleStorage:
    pass
""",
    "app/order_lifecycle/repository.py": """from app.order_lifecycle.models import OrderAttempt

class AttemptRepository:
    def __init__(self):
        self._db = {}

    def save(self, attempt: OrderAttempt):
        self._db[attempt.attempt_id] = attempt

    def get(self, attempt_id: str) -> OrderAttempt:
        return self._db.get(attempt_id)
""",
}

for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)
