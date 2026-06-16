from app.indemnity_plane.models import IndemnityTrustVerdict, TrustVerdict
def evaluate_trust(indemnity_id: str) -> IndemnityTrustVerdict:
    return IndemnityTrustVerdict(indemnity_id=indemnity_id, verdict=TrustVerdict.TRUSTED)
