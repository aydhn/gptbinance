import pytest
from app.policy_plane.models import PolicyRule
from app.policy_plane.enums import (
    RuleClass,
    SubjectClass,
    ActionClass,
    ResourceClass,
    ConflictSeverity,
)
from app.policy_plane.conflicts import ConflictDetector


def test_conflict_detection():
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

    detector = ConflictDetector()
    conflicts = detector.detect([allow_rule, deny_rule])

    assert len(conflicts) == 1
    assert conflicts[0].severity == ConflictSeverity.CRITICAL
    assert allow_rule.rule_id in conflicts[0].involved_rule_ids
    assert deny_rule.rule_id in conflicts[0].involved_rule_ids
