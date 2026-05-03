import uuid
from typing import List
from app.workspaces.models import ContaminationFinding, WorkspaceProfileRef, WorkspaceProfile
from app.workspaces.enums import ContaminationSeverity

class ContaminationChecker:
    def __init__(self):
        pass

    def check_for_contamination(self, workspace_id: str, profiles: List[WorkspaceProfile]) -> List[ContaminationFinding]:
        findings = []

        # Simple simulated check: Look for overlapping state roots among profiles in the workspace
        state_roots = {}
        for p in profiles:
            if p.scoped_paths:
                sr = p.scoped_paths.state_root
                if sr in state_roots:
                    # Overlap found!
                    findings.append(ContaminationFinding(
                        finding_id=str(uuid.uuid4()),
                        severity=ContaminationSeverity.CRITICAL if (p.live_affecting or state_roots[sr].live_affecting) else ContaminationSeverity.HIGH,
                        impacted_profiles=[
                            WorkspaceProfileRef(workspace_id=p.workspace_id, profile_id=p.profile_id, profile_type=p.profile_type),
                            WorkspaceProfileRef(workspace_id=state_roots[sr].workspace_id, profile_id=state_roots[sr].profile_id, profile_type=state_roots[sr].profile_type)
                        ],
                        evidence={"shared_state_root": sr},
                        recommended_actions=["Re-initialize scoped paths for impacted profiles", "Verify state integrity"]
                    ))
                else:
                    state_roots[sr] = p

        return findings
