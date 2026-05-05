import pytest
from datetime import datetime, timezone
from app.policy_kernel.models import PolicyInvariant, PolicyRuleVersion
from app.policy_kernel.enums import PolicyDomain, PolicyVerdict, RuleClass
from app.policy_kernel.invariants import (
    register_invariant,
    get_invariant,
    list_invariants,
)


def test_invariant_registry():
    invariant = PolicyInvariant(
        rule_id="TEST_INVARIANT",
        owner="test",
        rationale="test",
        domain=PolicyDomain.GENERAL,
        version=PolicyRuleVersion(
            version_id="v1", effective_from=datetime.now(timezone.utc)
        ),
    )
    register_invariant(invariant)

    assert invariant.rule_class == RuleClass.INVARIANT
    assert invariant.severity == PolicyVerdict.HARD_BLOCK
    assert not invariant.is_waivable
    assert get_invariant("TEST_INVARIANT") == invariant
