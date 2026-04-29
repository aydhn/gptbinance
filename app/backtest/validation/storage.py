import sqlite3
import json
from uuid import UUID
from typing import Optional, List
from pathlib import Path
import logging

from app.backtest.validation.models import (
    ValidationSummary,
    BenchmarkResult,
    ComparisonResult,
    AblationResult,
    RobustnessCheckResult,
    ResearchHonestyReport,
)

logger = logging.getLogger(__name__)


class ValidationStorage:
    def __init__(self, db_path: str = "data/validation.sqlite"):
        self.db_path = str(db_path)
        if self.db_path != ":memory:":
            Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        self._conn = None
        if self.db_path == ":memory:":
            self._conn = sqlite3.connect(self.db_path)
        self._init_db()

    def _get_conn(self):
        if self._conn:
            return self._conn
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        conn = self._get_conn()
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS validation_summaries (
                    validation_id TEXT PRIMARY KEY,
                    strategy_run_id TEXT NOT NULL,
                    status TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    summary_json TEXT NOT NULL
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_validation_strategy
                ON validation_summaries(strategy_run_id)
            """)
        if not self._conn:
            conn.close()

    def save_validation_summary(self, summary: ValidationSummary) -> None:
        conn = self._get_conn()
        with conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO validation_summaries
                (validation_id, strategy_run_id, status, created_at, summary_json)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    str(summary.validation_id),
                    str(summary.strategy_run_id),
                    summary.status.value,
                    summary.created_at.isoformat(),
                    summary.model_dump_json(),
                ),
            )
        logger.info(
            f"Saved ValidationSummary {summary.validation_id} for run {summary.strategy_run_id}"
        )
        if not self._conn:
            conn.close()

    def get_validation_summary(
        self, strategy_run_id: UUID
    ) -> Optional[ValidationSummary]:
        conn = self._get_conn()
        try:
            cursor = conn.execute(
                """
                SELECT summary_json FROM validation_summaries
                WHERE strategy_run_id = ?
                ORDER BY created_at DESC LIMIT 1
                """,
                (str(strategy_run_id),),
            )
            row = cursor.fetchone()
            if row:
                return ValidationSummary.model_validate_json(row[0])
            return None
        finally:
            if not self._conn:
                conn.close()
