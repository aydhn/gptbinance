from typing import List
from pathlib import Path
from app.research.regime.models import RegimeSnapshot


class RegimeStorage:
    def __init__(self, base_dir: str = "data/regime"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _get_file_path(self, symbol: str, interval: str) -> Path:
        return self.base_dir / f"{symbol}_{interval}_regime.jsonl"

    def save_snapshot(self, snapshot: RegimeSnapshot):
        file_path = self._get_file_path(snapshot.symbol, snapshot.interval)
        with open(file_path, "a") as f:
            f.write(snapshot.model_dump_json() + "\n")

    def load_recent_snapshots(
        self, symbol: str, interval: str, limit: int = 100
    ) -> List[RegimeSnapshot]:
        file_path = self._get_file_path(symbol, interval)
        if not file_path.exists():
            return []

        snapshots = []
        # Not memory efficient for huge files, but ok for now
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines[-limit:]:
                if line.strip():
                    snapshots.append(RegimeSnapshot.model_validate_json(line))
        return snapshots
