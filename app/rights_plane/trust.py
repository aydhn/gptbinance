from app.rights_plane.models import RightsTrustVerdict
from app.rights_plane.enums import TrustVerdict
from typing import Dict, Any

def evaluate_rights_trust(rights_manifest: Dict[str, Any]) -> RightsTrustVerdict:
    cautions = []
    blockers = []

    if rights_manifest.get("pseudo_consent_count", 0) > 0:
        cautions.append("Pseudo-consent paths active.")
    if rights_manifest.get("waiver_laundering_attempts", 0) > 0:
        blockers.append("Invalid waiver / laundering detected.")
    if rights_manifest.get("standing_burials", 0) > 0:
        blockers.append("Beneficiary standing explicitly buried.")

    verdict = TrustVerdict.TRUSTED
    if cautions: verdict = TrustVerdict.CAUTION
    if blockers: verdict = TrustVerdict.BLOCKED
    if rights_manifest.get("review_needed"): verdict = TrustVerdict.REVIEW_REQUIRED

    return RightsTrustVerdict(verdict=verdict, cautions=cautions, blockers=blockers)
