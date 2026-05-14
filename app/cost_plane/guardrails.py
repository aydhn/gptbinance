from app.cost_plane.models import GuardrailRecord
from app.cost_plane.enums import GuardrailClass
import uuid

class GuardrailManager:
    def __init__(self):
        self._records: list[GuardrailRecord] = []

    def evaluate_guardrail(self, budget_id: str, guardrail_class: GuardrailClass, ceiling: float, current_value: float) -> GuardrailRecord:
        breached = current_value > ceiling
        record = GuardrailRecord(
            guardrail_id=str(uuid.uuid4()),
            budget_id=budget_id,
            guardrail_class=guardrail_class,
            ceiling=ceiling,
            current_value=current_value,
            breached=breached
        )
        self._records.append(record)
        return record

    def list_records(self) -> list[GuardrailRecord]:
        return self._records
