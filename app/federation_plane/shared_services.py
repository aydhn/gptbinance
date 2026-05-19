from typing import Dict, List, Optional
from app.federation_plane.models import SharedServiceRecord
from app.federation_plane.exceptions import FederationPlaneError


class SharedServiceManager:
    def __init__(self):
        self._services: Dict[str, SharedServiceRecord] = {}

    def register(self, record: SharedServiceRecord):
        if not record.service_id or not record.blast_notes:
            raise FederationPlaneError(
                "No shared-service-free-risk fiction. Blast notes required."
            )
        self._services[record.service_id] = record

    def get_service(self, service_id: str) -> Optional[SharedServiceRecord]:
        return self._services.get(service_id)

    def list_services(self) -> List[SharedServiceRecord]:
        return list(self._services.values())
