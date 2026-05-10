from pydantic import BaseModel
from datetime import datetime, timezone

class IncidentActionRecord(BaseModel):
    incident_id: str
    action_type: str
    rationale: str
    executed_at: datetime
    executed_by: str

class IncidentActionEngine:
    @staticmethod
    def record_action(incident_id: str, action: str, rationale: str, operator: str) -> IncidentActionRecord:
        if not rationale:
            raise ValueError("Hidden action not allowed.")
        return IncidentActionRecord(
            incident_id=incident_id,
            action_type=action,
            rationale=rationale,
            executed_at=datetime.now(timezone.utc),
            executed_by=operator
        )
