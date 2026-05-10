from pydantic import BaseModel

class PostmortemLink(BaseModel):
    incident_id: str
    postmortem_id: str
    is_mandatory: bool


class IncidentPostmortemLinker:
    def get_postmortem_requirement(self, incident_severity: str) -> bool:
        if incident_severity in ["CRITICAL", "HIGH"]:
            return True
        return False

    def link_incident_to_postmortem(self, incident_id: str, postmortem_id: str):
        pass
