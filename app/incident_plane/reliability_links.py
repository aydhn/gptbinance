from pydantic import BaseModel

class ReliabilityLink(BaseModel):
    incident_id: str
    slo_breach_id: str
