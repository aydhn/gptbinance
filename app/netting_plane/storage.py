from typing import Dict, Any

class StorageManager:
    def __init__(self):
        self.store: Dict[str, Any] = {}

    def save(self, key: str, value: Any) -> None:
        self.store[key] = value

    def load(self, key: str) -> Any:
        return self.store.get(key)
