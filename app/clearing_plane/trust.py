from typing import Dict, Any
from app.clearing_plane.exceptions import ClearingPlaneError
from app.clearing_plane.enums import TrustVerdict

class TrustManager:
    def __init__(self):
        self.verdicts: Dict[str, Dict[str, Any]] = {}

    def register(self, clearing_id: str, data: Dict[str, Any]) -> str:
        self.verdicts[clearing_id] = data
        return clearing_id

    def calculate_trusted_verdict(self, clearing_id: str) -> Dict[str, Any]:
        data = self.verdicts.get(clearing_id, {})
        trade_clarity = data.get("trade_clarity", False)
        novation_sufficiency = data.get("novation_sufficiency", False)
        segregation_integrity = data.get("segregation_integrity", False)
        margin_sufficiency = data.get("margin_sufficiency", False)
        default_management = data.get("default_management_ready", False)

        breakdown = {
            "trade_clarity": trade_clarity,
            "novation_sufficiency": novation_sufficiency,
            "segregation_integrity": segregation_integrity,
            "margin_sufficiency": margin_sufficiency,
            "default_management": default_management
        }

        if not all(breakdown.values()):
            return {
                "verdict": TrustVerdict.DEGRADED,
                "status": "caution",
                "breakdown": breakdown
            }

        return {
            "verdict": TrustVerdict.TRUSTED,
            "status": "trusted_clearing_clean",
            "breakdown": breakdown
        }

    def evaluate(self, record_id: str) -> Dict[str, Any]:
        return self.calculate_trusted_verdict(record_id)
