# storage.py
import json
from typing import Dict, Any

class InsolvencyStorage:
    def __init__(self, file_path: str = "insolvency_data.json"):
        self.file_path = file_path
        self.data = {}

    def save(self, key: str, value: Any):
        self.data[key] = value
        # In a real app, write to file
        # with open(self.file_path, 'w') as f:
        #     json.dump(self.data, f)

    def load(self, key: str) -> Any:
        # In a real app, read from file
        return self.data.get(key)
