from app.workspaces.isolation import ContaminationChecker
from app.workspaces.models import WorkspaceProfile, ScopedPathSet
from app.workspaces.enums import ProfileType

def test_contamination_checker_shared_roots():
    checker = ContaminationChecker()
    paths = ScopedPathSet(
        config_root="/c", state_root="/shared/state", artifact_root="/a",
        log_root="/l", evidence_root="/e", backup_root="/b", metrics_root="/m", replays_root="/r", analytics_root="/an"
    )

    p1 = WorkspaceProfile(profile_id="p_1", workspace_id="ws_1", name="P1", profile_type=ProfileType.PAPER_DEFAULT, scoped_paths=paths)
    p2 = WorkspaceProfile(profile_id="p_2", workspace_id="ws_1", name="P2", profile_type=ProfileType.TESTNET_EXEC, scoped_paths=paths)

    findings = checker.check_for_contamination("ws_1", [p1, p2])
    assert len(findings) == 1
    assert findings[0].evidence["shared_state_root"] == "/shared/state"
