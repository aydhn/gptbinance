import pytest
from app.policy_plane.coverage import CoverageAnalyzer
from app.policy_plane.models import PolicyDefinition, PolicyRule
from app.policy_plane.enums import (
    PolicyClass,
    RuleClass,
    SubjectClass,
    ActionClass,
    ResourceClass,
)


def test_coverage():
    rule = PolicyRule(
        rule_class=RuleClass.ALLOW,
        subject_classes=[SubjectClass.HUMAN_OPERATOR],
        action_classes=[ActionClass.EXECUTE],
        resource_classes=[ResourceClass.SYMBOL],
        description="Coverage",
    )
    policy = PolicyDefinition(
        policy_id="POL-COV",
        policy_class=PolicyClass.MANDATORY,
        rules=[rule],
        description="Coverage Test",
    )
    analyzer = CoverageAnalyzer()
    uncovered = analyzer.get_uncovered_actions([policy])

    assert ActionClass.EXECUTE not in uncovered
    assert ActionClass.APPROVE in uncovered
