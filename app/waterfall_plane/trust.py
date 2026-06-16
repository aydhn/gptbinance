from app.waterfall_plane.models import WaterfallTrustVerdict
from app.waterfall_plane.enums import TrustVerdict

def evaluate_trust(waterfall_id: str, metrics: dict) -> WaterfallTrustVerdict:
    return WaterfallTrustVerdict(
        waterfall_id=waterfall_id,
        verdict=TrustVerdict.TRUSTED,
        claim_clarity=metrics.get("claim_clarity", True),
        rank_sufficiency=metrics.get("rank_sufficiency", True),
        pool_sufficiency=metrics.get("pool_sufficiency", True),
        reserve_adequacy=metrics.get("reserve_adequacy", True),
        distribution_sufficiency=metrics.get("distribution_sufficiency", True),
        clawback_sufficiency=metrics.get("clawback_sufficiency", True),
        contradiction_cleanliness=metrics.get("contradiction_cleanliness", True)
    )
