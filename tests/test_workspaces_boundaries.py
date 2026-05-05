from app.workspaces.boundaries import BoundaryChecker
from app.workspaces.models import WorkspaceProfile, ScopedPathSet
from app.workspaces.enums import ProfileType, BoundarySeverity


def test_verify_boundaries_missing_paths():
    checker = BoundaryChecker()
    p = WorkspaceProfile(
        profile_id="p_1",
        workspace_id="ws_1",
        name="P",
        profile_type=ProfileType.PAPER_DEFAULT,
    )

    boundary = checker.verify_boundaries(p)
    assert len(boundary.checks) == 1
    assert not boundary.checks[0].passed
    assert boundary.checks[0].severity == BoundarySeverity.BLOCKER


def test_verify_boundaries_live_paper_mix():
    checker = BoundaryChecker()
    paths = ScopedPathSet(
        config_root="/c",
        state_root="/paper/state",
        artifact_root="/a",
        log_root="/l",
        evidence_root="/e",
        backup_root="/b",
        metrics_root="/m",
        replays_root="/r",
        analytics_root="/an",
    )
    p = WorkspaceProfile(
        profile_id="p_1",
        workspace_id="ws_1",
        name="P",
        profile_type=ProfileType.CANARY_LIVE_CAUTION,
        live_affecting=True,
        scoped_paths=paths,
    )

    boundary = checker.verify_boundaries(p)
    assert any(
        c.severity == BoundarySeverity.BLOCKER and not c.passed for c in boundary.checks
    )
