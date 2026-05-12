from typing import List
from .registry import CanonicalTelemetryRegistry

class ObservabilityReporter:
    def __init__(self, registry: CanonicalTelemetryRegistry):
        self.registry = registry

    def generate_registry_summary(self) -> str:
        telemetry = self.registry.list_all()
        summary = "=== OBSERVABILITY REGISTRY SUMMARY ===\n"
        for t in telemetry:
            summary += f"- {t.telemetry_id} [{t.telemetry_class.value}] Producer: {t.producer}\n"
        return summary
