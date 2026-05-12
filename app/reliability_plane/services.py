from typing import Dict, List, Optional

from .models import ReliabilityService


class ReliabilityServiceManager:
    def __init__(self, registry):
        self._registry = registry

    def register_service(self, service: ReliabilityService) -> None:
        self._registry.register_service(service)

    def get_service(self, service_id: str) -> Optional[ReliabilityService]:
        return self._registry.get_service(service_id)

    def list_services(self) -> List[ReliabilityService]:
        return self._registry.list_services()
