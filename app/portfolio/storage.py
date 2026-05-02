import json
import sqlite3
from typing import Dict, Any, List, Optional
from app.portfolio.models import PortfolioDecisionBatch, PortfolioSummary


class PortfolioStorage:
    def __init__(self, db_path: str = "portfolio.sqlite"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS portfolio_batches (
                    run_id TEXT PRIMARY KEY,
                    timestamp TEXT,
                    payload TEXT
                )
                """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS portfolio_summaries (
                    run_id TEXT PRIMARY KEY,
                    timestamp TEXT,
                    payload TEXT
                )
                """)

    def save_batch(self, batch: PortfolioDecisionBatch):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO portfolio_batches (run_id, timestamp, payload) VALUES (?, ?, ?)",
                (batch.run_id, batch.timestamp.isoformat(), batch.model_dump_json()),
            )

    def load_batch(self, run_id: str) -> Optional[PortfolioDecisionBatch]:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(
                "SELECT payload FROM portfolio_batches WHERE run_id = ?", (run_id,)
            )
            row = cur.fetchone()
            if row:
                return PortfolioDecisionBatch.model_validate_json(row[0])
        return None

    def save_summary(self, summary: PortfolioSummary):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO portfolio_summaries (run_id, timestamp, payload) VALUES (?, ?, ?)",
                (
                    summary.run_id,
                    summary.timestamp.isoformat(),
                    summary.model_dump_json(),
                ),
            )

    def load_summary(self, run_id: str) -> Optional[PortfolioSummary]:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(
                "SELECT payload FROM portfolio_summaries WHERE run_id = ?", (run_id,)
            )
            row = cur.fetchone()
            if row:
                return PortfolioSummary.model_validate_json(row[0])
        return None
