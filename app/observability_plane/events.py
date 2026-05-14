from enum import Enum
from typing import Dict, List, Optional
from .models import EventDefinition
from .exceptions import InvalidTelemetryDefinitionError

class EventRegistry:
    def __init__(self):
        self._events: Dict[str, EventDefinition] = {}

    def register_event(self, event: EventDefinition) -> None:
        if not event.provenance:
            raise InvalidTelemetryDefinitionError("Events must declare provenance.")
        self._events[event.telemetry_id] = event

    def get_event(self, telemetry_id: str) -> Optional[EventDefinition]:
        return self._events.get(telemetry_id)

    def list_events(self) -> List[EventDefinition]:
        return list(self._events.values())

class ObservabilityEventType(str, Enum):
    DECISION_CREATED = 'decision_created'
    OPTION_COMPARED = 'option_compared'
    OUTCOME_REVIEWED = 'outcome_reviewed'