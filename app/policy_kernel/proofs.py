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

import uuid
from typing import Dict, Any
from app.incidents.enums import SignalType, IncidentSeverity, IncidentScopeType
from app.incidents.signals import SignalMapper
from app.incidents.intake import IncidentCommand

def emit_policy_hard_block_signal(profile_id: str, details: Dict[str, Any] = None):
    cmd = IncidentCommand()
    signal = SignalMapper.create_signal(
        signal_id=f"pol-{uuid.uuid4().hex[:8]}",
        signal_type=SignalType.POLICY_HARD_BLOCK,
        domain="policy",
        scope_type=IncidentScopeType.PROFILE,
        scope_ref=profile_id,
        severity=IncidentSeverity.MAJOR_INCIDENT,
        details=details or {"reason": "Policy blocked"}
    )
    cmd.ingest_signal(signal)
