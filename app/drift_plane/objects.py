from app.drift_plane.models import DriftObject
from app.drift_plane.enums import DriftClass
from app.drift_plane.exceptions import InvalidDriftObjectError
from typing import Dict

class DriftObjectManager:
    def __init__(self):
        self.objects: Dict[str, DriftObject] = {}

    def create_object(self, drift_id: str, class_type: DriftClass, owner: str, scope: str, baseline_posture: str, recurrence_posture: str) -> DriftObject:
        if not drift_id or not class_type:
            raise InvalidDriftObjectError("Vague drift names not allowed.")
        obj = DriftObject(
            drift_id=drift_id,
            class_type=class_type,
            owner=owner,
            scope=scope,
            baseline_posture=baseline_posture,
            recurrence_posture=recurrence_posture
        )
        self.objects[drift_id] = obj
        return obj

    def get_object(self, drift_id: str) -> DriftObject:
        return self.objects.get(drift_id)
