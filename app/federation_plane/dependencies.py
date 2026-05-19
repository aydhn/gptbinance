from typing import Dict, List, Optional
from app.federation_plane.models import DependencyFederationRecord
from app.federation_plane.exceptions import FederationPlaneError


class DependencyManager:
    def __init__(self):
        self._dependencies: Dict[str, DependencyFederationRecord] = {}

    def register(self, record: DependencyFederationRecord):
        if not record.dependency_id:
            raise FederationPlaneError("No isolated-domain fiction allowed.")
        self._dependencies[record.dependency_id] = record

    def get_dependency(
        self, dependency_id: str
    ) -> Optional[DependencyFederationRecord]:
        return self._dependencies.get(dependency_id)

    def list_dependencies(self) -> List[DependencyFederationRecord]:
        return list(self._dependencies.values())
