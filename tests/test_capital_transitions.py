from app.capital.transitions import create_transition_plan


def test_transition_plan():
    plan = create_transition_plan("canary_micro", "canary_small")
    assert plan.is_upgrade is True
    assert "governance_capital_committee" in plan.required_approvals
    assert "escalation_readiness_pass" in plan.required_checks

    plan2 = create_transition_plan("live_caution_tier_1", "canary_small")
    assert plan2.is_upgrade is False
