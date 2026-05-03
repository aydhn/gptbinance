import pytest
from app.workspaces.switching import ContextSwitcher
from app.workspaces.context import ContextManager
from app.workspaces.models import WorkspaceConfig, WorkspaceProfile
from app.workspaces.enums import ProfileType, SwitchVerdict
from app.workspaces.exceptions import WorkspaceSwitchError

def test_switch_preflight():
    manager = ContextManager()
    switcher = ContextSwitcher(manager)

    p_live = WorkspaceProfile(profile_id="p_live", workspace_id="ws_1", name="L", profile_type=ProfileType.CANARY_LIVE_CAUTION, live_affecting=True)
    p_paper = WorkspaceProfile(profile_id="p_paper", workspace_id="ws_1", name="P", profile_type=ProfileType.PAPER_DEFAULT, live_affecting=False)

    assert switcher.preflight_check(None, p_paper) == SwitchVerdict.ALLOWED
    assert switcher.preflight_check(None, p_live) == SwitchVerdict.CAUTION

def test_successful_switch():
    manager = ContextManager()
    switcher = ContextSwitcher(manager)
    ws = WorkspaceConfig(workspace_id="ws_1", name="Test")
    p = WorkspaceProfile(profile_id="p_1", workspace_id="ws_1", name="P", profile_type=ProfileType.PAPER_DEFAULT)

    record = switcher.switch(ws, p)

    assert record.verdict == SwitchVerdict.ALLOWED
    assert len(switcher.get_history()) == 1
    assert manager.get_active_context().active_profile.profile_id == "p_1"
