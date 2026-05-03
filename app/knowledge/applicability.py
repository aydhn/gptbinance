from typing import Dict, Any, List
from app.knowledge.models import KnowledgeItem, ApplicabilityRule
from app.knowledge.enums import ApplicabilityVerdict, DocumentStatus


class RunbookApplicabilityEngine:
    def evaluate(
        self, item: KnowledgeItem, context: Dict[str, Any]
    ) -> ApplicabilityVerdict:
        if item.status in (DocumentStatus.ARCHIVED, DocumentStatus.DEPRECATED):
            return ApplicabilityVerdict.BLOCKED

        if not item.applicability_rules:
            # If no rules, it's broadly applicable, but we might flag caution for critical actions if config says so.
            # Assuming broadly applicable for now.
            return ApplicabilityVerdict.APPLICABLE

        target_profile = context.get("profile")
        target_release = context.get("release")
        target_component = context.get("component")
        target_action = context.get("action")
        target_alert = context.get("alert")

        # Basic applicability logic: if rules exist, context must match AT LEAST ONE rule for it to be fully applicable.
        # Otherwise, CAUTION or BLOCKED. We'll say if there are rules and none match, CAUTION, unless strict mode.
        matches = False
        for rule in item.applicability_rules:
            if (
                target_profile
                and rule.target_profiles
                and target_profile in rule.target_profiles
            ):
                matches = True
            if (
                target_release
                and rule.target_releases
                and target_release in rule.target_releases
            ):
                matches = True
            if (
                target_component
                and rule.target_components
                and target_component in rule.target_components
            ):
                matches = True
            if (
                target_action
                and rule.target_actions
                and target_action in rule.target_actions
            ):
                matches = True
            if (
                target_alert
                and rule.target_alerts
                and target_alert in rule.target_alerts
            ):
                matches = True

        if matches:
            return ApplicabilityVerdict.APPLICABLE
        else:
            return ApplicabilityVerdict.CAUTION


applicability_engine = RunbookApplicabilityEngine()
