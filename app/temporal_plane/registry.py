from app.temporal_plane.base import TemporalRegistryBase
from app.temporal_plane.models import TemporalObject
from typing import List

class CanonicalTemporalRegistry(TemporalRegistryBase):
    def __init__(self):
        self._objects = {}
        self.allowed_families = [
            "decision_temporal_record",
            "approval_temporal_record",
            "change_temporal_record",
            "release_temporal_record",
            "autonomy_temporal_record",
            "contract_temporal_record",
            "environment_temporal_record",
            "provenance_temporal_record",
            "incident_temporal_record",
            "migration_temporal_record",
            "learning_temporal_record",
            "cross_plane_temporal_record"
        ]

    def register(self, t_obj: TemporalObject, family: str):
        if family not in self.allowed_families:
            raise ValueError(f"Invalid temporal family: {family}")
        if not t_obj.temporal_id:
            raise ValueError("Vague temporal ID not allowed")
        self._objects[t_obj.temporal_id] = t_obj

    def get(self, t_id: str) -> TemporalObject:
        return self._objects.get(t_id)
