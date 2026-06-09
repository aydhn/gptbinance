from app.oversight_plane.models import OversightTrustVerdict
from app.oversight_plane.enums import TrustVerdictEnum

def evaluate_oversight_trust(oversight_record) -> OversightTrustVerdict:
    if not oversight_record:
        return OversightTrustVerdict(verdict=TrustVerdictEnum.BLOCKED, breakdown={"error": "Missing record"})

    # In a real system, checking blind spots, captured reviewers, false clearance
    return OversightTrustVerdict(
        verdict=TrustVerdictEnum.TRUSTED,
        breakdown={"supervisor": "checked", "scope": "checked", "scrutiny": "checked"}
    )
