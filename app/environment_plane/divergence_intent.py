from app.environment_plane.models import IntendedDivergenceRecord
from app.environment_plane.enums import DivergenceClass

def define_intended_divergence(divergence_class: DivergenceClass, justification_notes: str) -> IntendedDivergenceRecord:
    return IntendedDivergenceRecord(divergence_class=divergence_class, justification_notes=justification_notes)
