from app.cost_plane.models import UsageCostRecord
import uuid

class UsageCostManager:
    def __init__(self):
        self._records: list[UsageCostRecord] = []

    def record_usage(self, cost_id: str, unit_cost: float, units_used: float, currency: str) -> UsageCostRecord:
        total = unit_cost * units_used
        record = UsageCostRecord(
            usage_id=str(uuid.uuid4()),
            cost_id=cost_id,
            unit_cost=unit_cost,
            units_used=units_used,
            total_cost=total,
            currency=currency
        )
        self._records.append(record)
        return record

    def list_records(self) -> list[UsageCostRecord]:
        return self._records
