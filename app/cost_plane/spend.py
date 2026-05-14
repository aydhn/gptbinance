from app.cost_plane.models import SpendRecord
from app.cost_plane.enums import SpendClass
import uuid

class SpendManager:
    def __init__(self):
        self._records: list[SpendRecord] = []

    def record_spend(self, cost_id: str, spend_class: SpendClass, amount: float, currency: str, proof_notes: str = None) -> SpendRecord:
        record = SpendRecord(
            spend_id=str(uuid.uuid4()),
            cost_id=cost_id,
            spend_class=spend_class,
            amount=amount,
            currency=currency,
            proof_notes=proof_notes
        )
        self._records.append(record)
        return record

    def list_records(self) -> list[SpendRecord]:
        return self._records
