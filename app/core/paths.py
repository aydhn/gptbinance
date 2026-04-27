import os
from pathlib import Path


def get_project_root() -> Path:
    """Returns the absolute path to the project root directory."""
    # Assuming app/core/paths.py, root is two levels up
    return Path(__file__).resolve().parent.parent.parent


class ProjectPaths:
    def __init__(self, root_dir: Path | None = None):
        self.root = root_dir or get_project_root()

        self.storage = self.root / "storage"
        self.logs = self.storage / "logs"
        self.raw_data = self.storage / "raw"
        self.processed_data = self.storage / "processed"
        self.state = self.storage / "state"
        self.artifacts = self.storage / "artifacts"

        # Ensure base directories exist when Paths object is created
        # though explicit bootstrap is preferred.
        self.required_dirs = [
            self.storage,
            self.logs,
            self.raw_data,
            self.processed_data,
            self.state,
            self.artifacts,
        ]

    def bootstrap_directories(self) -> list[Path]:
        """Creates all required directories. Returns list of created/verified paths."""
        for d in self.required_dirs:
            d.mkdir(parents=True, exist_ok=True)
        return self.required_dirs

# Global instance
PATHS = ProjectPaths()
