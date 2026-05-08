import unittest
from decimal import Decimal
from app.position_plane.exposures import ExposureCalculator
from app.position_plane.states import PositionStateManager
from app.position_plane.enums import ProductClass

class TestExposures(unittest.TestCase):
    def test_calculate_exposures(self):
        state1 = PositionStateManager.create_empty_state("BTCUSDT", ProductClass.SPOT_PAIR, "sleeve-1")
        PositionStateManager.apply_fill(state1, {"symbol": "BTCUSDT", "side": "long", "quantity": "1.0", "price": "50000"})

        state2 = PositionStateManager.create_empty_state("BTCUSDT", ProductClass.PERPETUAL, "sleeve-2")
        PositionStateManager.apply_fill(state2, {"symbol": "BTCUSDT", "side": "short", "quantity": "0.5", "price": "50000"})

        mark_prices = {"BTCUSDT": Decimal("50000")}
        exposure = ExposureCalculator.calculate_exposures([state1, state2], mark_prices)

        self.assertEqual(exposure.gross_exposure, Decimal("75000"))
        self.assertEqual(exposure.net_directional_exposure, Decimal("25000")) # 50k - 25k
        self.assertEqual(exposure.hedge_adjusted_exposure, Decimal("25000"))
        self.assertEqual(exposure.residual_directional_exposure, Decimal("25000"))

if __name__ == '__main__':
    unittest.main()
