from app.ledger.cost_basis import CostBasisEngine
from app.ledger.enums import ScopeType


def test_fifo_cost_basis():
    engine = CostBasisEngine()
    engine.add_lot("BTC", 1.0, 50000.0, ScopeType.PAPER)
    engine.add_lot("BTC", 0.5, 30000.0, ScopeType.PAPER)

    # Sell 1.2 BTC -> uses 1.0 from lot 1, 0.2 from lot 2
    cost = engine.consume_fifo("BTC", 1.2, ScopeType.PAPER)
    # Expected cost: 50000.0 + (0.2 * 60000.0) = 50000.0 + 12000.0 = 62000.0
    assert cost == 62000.0
    assert engine.lots[0].status == "CLOSED"
    import math

    assert math.isclose(engine.lots[1].remaining_amount, 0.3)
