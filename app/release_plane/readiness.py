from app.release_plane.models import ReleaseCandidateRef
from typing import List, Dict, Any
import uuid

class ReleaseReadinessReport:
    def __init__(self, report_id: str, candidate_ref: ReleaseCandidateRef, missing_blockers: List[str], sufficient: bool):
        self.report_id = report_id
        self.candidate_ref = candidate_ref
        self.missing_blockers = missing_blockers
        self.sufficient = sufficient
        self.proof_notes = "Readiness evaluated based on domain checks."

class ReleaseReadinessAggregator:
    def evaluate(self, candidate_id: str, domain_results: Dict[str, Any]) -> ReleaseReadinessReport:
        blockers = []
        if "reviews" not in domain_results or not domain_results["reviews"].get("passed"):
             blockers.append("Missing review blockers.")

        if "bundle_complete" not in domain_results or not domain_results["bundle_complete"]:
             blockers.append("Incomplete bundle blockers.")

        sufficient = len(blockers) == 0
        return ReleaseReadinessReport(
            report_id=f"rr-{uuid.uuid4().hex[:8]}",
            candidate_ref=ReleaseCandidateRef(candidate_id=candidate_id),
            missing_blockers=blockers,
            sufficient=sufficient
        )
