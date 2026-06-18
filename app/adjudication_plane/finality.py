from .models import *
from .exceptions import *

def check_finality_adjudication_linkage(ref_id: str, adjudication_id: str) -> dict:
    """Ensures finality linkage does not bypass determination posture."""
    if not adjudication_id:
        return {"safe": False, "caution": f"Explicit caution: no adjudication posture for finality"}
    return {"safe": True, "caution": None, "ref": ref_id, "adjudication_id": adjudication_id}

# RELIANCE PLANE INTEGRATION
# Enforces safe-decision-use, explicit freshness limits, and contradiction avoidance for finality.py.

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/adjudication_plane/finality.py")
    return integration.evaluate_posture()
