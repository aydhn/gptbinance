from datetime import datetime, timezone
from typing import Optional
from app.capital.models import CapitalTierRef
from app.capital.storage import capital_storage


class CapitalRepository:
    def __init__(self):
        # In a real system, this would load from a database or storage.
        # We start with paper_zero by default for safety.
        self._current_tier = CapitalTierRef(
            tier_id="paper_zero", assigned_at=datetime.now(timezone.utc)
        )

    def get_current_tier(self) -> CapitalTierRef:
        return self._current_tier

    def set_current_tier(self, tier_id: str):
        from app.capital.tiers import get_tier

        # validate tier exists
        get_tier(tier_id)

        self._current_tier = CapitalTierRef(
            tier_id=tier_id, assigned_at=datetime.now(timezone.utc)
        )
        capital_storage.record_tier_change(self._current_tier)


capital_repository = CapitalRepository()
