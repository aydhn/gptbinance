from typing import List
from app.policy_plane.models import PolicyRule, PolicyConflictRecord
from app.policy_plane.enums import RuleClass, ConflictSeverity


class ConflictDetector:
    def detect(self, rules: List[PolicyRule]) -> List[PolicyConflictRecord]:
        conflicts = []
        has_allow = False
        has_deny = False
        rule_ids = []

        for rule in rules:
            rule_ids.append(rule.rule_id)
            if rule.rule_class == RuleClass.ALLOW:
                has_allow = True
            if rule.rule_class == RuleClass.DENY:
                has_deny = True

        if has_allow and has_deny:
            conflicts.append(
                PolicyConflictRecord(
                    involved_rule_ids=rule_ids,
                    description="Direct ALLOW vs DENY conflict",
                    severity=ConflictSeverity.CRITICAL,
                )
            )

        return conflicts
