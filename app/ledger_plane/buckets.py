from typing import Dict, Any

from app.ledger_plane.models import BalanceBucket
from app.ledger_plane.enums import BalanceClass


class BalanceBucketBuilder:
    @staticmethod
    def build(
        bucket_class: BalanceClass,
        amount: float,
        asset: str,
        metadata: Dict[str, Any] = None,
    ) -> BalanceBucket:
        return BalanceBucket(
            bucket_class=bucket_class,
            amount=amount,
            asset=asset,
            metadata=metadata or {},
        )
