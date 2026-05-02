"""High-level repository for accessing paper run state."""

from typing import List, Optional
from .storage import PaperStorage
from .models import PaperArtifactManifest


class PaperRepository:
    def __init__(self, db_path: str = "paper_runtime.db"):
        self.storage = PaperStorage(db_path)

    def get_summary(self, run_id: str) -> Optional[PaperArtifactManifest]:
        return self.storage.get_manifest(run_id)

    def get_orders(self, run_id: str) -> List[dict]:
        return self.storage.get_orders(run_id)

    def get_fills(self, run_id: str) -> List[dict]:
        return self.storage.get_fills(run_id)

    def get_snapshots(self, run_id: str) -> List[dict]:
        return self.storage.get_snapshots(run_id)
