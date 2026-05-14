import json
from typing import Dict, Any

class ValueStorage:
    def __init__(self):
        self._store: Dict[str, Dict[str, Any]] = {}

    def save(self, category: str, record_id: str, data: Dict[str, Any]):
        if category not in self._store:
            self._store[category] = {}
        self._store[category][record_id] = data

    def load(self, category: str, record_id: str) -> Dict[str, Any]:
        return self._store.get(category, {}).get(record_id)

value_storage = ValueStorage()
