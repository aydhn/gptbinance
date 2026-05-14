import json
from typing import Dict, Any, List


class SupplyChainStorage:
    def __init__(self):
        self._data: Dict[str, Dict[str, Any]] = {
            "components": {},
            "origins": {},
            "dependencies": {},
            "builds": {},
            "provenance": {},
            "packages": {},
            "sboms": {},
            "signatures": {},
            "trust": {},
        }

    def save(self, collection: str, item_id: str, data: Any) -> None:
        if collection not in self._data:
            self._data[collection] = {}
        # Simple dict conversion for storage simulation
        if hasattr(data, "model_dump"):
            self._data[collection][item_id] = data.model_dump()
        else:
            self._data[collection][item_id] = data

    def load(self, collection: str, item_id: str) -> Any:
        return self._data.get(collection, {}).get(item_id)

    def list_all(self, collection: str) -> List[Any]:
        return list(self._data.get(collection, {}).values())
