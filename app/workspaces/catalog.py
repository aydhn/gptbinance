from typing import List, Optional, Dict
from app.workspaces.models import WorkspaceConfig, WorkspaceProfile, WorkspaceCatalogEntry
from app.workspaces.exceptions import InvalidWorkspaceConfigError

class WorkspaceCatalog:
    def __init__(self):
        self._workspaces: Dict[str, WorkspaceConfig] = {}
        self._profiles: Dict[str, List[WorkspaceProfile]] = {}

    def register_workspace(self, workspace: WorkspaceConfig) -> None:
        if workspace.workspace_id in self._workspaces:
            raise InvalidWorkspaceConfigError(f"Workspace {workspace.workspace_id} already exists.")
        self._workspaces[workspace.workspace_id] = workspace
        self._profiles[workspace.workspace_id] = []

    def register_profile(self, profile: WorkspaceProfile) -> None:
        if profile.workspace_id not in self._workspaces:
            raise InvalidWorkspaceConfigError(f"Workspace {profile.workspace_id} not found.")
        self._profiles[profile.workspace_id].append(profile)

    def get_workspace(self, workspace_id: str) -> Optional[WorkspaceConfig]:
        return self._workspaces.get(workspace_id)

    def get_profiles_for_workspace(self, workspace_id: str) -> List[WorkspaceProfile]:
        return self._profiles.get(workspace_id, [])

    def list_workspaces(self) -> List[WorkspaceConfig]:
        return list(self._workspaces.values())

    def get_catalog_entry(self, workspace_id: str) -> Optional[WorkspaceCatalogEntry]:
        ws = self.get_workspace(workspace_id)
        if not ws:
            return None
        return WorkspaceCatalogEntry(
            workspace=ws,
            profiles=self.get_profiles_for_workspace(workspace_id)
        )
