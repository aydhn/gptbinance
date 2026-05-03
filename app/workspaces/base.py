import abc
from typing import Dict, Any, List, Optional
from app.workspaces.models import (
    WorkspaceConfig,
    WorkspaceProfile,
    WorkspaceContext,
    BoundaryCheckResult,
    WorkspaceSwitchRecord
)

class WorkspaceResolverBase(abc.ABC):
    @abc.abstractmethod
    def resolve_workspace(self, workspace_id: str) -> Optional[WorkspaceConfig]:
        pass

class BoundaryCheckerBase(abc.ABC):
    @abc.abstractmethod
    def check_boundaries(self, profile: WorkspaceProfile) -> List[BoundaryCheckResult]:
        pass

class ContextSwitcherBase(abc.ABC):
    @abc.abstractmethod
    def switch_context(self, target_profile: WorkspaceProfile) -> WorkspaceSwitchRecord:
        pass

class ScopedStorageBase(abc.ABC):
    @abc.abstractmethod
    def get_scoped_path(self, profile: WorkspaceProfile, path_type: str) -> str:
        pass
