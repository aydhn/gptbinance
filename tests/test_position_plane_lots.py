import unittest
from decimal import Decimal
from app.position_plane.lots import LotManager
from app.position_plane.enums import Side


class TestPositionLots(unittest.TestCase):
    def test_consume_lot_partial(self):
        fill = {
            "symbol": "BTCUSDT",
            "side": "long",
            "quantity": "2.0",
            "price": "50000",
        }
        lot = LotManager.create_lot_from_fill(fill, "sleeve-1")

        lot, remaining = LotManager.consume_lot(lot, Decimal("1.0"))
        self.assertEqual(remaining, Decimal("0"))
        self.assertEqual(lot.remaining_quantity, Decimal("1.0"))
        self.assertFalse(lot.is_closed)

    def test_consume_lot_full_and_spill(self):
        fill = {
            "symbol": "BTCUSDT",
            "side": "long",
            "quantity": "2.0",
            "price": "50000",
        }
        lot = LotManager.create_lot_from_fill(fill, "sleeve-1")

        lot, remaining = LotManager.consume_lot(lot, Decimal("3.0"))
        self.assertEqual(remaining, Decimal("1.0"))
        self.assertEqual(lot.remaining_quantity, Decimal("0"))
        self.assertTrue(lot.is_closed)


if __name__ == "__main__":
    unittest.main()
