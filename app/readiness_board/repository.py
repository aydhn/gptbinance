from typing import Optional
from app.readiness_board.models import GoNoGoDecision, ReadinessDossier
from app.readiness_board.storage import ReadinessBoardStorage


class ReadinessBoardRepository:
    def __init__(self, storage: ReadinessBoardStorage):
        self.storage = storage

    def get_latest_decision(self, candidate_id: str) -> Optional[GoNoGoDecision]:
        return self.storage.get_latest_decision(candidate_id)

    def get_dossier_by_candidate(self, candidate_id: str) -> Optional[ReadinessDossier]:
        dossiers = [
            d for d in self.storage.dossiers.values() if d.candidate_id == candidate_id
        ]
        if dossiers:
            return sorted(dossiers, key=lambda x: x.created_at, reverse=True)[0]
        return None
