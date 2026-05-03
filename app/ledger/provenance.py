from app.ledger.models import LedgerEntry
from typing import List


class ProvenanceTracker:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry: LedgerEntry):
        self.entries.append(entry)

    def get_lineage(self, asset: str) -> List[LedgerEntry]:
        return [e for e in self.entries if any(p.asset == asset for p in e.postings)]
