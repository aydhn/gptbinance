import os
from pathlib import Path
from typing import Optional
from app.workspaces.models import WorkspaceProfile, ScopedPathSet
from app.workspaces.exceptions import ScopedPathError


class PathResolver:
    def __init__(self, base_dir: str = ".workspaces"):
        self.base_dir = Path(base_dir)

    def resolve_scoped_paths(self, profile: WorkspaceProfile) -> ScopedPathSet:
        profile_dir = self.base_dir / profile.workspace_id / profile.profile_id

        paths = ScopedPathSet(
            config_root=str(profile_dir / "config"),
            state_root=str(profile_dir / "state"),
            artifact_root=str(profile_dir / "artifacts"),
            log_root=str(profile_dir / "logs"),
            evidence_root=str(profile_dir / "evidence"),
            backup_root=str(profile_dir / "backups"),
            metrics_root=str(profile_dir / "metrics"),
            replays_root=str(profile_dir / "replays"),
            analytics_root=str(profile_dir / "analytics"),
        )
        return paths

    def ensure_paths_exist(self, paths: ScopedPathSet) -> None:
        try:
            for field, path_str in paths.model_dump().items():
                os.makedirs(path_str, exist_ok=True)
        except Exception as e:
            raise ScopedPathError(f"Failed to create scoped paths: {e}")
