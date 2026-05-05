from typing import Dict, Any, Optional
from pydantic import BaseModel


class MigrationStorageEngine:
    def __init__(self):
        # In-memory mock storage for models
        self._store: Dict[str, Dict[str, Any]] = {
            "definitions": {},
            "plans": {},
            "packs": {},
            "results": {},
            "debt": [],
        }

    def save(self, category: str, key: str, data: BaseModel):
        if category not in self._store:
            self._store[category] = {}
        if isinstance(self._store[category], dict):
            self._store[category][key] = data.model_dump()

    def load(self, category: str, key: str) -> Optional[Dict[str, Any]]:
        if category in self._store and isinstance(self._store[category], dict):
            return self._store[category].get(key)
        return None


storage_engine = MigrationStorageEngine()
