from typing import List, Dict
from app.constitution_plane.models import ConstitutionalRuleRecord

class ConstitutionalRulesManager:
    def __init__(self):
        self._rules: Dict[str, ConstitutionalRuleRecord] = {}

    def add_rule(self, rule: ConstitutionalRuleRecord):
        self._rules[rule.rule_id] = rule

    def get_non_negotiable_rules(self) -> List[ConstitutionalRuleRecord]:
        return [r for r in self._rules.values() if r.is_non_negotiable]
