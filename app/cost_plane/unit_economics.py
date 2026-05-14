from app.cost_plane.models import UnitEconomicsRecord
from app.cost_plane.enums import UnitEconomicsClass
import uuid

class UnitEconomicsManager:
    def __init__(self):
        self._records: list[UnitEconomicsRecord] = []

    def record_economics(self, cost_id: str, ue_class: UnitEconomicsClass, unit_cost: float, currency: str, denominator_quality_notes: str) -> UnitEconomicsRecord:
        record = UnitEconomicsRecord(
            record_id=str(uuid.uuid4()),
            cost_id=cost_id,
            ue_class=ue_class,
            unit_cost=unit_cost,
            currency=currency,
            denominator_quality_notes=denominator_quality_notes
        )
        self._records.append(record)
        return record

    def list_records(self) -> list[UnitEconomicsRecord]:
        return self._records
