from app.waterfall_plane.models import OverdistributionRecord

def register_overdistribution(record_id: str, claim_id: str, excess_amount: float) -> OverdistributionRecord:
    return OverdistributionRecord(record_id=record_id, claim_id=claim_id, excess_amount=excess_amount)
