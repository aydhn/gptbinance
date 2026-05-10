from pydantic import BaseModel

class IncidentDivergenceReport(BaseModel):
    incident_id: str
    has_divergence: bool
