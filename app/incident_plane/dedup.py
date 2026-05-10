from pydantic import BaseModel

class IncidentDedupRecord(BaseModel):
    primary_incident_id: str
    duplicate_incident_id: str
    confidence: str
    notes: str

class IncidentDedupEngine:
    @staticmethod
    def mark_duplicate(primary: str, duplicate: str, notes: str) -> IncidentDedupRecord:
        return IncidentDedupRecord(primary_incident_id=primary, duplicate_incident_id=duplicate, confidence="High", notes=notes)
