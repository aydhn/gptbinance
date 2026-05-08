import json
from typing import Dict, Any


class AllocationStorage:
    def __init__(self):
        self._store = {}

    def save(self, key: str, data: Any):
        # Dummy memory store
        self._store[key] = data

    def load(self, key: str) -> Any:
        return self._store.get(key)
