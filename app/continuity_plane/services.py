from typing import Dict, List, Optional
from app.continuity_plane.registry import CanonicalContinuityRegistry
from app.continuity_plane.models import ContinuityService

class ContinuityServiceRegistry:
    def __init__(self, canonical_registry: CanonicalContinuityRegistry):
        self._registry = canonical_registry

    def register_service(self, service: ContinuityService) -> None:
        self._registry.register(service)

    def get_service(self, service_id: str) -> Optional[ContinuityService]:
        return self._registry.get_service(service_id)

    def list_services(self) -> List[ContinuityService]:
        return self._registry.list_services()
