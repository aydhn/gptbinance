from app.liability_plane.storage import LiabilityStorage
from app.liability_plane.registry import CanonicalLiabilityRegistry
from app.liability_plane.liabilities import LiabilityManager

class LiabilityRepository:
    def __init__(self):
        self.storage = LiabilityStorage()
        self.registry = CanonicalLiabilityRegistry()
        self.manager = LiabilityManager()

    def register_and_save(self, obj):
        self.registry.register_liability(obj)
        record = self.manager.initialize_record(obj)
        self.storage.save(record)
        return record

    def get_liability_record(self, liability_id: str):
        return self.storage.load(liability_id)
