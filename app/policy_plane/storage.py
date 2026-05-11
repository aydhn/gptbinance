from typing import Dict, Any


class PolicyStorage:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    def save(self, key: str, obj: Any):
        self.data[key] = obj

    def load(self, key: str) -> Any:
        return self.data.get(key)


storage = PolicyStorage()
