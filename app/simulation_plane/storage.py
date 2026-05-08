from app.simulation_plane.exceptions import SimulationStorageError
from typing import Any


class SimulationStorage:
    def __init__(self):
        self._data = {}

    def save(self, key: str, value: Any) -> None:
        self._data[key] = value

    def load(self, key: str) -> Any:
        if key not in self._data:
            raise SimulationStorageError(f"Key {key} not found")
        return self._data[key]
