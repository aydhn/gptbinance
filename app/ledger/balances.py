from app.ledger.models import AssetBalanceSummary
from app.ledger.enums import BalanceStatus


class BalanceCalculator:
    def __init__(self, entries):
        self.entries = entries

    def get_summary(self, asset: str) -> AssetBalanceSummary:
        balance = 0.0
        for entry in self.entries:
            for p in entry.postings:
                if (
                    p.asset == asset and p.direction == 1
                ):  # Assuming debit increases asset for ASSET accounts
                    balance += p.amount
                elif p.asset == asset and p.direction == -1:
                    balance -= p.amount

        return AssetBalanceSummary(
            asset=asset,
            total_balance=balance,
            available_balance=balance,
            locked_balance=0.0,
            status=BalanceStatus.HEALTHY,
        )
