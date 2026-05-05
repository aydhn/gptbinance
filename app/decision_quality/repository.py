import sqlite3
from typing import Optional
import json
from .storage import DecisionQualityStore
from .models import (
    OpportunityCandidate,
    DecisionFunnelRecord,
    BlockReasonRecord,
    OpportunityOutcome,
)
from datetime import datetime


class DecisionQualityRepository:
    """
    Repository layer for interacting with DecisionQualityStore using Pydantic models.
    """

    def __init__(self, store: DecisionQualityStore):
        self.store = store

    def save_opportunity(self, candidate: OpportunityCandidate):
        with sqlite3.connect(self.store.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR REPLACE INTO opportunities
                (id, symbol, timestamp, timeframe, regime, strategy_family, profile, signal_strength, market_truth_posture, event_risk_context, universe_eligibility_context, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    candidate.id,
                    candidate.symbol,
                    candidate.timestamp.isoformat(),
                    candidate.timeframe,
                    candidate.regime,
                    candidate.strategy_family,
                    candidate.profile,
                    candidate.signal_strength,
                    candidate.market_truth_posture,
                    candidate.event_risk_context,
                    candidate.universe_eligibility_context,
                    self.store._dict_to_json(candidate.metadata),
                ),
            )
            conn.commit()

    def get_opportunity(self, opportunity_id: str) -> Optional[OpportunityCandidate]:
        with sqlite3.connect(self.store.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM opportunities WHERE id = ?", (opportunity_id,)
            )
            row = cursor.fetchone()
            if row:
                return OpportunityCandidate(
                    id=row[0],
                    symbol=row[1],
                    timestamp=datetime.fromisoformat(row[2]),
                    timeframe=row[3],
                    regime=row[4],
                    strategy_family=row[5],
                    profile=row[6],
                    signal_strength=row[7],
                    market_truth_posture=row[8],
                    event_risk_context=row[9],
                    universe_eligibility_context=row[10],
                    metadata=self.store._json_to_dict(row[11]),
                )
            return None

    def save_funnel(self, record: DecisionFunnelRecord):
        with sqlite3.connect(self.store.db_path) as conn:
            cursor = conn.cursor()
            stages_json = json.dumps([s.dict() for s in record.stages], default=str)
            cursor.execute(
                """
                INSERT OR REPLACE INTO funnel_records
                (opportunity_id, final_class, created_at, stages_json)
                VALUES (?, ?, ?, ?)
            """,
                (
                    record.opportunity_id,
                    record.final_class.value,
                    record.created_at.isoformat(),
                    stages_json,
                ),
            )
            conn.commit()

    def save_block_reason(self, reason: BlockReasonRecord):
        with sqlite3.connect(self.store.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR REPLACE INTO block_reasons
                (id, opportunity_id, reason_class, description, is_primary, evidence_refs)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    reason.id,
                    reason.opportunity_id,
                    reason.reason_class.value,
                    reason.description,
                    reason.is_primary,
                    json.dumps(reason.evidence_refs),
                ),
            )
            conn.commit()

    def save_outcome(self, outcome: OpportunityOutcome):
        with sqlite3.connect(self.store.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR REPLACE INTO outcomes
                (opportunity_id, window_type, start_time, end_time, realized_pnl, max_favorable_excursion, max_adverse_excursion, confidence, verdict, evidence_refs)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    outcome.opportunity_id,
                    outcome.window.window_type.value,
                    outcome.window.start_time.isoformat(),
                    outcome.window.end_time.isoformat(),
                    outcome.realized_pnl,
                    outcome.max_favorable_excursion,
                    outcome.max_adverse_excursion,
                    outcome.confidence.value,
                    outcome.verdict.value,
                    json.dumps(outcome.evidence_refs),
                ),
            )
            conn.commit()
