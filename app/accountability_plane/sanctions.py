
from app.accountability_plane.exceptions import InvalidSanctionError, AccountabilityTheaterViolation
from app.accountability_plane.models import SanctionRecord
from app.accountability_plane.enums import SanctionClass

class SanctionsManager:
    def __init__(self):
        self._store = {}

    def apply_sanction(self, sanction_id: str, breach_ref: str, subject_ref: str, tier_ref: str, is_symbolic: bool = False) -> SanctionRecord:
        if is_symbolic:
            raise AccountabilityTheaterViolation("Symbolic sanctions are prohibited.")
        if not breach_ref or not subject_ref:
            raise InvalidSanctionError("Sanction must map to a specific subject and proven breach.")

        record = SanctionRecord(
            sanction_id=sanction_id,
            tier_ref=tier_ref,
            breach_ref=breach_ref,
            subject_ref=subject_ref,
            is_symbolic=is_symbolic
        )
        self._store[sanction_id] = record
        return record

    def get(self, sanction_id: str) -> SanctionRecord:
        return self._store.get(sanction_id)
