from app.postmortems.models import ActionTrackingRecord


class ActionTracker:
    def track(self, action_id: str) -> ActionTrackingRecord:
        return ActionTrackingRecord(action_id=action_id, status="open")
