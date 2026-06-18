from typing import List, Dict, Any
from datetime import datetime
from app.collateral_plane.exceptions import CollateralPlaneError
from app.collateral_plane.models import CollateralObject

class EligibilityManager:
    """
    Manager for eligibility in the collateral plane.
    Ensures strict governance and visibility.
    """
    def __init__(self):
        self.records: Dict[str, Any] = {}

    def register_eligibility(self, entity_id: str, data: Dict[str, Any]) -> str:
        if not entity_id:
            raise CollateralPlaneError("Entity ID required for eligibility")

        # Enforce no theater: ensure lineage refs are present
        data["lineage_refs"] = data.get("lineage_refs", []) + [f"registered_eligibility_{datetime.utcnow().isoformat()}"]
        self.records[entity_id] = data
        return entity_id

    def get_eligibility(self, entity_id: str) -> Dict[str, Any]:
        return self.records.get(entity_id, {})

    def evaluate_integrity(self, entity_id: str) -> List[str]:
        """
        Returns a list of cautions or an empty list if clean.
        """
        cautions = []
        record = self.records.get(entity_id)
        if not record:
            cautions.append(f"Missing eligibility record for {entity_id}")
        # Domain specific checks would go here (e.g. stale valuation check)
        return cautions

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/collateral_plane/eligibility.py")
    return integration.evaluate_posture()
