from app.policy_plane.models import PolicyInvariant
from app.policy_plane.enums import InvariantClass


def create_environment_separation_invariant(
    description: str, proof_notes: str
) -> PolicyInvariant:
    return PolicyInvariant(
        invariant_class=InvariantClass.ENVIRONMENT_SEPARATION,
        description=description,
        proof_notes=proof_notes,
    )


def create_no_bypassable_invariant(
    description: str, proof_notes: str
) -> PolicyInvariant:
    return PolicyInvariant(
        invariant_class=InvariantClass.NON_BYPASSABLE,
        description=description,
        proof_notes=proof_notes,
    )
