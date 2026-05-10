from app.release_plane.models import ReleaseCandidateRef
from typing import Dict, Any, List
import uuid

class ReleaseQualityReport:
    def __init__(self, report_id: str, candidate_id: str, issues: List[str], passed: bool):
        self.report_id = report_id
        self.candidate_ref = ReleaseCandidateRef(candidate_id=candidate_id)
        self.issues = issues
        self.passed = passed

class ReleaseQualityChecker:
    def check(self, candidate_id: str, context: Dict[str, Any]) -> ReleaseQualityReport:
        issues = []
        if context.get("missing_pins"):
            issues.append("Missing Pins")
        if context.get("incomplete_rollback_path"):
            issues.append("Incomplete rollback path")
        if context.get("stale_candidate"):
            issues.append("Stale candidate")
        if context.get("weak_canary_evidence"):
            issues.append("Weak canary evidence")
        if context.get("hidden_diff_suspicion"):
            issues.append("Hidden diff suspicion")
        if context.get("environment_mismatch"):
            issues.append("Environment mismatch")

        passed = len(issues) == 0
        return ReleaseQualityReport(
            report_id=f"qual-{uuid.uuid4().hex[:8]}",
            candidate_id=candidate_id,
            issues=issues,
            passed=passed
        )
