from app.ledger.models import LedgerPosting, LedgerAccountRef


class PostingBuilder:
    @staticmethod
    def create_pair(
        amount: float,
        asset: str,
        debit_ref: LedgerAccountRef,
        credit_ref: LedgerAccountRef,
    ):
        return [
            LedgerPosting(
                account_ref=debit_ref, amount=amount, asset=asset, direction=1
            ),
            LedgerPosting(
                account_ref=credit_ref, amount=amount, asset=asset, direction=-1
            ),
        ]
