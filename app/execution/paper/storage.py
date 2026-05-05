"""Storage interfaces and implementation for paper session artifacts."""

import json
import sqlite3
import os
import logging
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from .models import (
    PaperSessionConfig,
    PaperRuntimeSummary,
    PaperArtifactManifest,
    PaperOrder,
    PaperFill,
    PaperPosition,
    PaperEquitySnapshot,
    SessionHealthSnapshot,
)

logger = logging.getLogger(__name__)


def adapt_datetime(ts: datetime) -> str:
    return ts.isoformat()


sqlite3.register_adapter(datetime, adapt_datetime)


class PaperStorage:
    def __init__(self, db_path: str = "paper_runtime.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS session_manifests (
                    run_id TEXT PRIMARY KEY,
                    config_json TEXT,
                    summary_json TEXT,
                    start_time TEXT,
                    end_time TEXT
                )
            """
            )
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS paper_orders (
                    run_id TEXT,
                    order_id TEXT,
                    intent_id TEXT,
                    symbol TEXT,
                    side TEXT,
                    qty REAL,
                    status TEXT,
                    created_at TEXT,
                    filled_at TEXT,
                    rejection_reason TEXT,
                    PRIMARY KEY (run_id, order_id)
                )
            """
            )
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS paper_fills (
                    run_id TEXT,
                    fill_id TEXT,
                    order_id TEXT,
                    symbol TEXT,
                    side TEXT,
                    qty REAL,
                    price REAL,
                    fees REAL,
                    slippage REAL,
                    timestamp TEXT,
                    PRIMARY KEY (run_id, fill_id)
                )
            """
            )
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS paper_snapshots (
                    run_id TEXT,
                    timestamp TEXT,
                    equity REAL,
                    drawdown_pct REAL,
                    health TEXT,
                    PRIMARY KEY (run_id, timestamp)
                )
            """
            )
            conn.commit()

    def save_manifest(self, manifest: PaperArtifactManifest):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute(
                """
                INSERT OR REPLACE INTO session_manifests
                (run_id, config_json, summary_json, start_time, end_time)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    manifest.run_id,
                    manifest.config.model_dump_json(),
                    manifest.summary.model_dump_json(),
                    manifest.summary.start_time,
                    manifest.summary.end_time,
                ),
            )
            conn.commit()

    def save_order(self, run_id: str, order: PaperOrder):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute(
                """
                INSERT OR REPLACE INTO paper_orders
                (run_id, order_id, intent_id, symbol, side, qty, status, created_at, filled_at, rejection_reason)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    run_id,
                    order.order_id,
                    order.intent_id,
                    order.symbol,
                    order.side,
                    order.qty,
                    order.status.value,
                    order.created_at,
                    order.filled_at,
                    order.rejection_reason,
                ),
            )
            conn.commit()

    def save_fill(self, run_id: str, fill: PaperFill):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute(
                """
                INSERT OR REPLACE INTO paper_fills
                (run_id, fill_id, order_id, symbol, side, qty, price, fees, slippage, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    run_id,
                    fill.fill_id,
                    fill.order_id,
                    fill.symbol,
                    fill.side,
                    fill.qty,
                    fill.price,
                    fill.fees,
                    fill.slippage,
                    fill.timestamp,
                ),
            )
            conn.commit()

    def save_snapshot(
        self, run_id: str, equity: PaperEquitySnapshot, health: SessionHealthSnapshot
    ):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute(
                """
                INSERT INTO paper_snapshots
                (run_id, timestamp, equity, drawdown_pct, health)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    run_id,
                    equity.timestamp,
                    equity.equity,
                    equity.drawdown_pct,
                    health.health.value,
                ),
            )
            conn.commit()

    def get_manifest(self, run_id: str) -> Optional[PaperArtifactManifest]:
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute(
                "SELECT config_json, summary_json FROM session_manifests WHERE run_id = ?",
                (run_id,),
            )
            row = c.fetchone()
            if row:
                config = PaperSessionConfig.model_validate_json(row[0])
                summary = PaperRuntimeSummary.model_validate_json(row[1])
                return PaperArtifactManifest(
                    run_id=run_id, config=config, summary=summary
                )
        return None

    def get_orders(self, run_id: str) -> List[dict]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(
                "SELECT * FROM paper_orders WHERE run_id = ? ORDER BY created_at",
                (run_id,),
            )
            return [dict(row) for row in c.fetchall()]

    def get_fills(self, run_id: str) -> List[dict]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(
                "SELECT * FROM paper_fills WHERE run_id = ? ORDER BY timestamp",
                (run_id,),
            )
            return [dict(row) for row in c.fetchall()]

    def get_snapshots(self, run_id: str) -> List[dict]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(
                "SELECT * FROM paper_snapshots WHERE run_id = ? ORDER BY timestamp",
                (run_id,),
            )
            return [dict(row) for row in c.fetchall()]
