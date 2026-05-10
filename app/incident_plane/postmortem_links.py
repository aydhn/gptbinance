from pydantic import BaseModel

class PostmortemLink(BaseModel):
    incident_id: str
    postmortem_id: str
    is_mandatory: bool
