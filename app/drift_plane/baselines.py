from app.drift_plane.models import BaselineRecord, BaselineScopeRecord
from app.drift_plane.enums import BaselineClass
from typing import Dict
from datetime import datetime

class BaselineManager:
    def __init__(self):
        self.baselines: Dict[str, BaselineRecord] = {}

    def set_baseline(self, baseline_id: str, class_type: BaselineClass, owner: str, scope: BaselineScopeRecord):
        self.baselines[baseline_id] = BaselineRecord(
            baseline_id=baseline_id,
            class_type=class_type,
            scope=scope,
            established_at=datetime.utcnow(),
            owner=owner
        )

    def get_baseline(self, baseline_id: str) -> BaselineRecord:
        return self.baselines.get(baseline_id)
