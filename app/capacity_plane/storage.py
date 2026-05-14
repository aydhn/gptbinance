import json
from typing import Any, Dict

# Abstract storage representation
_storage_backend: Dict[str, Any] = {}


def store_capacity_artifact(key: str, data: Any) -> None:
    _storage_backend[key] = data


def get_capacity_artifact(key: str) -> Any:
    return _storage_backend.get(key)
