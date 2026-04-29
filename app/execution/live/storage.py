import json
import logging
from typing import Dict, Any
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)


class ExecutionStorage:
    def __init__(self, base_path: str = "data/execution"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def _get_run_dir(self, run_id: str) -> Path:
        run_dir = self.base_path / run_id
        run_dir.mkdir(parents=True, exist_ok=True)
        return run_dir

    def save_audit_record(self, run_id: str, record: Dict[str, Any]):
        run_dir = self._get_run_dir(run_id)
        audit_file = run_dir / "audit.jsonl"
        with open(audit_file, "a") as f:
            # Custom encoder for datetime/Decimal needed in production
            f.write(json.dumps(record, default=str) + "\n")

    def save_snapshot(self, run_id: str, name: str, data: Dict[str, Any]):
        run_dir = self._get_run_dir(run_id)
        snapshot_file = run_dir / f"{name}_{datetime.utcnow().timestamp()}.json"
        with open(snapshot_file, "w") as f:
            f.write(json.dumps(data, default=str))
