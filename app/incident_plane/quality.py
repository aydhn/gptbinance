from pydantic import BaseModel

class IncidentQualityReport(BaseModel):
    incident_id: str
    is_high_quality: bool
