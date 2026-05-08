from datetime import datetime, timezone
import uuid
from typing import List, Dict, Any

from app.ledger_plane.models import BalanceState, BalanceBucket
from app.ledger_plane.enums import BalanceClass


class BalanceStateBuilder:
    @staticmethod
    def build(
        account_scope: str,
        asset: str,
        buckets: List[BalanceBucket],
        authoritative: bool = False,
        metadata: Dict[str, Any] = None,
    ) -> BalanceState:
        return BalanceState(
            id=str(uuid.uuid4()),
            account_scope=account_scope,
            asset=asset,
            buckets=buckets,
            timestamp=datetime.now(timezone.utc),
            authoritative=authoritative,
            metadata=metadata or {},
        )
