class ScopeControlManager:
    def __init__(self):
        self.records = {}

    def add(self, entity_id: str, data: dict):
        self.records[entity_id] = data
        return data

    def get(self, entity_id: str):
        return self.records.get(entity_id)

    def list_all(self):
        return list(self.records.values())
