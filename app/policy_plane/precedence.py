from typing import List, Dict
from app.policy_plane.models import PolicyRule, PolicyPrecedenceRecord
from app.policy_plane.enums import RuleClass


class PrecedenceEvaluator:
    def resolve(self, rules: List[PolicyRule]) -> PolicyPrecedenceRecord:
        if not rules:
            return None

        winning_rule = None
        losing_rules = []
        reason = ""

        # Deny overrides everything
        deny_rules = [r for r in rules if r.rule_class == RuleClass.DENY]
        if deny_rules:
            winning_rule = deny_rules[0]
            losing_rules = [r for r in rules if r != winning_rule]
            reason = "DENY_OVERRIDES"
        else:
            # Simple precedence for now: first rule wins if not deny
            winning_rule = rules[0]
            losing_rules = rules[1:]
            reason = "FIRST_MATCH"

        return PolicyPrecedenceRecord(
            winning_rule_id=winning_rule.rule_id,
            losing_rule_ids=[r.rule_id for r in losing_rules],
            reason=reason,
        )
