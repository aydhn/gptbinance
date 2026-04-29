import logging
from typing import Dict, Any, List

from app.backtest.validation.models import RobustnessCheckResult, RobustnessCheckType
from app.backtest.models import BacktestConfig, PerformanceSummary as BacktestSummary
from app.backtest.engine import BacktestEngine

logger = logging.getLogger(__name__)


class RobustnessRunner:
    """Performs sanity checks (not full optimization) to check for fragility."""

    def check_fee_sensitivity(
        self, base_config: BacktestConfig, base_summary: BacktestSummary
    ) -> RobustnessCheckResult:
        """Checks if slightly higher fees kill the strategy."""
        test_config = base_config.copy(deep=True)
        # Increase fee by 50%
        original_fee = getattr(test_config, "fee_rate", 0.001)
        # since config might not have fee rate let's just skip modifying if it fails
        if hasattr(test_config, "fee_rate"):
            test_config.fee_rate = original_fee * 1.5 if original_fee > 0 else 0.001

        engine = BacktestEngine(config=test_config)
        engine.run()
        res_summary = engine.get_summary()

        base_ret = base_summary.total_return_pct
        test_ret = res_summary.total_return_pct

        # Fragile if it goes from positive to negative
        is_fragile = base_ret > 0 and test_ret < 0

        return RobustnessCheckResult(
            check_type=RobustnessCheckType.FEE_PERTURBATION,
            description=f"Increased fee from {original_fee} to {test_config.fee_rate}",
            is_fragile=is_fragile,
            details={
                "base_return": base_ret,
                "perturbed_return": test_ret,
                "drop_pct": (
                    ((base_ret - test_ret) / base_ret * 100) if base_ret != 0 else 0
                ),
            },
        )

    def check_slippage_sensitivity(
        self, base_config: BacktestConfig, base_summary: BacktestSummary
    ) -> RobustnessCheckResult:
        """Checks if slightly higher slippage kills the strategy."""
        test_config = base_config.copy(deep=True)
        original_slip = getattr(test_config, "slippage_rate", 0.001)
        if hasattr(test_config, "slippage_rate"):
            test_config.slippage_rate = (
                original_slip * 2.0 if original_slip > 0 else 0.001
            )

        engine = BacktestEngine(config=test_config)
        engine.run()
        res_summary = engine.get_summary()

        base_ret = base_summary.total_return_pct
        test_ret = res_summary.total_return_pct

        is_fragile = base_ret > 0 and test_ret < 0

        return RobustnessCheckResult(
            check_type=RobustnessCheckType.SLIPPAGE_PERTURBATION,
            description=f"Increased slippage from {original_slip} to {test_config.slippage_rate}",
            is_fragile=is_fragile,
            details={"base_return": base_ret, "perturbed_return": test_ret},
        )

    def run_all(
        self, base_config: BacktestConfig, base_summary: BacktestSummary
    ) -> List[RobustnessCheckResult]:
        return [
            self.check_fee_sensitivity(base_config, base_summary),
            self.check_slippage_sensitivity(base_config, base_summary),
        ]
