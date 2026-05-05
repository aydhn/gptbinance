import json


class ExperimentStorage:
    def __init__(self):
        self.data = {}

    def save(self, key: str, value: dict):
        self.data[key] = json.dumps(value)

    def load(self, key: str) -> dict:
        if key in self.data:
            return json.loads(self.data[key])
        return {}
