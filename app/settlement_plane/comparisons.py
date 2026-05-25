from app.settlement_plane.models import SettlementComparisonRecord

def compare_settlements(s1_id: str, s2_id: str):
    return SettlementComparisonRecord(
        id=f"cmp_{s1_id}_{s2_id}",
        settlement_a=s1_id,
        settlement_b=s2_id,
        differences={"scope": "different"}
    )
