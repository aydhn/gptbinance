import uuid
from datetime import datetime, timezone
from typing import Optional, Dict, Any
from app.workspaces.models import (
    WorkspaceProfile,
    WorkspaceProfileRef,
    WorkspaceSwitchRecord,
    WorkspaceConfig
)
from app.workspaces.enums import SwitchVerdict, ContextStatus
from app.workspaces.context import ContextManager
from app.workspaces.exceptions import WorkspaceSwitchError

class ContextSwitcher:
    def __init__(self, context_manager: ContextManager):
        self.context_manager = context_manager
        self.switch_history: list[WorkspaceSwitchRecord] = []

    def preflight_check(self, current: Optional[WorkspaceProfile], target: WorkspaceProfile) -> SwitchVerdict:
        if current and current.profile_id == target.profile_id:
            return SwitchVerdict.CAUTION # Switching to same profile

        if target.live_affecting:
            return SwitchVerdict.CAUTION # Require explicit confirmation for live profiles

        return SwitchVerdict.ALLOWED

    def switch(self, target_workspace: WorkspaceConfig, target_profile: WorkspaceProfile, reason: str = "Manual switch") -> WorkspaceSwitchRecord:
        current_context = self.context_manager.get_active_context()
        current_profile = current_context.active_profile

        verdict = self.preflight_check(current_profile, target_profile)
        if verdict == SwitchVerdict.DENIED:
            raise WorkspaceSwitchError("Switch denied by preflight checks.")

        # Create record
        from_ref = None
        if current_profile:
            from_ref = WorkspaceProfileRef(
                workspace_id=current_profile.workspace_id,
                profile_id=current_profile.profile_id,
                profile_type=current_profile.profile_type
            )

        to_ref = WorkspaceProfileRef(
            workspace_id=target_profile.workspace_id,
            profile_id=target_profile.profile_id,
            profile_type=target_profile.profile_type
        )

        record = WorkspaceSwitchRecord(
            switch_id=str(uuid.uuid4()),
            from_profile=from_ref,
            to_profile=to_ref,
            verdict=verdict,
            reason=reason,
            timestamp=datetime.now(timezone.utc)
        )

        # Apply switch
        self.context_manager.set_active_context(target_workspace, target_profile)
        self.context_manager.get_active_context().last_switch_at = record.timestamp
        self.switch_history.append(record)

        return record

    def get_history(self) -> list[WorkspaceSwitchRecord]:
        return self.switch_history
