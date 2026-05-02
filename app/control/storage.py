import json
import os
from typing import Optional
from app.control.models import ApprovalRecord


class ControlStorage:
    def __init__(self, storage_dir: str = "data/control"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def save_record(self, record: ApprovalRecord) -> None:
        path = os.path.join(self.storage_dir, f"{record.request.id}.json")
        with open(path, "w") as f:
            f.write(record.model_dump_json(indent=2))

    def load_record(self, request_id: str) -> Optional[ApprovalRecord]:
        path = os.path.join(self.storage_dir, f"{request_id}.json")
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
                return ApprovalRecord(**data)
        return None


storage = ControlStorage()
