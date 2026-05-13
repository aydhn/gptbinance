from typing import Dict, List, Optional
from app.continuity_plane.base import ContinuityRegistryBase
from app.continuity_plane.models import ContinuityService
from app.continuity_plane.exceptions import InvalidContinuityDefinition

class CanonicalContinuityRegistry(ContinuityRegistryBase):
    def __init__(self):
        self._services: Dict[str, ContinuityService] = {}

    def register(self, obj: ContinuityService) -> None:
        if not obj.service_id:
            raise InvalidContinuityDefinition("service_id cannot be empty")
        self._services[obj.service_id] = obj

    def get_service(self, service_id: str) -> Optional[ContinuityService]:
        return self._services.get(service_id)

    def list_services(self) -> List[ContinuityService]:
        return list(self._services.values())
