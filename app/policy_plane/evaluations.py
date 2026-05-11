from typing import List, Optional
from app.policy_plane.models import (
    PolicySubject,
    PolicyAction,
    PolicyResource,
    PolicyContext,
    PolicyEvaluationRecord,
    PolicyVerdict,
    PolicyRule,
)
from app.policy_plane.enums import RuleClass, VerdictClass
from app.policy_plane.registry import registry
from app.policy_plane.precedence import PrecedenceEvaluator
from app.policy_plane.conflicts import ConflictDetector


class PolicyEvaluationEngine:
    def __init__(self):
        self.precedence = PrecedenceEvaluator()
        self.conflicts = ConflictDetector()

    def evaluate(
        self,
        subject: PolicySubject,
        action: PolicyAction,
        resource: PolicyResource,
        context: PolicyContext,
    ) -> PolicyEvaluationRecord:

        applicable_rules = []
        evaluated_policies = []

        for policy in registry.list_policies():
            evaluated_policies.append(policy.policy_id)
            for rule in policy.rules:
                if (
                    subject.subject_class in rule.subject_classes
                    and action.action_class in rule.action_classes
                    and resource.resource_class in rule.resource_classes
                ):
                    applicable_rules.append(rule)

        conflicts = self.conflicts.detect(applicable_rules)
        # In a real system, we might block if there are critical conflicts

        precedence_record = self.precedence.resolve(applicable_rules)

        if not precedence_record:
            verdict = PolicyVerdict(
                verdict_class=VerdictClass.BLOCKED_PENDING_CONTEXT,
                reason="No applicable rules found (Default Deny)",
                proof_notes="Coverage gap detected",
            )
        else:
            winning_rule = next(
                r
                for r in applicable_rules
                if r.rule_id == precedence_record.winning_rule_id
            )
            if winning_rule.rule_class == RuleClass.DENY:
                verdict_class = VerdictClass.DENY
            elif winning_rule.rule_class == RuleClass.ALLOW:
                verdict_class = VerdictClass.ALLOW
            elif winning_rule.rule_class == RuleClass.REQUIRE_REVIEW:
                verdict_class = VerdictClass.ALLOW_WITH_REVIEW
            else:
                verdict_class = VerdictClass.DENY

            verdict = PolicyVerdict(
                verdict_class=verdict_class,
                reason=precedence_record.reason,
                proof_notes=f"Evaluated against rule {winning_rule.rule_id}",
            )

        return PolicyEvaluationRecord(
            subject=subject,
            action=action,
            resource=resource,
            context=context,
            verdict=verdict,
            evaluated_policies=evaluated_policies,
        )

class PolicyEvaluationMigrationRef:
    def destructive_migration_verdict(self):
        pass
