from typing import Dict, List, Optional
from .models import TraceDefinition
from .exceptions import InvalidSchemaContractError

class TraceRegistry:
    def __init__(self):
        self._traces: Dict[str, TraceDefinition] = {}

    def register_trace(self, trace: TraceDefinition) -> None:
        if trace.parent_child_linkage is False:
            raise InvalidSchemaContractError("Traces must support parent-child linkage.")
        self._traces[trace.telemetry_id] = trace

    def get_trace(self, telemetry_id: str) -> Optional[TraceDefinition]:
        return self._traces.get(telemetry_id)

    def list_traces(self) -> List[TraceDefinition]:
        return list(self._traces.values())
