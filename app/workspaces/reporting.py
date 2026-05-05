from typing import List
from app.workspaces.models import (
    WorkspaceHealthSummary,
    WorkspaceCatalogEntry,
    ProfileBoundary,
    ContaminationFinding,
)
from app.workspaces.enums import WorkspaceReadiness, BoundarySeverity


class WorkspaceReporter:
    def generate_health_summary(
        self,
        catalog_entry: WorkspaceCatalogEntry,
        boundaries: List[ProfileBoundary],
        findings: List[ContaminationFinding],
    ) -> WorkspaceHealthSummary:
        blockers = sum(
            1
            for b in boundaries
            for c in b.checks
            if c.severity == BoundarySeverity.BLOCKER and not c.passed
        )

        readiness = WorkspaceReadiness.READY
        if blockers > 0 or len(findings) > 0:
            readiness = WorkspaceReadiness.DEGRADED

        return WorkspaceHealthSummary(
            workspace_id=catalog_entry.workspace.workspace_id,
            readiness=readiness,
            boundary_violations=blockers,
            contamination_suspicions=len(findings),
        )

    def format_boundary_report(self, boundary: ProfileBoundary) -> str:
        report = f"Boundary Report for Profile: {boundary.profile_ref.profile_id}\n"
        report += f"Last Verified: {boundary.last_verified}\n"
        report += "-" * 40 + "\n"
        for check in boundary.checks:
            status = "PASS" if check.passed else "FAIL"
            report += f"[{status}] ({check.severity.value.upper()}) {check.details}\n"
        return report
