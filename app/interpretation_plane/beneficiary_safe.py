from app.interpretation_plane.models import InterpretationObject, ReadingRecord
from app.interpretation_plane.exceptions import BeneficiaryErasingConstructionViolation

def enforce_beneficiary_safety(obj: InterpretationObject, selected_reading: ReadingRecord):
    safe_readings = [r for r in obj.readings.values() if r.is_beneficiary_safe and not r.is_rejected]

    if safe_readings and not selected_reading.is_beneficiary_safe:
        raise BeneficiaryErasingConstructionViolation(
            f"Reading {selected_reading.reading_id} erases beneficiary rights while safe alternative exists."
        )
