from app.market_truth.models import FreshnessBudget


class BudgetRegistry:
    BUDGETS = {
        "paper_default": FreshnessBudget(
            profile_name="paper_default", max_lag_ms=5000.0, max_silence_ms=15000.0
        ),
        "shadow_research": FreshnessBudget(
            profile_name="shadow_research", max_lag_ms=3000.0, max_silence_ms=10000.0
        ),
        "testnet_exec": FreshnessBudget(
            profile_name="testnet_exec", max_lag_ms=1000.0, max_silence_ms=5000.0
        ),
        "canary_live_caution": FreshnessBudget(
            profile_name="canary_live_caution", max_lag_ms=500.0, max_silence_ms=2000.0
        ),
        "derivatives_testnet": FreshnessBudget(
            profile_name="derivatives_testnet", max_lag_ms=800.0, max_silence_ms=3000.0
        ),
    }

    @classmethod
    def get_budget(cls, profile_name: str) -> FreshnessBudget:
        return cls.BUDGETS.get(profile_name, cls.BUDGETS["paper_default"])
