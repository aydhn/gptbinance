from app.position_plane.models import PositionState, PositionTrustVerdict
from app.position_plane.enums import TrustVerdict


class TrustEngine:
    @staticmethod
    def evaluate_trust(
        state: PositionState, has_stale_marks: bool, has_missing_fees: bool
    ) -> PositionTrustVerdict:
        verdict = TrustVerdict.TRUSTED
        reasons = []

        if not state.is_authoritative:
            verdict = TrustVerdict.DEGRADED
            reasons.append("State is marked as approximate/non-authoritative.")

        if has_stale_marks:
            verdict = TrustVerdict.CAUTION
            reasons.append("Stale marks detected, unrealized PnL confidence is low.")

        if has_missing_fees:
            if verdict == TrustVerdict.TRUSTED:
                verdict = TrustVerdict.CAUTION
            reasons.append("Missing fee or funding attribution records.")

        return PositionTrustVerdict(
            verdict=verdict,
            symbol=state.symbol,
            reasons=reasons,
            breakdown={
                "stale_marks": has_stale_marks,
                "missing_fees": has_missing_fees,
            },
        )
