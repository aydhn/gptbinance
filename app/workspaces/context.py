from typing import Optional
from app.workspaces.models import WorkspaceContext, WorkspaceConfig, WorkspaceProfile
from app.workspaces.enums import ContextStatus
from app.workspaces.exceptions import WrongWorkspaceContextError


class ContextManager:
    def __init__(self):
        self._active_context: WorkspaceContext = WorkspaceContext()

    def get_active_context(self) -> WorkspaceContext:
        return self._active_context

    def require_active_context(self) -> WorkspaceContext:
        if (
            self._active_context.status != ContextStatus.ACTIVE
            or not self._active_context.active_profile
        ):
            raise WrongWorkspaceContextError("No active workspace context.")
        return self._active_context

    def set_active_context(
        self, workspace: WorkspaceConfig, profile: WorkspaceProfile
    ) -> None:
        if profile.workspace_id != workspace.workspace_id:
            raise WrongWorkspaceContextError(
                f"Profile {profile.profile_id} does not belong to workspace {workspace.workspace_id}."
            )

        self._active_context.active_workspace = workspace
        self._active_context.active_profile = profile
        self._active_context.status = ContextStatus.ACTIVE

    def clear_context(self) -> None:
        self._active_context = WorkspaceContext()
