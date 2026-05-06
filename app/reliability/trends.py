import uuid
from typing import List, Dict
from app.reliability.enums import ReliabilityDomain, TrendClass, ScorecardVerdict
from app.reliability.models import ReliabilityTrendReport, HealthScorecard


class HistoricalReliabilityTrendAnalysis:
    @staticmethod
    def analyze_domain_trend(
        domain: ReliabilityDomain, historical_scorecards: List[HealthScorecard]
    ) -> ReliabilityTrendReport:
        if not historical_scorecards:
            return ReliabilityTrendReport(
                trend_id=f"trend_{uuid.uuid4().hex[:8]}",
                domain=domain,
                trend_class=TrendClass.STABLE,
                caveats=["Not enough historical data."],
            )

        # Simplified trend analysis
        # Assuming scorecards are sorted newest first
        recent = historical_scorecards[:3]
        older = historical_scorecards[3:10]

        recent_degraded = sum(
            1
            for s in recent
            if s.verdict in [ScorecardVerdict.DEGRADED, ScorecardVerdict.BLOCKED]
        )
        older_degraded = sum(
            1
            for s in older
            if s.verdict in [ScorecardVerdict.DEGRADED, ScorecardVerdict.BLOCKED]
        )

        trend = TrendClass.STABLE
        if recent_degraded > older_degraded and recent_degraded > 0:
            trend = TrendClass.DEGRADING
        elif older_degraded > recent_degraded and recent_degraded == 0:
            trend = TrendClass.IMPROVING

        # Mock repeated failure families extraction
        repeated = []
        if trend == TrendClass.DEGRADING:
            repeated.append("repeated_domain_degradation")

        return ReliabilityTrendReport(
            trend_id=f"trend_{uuid.uuid4().hex[:8]}",
            domain=domain,
            trend_class=trend,
            repeated_failure_families=repeated,
        )
