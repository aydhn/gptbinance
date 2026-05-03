from app.stressrisk.models import StressRun


class TailRiskReporter:
    def generate_summary(self, run: StressRun) -> str:
        lines = [
            f"=== TAIL RISK SUMMARY (Run: {run.run_id}) ===",
            f"Profile: {run.profile}",
            f"Total Loss Est: {run.portfolio_snapshot.total_estimated_loss}",
            f"Budget Verdict: {run.budget_result.verdict.value}",
            f"Overlay Verdict: {run.overlay_decision.verdict.value}",
        ]
        return "\n".join(lines)
