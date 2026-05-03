import json
import sqlite3
from typing import Dict, Any, List, Optional
from app.knowledge.models import KnowledgeItem, QuizResult, OperatorReadinessRecord


class KnowledgeStorage:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS knowledge_items (
                item_id TEXT PRIMARY KEY,
                item_type TEXT,
                data TEXT
            )
        """
        )
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS quiz_results (
                quiz_id TEXT,
                operator_id TEXT,
                data TEXT
            )
        """
        )
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS readiness_records (
                operator_id TEXT PRIMARY KEY,
                data TEXT
            )
        """
        )
        self.conn.commit()

    def save_item(self, item: KnowledgeItem):
        data = item.model_dump_json()
        self.conn.execute(
            "INSERT OR REPLACE INTO knowledge_items (item_id, item_type, data) VALUES (?, ?, ?)",
            (item.item_id, item.item_type.value, data),
        )
        self.conn.commit()

    def get_items(self) -> List[Dict[str, Any]]:
        cursor = self.conn.execute("SELECT data FROM knowledge_items")
        return [json.loads(row["data"]) for row in cursor.fetchall()]

    def save_quiz_result(self, result: QuizResult):
        self.conn.execute(
            "INSERT INTO quiz_results (quiz_id, operator_id, data) VALUES (?, ?, ?)",
            (result.quiz_id, result.operator_id, result.model_dump_json()),
        )
        self.conn.commit()

    def save_readiness_record(self, record: OperatorReadinessRecord):
        self.conn.execute(
            "INSERT OR REPLACE INTO readiness_records (operator_id, data) VALUES (?, ?)",
            (record.operator_id, record.model_dump_json()),
        )
        self.conn.commit()
