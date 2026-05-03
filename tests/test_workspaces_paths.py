import os
import shutil
from app.workspaces.paths import PathResolver
from app.workspaces.models import WorkspaceProfile
from app.workspaces.enums import ProfileType

def test_resolve_scoped_paths():
    resolver = PathResolver(base_dir="/tmp/test_workspaces")
    p = WorkspaceProfile(profile_id="p_1", workspace_id="ws_1", name="P", profile_type=ProfileType.PAPER_DEFAULT)

    paths = resolver.resolve_scoped_paths(p)
    assert "/tmp/test_workspaces/ws_1/p_1/config" in paths.config_root

def test_ensure_paths_exist():
    resolver = PathResolver(base_dir="/tmp/test_workspaces")
    p = WorkspaceProfile(profile_id="p_1", workspace_id="ws_1", name="P", profile_type=ProfileType.PAPER_DEFAULT)
    paths = resolver.resolve_scoped_paths(p)

    resolver.ensure_paths_exist(paths)
    assert os.path.exists(paths.config_root)
    assert os.path.exists(paths.state_root)

    # Cleanup
    shutil.rmtree("/tmp/test_workspaces", ignore_errors=True)
