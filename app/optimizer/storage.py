import json
import sqlite3
import os
from typing import Optional, List, Dict
from app.optimizer.models import OptimizerRun, TrialArtifactManifest, TrialResult


class OptimizerStorage:
    def __init__(self, db_path: str = "data/optimizer.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS optimizer_runs (
                    run_id TEXT PRIMARY KEY,
                    symbol TEXT,
                    strategy_family TEXT,
                    status TEXT,
                    run_data JSON
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS optimizer_trials (
                    trial_id TEXT PRIMARY KEY,
                    run_id TEXT,
                    candidate_id TEXT,
                    metrics JSON,
                    guard_report JSON,
                    trial_data JSON,
                    FOREIGN KEY(run_id) REFERENCES optimizer_runs(run_id)
                )
            """)

    def save_run(self, run: OptimizerRun) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO optimizer_runs (run_id, symbol, strategy_family, status, run_data) VALUES (?, ?, ?, ?, ?)",
                (
                    run.run_id,
                    run.config.symbol,
                    run.config.strategy_family,
                    run.status.value,
                    run.json(),
                ),
            )
            for trial in run.trials:
                self.save_trial(trial)

    def save_trial(self, trial: TrialResult) -> None:
        metrics_json = trial.metrics.json() if trial.metrics else "{}"
        guard_json = trial.guard_report.json() if trial.guard_report else "{}"

        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """INSERT OR REPLACE INTO optimizer_trials
                   (trial_id, run_id, candidate_id, metrics, guard_report, trial_data)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    trial.trial_id,
                    trial.config.run_id,
                    trial.config.candidate.candidate_id,
                    metrics_json,
                    guard_json,
                    trial.json(),
                ),
            )

    def load_run(self, run_id: str) -> Optional[OptimizerRun]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT run_data FROM optimizer_runs WHERE run_id = ?", (run_id,)
            ).fetchone()
            if row:
                return OptimizerRun.parse_raw(row["run_data"])
        return None

    def load_trial(self, trial_id: str) -> Optional[TrialResult]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT trial_data FROM optimizer_trials WHERE trial_id = ?",
                (trial_id,),
            ).fetchone()
            if row:
                return TrialResult.parse_raw(row["trial_data"])
        return None
