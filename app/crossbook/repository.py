"""
repository.py
"""
from app.crossbook.storage import CrossBookStorage


class CrossBookRepository:
    def __init__(self, storage: CrossBookStorage):
        self.storage = storage

    def get_latest_graph(self):
        if not self.storage.graphs:
            return None
        return list(self.storage.graphs.values())[-1]

    def get_latest_decision(self):
        if not self.storage.decisions:
            return None
        return list(self.storage.decisions.values())[-1]


crossbook_repository = CrossBookRepository(CrossBookStorage())
