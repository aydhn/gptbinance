from pydantic import BaseModel

class IncidentEquivalenceReport(BaseModel):
    incident_id: str
    is_equivalent_across_envs: bool
    notes: str
