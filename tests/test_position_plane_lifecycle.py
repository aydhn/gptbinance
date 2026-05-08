import unittest
from decimal import Decimal
from app.position_plane.lifecycle import LifecycleManager
from app.position_plane.enums import LifecycleState, Side
from app.position_plane.states import PositionStateManager
from app.position_plane.enums import ProductClass


class TestLifecycle(unittest.TestCase):
    def test_determine_next_state(self):
        state = LifecycleManager.determine_next_state(
            LifecycleState.OPEN, Decimal("1.0"), Decimal("0.5"), Side.LONG, Side.SHORT
        )
        self.assertEqual(state, LifecycleState.SCALING_OUT)

        state = LifecycleManager.determine_next_state(
            LifecycleState.OPEN, Decimal("1.0"), Decimal("1.0"), Side.LONG, Side.SHORT
        )
        self.assertEqual(state, LifecycleState.CLOSED)

        state = LifecycleManager.determine_next_state(
            LifecycleState.OPEN, Decimal("1.0"), Decimal("2.0"), Side.LONG, Side.SHORT
        )
        self.assertEqual(state, LifecycleState.REVERSING)

        state = LifecycleManager.determine_next_state(
            LifecycleState.OPEN, Decimal("1.0"), Decimal("1.0"), Side.LONG, Side.LONG
        )
        self.assertEqual(state, LifecycleState.SCALING_IN)


if __name__ == "__main__":
    unittest.main()
