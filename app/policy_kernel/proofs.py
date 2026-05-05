from app.policy_kernel.models import PolicyDecision


def generate_decision_proof(decision: PolicyDecision) -> str:
    lines = [
        "--- POLICY DECISION PROOF ---",
        f"Decision ID: {decision.decision_id}",
        f"Timestamp: {decision.timestamp.isoformat()}",
        f"Action: {decision.action_type}",
        f"Final Verdict: {decision.final_verdict.name}",
        f"Reasoning: {decision.reasoning}",
        "",
        "--- EVALUATED RULES ---",
    ]

    for node in decision.graph.nodes:
        status = "OVERRIDDEN" if node.is_overridden else "ACTIVE"
        waiver_info = (
            f" (Waived by: {node.waiver_applied})" if node.waiver_applied else ""
        )
        lines.append(f"- Rule ID: {node.rule_id} [{status}]")
        lines.append(f"  Verdict: {node.verdict.name}{waiver_info}")
        lines.append(f"  Reason: {node.reasoning}")
        lines.append(f"  Evidence Used: {', '.join(node.evidence_used)}")

    lines.extend(
        [
            "",
            "--- WINNING RULES ---",
            (
                ", ".join(decision.winning_rules)
                if decision.winning_rules
                else "None (Default ALLOW)"
            ),
        ]
    )

    return "\n".join(lines)
