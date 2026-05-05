import uuid
from datetime import datetime, timezone
from app.universe.models import UniverseDiff, UniverseImpactReport
from app.workspaces.enums import ProfileType


class ImpactAnalyzer:
    def analyze(self, diff: UniverseDiff) -> UniverseImpactReport:
        # Dummy analysis logic, would integrate with strategies/profiles in reality
        impacted_strats = []
        severity = "low"
        recommendations = []

        if diff.removed or diff.eligibility_changed:
            impacted_strats.append("all_active_strategies")
            severity = "medium"
            if len(diff.removed) > 10:
                severity = "high"
            recommendations.append(
                "Review portfolio allocation for removed/blocked symbols"
            )
            recommendations.append("Check open orders for ineligible symbols")

        return UniverseImpactReport(
            report_id=f"impact_{uuid.uuid4().hex[:8]}",
            diff_id=diff.diff_id,
            impacted_strategies=impacted_strats,
            impacted_profiles=[ProfileType.CANARY_LIVE_CAUTION],  # Assuming for now
            severity=severity,
            recommendations=recommendations,
            created_at=datetime.now(timezone.utc),
        )
