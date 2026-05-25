from app.settlement_plane.models import SettlementTrustVerdict, SettlementRecord
from app.settlement_plane.enums import TrustVerdict

class SettlementTrustEngine:
    def evaluate(self, settlement: SettlementRecord) -> SettlementTrustVerdict:
        if not settlement.release_refs:
            return SettlementTrustVerdict(
                id=f"tv_{settlement.id}",
                settlement_id=settlement.id,
                verdict=TrustVerdict.REVIEW_REQUIRED,
                factors={"release_rigor": "missing"}
            )
        return SettlementTrustVerdict(
            id=f"tv_{settlement.id}",
            settlement_id=settlement.id,
            verdict=TrustVerdict.TRUSTED,
            factors={"release_rigor": "strong"}
        )
