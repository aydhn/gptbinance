import uuid
from datetime import datetime, timezone
from typing import List, Dict
from .models import RiskState, RiskBreachRecord, RiskTrustVerdict
from .enums import TrustVerdict, BreachClass


class TrustedRiskVerdictEngine:
    def evaluate(
        self, states: List[RiskState], breaches: List[RiskBreachRecord]
    ) -> RiskTrustVerdict:
        factors: Dict[str, str] = {}
        breakdown: List[str] = []
        verdict = TrustVerdict.TRUSTED

        # Check authority
        unauthoritative = [s for s in states if not s.authoritative]
        if unauthoritative:
            factors["authority"] = "APPROXIMATE"
            breakdown.append(f"{len(unauthoritative)} states are not authoritative.")
            verdict = TrustVerdict.DEGRADED

        # Check breaches
        emergency = [b for b in breaches if b.breach_class == BreachClass.EMERGENCY]
        if emergency:
            factors["breaches"] = "EMERGENCY"
            breakdown.append(f"{len(emergency)} emergency breaches detected.")
            verdict = TrustVerdict.BLOCKED
        elif [b for b in breaches if b.breach_class == BreachClass.HARD]:
            factors["breaches"] = "HARD"
            breakdown.append("Hard breaches detected.")
            verdict = TrustVerdict.CAUTION

        if verdict == TrustVerdict.TRUSTED:
            factors["status"] = "ALL_CLEAR"
            breakdown.append("Risk posture is clean and authoritative.")

        return RiskTrustVerdict(
            verdict_id=str(uuid.uuid4()),
            verdict=verdict,
            factors=factors,
            breakdown=breakdown,
            timestamp=datetime.now(timezone.utc),
        )
