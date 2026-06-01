
from app.accountability_plane.exceptions import InvalidBreachFindingError
from app.accountability_plane.models import BreachRecord
from app.accountability_plane.enums import BreachClass

class BreachesManager:
    def __init__(self):
        self._store = {}

    def register_breach(self, breach_id: str, duty_ref: str, breach_class: BreachClass, evidence_refs: list) -> BreachRecord:
        if not evidence_refs:
            raise InvalidBreachFindingError("Breach without evidence is not allowed.")
        if not duty_ref:
            raise InvalidBreachFindingError("Breach must map to an explicit duty.")

        record = BreachRecord(
            breach_id=breach_id,
            breach_class=breach_class,
            duty_ref=duty_ref,
            evidence_refs=evidence_refs
        )
        self._store[breach_id] = record
        return record

    def get(self, breach_id: str) -> BreachRecord:
        return self._store.get(breach_id)
