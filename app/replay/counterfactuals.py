import logging
from typing import List

from app.replay.models import (
    CounterfactualSpec,
    CounterfactualResult,
    ReplayConfig,
    EventTimeline,
    PointInTimeSnapshot,
    ReplayDiff,
)
from app.replay.enums import DiffSeverity

logger = logging.getLogger(__name__)


class DummyCounterfactualEngine:
    def run_counterfactuals(
        self,
        specs: List[CounterfactualSpec],
        config: ReplayConfig,
        timeline: EventTimeline,
        snapshot: PointInTimeSnapshot,
    ) -> List[CounterfactualResult]:
        logger.info(f"Running {len(specs)} counterfactuals")
        results = []
        for spec in specs:
            results.append(
                CounterfactualResult(
                    spec=spec,
                    historical_outcome={"status": "executed"},
                    counterfactual_outcome={"status": "blocked"},
                    diffs=[
                        ReplayDiff(
                            stage="execution",
                            original_value="executed",
                            replayed_value="blocked",
                            severity=DiffSeverity.CRITICAL,
                            description="Counterfactual blocked execution",
                        )
                    ],
                    explanation="Counterfactual simulation results",
                )
            )
        return results
