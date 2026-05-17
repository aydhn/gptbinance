from typing import Dict, Optional, List
from .models import StateObject, LifecycleDefinition

class StateRegistry:
    def __init__(self):
        self._objects: Dict[str, StateObject] = {}
        self._lifecycles: Dict[str, LifecycleDefinition] = {}

    def register_lifecycle(self, definition: LifecycleDefinition) -> None:
        self._lifecycles[definition.lifecycle_id] = definition

    def register_object(self, obj: StateObject) -> None:
        self._objects[obj.state_id] = obj

    def get_object(self, state_id: str) -> Optional[StateObject]:
        return self._objects.get(state_id)

    def get_all_objects(self) -> List[StateObject]:
        return list(self._objects.values())

    def get_lifecycle(self, lifecycle_id: str) -> Optional[LifecycleDefinition]:
        return self._lifecycles.get(lifecycle_id)

state_registry = StateRegistry()
