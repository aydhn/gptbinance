from typing import List
from app.readiness_board.models import GoNoGoDecision
from app.readiness_board.storage import ReadinessBoardStorage


class HistoryManager:
    def __init__(self, storage: ReadinessBoardStorage):
        self.storage = storage

    def get_candidate_history(self, candidate_id: str) -> List[GoNoGoDecision]:
        # Filter all decisions for this candidate via dossiers
        dossier_ids = [
            d.dossier_id
            for d in self.storage.dossiers.values()
            if d.candidate_id == candidate_id
        ]
        decisions = [
            d for d in self.storage.decisions.values() if d.dossier_id in dossier_ids
        ]
        return sorted(decisions, key=lambda x: x.decided_at, reverse=True)


# Incident integration: include board decision lineage in snapshots