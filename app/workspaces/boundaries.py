import uuid
from typing import List, Dict, Any
from app.workspaces.models import WorkspaceProfile, ProfileBoundary, BoundaryCheckResult, WorkspaceProfileRef
from app.workspaces.enums import BoundarySeverity

class BoundaryChecker:
    def __init__(self):
        pass

    def verify_boundaries(self, profile: WorkspaceProfile) -> ProfileBoundary:
        checks = []

        # Example check: Verify paths are defined
        if not profile.scoped_paths:
            checks.append(BoundaryCheckResult(
                check_id=str(uuid.uuid4()),
                passed=False,
                severity=BoundarySeverity.BLOCKER,
                details="Profile scoped paths are not initialized.",
                evidence={"profile_id": profile.profile_id}
            ))
        else:
            checks.append(BoundaryCheckResult(
                check_id=str(uuid.uuid4()),
                passed=True,
                severity=BoundarySeverity.INFO,
                details="Profile scoped paths are initialized."
            ))

        # Example check: Live profiles shouldn't share paper directories
        if profile.live_affecting and profile.scoped_paths and "paper" in str(profile.scoped_paths.state_root):
            checks.append(BoundaryCheckResult(
                check_id=str(uuid.uuid4()),
                passed=False,
                severity=BoundarySeverity.BLOCKER,
                details="Live profile appears to be using a paper/test state directory.",
                evidence={"state_root": profile.scoped_paths.state_root}
            ))

        return ProfileBoundary(
            profile_ref=WorkspaceProfileRef(
                workspace_id=profile.workspace_id,
                profile_id=profile.profile_id,
                profile_type=profile.profile_type
            ),
            checks=checks
        )
