from typing import Dict, List
from app.environment_plane.models import EnvironmentObject
from app.environment_plane.exceptions import EnvironmentStorageError

class EnvironmentStorage:
    def __init__(self):
        self._data: Dict[str, EnvironmentObject] = {}

    def save(self, env: EnvironmentObject) -> None:
        self._data[env.environment_id] = env

    def load(self, environment_id: str) -> EnvironmentObject:
        if environment_id not in self._data:
            raise EnvironmentStorageError(f"Environment {environment_id} not found in storage")
        return self._data[environment_id]

    def load_all(self) -> List[EnvironmentObject]:
        return list(self._data.values())
