import pytest
from datetime import datetime, timezone
from app.policy_kernel.models import PolicyRule, PolicyRuleVersion
from app.policy_kernel.enums import PolicyDomain, PolicyVerdict
from app.policy_kernel.rules import register_rule, get_rule, list_rules


def test_rule_registry():
    rule = PolicyRule(
        rule_id="TEST_RULE",
        owner="test",
        rationale="test",
        domain=PolicyDomain.GENERAL,
        severity=PolicyVerdict.CAUTION,
        version=PolicyRuleVersion(
            version_id="v1", effective_from=datetime.now(timezone.utc)
        ),
    )
    register_rule(rule)
    assert get_rule("TEST_RULE") == rule
    assert rule in list_rules()
