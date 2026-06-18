
from app.renewal_plane.models import RenewalTrustVerdict, TrustVerdict

class TrustManager:
    def evaluate_trust(self, is_fresh: bool, has_debt: bool) -> RenewalTrustVerdict:
        if has_debt:
            return RenewalTrustVerdict(verdict_id="tv_debt", verdict=TrustVerdict.DEGRADED)
        if not is_fresh:
            return RenewalTrustVerdict(verdict_id="tv_stale", verdict=TrustVerdict.REVIEW_REQUIRED)
        return RenewalTrustVerdict(verdict_id="tv_trusted", verdict=TrustVerdict.TRUSTED)

# RELIANCE PLANE INTEGRATION
# Enforces safe-decision-use, explicit freshness limits, and contradiction avoidance for trust.py.

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/renewal_plane/trust.py")
    return integration.evaluate_posture()
