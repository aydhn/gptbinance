from typing import Dict, List, Optional
from datetime import datetime, timezone
from app.observability.models import (
    SliDefinition,
    SliSnapshot,
    SloDefinition,
    SloEvaluation,
)
from app.observability.enums import SloStatus


class SloEngine:
    def __init__(self):
        self._slis: Dict[str, SliDefinition] = {}
        self._slos: Dict[str, SloDefinition] = {}
        self._snapshots: List[SliSnapshot] = []
        self._evaluations: List[SloEvaluation] = []

    def register_sli(self, sli: SliDefinition) -> None:
        self._slis[sli.sli_id] = sli

    def register_slo(self, slo: SloDefinition) -> None:
        self._slos[slo.slo_id] = slo

    def record_sli_snapshot(
        self, sli_id: str, current_value: float, period_seconds: int
    ) -> None:
        snapshot = SliSnapshot(
            sli_id=sli_id,
            current_value=current_value,
            period_seconds=period_seconds,
            timestamp=datetime.now(timezone.utc),
        )
        self._snapshots.append(snapshot)
        self._evaluate_related_slos(sli_id, current_value)

    def _evaluate_related_slos(self, sli_id: str, current_sli_value: float) -> None:
        for slo in self._slos.values():
            if slo.sli_id == sli_id:
                status = SloStatus.HEALTHY
                explanation = "SLO is healthy."

                # Check if lower is better (e.g. lag) or higher is better (e.g. success rate)
                if slo.breach_threshold > slo.warning_threshold:
                    # Lower is better (e.g. lag)
                    if current_sli_value > slo.breach_threshold:
                        status = SloStatus.BREACH
                        explanation = f"SLI value {current_sli_value} above breach threshold {slo.breach_threshold}"
                    elif current_sli_value > slo.warning_threshold:
                        status = SloStatus.CAUTION
                        explanation = f"SLI value {current_sli_value} above warning threshold {slo.warning_threshold}"
                else:
                    # Higher is better (e.g. success rate)
                    if current_sli_value < slo.breach_threshold:
                        status = SloStatus.BREACH
                        explanation = f"SLI value {current_sli_value} below breach threshold {slo.breach_threshold}"
                    elif current_sli_value < slo.warning_threshold:
                        status = SloStatus.CAUTION
                        explanation = f"SLI value {current_sli_value} below warning threshold {slo.warning_threshold}"

                evaluation = SloEvaluation(
                    slo_id=slo.slo_id,
                    status=status,
                    current_sli_value=current_sli_value,
                    explanation=explanation,
                    timestamp=datetime.now(timezone.utc),
                )
                self._evaluations.append(evaluation)

    def get_latest_evaluations(self) -> List[SloEvaluation]:
        # Return most recent evaluation per SLO
        latest: Dict[str, SloEvaluation] = {}
        for ev in self._evaluations:
            if ev.slo_id not in latest or ev.timestamp > latest[ev.slo_id].timestamp:
                latest[ev.slo_id] = ev
        return list(latest.values())


engine = SloEngine()
