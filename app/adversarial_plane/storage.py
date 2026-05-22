from typing import Dict, Any

class StorageManager:
    def __init__(self):
        self._store = {}

    def save(self, key: str, data: Any):
        self._store[key] = data

    def load(self, key: str) -> Any:
        return self._store.get(key)

    def delete(self, key: str):
        if key in self._store:
            del self._store[key]
