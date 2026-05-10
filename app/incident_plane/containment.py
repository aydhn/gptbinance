from pydantic import BaseModel
from datetime import datetime, timezone

class ContainmentRecord(BaseModel):
    incident_id: str
    scopes_contained: list
    active_holds: list
    is_complete: bool

class IncidentContainmentEngine:
    @staticmethod
    def record_containment(incident_id: str, scopes: list, holds: list) -> ContainmentRecord:
        return ContainmentRecord(
            incident_id=incident_id,
            scopes_contained=scopes,
            active_holds=holds,
            is_complete=True
        )
