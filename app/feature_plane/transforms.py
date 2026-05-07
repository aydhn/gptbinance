from typing import Dict, Any


class TransformRegistry:
    def __init__(self):
        self._transforms: Dict[str, Any] = {}

    def register_transform(self, name: str, func: Any):
        self._transforms[name] = func
