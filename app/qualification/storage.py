import json
import os
from typing import Dict
from app.qualification.models import QualificationRun

# Simple JSON-based file storage for mock implementation
STORAGE_DIR = "data/qualification"
os.makedirs(STORAGE_DIR, exist_ok=True)


class QualificationStorage:
    def save_run(self, run: QualificationRun):
        path = os.path.join(STORAGE_DIR, f"{run.run_id}.json")
        with open(path, "w") as f:
            f.write(run.model_dump_json(indent=2))

    def get_run(self, run_id: str) -> QualificationRun:
        path = os.path.join(STORAGE_DIR, f"{run_id}.json")
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            data = json.load(f)
            return QualificationRun.model_validate(data)
