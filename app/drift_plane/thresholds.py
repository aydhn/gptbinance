from app.drift_plane.models import ThresholdBreachRecord
from app.drift_plane.enums import BreachClass
from typing import Dict
from datetime import datetime

class ThresholdManager:
    def __init__(self):
        self.breaches: Dict[str, ThresholdBreachRecord] = {}

    def add_breach(self, breach_id: str, class_type: BreachClass, threshold_id: str):
        self.breaches[breach_id] = ThresholdBreachRecord(
            breach_id=breach_id,
            class_type=class_type,
            threshold_id=threshold_id,
            breached_at=datetime.utcnow()
        )

    def get_breach(self, breach_id: str) -> ThresholdBreachRecord:
        return self.breaches.get(breach_id)

    # ADAPTATION PLANE INTEGRATION: threshold changes adaptation-plane recalibration safety and side-effect refs ile canonical bağlansın
    # ADAPTATION PLANE INTEGRATION: threshold relaxation treated corrective without adaptation verification explicit caution üretsin