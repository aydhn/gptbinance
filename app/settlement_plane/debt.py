from app.settlement_plane.models import SettlementDebtRecord

def track_debt(settlement_id: str, debt_type: str):
    return SettlementDebtRecord(
        id=f"debt_{settlement_id}",
        settlement_id=settlement_id,
        debt_type=debt_type
    )
