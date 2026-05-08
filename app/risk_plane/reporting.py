from typing import List
from .models import RiskState, RiskBreachRecord, RiskResponseIntent, RiskTrustVerdict


def format_risk_summary(
    states: List[RiskState],
    breaches: List[RiskBreachRecord],
    intents: List[RiskResponseIntent],
    trust: RiskTrustVerdict,
) -> str:
    lines = []
    lines.append("=== RISK PLANE SUMMARY ===")
    lines.append(f"Trust Verdict: {trust.verdict.value}")
    lines.append(f"Active States: {len(states)}")
    lines.append(f"Active Breaches: {len(breaches)}")
    lines.append(f"Active Intents: {len(intents)}")

    if breaches:
        lines.append("--- BREACH DETAILS ---")
        for b in breaches:
            lines.append(
                f"[{b.breach_class.value}] Limit {b.limit_ref.limit_id} breached. Value: {b.breached_value:.2f}"
            )

    if intents:
        lines.append("--- RESPONSE INTENTS ---")
        for r in intents:
            lines.append(
                f"[{r.response_class.value}] -> {r.target_domain.value}:{r.target_id}"
            )

    lines.append("==========================")
    return "\n".join(lines)
