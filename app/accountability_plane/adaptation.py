"""
Canonical Module: adaptation
Part of Phase 135 - Accountability Plane
"""
from app.accountability_plane.exceptions import AccountabilityPlaneError

class AdaptationManager:
    def __init__(self):
        self._store = {}

    def register(self, record):
        if hasattr(record, 'id'):
            self._store[record.id] = record
        else:
            self._store[id(record)] = record
        return record

    def get(self, record_id: str):
        return self._store.get(record_id)

    def get_all(self):
        return list(self._store.values())
