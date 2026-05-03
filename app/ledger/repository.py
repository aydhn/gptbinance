from app.ledger.models import LedgerEntry
from app.ledger.storage import LedgerStorage


class LedgerRepository:
    def __init__(self, storage: LedgerStorage):
        self.storage = storage
        self.in_memory_entries = []

    def append(self, entry: LedgerEntry):
        self.in_memory_entries.append(entry)
        self.storage.write(entry)
