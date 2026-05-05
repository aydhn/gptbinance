import pytest
from app.workspaces.context import ContextManager
from app.workspaces.models import WorkspaceConfig, WorkspaceProfile
from app.workspaces.enums import ProfileType, ContextStatus
from app.workspaces.exceptions import WrongWorkspaceContextError


def test_context_set_and_get():
    manager = ContextManager()
    ws = WorkspaceConfig(workspace_id="ws_1", name="Test")
    p = WorkspaceProfile(
        profile_id="p_1",
        workspace_id="ws_1",
        name="P",
        profile_type=ProfileType.PAPER_DEFAULT,
    )

    manager.set_active_context(ws, p)
    ctx = manager.get_active_context()

    assert ctx.status == ContextStatus.ACTIVE
    assert ctx.active_workspace.workspace_id == "ws_1"


def test_require_active_context_fails_when_stale():
    manager = ContextManager()
    with pytest.raises(WrongWorkspaceContextError):
        manager.require_active_context()


def test_context_mismatch_fails():
    manager = ContextManager()
    ws = WorkspaceConfig(workspace_id="ws_1", name="Test")
    p = WorkspaceProfile(
        profile_id="p_1",
        workspace_id="ws_2",
        name="P",
        profile_type=ProfileType.PAPER_DEFAULT,
    )

    with pytest.raises(WrongWorkspaceContextError):
        manager.set_active_context(ws, p)
