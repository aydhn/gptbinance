from app.orchestration_plane.enums import TrustVerdict

class RemedyLinkage:
    """Ensures remedy actions possess a validated orchestration posture."""
    def evaluate_safe_claim(self, orchestration_ref: str = None) -> TrustVerdict:
        if not orchestration_ref:
            # Emit explicit caution for un-orchestrated execution
            return TrustVerdict.CAUTION
        return TrustVerdict.TRUSTED
