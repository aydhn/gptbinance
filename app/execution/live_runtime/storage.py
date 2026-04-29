import json
import os
from datetime import datetime
from pathlib import Path
from app.execution.live_runtime.models import (
    LiveAccountSnapshot,
    LiveEquitySnapshot,
    LiveAuditRecord,
    LiveRun,
    LiveAfterActionSummary,
)


class LiveStorage:
    def __init__(self, base_dir: str = "data/live_runs"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _get_run_dir(self, run_id: str) -> Path:
        run_dir = self.base_dir / run_id
        run_dir.mkdir(exist_ok=True)
        return run_dir

    def save_run(self, run: LiveRun) -> None:
        path = self._get_run_dir(run.run_id) / "run.json"
        with open(path, "w") as f:
            f.write(run.model_dump_json(indent=2))

    def get_run(self, run_id: str) -> LiveRun | None:
        path = self._get_run_dir(run_id) / "run.json"
        if path.exists():
            return LiveRun.model_validate_json(path.read_text())
        return None

    def save_account_snapshot(self, run_id: str, snapshot: LiveAccountSnapshot) -> None:
        path = (
            self._get_run_dir(run_id) / f"account_{snapshot.timestamp.timestamp()}.json"
        )
        with open(path, "w") as f:
            f.write(snapshot.model_dump_json(indent=2))

    def get_latest_account_snapshot(self, run_id: str) -> LiveAccountSnapshot | None:
        d = self._get_run_dir(run_id)
        files = sorted(d.glob("account_*.json"))
        if files:
            return LiveAccountSnapshot.model_validate_json(files[-1].read_text())
        return None

    def save_equity_snapshot(self, run_id: str, snapshot: LiveEquitySnapshot) -> None:
        path = (
            self._get_run_dir(run_id) / f"equity_{snapshot.timestamp.timestamp()}.json"
        )
        with open(path, "w") as f:
            f.write(snapshot.model_dump_json(indent=2))

    def get_latest_equity_snapshot(self, run_id: str) -> LiveEquitySnapshot | None:
        d = self._get_run_dir(run_id)
        files = sorted(d.glob("equity_*.json"))
        if files:
            return LiveEquitySnapshot.model_validate_json(files[-1].read_text())
        return None

    def save_audit_records(self, run_id: str, records: list[LiveAuditRecord]) -> None:
        path = self._get_run_dir(run_id) / "audit.json"
        with open(path, "w") as f:
            json.dump([r.model_dump() for r in records], f, indent=2, default=str)

    def get_audit_records(self, run_id: str) -> list[LiveAuditRecord]:
        path = self._get_run_dir(run_id) / "audit.json"
        if path.exists():
            data = json.loads(path.read_text())
            return [LiveAuditRecord(**r) for r in data]
        return []

    def save_after_action_summary(
        self, run_id: str, summary: LiveAfterActionSummary
    ) -> None:
        path = self._get_run_dir(run_id) / "after_action.json"
        with open(path, "w") as f:
            f.write(summary.model_dump_json(indent=2))

    def get_after_action_summary(self, run_id: str) -> LiveAfterActionSummary | None:
        path = self._get_run_dir(run_id) / "after_action.json"
        if path.exists():
            return LiveAfterActionSummary.model_validate_json(path.read_text())
        return None
