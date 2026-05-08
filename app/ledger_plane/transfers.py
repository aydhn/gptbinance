from datetime import datetime, timezone
import uuid
from typing import List, Dict, Any

from app.ledger_plane.models import TransferRecord, TransferChain
from app.ledger_plane.enums import TransferClass

class TransferManager:
    @staticmethod
    def build_record(transfer_class: TransferClass, asset: str, amount: float, source_scope: str, target_scope: str, status: str, metadata: Dict[str, Any] = None) -> TransferRecord:
        return TransferRecord(
            id=str(uuid.uuid4()),
            transfer_class=transfer_class,
            asset=asset,
            amount=amount,
            source_scope=source_scope,
            target_scope=target_scope,
            status=status,
            timestamp=datetime.now(timezone.utc),
            metadata=metadata or {}
        )

    @staticmethod
    def build_chain(records: List[TransferRecord]) -> TransferChain:
        return TransferChain(
            chain_id=str(uuid.uuid4()),
            records=records
        )
