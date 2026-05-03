from app.stressrisk.models import TailLossBudget, StressBudgetResult
from app.stressrisk.enums import BudgetVerdict


class BudgetManager:
    def get_budget(self, profile: str) -> TailLossBudget:
        if profile == "canary_live_caution":
            return TailLossBudget(
                profile=profile,
                max_daily_stress_loss=500.0,
                max_scenario_loss=200.0,
                max_concentration_loss=100.0,
            )
        elif profile == "live":
            return TailLossBudget(
                profile=profile,
                max_daily_stress_loss=2000.0,
                max_scenario_loss=1000.0,
                max_concentration_loss=500.0,
            )
        else:  # paper/testnet
            return TailLossBudget(
                profile=profile,
                max_daily_stress_loss=10000.0,
                max_scenario_loss=5000.0,
                max_concentration_loss=2500.0,
            )

    def evaluate(
        self, profile: str, estimated_scenario_loss: float
    ) -> StressBudgetResult:
        budget = self.get_budget(profile)
        verdict = BudgetVerdict.PASS
        reasons = []
        pct = (
            (estimated_scenario_loss / budget.max_scenario_loss) * 100.0
            if budget.max_scenario_loss > 0
            else 0
        )
        if estimated_scenario_loss > budget.max_scenario_loss:
            verdict = BudgetVerdict.BREACH
            reasons.append(
                f"Scenario loss {estimated_scenario_loss} exceeds budget {budget.max_scenario_loss}"
            )
        elif estimated_scenario_loss > budget.max_scenario_loss * 0.8:
            verdict = BudgetVerdict.CAUTION
            reasons.append("Approaching scenario loss budget")

        return StressBudgetResult(
            profile=profile,
            verdict=verdict,
            utilized_daily_budget_pct=0.0,
            utilized_scenario_budget_pct=pct,
            reasons=reasons,
        )
