from typing import Dict, Any
from app.settlement_plane.models import SSIRecord

class SSIEvaluator:
    def evaluate(self, context: Dict[str, Any]) -> SSIRecord:
        is_stale = context.get("stale_ssi", False)
        is_conflicting = context.get("conflicting_ssi", False)

        if is_stale:
            return SSIRecord(
                id="ssi_stale",
                status="stale",
                details="Stale SSI detected",
                lineage_refs=[]
            )

        if is_conflicting:
            return SSIRecord(
                id="ssi_conflict",
                status="conflicting",
                details="Conflicting SSI detected",
                lineage_refs=[]
            )

        return SSIRecord(
            id="ssi_valid",
            status="valid",
            details="Valid SSI",
            lineage_refs=[]
        )
