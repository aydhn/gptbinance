from app.incident_plane.models import IncidentManifest
from app.incident_plane.enums import IncidentTrustVerdict, IncidentStatus, VerificationVerdict, IncidentSeverity

class IncidentTrustEngine:
    @staticmethod
    def evaluate(manifest: IncidentManifest) -> IncidentTrustVerdict:
        if manifest.current_status not in [IncidentStatus.CLOSED, IncidentStatus.RESOLVED, IncidentStatus.FALSE_POSITIVE]:
            if manifest.severity == IncidentSeverity.SEV0_EMERGENCY:
                return IncidentTrustVerdict.BLOCKED
            if manifest.severity == IncidentSeverity.SEV1_HIGH:
                return IncidentTrustVerdict.DEGRADED

        if manifest.current_status in [IncidentStatus.RESOLVED, IncidentStatus.CLOSED]:
            if not manifest.verification or manifest.verification.verdict != VerificationVerdict.VERIFIED:
                return IncidentTrustVerdict.REVIEW_REQUIRED

        return IncidentTrustVerdict.TRUSTED
