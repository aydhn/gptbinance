from typing import Any
from app.postmortems.models import TriggerEvent
from typing import List


class TriggerDetector:
    def detect(self, chronology: Any, causal_graph: Any) -> List[TriggerEvent]:
        triggers = []
        if chronology and hasattr(chronology, "events") and chronology.events:
            triggers.append(
                TriggerEvent(
                    event_id="trig_first", description=chronology.events[0].description
                )
            )
        return triggers
