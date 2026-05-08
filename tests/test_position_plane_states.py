import unittest
from decimal import Decimal
from app.position_plane.enums import ProductClass, Side, LifecycleState
from app.position_plane.states import PositionStateManager


class TestPositionStates(unittest.TestCase):
    def test_apply_fill_open_long(self):
        state = PositionStateManager.create_empty_state(
            "BTCUSDT", ProductClass.SPOT_PAIR, "sleeve-1"
        )
        fill = {
            "symbol": "BTCUSDT",
            "side": "long",
            "quantity": "1.0",
            "price": "50000",
        }
        PositionStateManager.apply_fill(state, fill)

        self.assertEqual(state.quantity, Decimal("1.0"))
        self.assertEqual(state.side, Side.LONG)
        self.assertEqual(state.lifecycle_state, LifecycleState.OPEN)
        self.assertEqual(len(state.open_lots), 1)

    def test_apply_fill_reverse(self):
        state = PositionStateManager.create_empty_state(
            "BTCUSDT", ProductClass.SPOT_PAIR, "sleeve-1"
        )
        fill1 = {
            "symbol": "BTCUSDT",
            "side": "long",
            "quantity": "1.0",
            "price": "50000",
        }
        PositionStateManager.apply_fill(state, fill1)

        fill2 = {
            "symbol": "BTCUSDT",
            "side": "short",
            "quantity": "1.5",
            "price": "51000",
        }
        PositionStateManager.apply_fill(state, fill2)

        self.assertEqual(state.quantity, Decimal("0.5"))
        self.assertEqual(state.side, Side.SHORT)
        self.assertEqual(state.lifecycle_state, LifecycleState.OPEN)
        self.assertEqual(len(state.open_lots), 1)
        self.assertEqual(state.open_lots[0].side, Side.SHORT)


if __name__ == "__main__":
    unittest.main()
