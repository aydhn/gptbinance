import hashlib
import json
import os
from typing import List
from app.security.models import EvidenceChainEntry
from app.security.enums import EvidenceStatus

class EvidenceChain:
    def __init__(self, storage_path: str = "data/security/evidence.jsonl"):
        self.storage_path = storage_path
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)

    def append_event(self, event_type: str, payload: dict) -> EvidenceChainEntry:
        payload_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        prev_entry = self.get_last_entry()
        prev_hash = prev_entry.payload_hash if prev_entry else "GENESIS"
        seq_num = (prev_entry.seq_num + 1) if prev_entry else 1

        entry = EvidenceChainEntry(
            seq_num=seq_num,
            event_type=event_type,
            payload_hash=payload_hash,
            previous_hash=prev_hash
        )

        with open(self.storage_path, "a") as f:
            f.write(entry.model_dump_json() + "\n")

        return entry

    def get_last_entry(self) -> EvidenceChainEntry:
        if not os.path.exists(self.storage_path):
            return None
        with open(self.storage_path, "r") as f:
            lines = f.readlines()
            if not lines:
                return None
            return EvidenceChainEntry.model_validate_json(lines[-1])

    def verify_chain(self) -> EvidenceStatus:
        if not os.path.exists(self.storage_path):
            return EvidenceStatus.VALID

        with open(self.storage_path, "r") as f:
            lines = f.readlines()

        prev_hash = "GENESIS"
        for idx, line in enumerate(lines):
            entry = EvidenceChainEntry.model_validate_json(line)
            if entry.previous_hash != prev_hash:
                return EvidenceStatus.TAMPER_SUSPECTED
            prev_hash = entry.payload_hash

        return EvidenceStatus.VALID
