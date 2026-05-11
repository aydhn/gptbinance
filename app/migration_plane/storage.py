from typing import Dict, Any

class StorageManager:
    def __init__(self):
        self._data = {}

    def save(self, collection: str, item_id: str, item: Any) -> None:
        if collection not in self._data:
            self._data[collection] = {}
        self._data[collection][item_id] = item

    def get(self, collection: str, item_id: str) -> Any:
        return self._data.get(collection, {}).get(item_id)
