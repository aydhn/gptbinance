from pydantic import BaseModel

class IncidentCorrelationReport(BaseModel):
    family_id: str
    incident_ids: list
    relation_type: str

class IncidentCorrelationEngine:
    @staticmethod
    def correlate(incident_ids: list, relation: str) -> IncidentCorrelationReport:
        return IncidentCorrelationReport(family_id="FAM-001", incident_ids=incident_ids, relation_type=relation)
