from app.market_truth.models import FreshnessReport
from app.market_truth.enums import FreshnessClass, TruthDomain
from app.market_truth.budgets import BudgetRegistry


class FreshnessEvaluator:
    def evaluate(
        self,
        symbol: str,
        domain: TruthDomain,
        profile_name: str,
        lag_ms: float,
        silence_ms: float,
    ) -> FreshnessReport:
        budget = BudgetRegistry.get_budget(profile_name)

        freshness_class = FreshnessClass.HEALTHY
        if lag_ms > budget.max_lag_ms or silence_ms > budget.max_silence_ms:
            # Over budget
            if profile_name in ["canary_live_caution", "derivatives_testnet"]:
                freshness_class = FreshnessClass.STALE  # Critical block
            else:
                freshness_class = FreshnessClass.DEGRADED

        return FreshnessReport(
            symbol=symbol,
            domain=domain,
            freshness_class=freshness_class,
            lag_ms=lag_ms,
            silence_ms=silence_ms,
        )
