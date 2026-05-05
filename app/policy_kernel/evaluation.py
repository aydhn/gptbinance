from typing import List
import uuid
from app.policy_kernel.models import (
    PolicyContext,
    PolicyEvidenceBundle,
    PolicyDecisionNode,
    PolicyDecisionGraph,
    PolicyDecision,
)
from app.policy_kernel.enums import PolicyVerdict
from app.policy_kernel.rules import list_rules
from app.policy_kernel.invariants import list_invariants
from app.policy_kernel.precedence import resolve_precedence
from app.policy_kernel.waivers import get_active_waiver


def evaluate_policy(
    action_type: str, context: PolicyContext, evidence: PolicyEvidenceBundle
) -> PolicyDecision:
    nodes: List[PolicyDecisionNode] = []

    # 1. Evaluate Invariants (Non-bypassable)
    for invariant in list_invariants():
        # simplified evaluation logic for demonstration
        is_violated = False
        if invariant.effective_scope and context.mode in invariant.effective_scope:
            # check evidence
            for req_ev in invariant.required_evidence:
                if not getattr(evidence, req_ev, None):
                    is_violated = True
                    break

        if is_violated:
            nodes.append(
                PolicyDecisionNode(
                    rule_id=invariant.rule_id,
                    verdict=invariant.severity,
                    evidence_used=invariant.required_evidence,
                    reasoning=f"Invariant violated: {invariant.rationale}",
                )
            )

    # 2. Evaluate Normal Rules
    for rule in list_rules():
        is_violated = False
        if rule.effective_scope and context.mode in rule.effective_scope:
            for req_ev in rule.required_evidence:
                if not getattr(evidence, req_ev, None):
                    is_violated = True
                    break

        if is_violated:
            # Check for waiver
            waiver = None
            if rule.is_waivable:
                waiver = get_active_waiver(rule.rule_id, context.mode)

            if waiver:
                nodes.append(
                    PolicyDecisionNode(
                        rule_id=rule.rule_id,
                        verdict=PolicyVerdict.ALLOW,
                        evidence_used=rule.required_evidence,
                        reasoning=f"Rule waived by {waiver.waiver_id}",
                        waiver_applied=waiver.waiver_id,
                    )
                )
            else:
                nodes.append(
                    PolicyDecisionNode(
                        rule_id=rule.rule_id,
                        verdict=rule.severity,
                        evidence_used=rule.required_evidence,
                        reasoning=f"Rule violated: {rule.rationale}",
                    )
                )

    # 3. Resolve Precedence
    final_verdict = resolve_precedence(nodes)

    # 4. Construct winning rules
    winning_rules = [
        n.rule_id for n in nodes if n.verdict == final_verdict and not n.is_overridden
    ]

    graph = PolicyDecisionGraph(nodes=nodes, root_verdict=final_verdict)

    return PolicyDecision(
        decision_id=str(uuid.uuid4()),
        action_type=action_type,
        context=context,
        evidence=evidence,
        graph=graph,
        final_verdict=final_verdict,
        winning_rules=winning_rules,
        reasoning=f"Precedence resolved to {final_verdict.name} based on {len(winning_rules)} winning rules.",
    )
