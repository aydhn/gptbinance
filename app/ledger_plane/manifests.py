from datetime import datetime, timezone
import uuid
import hashlib
import json
from typing import List, Dict, Any

from app.ledger_plane.models import LedgerManifest, LedgerManifestEntry

class LedgerManifestBuilder:
    @staticmethod
    def build(entries: List[LedgerManifestEntry]) -> LedgerManifest:
        entry_dicts = [e.model_dump() for e in entries]
        hash_value = hashlib.sha256(json.dumps(entry_dicts, sort_keys=True).encode()).hexdigest()
        return LedgerManifest(
            manifest_id=str(uuid.uuid4()),
            entries=entries,
            timestamp=datetime.now(timezone.utc),
            hash_value=hash_value
        )
