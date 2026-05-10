from typing import List
from app.policy_plane.models import PolicyDefinition
from app.policy_plane.enums import ActionClass


class CoverageAnalyzer:
    def get_uncovered_actions(
        self, policies: List[PolicyDefinition]
    ) -> List[ActionClass]:
        covered = set()
        for policy in policies:
            for rule in policy.rules:
                covered.update(rule.action_classes)

        all_actions = set(ActionClass)
        return list(all_actions - covered)
