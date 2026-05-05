from typing import Dict, List
from app.policy_kernel.models import PolicyInvariant, PolicyRuleVersion
from app.policy_kernel.enums import PolicyDomain, PolicyVerdict
from datetime import datetime, timezone

_INVARIANT_REGISTRY: Dict[str, PolicyInvariant] = {}


def register_invariant(invariant: PolicyInvariant):
    _INVARIANT_REGISTRY[invariant.rule_id] = invariant


def get_invariant(rule_id: str) -> PolicyInvariant:
    return _INVARIANT_REGISTRY.get(rule_id)


def list_invariants() -> List[PolicyInvariant]:
    return list(_INVARIANT_REGISTRY.values())


# Sample Invariants
register_invariant(
    PolicyInvariant(
        rule_id="INV_NO_LIVE_ACTION_WITHOUT_SCOPED_CONTEXT",
        owner="core_safety",
        rationale="No live action can occur without an explicit scoped context (workspace/profile matching).",
        domain=PolicyDomain.WORKSPACE,
        severity=PolicyVerdict.HARD_BLOCK,
        required_evidence=["workspace_refs"],
        version=PolicyRuleVersion(
            version_id="v1", effective_from=datetime.now(timezone.utc)
        ),
    )
)

register_invariant(
    PolicyInvariant(
        rule_id="INV_NO_VENUE_AFFECTING_REMEDIATION_AUTO_APPLY",
        owner="remediation_safety",
        rationale="Venue-affecting remediations cannot be auto-applied; they require explicit review.",
        domain=PolicyDomain.REMEDIATION,
        severity=PolicyVerdict.HARD_BLOCK,
        required_evidence=["control_refs"],
        version=PolicyRuleVersion(
            version_id="v1", effective_from=datetime.now(timezone.utc)
        ),
    )
)

register_invariant(
    PolicyInvariant(
        rule_id="INV_NO_REDUCE_ONLY_EXPOSURE_INCREASE",
        owner="order_intent_safety",
        rationale="A reduce-only intent compiling into an exposure-increasing plan is strictly blocked.",
        domain=PolicyDomain.ORDER_INTENT,
        severity=PolicyVerdict.HARD_BLOCK,
        required_evidence=["lifecycle_refs"],
        version=PolicyRuleVersion(
            version_id="v1", effective_from=datetime.now(timezone.utc)
        ),
    )
)

register_invariant(
    PolicyInvariant(
        rule_id="INV_NO_POLICY_ALLOW_UNDER_NON_WAIVABLE_HARD_BLOCK",
        owner="policy_kernel",
        rationale="No policy allow is possible if a non-waivable hard block is present.",
        domain=PolicyDomain.GENERAL,
        severity=PolicyVerdict.HARD_BLOCK,
        version=PolicyRuleVersion(
            version_id="v1", effective_from=datetime.now(timezone.utc)
        ),
    )
)
