import uuid
from typing import List, Dict
from app.readiness_board.models import (
    ReadinessDossier,
    ReadinessDomainVerdict,
    EvidenceConflict,
)
from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.enums import ReadinessDomain


class DossierBuilder:
    def __init__(self, storage: ReadinessBoardStorage):
        self.storage = storage

    def build_dossier(
        self,
        candidate_id: str,
        snapshot_id: str,
        domain_verdicts: Dict[ReadinessDomain, ReadinessDomainVerdict],
        admissible_refs: List[str],
        inadmissible_refs: List[str],
        conflicts: List[EvidenceConflict],
    ) -> ReadinessDossier:
        dossier = ReadinessDossier(
            dossier_id=f"dos_{uuid.uuid4().hex[:8]}",
            candidate_id=candidate_id,
            snapshot_id=snapshot_id,
            domain_verdicts=domain_verdicts,
            admissible_evidence_refs=admissible_refs,
            inadmissible_evidence_refs=inadmissible_refs,
            conflicts=conflicts,
        )
        self.storage.save_dossier(dossier)
        return dossier
