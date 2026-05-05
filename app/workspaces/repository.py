import uuid
from typing import List, Optional
from app.workspaces.models import WorkspaceConfig, WorkspaceProfile
from app.workspaces.catalog import WorkspaceCatalog
from app.workspaces.paths import PathResolver


class WorkspaceRepository:
    def __init__(self, catalog: WorkspaceCatalog, path_resolver: PathResolver):
        self.catalog = catalog
        self.path_resolver = path_resolver

    def create_workspace(self, name: str, description: str = "") -> WorkspaceConfig:
        ws = WorkspaceConfig(
            workspace_id=str(uuid.uuid4())[:8], name=name, description=description
        )
        self.catalog.register_workspace(ws)
        return ws

    def create_profile(
        self, workspace_id: str, name: str, profile_type
    ) -> WorkspaceProfile:
        ws = self.catalog.get_workspace(workspace_id)
        if not ws:
            raise ValueError(f"Workspace {workspace_id} not found")

        profile = WorkspaceProfile(
            profile_id=str(uuid.uuid4())[:8],
            workspace_id=workspace_id,
            name=name,
            profile_type=profile_type,
        )

        # Resolve and create paths
        profile.scoped_paths = self.path_resolver.resolve_scoped_paths(profile)
        self.path_resolver.ensure_paths_exist(profile.scoped_paths)

        self.catalog.register_profile(profile)
        return profile
