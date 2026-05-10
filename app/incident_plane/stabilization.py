from pydantic import BaseModel

class StabilizationRecord(BaseModel):
    incident_id: str
    is_stable: bool
    caveats: str

class IncidentStabilizationEngine:
    @staticmethod
    def mark_stabilized(incident_id: str, caveats: str) -> StabilizationRecord:
        return StabilizationRecord(incident_id=incident_id, is_stable=True, caveats=caveats)
