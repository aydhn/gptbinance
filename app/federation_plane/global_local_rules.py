from typing import Dict, List, Optional
from app.federation_plane.models import GlobalLocalRuleRecord
from app.federation_plane.exceptions import FederationPlaneError


class GlobalLocalRuleManager:
    def __init__(self):
        self._rules: Dict[str, GlobalLocalRuleRecord] = {}

    def register(self, record: GlobalLocalRuleRecord):
        if not record.rule_id:
            raise FederationPlaneError("No hidden rule shadowing allowed.")
        self._rules[record.rule_id] = record

    def get_rule(self, rule_id: str) -> Optional[GlobalLocalRuleRecord]:
        return self._rules.get(rule_id)

    def list_rules(self) -> List[GlobalLocalRuleRecord]:
        return list(self._rules.values())
