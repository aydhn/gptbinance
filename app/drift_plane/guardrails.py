from app.drift_plane.models import GuardrailDeviationRecord
from app.drift_plane.enums import GuardrailClass
from typing import Dict
from datetime import datetime

class GuardrailManager:
    def __init__(self):
        self.deviations: Dict[str, GuardrailDeviationRecord] = {}

    def add_deviation(self, deviation_id: str, class_type: GuardrailClass, guardrail_id: str):
        self.deviations[deviation_id] = GuardrailDeviationRecord(
            deviation_id=deviation_id,
            class_type=class_type,
            guardrail_id=guardrail_id,
            deviated_at=datetime.utcnow()
        )

    def get_deviation(self, deviation_id: str) -> GuardrailDeviationRecord:
        return self.deviations.get(deviation_id)
