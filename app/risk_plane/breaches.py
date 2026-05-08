from datetime import datetime, timezone
import uuid
from typing import Optional
from .models import (
    RiskState,
    RiskLimitDefinition,
    RiskBreachRecord,
    RiskLimitRef,
    RiskStateRef,
)
from .enums import BreachClass, LimitClass


class CanonicalBreachClassifier:
    def classify(
        self, state: RiskState, limit: RiskLimitDefinition, current_value: float
    ) -> Optional[RiskBreachRecord]:
        if current_value <= limit.value:
            return None  # No breach

        ratio = current_value / limit.value

        breach_class = BreachClass.ADVISORY
        if limit.limit_class == LimitClass.HARD or ratio > 1.5:
            breach_class = BreachClass.HARD
        elif limit.limit_class == LimitClass.EMERGENCY or ratio > 2.0:
            breach_class = BreachClass.EMERGENCY
        elif limit.limit_class == LimitClass.SOFT or ratio > 1.1:
            breach_class = BreachClass.SOFT

        blast_radius = "LOCAL" if state.domain in ["SYMBOL", "SLEEVE"] else "GLOBAL"

        return RiskBreachRecord(
            breach_id=str(uuid.uuid4()),
            limit_ref=RiskLimitRef(
                limit_id=limit.limit_id,
                limit_class=limit.limit_class,
                owner_domain=limit.owner_domain,
            ),
            state_ref=RiskStateRef(
                state_id=state.state_id, domain=state.domain, target_id=state.target_id
            ),
            breach_class=breach_class,
            breached_value=current_value,
            timestamp=datetime.now(timezone.utc),
            repeated_family=False,  # Needs history check in real impl
            blast_radius=blast_radius,
            proof_notes=[
                f"Value {current_value} exceeded limit {limit.value} ({breach_class.value})"
            ],
        )
