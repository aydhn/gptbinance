import json
from typing import Dict, Any, List
from pydantic import BaseModel


class ReliabilityStorage:
    def __init__(self):
        self._data: Dict[str, Any] = {}

    def save(self, key: str, item: BaseModel):
        self._data[key] = item.model_dump()

    def get(self, key: str) -> dict:
        return self._data.get(key)

    def list_all(self, prefix: str) -> List[dict]:
        return [v for k, v in self._data.items() if k.startswith(prefix)]


storage = ReliabilityStorage()
