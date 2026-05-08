from datetime import datetime, timezone
import uuid
from typing import List
from .models import RiskBreachRecord, RiskResponseIntent
from .enums import BreachClass, ResponseClass


class ResponseIntentEngine:
    def generate_intents(
        self, breaches: List[RiskBreachRecord]
    ) -> List[RiskResponseIntent]:
        intents = []
        for breach in breaches:
            response_class = ResponseClass.REVIEW_REQUIRED
            if breach.breach_class == BreachClass.EMERGENCY:
                response_class = ResponseClass.EMERGENCY_DELEVERAGE_INTENT
            elif breach.breach_class == BreachClass.HARD:
                response_class = ResponseClass.NO_NEW_EXPOSURE
            elif breach.breach_class == BreachClass.SOFT:
                response_class = ResponseClass.REDUCE_EXPOSURE

            intent = RiskResponseIntent(
                intent_id=str(uuid.uuid4()),
                response_class=response_class,
                source_breach_refs=[breach.breach_id],
                target_domain=breach.state_ref.domain,
                target_id=breach.state_ref.target_id,
                rationale=f"Generated from {breach.breach_class.value} breach on limit {breach.limit_ref.limit_id}",
                timestamp=datetime.now(timezone.utc),
            )
            intents.append(intent)
        return intents
