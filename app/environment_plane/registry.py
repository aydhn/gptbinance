from typing import Dict, List
from app.environment_plane.base import EnvironmentRegistryBase
from app.environment_plane.models import EnvironmentObject
from app.environment_plane.exceptions import InvalidEnvironmentObjectError

class CanonicalEnvironmentRegistry(EnvironmentRegistryBase):
    def __init__(self):
        self._environments: Dict[str, EnvironmentObject] = {}

    def register(self, env: EnvironmentObject) -> None:
        if not env.environment_id:
            raise InvalidEnvironmentObjectError("Environment ID must be provided")
        self._environments[env.environment_id] = env

    def get(self, environment_id: str) -> EnvironmentObject:
        if environment_id not in self._environments:
            raise InvalidEnvironmentObjectError(f"Environment {environment_id} not found")
        return self._environments[environment_id]

    def list_all(self) -> List[EnvironmentObject]:
        return list(self._environments.values())
