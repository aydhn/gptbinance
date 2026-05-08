import json
from typing import Dict, Any


class ExecutionStorage:
    def __init__(self):
        self.data: Dict[str, Dict[str, Any]] = {
            "manifests": {},
            "attempts": {},
            "idempotency": {},
            "quality_reports": {},
        }

    def save_manifest(self, manifest):
        self.data["manifests"][manifest.manifest_id] = manifest.model_dump()

    def get_manifest(self, manifest_id: str):
        return self.data["manifests"].get(manifest_id)
