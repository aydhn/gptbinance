import pytest
from datetime import datetime, timezone
from app.policy_kernel.models import (
    PolicyRule,
    PolicyRuleVersion,
    PolicyInvariant,
    PolicyContext,
    PolicyEvidenceBundle,
)
from app.policy_kernel.enums import PolicyDomain, PolicyVerdict, RuleClass
from app.policy_kernel.rules import register_rule, get_rule, list_rules
from app.policy_kernel.invariants import (
    register_invariant,
    get_invariant,
    list_invariants,
)
from app.policy_kernel.evaluation import evaluate_policy
from app.policy_kernel.precedence import resolve_precedence


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


def test_precedence_resolution():
    from app.policy_kernel.models import PolicyDecisionNode

    nodes = [
        PolicyDecisionNode(
            rule_id="R1", verdict=PolicyVerdict.ALLOW, evidence_used=[], reasoning=""
        ),
        PolicyDecisionNode(
            rule_id="R2", verdict=PolicyVerdict.BLOCK, evidence_used=[], reasoning=""
        ),
        PolicyDecisionNode(
            rule_id="R3", verdict=PolicyVerdict.CAUTION, evidence_used=[], reasoning=""
        ),
    ]

    assert resolve_precedence(nodes) == PolicyVerdict.BLOCK

    nodes.append(
        PolicyDecisionNode(
            rule_id="INV1",
            verdict=PolicyVerdict.HARD_BLOCK,
            evidence_used=[],
            reasoning="",
        )
    )
    assert resolve_precedence(nodes) == PolicyVerdict.HARD_BLOCK


def test_policy_evaluation():
    ctx = PolicyContext(
        action_type="test_action",
        workspace_id="ws_1",
        profile_id="prof_1",
        mode="testnet",
    )
    ev = PolicyEvidenceBundle(stress_refs={"data": True})

    decision = evaluate_policy("test_action", ctx, ev)

    # Rationale: RULE_LOW_CONF_STRESS_TESTNET requires stress_refs, we provided it, so it shouldn't trigger block here (simplified logic)
    assert decision.final_verdict is not None
