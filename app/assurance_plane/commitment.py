from app.assurance_plane.models import AssuranceRecord
from typing import List

def check_commitment_linkage(record: AssuranceRecord) -> List[str]:
    # Ensure there is proper assurance evidence for this specific domain.
    warnings = []
    if not record.cases or not any(c.is_complete for c in record.cases):
        warnings.append("No commitment-safe claim without complete assurance posture.")
    return warnings
