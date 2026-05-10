from typing import List
from app.postmortem_plane.models import SourceIncidentBundle
from app.postmortem_plane.exceptions import PostmortemPlaneError

class IncidentLinker:
    @staticmethod
    def create_bundle(incident_ids: List[str], severity: str, radius: str, family: str = None) -> SourceIncidentBundle:
        if not incident_ids:
            raise PostmortemPlaneError("Cannot create bundle without incidents")
        return SourceIncidentBundle(
            incident_ids=incident_ids,
            severity_carryover=severity,
            blast_radius=radius,
            incident_family=family
        )
