import json

class CostStorage:
    def __init__(self):
        self._db = {}

    def save(self, collection: str, record_id: str, data: dict):
        if collection not in self._db:
            self._db[collection] = {}
        self._db[collection][record_id] = data

    def get(self, collection: str, record_id: str):
        return self._db.get(collection, {}).get(record_id)

    def list(self, collection: str):
        return list(self._db.get(collection, {}).values())
