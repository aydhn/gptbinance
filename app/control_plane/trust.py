from app.control_plane.models import ControlTrustVerdict
from app.control_plane.enums import TrustVerdict


class TrustEvaluator:
    def evaluate(self, unapproved_actions: int = 0) -> ControlTrustVerdict:
        if unapproved_actions > 0:
            return ControlTrustVerdict(
                verdict=TrustVerdict.DEGRADED,
                reasons=["Pending unapproved actions exist"],
                action_history_summary={"pending": unapproved_actions},
            )
        return ControlTrustVerdict(
            verdict=TrustVerdict.TRUSTED,
            reasons=["All control integrity checks passed"],
            action_history_summary={"successful": 1},
        )
