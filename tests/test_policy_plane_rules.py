import pytest
from app.policy_plane.rules import (
    create_allow_rule,
    create_deny_rule,
    create_require_review_rule,
    create_require_evidence_rule,
)
from app.policy_plane.enums import RuleClass, SubjectClass, ActionClass, ResourceClass


def test_create_allow_rule():
    rule = create_allow_rule(
        [SubjectClass.HUMAN_OPERATOR],
        [ActionClass.EXECUTE],
        [ResourceClass.SYMBOL],
        "Allow rule",
    )
    assert rule.rule_class == RuleClass.ALLOW


def test_create_deny_rule():
    rule = create_deny_rule(
        [SubjectClass.HUMAN_OPERATOR],
        [ActionClass.EXECUTE],
        [ResourceClass.SYMBOL],
        "Deny rule",
    )
    assert rule.rule_class == RuleClass.DENY


def test_create_require_review_rule():
    rule = create_require_review_rule(
        [SubjectClass.HUMAN_OPERATOR],
        [ActionClass.EXECUTE],
        [ResourceClass.SYMBOL],
        "Review rule",
    )
    assert rule.rule_class == RuleClass.REQUIRE_REVIEW


def test_create_require_evidence_rule():
    rule = create_require_evidence_rule(
        [SubjectClass.HUMAN_OPERATOR],
        [ActionClass.EXECUTE],
        [ResourceClass.SYMBOL],
        "Evidence rule",
    )
    assert rule.rule_class == RuleClass.REQUIRE_EVIDENCE
