from app.portfolio.models import PortfolioDecision, PortfolioDecisionBatch


class ExplainabilityEngine:
    def explain_decision(self, decision: PortfolioDecision) -> str:
        lines = [f"Intent: {decision.intent_id}"]
        lines.append(f"Verdict: {decision.verdict.value.upper()}")

        if decision.blocking_reasons:
            lines.append("Blocking Reasons:")
            for reason in decision.blocking_reasons:
                lines.append(f"  - {reason}")

        if decision.rationale:
            lines.append(f"Ranking Rationale: {decision.rationale}")

        if decision.allocation:
            lines.append(f"Allocation:")
            lines.append(f"  Requested: {decision.allocation.requested_notional:.2f}")
            lines.append(f"  Approved:  {decision.allocation.approved_notional:.2f}")
            lines.append(f"  Reduction: {decision.allocation.reduction_ratio:.2%}")

        return "\n".join(lines)

    def explain_batch(self, batch: PortfolioDecisionBatch) -> str:
        out = [f"--- Portfolio Decision Batch: {batch.run_id} ---"]
        for d in batch.decisions:
            out.append(self.explain_decision(d))
            out.append("-" * 20)
        return "\n".join(out)
