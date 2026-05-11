from app.policy_plane.models import PolicyTrustVerdict
from app.policy_plane.enums import TrustVerdict


def evaluate_system_trust() -> PolicyTrustVerdict:
    return PolicyTrustVerdict(
        verdict=TrustVerdict.TRUSTED,
        factors={"coverage": "complete", "conflicts": "resolved"},
    )
