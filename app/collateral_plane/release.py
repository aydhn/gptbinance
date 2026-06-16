from typing import List, Dict, Any
from datetime import datetime
from app.collateral_plane.exceptions import CollateralPlaneError
from app.collateral_plane.models import CollateralObject

class ReleaseManager:
    """
    Manager for release in the collateral plane.
    Ensures strict governance and visibility.
    """
    def __init__(self):
        self.records: Dict[str, Any] = {}

    def register_release(self, entity_id: str, data: Dict[str, Any]) -> str:
        if not entity_id:
            raise CollateralPlaneError("Entity ID required for release")

        # Enforce no theater: ensure lineage refs are present
        data["lineage_refs"] = data.get("lineage_refs", []) + [f"registered_release_{datetime.utcnow().isoformat()}"]
        self.records[entity_id] = data
        return entity_id

    def get_release(self, entity_id: str) -> Dict[str, Any]:
        return self.records.get(entity_id, {})

    def evaluate_integrity(self, entity_id: str) -> List[str]:
        """
        Returns a list of cautions or an empty list if clean.
        """
        cautions = []
        record = self.records.get(entity_id)
        if not record:
            cautions.append(f"Missing release record for {entity_id}")
        # Domain specific checks would go here (e.g. stale valuation check)
        return cautions
