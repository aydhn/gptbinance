from typing import Dict, Any
from app.postmortems.models import ActionTrackingRecord


class ActionTracker:
    def track(self, action_id: str) -> ActionTrackingRecord:
        return ActionTrackingRecord(action_id=action_id, status="open")

    def export_capa_closure_metrics(self) -> Dict[str, Any]:
        return {"overdue_critical_capa_ratio": 0.0}
