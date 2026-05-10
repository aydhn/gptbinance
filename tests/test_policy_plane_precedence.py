import pytest
from app.policy_plane.models import PolicyRule
from app.policy_plane.enums import RuleClass, SubjectClass, ActionClass, ResourceClass
from app.policy_plane.precedence import PrecedenceEvaluator


def test_precedence_deny_overrides():
    allow_rule = PolicyRule(
        rule_class=RuleClass.ALLOW,
        subject_classes=[SubjectClass.HUMAN_OPERATOR],
        action_classes=[ActionClass.EXECUTE],
        resource_classes=[ResourceClass.SYMBOL],
        description="Allow",
    )
    deny_rule = PolicyRule(
        rule_class=RuleClass.DENY,
        subject_classes=[SubjectClass.HUMAN_OPERATOR],
        action_classes=[ActionClass.EXECUTE],
        resource_classes=[ResourceClass.SYMBOL],
        description="Deny",
    )

    evaluator = PrecedenceEvaluator()
    record = evaluator.resolve([allow_rule, deny_rule])

    assert record.winning_rule_id == deny_rule.rule_id
    assert record.reason == "DENY_OVERRIDES"
    assert allow_rule.rule_id in record.losing_rule_ids
