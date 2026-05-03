from app.ledger.models import CostBasisLot
from app.ledger.enums import ScopeType
from datetime import datetime, timezone
import uuid


class CostBasisEngine:
    def __init__(self):
        self.lots = []

    def add_lot(self, asset: str, amount: float, cost: float, scope: ScopeType):
        lot = CostBasisLot(
            lot_id=str(uuid.uuid4()),
            asset=asset,
            acquired_amount=amount,
            remaining_amount=amount,
            cost_basis_total=cost,
            cost_basis_per_unit=cost / amount if amount > 0 else 0,
            acquired_at=datetime.now(timezone.utc),
            scope=scope,
        )
        self.lots.append(lot)
        return lot

    def consume_fifo(self, asset: str, amount: float, scope: ScopeType):
        # Simplistic FIFO
        to_consume = amount
        consumed_cost = 0.0

        relevant_lots = [
            l
            for l in self.lots
            if l.asset == asset and l.scope == scope and l.remaining_amount > 0
        ]
        relevant_lots.sort(key=lambda x: x.acquired_at)

        for lot in relevant_lots:
            if to_consume <= 0:
                break
            take = min(lot.remaining_amount, to_consume)
            lot.remaining_amount -= take
            to_consume -= take
            consumed_cost += take * lot.cost_basis_per_unit
            if lot.remaining_amount == 0:
                lot.status = "CLOSED"

        return consumed_cost
