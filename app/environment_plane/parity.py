from app.environment_plane.models import ParityRecord
from app.environment_plane.enums import ParityClass

def evaluate_parity(parity_class: ParityClass, sufficiency_notes: str) -> ParityRecord:
    return ParityRecord(parity_class=parity_class, sufficiency_notes=sufficiency_notes)
