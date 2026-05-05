import pytest
from app.workspaces.catalog import WorkspaceCatalog
from app.workspaces.models import WorkspaceConfig, WorkspaceProfile
from app.workspaces.enums import WorkspaceType, ProfileType
from app.workspaces.exceptions import InvalidWorkspaceConfigError


def test_workspace_registration():
    catalog = WorkspaceCatalog()
    ws = WorkspaceConfig(workspace_id="ws_1", name="Test WS")
    catalog.register_workspace(ws)

    assert catalog.get_workspace("ws_1") is not None
    assert len(catalog.list_workspaces()) == 1


def test_duplicate_workspace_registration():
    catalog = WorkspaceCatalog()
    ws = WorkspaceConfig(workspace_id="ws_1", name="Test WS")
    catalog.register_workspace(ws)

    with pytest.raises(InvalidWorkspaceConfigError):
        catalog.register_workspace(ws)


def test_profile_registration():
    catalog = WorkspaceCatalog()
    ws = WorkspaceConfig(workspace_id="ws_1", name="Test WS")
    catalog.register_workspace(ws)

    profile = WorkspaceProfile(
        profile_id="p_1",
        workspace_id="ws_1",
        name="Test Profile",
        profile_type=ProfileType.PAPER_DEFAULT,
    )
    catalog.register_profile(profile)

    profiles = catalog.get_profiles_for_workspace("ws_1")
    assert len(profiles) == 1
    assert profiles[0].profile_id == "p_1"
