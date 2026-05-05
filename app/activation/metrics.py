from typing import Dict, Any, List
from app.activation.models import ProbationMetric


class MetricsAggregator:
    @staticmethod
    def evaluate_metrics(raw_metrics: Dict[str, Any]) -> List[ProbationMetric]:
        evaluated = []

        # Example metric 1: Market Truth Health
        mt_health = raw_metrics.get("market_truth_health", 1.0)
        evaluated.append(
            ProbationMetric(
                metric_name="market_truth_health",
                value=mt_health,
                threshold=0.95,
                is_breached=mt_health < 0.95,
                description="Market data freshness and completeness",
            )
        )

        # Example metric 2: Shadow Cleanliness
        shadow_drift = raw_metrics.get("shadow_drift_events", 0)
        evaluated.append(
            ProbationMetric(
                metric_name="shadow_cleanliness",
                value=shadow_drift,
                threshold=5.0,  # max allowed drift events
                is_breached=shadow_drift > 5.0,
                description="Number of unresolved shadow drift events",
            )
        )

        # Example metric 3: Lifecycle Health
        orphans = raw_metrics.get("lifecycle_orphans", 0)
        evaluated.append(
            ProbationMetric(
                metric_name="lifecycle_health",
                value=orphans,
                threshold=1.0,
                is_breached=orphans >= 1.0,
                description="Unresolved orphan orders",
            )
        )

        return evaluated
