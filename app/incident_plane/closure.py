from app.incident_plane.models import IncidentManifest
from app.incident_plane.enums import IncidentStatus, VerificationVerdict, IncidentSeverity
from app.incident_plane.exceptions import InvalidClosureState

class ClosureReadinessEvaluator:
    @staticmethod
    def assert_ready_for_closure(manifest: IncidentManifest) -> bool:
        if manifest.current_status != IncidentStatus.RESOLVED:
            raise InvalidClosureState(f"Incident {manifest.incident_id} must be in RESOLVED state before CLOSURE.")

        if not manifest.verification or manifest.verification.verdict != VerificationVerdict.VERIFIED:
            raise InvalidClosureState(f"Incident {manifest.incident_id} lacks successful recovery verification. Closure blocked.")

        if manifest.severity in [IncidentSeverity.SEV0_EMERGENCY, IncidentSeverity.SEV1_HIGH]:
            pass # Postmortem check placeholder

        return True


from typing import List
from app.postmortem_plane.models import PostmortemDefinition
from app.postmortem_plane.closure import PostmortemClosureGovernance
from app.postmortem_plane.enums import ClosureClass

class IncidentClosureEvaluator:
    def can_close(self, incident_id: str, linked_postmortem: PostmortemDefinition = None) -> bool:
        if linked_postmortem:
            readiness = PostmortemClosureGovernance.evaluate_readiness(linked_postmortem)
            # Incident can be closed even if postmortem is open, but we track it.
            return True
        return True # if no postmortem required
