import json
import os
import logging
from uuid import UUID
from typing import Optional

from app.backtest.walkforward.models import WalkForwardRun, WalkForwardArtifactManifest

logger = logging.getLogger(__name__)


class WalkForwardStorage:
    def __init__(self, base_dir: str = "data/runs/walkforward"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def _get_run_dir(self, run_id: str) -> str:
        return os.path.join(self.base_dir, run_id)

    def save_run(self, run: WalkForwardRun) -> None:
        run_dir = self._get_run_dir(run.run_id)
        os.makedirs(run_dir, exist_ok=True)

        run_file = os.path.join(run_dir, "run.json")
        with open(run_file, "w") as f:
            f.write(run.model_dump_json(indent=2))

    def load_run(self, run_id: str) -> Optional[WalkForwardRun]:
        run_file = os.path.join(self._get_run_dir(run_id), "run.json")
        if not os.path.exists(run_file):
            return None

        with open(run_file, "r") as f:
            data = json.load(f)
            return WalkForwardRun(**data)

    def save_manifest(self, manifest: WalkForwardArtifactManifest) -> None:
        run_dir = self._get_run_dir(manifest.run_id)
        os.makedirs(run_dir, exist_ok=True)

        manifest_file = os.path.join(run_dir, "manifest.json")
        with open(manifest_file, "w") as f:
            f.write(manifest.model_dump_json(indent=2))
