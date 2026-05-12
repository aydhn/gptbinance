import json
from pathlib import Path
from typing import Any, Dict


class StorageAdapter:
    def __init__(self, storage_path: str):
        self._storage_path = Path(storage_path)
        self._storage_path.mkdir(parents=True, exist_ok=True)

    def save(self, key: str, data: Dict[str, Any]) -> None:
        file_path = self._storage_path / f"{key}.json"
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)

    def load(self, key: str) -> Dict[str, Any]:
        file_path = self._storage_path / f"{key}.json"
        if not file_path.exists():
            return {}
        with open(file_path, "r") as f:
            return json.load(f)
