import unittest
from decimal import Decimal
from app.position_plane.pnl import PnLOrchestrator
from app.position_plane.models import RealizedPnLRecord, UnrealizedPnLRecord
import uuid
from datetime import datetime, timezone

class TestPnL(unittest.TestCase):
    def test_pnl_orchestrator(self):
        realized = RealizedPnLRecord(
            record_id=str(uuid.uuid4()), symbol="BTCUSDT", sleeve_id="s1",
            amount=Decimal("100"), currency="USDT", source_lot_id="l1", close_fill_id="f1"
        )
        unrealized = UnrealizedPnLRecord(
            record_id=str(uuid.uuid4()), symbol="BTCUSDT", sleeve_id="s1",
            amount=Decimal("50"), currency="USDT", mark_price=Decimal("50000"),
            mark_source="binance", mark_timestamp=datetime.now(timezone.utc), confidence=1.0
        )

        breakdown = PnLOrchestrator.generate_breakdown("BTCUSDT", [realized], [unrealized], [], [], [])
        self.assertEqual(breakdown.realized_pnl, Decimal("100"))
        self.assertEqual(breakdown.unrealized_pnl, Decimal("50"))
        self.assertEqual(breakdown.total_fees, Decimal("0"))

if __name__ == '__main__':
    unittest.main()
