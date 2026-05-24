from typing import Dict, List, Optional
from app.enforcement_plane.models import EnforcementObject
from app.enforcement_plane.exceptions import InvalidEnforcementObjectError

class CanonicalEnforcementRegistry:
    def __init__(self):
        self._enforcements: Dict[str, EnforcementObject] = {}

    def register(self, enforcement: EnforcementObject) -> None:
        if not enforcement.enforcement_id:
            raise InvalidEnforcementObjectError("Enforcement ID is required")
        self._enforcements[enforcement.enforcement_id] = enforcement

    def get(self, enforcement_id: str) -> Optional[EnforcementObject]:
        return self._enforcements.get(enforcement_id)

    def list_all(self) -> List[EnforcementObject]:
        return list(self._enforcements.values())

    def list_by_class(self, enforcement_class) -> List[EnforcementObject]:
        return [e for e in self._enforcements.values() if e.enforcement_class == enforcement_class]
