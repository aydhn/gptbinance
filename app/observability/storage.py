import sqlite3
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, Dict
from app.observability.models import (
    ObservabilityConfig,
    MetricSample,
    AlertEvent,
    TelemetryEvent,
)


class ObservabilityStorage:
    def __init__(self, config: ObservabilityConfig):
        self.config = config
        self.db_path = Path(self.config.storage_path) / "observability.db"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS metric_samples (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    metric_name TEXT NOT NULL,
                    value REAL NOT NULL,
                    timestamp TEXT NOT NULL,
                    tags TEXT,
                    run_id TEXT
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS telemetry_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_type TEXT NOT NULL,
                    component TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    severity TEXT,
                    details TEXT,
                    run_id TEXT
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS active_alerts (
                    alert_id TEXT PRIMARY KEY,
                    rule_id TEXT NOT NULL,
                    component TEXT NOT NULL,
                    severity TEXT NOT NULL,
                    state TEXT NOT NULL,
                    first_seen TEXT NOT NULL,
                    last_seen TEXT NOT NULL,
                    occurrence_count INTEGER,
                    evidence TEXT,
                    runbook_ref TEXT
                )
            """)
            conn.commit()

    def save_metric_sample(self, sample: MetricSample) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO metric_samples (metric_name, value, timestamp, tags, run_id) VALUES (?, ?, ?, ?, ?)",
                (
                    sample.metric_name,
                    sample.value,
                    sample.timestamp.isoformat(),
                    json.dumps(sample.tags),
                    sample.run_id,
                ),
            )

    def save_telemetry_event(self, event: TelemetryEvent) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO telemetry_events (event_type, component, timestamp, severity, details, run_id) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    event.event_type,
                    event.component.value,
                    event.timestamp.isoformat(),
                    event.severity.value,
                    json.dumps(event.details),
                    event.run_id,
                ),
            )

    def upsert_alert(self, alert: AlertEvent) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT INTO active_alerts (alert_id, rule_id, component, severity, state, first_seen, last_seen, occurrence_count, evidence, runbook_ref)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(alert_id) DO UPDATE SET
                    state=excluded.state,
                    last_seen=excluded.last_seen,
                    occurrence_count=excluded.occurrence_count,
                    evidence=excluded.evidence
                """,
                (
                    alert.alert_id,
                    alert.rule_id,
                    alert.component.value,
                    alert.severity.value,
                    alert.state.value,
                    alert.first_seen.isoformat(),
                    alert.last_seen.isoformat(),
                    alert.occurrence_count,
                    json.dumps(alert.evidence),
                    alert.runbook_ref,
                ),
            )
