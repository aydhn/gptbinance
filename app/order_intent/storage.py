from typing import Optional
import sqlite3
from app.order_intent.models import IntentCompilationResult


class IntentStorage:
    def __init__(self, db_path: str = "intent_ledger.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS compile_results (
                    run_id TEXT PRIMARY KEY,
                    intent_id TEXT,
                    intent_type TEXT,
                    symbol TEXT,
                    verdict TEXT,
                    result_json TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def save_result(self, result: IntentCompilationResult):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT INTO compile_results (run_id, intent_id, intent_type, symbol, verdict, result_json)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    result.audit_record.run_id,
                    result.intent.intent_id,
                    result.intent.intent_type.value,
                    result.intent.symbol,
                    result.verdict.value,
                    result.model_dump_json(),
                ),
            )
            conn.commit()

    def get_result(self, run_id: str) -> Optional[IntentCompilationResult]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT result_json FROM compile_results WHERE run_id = ?", (run_id,)
            )
            row = cursor.fetchone()
            if row:
                return IntentCompilationResult.model_validate_json(row[0])
        return None
