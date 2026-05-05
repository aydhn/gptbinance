import uuid
from typing import Dict, Any
from app.readiness_board.models import EvidenceSubmission
from app.readiness_board.enums import EvidenceClass
from app.readiness_board.storage import ReadinessBoardStorage


class EvidenceIntake:
    def __init__(self, storage: ReadinessBoardStorage):
        self.storage = storage

    def submit_evidence(
        self,
        candidate_id: str,
        evidence_class: EvidenceClass,
        content: Dict[str, Any],
        source_ref: str,
    ) -> EvidenceSubmission:
        submission = EvidenceSubmission(
            submission_id=f"evid_{uuid.uuid4().hex[:8]}",
            candidate_id=candidate_id,
            evidence_class=evidence_class,
            content=content,
            source_ref=source_ref,
        )
        self.storage.save_evidence(submission)
        return submission
