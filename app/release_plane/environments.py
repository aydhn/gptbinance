from typing import Dict, List, Optional
from app.release_plane.models import EnvironmentTarget
from app.release_plane.enums import EnvironmentClass
from app.release_plane.exceptions import ReleasePlaneError

class EnvironmentRegistry:
    def __init__(self):
        self._environments: Dict[str, EnvironmentTarget] = {}

    def register(self, target: EnvironmentTarget) -> None:
        key = target.environment_class.value
        if key in self._environments:
            raise ReleasePlaneError(f"Environment {key} already registered. Hidden env aliases are prohibited.")
        self._environments[key] = target

    def get(self, env_class: EnvironmentClass) -> Optional[EnvironmentTarget]:
        return self._environments.get(env_class.value)

    def get_all(self) -> List[EnvironmentTarget]:
        return list(self._environments.values())

env_registry = EnvironmentRegistry()

# Register core environments
env_registry.register(EnvironmentTarget(environment_class=EnvironmentClass.REPLAY, isolation_rules={"read_only": True}, metadata={}))
env_registry.register(EnvironmentTarget(environment_class=EnvironmentClass.PAPER, isolation_rules={"no_live_execution": True}, metadata={}))
env_registry.register(EnvironmentTarget(environment_class=EnvironmentClass.PROBATION, isolation_rules={"strict_caps": True}, metadata={}))
env_registry.register(EnvironmentTarget(environment_class=EnvironmentClass.LIVE_CANARY, isolation_rules={"canary_scope_only": True}, metadata={}))
env_registry.register(EnvironmentTarget(environment_class=EnvironmentClass.LIVE_FULL, isolation_rules={"none": True}, metadata={}))
env_registry.register(EnvironmentTarget(environment_class=EnvironmentClass.TEST, isolation_rules={"mocked_interfaces": True}, metadata={}))
