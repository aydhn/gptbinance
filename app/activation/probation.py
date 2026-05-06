from typing import Dict, Any
from app.activation.base import ProbationEvaluatorBase
from app.activation.models import ProbationStatus
from app.activation.enums import ProbationVerdict
from app.activation.metrics import MetricsAggregator


class ProbationEvaluator(ProbationEvaluatorBase):
    def evaluate(self, intent_id: str, metrics_data: Dict[str, Any]) -> ProbationStatus:
        metrics = MetricsAggregator.evaluate_metrics(metrics_data)

        breaches = [m for m in metrics if m.is_breached]
        blockers = [m.metric_name for m in breaches]

        if not breaches:
            verdict = ProbationVerdict.PASS
        elif any(
            m.metric_name in ["market_truth_health", "shadow_cleanliness"]
            for m in breaches
        ):
            verdict = ProbationVerdict.FAIL
        else:
            verdict = ProbationVerdict.CAUTION

        return ProbationStatus(
            intent_id=intent_id, verdict=verdict, metrics=metrics, blockers=blockers
        )


# Exported signals to incident command: Probation failures -> Incident Intake


# Exported signals to incident command: Probation failures -> Incident Intake
def export_probation_metrics_to_scorecard() -> Dict[str, Any]:
    return {"status": "healthy", "recent_breaches": []}
