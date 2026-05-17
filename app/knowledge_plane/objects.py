class ObjectsManager:
    def __init__(self):
        self.records = {}
    def register(self, record):
        self.records[record.knowledge_id] = record
    def get(self, id):
        return self.records.get(id)
