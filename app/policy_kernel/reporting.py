from app.policy_kernel.rules import list_rules
from app.policy_kernel.invariants import list_invariants
from app.policy_kernel.waivers import list_active_waivers
from app.policy_kernel.drift import list_drifts
from app.policy_kernel.gaps import list_gaps


def generate_policy_audit_summary() -> str:
    rules = list_rules()
    invariants = list_invariants()
    waivers = list_active_waivers()
    drifts = list_drifts()
    gaps = list_gaps()

    lines = [
        "=== POLICY CONSTITUTION AUDIT SUMMARY ===",
        f"Total Active Rules: {len(rules)}",
        f"Total Non-bypassable Invariants: {len(invariants)}",
        f"Active Waivers: {len(waivers)}",
        f"Detected Policy Drifts: {len(drifts)}",
        f"Identified Policy Gaps: {len(gaps)}",
        "",
        "--- CRITICAL DRIFTS ---",
    ]

    critical_drifts = [d for d in drifts if d.severity.name == "CRITICAL"]
    if critical_drifts:
        for d in critical_drifts:
            lines.append(
                f"- [{d.module_name}] {d.action_type}: Declared {d.declared_verdict.name}, Actual {d.actual_verdict.name}"
            )
    else:
        lines.append("None detected.")

    lines.extend(["", "--- CRITICAL GAPS ---"])
    critical_gaps = [g for g in gaps if g.severity.name == "CRITICAL"]
    if critical_gaps:
        for g in critical_gaps:
            lines.append(f"- [{g.domain.name}] {g.description}")
    else:
        lines.append("None detected.")

    return "\n".join(lines)
