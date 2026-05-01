from datetime import datetime
from app.analytics.journal import TradeJournalBuilder
from app.analytics.models import TradeJournalEntry
from app.analytics.enums import JournalEventType


def test_trade_journal_lifecycle():
    builder = TradeJournalBuilder()

    t1 = datetime(2025, 1, 1, 10, 0)
    t2 = datetime(2025, 1, 1, 11, 0)

    e1 = TradeJournalEntry(
        entry_id="1",
        run_id="r1",
        timestamp=t1,
        event_type=JournalEventType.ORDER_FILLED,
        symbol="BTCUSDT",
        order_ref="o1",
        details={"realized_pnl": -5.0, "strategy_family": "trend"},
    )
    e2 = TradeJournalEntry(
        entry_id="2",
        run_id="r1",
        timestamp=t2,
        event_type=JournalEventType.POSITION_CLOSED,
        symbol="BTCUSDT",
        order_ref="o1",
        details={"realized_pnl": 15.0},
    )

    e3 = TradeJournalEntry(
        entry_id="3",
        run_id="r1",
        timestamp=t1,
        event_type=JournalEventType.ORDER_FILLED,
        symbol="ETHUSDT",
        order_ref="o2",
        details={"realized_pnl": 0.0},
    )

    builder.add_entry(e1)
    builder.add_entry(e2)
    builder.add_entry(e3)

    summaries = builder.generate_lifecycle_summaries("r1")

    assert len(summaries) == 2

    s_btc = [s for s in summaries if s.trade_id == "o1"][0]
    assert s_btc.is_complete is True
    assert s_btc.pnl == -5.0  # We only sum filled pnls in our simple mock

    s_eth = [s for s in summaries if s.trade_id == "o2"][0]
    assert s_eth.is_complete is False
