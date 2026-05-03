import json
import os
from pathlib import Path
from typing import Optional, Dict, Any

class WorkspaceStorageBackend:
    def __init__(self, data_dir: str = ".workspaces_data"):
        self.data_dir = Path(data_dir)
        os.makedirs(self.data_dir, exist_ok=True)

    def _get_workspace_path(self, workspace_id: str) -> Path:
        return self.data_dir / f"{workspace_id}.json"

    def save_workspace_data(self, workspace_id: str, data: Dict[str, Any]) -> None:
        path = self._get_workspace_path(workspace_id)
        with open(path, "w") as f:
            json.dump(data, f, indent=2, default=str)

    def load_workspace_data(self, workspace_id: str) -> Optional[Dict[str, Any]]:
        path = self._get_workspace_path(workspace_id)
        if not path.exists():
            return None
        with open(path, "r") as f:
            return json.load(f)
