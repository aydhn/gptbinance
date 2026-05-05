from app.shadow_state.models import ConvergenceRun, TruthfulnessReport
from app.shadow_state.enums import ConvergenceVerdict, TruthfulnessClass
import uuid


class Reporter:
    def generate_truthfulness_report(self, run: ConvergenceRun) -> TruthfulnessReport:
        overall = TruthfulnessClass.HIGH_CONFIDENCE
        if run.global_verdict == ConvergenceVerdict.CRITICAL_DIVERGENCE:
            overall = TruthfulnessClass.UNTRUSTWORTHY
        elif run.global_verdict == ConvergenceVerdict.SUSPICIOUS_DIVERGENCE:
            overall = TruthfulnessClass.DEGRADED

        blockers = []
        if overall == TruthfulnessClass.UNTRUSTWORTHY:
            blockers.append(
                "Critical divergence detected; shadow cleanliness violated."
            )

        return TruthfulnessReport(
            report_id=f"rep_{uuid.uuid4().hex[:8]}",
            run_ref=run.run_id,
            overall_class=overall,
            blockers=blockers,
            warnings=["Please review the remediation plan."],
            next_actions=["Run remediation planner", "Request review approval"],
        )
