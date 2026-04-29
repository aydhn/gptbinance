from app.risk.models import RiskDecision


class RiskExplainer:
    def explain(self, decision: RiskDecision) -> str:
        lines = [f"Verdict: {decision.verdict.name}"]
        lines.append(f"Rationale: {decision.rationale}")

        if decision.sizing:
            lines.append(f"Requested Size: {decision.sizing.requested_size}")
            lines.append(f"Approved Size: {decision.sizing.approved_size}")
            for k, v in decision.sizing.scaling_factors_applied.items():
                lines.append(f"  - {k} adjustment: {v}")

        if decision.rejection_reasons:
            lines.append("Rejections/Warnings:")
            for r in decision.rejection_reasons:
                lines.append(f"  - [{r.severity.name}] {r.source}: {r.rationale}")

        return "\n".join(lines)
