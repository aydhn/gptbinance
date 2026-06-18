from typing import Dict, Any

class Repository:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    def write(self, record_id: str, data: Any) -> None:
        self.data[record_id] = data

    def read(self, record_id: str) -> Any:
        return self.data.get(record_id)
