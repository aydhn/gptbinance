from typing import Dict, List, Optional
from datetime import datetime, timezone
from app.observability.models import (
    HealthSignal,
    ComponentHealthSnapshot,
    SystemHealthSnapshot,
)
from app.observability.enums import ComponentType, HealthSeverity
from app.observability.exceptions import HealthAggregationError


class HealthAggregator:
    def __init__(self):
        self._signals: List[HealthSignal] = []

    def record_signal(
        self,
        component: ComponentType,
        severity: HealthSeverity,
        reason: str,
        metrics_refs: Optional[List[str]] = None,
    ) -> None:
        signal = HealthSignal(
            component=component,
            severity=severity,
            reason=reason,
            timestamp=datetime.now(timezone.utc),
            metrics_refs=metrics_refs or [],
        )
        self._signals.append(signal)

    def evaluate_component(self, component: ComponentType) -> ComponentHealthSnapshot:
        comp_signals = [s for s in self._signals if s.component == component]

        severity = HealthSeverity.HEALTHY
        explanation = "Component is healthy."

        if not comp_signals:
            return ComponentHealthSnapshot(
                component=component,
                severity=severity,
                last_updated=datetime.now(timezone.utc),
                signals=[],
                explanation=explanation,
            )

        # Evaluate severity based on highest signal severity
        severity_map = {
            HealthSeverity.HEALTHY: 0,
            HealthSeverity.DEGRADED: 1,
            HealthSeverity.CRITICAL: 2,
            HealthSeverity.HALTED: 3,
        }

        max_sev = max(comp_signals, key=lambda s: severity_map[s.severity])
        severity = max_sev.severity
        explanation = f"Evaluated to {severity.value}. Reason: {max_sev.reason}"

        return ComponentHealthSnapshot(
            component=component,
            severity=severity,
            last_updated=datetime.now(timezone.utc),
            signals=comp_signals[-10:],  # Keep recent
            explanation=explanation,
        )

    def evaluate_system(self) -> SystemHealthSnapshot:
        components_health: Dict[ComponentType, ComponentHealthSnapshot] = {}
        sys_severity = HealthSeverity.HEALTHY

        severity_map = {
            HealthSeverity.HEALTHY: 0,
            HealthSeverity.DEGRADED: 1,
            HealthSeverity.CRITICAL: 2,
            HealthSeverity.HALTED: 3,
        }

        for comp in ComponentType:
            comp_health = self.evaluate_component(comp)
            components_health[comp] = comp_health
            if severity_map[comp_health.severity] > severity_map[sys_severity]:
                sys_severity = comp_health.severity

        summary = f"System health is {sys_severity.value}"

        return SystemHealthSnapshot(
            severity=sys_severity,
            timestamp=datetime.now(timezone.utc),
            components=components_health,
            summary=summary,
        )

    def clear_signals(self) -> None:
        self._signals.clear()


aggregator = HealthAggregator()
