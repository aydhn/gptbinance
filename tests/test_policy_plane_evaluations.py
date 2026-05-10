import pytest
from app.policy_plane.evaluations import PolicyEvaluationEngine
from app.policy_plane.contexts import ContextBuilder
from app.policy_plane.subjects import create_human_operator
from app.policy_plane.actions import create_execute_action
from app.policy_plane.resources import create_symbol_resource
from app.policy_plane.models import PolicyDefinition
from app.policy_plane.rules import create_allow_rule, create_deny_rule
from app.policy_plane.enums import PolicyClass, SubjectClass, ActionClass, ResourceClass
from app.policy_plane.registry import registry


def test_evaluation_deny_overrides():
    registry.clear()

    allow_rule = create_allow_rule(
        [SubjectClass.HUMAN_OPERATOR],
        [ActionClass.EXECUTE],
        [ResourceClass.SYMBOL],
        "Allow execution",
    )
    deny_rule = create_deny_rule(
        [SubjectClass.HUMAN_OPERATOR],
        [ActionClass.EXECUTE],
        [ResourceClass.SYMBOL],
        "Deny execution",
    )

    policy = PolicyDefinition(
        policy_id="POL-002",
        policy_class=PolicyClass.MANDATORY,
        rules=[allow_rule, deny_rule],
        description="Conflict policy",
    )
    registry.register(policy)

    engine = PolicyEvaluationEngine()
    subject = create_human_operator("user1")
    action = create_execute_action()
    resource = create_symbol_resource("BTCUSD")
    context = ContextBuilder().with_environment("live").build()

    record = engine.evaluate(subject, action, resource, context)
    assert record.verdict.verdict_class.name == "DENY"
    assert record.verdict.reason == "DENY_OVERRIDES"
