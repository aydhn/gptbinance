import logging
from typing import List, Any

from app.analytics.base import JournalBuilderBase
from app.analytics.models import TradeJournalEntry, TradeLifecycleSummary
from app.analytics.enums import JournalEventType

logger = logging.getLogger(__name__)


class TradeJournalBuilder(JournalBuilderBase):
    def __init__(self):
        self.entries: List[TradeJournalEntry] = []

    def add_entry(self, entry: TradeJournalEntry):
        self.entries.append(entry)

    def build(self, run_id: str, data: Any = None) -> List[TradeJournalEntry]:
        # Typically this would merge raw streams from Risk/Portfolio/Execution into one unified lineage.
        # For this skeleton, we just return the in-memory built entries.
        return self.entries

    def generate_lifecycle_summaries(self, run_id: str) -> List[TradeLifecycleSummary]:
        summaries = {}

        # Group entries by symbol and order_ref (assuming order_ref ties a lifecycle)
        # Real logic would be far more robust tying entry to exit
        for entry in self.entries:
            if entry.run_id != run_id:
                continue

            # Use order_ref as a crude trade_id grouping key for now
            trade_id = entry.order_ref or entry.entry_id

            if trade_id not in summaries:
                summaries[trade_id] = TradeLifecycleSummary(
                    trade_id=trade_id,
                    symbol=entry.symbol,
                    open_time=entry.timestamp,
                    strategy_family=entry.details.get("strategy_family", "unknown"),
                    regime=entry.details.get("regime", "unknown"),
                    journal_refs=[],
                )

            summaries[trade_id].journal_refs.append(entry.entry_id)

            if entry.event_type == JournalEventType.ORDER_FILLED:
                summaries[trade_id].pnl += entry.details.get("realized_pnl", 0.0)
                summaries[trade_id].fees += entry.details.get("fee", 0.0)

            if entry.event_type == JournalEventType.POSITION_CLOSED:
                summaries[trade_id].close_time = entry.timestamp
                summaries[trade_id].is_complete = True

        # Warn on incomplete lifecycles
        res = []
        for s in summaries.values():
            if not s.is_complete:
                logger.warning(
                    f"Incomplete lifecycle detected for trade_id: {s.trade_id}"
                )
            res.append(s)

        return res
