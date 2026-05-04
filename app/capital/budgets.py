from typing import Any
from typing import Dict, List, Tuple
from app.capital.models import ExposureBudget, LossBudget
from app.capital.enums import LossWindow, BudgetSeverity
from app.capital.exceptions import LossBudgetError
from app.capital.base import BudgetEvaluatorBase


class DefaultBudgetEvaluator(BudgetEvaluatorBase):
    def evaluate_utilization(
        self, budget: ExposureBudget, current_usage: Dict[str, float]
    ) -> Dict[str, Any]:
        results = {"breaches": [], "cautions": [], "ok": True}

        # Check overall capital cap
        deployed = current_usage.get("total_deployed", 0.0)
        if deployed > budget.max_deployable_capital:
            results["breaches"].append(
                f"Deployed capital {deployed} exceeds max cap {budget.max_deployable_capital}"
            )
            results["ok"] = False

        # Check position count
        positions = int(current_usage.get("concurrent_positions", 0))
        if positions > budget.max_concurrent_positions:
            results["breaches"].append(
                f"Concurrent positions {positions} exceeds cap {budget.max_concurrent_positions}"
            )
            results["ok"] = False

        # Check leverage
        leverage = current_usage.get("current_leverage", 1.0)
        if leverage > budget.max_leverage:
            results["breaches"].append(
                f"Leverage {leverage}x exceeds max allowed {budget.max_leverage}x"
            )
            results["ok"] = False

        # Evaluate specific loss budgets
        for lb in budget.loss_budgets:
            key = f"loss_{lb.window.value}"
            current_loss = current_usage.get(key, 0.0)

            if current_loss >= lb.max_loss_amount:
                msg = (
                    f"{lb.window.value} loss {current_loss} >= max {lb.max_loss_amount}"
                )
                if lb.severity == BudgetSeverity.HARD:
                    results["breaches"].append(msg)
                    results["ok"] = False
                else:
                    results["cautions"].append(msg)

            elif current_loss >= lb.max_loss_amount * 0.8:
                # 80% utilization warning
                results["cautions"].append(
                    f"{lb.window.value} loss at {current_loss} nearing max {lb.max_loss_amount}"
                )

        return results


budget_evaluator = DefaultBudgetEvaluator()
