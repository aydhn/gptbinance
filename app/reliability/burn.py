import uuid
from typing import List, Optional
from datetime import datetime, timezone
from app.reliability.enums import BurnSeverity
from app.reliability.models import BurnRateReport, ErrorBudget
from app.reliability.exceptions import BurnRateError


class BurnRateAnalytics:
    @staticmethod
    def calculate_burn_rate(
        budget: ErrorBudget,
        short_window_consumption: float,
        long_window_consumption: float,
        short_duration_hrs: float,
        long_duration_hrs: float,
    ) -> BurnRateReport:
        if budget.total_budget_value <= 0:
            raise BurnRateError(
                "Budget total value must be > 0 to calculate burn rate."
            )

        short_burn = short_window_consumption / budget.total_budget_value
        long_burn = long_window_consumption / budget.total_budget_value

        # Determine Severity based on generic SRE practices
        # Fast Burn: Burning > 10% of budget in a short window (e.g. 1 hour)
        # Slow Burn: Burning > 5% of budget in a longer window (e.g. 6 hours)

        severity = BurnSeverity.HEALTHY
        caveats = []

        if short_burn > 0.10:
            severity = BurnSeverity.FAST_BURN
        elif long_burn > 0.05:
            severity = BurnSeverity.SLOW_BURN
        elif short_burn > 0.02 or long_burn > 0.02:
            severity = BurnSeverity.NORMAL

        # Projection (linear)
        projected_exhaustion: Optional[float] = None
        if short_burn > 0:
            # hours until exhaustion based on short burn rate
            rate_per_hour = short_burn / max(0.1, short_duration_hrs)
            if rate_per_hour > 0:
                projected_exhaustion = budget.remaining_budget / (
                    rate_per_hour * budget.total_budget_value
                )

        if projected_exhaustion is not None and projected_exhaustion < 4.0:
            caveats.append("Budget projected to exhaust in under 4 hours.")

        return BurnRateReport(
            report_id=f"br_{uuid.uuid4().hex[:8]}",
            budget_id=budget.budget_id,
            short_window_burn_rate=short_burn,
            long_window_burn_rate=long_burn,
            severity=severity,
            projected_exhaustion_hours=projected_exhaustion,
            caveats=caveats,
        )
