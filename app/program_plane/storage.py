from typing import Dict, Any

class ProgramStorage:
    def __init__(self):
        self._data: Dict[str, Any] = {}

    def save(self, key: str, value: Any):
        self._data[key] = value

    def load(self, key: str) -> Any:
        return self._data.get(key)
