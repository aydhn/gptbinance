import sqlite3
import json
from typing import Any
from .models import DecisionQualityConfig


class DecisionQualityStore:
    """
    SQLite-based storage for decision quality records.
    """

    def __init__(self, config: DecisionQualityConfig):
        self.db_path = config.storage_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Opportunity Candidates
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS opportunities (
                    id TEXT PRIMARY KEY,
                    symbol TEXT,
                    timestamp TEXT,
                    timeframe TEXT,
                    regime TEXT,
                    strategy_family TEXT,
                    profile TEXT,
                    signal_strength REAL,
                    market_truth_posture TEXT,
                    event_risk_context TEXT,
                    universe_eligibility_context TEXT,
                    metadata TEXT
                )
            """
            )

            # Funnel Records
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS funnel_records (
                    opportunity_id TEXT PRIMARY KEY,
                    final_class TEXT,
                    created_at TEXT,
                    stages_json TEXT
                )
            """
            )

            # Block Reasons
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS block_reasons (
                    id TEXT PRIMARY KEY,
                    opportunity_id TEXT,
                    reason_class TEXT,
                    description TEXT,
                    is_primary BOOLEAN,
                    evidence_refs TEXT
                )
            """
            )

            # Outcomes
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS outcomes (
                    opportunity_id TEXT PRIMARY KEY,
                    window_type TEXT,
                    start_time TEXT,
                    end_time TEXT,
                    realized_pnl REAL,
                    max_favorable_excursion REAL,
                    max_adverse_excursion REAL,
                    confidence TEXT,
                    verdict TEXT,
                    evidence_refs TEXT
                )
            """
            )

            conn.commit()

    def _dict_to_json(self, d: Any) -> str:
        return json.dumps(d) if d else "{}"

    def _json_to_dict(self, s: str) -> dict:
        return json.loads(s) if s else {}
