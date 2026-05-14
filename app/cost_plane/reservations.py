from app.cost_plane.models import ReservationCostRecord
import uuid

class ReservationManager:
    def __init__(self):
        self._records: list[ReservationCostRecord] = []

    def record_reservation(self, cost_id: str, reserved_capacity: float, used_capacity: float, unit_cost: float, currency: str) -> ReservationCostRecord:
        unused = reserved_capacity - used_capacity
        cost_of_unused = max(0, unused * unit_cost)

        record = ReservationCostRecord(
            reservation_id=str(uuid.uuid4()),
            cost_id=cost_id,
            reserved_capacity=reserved_capacity,
            used_capacity=used_capacity,
            cost_of_unused=cost_of_unused,
            currency=currency
        )
        self._records.append(record)
        return record

    def list_records(self) -> list[ReservationCostRecord]:
        return self._records
