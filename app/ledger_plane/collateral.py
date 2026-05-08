from datetime import datetime, timezone
import uuid
from typing import Dict, Any

from app.ledger_plane.models import CollateralState
from app.ledger_plane.enums import CollateralClass

class CollateralTruthBuilder:
    @staticmethod
    def build(account_scope: str, asset: str, collateral_class: CollateralClass, amount: float, metadata: Dict[str, Any] = None) -> CollateralState:
        return CollateralState(
            id=str(uuid.uuid4()),
            account_scope=account_scope,
            asset=asset,
            collateral_class=collateral_class,
            amount=amount,
            timestamp=datetime.now(timezone.utc),
            metadata=metadata or {}
        )
