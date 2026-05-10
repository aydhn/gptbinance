from app.policy_plane.models import PolicyEquivalenceReport, PolicyAction
from app.policy_plane.enums import EquivalenceVerdict


def compare_environments(
    action: PolicyAction, envs: list[str]
) -> PolicyEquivalenceReport:
    # Simplified mock for equivalence comparison
    return PolicyEquivalenceReport(
        action=action, environments_compared=envs, verdict=EquivalenceVerdict.EQUIVALENT
    )
