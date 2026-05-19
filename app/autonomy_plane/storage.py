import json
from dataclasses import asdict
from typing import Any

class AutonomyStorage:
    def _to_dict(self, obj: Any) -> dict:
        return asdict(obj)

    def write(self, path: str, obj: Any) -> None:
        data = self._to_dict(obj)
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)

storage = AutonomyStorage()
