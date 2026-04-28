import json
import os
from pathlib import Path
from datetime import datetime
from typing import Optional, List
from app.backtest.models import (
    BacktestResult,
    BacktestArtifactManifest,
    TradeRecord,
    EquitySnapshot,
)


class BacktestStorage:
    def __init__(self, base_dir: str = "data/backtests"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save_result(
        self,
        result: BacktestResult,
        trades: List[TradeRecord],
        equity_snapshots: List[EquitySnapshot],
    ) -> BacktestArtifactManifest:
        run_dir = self.base_dir / result.run.run_id
        run_dir.mkdir(parents=True, exist_ok=True)

        config_path = run_dir / "config.json"
        with open(config_path, "w") as f:
            f.write(result.run.config.model_dump_json(indent=2))

        summary_path = run_dir / "summary.json"
        with open(summary_path, "w") as f:
            f.write(result.summary.model_dump_json(indent=2))

        trade_log_path = run_dir / "trades.jsonl"
        with open(trade_log_path, "w") as f:
            for t in trades:
                f.write(t.model_dump_json() + "\n")

        equity_curve_path = run_dir / "equity.jsonl"
        with open(equity_curve_path, "w") as f:
            for snap in equity_snapshots:
                f.write(snap.model_dump_json() + "\n")

        manifest = BacktestArtifactManifest(
            run_id=result.run.run_id,
            timestamp=datetime.now(),
            config_path=str(config_path),
            trade_log_path=str(trade_log_path),
            equity_curve_path=str(equity_curve_path),
            summary_path=str(summary_path),
        )

        manifest_path = run_dir / "manifest.json"
        with open(manifest_path, "w") as f:
            f.write(manifest.model_dump_json(indent=2))

        return manifest

    def load_summary(self, run_id: str) -> Optional[dict]:
        path = self.base_dir / run_id / "summary.json"
        if path.exists():
            with open(path, "r") as f:
                return json.load(f)
        return None

    def load_trades(self, run_id: str) -> List[dict]:
        path = self.base_dir / run_id / "trades.jsonl"
        trades = []
        if path.exists():
            with open(path, "r") as f:
                for line in f:
                    trades.append(json.loads(line))
        return trades

    def load_equity(self, run_id: str) -> List[dict]:
        path = self.base_dir / run_id / "equity.jsonl"
        equity = []
        if path.exists():
            with open(path, "r") as f:
                for line in f:
                    equity.append(json.loads(line))
        return equity
