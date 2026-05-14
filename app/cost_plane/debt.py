from app.cost_plane.models import CostDebtRecord
import uuid

class CostDebtManager:
    def __init__(self):
        self._records: list[CostDebtRecord] = []

    def record_debt(self, cost_id: str, description: str, severity: str, amount: float, currency: str) -> CostDebtRecord:
        record = CostDebtRecord(
            debt_id=str(uuid.uuid4()),
            cost_id=cost_id,
            description=description,
            severity=severity,
            amount=amount,
            currency=currency
        )
        self._records.append(record)
        return record

    def list_records(self) -> list[CostDebtRecord]:
        return self._records
