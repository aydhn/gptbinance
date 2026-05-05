import pytest
from app.workspaces.repository import WorkspaceRepository
from app.workspaces.catalog import WorkspaceCatalog
from app.workspaces.paths import PathResolver
from app.workspaces.enums import ProfileType


def test_create_workspace_and_profile():
    catalog = WorkspaceCatalog()
    resolver = PathResolver(base_dir="/tmp/repo_test")
    repo = WorkspaceRepository(catalog, resolver)

    ws = repo.create_workspace("Test WS")
    assert ws.workspace_id is not None

    p = repo.create_profile(ws.workspace_id, "Test Profile", ProfileType.PAPER_DEFAULT)
    assert p.profile_id is not None
    assert p.scoped_paths is not None
