from app.ledger.models import LedgerEntry, LedgerPosting
from app.ledger.exceptions import PostingImbalanceError, ScopeMismatchError
from typing import List


class LedgerEntryManager:
    @staticmethod
    def validate_and_create(
        entry_id: str,
        postings: List[LedgerPosting],
        entry_type,
        event_ref,
        scope,
        classification,
    ) -> LedgerEntry:
        # Validate scope contamination
        for p in postings:
            if p.account_ref.scope != scope:
                raise ScopeMismatchError(
                    f"Posting scope {p.account_ref.scope} does not match entry scope {scope}"
                )

        # Validate double-entry balance
        balance_map = {}
        for p in postings:
            if p.asset not in balance_map:
                balance_map[p.asset] = 0.0
            balance_map[p.asset] += p.amount * p.direction

        # For single asset entries (like crypto deposits), double entry implies debiting an asset account and crediting an equity/clearing account in the same asset
        for asset, total in balance_map.items():
            if abs(total) > 1e-8:
                raise PostingImbalanceError(
                    f"Imbalance detected for asset {asset}: {total}"
                )

        return LedgerEntry(
            entry_id=entry_id,
            type=entry_type,
            event_ref=event_ref,
            postings=postings,
            scope=scope,
            classification=classification,
        )
