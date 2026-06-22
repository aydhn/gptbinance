from typing import Dict, Any
from app.settlement_plane.base import BaseTrustEvaluator
from app.settlement_plane.models import SettlementTrustVerdict
from app.settlement_plane.enums import TrustVerdict

class SettlementTrustEvaluator(BaseTrustEvaluator):
    def evaluate(self, obj_id: str, factors: Dict[str, Any]) -> SettlementTrustVerdict:
        instruction_clarity = factors.get("instruction_clarity", False)
        ssi_sufficiency = factors.get("ssi_sufficiency", False)
        matching_sufficiency = factors.get("matching_sufficiency", False)
        funding_sufficiency = factors.get("funding_sufficiency", False)
        finality_sufficiency = factors.get("finality_sufficiency", False)

        if not all([instruction_clarity, ssi_sufficiency, matching_sufficiency]):
            verdict = TrustVerdict.BLOCKED
        elif not all([funding_sufficiency, finality_sufficiency]):
            verdict = TrustVerdict.DEGRADED
        else:
            verdict = TrustVerdict.TRUSTED

        return SettlementTrustVerdict(
            id=f"trust_{obj_id}",
            settlement_id=obj_id,
            verdict=verdict,
            factors={k: str(v) for k, v in factors.items()}
        )
