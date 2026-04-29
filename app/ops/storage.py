import json
from pathlib import Path
from typing import Optional, List, Dict, Any


class OpsStorage:
    def __init__(self, storage_dir: str = "data/ops"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def _get_file_path(self, run_id: str, doc_type: str) -> Path:
        return self.storage_dir / f"{run_id}_{doc_type}.json"

    def save_record(self, run_id: str, doc_type: str, data: Dict[str, Any]) -> None:
        path = self._get_file_path(run_id, doc_type)
        with path.open("w") as f:
            json.dump(data, f, indent=2, default=str)

    def append_record(self, run_id: str, doc_type: str, data: Dict[str, Any]) -> None:
        path = self._get_file_path(run_id, doc_type)
        records = self.load_records(run_id, doc_type) or []
        records.append(data)
        with path.open("w") as f:
            json.dump(records, f, indent=2, default=str)

    def load_record(self, run_id: str, doc_type: str) -> Optional[Dict[str, Any]]:
        path = self._get_file_path(run_id, doc_type)
        if not path.exists():
            return None
        with path.open("r") as f:
            return json.load(f)

    def load_records(
        self, run_id: str, doc_type: str
    ) -> Optional[List[Dict[str, Any]]]:
        path = self._get_file_path(run_id, doc_type)
        if not path.exists():
            return None
        with path.open("r") as f:
            return json.load(f)
