from app.policy_plane.models import PolicyVerdict
from app.policy_plane.enums import VerdictClass


class VerdictEngine:
    pass


def create_allow_verdict(reason: str, proof: str) -> PolicyVerdict:
    return PolicyVerdict(
        verdict_class=VerdictClass.ALLOW, reason=reason, proof_notes=proof
    )


def create_deny_verdict(reason: str, proof: str) -> PolicyVerdict:
    return PolicyVerdict(
        verdict_class=VerdictClass.DENY, reason=reason, proof_notes=proof
    )
