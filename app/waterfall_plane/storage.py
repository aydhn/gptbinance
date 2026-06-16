import json

class WaterfallStorage:
    def __init__(self, file_path: str = "waterfall_storage.json"):
        self.file_path = file_path
        self._data = {}

    def save(self, record_id: str, record_data: dict):
        self._data[record_id] = record_data
        with open(self.file_path, "w") as f:
            json.dump(self._data, f)

    def load(self, record_id: str) -> dict:
        return self._data.get(record_id, {})
