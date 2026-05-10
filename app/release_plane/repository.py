from typing import Any, List, Optional
from app.release_plane.storage import ReleasePlaneStorage

class ReleasePlaneRepository:
    def __init__(self, storage: ReleasePlaneStorage):
        self.storage = storage

    def save_release(self, release: Any):
        self.storage.save("releases", release.release_id, release)

    def get_release(self, release_id: str) -> Optional[Any]:
        return self.storage.load("releases", release_id)

    def save_candidate(self, candidate: Any):
        self.storage.save("candidates", candidate.candidate_id, candidate)

    def get_latest_trusted_release(self) -> Optional[Any]:
        # Implementation to fetch latest from storage based on trust verdict
        # Simplified for now
        releases = list(self.storage.releases.values())
        if releases:
             return releases[-1]
        return None
