"""
Migrations module for Adaptation Plane
"""

class MigrationsManager:
    def __init__(self):
        self.records = {}

    def add_record(self, record_id, data):
        self.records[record_id] = data

    def get_record(self, record_id):
        return self.records.get(record_id)

    def evaluate(self, *args, **kwargs):
        return "evaluated"
