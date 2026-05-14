from typing import Dict, List, Optional
from app.continuity_plane.models import ContinuityIncidentLink

class ContinuityIncidentManager:
    def __init__(self):
        self._links: Dict[str, ContinuityIncidentLink] = {}

    def record_link(self, link: ContinuityIncidentLink) -> None:
        self._links[link.incident_id] = link

    def get_links_for_service(self, service_id: str) -> List[ContinuityIncidentLink]:
        return [l for l in self._links.values() if l.service_id == service_id]
