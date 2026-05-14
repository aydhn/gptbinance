from app.cost_plane.models import VarianceRecord
from app.cost_plane.enums import VarianceClass
import uuid

class VarianceManager:
    def __init__(self):
        self._records: list[VarianceRecord] = []

    def record_variance(self, cost_id: str, variance_class: VarianceClass, expected: float, actual: float, is_anomaly: bool, proof_notes: str = None) -> VarianceRecord:
        variance_amount = actual - expected
        record = VarianceRecord(
            variance_id=str(uuid.uuid4()),
            cost_id=cost_id,
            variance_class=variance_class,
            expected=expected,
            actual=actual,
            variance_amount=variance_amount,
            is_anomaly=is_anomaly,
            proof_notes=proof_notes
        )
        self._records.append(record)
        return record

    def list_records(self) -> list[VarianceRecord]:
        return self._records
