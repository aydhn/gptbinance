from typing import Dict, List, Optional
from .models import TelemetryDefinition
from .exceptions import InvalidTelemetryDefinitionError

class CanonicalTelemetryRegistry:
    def __init__(self):
        self._definitions: Dict[str, TelemetryDefinition] = {}

    def register(self, definition: TelemetryDefinition) -> None:
        if definition.telemetry_id in self._definitions:
            raise InvalidTelemetryDefinitionError(f"Duplicate telemetry id: {definition.telemetry_id}")
        if not definition.telemetry_id or not definition.producer:
            raise InvalidTelemetryDefinitionError("Telemetry requires id and producer.")
        self._definitions[definition.telemetry_id] = definition

    def get(self, telemetry_id: str) -> Optional[TelemetryDefinition]:
        return self._definitions.get(telemetry_id)

    def list_all(self) -> List[TelemetryDefinition]:
        return list(self._definitions.values())

    def assert_registered(self, telemetry_id: str) -> None:
        if telemetry_id not in self._definitions:
            raise InvalidTelemetryDefinitionError(f"Undocumented telemetry id: {telemetry_id}")
