from app.policy_plane.models import PolicyObligation
from app.policy_plane.enums import ObligationClass


def create_must_attach_evidence_obligation(
    description: str, refs: list[str] = None
) -> PolicyObligation:
    return PolicyObligation(
        obligation_class=ObligationClass.MUST_ATTACH_EVIDENCE,
        description=description,
        lineage_refs=refs or [],
    )


def create_must_wait_for_approval_obligation(
    description: str, refs: list[str] = None
) -> PolicyObligation:
    return PolicyObligation(
        obligation_class=ObligationClass.MUST_WAIT_FOR_APPROVAL,
        description=description,
        lineage_refs=refs or [],
    )
