import json
from app.ledger.models import LedgerEntry


class LedgerStorage:
    def __init__(self, filepath: str = "ledger_store.jsonl"):
        self.filepath = filepath

    def write(self, entry: LedgerEntry):
        with open(self.filepath, "a") as f:
            f.write(entry.json() + "\n")
