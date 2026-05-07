from typing import Dict, List
from app.config_plane.models import ConfigParameter
from app.config_plane.exceptions import InvalidParameterDefinition


class ParameterRegistry:
    def __init__(self):
        self._params: Dict[str, ConfigParameter] = {}

    def register(self, param: ConfigParameter):
        self._params[param.name] = param

    def get(self, name: str) -> ConfigParameter:
        if name not in self._params:
            raise InvalidParameterDefinition(f"Parameter {name} not registered")
        return self._params[name]

    def list_all(self) -> List[ConfigParameter]:
        return list(self._params.values())
