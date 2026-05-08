import unittest
from decimal import Decimal
from app.position_plane.lots import LotManager
from app.position_plane.cost_basis import CostBasisCalculator
from app.position_plane.enums import CostBasisClass


class TestCostBasis(unittest.TestCase):
    def test_weighted_average(self):
        lot1 = LotManager.create_lot_from_fill(
            {"symbol": "BTC", "side": "long", "quantity": "1.0", "price": "100"},
            "sleeve-1",
        )
        lot2 = LotManager.create_lot_from_fill(
            {"symbol": "BTC", "side": "long", "quantity": "2.0", "price": "200"},
            "sleeve-1",
        )

        basis = CostBasisCalculator.calculate(
            [lot1, lot2], CostBasisClass.WEIGHTED_AVERAGE
        )
        # (1*100 + 2*200) / 3 = 500 / 3 = 166.666...
        self.assertAlmostEqual(float(basis), 166.6666666, places=5)


if __name__ == "__main__":
    unittest.main()
