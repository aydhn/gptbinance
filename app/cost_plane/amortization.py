from app.cost_plane.models import AmortizationRecord
from app.cost_plane.enums import AmortizationClass
import uuid

class AmortizationManager:
    def __init__(self):
        self._records: list[AmortizationRecord] = []

    def record_amortization(self, cost_id: str, amortization_class: AmortizationClass, total_amount: float, amortized_amount_per_period: float, currency: str, proof_notes: str = None) -> AmortizationRecord:
        record = AmortizationRecord(
            amortization_id=str(uuid.uuid4()),
            cost_id=cost_id,
            amortization_class=amortization_class,
            total_amount=total_amount,
            amortized_amount_per_period=amortized_amount_per_period,
            currency=currency,
            proof_notes=proof_notes
        )
        self._records.append(record)
        return record

    def list_records(self) -> list[AmortizationRecord]:
        return self._records
