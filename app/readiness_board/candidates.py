import uuid
from typing import Dict, Any, List, Optional
from app.readiness_board.models import CandidateRecord, CandidateScope
from app.readiness_board.enums import CandidateClass
from app.readiness_board.storage import ReadinessBoardStorage


class CandidateRegistry:
    def __init__(self, storage: ReadinessBoardStorage):
        self.storage = storage

    def register_candidate(
        self,
        candidate_class: CandidateClass,
        scope: CandidateScope,
        metadata: Optional[Dict[str, Any]] = None,
        lineage_refs: Optional[List[str]] = None,
    ) -> CandidateRecord:
        record = CandidateRecord(
            candidate_id=f"cand_{uuid.uuid4().hex[:8]}",
            candidate_class=candidate_class,
            scope=scope,
            metadata=metadata or {},
            lineage_refs=lineage_refs or [],
        )
        self.storage.save_candidate(record)
        return record

    def get_candidate(self, candidate_id: str) -> Optional[CandidateRecord]:
        return self.storage.get_candidate(candidate_id)
