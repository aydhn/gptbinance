from app.cost_plane.models import FeeRecord, ExchangeFeeSchedule
from app.cost_plane.enums import FeeClass
import uuid

class FeeManager:
    def __init__(self):
        self._records: list[FeeRecord] = []
        self._schedules: list[ExchangeFeeSchedule] = []

    def record_fee(self, cost_id: str, fee_class: FeeClass, amount: float, currency: str, drift_warnings: list[str] = None) -> FeeRecord:
        record = FeeRecord(
            fee_id=str(uuid.uuid4()),
            cost_id=cost_id,
            fee_class=fee_class,
            amount=amount,
            currency=currency,
            drift_warnings=drift_warnings or []
        )
        self._records.append(record)
        return record

    def add_schedule(self, schedule: ExchangeFeeSchedule):
        self._schedules.append(schedule)
