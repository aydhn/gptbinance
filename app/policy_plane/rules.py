from app.policy_plane.models import PolicyRule
from app.policy_plane.enums import RuleClass, SubjectClass, ActionClass, ResourceClass


def create_allow_rule(subject_classes, action_classes, resource_classes, description):
    return PolicyRule(
        rule_class=RuleClass.ALLOW,
        subject_classes=subject_classes,
        action_classes=action_classes,
        resource_classes=resource_classes,
        description=description,
    )


def create_deny_rule(subject_classes, action_classes, resource_classes, description):
    return PolicyRule(
        rule_class=RuleClass.DENY,
        subject_classes=subject_classes,
        action_classes=action_classes,
        resource_classes=resource_classes,
        description=description,
    )


def create_require_review_rule(
    subject_classes, action_classes, resource_classes, description
):
    return PolicyRule(
        rule_class=RuleClass.REQUIRE_REVIEW,
        subject_classes=subject_classes,
        action_classes=action_classes,
        resource_classes=resource_classes,
        description=description,
    )


def create_require_evidence_rule(
    subject_classes, action_classes, resource_classes, description
):
    return PolicyRule(
        rule_class=RuleClass.REQUIRE_EVIDENCE,
        subject_classes=subject_classes,
        action_classes=action_classes,
        resource_classes=resource_classes,
        description=description,
    )
