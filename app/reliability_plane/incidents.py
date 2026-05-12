from datetime import datetime
from typing import Dict, List, Optional

from .models import ReliabilityIncidentLink


class IncidentLinkManager:
    def __init__(self):
        self._links: Dict[str, List[ReliabilityIncidentLink]] = {}

    def link_incident(self, link: ReliabilityIncidentLink) -> None:
        if link.service_id not in self._links:
            self._links[link.service_id] = []
        self._links[link.service_id].append(link)

    def get_links(self, service_id: str) -> List[ReliabilityIncidentLink]:
        return self._links.get(service_id, [])
