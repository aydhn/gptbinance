from typing import Any

class ObservabilityStorageEngine:
    def __init__(self):
        self.data = {}

    def write(self, key: str, value: Any) -> None:
        self.data[key] = value

    def read(self, key: str) -> Any:
        return self.data.get(key)
